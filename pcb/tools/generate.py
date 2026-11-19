#!/usr/bin/env python3
"""Generate the three ARTT KiCad projects: schematic, board and project file.

Run from the pcb/ folder:

    python3 tools/generate.py

Needs KiCad 7 or later with its Python module (pcbnew) and the standard
symbol and footprint libraries. The script made the first version of the
boards. Once a board is edited by hand in KiCad, the KiCad files are the
source and this script must not be run over them again.
"""
import json
import os
import re
import sys
import uuid

import pcbnew

HERE = os.path.dirname(os.path.abspath(__file__))
PCB = os.path.dirname(HERE)
SYM_DIR = os.environ.get("KICAD_SYMBOL_DIR", "/usr/share/kicad/symbols")
FP_DIR = os.environ.get("KICAD_FOOTPRINT_DIR", "/usr/share/kicad/footprints")
ARTT_LIB = os.path.join(PCB, "lib", "artt.pretty")
DATE = "2026-11-19"
REV = "C"
NS = uuid.UUID("6f0f3b52-1c55-4a5e-9d0e-a7770b0a0001")


def uid(*key):
    return str(uuid.uuid5(NS, "/".join(str(k) for k in key)))


# --------------------------------------------------------------------------
# Schematic writer
# --------------------------------------------------------------------------

def lib_symbol(lib, name):
    """Return (text of the library symbol renamed Lib:Name, {pin: (x, y, angle)})."""
    text = open(os.path.join(SYM_DIR, lib + ".kicad_sym")).read()
    start = text.index('(symbol "%s"' % name)
    depth, i, in_str = 0, start, False
    while True:
        c = text[i]
        if in_str:
            if c == "\\":
                i += 1
            elif c == '"':
                in_str = False
        elif c == '"':
            in_str = True
        elif c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
            if depth == 0:
                break
        i += 1
    chunk = text[start:i + 1]
    if "(extends" in chunk:
        raise SystemExit("symbol %s:%s extends another symbol" % (lib, name))
    pins = {}
    for m in re.finditer(r'\(pin \w+ \w+ \(at ([-\d.]+) ([-\d.]+) (\d+)\).*?\(number "([^"]+)"', chunk, re.S):
        pins[m.group(4)] = (float(m.group(1)), float(m.group(2)), int(m.group(3)))
    chunk = chunk.replace('(symbol "%s"' % name, '(symbol "%s:%s"' % (lib, name), 1)
    return chunk, pins


