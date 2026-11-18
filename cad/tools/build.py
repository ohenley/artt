#!/usr/bin/env python3
"""Build STEP, STL, PDF, and DXF exports from the OpenSCAD part files.

OpenSCAD files are the only source. This script asks OpenSCAD for each part's
CSG tree and its parameter data, rebuilds the tree in OpenCASCADE to get true
cylinders and planes for STEP, then projects that solid into orthographic views.

    python build.py            build every part, then rewrite the drawings table in cad/README.md
    python build.py NAME       build one part file, without .scad
    python build.py --check    check that every PH and DV row is logged in TO-CONFIRM.md
                               and that the README table matches the part files

Requires: openscad on PATH, and the packages in requirements.txt.
License: MIT, see LICENSE in this directory.
"""
import datetime
import json
import math
import os
import re
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

import ezdxf
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import PathPatch
from matplotlib.path import Path as MplPath
import numpy as np
from OCP.Bnd import Bnd_Box
from OCP.BRep import BRep_Tool
from OCP.BRepAdaptor import BRepAdaptor_Curve, BRepAdaptor_Surface
from OCP.BRepAlgoAPI import BRepAlgoAPI_Common, BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCP.BRepBndLib import BRepBndLib
from OCP.BRepBuilderAPI import (
    BRepBuilderAPI_MakeEdge,
    BRepBuilderAPI_MakeFace,
    BRepBuilderAPI_MakePolygon,
    BRepBuilderAPI_MakeWire,
    BRepBuilderAPI_Transform,
)
from OCP.BRepCheck import BRepCheck_Analyzer
from OCP.BRepGProp import BRepGProp
from OCP.BRepLib import BRepLib
from OCP.BRepPrimAPI import (
    BRepPrimAPI_MakeBox,
    BRepPrimAPI_MakeCone,
    BRepPrimAPI_MakeCylinder,
    BRepPrimAPI_MakePrism,
    BRepPrimAPI_MakeRevol,
)
from OCP.BRepTools import BRepTools_WireExplorer
from OCP.GCPnts import GCPnts_QuasiUniformDeflection
from OCP.GProp import GProp_GProps
from OCP.GeomAbs import GeomAbs_Line, GeomAbs_Plane
from OCP.HLRAlgo import HLRAlgo_Projector
from OCP.HLRBRep import HLRBRep_Algo, HLRBRep_HLRToShape
from OCP.IFSelect import IFSelect_RetDone
from OCP.Interface import Interface_Static
from OCP.STEPControl import STEPControl_AsIs, STEPControl_Reader, STEPControl_Writer
from OCP.ShapeUpgrade import ShapeUpgrade_UnifySameDomain
from OCP.TopAbs import TopAbs_EDGE, TopAbs_FACE, TopAbs_REVERSED, TopAbs_WIRE
from OCP.TopExp import TopExp_Explorer
from OCP.TopoDS import TopoDS
from OCP.gp import gp_Ax1, gp_Ax2, gp_Circ, gp_Dir, gp_Pnt, gp_Trsf, gp_Vec

ROOT = Path(__file__).resolve().parents[1]
PARTS = ROOT / "parts"
EXPORTS = ROOT / "exports"
TO_CONFIRM = ROOT.parent / "TO-CONFIRM.md"
README = ROOT / "README.md"
DRAWING_DATE = "2026-11-18"
REVISION = "B"
# Fixed timestamps, so that rebuilding an unchanged part leaves its files unchanged.
FIXED_TIME = datetime.datetime(2026, 11, 18, 12, 0, 0, tzinfo=datetime.timezone.utc)
FIXED_JULIAN = 2461363.5  # the same instant as a DXF Julian date
FIXED_GUID = "{00000000-0000-0000-0000-000000000000}"

SHEET_W, SHEET_H = 420.0, 297.0  # A3 landscape, mm
RED = "#c00000"       # PH: placeholder
BLUE = "#0050b0"      # DV: derived from sources, verify on the part
INK = "#000000"       # sourced
GREY = "#555555"
DXF_COLOR = {RED: 1, BLUE: 5}

EVIDENCE = {
    "F": "factory document",
    "O": "owner report",
    "C": "community drawing",
    "S": "industry standard",
    "D": "design choice",
    "M": "measured",
    "DV": "DERIVED, verify on the part",
    "PH": "PLACEHOLDER, measure first",
}
# Codes that need a row in TO-CONFIRM.md.
OPEN_CODES = {"PH", "DV"}

STATUS_TEXT = {
    "GEOMETRY COMPLETE": "All dimensions from the cited source. Tolerances and fit are not established.",
    "REFERENCE": "Reference for a part to buy. Do not machine from this sheet.",
    "DERIVED": "Prototype and fit test only. Dimensions marked DV are worked out from sources and not yet verified on a part.",
    "PRELIMINARY": "NOT FOR MANUFACTURE until every red dimension is measured.",
    "CONCEPT": "NOT FOR MANUFACTURE. Concept layout; red dimensions are not measurements.",
}
# Status: (file prefix, watermark, colour).
STATUS_MARK = {
    "GEOMETRY COMPLETE": ("", None, INK),
    "REFERENCE": ("", None, INK),
    "DERIVED": ("DERIVED-", "FIT TEST ONLY", BLUE),
    "PRELIMINARY": ("PRELIMINARY-", "NOT FOR MANUFACTURE", RED),
    "CONCEPT": ("PRELIMINARY-", "NOT FOR MANUFACTURE", RED),
}
# The tables a part can be claimed to fit, in the order the pages use.
TABLES = ["XA", "XB", "XB1", "AR77XB", "The AR Turntable and Legend", "EB-101", "ES-1", "ETL-1"]
FIT_WORDS = ("Fitted by AR", "Fits", "Fits with a change", "Does not fit", "Unconfirmed")


def row_color(row):
    return {"PH": RED, "DV": BLUE}.get(row[3], INK)


def row_tag(row):
    return f" {row[3]}" if row[3] in OPEN_CODES else ""

# Third-angle views: (direction from part to viewer, sheet x axis).
VIEWS = {
    "front": ((0, -1, 0), (1, 0, 0)),
    "top": ((0, 0, 1), (1, 0, 0)),
    "bottom": ((0, 0, -1), (1, 0, 0)),
    "right": ((1, 0, 0), (0, 1, 0)),
    "left": ((-1, 0, 0), (0, -1, 0)),
    "rear": ((0, 1, 0), (-1, 0, 0)),
    "iso": ((1, -1, 0.8), (1, 1, 0)),
}


# OpenSCAD

def openscad(scad, out, defines=()):
    cmd = ["openscad", "-o", str(out)]
    for key, value in defines:
        cmd += ["-D", f"{key}={value}"]
    cmd.append(str(scad))
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=scad.parent)
    if result.returncode or not Path(out).exists():
        raise RuntimeError(f"OpenSCAD failed for {scad.name}:\n{result.stderr}")
    return result.stderr


def read_part_data(console):
    meta, params, dims = {}, [], []
    for line in console.splitlines():
        match = re.match(r'ECHO: (META|PARAM|DIM) = (.*)$', line)
        if not match:
            continue
        data = json.loads(match.group(2))
        if match.group(1) == "META":
            meta = {key: value for key, value in data}
        elif match.group(1) == "PARAM":
            params.append(data)
        else:
            dims.append(data)
    if not meta:
        raise RuntimeError("No META data echoed by part file")
    return meta, {row[0]: row for row in params}, dims


# CSG tree to OpenCASCADE solid

def split_args(text):
    args, depth, start, in_str = [], 0, 0, False
    for i, ch in enumerate(text):
        if ch == '"':
            in_str = not in_str
        elif not in_str:
            if ch in "([":
                depth += 1
            elif ch in ")]":
                depth -= 1
            elif ch == "," and depth == 0:
                args.append(text[start:i])
                start = i + 1
    if text[start:].strip():
        args.append(text[start:])
    return args


