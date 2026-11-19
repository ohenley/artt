#!/usr/bin/env python3
"""Check the three ARTT boards and export what a reader or a board house needs.

Run from the pcb/ folder:

    python3 tools/check.py

For each project it does four things:
1. exports the netlist from the schematic and compares it, pad by pad, with the board;
2. runs KiCad's design rule check on the board and writes drc-report.txt;
3. exports the schematic as PDF and the board as SVG and PNG previews into docs/
   (PNG only if rsvg-convert is installed);
4. exports Gerber and drill files into fab/.

It exits with an error if the schematic and the board disagree, or if the
design rule check reports an error or an unconnected pad.
"""
import os
import re
import shutil
import subprocess
import sys

import pcbnew

PCB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECTS = [("power-board", "artt-power-board"),
            ("audio-strip-board", "artt-audio-strip-board"),
            ("rear-jack-panel", "artt-rear-jack-panel")]


def run(*cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout, r.stderr)
        raise SystemExit("command failed: " + " ".join(cmd))
    return r.stdout


def schematic_nets(sch, tmp):
    run("kicad-cli", "sch", "export", "netlist", "-o", tmp, sch)
    text = open(tmp).read()
    nets = {}
    for m in re.finditer(r'\(net \(code "?\d+"?\) \(name "([^"]*)"\)(.*?)(?=\(net \(code|\Z)', text, re.S):
        for n in re.finditer(r'\(node \(ref "([^"]+)"\) \(pin "([^"]+)"\)', m.group(2)):
            nets[(n.group(1), n.group(2))] = m.group(1)
    os.remove(tmp)
    return nets


def board_nets(board):
    nets = {}
    for fp in board.GetFootprints():
        for pad in fp.Pads():
            if pad.GetNumber() and pad.GetNetname():
                nets[(fp.GetReference(), pad.GetNumber())] = pad.GetNetname()
    return nets


def main():
    bad = False
    for folder, name in PROJECTS:
        d = os.path.join(PCB, folder)
        sch = os.path.join(d, name + ".kicad_sch")
        pcb = os.path.join(d, name + ".kicad_pcb")
        docs = os.path.join(d, "docs")
        fab = os.path.join(d, "fab")
        os.makedirs(docs, exist_ok=True)
        os.makedirs(fab, exist_ok=True)
        print("==", name)

        s = schematic_nets(sch, os.path.join(d, "tmp.net"))
        board = pcbnew.LoadBoard(pcb)
        b = board_nets(board)
        if s == b:
            print("   schematic and board agree: %d pads on %d nets" % (len(s), len(set(s.values()))))
        else:
            bad = True
            for k in sorted(set(s) | set(b)):
                if s.get(k) != b.get(k):
                    print("   MISMATCH %s pin %s: schematic %s, board %s" % (k[0], k[1], s.get(k), b.get(k)))

        report = os.path.join(d, "drc-report.txt")
        pcbnew.WriteDRCReport(board, report, pcbnew.EDA_UNITS_MILLIMETRES, True)
        text = open(report).read().replace(PCB + os.sep, "pcb/")
        text = re.sub(r"\*\* Created on .*? \*\*\n", "", text)
        open(report, "w").write(text)
        counts = re.findall(r"\*\* Found (\d+) (DRC violations|unconnected pads|Footprint errors) \*\*", text)
        errors = len(re.findall(r"Severity: error", text))
        warnings = len(re.findall(r"Severity: warning", text))
        print("   design rule check: %s; %d errors, %d warnings" % (", ".join("%s %s" % c for c in counts), errors, warnings))
        unconnected = int(dict((c[1], c[0]) for c in counts).get("unconnected pads", 0))
        if errors or unconnected:
            bad = True

        run("kicad-cli", "sch", "export", "pdf", "-o", os.path.join(docs, name + "-schematic.pdf"), sch)
        run("kicad-cli", "pcb", "export", "svg", "--page-size-mode", "2", "--exclude-drawing-sheet",
            "-l", "B.Cu,F.Cu,F.SilkS,Cmts.User,Dwgs.User,Edge.Cuts" + (",F.Fab" if "panel" in name else ""), "-o", os.path.join(docs, name + "-top.svg"), pcb)
        run("kicad-cli", "pcb", "export", "svg", "--page-size-mode", "2", "--exclude-drawing-sheet", "--mirror",
            "-l", "B.Cu,B.SilkS,Edge.Cuts", "-o", os.path.join(docs, name + "-bottom.svg"), pcb)
        if shutil.which("rsvg-convert"):
            for side in ("top", "bottom"):
                base = os.path.join(docs, "%s-%s" % (name, side))
                run("rsvg-convert", "-b", "white", "-z", "4", base + ".svg", "-o", base + ".png")
        run("kicad-cli", "pcb", "export", "gerbers", "-o", fab + "/",
            "-l", "F.Cu,B.Cu,F.SilkS,B.SilkS,F.Mask,B.Mask,Edge.Cuts", pcb)
        run("kicad-cli", "pcb", "export", "drill", "-o", fab + "/", "--excellon-separate-th", pcb)
    if bad:
        raise SystemExit("CHECK FAILED")
    print("all checks passed")


if __name__ == "__main__":
    main()