class Schematic:
    def __init__(self, project, title, comments):
        self.project = project
        self.title = title
        self.comments = comments
        self.root = uid(project, "root")
        self.libs = {}
        self.items = []
        self.symbols = {}   # ref -> uuid
        self.nets = {}      # net -> [(ref, pin)]

    def _lib(self, lib_id):
        if lib_id not in self.libs:
            lib, name = lib_id.split(":")
            self.libs[lib_id] = lib_symbol(lib, name)
        return self.libs[lib_id]

    @staticmethod
    def _tf(dx, dy, rot, mirror):
        """Screen offset of a point after the symbol's mirror and rotation."""
        if mirror:
            dx = -dx
        for _ in range(rot // 90):
            dx, dy = dy, -dx
        return dx, dy

    def symbol(self, lib_id, ref, value, footprint, x, y, nets=None, ref_at=None, val_at=None, rot=0, mirror=False):
        _, pins = self._lib(lib_id)
        su = uid(self.project, "sym", ref)
        self.symbols[ref] = su
        ref_at = ref_at or (x, y - 7.62)
        val_at = val_at or (x, y + 10.16)
        fa = 90 if rot in (90, 270) else 0   # keeps the field text horizontal on a turned symbol
        out = []
        out.append('  (symbol (lib_id "%s") (at %s %s %d)%s (unit 1)' % (lib_id, x, y, rot, " (mirror y)" if mirror else ""))
        out.append('    (in_bom yes) (on_board yes) (dnp no)')
        out.append('    (uuid %s)' % su)
        out.append('    (property "Reference" "%s" (at %s %s %d) (effects (font (size 1.27 1.27)) (justify left)))' % (ref, ref_at[0], ref_at[1], fa))
        out.append('    (property "Value" "%s" (at %s %s %d) (effects (font (size 1.27 1.27)) (justify left)))' % (value, val_at[0], val_at[1], fa))
        out.append('    (property "Footprint" "%s" (at %s %s 0) (effects (font (size 1.27 1.27)) hide))' % (footprint, x, y))
        out.append('    (property "Datasheet" "~" (at %s %s 0) (effects (font (size 1.27 1.27)) hide))' % (x, y))
        for num in pins:
            out.append('    (pin "%s" (uuid %s))' % (num, uid(self.project, "pin", ref, num)))
        out.append('    (instances (project "%s" (path "/%s" (reference "%s") (unit 1))))' % (self.project, self.root, ref))
        out.append('  )')
        self.items.append("\n".join(out))
        self.pinpos = getattr(self, "pinpos", {})
        for num, (px, py, ang) in pins.items():
            ox, oy = self._tf(px, -py, rot, mirror)
            ex, ey = round(x + ox, 4), round(y + oy, 4)
            d0 = {0: (-1, 0), 180: (1, 0), 90: (0, 1), 270: (0, -1)}[ang]
            dx, dy = self._tf(d0[0], d0[1], rot, mirror)
            self.pinpos[(ref, num)] = (ex, ey, dx, dy)
        for num, net in (nets or {}).items():
            ex, ey, dx, dy = self.pinpos[(ref, num)]
            stub = 5.08
            lx, ly = round(ex + dx * stub, 4), round(ey + dy * stub, 4)
            self.wire([(ex, ey), (lx, ly)])
            self.label(net, lx, ly, {(-1, 0): 180, (1, 0): 0, (0, 1): 270, (0, -1): 90}[(dx, dy)])
        return su

    def pin(self, ref, num):
        return self.pinpos[(ref, num)][:2]

    def wire(self, pts):
        self.segs = getattr(self, "segs", [])
        for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
            if x1 != x2 and y1 != y2:
                raise SystemExit("schematic wire is not horizontal or vertical: %s %s" % ((x1, y1), (x2, y2)))
            self.segs.append(((x1, y1), (x2, y2)))

    def junction(self, x, y):
        self.juncs = getattr(self, "juncs", [])
        self.juncs.append((x, y))

    def _wires_out(self):
        """Wires are cut at every junction, so that wire ends meet exactly there."""
        out = []
        for (x1, y1), (x2, y2) in getattr(self, "segs", []):
            cuts = [(x1, y1), (x2, y2)]
            for jx, jy in getattr(self, "juncs", []):
                if x1 == x2 == jx and min(y1, y2) < jy < max(y1, y2):
                    cuts.append((jx, jy))
                if y1 == y2 == jy and min(x1, x2) < jx < max(x1, x2):
                    cuts.append((jx, jy))
            cuts.sort()
            for (ax, ay), (bx, by) in zip(cuts, cuts[1:]):
                out.append('  (wire (pts (xy %s %s) (xy %s %s)) (stroke (width 0) (type default)) (uuid %s))'
                           % (ax, ay, bx, by, uid(self.project, "wire", ax, ay, bx, by)))
        for jx, jy in getattr(self, "juncs", []):
            out.append('  (junction (at %s %s) (diameter 0) (color 0 0 0 0) (uuid %s))' % (jx, jy, uid(self.project, "junction", jx, jy)))
        return out

    def label(self, net, x, y, ang=0):
        just = {0: "left bottom", 90: "left bottom", 180: "right bottom", 270: "right bottom"}[ang]
        self.items.append('  (label "%s" (at %s %s %s) (effects (font (size 1.27 1.27)) (justify %s)) (uuid %s))'
                          % (net, x, y, ang, just, uid(self.project, "label", net, x, y)))

    def text(self, s, x, y, size=1.6):
        s = s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
        self.items.append('  (text "%s" (at %s %s 0) (effects (font (size %s %s)) (justify left bottom)) (uuid %s))'
                          % (s, x, y, size, size, uid(self.project, "text", x, y)))

    def write(self, path):
        out = ['(kicad_sch (version 20230121) (generator eeschema)', '', '  (uuid %s)' % self.root, '', '  (paper "A4")', '']
        out.append('  (title_block')
        out.append('    (title "%s")' % self.title)
        out.append('    (date "%s")' % DATE)
        out.append('    (rev "%s")' % REV)
        out.append('    (company "ARTT, the open reference for Acoustic Research turntables")')
        for i, c in enumerate(self.comments, 1):
            out.append('    (comment %d "%s")' % (i, c))
        out.append('  )')
        out.append('')
        out.append('  (lib_symbols')
        for chunk, _ in self.libs.values():
            out.append("    " + chunk.replace("\n", "\n  "))
        out.append('  )')
        out.append('')
        out.extend(self.items)
        out.extend(self._wires_out())
        out.append('')
        out.append('  (sheet_instances (path "/" (page "1")))')
        out.append(')')
        open(path, "w").write("\n".join(out) + "\n")


# --------------------------------------------------------------------------
# Board writer
# --------------------------------------------------------------------------

OX, OY = 90.0, 60.0   # where the board's top left corner sits on the page


def V(x, y):
    return pcbnew.VECTOR2I(pcbnew.FromMM(OX + x), pcbnew.FromMM(OY + y))


class Board:
    def __init__(self, project, title, w, h, comments):
        self.project = project
        self.b = pcbnew.BOARD()
        tb = self.b.GetTitleBlock()
        tb.SetTitle(title)
        tb.SetDate(DATE)
        tb.SetRevision(REV)
        tb.SetCompany("ARTT, the open reference for Acoustic Research turntables")
        for i, c in enumerate(comments):
            tb.SetComment(i, c)
        self.netmap = {}
        self.w, self.h = w, h
        s = pcbnew.PCB_SHAPE(self.b)
        s.SetShape(pcbnew.SHAPE_T_RECT)
        s.SetStart(V(0, 0))
        s.SetEnd(V(w, h))
        s.SetLayer(pcbnew.Edge_Cuts)
        s.SetWidth(pcbnew.FromMM(0.1))
        self.b.Add(s)

    def net(self, name):
        if name not in self.netmap:
            ni = pcbnew.NETINFO_ITEM(self.b, "/" + name)
            self.b.Add(ni)
            self.netmap[name] = ni
        return self.netmap[name]

    def place(self, lib, name, ref, value, x, y, rot=0, nets=None, sym_uuid=None, ref_at=None, ref_size=1.0, hide_value=False):
        libdir = ARTT_LIB if lib == "artt" else os.path.join(FP_DIR, lib + ".pretty")
        fp = pcbnew.FootprintLoad(libdir, name)
        if fp is None:
            raise SystemExit("footprint not found: %s:%s" % (lib, name))
        fp.SetFPID(pcbnew.LIB_ID(lib, name))
        fp.SetReference(ref)
        fp.SetValue(value)
        fp.SetPosition(V(x, y))
        if rot:
            fp.SetOrientationDegrees(rot)
        if sym_uuid:
            fp.SetPath(pcbnew.KIID_PATH("/" + sym_uuid))
        if hide_value:
            fp.Value().SetVisible(False)
        r = fp.Reference()
        if ref_at is None:
            r.SetVisible(False)
        else:
            r.SetVisible(True)
            r.SetPosition(V(*ref_at))
            r.SetTextAngleDegrees(0)
            r.SetTextSize(pcbnew.VECTOR2I(pcbnew.FromMM(ref_size), pcbnew.FromMM(ref_size)))
            r.SetTextThickness(pcbnew.FromMM(0.15))
            r.SetLayer(pcbnew.F_SilkS)
        for pad in fp.Pads():
            n = pad.GetNumber()
            if nets and n in nets:
                pad.SetNet(self.net(nets[n]))
        self.b.Add(fp)
        return fp

    def track(self, net, pts, width, layer=None):
        layer = pcbnew.B_Cu if layer is None else layer
        for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
            t = pcbnew.PCB_TRACK(self.b)
            t.SetStart(V(x1, y1))
            t.SetEnd(V(x2, y2))
            t.SetWidth(pcbnew.FromMM(width))
            t.SetLayer(layer)
            t.SetNet(self.net(net))
            self.b.Add(t)

    def text(self, s, x, y, size=1.0, layer=None, thick=None, mirror=False):
        layer = pcbnew.F_SilkS if layer is None else layer
        t = pcbnew.PCB_TEXT(self.b)
        t.SetText(s)
        t.SetPosition(V(x, y))
        t.SetLayer(layer)
        t.SetTextSize(pcbnew.VECTOR2I(pcbnew.FromMM(size), pcbnew.FromMM(size)))
        t.SetTextThickness(pcbnew.FromMM(thick if thick else max(0.12, size * 0.15)))
        t.SetHorizJustify(pcbnew.GR_TEXT_H_ALIGN_CENTER)
        t.SetVertJustify(pcbnew.GR_TEXT_V_ALIGN_CENTER)
        if mirror:
            t.SetMirrored(True)
        self.b.Add(t)

    def rect(self, x1, y1, x2, y2, layer, width=0.1):
        s = pcbnew.PCB_SHAPE(self.b)
        s.SetShape(pcbnew.SHAPE_T_RECT)
        s.SetStart(V(x1, y1))
        s.SetEnd(V(x2, y2))
        s.SetLayer(layer)
        s.SetWidth(pcbnew.FromMM(width))
        self.b.Add(s)

    def save(self, path):
        pcbnew.SaveBoard(path, self.b)


def project_file(path, name, classes, patterns):
    default = {"bus_width": 12, "clearance": 0.2, "diff_pair_gap": 0.25, "diff_pair_via_gap": 0.25,
               "diff_pair_width": 0.2, "line_style": 0, "microvia_diameter": 0.3, "microvia_drill": 0.1,
               "name": "Default", "pcb_color": "rgba(0, 0, 0, 0.000)", "schematic_color": "rgba(0, 0, 0, 0.000)",
               "track_width": 0.6, "via_diameter": 0.8, "via_drill": 0.4, "wire_width": 6}
    cls = [default]
    for c in classes:
        d = dict(default)
        d.update(c)
        cls.append(d)
    pro = {
        "board": {"design_settings": {
            "defaults": {},
            "diff_pair_dimensions": [],
            "drc_exclusions": [],
            "rules": {"min_clearance": 0.2, "min_copper_edge_clearance": 0.5, "min_hole_clearance": 0.25,
                      "min_hole_to_hole": 0.5, "min_through_hole_diameter": 0.3, "min_track_width": 0.2,
                      "min_via_annular_width": 0.1, "min_via_diameter": 0.5, "min_silk_clearance": 0.0,
                      "min_text_height": 0.7, "min_text_thickness": 0.1, "solder_mask_to_copper_clearance": 0.0},
            "track_widths": [0.0, 0.6, 1.0, 1.5, 2.5],
            "via_dimensions": []}},
        "boards": [],
        "libraries": {"pinned_footprint_libs": [], "pinned_symbol_libs": []},
        "meta": {"filename": name + ".kicad_pro", "version": 1},
        "net_settings": {"classes": cls, "meta": {"version": 3}, "net_colors": None,
                         "netclass_assignments": None, "netclass_patterns": patterns},
        "pcbnew": {"page_layout_descr_file": ""},
        "sheets": [[uid(name, "root"), ""]],
        "text_variables": {},
    }
    json.dump(pro, open(path, "w"), indent=2)
    open(os.path.join(os.path.dirname(path), "fp-lib-table"), "w").write(
        '(fp_lib_table\n  (lib (name "artt")(type "KiCad")(uri "${KIPRJMOD}/../lib/artt.pretty")(options "")(descr "ARTT project footprints"))\n)\n')


F = pcbnew.F_Cu
TB3 = ("TerminalBlock_MetzConnect", "TerminalBlock_MetzConnect_Type171_RT13703HBWC_1x03_P7.50mm_Horizontal")
TB2 = ("TerminalBlock_MetzConnect", "TerminalBlock_MetzConnect_Type171_RT13702HBWC_1x02_P7.50mm_Horizontal")
TB4 = ("TerminalBlock_MetzConnect", "TerminalBlock_MetzConnect_Type171_RT13704HBWC_1x04_P7.50mm_Horizontal")
TBS = ("TerminalBlock_Phoenix", "TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal")
FUSE = ("Fuse", "Fuseholder_Cylinder-5x20mm_Schurter_FAB_0031-355x_Horizontal_Closed")
HOLE = ("MountingHole", "MountingHole_3.2mm_M3")
WIRE = ("Connector_Wire", "SolderWire-0.1sqmm_1x01_D0.4mm_OD1mm_Relief")
CLOAD = ("Capacitor_THT", "C_Rect_L7.2mm_W2.5mm_P5.00mm_FKS2_FKP2_MKS2_MKP2")


def fpid(t):
    return "%s:%s" % t


# --------------------------------------------------------------------------
# Board 1: power
# --------------------------------------------------------------------------

def power_board():
    name = "artt-power-board"
    d = os.path.join(PCB, "power-board")
    title = "ARTT power board"
    comments = ["Fuse, switch capacitor, motor capacitor and voltage links for the AR XA motor circuit",
                "Circuit: XA service manual, page 3. XB and AR77XB: confirm on the table",
                "Status: PRELIMINARY. Mains voltage. Not safety certified"]
    WS = ("artt", "Hole_NPTH_3.5mm_Wood_Screw")
    parts = [
        # ref, symbol, value, footprint, nets
        ("J1", "Connector:Screw_Terminal_01x03", "MAINS IN", TB3, {"1": "L_IN", "2": "N", "3": "PE"}),
        ("F1", "Device:Fuse", "5x20 mm, value from motor label", FUSE, {"1": "L_IN", "2": "L_FUSED"}),
        ("J2", "Connector:Screw_Terminal_01x02", "SWITCH", TB2, {"1": "L_SW", "2": "L_FUSED"}),
        ("C2", "Device:C", "0.022uF (120 V) or 0.01uF (220 V)", ("artt", "C_Film_MultiPitch_P10_P15"), {"1": "L_FUSED", "2": "L_SW"}),
        ("C1", "Device:C", "0.1uF (120 V) or 0.39uF (220 V)", ("artt", "C_Film_MultiPitch_P15_P22.5_P27.5"), {"1": "L_SW", "2": "M_RED"}),
        ("JP1", "Jumper:Jumper_3_Open", "1-2: 120 V. 2-3: 220 V", ("artt", "WireLink_3Way_120V_Left_220V_Up"), {"1": "N", "2": "M_WHT1", "3": "L_SW"}),
        ("JP2", "Jumper:Jumper_3_Open", "1-2: 120 V. 2-3: 220 V", ("artt", "WireLink_3Way_120V_Left_220V_Up"), {"1": "L_SW", "2": "M_WHT2", "3": "M_RED"}),
        ("J3", "Connector:Screw_Terminal_01x04", "MOTOR", TB4, {"1": "N", "2": "M_WHT2", "3": "M_RED", "4": "M_WHT1"}),
        ("J4", "Connector:Screw_Terminal_01x02", "TOP PLATE EARTH", TB2, {"1": "PE", "2": "PE"}),
    ]
    sch = Schematic(name, title, comments)
    P = {p[0]: p for p in parts}

    def sym(ref, x, y, nets=None, rot=0, mirror=False, ref_at=None, val_at=None):
        _, lib_id, val, fp = P[ref][:4]
        sch.symbol(lib_id, ref, val, fpid(fp), x, y, nets, ref_at, val_at, rot, mirror)

    Y = 68.58                      # the line runs left to right along this row
    sym("J1", 45.72, 71.12, mirror=True, ref_at=(40.64, 63.5), val_at=(35.56, 81.28))
    sym("F1", 76.2, Y, rot=90, ref_at=(77.47, 63.5), val_at=(100.33, 76.2))
    sym("J2", 106.68, 88.9, rot=270, ref_at=(111.76, 87.63), val_at=(111.76, 90.17))
    sym("C2", 114.3, Y, rot=90, ref_at=(115.57, 62.23), val_at=(133.35, 58.42))
    sym("C1", 198.12, 43.18, rot=90, ref_at=(199.39, 36.83), val_at=(215.9, 33.02))
    sym("JP1", 165.1, 86.36, {"2": "M_WHT1"}, ref_at=(160.02, 78.74), val_at=(160.02, 81.28))
    sym("JP2", 198.12, Y, {"2": "M_WHT2"}, ref_at=(193.04, 60.96), val_at=(193.04, 63.5))
    sym("J3", 254, 81.28, P["J3"][4], ref_at=(252.73, 73.66), val_at=(252.73, 92.71))
    sym("J4", 238.76, 124.46, ref_at=(243.84, 124.46), val_at=(243.84, 127))
    for i in range(4):
        y = 27.94 + i * 7.62
        sch.symbol("Mechanical:MountingHole", "H%d" % (i + 1), "Wood screw, on a spacer", fpid(WS), 254, y, {},
                   ref_at=(256.54, y - 1.27), val_at=(256.54, y + 1.27))
    pin = sch.pin
    # line: J1 to fuse, fuse to switch terminal and C2
    sch.wire([pin("J1", "1"), pin("F1", "1")])
    sch.label("L_IN", 58.42, Y)
    sch.wire([pin("F1", "2"), pin("C2", "1")])
    sch.wire([(104.14, Y), pin("J2", "2")])
    sch.junction(104.14, Y)
    sch.label("L_FUSED", 85.09, Y)
    # switched line: switch terminal and C2 to C1, JP1 pin 3 and JP2 pin 1
    sch.wire([pin("J2", "1"), (106.68, 78.74), (124.46, 78.74), (124.46, Y)])
    sch.wire([pin("C2", "2"), (124.46, Y), pin("JP2", "1")])
    sch.junction(124.46, Y)
    sch.label("L_SW", 144.78, Y)
    sch.wire([(139.7, Y), (139.7, 43.18), pin("C1", "1")])
    sch.junction(139.7, Y)
    sch.wire([pin("JP1", "3"), (175.26, 86.36), (175.26, Y)])
    sch.junction(175.26, Y)
    # motor red lead: C1 and JP2 pin 3
    sch.wire([pin("JP2", "3"), (210.82, Y), (210.82, 43.18), pin("C1", "2")])
    sch.wire([(210.82, 55.88), (215.9, 55.88)])
    sch.junction(210.82, 55.88)
    sch.label("M_RED", 215.9, 55.88)
    # neutral: J1 to JP1 pin 1 (the motor green lead joins by label at J3)
    sch.wire([pin("J1", "2"), (60.96, 71.12), (60.96, 119.38), (152.4, 119.38), (152.4, 86.36), pin("JP1", "1")])
    sch.label("N", 101.6, 119.38)
    # protective earth: J1 to J4
    sch.wire([pin("J1", "3"), (55.88, 73.66), (55.88, 127), pin("J4", "2")])
    sch.wire([pin("J4", "1"), pin("J4", "2")])
    sch.label("PE", 101.6, 127)
    sch.text("MAINS VOLTAGE ON EVERY NET EXCEPT PE. UNPLUG BEFORE TOUCHING.", 30.48, 20.32, 2.2)
    sch.text("to the switch\nand back", 111.76, 97.79, 1.27)
    sch.text("motor leads", 252.73, 71.12, 1.27)
    sch.text("to a ring lug\non the top plate", 243.84, 121.92, 1.27)
    sch.text(
        "How the circuit reads (XA service manual, page 3):\n"
        "- Line comes in on J1, goes through fuse F1, then out to the switch and back on J2.\n"
        "- C2 sits across the switch. After the switch the net is L_SW.\n"
        "- C1 goes from L_SW to the motor's RED lead.\n"
        "- The motor has four leads, paired by winding:\n"
        "  WHITE and RED are winding 1. WHITE and GREEN are winding 2.\n"
        "- GREEN always goes to neutral.\n"
        "\n"
        "120 V: fit JP1 and JP2 in position 1-2 (board: 120, link pointing left).\n"
        "  Winding 1 white goes to neutral. Winding 2 white goes to L_SW.\n"
        "  The windings are in parallel, with C1 in series with winding 1.\n"
        "220 V: fit JP1 and JP2 in position 2-3 (board: 220, link pointing up).\n"
        "  Winding 1 white goes to L_SW. Winding 2 white goes to RED.\n"
        "  The windings are in series, with C1 across winding 1.\n"
        "Never fit both positions on one jumper.\n"
        "\n"
        "To confirm before power: the manual's 120 V drawing does not show where\n"
        "the winding 1 white lead returns. Neutral is the reading used here\n"
        "(circuit logic and the under-plate picture). Check on an unmodified table.",
        30.48, 187.96, 1.4)
    sch.write(os.path.join(d, name + ".kicad_sch"))

    # The board is a strip that screws flat to the inside face of a plinth wall,
    # long edge horizontal. Wires run along the wall, so the terminals are on the
    # two ends: mains in and earth on the left, switch and motor on the right.
    W, H = 130.0, 70.0
    bd = Board(name, title, W, H, comments)
    U = sch.symbols
    N = {p[0]: p[4] for p in parts}
    V_ = {p[0]: p[2] for p in parts}
    LX, RX = 8, 122                            # the two terminal columns
    bd.place(*TB3, "J1", V_["J1"], LX, 10, 270, N["J1"], U["J1"])      # pins at y 10, 17.5, 25
    bd.place(*TB2, "J4", V_["J4"], LX, 37, 270, N["J4"], U["J4"])      # pins at y 37, 44.5
    bd.place(*TB2, "J2", V_["J2"], RX, 17.5, 90, N["J2"], U["J2"])     # pin 1 at y 17.5, pin 2 at y 10
    bd.place(*TB4, "J3", V_["J3"], RX, 62, 90, N["J3"], U["J3"])       # pins 1 to 4 at y 62, 54.5, 47, 39.5
    bd.place(*FUSE, "F1", V_["F1"], 24, 10, 0, N["F1"], U["F1"], ref_at=(26.6, 18.4))
    bd.place("artt", "C_Film_MultiPitch_P15_P22.5_P27.5", "C1", V_["C1"], 66, 16, 0, N["C1"], U["C1"], ref_at=(59.8, 16))
    bd.place("artt", "C_Film_MultiPitch_P10_P15", "C2", V_["C2"], 51, 54.5, 0, N["C2"], U["C2"], ref_at=(45.6, 51.6))
    bd.place("artt", "WireLink_3Way_120V_Left_220V_Up", "JP1", V_["JP1"], 104, 39.5, 0, N["JP1"], U["JP1"], ref_at=(99.7, 36.4))
    bd.place("artt", "WireLink_3Way_120V_Left_220V_Up", "JP2", V_["JP2"], 104, 54.5, 0, N["JP2"], U["JP2"], ref_at=(99.7, 51.4))
    for i, (x, y) in enumerate([(25.5, 27), (25.5, 58), (124, 28.5), (74, 65)]):
        bd.place(*WS, "H%d" % (i + 1), "Wood screw, on a spacer", x, y, 0, None, U["H%d" % (i + 1)], hide_value=True)

    M, E = 1.5, 2.5
    bd.track("L_IN", [(LX, 10), (24, 10)], M)
    bd.track("PE", [(LX, 25), (LX, 44.5)], E)
    bd.track("PE", [(LX, 25), (LX, 44.5)], E, F)
    bd.track("N", [(LX, 17.5), (14.5, 17.5), (14.5, 39.5), (96.5, 39.5)], M, F)
    bd.track("N", [(91, 39.5), (91, 62), (RX, 62)], M, F)
    bd.track("L_FUSED", [(34, 10), (RX, 10)], M, F)
    bd.track("L_FUSED", [(34, 10), (36.5, 12.5), (36.5, 54.5), (51, 54.5)], M)
    bd.track("L_SW", [(61, 54.5), (96.5, 54.5)], M)
    bd.track("L_SW", [(66, 54.5), (66, 16)], M)
    bd.track("L_SW", [(66, 16), (66, 32), (104, 32)], M, F)
    bd.track("L_SW", [(104, 32), (113, 32), (113, 17.5), (RX, 17.5)], M)
    bd.track("M_RED", [(81, 16), (93.5, 16)], M)
    bd.track("M_RED", [(88.5, 16), (88.5, 47), (RX, 47)], M)
    bd.track("M_WHT1", [(104, 39.5), (RX, 39.5)], M)
    bd.track("M_WHT2", [(104, 54.5), (RX, 54.5)], M)

    bd.text("J1 MAINS IN", 11, 2.6, 1.0)
    bd.text("J4 TOP PLATE", 11.5, 51.2, 1.0)
    for y, t in [(10, "LINE"), (17.5, "NEUT"), (25, "EARTH"), (37, "EARTH"), (44.5, "EARTH")]:
        bd.text(t, 18.4, y, 1.0)
    bd.text("J2 SWITCH", 119, 2.6, 1.0)
    bd.text("J3 MOTOR", 119, 68.2, 1.0)
    for y, t in [(39.5, "WHT"), (47, "RED"), (54.5, "WHT"), (62, "GRN")]:
        bd.text(t, 113.4, y - 2.2, 1.0)
    bd.text("WINDING 1", 110.4, 41.1, 0.8)
    bd.text("WINDING 2", 110.4, 56.1, 0.8)
    bd.text("FUSE 5x20: VALUE FROM MOTOR LABEL", 44.6, 18.4, 0.9)
    bd.text("MOTOR CAP: 0.1uF AT 120V, 0.39uF AT 220V", 80, 24.6, 0.9)
    bd.text("SWITCH CAP: 0.022uF AT 120V", 54, 46.2, 0.8)
    bd.text("0.01uF AT 220V", 54, 47.8, 0.8)
    bd.text("120V: BOTH LINKS LEFT", 77.5, 43.8, 0.9)
    bd.text("220V: BOTH LINKS UP", 77.5, 45.8, 0.9)
    bd.text("DANGER MAINS VOLTAGE", 48, 64.2, 1.6, thick=0.3)
    bd.text("UNPLUG BEFORE TOUCHING", 48, 67.3, 1.0)
    bd.text("ARTT POWER BOARD REV C", 96, 67.3, 1.0)
    bd.text("DANGER MAINS VOLTAGE. UNPLUG FIRST.", 48, 64.2, 1.3, pcbnew.B_SilkS, 0.25, True)
    bd.text("ON SPACERS. INSULATING SHEET BEHIND", 48, 67.3, 1.0, pcbnew.B_SilkS, None, True)
    bd.save(os.path.join(d, name + ".kicad_pcb"))
    project_file(os.path.join(d, name + ".kicad_pro"), name,
                 [{"name": "Mains", "clearance": 2.5, "track_width": 1.5},
                  {"name": "Earth", "clearance": 4.0, "track_width": 2.5}],
                 [{"netclass": "Earth", "pattern": "/PE"},
                  {"netclass": "Mains", "pattern": "/L_*"},
                  {"netclass": "Mains", "pattern": "/N"},
                  {"netclass": "Mains", "pattern": "/M_*"}])
    return d, name, sch


# --------------------------------------------------------------------------
# Board 2: audio strip
# --------------------------------------------------------------------------

def audio_board():
    name = "artt-audio-strip-board"
    d = os.path.join(PCB, "audio-strip-board")
    title = "ARTT audio strip board"
    comments = ["Replaces the audio terminal strip under the top plate",
                "Arm wires in on solder pads. Jacks and ground post out on screw terminals",
                "Status: PRELIMINARY. Screws to the inside of the rear wall, next to the arm pivot"]
    arm = [("J1", "ARM L SIG", "L_SIG", 14), ("J2", "ARM L GND", "L_GND", 23), ("J3", "ARM SHIELD", "SHIELD", 32),
           ("J4", "ARM R GND", "R_GND", 41), ("J5", "ARM R SIG", "R_SIG", 50)]
    sch = Schematic(name, title, comments)
    rows = {"J1": 53.34, "J2": 63.5, "J3": 81.28, "J4": 99.06, "J5": 109.22}
    for ref, val, net, _ in arm:
        y = rows[ref]
        sch.symbol("Connector:Conn_01x01_Pin", ref, val, fpid(WIRE), 50.8, y, ref_at=(33.02, y - 1.27), val_at=(33.02, y + 1.27))
        sch.label(net, 66.04, y)
    sch.symbol("Device:C", "C1", "Left load, optional", fpid(CLOAD), 106.68, 58.42, ref_at=(110.49, 57.15), val_at=(110.49, 59.69))
    sch.symbol("Device:C", "C2", "Right load, optional", fpid(CLOAD), 106.68, 104.14, ref_at=(110.49, 102.87), val_at=(110.49, 105.41))
    sch.symbol("Connector:Screw_Terminal_01x02", "J6", "LEFT JACK", fpid(TBS), 157.48, 53.34, ref_at=(162.56, 53.34), val_at=(162.56, 55.88))
    sch.symbol("Connector:Screw_Terminal_01x02", "J7", "GROUND POST", fpid(TBS), 157.48, 81.28, ref_at=(162.56, 81.28), val_at=(162.56, 83.82))
    sch.symbol("Connector:Screw_Terminal_01x02", "J8", "RIGHT JACK", fpid(TBS), 157.48, 104.14, ref_at=(162.56, 104.14), val_at=(162.56, 106.68))
    for i in range(2):
        sch.symbol("Mechanical:MountingHole", "H%d" % (i + 1), "Wood screw, on a spacer", "artt:Hole_NPTH_3.5mm_Wood_Screw", 215.9, 53.34 + i * 7.62, {},
                   ref_at=(218.44, 52.07 + i * 7.62), val_at=(218.44, 54.61 + i * 7.62))
    pin = sch.pin
    sch.wire([pin("J1", "1"), pin("J6", "1")])
    sch.wire([pin("J2", "1"), (142.24, 63.5), (142.24, 55.88), pin("J6", "2")])
    sch.wire([pin("C1", "1"), (106.68, 53.34)])
    sch.wire([pin("C1", "2"), (106.68, 63.5)])
    sch.junction(106.68, 53.34)
    sch.junction(106.68, 63.5)
    sch.wire([pin("J3", "1"), pin("J7", "1")])
    sch.wire([pin("J7", "1"), pin("J7", "2")])
    sch.wire([pin("J4", "1"), (142.24, 99.06), (142.24, 104.14), pin("J8", "1")])
    sch.wire([pin("J5", "1"), (142.24, 109.22), (142.24, 106.68), pin("J8", "2")])
    sch.wire([pin("C2", "1"), (106.68, 99.06)])
    sch.wire([pin("C2", "2"), (106.68, 109.22)])
    sch.junction(106.68, 99.06)
    sch.junction(106.68, 109.22)
    sch.text("five arm wires,\nsoldered", 33.02, 43.18, 1.27)
    sch.text("screw terminals,\nto the jacks and the ground post", 157.48, 43.18, 1.27)
    sch.text(
        "How the board reads:\n"
        "- Five arm wires are soldered to J1 to J5. Each pad has a second hole beside it:\n"
        "  thread the wire through that hole first, as strain relief.\n"
        "- Left signal and left ground go to the left jack (J6).\n"
        "- Right signal and right ground go to the right jack (J8).\n"
        "- The arm shield goes to the ground post (J7). It is not joined to either channel ground on this board.\n"
        "- C1 and C2 are empty places for cartridge loading capacitors.\n"
        "  Leave them empty unless the cartridge needs more capacitance.\n"
        "\n"
        "Find which arm wire is which with an ohmmeter from the headshell pins:\n"
        "left is white (signal) and green (ground), right is red (signal) and black (ground).\n"
        "The wire colours inside the arm are not the headshell colours.",
        30.48, 180.34, 1.4)
    sch.write(os.path.join(d, name + ".kicad_sch"))

    # Screws flat to the inside of the rear wall, next to the arm pivot. Arm wires
    # come down to the top edge. The three outputs leave from the left end and run
    # along the wall to the jacks and the ground post.
    W, H = 72.0, 47.0
    bd = Board(name, title, W, H, comments)
    U = sch.symbols
    armx = {"J1": 24, "J2": 33, "J3": 42, "J4": 51, "J5": 60}
    for ref, val, net, _ in arm:
        bd.place(*WIRE, ref, val, armx[ref], 12, 180, {"1": net}, U[ref])
    TX = 7                                      # the terminal column
    bd.place(*TBS, "J6", "LEFT JACK", TX, 10, 270, {"1": "L_SIG", "2": "L_GND"}, U["J6"])      # pins at y 10, 15.08
    bd.place(*TBS, "J7", "GROUND POST", TX, 22.5, 270, {"1": "SHIELD", "2": "SHIELD"}, U["J7"])  # pins at y 22.5, 27.58
    bd.place(*TBS, "J8", "RIGHT JACK", TX, 35, 270, {"1": "R_GND", "2": "R_SIG"}, U["J8"])     # pins at y 35, 40.08
    bd.place(*CLOAD, "C1", "Left load, optional", 18, 10.04, 270, {"1": "L_SIG", "2": "L_GND"}, U["C1"])
    bd.place(*CLOAD, "C2", "Right load, optional", 18, 35.04, 270, {"1": "R_GND", "2": "R_SIG"}, U["C2"])
    for i, (x, y) in enumerate([(30, 28.75), (67, 28.75)]):
        bd.place("artt", "Hole_NPTH_3.5mm_Wood_Screw", "H%d" % (i + 1), "Wood screw, on a spacer", x, y, 0, None, U["H%d" % (i + 1)], hide_value=True)
    S, G = 0.6, 1.0
    bd.track("L_SIG", [(TX, 10), (18, 10.04), (22.04, 10.04), (24, 12)], S)
    bd.track("L_GND", [(TX, 15.08), (18, 15.04), (33, 15.04), (33, 12)], S)
    bd.track("SHIELD", [(TX, 27.58), (TX, 22.5), (42, 22.5), (42, 12)], G)
    bd.track("R_GND", [(TX, 35), (18, 35.04), (51, 35.04), (51, 12)], S)
    bd.track("R_SIG", [(TX, 40.08), (18, 40.04), (60, 40.04), (60, 12)], S)
    bd.text("ARM WIRES IN", 42, 2.4, 1.0)
    for (ref, val, net, _), top, col in zip(arm, ["L SIG", "L GND", "SHIELD", "R GND", "R SIG"],
                                            ["WHITE", "GREEN", "ARM TUBE", "BLACK", "RED"]):
        bd.text(top, armx[ref] + 4.5, 11.2, 0.9)
        bd.text(col, armx[ref] + 4.5, 12.9, 0.8)
    for y, t in [(10, "SIG"), (15.08, "GND"), (22.5, "GND"), (27.58, "GND"), (35, "GND"), (40.08, "SIG")]:
        bd.text(t, 14.6, y - 1.7, 0.8)
    bd.text("C1 OPT", 18, 6.6, 0.8)
    bd.text("C2 OPT", 18, 44.4, 0.8)
    bd.text("LEFT JACK", 28, 18.6, 1.0)
    bd.text("GROUND POST", 44, 26.2, 1.0)
    bd.text("RIGHT JACK", 44, 31.4, 1.0)
    bd.text("ARTT AUDIO STRIP BOARD REV C", 42, 44.2, 1.0)
    bd.text("SECOND LABEL ROW = HEADSHELL WIRE COLOUR", 40, 44.2, 0.9, pcbnew.B_SilkS, None, True)
    bd.save(os.path.join(d, name + ".kicad_pcb"))
    project_file(os.path.join(d, name + ".kicad_pro"), name,
                 [{"name": "Audio", "clearance": 0.5, "track_width": 0.6}],
                 [{"netclass": "Audio", "pattern": "/*"}])
    return d, name, sch


# --------------------------------------------------------------------------
# Board 3: rear jack panel (no copper)
# --------------------------------------------------------------------------

def rear_panel():
    name = "artt-rear-jack-panel"
    d = os.path.join(PCB, "rear-jack-panel")
    title = "ARTT rear jack panel"
    comments = ["Bare fibreglass panel for two RCA jacks and the ground post. No copper",
                "Screws to the inside of the rear wall, over a cutout of about 4 1/8 x 1 3/8 in (Galo)",
                "Status: PRELIMINARY. Set the hole sizes from your jacks before ordering"]
    holes = [("H1", "Wood screw", "Hole_NPTH_3.5mm_Wood_Screw", 5.5, 5), ("H2", "Wood screw", "Hole_NPTH_3.5mm_Wood_Screw", 129.5, 5),
             ("H3", "Wood screw", "Hole_NPTH_3.5mm_Wood_Screw", 5.5, 55), ("H4", "Wood screw", "Hole_NPTH_3.5mm_Wood_Screw", 129.5, 55),
             ("H5", "LEFT RCA JACK", "Hole_NPTH_9.6mm_RCA_Jack", 37.5, 30), ("H6", "RIGHT RCA JACK", "Hole_NPTH_9.6mm_RCA_Jack", 67.5, 30),
             ("H7", "GROUND POST", "Hole_NPTH_3.7mm_Ground_Post", 97.5, 30)]
    sch = Schematic(name, title, comments)
    for i, (ref, val, fp, _, _) in enumerate(holes):
        x = 50.8 + (i % 4) * 38.1
        y = 60.96 + (i // 4) * 25.4
        sch.symbol("Mechanical:MountingHole", ref, val, "artt:" + fp, x, y, {}, ref_at=(x + 2.54, y - 1.27), val_at=(x + 2.54, y + 1.27))
    sch.text("This panel has no circuit. The symbols are the seven holes, so the board and the schematic stay in step.\n"
             "The jacks are insulated from each other and from the metalwork because the panel is fibreglass with no copper.",
             30.48, 127, 1.5)
    sch.write(os.path.join(d, name + ".kicad_sch"))

    W, H = 135.0, 60.0
    bd = Board(name, title, W, H, comments)
    for ref, val, fp, x, y in holes:
        bd.place("artt", fp, ref, val, x, y, 0, None, sch.symbols[ref], hide_value=(val == "Wood screw"))
    bd.text("LEFT", 37.5, 17.5, 2.0, thick=0.3)
    bd.text("RIGHT", 67.5, 17.5, 2.0, thick=0.3)
    bd.text("GROUND", 97.5, 22.5, 2.0, thick=0.3)
    bd.text("ARTT REAR JACK PANEL REV C", 67.5, 44.6, 1.2)
    bd.rect(67.5 - 52.3875, 30 - 17.4625, 67.5 + 52.3875, 30 + 17.4625, pcbnew.Dwgs_User, 0.15)
    bd.text("PLINTH CUTOUT 4 1/8 x 1 3/8 IN: THIS FACE SHOWS THROUGH IT", 67.5, 52.5, 1.2, pcbnew.Dwgs_User)
    bd.text("LEFT", 37.5, 17.5, 2.0, pcbnew.B_SilkS, 0.3, True)
    bd.text("RIGHT", 67.5, 17.5, 2.0, pcbnew.B_SilkS, 0.3, True)
    bd.text("GROUND", 97.5, 22.5, 2.0, pcbnew.B_SilkS, 0.3, True)
    bd.text("THIS FACE TOWARD THE INSIDE OF THE PLINTH", 67.5, 53, 1.2, pcbnew.B_SilkS, None, True)
    bd.save(os.path.join(d, name + ".kicad_pcb"))
    project_file(os.path.join(d, name + ".kicad_pro"), name, [], [])
    return d, name, sch


if __name__ == "__main__":
    for f in (power_board, audio_board, rear_panel):
        d, name, sch = f()
        print("wrote", os.path.relpath(os.path.join(d, name), PCB))