def parse_args(text):
    named, positional = {}, []
    for arg in split_args(text):
        match = re.match(r"\s*(\$?\w+)\s*=\s*(.*)$", arg, re.S)
        value = match.group(2) if match else arg
        parsed = json.loads(re.sub(r"\bundef\b", "null", value.strip()))
        if match:
            named[match.group(1)] = parsed
        else:
            positional.append(parsed)
    return named, positional


def parse_csg(text):
    pos = 0

    def skip():
        nonlocal pos
        while pos < len(text) and text[pos].isspace():
            pos += 1

    def nodes():
        nonlocal pos
        result = []
        while True:
            skip()
            if pos >= len(text) or text[pos] == "}":
                return result
            if text[pos] == ";":
                pos += 1
                continue
            match = re.compile(r"(\w+)\s*\(").match(text, pos)
            if not match:
                raise ValueError(f"Cannot parse CSG at: {text[pos:pos + 60]!r}")
            pos = match.end()
            depth, start, in_str = 1, pos, False
            while depth:
                ch = text[pos]
                if ch == '"':
                    in_str = not in_str
                elif not in_str and ch == "(":
                    depth += 1
                elif not in_str and ch == ")":
                    depth -= 1
                pos += 1
            named, positional = parse_args(text[start:pos - 1])
            skip()
            children = []
            if pos < len(text) and text[pos] == "{":
                pos += 1
                children = nodes()
                skip()
                pos += 1
            result.append((match.group(1), named, positional, children))

    return nodes()


def clean(shape):
    unify = ShapeUpgrade_UnifySameDomain(shape, True, True, True)
    unify.Build()
    return unify.Shape()


def fuse_all(shapes):
    if not shapes:
        return None
    result = shapes[0]
    for shape in shapes[1:]:
        result = BRepAlgoAPI_Fuse(result, shape).Shape()
    return clean(result)


def polygon_face(points):
    poly = BRepBuilderAPI_MakePolygon()
    for x, y in points:
        poly.Add(gp_Pnt(x, y, 0))
    poly.Close()
    return BRepBuilderAPI_MakeFace(poly.Wire()).Face()


def build_2d(node):
    name, named, positional, children = node
    if name == "polygon":
        if named.get("paths") and len(named["paths"]) > 1:
            raise ValueError("Polygons with holes are not supported")
        return polygon_face(named["points"])
    if name == "square":
        x, y = named["size"]
        ox, oy = (-x / 2, -y / 2) if named.get("center") else (0, 0)
        return polygon_face([(ox, oy), (ox + x, oy), (ox + x, oy + y), (ox, oy + y)])
    if name == "circle":
        circle = gp_Circ(gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1)), named["r"])
        wire = BRepBuilderAPI_MakeWire(BRepBuilderAPI_MakeEdge(circle).Edge()).Wire()
        return BRepBuilderAPI_MakeFace(wire).Face()
    if name in ("group", "union") and len(children) == 1:
        return build_2d(children[0])
    raise ValueError(f"Unsupported 2D node in part file: {name}")


def build_3d(node):
    name, named, positional, children = node
    if name == "cube":
        x, y, z = named["size"]
        ox, oy, oz = (-x / 2, -y / 2, -z / 2) if named.get("center") else (0, 0, 0)
        return BRepPrimAPI_MakeBox(gp_Pnt(ox, oy, oz), x, y, z).Shape()
    if name == "cylinder":
        h, r1, r2 = named["h"], named["r1"], named["r2"]
        z0 = -h / 2 if named.get("center") else 0
        axis = gp_Ax2(gp_Pnt(0, 0, z0), gp_Dir(0, 0, 1))
        if abs(r1 - r2) < 1e-9:
            return BRepPrimAPI_MakeCylinder(axis, r1, h).Shape()
        return BRepPrimAPI_MakeCone(axis, r1, r2, h).Shape()
    if name in ("group", "union", "render"):
        return fuse_all([s for s in (build_3d(c) for c in children) if s is not None])
    if name == "difference":
        result = build_3d(children[0])
        for child in children[1:]:
            cut = build_3d(child)
            if cut is not None:
                result = BRepAlgoAPI_Cut(result, cut).Shape()
        return clean(result)
    if name == "intersection":
        result = build_3d(children[0])
        for child in children[1:]:
            result = BRepAlgoAPI_Common(result, build_3d(child)).Shape()
        return clean(result)
    if name == "multmatrix":
        m = named.get("m") or positional[0]
        trsf = gp_Trsf()
        trsf.SetValues(*m[0], *m[1], *m[2])
        child = fuse_all([s for s in (build_3d(c) for c in children) if s is not None])
        return None if child is None else BRepBuilderAPI_Transform(child, trsf, True).Shape()
    if name == "linear_extrude":
        if named.get("twist"):
            raise ValueError("Twisted extrusion is not supported")
        face = build_2d(("group", {}, [], children))
        h = named["height"]
        shape = BRepPrimAPI_MakePrism(face, gp_Vec(0, 0, h)).Shape()
        if named.get("center"):
            trsf = gp_Trsf()
            trsf.SetTranslation(gp_Vec(0, 0, -h / 2))
            shape = BRepBuilderAPI_Transform(shape, trsf, True).Shape()
        return shape
    if name == "rotate_extrude":
        face = build_2d(("group", {}, [], children))
        trsf = gp_Trsf()
        trsf.SetRotation(gp_Ax1(gp_Pnt(0, 0, 0), gp_Dir(1, 0, 0)), math.pi / 2)
        face = BRepBuilderAPI_Transform(face, trsf, True).Shape()
        angle = math.radians(named.get("angle", 360))
        return BRepPrimAPI_MakeRevol(face, gp_Ax1(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1)), angle).Shape()
    raise ValueError(f"Unsupported CSG node in part file: {name}")


def solid_volume(shape):
    props = GProp_GProps()
    BRepGProp.VolumeProperties_s(shape, props)
    return props.Mass()


def stl_volume(path):
    numbers = re.findall(r"vertex\s+(\S+)\s+(\S+)\s+(\S+)", Path(path).read_text())
    tri = np.array(numbers, dtype=float).reshape(-1, 3, 3)
    return float(np.abs(np.einsum("ij,ij->i", tri[:, 0], np.cross(tri[:, 1], tri[:, 2])).sum()) / 6)


def write_step(shape, path):
    Interface_Static.SetCVal_s("write.step.unit", "MM")
    Interface_Static.SetCVal_s("write.step.schema", "AP214IS")
    writer = STEPControl_Writer()
    writer.Transfer(shape, STEPControl_AsIs)
    if writer.Write(str(path)) != IFSelect_RetDone:
        raise RuntimeError(f"STEP write failed: {path}")
    # Drop the timestamp and the library build number so rebuilding an unchanged
    # part leaves the file unchanged.
    text = Path(path).read_text()
    text = re.sub(r"FILE_NAME\('[^']*','[^']*'", f"FILE_NAME('{Path(path).name}','{DRAWING_DATE}'", text, count=1)
    text = re.sub(r"Open CASCADE STEP translator [\d.]+ \d+", "Open CASCADE STEP translator", text)
    Path(path).write_text(text)


def read_step_volume(path):
    reader = STEPControl_Reader()
    if reader.ReadFile(str(path)) != IFSelect_RetDone:
        raise RuntimeError(f"STEP re-read failed: {path}")
    reader.TransferRoots()
    return solid_volume(reader.OneShape())


# Projection

def view_axes(name):
    n, x = VIEWS[name]
    n = np.array(n, dtype=float)
    n /= np.linalg.norm(n)
    x = np.array(x, dtype=float)
    x -= n * x.dot(n)
    x /= np.linalg.norm(x)
    return n, x, np.cross(n, x)


def edge_polyline(edge):
    curve = BRepAdaptor_Curve(edge)
    if curve.GetType() == GeomAbs_Line:
        a, b = curve.Value(curve.FirstParameter()), curve.Value(curve.LastParameter())
        return [(a.X(), a.Y()), (b.X(), b.Y())]
    sampler = GCPnts_QuasiUniformDeflection(curve, 0.005)
    if not sampler.IsDone():
        return []
    return [(sampler.Value(i).X(), sampler.Value(i).Y()) for i in range(1, sampler.NbPoints() + 1)]


def compound_polylines(compound):
    lines = []
    if compound is None or compound.IsNull():
        return lines
    BRepLib.BuildCurves3d_s(compound)
    explorer = TopExp_Explorer(compound, TopAbs_EDGE)
    while explorer.More():
        line = edge_polyline(TopoDS.Edge(explorer.Current()))
        if len(line) > 1:
            lines.append(line)
        explorer.Next()
    return lines


def hlr(shape, view):
    n, x, _ = view_axes(view)
    algo = HLRBRep_Algo()
    algo.Add(shape)
    frame = gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(*n), gp_Dir(*x))
    algo.Projector(HLRAlgo_Projector(frame))
    algo.Update()
    algo.Hide()
    out = HLRBRep_HLRToShape(algo)
    visible = compound_polylines(out.VCompound()) + compound_polylines(out.OutLineVCompound())
    hidden = compound_polylines(out.HCompound()) + compound_polylines(out.OutLineHCompound())
    if view == "iso":
        visible += compound_polylines(out.Rg1LineVCompound())
        hidden = []
    return visible, drop_overlaps(hidden, visible)


def drop_overlaps(hidden, visible, tolerance=0.01):
    """Remove hidden lines that lie on a visible edge, as a drafter would."""
    segments = [(np.array(a), np.array(b)) for line in visible for a, b in zip(line, line[1:])]
    if not segments:
        return hidden
    starts = np.array([s[0] for s in segments])
    deltas = np.array([s[1] - s[0] for s in segments])
    lengths = np.maximum((deltas ** 2).sum(axis=1), 1e-12)
    kept = []
    for line in hidden:
        pts = np.array(line)
        mids = (pts[:-1] + pts[1:]) / 2
        samples = np.vstack([pts, mids])
        covered = True
        for point in samples:
            frac = np.clip(((point - starts) * deltas).sum(axis=1) / lengths, 0, 1)
            nearest = starts + deltas * frac[:, None]
            if np.sqrt(((point - nearest) ** 2).sum(axis=1)).min() > tolerance:
                covered = False
                break
        if not covered:
            kept.append(line)
    return kept


def bounds(lines):
    pts = np.array([p for line in lines for p in line])
    return pts[:, 0].min(), pts[:, 0].max(), pts[:, 1].min(), pts[:, 1].max()


def section_cut(shape, axis, position):
    """Remove the half of the part nearer the viewer; return it and the cut faces."""
    box = Bnd_Box()
    BRepBndLib.Add_s(shape, box)
    lo, hi = box.CornerMin(), box.CornerMax()
    x0, y0, z0, x1, y1, z1 = lo.X(), lo.Y(), lo.Z(), hi.X(), hi.Y(), hi.Z()
    pad = 5.0
    if axis == "y":
        cutter = BRepPrimAPI_MakeBox(
            gp_Pnt(x0 - pad, y0 - pad, z0 - pad), x1 - x0 + 2 * pad, position - y0 + pad, z1 - z0 + 2 * pad
        ).Shape()
    elif axis == "x":
        cutter = BRepPrimAPI_MakeBox(
            gp_Pnt(position, y0 - pad, z0 - pad), x1 - position + pad, y1 - y0 + 2 * pad, z1 - z0 + 2 * pad
        ).Shape()
    else:
        raise ValueError("Only sections on an X or a Y plane are supported")
    cut = clean(BRepAlgoAPI_Cut(shape, cutter).Shape())
    faces = []
    explorer = TopExp_Explorer(cut, TopAbs_FACE)
    while explorer.More():
        face = TopoDS.Face(explorer.Current())
        surface = BRepAdaptor_Surface(face)
        if surface.GetType() == GeomAbs_Plane:
            normal = surface.Plane().Axis().Direction()
            location = surface.Plane().Location()
            along, where = (normal.Y(), location.Y()) if axis == "y" else (normal.X(), location.X())
            if abs(abs(along) - 1) < 1e-6 and abs(where - position) < 1e-6:
                faces.append(face)
        explorer.Next()
    return cut, faces


def face_loops(face, axis="y"):
    loops = []
    wires = TopExp_Explorer(face, TopAbs_WIRE)
    while wires.More():
        wire = TopoDS.Wire(wires.Current())
        loop = []
        edges = BRepTools_WireExplorer(wire)
        while edges.More():
            edge = edges.Current()
            curve = BRepAdaptor_Curve(edge)
            params = np.linspace(curve.FirstParameter(), curve.LastParameter(), 2 if curve.GetType() == GeomAbs_Line else 25)
            pts = [curve.Value(float(t)) for t in params]
            pts = [(p.X() if axis == "y" else p.Y(), p.Z()) for p in pts]
            if edge.Orientation() == TopAbs_REVERSED:
                pts.reverse()
            loop.extend(pts[:-1])
            edges.Next()
        loops.append(loop)
        wires.Next()
    return loops


# Drawing primitives. One display list renders to both PDF and DXF.

class Sheet:
    def __init__(self):
        self.lines = []
        self.texts = []
        self.hatches = []
        self.fills = []
        self.arrows = []

    def line(self, pts, layer="VISIBLE", color=INK):
        self.lines.append((pts, layer, color))

    def text(self, x, y, s, size=7.0, ha="left", va="bottom", color=INK, rot=0, weight="normal"):
        self.texts.append((x, y, s, size, ha, va, color, rot, weight))

    def arrow(self, tip, direction, color=INK):
        self.arrows.append((tip, direction, color))


LINE_STYLES = {
    "VISIBLE": dict(lw=0.65, ls="-"),
    "HIDDEN": dict(lw=0.30, ls=(0, (4, 2.4))),
    "CENTER": dict(lw=0.25, ls=(0, (9, 2, 2, 2))),
    "DIM": dict(lw=0.25, ls="-"),
    "FRAME": dict(lw=0.55, ls="-"),
    "THIN": dict(lw=0.25, ls="-"),
}


def render_pdf_page(sheet, pdf, watermark=None, watermark_color=RED):
    fig = plt.figure(figsize=(SHEET_W / 25.4, SHEET_H / 25.4))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, SHEET_W)
    ax.set_ylim(0, SHEET_H)
    ax.set_aspect("equal")
    ax.axis("off")
    for loops in sheet.hatches:
        verts, codes = [], []
        for loop in loops:
            verts += loop + [loop[0]]
            codes += [MplPath.MOVETO] + [MplPath.LINETO] * (len(loop) - 1) + [MplPath.CLOSEPOLY]
        ax.add_patch(PathPatch(MplPath(verts, codes), facecolor="none", edgecolor=GREY, hatch="////", lw=0))
    for loops in sheet.fills:
        for loop in loops:
            xs, ys = zip(*loop)
            ax.fill(xs, ys, color=INK, lw=0)
    for pts, layer, color in sheet.lines:
        xs, ys = zip(*pts)
        ax.plot(xs, ys, color=color, solid_capstyle="round", **LINE_STYLES[layer])
    for tip, direction, color in sheet.arrows:
        tx, ty = tip
        dx, dy = direction
        px, py = -dy, dx
        length, half = 2.4, 0.42
        ax.fill(
            [tx, tx - dx * length + px * half, tx - dx * length - px * half],
            [ty, ty - dy * length + py * half, ty - dy * length - py * half],
            color=color,
            lw=0,
        )
    for x, y, s, size, ha, va, color, rot, weight in sheet.texts:
        ax.text(x, y, s, fontsize=size, ha=ha, va=va, color=color, rotation=rot, fontweight=weight, family="DejaVu Sans")
    if watermark:
        ax.text(
            SHEET_W / 2, 182, watermark, fontsize=46, color=watermark_color, alpha=0.10, rotation=24,
            ha="center", va="center", fontweight="bold", family="DejaVu Sans",
        )
    pdf.savefig(fig)
    plt.close(fig)


def open_pdf(path):
    """A PdfPages with fixed metadata, so an unchanged part gives an unchanged file."""
    return PdfPages(path, metadata={"CreationDate": FIXED_TIME, "ModDate": FIXED_TIME,
                                    "Creator": "cad/tools/build.py", "Producer": "matplotlib"})


def render_dxf(sheet, path):
    doc = ezdxf.new("R2010", setup=True)
    doc.units = ezdxf.units.MM
    linetypes = {"HIDDEN": "DASHED", "CENTER": "CENTER"}
    for layer in LINE_STYLES:
        doc.layers.add(layer, linetype=linetypes.get(layer, "Continuous"))
    doc.layers.add("TEXT")
    space = doc.modelspace()
    for loops in sheet.hatches:
        hatch = space.add_hatch(dxfattribs={"layer": "THIN"})
        hatch.set_pattern_fill("ANSI31", scale=0.5)
        for loop in loops:
            hatch.paths.add_polyline_path(loop, is_closed=True)
    for pts, layer, color in sheet.lines:
        attrs = {"layer": layer}
        if color in DXF_COLOR:
            attrs["color"] = DXF_COLOR[color]
        space.add_lwpolyline(pts, dxfattribs=attrs)
    for tip, direction, color in sheet.arrows:
        tx, ty = tip
        dx, dy = direction
        px, py = -dy, dx
        attrs = {"layer": "DIM"}
        if color in DXF_COLOR:
            attrs["color"] = DXF_COLOR[color]
        space.add_lwpolyline(
            [(tx, ty), (tx - dx * 2.4 + px * 0.42, ty - dy * 2.4 + py * 0.42),
             (tx - dx * 2.4 - px * 0.42, ty - dy * 2.4 - py * 0.42)],
            close=True, dxfattribs=attrs,
        )
    for x, y, s, size, ha, va, color, rot, _ in sheet.texts:
        attrs = {"layer": "TEXT", "rotation": rot, "style": "OpenSans"}
        if color in DXF_COLOR:
            attrs["color"] = DXF_COLOR[color]
        for i, line in enumerate(s.split("\n")):
            entity = space.add_text(line, height=size * 0.3528 * 0.72, dxfattribs=attrs)
            align = {"left": "LEFT", "center": "CENTER", "right": "RIGHT"}[ha]
            entity.set_placement((x, y - i * size * 0.45), align=ezdxf.enums.TextEntityAlignment[align])
    for key in ("$TDCREATE", "$TDUCREATE"):
        doc.header[key] = FIXED_JULIAN
    doc.header["$FINGERPRINTGUID"] = FIXED_GUID
    doc.saveas(path)
    # ezdxf stamps the update time, a version GUID and a save timestamp on every
    # save. Fix them, so an unchanged part gives an unchanged file.
    text = Path(path).read_text()
    text = re.sub(r"(\$TDU?UPDATE\n 40\n)[\d.]+", lambda m: f"{m.group(1)}{FIXED_JULIAN}", text)
    text = re.sub(r"(\$VERSIONGUID\n  2\n)\{[0-9A-F-]+\}", lambda m: f"{m.group(1)}{FIXED_GUID}", text)
    text = re.sub(r"(\n  1\n)(\d+\.\d+\.\d+) @ [0-9T:.+-]+", lambda m: f"{m.group(1)}{m.group(2)} @ {FIXED_TIME.isoformat()}", text)
    Path(path).write_text(text)


def format_value(row):
    value_mm, unit = row[2], row[4]
    if unit == "in":
        return f"{value_mm / 25.4:.3f} in ({value_mm:.2f})"
    if unit == "deg":
        return f"{value_mm:g} deg"
    if unit in ("g", "g/cm3", "lines"):
        return f"{value_mm:g} {unit}"
    if unit == "":
        return f"{value_mm:g}"
    return f"{value_mm:g} mm ({value_mm / 25.4:.3f} in)"


def draw_leader(sheet, dim, place, params, box, scale):
    """Diameter leader: [view, "d", center, radius, offset, id, prefix, angle_deg]."""
    center = place(dim[2])
    radius = dim[3] * scale
    offset, param_id = dim[4], dim[5]
    prefix = dim[6] if len(dim) > 6 else ""
    angle = math.radians(dim[7] if len(dim) > 7 else 45)
    row = params[param_id]
    color = row_color(row)
    cos_a, sin_a = math.cos(angle), math.sin(angle)
    tip = (center[0] + radius * cos_a, center[1] + radius * sin_a)
    target_y = box[3] + offset if sin_a > 0 else box[2] - offset
    run = (target_y - tip[1]) / sin_a
    knee = (tip[0] + run * cos_a, target_y)
    side = 1 if cos_a >= 0 else -1
    end = (knee[0] + side * 4, target_y)
    sheet.line([tip, knee, end], "DIM", color)
    sheet.arrow(tip, (-cos_a, -sin_a), color)
    label = f"{prefix}{format_value(row)}  {param_id}{row_tag(row)}"
    sheet.text(end[0] + side * 0.8, target_y, label, 6.2, "left" if side > 0 else "right", "center", color)


def draw_arc_dim(sheet, dim, place, params):
    """Radius or angle of an arc in the XY plane. The label sits beside the arc center.

    Radius: [view, "r", center, radius, at_deg, id, dx, dy, ha].
    Angle:  [view, "a", center, radius, start_deg, end_deg, id, dx, dy, ha].
    dx and dy move the label from the center, in sheet mm.
    """
    kind, center, radius = dim[1], dim[2], dim[3]
    param_id, dx, dy, ha = dim[5:9] if kind == "r" else dim[6:10]
    row = params[param_id]
    color = row_color(row)

    def at(angle, r):
        a = math.radians(angle)
        return place((center[0] + r * math.cos(a), center[1] + r * math.sin(a), center[2]))

    def unit(tip, back):
        length = math.hypot(tip[0] - back[0], tip[1] - back[1])
        return ((tip[0] - back[0]) / length, (tip[1] - back[1]) / length)

    origin = place(center)
    if kind == "r":
        tip = at(dim[4], radius)
        sheet.line([origin, tip], "DIM", color)
        sheet.arrow(tip, unit(tip, origin), color)
        prefix = "R"
    else:
        start, end = dim[4], dim[5]
        for angle in (start, end):
            sheet.line([origin, at(angle, radius + 2)], "DIM", color)
        arc = [at(start + (end - start) * i / 24, radius) for i in range(25)]
        sheet.line(arc, "DIM", color)
        sheet.arrow(arc[0], unit(arc[0], arc[1]), color)
        sheet.arrow(arc[-1], unit(arc[-1], arc[-2]), color)
        prefix = ""
    label = f"{prefix}{format_value(row)}  {param_id}{row_tag(row)}"
    sheet.text(origin[0] + dx, origin[1] + dy, label, 6.2, ha, "center", color)


def draw_dim(sheet, dim, place, params, box, scale):
    kind = dim[1]
    if kind == "d":
        draw_leader(sheet, dim, place, params, box, scale)
        return
    if kind in ("r", "a"):
        draw_arc_dim(sheet, dim, place, params)
        return
    a, b = dim[2], dim[3]
    pa, pb = place(a), place(b)
    if kind == "cl":
        sheet.line([pa, pb], "CENTER", GREY)
        return
    offset, param_id = dim[4], dim[5]
    prefix = dim[6] if len(dim) > 6 else ""
    suffix = dim[7] if len(dim) > 7 else ""
    row = params[param_id]
    color = row_color(row)
    label = f"{prefix}{format_value(row)}"
    label += f"  {param_id}{row_tag(row)}"
    if suffix:
        label += f", {suffix}"
    x0, x1, y0, y1 = box
    if kind == "h":
        y = (y1 if offset > 0 else y0) + offset
        ax_, bx_ = sorted((pa[0], pb[0]))
        for p in (pa, pb):
            sheet.line([(p[0], p[1] + math.copysign(0.8, y - p[1])), (p[0], y + math.copysign(1.2, y - p[1]))], "DIM", color)
        sheet.line([(ax_, y), (bx_, y)], "DIM", color)
        if bx_ - ax_ > 6:
            sheet.arrow((ax_, y), (-1, 0), color)
            sheet.arrow((bx_, y), (1, 0), color)
        else:
            sheet.line([(ax_ - 5, y), (bx_ + 5, y)], "DIM", color)
            sheet.arrow((ax_, y), (1, 0), color)
            sheet.arrow((bx_, y), (-1, 0), color)
        sheet.text((ax_ + bx_) / 2, y + 0.7, label, 6.2, "center", "bottom", color)
    else:
        x = (x1 if offset > 0 else x0) + offset
        ay, by = sorted((pa[1], pb[1]))
        for p in (pa, pb):
            sheet.line([(p[0] + math.copysign(0.8, x - p[0]), p[1]), (x + math.copysign(1.2, x - p[0]), p[1])], "DIM", color)
        sheet.line([(x, ay), (x, by)], "DIM", color)
        if by - ay > 6:
            sheet.arrow((x, ay), (0, -1), color)
            sheet.arrow((x, by), (0, 1), color)
        else:
            sheet.line([(x, ay - 5), (x, by + 5)], "DIM", color)
            sheet.arrow((x, ay), (0, 1), color)
            sheet.arrow((x, by), (0, -1), color)
        sheet.text(x - 0.7, (ay + by) / 2, label, 6.2, "right", "center", color, rot=90)


def third_angle_symbol(sheet, x, y):
    """ISO third-angle symbol: end view left, side view right."""
    r1, r2, w = 2.6, 1.5, 7.0
    for r in (r1, r2):
        pts = [(x + r * math.cos(t), y + r * math.sin(t)) for t in np.linspace(0, 2 * math.pi, 40)]
        sheet.line(pts, "THIN")
    sx = x + 5.5
    sheet.line([(sx, y - r2), (sx, y + r2), (sx + w, y + r1), (sx + w, y - r1), (sx, y - r2)], "THIN")


ISO_MAX = 68.0  # largest side of the isometric view on the sheet, mm
BAND_TOP = 88.0  # top of the notes and title band
SPLIT = 226.0  # left edge of the title block
STACK_TOP = 272.0  # top of the view stack; labels above it stay inside the border
STACK_BOTTOM = BAND_TOP + 17.0  # lowest edge for the stack, above its title and the band
VIEW_GAP = 28.0  # space between views, for dimensions and view titles
EXTRAS_GAP = 44.0  # wider gap before the isometric and section column
SECTION_VIEW = {"y": "front", "x": "right"}
SECTION_INSET = 12.0  # moves a section clear of the bottom view's dimensions
MARGIN_LEFT_VIEW = 22.0  # left margin when a left view is drawn
MARGIN_NO_LEFT = 42.0  # left margin otherwise, leaving room for labels


def margin_for(views):
    return MARGIN_LEFT_VIEW if "left" in views else MARGIN_NO_LEFT


def iso_scale(sizes, scale):
    return min(scale, ISO_MAX / max(sizes["iso"]))


def view_scale_for(view, sizes, scale, view_scales):
    """Sheet scale of one view. meta "view_scales" can enlarge a view: [["rear", 0.4]]."""
    if view in view_scales:
        return view_scales[view]
    return iso_scale(sizes, scale) if view == "iso" else scale


def layout_scale(sizes, views, sections, view_scales):
    """Largest standard scale that fits the views in the area above the title band."""
    area_w, extras_h = 405.0 - margin_for(views), STACK_TOP - STACK_BOTTOM + 15.0
    stack_h = STACK_TOP - STACK_BOTTOM
    gap = VIEW_GAP
    for scale in (20, 10, 5, 2, 1, 0.5, 0.2, 0.1):
        def size(v):
            s = view_scale_for(v, sizes, scale, view_scales)
            return sizes[v][0] * s, sizes[v][1] * s

        width = size("front")[0]
        for side in ("left", "right"):
            if side in views:
                width += size(side)[0] + gap
        extras = [v for v in ("iso", *sections) if v in sizes]
        if "bottom" in views:
            # Isometric beside the top view; section beside the bottom view.
            if "right" in views:
                width -= size("right")[0]
            width += max([size("right")[0] if "right" in views else 0] + [size(v)[0] + SECTION_INSET for v in extras])
        elif extras:
            width += max(size(v)[0] for v in extras) + EXTRAS_GAP
        height = size("front")[1]
        for stacked in ("top", "bottom", "rear"):
            if stacked in views:
                height += size(stacked)[1] + gap
        if "rear" in views:
            width = max(width, size("rear")[0])
        extra_h = 0 if "bottom" in views else sum(size(v)[1] for v in extras) + gap * (len(extras) - 1)
        if width <= area_w and height <= stack_h and extra_h <= extras_h:
            return scale
    raise RuntimeError("Part does not fit the sheet at any standard scale")


def scale_text(scale):
    return f"{scale:g}:1" if scale >= 1 else f"1:{1 / scale:g}"


def main_sheet(meta, params, dims, shape, variant_label, volume):
    view_names = meta["views"]
    section_specs = meta.get("sections", [])
    projected, sizes = {}, {}
    for name in view_names:
        visible, hidden = hlr(shape, name)
        projected[name] = (visible, hidden, view_axes(name))
        x0, x1, y0, y1 = bounds(visible + hidden)
        sizes[name] = (x1 - x0, y1 - y0)
    section_faces = {}
    for label, axis, position in section_specs:
        cut, faces = section_cut(shape, axis, position)
        visible, hidden = hlr(cut, SECTION_VIEW[axis])
        projected[label] = (visible, [], view_axes(SECTION_VIEW[axis]))
        section_faces[label] = faces
        x0, x1, y0, y1 = bounds(visible)
        sizes[label] = (x1 - x0, y1 - y0)

    section_names = [s[0] for s in section_specs]
    section_axis = {s[0]: s[1] for s in section_specs}
    view_scales = dict(meta.get("view_scales", []))
    scale = layout_scale(sizes, view_names, section_names, view_scales)
    sheet = Sheet()
    origin = {}
    area_top = 287.0

    def size(v):
        s = view_scale_for(v, sizes, scale, view_scales)
        return sizes[v][0] * s, sizes[v][1] * s

    # Column positions, left to right.
    gap = VIEW_GAP
    x = margin_for(view_names)
    left_w = size("left")[0] if "left" in view_names else 0
    if left_w:
        x += left_w + gap
    front_x = x
    right_x = front_x + size("front")[0] + gap
    extras_x = right_x + (size("right")[0] if "right" in view_names else -gap) + EXTRAS_GAP

    # Rows: top above front, bottom below, third-angle.
    y = STACK_TOP
    if "top" in view_names:
        y -= size("top")[1]
        origin["top"] = (front_x, y)
        y -= gap
    y -= size("front")[1]
    origin["front"] = (front_x, y)
    front_y = y
    if "bottom" in view_names:
        y -= gap + size("bottom")[1]
        origin["bottom"] = (front_x, y)
    if "rear" in view_names:
        # Below the stack and labeled, so it can carry its own scale.
        y -= gap + size("rear")[1]
        origin["rear"] = (front_x, y)
    if "left" in view_names:
        origin["left"] = (front_x - gap - size("left")[0], front_y)
    if "right" in view_names:
        origin["right"] = (right_x, front_y)
    if "bottom" in view_names:
        if "iso" in sizes:
            origin["iso"] = (right_x, area_top - size("iso")[1])
        row_top = origin["bottom"][1] + size("bottom")[1]
        for v in section_names:
            origin[v] = (right_x + SECTION_INSET, row_top - size(v)[1])
            row_top -= size(v)[1] + gap
    else:
        y = area_top
        for v in [v for v in ("iso", *section_names) if v in sizes]:
            y -= size(v)[1]
            origin[v] = (extras_x, y)
            y -= gap

    placers = {}
    for name, (visible, hidden, axes) in projected.items():
        x0, x1, y0, y1 = bounds(visible + hidden)
        ox, oy = origin[name]

        view_scale = view_scale_for(name, sizes, scale, view_scales)

        def to_sheet(p, ox=ox, oy=oy, x0=x0, y0=y0, s=view_scale):
            return (ox + (p[0] - x0) * s, oy + (p[1] - y0) * s)

        for line in hidden:
            sheet.line([to_sheet(p) for p in line], "HIDDEN")
        for line in visible:
            sheet.line([to_sheet(p) for p in line], "VISIBLE")
        if name in section_faces:
            for face in section_faces[name]:
                sheet.hatches.append([[to_sheet(p) for p in loop] for loop in face_loops(face, section_axis[name])])

        _, ax_x, ax_y = axes

        def place(p3, to_sheet=to_sheet, ax_x=ax_x, ax_y=ax_y):
            p3 = np.array(p3, dtype=float)
            return to_sheet((p3.dot(ax_x), p3.dot(ax_y)))

        placers[name] = place
        box = (ox, ox + (x1 - x0) * view_scale, oy, oy + (y1 - y0) * view_scale)
        title = {"iso": "ISOMETRIC, FOR REFERENCE"}.get(name, name.upper())
        if name in view_scales:
            title = f"{title}, SCALE {scale_text(view_scale)}"
        if name in section_faces:
            position = section_specs[section_names.index(name)][2]
            title = f"SECTION {name}-{name}, {section_axis[name].upper()} = {position:g} mm"
        sheet.text((box[0] + box[1]) / 2, oy - 4 if name == "iso" else oy - 13, title, 6.5, "center", "top", GREY, weight="bold")
        projected[name] = (visible, hidden, axes, box, view_scale)

    if "top" in placers:
        for label, axis, position in section_specs:
            x0_, x1_, y0_, y1_ = projected["top"][3]
            if axis == "x":
                # Cutting plane seen edge-on as a vertical line; arrows point at the kept half.
                x_ = placers["top"]((position, 0, 0))[0]
                sheet.line([(x_, y0_ - 7), (x_, y1_ + 7)], "CENTER", GREY)
                for y_, direction in ((y0_ - 7, 1), (y1_ + 7, -1)):
                    sheet.line([(x_, y_), (x_ - 5, y_)], "DIM")
                    sheet.arrow((x_ - 5, y_), (-1, 0))
                    sheet.text(x_ - 2.5, y_ - 1.2 * direction, label, 8, "center", "top" if direction > 0 else "bottom", weight="bold")
                continue
            y_ = placers["top"]((0, position, 0))[1]
            sheet.line([(x0_ - 7, y_), (x1_ + 7, y_)], "CENTER", GREY)
            for x_, direction in ((x0_ - 7, 1), (x1_ + 7, -1)):
                sheet.line([(x_, y_), (x_, y_ + 5)], "DIM")
                sheet.arrow((x_, y_ + 5), (0, 1))
                sheet.text(x_ - 1.2 * direction, y_ + 2.5, label, 8, "right" if direction > 0 else "left", "center", weight="bold")

    for dim in dims:
        draw_dim(sheet, dim, placers[dim[0]], params, projected[dim[0]][3], projected[dim[0]][4])

    draw_frame(sheet, meta, params, variant_label, scale, volume)
    return sheet


def fits_text(meta):
    """One line per table: 'XA: fitted by AR (XA service manual p. 4, item 22B)'."""
    parts = []
    for table, word, evidence in meta.get("fits", []):
        if word not in FIT_WORDS:
            raise RuntimeError(f"{meta['id']}: fit word {word!r} for {table} is not one of {FIT_WORDS}")
        if table not in TABLES:
            raise RuntimeError(f"{meta['id']}: {table!r} is not a table name in TABLES")
        if word != "Unconfirmed" and not evidence:
            raise RuntimeError(f"{meta['id']}: fit {word!r} for {table} needs evidence")
        parts.append(f"{table}: {fit_word(word)}" + (f" ({evidence})" if evidence else ""))
    return "; ".join(parts)


def fit_word(word):
    """'Fitted by AR' -> 'fitted by AR'."""
    return word[0].lower() + word[1:]


def mass_text(meta, volume):
    mass = volume / 1000 * meta["density"]
    text = f"{mass:.2f} g at {meta['density']:g} g/cm3, calculated from this model"
    if "reference_mass_g" in meta:
        text += f"; reported {meta['reference_mass_g']:g} g"
    if "target_mass_g" in meta:
        target = meta["target_mass_g"]
        text += f"; target {target:g} g ({meta.get('target_mass_source', 'source not given')}), model is {mass - target:+.1f} g from it"
    return text


def draw_frame(sheet, meta, params, variant_label, scale, volume):
    # Border.
    sheet.line([(8, 8), (412, 8), (412, 289), (8, 289), (8, 8)], "FRAME")
    band_top = BAND_TOP
    sheet.line([(8, band_top), (412, band_top)], "FRAME")
    split = SPLIT
    sheet.line([(split, 8), (split, band_top)], "FRAME")

    # Notes column.
    status = meta["status"]
    y = band_top - 3
    sheet.text(11, y, "NOTES", 7, "left", "top", weight="bold")
    y -= 4.2
    notes = list(meta.get("notes", []))
    notes.append("Do not scale this drawing. Use the dimensions shown, or the STEP model once its placeholders are cleared.")
    notes.append("Tolerances: none supplied by the source. Agree them with the maker before ordering.")
    for i, note in enumerate(notes, 1):
        wrapped = textwrap.wrap(note, 126)
        for j, line in enumerate(wrapped):
            sheet.text(11, y, f"{i}. {line}" if j == 0 else f"    {line}", 6.2, "left", "top")
            y -= 3.1
        y -= 0.5
    # Legend: the three kinds of dimension, each in its own colour.
    codes = {r[3] for r in params.values()}
    sheet.text(11, 11, "Dimension colours:", 6.2, "left", "bottom", GREY)
    sheet.text(36, 11, "black = from the cited source", 6.2, "left", "bottom", INK)
    sheet.text(78, 11, "blue DV = derived from sources, verify on the part", 6.2, "left", "bottom", BLUE if "DV" in codes else GREY)
    sheet.text(146, 11, "red PH = placeholder, not a measurement", 6.2, "left", "bottom", RED if "PH" in codes else GREY)
    sheet.text(200, 11, "ID and evidence: page 2", 6.2, "left", "bottom", GREY)

    # Title block.
    x0, x1 = split, 412.0
    sheet.text(x0 + 3, band_top - 3, "ACOUSTIC RESEARCH TURNTABLE RESTORATION REFERENCE", 6, "left", "top", GREY)
    title = meta["title"]
    sheet.text(x0 + 3, band_top - 7.5, title, 12, "left", "top", weight="bold")
    subtitle = variant_label or ""
    sheet.text(x0 + 3, band_top - 13.5, subtitle, 8, "left", "top")
    status_color = STATUS_MARK[status][2]
    sheet.text(x0 + 3, band_top - 18, status, 9, "left", "top", status_color, weight="bold")
    y = band_top - 22.3
    for line in textwrap.wrap(STATUS_TEXT[status], 112):
        sheet.text(x0 + 3, y, line, 6.2, "left", "top", status_color)
        y -= 3
    rows = [
        ("Part", f"{meta['part_name']}, page {meta['part']}"),
        ("Version", meta["version"]),
        ("Material", meta["material"]),
        ("Fits", fits_text(meta)),
        ("Make", meta["make"]),
        ("Scope", meta["scope"]),
        ("Est. mass", mass_text(meta, volume)),
    ]
    if "formula" in meta:
        rows.append(("Formula", meta["formula"]))
    if "final_check" in meta:
        rows.append(("Final check", meta["final_check"]))
    y -= 0.7
    for key, value in rows:
        sheet.text(x0 + 3, y, key, 6, "left", "top", GREY)
        for line in textwrap.wrap(value, 108):
            sheet.text(x0 + 19, y, line, 6.2, "left", "top", weight="bold" if key == "Final check" else "normal")
            y -= 3
        y -= 0.4
    if y < 21.5:
        raise RuntimeError(f"{meta['id']}: title block text runs into the drawing cells; shorten the metadata")
    sheet.line([(x0, 21), (x1, 21)], "THIN")
    cells = [
        ("Drawing", meta["id"]),
        ("Units", "mm unless shown"),
        ("Scale", scale_text(scale)),
        ("Rev", REVISION),
        ("Date", DRAWING_DATE),
    ]
    widths = [80, 28, 18, 12, 24]
    cx = x0
    for (label, value), width in zip(cells, widths):
        sheet.text(cx + 2, 20.3, label, 5.5, "left", "top", GREY)
        sheet.text(cx + 2, 16.6, value, 6.6, "left", "top")
        cx += width
        if cx < x1:
            sheet.line([(cx, 21), (cx, 13)], "THIN")
    sheet.line([(x0, 13), (x1, 13)], "THIN")
    sheet.text(x0 + 3, 12, "Not fit-tested. Generated from the OpenSCAD source. License: CC BY-SA 4.0.", 6.2, "left", "top")
    sheet.text(x1 - 21, 10.2, "THIRD ANGLE", 5, "right", "center", GREY)
    third_angle_symbol(sheet, x1 - 18, 10.2)


def register_sheet(meta, params, variant_label):
    sheet = Sheet()
    sheet.line([(8, 8), (412, 8), (412, 289), (8, 289), (8, 8)], "FRAME")
    sheet.text(14, 282, f"Dimension register: {meta['title']}", 12, "left", "top", weight="bold")
    sheet.text(14, 275, variant_label or meta["id"], 8, "left", "top", GREY)
    columns = [(14, "ID"), (30, "Dimension"), (150, "Value"), (205, "Evidence"), (255, "Source, or how to check")]
    y = 266
    for x, head in columns:
        sheet.text(x, y, head, 7.5, "left", "bottom", weight="bold")
    sheet.line([(14, y - 1.5), (406, y - 1.5)], "THIN")
    y -= 6
    for row in params.values():
        color = row_color(row)
        how = textwrap.wrap(row[5], 62)
        name = textwrap.wrap(row[1], 62)
        sheet.text(14, y, row[0], 7, "left", "top", color)
        for i, line in enumerate(name):
            sheet.text(30, y - i * 3.4, line, 7, "left", "top", color)
        sheet.text(150, y, format_value(row), 7, "left", "top", color)
        sheet.text(205, y, EVIDENCE[row[3]], 7, "left", "top", color)
        for i, line in enumerate(how):
            sheet.text(255, y - i * 3.4, line, 7, "left", "top", color)
        y -= max(len(how), len(name)) * 3.4 + 2.2
        if y < 14:
            raise RuntimeError(f"{meta['id']}: the register does not fit on one page")
    y -= 3
    placeholders = [r for r in params.values() if r[3] == "PH"]
    derived = [r for r in params.values() if r[3] == "DV"]
    if placeholders:
        message = f"{len(placeholders)} placeholder value(s). Do not order until each is measured; they are logged in TO-CONFIRM.md."
        color = RED
    elif derived:
        message = f"No placeholders. {len(derived)} derived value(s) to verify on a part before ordering in final material; logged in TO-CONFIRM.md."
        color = BLUE
    else:
        message = "No placeholders. Tolerances and fit still need agreeing with the maker."
        color = INK
    sheet.text(14, y, message, 8, "left", "top", color, weight="bold")
    if derived:
        y -= 5
        sheet.text(14, y, f"{len(derived)} derived value(s), shown in blue with DV: the Source column gives the derivation and how to verify it.", 7, "left", "top", BLUE)
    return sheet


def print_sheet(meta, shape, variant_label):
    """A 1:1 page: the top view outline, with the polygons in meta 'print_fills' filled black."""
    sheet = Sheet()
    sheet.line([(8, 8), (412, 8), (412, 289), (8, 289), (8, 8)], "FRAME")
    sheet.text(14, 282, f"Print at 100%: {meta['title']}", 12, "left", "top", weight="bold")
    sheet.text(14, 275, variant_label or meta["id"], 8, "left", "top", GREY)
    visible, hidden = hlr(shape, "top")
    x0, x1, y0, y1 = bounds(visible)
    cx, cy = SHEET_W / 2, 150.0
    _, ax_x, ax_y = view_axes("top")

    def place(p):
        return (cx + (p[0] - (x0 + x1) / 2), cy + (p[1] - (y0 + y1) / 2))

    for line in visible:
        sheet.line([place(p) for p in line], "VISIBLE")
    for loop in meta.get("print_fills", []):
        pts = [place((np.array([p[0], p[1], 0]).dot(ax_x), np.array([p[0], p[1], 0]).dot(ax_y))) for p in loop]
        sheet.fills.append([pts])
    # A 100 mm check bar: measure it after printing.
    bx, by = 14.0, 20.0
    sheet.line([(bx, by), (bx + 100, by)], "FRAME")
    for x in (bx, bx + 50, bx + 100):
        sheet.line([(x, by - 2), (x, by + 2)], "FRAME")
    sheet.text(bx, by + 3, "100 mm check bar: measure it after printing. If it is not 100 mm, set the printer to 100% with no fit-to-page.", 7, "left", "bottom")
    for i, note in enumerate(meta.get("print_notes", []), 1):
        sheet.text(14, by - 5 - i * 3.4, f"{i}. {note}", 6.2, "left", "top")
    return sheet


# Build one part

def validate_meta(meta, params):
    for key in ("id", "title", "status", "scope", "material", "density", "make", "part", "part_name", "version", "fits"):
        if key not in meta:
            raise RuntimeError(f"{meta.get('id', '?')}: metadata is missing {key!r}")
    if not (ROOT.parent / meta["part"]).exists():
        raise RuntimeError(f"{meta['id']}: part page {meta['part']} does not exist")
    fits_text(meta)
    codes = {r[3] for r in params.values()}
    bad = codes - set(EVIDENCE)
    if bad:
        raise RuntimeError(f"{meta['id']}: unknown evidence code(s) {sorted(bad)}")
    status = meta["status"]
    if status == "DERIVED" and ("PH" in codes or "DV" not in codes):
        raise RuntimeError(f"{meta['id']}: status DERIVED needs no PH row and at least one DV row")
    if status == "GEOMETRY COMPLETE" and codes & OPEN_CODES:
        raise RuntimeError(f"{meta['id']}: status {status} cannot have PH or DV rows")


def variant_runs(scad, tmp):
    """Yield (number, label, meta, params, dims, csg_path) for each variant of a part file."""
    probe = tmp / "probe.csg"
    meta, _, _ = read_part_data(openscad(scad, probe))
    variants = meta.get("variants", [[1, ""]])
    runs = []
    for number, label in variants:
        csg = tmp / f"{number}.csg"
        meta, params, dims = read_part_data(openscad(scad, csg, [("variant", number)]))
        validate_meta(meta, params)
        runs.append((number, label, meta, params, dims, csg))
    # Variants with their own ids get their own folders; size variants share one and take a suffix.
    own = len({run[2]["id"] for run in runs}) == len(runs)
    for number, label, meta, params, dims, csg in runs:
        stem_id = meta["id"] if own else f"{meta['id']}-{number}"
        yield number, label, meta, params, dims, csg, meta["id"], stem_id


def build_part(scad):
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        report = []
        for number, label, meta, params, dims, csg, folder, stem_id in variant_runs(scad, tmp):
            outdir = EXPORTS / folder
            outdir.mkdir(parents=True, exist_ok=True)
            prefix, watermark, color = STATUS_MARK[meta["status"]]
            stem = f"{prefix}{stem_id}"
            shape = fuse_all([s for s in (build_3d(n) for n in parse_csg(csg.read_text())) if s is not None])
            if not BRepCheck_Analyzer(shape).IsValid():
                raise RuntimeError(f"Invalid solid: {stem}")

            step = outdir / f"{stem}.step"
            stl = outdir / f"{stem}.stl"
            write_step(shape, step)
            openscad(scad, stl, [("variant", number)])

            volume = solid_volume(shape)
            mesh_volume = stl_volume(stl)
            step_volume = read_step_volume(step)
            mesh_error = abs(mesh_volume - volume) / volume
            step_error = abs(step_volume - volume) / volume
            if mesh_error > 0.01 or step_error > 1e-4:
                raise RuntimeError(f"{stem}: volume check failed, mesh {mesh_error:.3%}, step {step_error:.3%}")

            page1 = main_sheet(meta, params, dims, shape, label, volume)
            page2 = register_sheet(meta, params, label)
            with open_pdf(outdir / f"{stem}.pdf") as pdf:
                render_pdf_page(page1, pdf, watermark, color)
                render_pdf_page(page2, pdf)
                if meta.get("print_1to1"):
                    render_pdf_page(print_sheet(meta, shape, label), pdf)
            render_dxf(page1, outdir / f"{stem}-drawing.dxf")
            if meta.get("flat"):
                openscad(scad, outdir / f"{stem}-flat-1to1.dxf", [("variant", number), ("flat", "true")])

            placeholders = sum(1 for r in params.values() if r[3] == "PH")
            derived = sum(1 for r in params.values() if r[3] == "DV")
            report.append(
                f"  {stem}: {volume:.2f} mm3, {volume / 1000 * meta['density']:.2f} g, "
                f"mesh diff {mesh_error:.3%}, placeholders {placeholders}, derived {derived}"
            )
        return report


def all_parts():
    """Metadata of every variant of every part file, without building anything."""
    found = []
    for scad in sorted(PARTS.glob("*.scad")):
        with tempfile.TemporaryDirectory() as tmp:
            for number, label, meta, params, dims, csg, folder, stem_id in variant_runs(scad, Path(tmp)):
                found.append((scad, number, label, meta, params, folder, stem_id))
    return found


def open_rows(parts):
    """{id: (code, scad name)} for every PH and DV row."""
    rows = {}
    for scad, number, label, meta, params, folder, stem_id in parts:
        for row in params.values():
            if row[3] in OPEN_CODES:
                rows[row[0]] = (row[3], scad.name)
    return rows


def status_cell(meta, params):
    ph = sum(1 for r in params.values() if r[3] == "PH")
    dv = sum(1 for r in params.values() if r[3] == "DV")
    status = meta["status"]
    if status == "GEOMETRY COMPLETE":
        return "Complete"
    if status == "REFERENCE":
        return "Reference; buy it"
    if status == "DERIVED":
        return f"Derived: {dv} to verify"
    text = f"{ph} placeholder" + ("s" if ph != 1 else "")
    if dv:
        text += f", {dv} derived"
    return ("Concept: " if status == "CONCEPT" else "") + text


def readme_table(parts):
    """The drawings table of cad/README.md, one row per export folder."""
    rows = {}
    for scad, number, label, meta, params, folder, stem_id in parts:
        prefix = STATUS_MARK[meta["status"]][0]
        entry = rows.setdefault(folder, {"meta": meta, "params": params, "scad": scad.name, "stems": [], "labels": []})
        entry["stems"].append(f"{prefix}{stem_id}")
        entry["labels"].append(label)
    lines = [
        "| Part | Version | Material | Fits | Status | Drawing | Files |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    # One part's sheets together, in the order the part files give them.
    order = sorted(rows, key=lambda f: (rows[f]["meta"]["part_name"], rows[f]["scad"], list(rows).index(f)))
    for folder in order:
        entry = rows[folder]
        meta, params = entry["meta"], entry["params"]
        fits = "; ".join(f"{t}: {fit_word(w)}" for t, w, e in meta.get("fits", [])) or "Unconfirmed"
        if len(entry["stems"]) == 1:
            stem = entry["stems"][0]
            drawing = f"[PDF](exports/{folder}/{stem}.pdf)"
            files = f"[STEP](exports/{folder}/{stem}.step) · [scad](parts/{entry['scad']})"
        else:
            drawing = " · ".join(f"[{label}](exports/{folder}/{stem}.pdf)" for stem, label in zip(entry["stems"], entry["labels"]))
            files = f"[Folder](exports/{folder}/) · [scad](parts/{entry['scad']})"
        lines.append(
            f"| [{meta['part_name']}](../{meta['part']}) | {meta['version']} | {meta['material']} | {fits} | "
            f"{status_cell(meta, params)} | {drawing} | {files} |"
        )
    return "\n".join(lines)


README_START = "<!-- drawings table: written by cad/tools/build.py from the part files. Do not edit by hand. -->"
README_END = "<!-- end of drawings table -->"


def readme_with_table(table):
    text = README.read_text()
    start, end = text.index(README_START), text.index(README_END)
    return text[: start + len(README_START)] + "\n" + table + "\n" + text[end:]


def write_readme(parts):
    README.write_text(readme_with_table(readme_table(parts)))


def check():
    parts = all_parts()
    confirm = TO_CONFIRM.read_text()
    logged = {}
    for match in re.finditer(r"^\| ([A-Z]{2}\d+) \| [^|]* \| ([^|]*) \|", confirm, re.M):
        logged[match.group(1)] = match.group(2).strip()
    problems = 0
    rows = open_rows(parts)
    for key, (code, name) in sorted(rows.items()):
        if key not in logged:
            print(f"NOT LOGGED in TO-CONFIRM.md: {key} {code} ({name})")
            problems += 1
        elif code == "DV" and not logged[key].startswith("Derived:"):
            print(f"DV ROW WITHOUT 'Derived:' in TO-CONFIRM.md: {key} ({name}): value now is {logged[key]!r}")
            problems += 1
    counts = {code: sum(1 for c, _ in rows.values() if c == code) for code in OPEN_CODES}
    print(f"{counts['PH']} placeholders and {counts['DV']} derived values; {problems} problem(s)")
    if README.read_text() != readme_with_table(readme_table(parts)):
        print("cad/README.md drawings table is out of date: run build.py with no arguments")
        problems += 1
    return 1 if problems else 0


def main():
    # ezdxf orders some objects by Python's hash seed, so fix the seed: an
    # unchanged part then gives an unchanged DXF.
    if os.environ.get("PYTHONHASHSEED") != "0":
        os.execve(sys.executable, [sys.executable] + sys.argv, {**os.environ, "PYTHONHASHSEED": "0"})
    args = sys.argv[1:]
    if args == ["--check"]:
        return check()
    names = args or [p.stem for p in sorted(PARTS.glob("*.scad"))]
    for name in names:
        scad = PARTS / f"{name}.scad"
        print(name)
        for line in build_part(scad):
            print(line)
    write_readme(all_parts())
    return 0


if __name__ == "__main__":
    sys.exit(main())
