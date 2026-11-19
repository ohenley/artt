#!/usr/bin/env python3
"""Draw the plain-language diagrams used by docs/what-goes-where.md and the wiring pages.

Run with the packages in requirements.txt. Output goes to docs/images/: PNG for the
older diagrams, SVG for the wiring diagrams. Only the hardware-set sizes are true to
the source; the others are schematic.
License: MIT, see LICENSE in this directory.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle

OUT = Path(__file__).resolve().parents[2] / "docs" / "images"
INK = "#222222"
GREY = "#777777"
ACCENT = "#c0392b"
SHELL = "#d9dde2"
CART = "#b9c7d6"
WOOD = "#d2a679"
BRASS = "#d4b24c"
METAL = "#9aa3ab"
FONT = 10


def rect(ax, x, y, w, h, color, **kw):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=color, edgecolor=kw.pop("edge", INK), linewidth=kw.pop("lw", 1.0), **kw))


def note(ax, text, xy, xytext, color=INK, ha="left"):
    ax.annotate(
        text, xy=xy, xytext=xytext, fontsize=FONT, color=color, ha=ha, va="center",
        arrowprops=dict(arrowstyle="-|>", color=color, lw=0.9, shrinkA=2, shrinkB=0),
    )


def setup(ax, title, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=12, fontweight="bold", color=INK, pad=8)


def screw(ax, x, top, bottom, head_at_top, head_w=2.6, head_h=1.1, d=1.0):
    """A vertical screw. The head is at the top or the bottom of the shank."""
    rect(ax, x - d / 2, bottom, d, top - bottom, METAL, lw=0.8, zorder=5)
    y = top if head_at_top else bottom - head_h
    rect(ax, x - head_w / 2, y, head_w, head_h, METAL, lw=0.8, zorder=6)


def mounting():
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 6.4))

    # Left: the original AR arrangement.
    ax = axes[0]
    setup(ax, "Original AR way: 2 screws go UP from below", (-9, 45), (-13, 19))
    rect(ax, 0, 11, 30, 2.4, SHELL)
    rect(ax, 0, 4.5, 1.6, 6.6, SHELL)
    rect(ax, 28.4, 4.5, 1.6, 6.6, SHELL)
    rect(ax, 30, 6.5, 6, 3.2, SHELL)
    ax.text(15, 14.2, "AR plastic shell", ha="center", fontsize=FONT, color=INK)
    ax.text(38.2, 8.1, "to\narm", ha="left", va="center", fontsize=FONT, color=GREY)

    rect(ax, 14.2, 8.2, 2.6, 2.8, BRASS)  # stud
    rect(ax, 14.1, 6.5, 2.8, 1.7, "#8fb98f")  # bushing
    rect(ax, 5, -1, 20, 7.5, CART)  # cartridge
    rect(ax, 5.5, 6.5, 5, 1.8, "#c9b28f", hatch="////")  # shim at the front
    ax.text(9.5, 1.5, "cartridge", ha="center", fontsize=FONT, color=INK)
    screw(ax, 15.5, 9.8, 3.0, head_at_top=False)
    ax.plot([4.5, 0.6], [-1, -5.4], color=INK, lw=2)
    ax.plot([0.6], [-5.4], "v", color=INK, ms=6)

    note(ax, "threaded stud in the shell\n(2, one each side)", (16.8, 9.4), (32, 15.6))
    note(ax, "standoff bushing, if your\ncartridge needs one", (16.9, 7.2), (23, -5.7))
    note(ax, "1 of the 4 screw lengths,\nthrough the cartridge's ear", (14.4, 2.2), (9, -9.2), ha="left")
    note(ax, "shim block, only if\nthe sheet calls for one", (6.5, 7.6), (-8.5, 14.5))
    ax.text(-4, -6.8, "stylus", fontsize=FONT, color=INK, ha="left")

    # Right: the PMMA shell with a Grado Master4.
    ax = axes[1]
    setup(ax, "Your Grado Master4 plan: 2 screws go DOWN from the top", (-9, 45), (-13, 19))
    rect(ax, 0, 8, 30, 3.5, "#cfe7ee", edge="#2a6f85")
    rect(ax, 0, 2, 2.2, 6, "#cfe7ee", edge="#2a6f85")
    rect(ax, 26, 2, 4, 6, "#cfe7ee", edge="#2a6f85")
    rect(ax, 30, 4, 6, 4, "#cfe7ee", edge="#2a6f85")
    ax.text(38.2, 6, "to\narm", ha="left", va="center", fontsize=FONT, color=GREY)
    rect(ax, 13.4, 10.4, 4.2, 1.1, "white", edge="#2a6f85", lw=0.8, zorder=3)  # recess
    rect(ax, 14.2, 8, 2.6, 2.4, "white", edge="#2a6f85", lw=0.8, zorder=3)  # slot
    rect(ax, 3.5, -2.5, 21, 10.5, WOOD)
    ax.text(10, 1.5, "Grado Master4\n(wood body,\nthreaded holes)", ha="center", va="center", fontsize=FONT, color=INK)
    screw(ax, 15.5, 10.4, 3.2, head_at_top=True, head_w=3.4, head_h=1.0)
    ax.plot([3, -0.6], [-2.5, -6.4], color=INK, lw=2)
    ax.plot([-0.6], [-6.4], "v", color=INK, ms=6)

    note(ax, "Grado's own screw,\nfrom the top", (16.5, 11.3), (22, 16.6))
    note(ax, "slot and recess milled\nin the PMMA shell", (14.1, 9.4), (-8.5, 15))
    note(ax, "thread is in the cartridge body:\nno studs, no AR screws", (16.0, 4.6), (12, -8.6))
    ax.text(-5.5, -8.1, "stylus", fontsize=FONT, color=INK, ha="left")

    fig.text(0.5, 0.02, "Side views, front of the shell at left. Schematic, not to scale. Left panel follows AR sheet L-1591; right panel is a concept, not fit-tested.",
             ha="center", fontsize=9, color=GREY)
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    fig.savefig(OUT / "cartridge-mounting.png", dpi=130, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)


def hardware_set():
    """True relative sizes from the RDW drawing, in inches."""
    fig, ax = plt.subplots(figsize=(13, 5.6))
    setup(ax, "The AR hardware bag: you use 1 pair of screws, and the rest stays in the bag", (-0.15, 3.75), (-0.98, 0.33))
    x = 0.15
    for i, length in enumerate((0.183, 0.356, 0.462, 0.612), 1):
        rect(ax, x - 0.05, -length, 0.1, length, METAL)
        rect(ax, x - 0.09, 0, 0.18, 0.06, METAL)
        ax.text(x, -length - 0.05, f"#{i}\n{length} in\n2 of these", ha="center", va="top", fontsize=FONT)
        x += 0.36
    ax.text(0.69, 0.14, "#3-48 aluminum screws: pick one length", ha="center", fontsize=FONT, fontweight="bold")

    x = 1.72
    for i, height in enumerate((0.050, 0.100, 0.150), 1):
        rect(ax, x - 0.09, -height, 0.18, height, "#8fb98f")
        ax.text(x, -height - 0.05, f"#{i}\n{height:.3f} in\n2 of these", ha="center", va="top", fontsize=FONT)
        x += 0.32
    ax.text(2.04, 0.14, "standoff bushings, 0.180 in wide", ha="center", fontsize=FONT, fontweight="bold")
    ax.text(2.04, 0.06, "add height when the table says so", ha="center", fontsize=9, color=GREY)

    x = 2.68
    for i, thick in enumerate((0.045, 0.080, 0.125), 1):
        y = -0.1 - (i - 1) * 0.27
        rect(ax, x, y - thick, 0.805, thick, "#c9b28f", hatch="////")
        ax.text(x + 0.40, y - thick - 0.018, f"#{i}, {thick:.3f} in thick", ha="center", va="top", fontsize=FONT)
    ax.text(3.08, 0.14, "shim blocks, 0.805 in long", ha="center", fontsize=FONT, fontweight="bold")
    ax.text(3.08, 0.06, "tilt the cartridge's front end", ha="center", fontsize=9, color=GREY)

    rect(ax, 1.70, -0.78, 0.112, 0.125, BRASS)
    ax.text(1.85, -0.72, "#4-40 brass set screw,\n0.125 in. 1 in the set.\nWhere it goes: unconfirmed.", va="center", fontsize=FONT, color=ACCENT)
    ax.text(1.8, -0.93, "Sizes are to scale with each other. Screw heads are illustrative. Source: RDW community drawing, 2023.", ha="center", fontsize=9, color=GREY)
    fig.tight_layout()
    fig.savefig(OUT / "hardware-set.png", dpi=130, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)


def overhang():
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.8))

    # Left: what overhang is.
    ax = axes[0]
    setup(ax, "Overhang: how far the needle reaches past the spindle", (-9.5, 12.2), (-6.9, 6.3))
    ax.add_patch(Circle((0, 0), 5.9, facecolor="#eeeeee", edgecolor=GREY, lw=1))
    ax.add_patch(Circle((0, 0), 0.14, facecolor=INK, edgecolor=INK))
    ax.text(0, 4.7, "record", ha="center", fontsize=FONT, color=GREY)
    pivot = (8.31, 0)
    tip = (-0.688, 0)
    ax.plot([pivot[0], tip[0]], [0, 0], color=METAL, lw=5, solid_capstyle="round")
    ax.add_patch(Circle(pivot, 0.45, facecolor=METAL, edgecolor=INK))
    ax.add_patch(Circle(tip, 0.09, facecolor=ACCENT, edgecolor=ACCENT, zorder=6))
    ax.text(8.31, 0.95, "arm pivot", ha="center", fontsize=FONT)
    note(ax, "needle", tip, (-5.4, -3.2), color=ACCENT)
    note(ax, "spindle (record's center)", (0, 0), (-1.6, -3.9))
    ax.annotate("", xy=(tip[0], 1.3), xytext=(0, 1.3), arrowprops=dict(arrowstyle="<->", color=ACCENT, lw=1.2))
    ax.plot([tip[0], tip[0]], [0.1, 1.45], color=ACCENT, lw=0.7)
    ax.plot([0, 0], [0.15, 1.45], color=ACCENT, lw=0.7)
    ax.text(-0.34, 2.45, "overhang\n0.688 in\n(17.48 mm)", ha="center", va="center", fontsize=FONT, color=ACCENT, fontweight="bold")
    ax.annotate("", xy=(0, -1.4), xytext=(pivot[0], -1.4), arrowprops=dict(arrowstyle="<->", color=INK, lw=0.8))
    ax.text(4.2, -1.95, "pivot to needle is 9 in, so pivot to spindle is about 8.3 in", ha="center", fontsize=9)
    ax.text(1.3, -6.6, "Arm swung over the spindle only to show the geometry.", ha="center", fontsize=9, color=GREY)

    # Right: the gauge.
    ax = axes[1]
    setup(ax, "The gauge: a strip with 2 holes that checks that distance", (-4.2, 9.5), (-3.1, 3.6))
    rect(ax, -1.5, -0.9, 6.5, 1.8, "#cfe7ee", edge="#2a6f85")
    ax.add_patch(Circle((0, 0), 0.5, facecolor="#555555", edgecolor=INK))
    ax.add_patch(Circle((3.0, 0), 0.12, facecolor="white", edgecolor=ACCENT, lw=1.4))
    note(ax, "big hole drops over\nthe spindle", (0, 0.5), (-4, 2.4))
    note(ax, "needle goes in the small hole.\nIf it lands there, overhang is right.", (3.0, 0.14), (2.0, 2.4), color=ACCENT)
    ax.annotate("", xy=(0, -1.25), xytext=(3.0, -1.25), arrowprops=dict(arrowstyle="<->", color=ACCENT, lw=1.2))
    ax.text(1.5, -1.72, "0.688 in center to center", ha="center", fontsize=FONT, color=ACCENT, fontweight="bold")
    ax.text(2.5, -2.6, "Only this one distance matters. AR's own gauge may look different; its outline has not been found.", ha="center", fontsize=9, color=GREY)

    fig.tight_layout()
    fig.savefig(OUT / "overhang.png", dpi=130, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)


def grounding():
    """Proposed scheme for the IEC inlet mod. Schematic; not built or tested."""
    fig, ax = plt.subplots(figsize=(12, 6.2))
    setup(ax, "Proposed ground scheme: one star point, nothing else bridged", (0, 100), (2, 58))

    def box(x, y, w, h, text, color="#eef1f4"):
        rect(ax, x, y, w, h, color)
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=FONT)

    def wire(points, color=INK, style="-", lw=2.0):
        xs, ys = zip(*points)
        ax.plot(xs, ys, color=color, linestyle=style, linewidth=lw, solid_capstyle="round")

    box(3, 42, 19, 11, "IEC inlet\nearth pin", "#f6dedb")
    box(34, 42, 22, 11, "Metal top plate")
    box(38, 18, 24, 12, "GROUND POST\nstar point", "#fbeeb8")
    box(3, 18, 19, 11, "Arm ground braid\nand T-bar")
    box(76, 5, 21, 48, "Phono stage", "#dcecdc")
    box(38, 5, 24, 7, "L and R jacks, insulated")

    wire([(22, 47.5), (34, 47.5)], ACCENT)
    ax.text(28, 49, "mains earth", ha="center", fontsize=9, color=ACCENT)
    wire([(50, 42), (50, 30)])
    ax.text(51, 36, "one link only", ha="left", fontsize=9)
    wire([(22, 24), (38, 24)])
    ax.text(30, 25.3, "signal ground", ha="center", fontsize=9)
    wire([(62, 24), (76, 24)], style="--")
    ax.text(69, 25.3, "ground lead:", ha="center", fontsize=9)
    ax.text(69, 21.3, "test on and off", ha="center", fontsize=9)
    wire([(62, 8.5), (76, 8.5)], GREY, lw=1.2)
    ax.text(69, 9.8, "interconnects", ha="center", fontsize=9, color=GREY)
    fig.text(0.5, 0.015, "Schematic. Proposed, not built or tested. Never lift mains earth to cure hum. L and R grounds meet only at the phono stage.",
             ha="center", fontsize=9, color=GREY)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(OUT / "grounding-scheme.png", dpi=130, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)




# ---------------------------------------------------------------------------
# Wiring diagrams, as SVG. One subject per drawing: power, audio, or ground.
# The facts drawn here are cited on docs/wiring/README.md and the model pages;
# a dashed line is a connection that no held source draws.

matplotlib.rcParams["svg.fonttype"] = "none"
matplotlib.rcParams["font.family"] = "sans-serif"
matplotlib.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica", "sans-serif"]

MAINS = "#b03a2e"
LEFT = "#1f5f8b"
RIGHT = "#b03a2e"
GND = "#4f5b62"
NOTE = "#555555"
UNSURE = (0, (4, 3))


def sheet(title, w=10.0, h=5.6, xlim=(0, 106), ylim=(0, 62)):
    fig, ax = plt.subplots(figsize=(w, h))
    setup(ax, title, xlim, ylim)
    return fig, ax


def save_svg(fig, name, footer):
    fig.text(0.5, 0.01, footer, ha="center", va="bottom", fontsize=8.2, color=NOTE, wrap=True)
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    fig.savefig(OUT / f"{name}.svg", format="svg", bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)


def box(ax, x, y, w, h, text, color="#eef1f4", fs=FONT, ls="-", edge=INK):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=color, edgecolor=edge, linewidth=1.0, linestyle=ls, zorder=2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=INK, zorder=3)


def wire(ax, pts, color=INK, ls="-", lw=1.8):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=color, linestyle=ls, linewidth=lw, solid_capstyle="round", zorder=4)


def dot(ax, x, y, color=INK):
    ax.add_patch(Circle((x, y), 0.55, facecolor=color, edgecolor=color, zorder=5))


def label(ax, x, y, text, color=INK, ha="center", va="bottom", fs=None):
    ax.text(x, y, text, ha=ha, va=va, fontsize=fs or FONT - 1, color=color, zorder=6)


def cap(ax, x, y, color=INK, ls="-"):
    """Capacitor symbol on a horizontal wire centred at x, y."""
    wire(ax, [(x - 2.4, y), (x - 0.7, y)], color, ls)
    wire(ax, [(x + 0.7, y), (x + 2.4, y)], color, ls)
    ax.plot([x - 0.7, x - 0.7], [y - 1.8, y + 1.8], color=color, lw=1.8, zorder=4)
    ax.plot([x + 0.7, x + 0.7], [y - 1.8, y + 1.8], color=color, lw=1.8, zorder=4)


def fuse(ax, x, y, w, color=INK):
    ax.add_patch(Rectangle((x, y - 1.3), w, 2.6, facecolor="white", edgecolor=color, linewidth=1.4, zorder=4))
    ax.plot([x, x + w], [y, y], color=color, lw=1.2, zorder=5)


def switch(ax, x, y, w, color=INK):
    ax.add_patch(Circle((x, y), 0.5, facecolor="white", edgecolor=color, zorder=5))
    ax.add_patch(Circle((x + w, y), 0.5, facecolor="white", edgecolor=color, zorder=5))
    ax.plot([x + 0.4, x + w - 1.2], [y + 0.3, y + 3.0], color=color, lw=1.8, zorder=5)


def coil(ax, x0, x1, y, color=INK, n=5):
    import numpy as np
    t = np.linspace(0, 1, 80)
    xs = x0 + (x1 - x0) * t
    ys = y + 1.4 * np.abs(np.sin(np.pi * n * t))
    ax.plot(xs, ys, color=color, lw=1.6, zorder=4)


def cross(ax, x, y, color=ACCENT):
    ax.plot([x - 1.2, x + 1.2], [y - 1.2, y + 1.2], color=color, lw=2.2, zorder=7)
    ax.plot([x - 1.2, x + 1.2], [y + 1.2, y - 1.2], color=color, lw=2.2, zorder=7)


# ---- power ----------------------------------------------------------------

def power_front_end(ax, spec):
    """The modded part: inlet, fuse, switch with its capacitor, earth to the plate."""
    box(ax, 2, 22, 14, 27, "IEC inlet\nfused", "#f6dedb")
    for y, name in ((44, "line"), (35, "neutral"), (26, "earth")):
        wire(ax, [(16, y), (19, y)], MAINS if name != "earth" else "#2e7d32")
        label(ax, 17.5, y + 0.6, name, NOTE, fs=8)
    wire(ax, [(19, 44), (22, 44)], MAINS)
    fuse(ax, 22, 44, 8, MAINS)
    label(ax, 26, 41.6, spec["fuse"], MAINS, va="top", fs=8.2)
    wire(ax, [(30, 44), (36, 44)], MAINS)
    dot(ax, 34, 44, MAINS)
    switch(ax, 36, 44, 8, MAINS)
    label(ax, 40, 48.4, spec["switch"], INK, fs=8.5)
    wire(ax, [(44, 44), (48, 44)], MAINS)
    dot(ax, 48, 44, MAINS)
    # capacitor across the switch
    wire(ax, [(34, 44), (34, 36), (38.6, 36)], MAINS, spec.get("c2_ls", "-"))
    cap(ax, 41, 36, MAINS, spec.get("c2_ls", "-"))
    wire(ax, [(43.4, 36), (48, 36), (48, 44)], MAINS, spec.get("c2_ls", "-"))
    label(ax, 41, 32.6, spec["c2"], INK, va="top", fs=8.5)
    # neutral and earth
    wire(ax, [(19, 35), (21, 35), (21, 10), (92, 10)], MAINS, spec.get("n_ls", "-"))
    wire(ax, [(19, 26), (19, 4), (40, 4)], "#2e7d32")
    dot(ax, 40, 4, "#2e7d32")
    ax.plot([40, 62], [3.2, 3.2], color=METAL, lw=5, solid_capstyle="butt", zorder=3)
    label(ax, 51, 4.6, "metal top plate: ring lug and star washer under a plate screw", "#2e7d32", fs=8.5)


def power_motor(ax, spec):
    """The stock motor circuit after the switch, as the model page states it."""
    ls = spec.get("motor_ls", "-")
    wire(ax, [(48, 44), (54, 44)], MAINS, ls)
    dot(ax, 54, 44, MAINS)
    wire(ax, [(54, 44), (57.6, 44)], MAINS, ls)
    cap(ax, 60, 44, MAINS, ls)
    wire(ax, [(62.4, 44), (70, 44)], MAINS, ls)
    label(ax, 59, 46.6, spec["c1"], INK, fs=8.2)
    wire(ax, [(54, 44), (54, 33), (70, 33)], MAINS, ls)
    box(ax, 70, 26, 18, 30, "", "#f7f7f7")
    label(ax, 79, 52.6, spec["motor"], INK, fs=8.5)
    coil(ax, 73, 85, 44, MAINS)
    coil(ax, 73, 85, 33, MAINS)
    wire(ax, [(70, 44), (73, 44)], MAINS, ls)
    wire(ax, [(70, 33), (73, 33)], MAINS, ls)
    wire(ax, [(85, 44), (92, 44)], MAINS, ls)
    wire(ax, [(85, 33), (92, 33)], MAINS, ls)
    wire(ax, [(92, 33), (92, 10)], MAINS, spec.get("n_ls", "-"))
    wire(ax, [(92, 44), (92, 33)], MAINS, spec.get("return_ls", ls))
    dot(ax, 92, 33, MAINS)
    for (x, y, text, ha) in spec["leads"]:
        label(ax, x, y, text, INK, ha=ha, fs=8.2)
    label(ax, 56, 21, spec.get("motor_note", ""), NOTE, ha="left", va="center", fs=7.8)
    label(ax, 72, 11.2, spec.get("neutral_note", "stock neutral point"), NOTE, fs=8)


def power_generic():
    fig, ax = sheet("Power, modded: inlet and fuse feed the stock switch circuit")
    spec = dict(fuse="fuse: value from the motor label", switch="stock switch", c2="stock capacitor across the switch")
    power_front_end(ax, spec)
    wire(ax, [(48, 44), (56, 44)], MAINS)
    box(ax, 56, 30, 32, 20, "stock motor circuit,\nunchanged:\nsee the model page", "#f7f7f7")
    wire(ax, [(88, 40), (92, 40), (92, 10)], MAINS)
    label(ax, 72, 11.2, "stock neutral point", NOTE, fs=8)
    save_svg(fig, "wiring-power",
             "Mains voltage is present on the switch and on both capacitors. Unplug before opening. Only the inlet, the fuse and the earth wire are new.")


def power_xa():
    fig, ax = sheet("XA power, modded: 120 V circuit from the service manual, inlet and fuse added")
    spec = dict(
        fuse="fuse: value not known, row IE1",
        switch="stock switch",
        c2="switch capacitor C-2: 0.022 µF, 600 V DC",
        c1="motor capacitor C-1\n0.1 µF, 600 V DC",
        motor="motor, four leads",
        leads=[(69.3, 45.0, "red", "right"), (69.3, 34.0, "white", "right"), (92.8, 45.0, "white", "left"), (92.8, 34.2, "green", "left")],
        motor_note="lead colours for serials XA176235 to XA204462:\ngray, blue, red, gray, in the same order",
        return_ls=UNSURE,
    )
    power_front_end(ax, spec)
    power_motor(ax, spec)
    label(ax, 93.5, 39, "join as read\non the schematic,\nrow EL11", NOTE, ha="left", va="center", fs=7.6)
    save_svg(fig, "xa-wiring-power",
             "Factory circuit: XA service manual, p. 3, 120 V. Values for 220 V differ. Dashed: the return of the first winding, read from the schematic. Mains voltage on the switch and both capacitors.")


def power_xb():
    fig, ax = sheet("XB power, modded: the parts on drawing 119, inlet and fuse added")
    spec = dict(
        fuse="fuse: value not known, row IE1",
        switch="switch 802004",
        c2="switch capacitor 803004, item 46:\nvalue not on the drawing, row EL4",
        c1="motor capacitor 803002, item 44\nvalue not on the drawing, row EL4",
        motor="motor 802006, item 40",
        leads=[],
        motor_note="lead colours: not on the drawing.\nFour crimp nuts 500018, item 47.\nYellow wire 602006 and black wire 602004\nrun to the switch; which one is line\nis not on the drawing",
        motor_ls=UNSURE, c2_ls=UNSURE,
    )
    power_front_end(ax, spec)
    power_motor(ax, spec)
    save_svg(fig, "xb-wiring-power",
             "Parts and part numbers: drawing 119. Dashed: the circuit itself is not drawn on any held XB document and follows the XA pattern, row EL14. Mains voltage on the switch and both capacitors.")


def power_ar77xb():
    fig, ax = sheet("AR77XB power: XB pattern, to confirm on the table. Inlet and fuse added")
    spec = dict(
        fuse="fuse: value not known, row IE1",
        switch="switch: to read",
        c2="switch capacitor: value to read, row EL5",
        c1="motor capacitor:\nvalue to read, row EL5",
        motor="motor: to read, row EL5",
        leads=[],
        motor_note="lead count and colours: to read on the table",
        motor_ls=UNSURE, c2_ls=UNSURE, n_ls=UNSURE,
    )
    power_front_end(ax, spec)
    power_motor(ax, spec)
    save_svg(fig, "ar77xb-wiring-power",
             "No factory wiring source exists for the AR77XB. Everything dashed is the XB pattern and must be read on the table before any wire is cut. Mains voltage on the switch and both capacitors.")


# ---- audio ----------------------------------------------------------------

LUG_Y = (48, 41, 34, 27, 20)
TARGETS = {
    "left centre": (47, LEFT), "left sleeve": (42, LEFT),
    "right centre": (29, RIGHT), "right sleeve": (24, RIGHT),
    "ground post": (9, GND),
}


def audio_frame(ax, title_left="from the arm", title_right="to the jacks in the plinth"):
    box(ax, 44, 15, 6, 38, "", "#e2e6ea")
    for i, y in enumerate(LUG_Y, 1):
        ax.add_patch(Rectangle((45.9, y - 1.1), 2.2, 2.2, facecolor=METAL, edgecolor=INK, lw=0.8, zorder=3))
        label(ax, 47, y + 1.4, f"lug {i}", INK, fs=7.5)
        wire(ax, [(40, y), (44, y)], INK, lw=1.4)
        wire(ax, [(50, y), (54, y)], INK, lw=1.4)
    label(ax, 47, 54.2, "terminal strip", INK, fs=9)
    label(ax, 20, 56.5, title_left, INK, fs=9)
    label(ax, 80, 56.5, title_right, INK, fs=9)
    for name, y0, y1, colour in (("left jack, insulated", 39, 51, LEFT), ("right jack, insulated", 21, 33, RIGHT)):
        box(ax, 80, y0, 18, y1 - y0, name, "#f7f7f7", fs=8.5)
        wire(ax, [(78, y1 - 4), (80, y1 - 4)], colour, lw=1.4)
        wire(ax, [(78, y0 + 3), (80, y0 + 3)], colour, lw=1.4)
        label(ax, 80.4, y1 - 4 + 0.5, "centre", NOTE, ha="left", fs=7.5)
        label(ax, 80.4, y0 + 3 + 0.5, "sleeve", NOTE, ha="left", fs=7.5)
    box(ax, 80, 5, 18, 8, "ground post", "#fbeeb8", fs=8.5)
    wire(ax, [(78, 9), (80, 9)], GND, lw=1.4)


def audio_route(ax, lug, target, k, ls="-"):
    y0 = LUG_Y[lug - 1]
    y1, colour = TARGETS[target]
    xch = 58 + 3.2 * k
    wire(ax, [(54, y0), (xch, y0), (xch, y1), (78, y1)], colour, ls, lw=1.6)


def audio_page(name, title, lugs, footer, arm_header="from the arm"):
    """lugs: five tuples (arm wire, role, target or None, line style)."""
    fig, ax = sheet(title)
    audio_frame(ax, arm_header)
    for i, (arm, role, target, ls) in enumerate(lugs, 1):
        y = LUG_Y[i - 1]
        label(ax, 39, y + 0.5, arm, INK, ha="right", fs=8.5)
        label(ax, 39, y - 0.6, role, NOTE, ha="right", va="top", fs=7.5)
        if target:
            audio_route(ax, i, target, i - 1, ls)
    label(ax, 66, 2.5, "each channel: one short twisted pair, signal to the centre, ground to the sleeve", NOTE, fs=8)
    save_svg(fig, name, footer)


def audio_generic():
    lugs = [("left signal", "", "left centre", "-"), ("left ground", "", "left sleeve", "-"),
            ("right signal", "", "right centre", "-"), ("right ground", "", "right sleeve", "-"),
            ("arm shield", "", "ground post", "-")]
    audio_page("wiring-audio", "Audio, modded: strip lugs to two insulated jacks and the ground post", lugs,
               "The lug order is the model's, not this one: see the model page. Find each wire with an ohmmeter from the shell pin before soldering.",
               arm_header="from the arm (order differs by model)")


def audio_xa():
    lugs = [("green", "left ground", "left sleeve", "-"),
            ("yellow, pink or blue", "left signal", "left centre", "-"),
            ("red", "right signal", "right centre", "-"),
            ("copper", "right ground", "right sleeve", "-"),
            ("shield", "arm shield", "ground post", "-")]
    audio_page("xa-wiring-audio", "XA audio, modded: the five strip lugs of the service manual, p. 4", lugs,
               "Arm wire colours and lug order: XA service manual, p. 4, as read from the drawing, row EL13. Roles from the cable side labels on the same drawing and AR's shell code. Check every lug with the ohmmeter.")


def audio_xb():
    lugs = [("silver", "arm shield (proposed)", "ground post", UNSURE),
            ("copper", "right ground (proposed)", "right sleeve", UNSURE),
            ("red", "right signal (proposed)", "right centre", UNSURE),
            ("blue", "left signal (proposed)", "left centre", UNSURE),
            ("green", "left ground (proposed)", "left sleeve", UNSURE)]
    audio_page("xb-wiring-audio", "XB audio, modded: the five strip lugs of drawing 119", lugs,
               "Arm wire colours and lug order: drawing 119 wiring detail. Dashed: the channel of each lug is not printed on the drawing; the reading is Unconfirmed, row EL12. The ohmmeter settles it.")


def audio_ar77xb():
    lugs = [("to read", "", None, UNSURE), ("to read", "", None, UNSURE), ("to read", "", None, UNSURE),
            ("to read", "", None, UNSURE), ("to read", "", None, UNSURE)]
    fig, ax = sheet("AR77XB audio: XB pattern, to confirm on the table")
    audio_frame(ax, "from the arm: colours to read")
    for i, (arm, role, target, ls) in enumerate(lugs, 1):
        label(ax, 39, LUG_Y[i - 1] + 0.5, arm, NOTE, ha="right", fs=8.5)
    for k, (target, text) in enumerate((("left centre", "left signal"), ("left sleeve", "left ground"),
                                        ("right centre", "right signal"), ("right sleeve", "right ground"),
                                        ("ground post", "arm shield"))):
        y1, colour = TARGETS[target]
        wire(ax, [(56, 34), (60 + 2.5 * k, 34), (60 + 2.5 * k, y1), (78, y1)], colour, UNSURE, lw=1.4)
    wire(ax, [(54, 48), (56, 48), (56, 20), (54, 20)], INK, lw=1.2)
    label(ax, 66, 2.5, "which lug carries which wire: find with the ohmmeter, row EL14", NOTE, fs=8)
    save_svg(fig, "ar77xb-wiring-audio",
             "No AR77XB source shows the strip or the arm wire colours. The strip may not even have five lugs. Read it on the table, then fill the table on the page.")


# ---- ground ---------------------------------------------------------------

def ground_page(name, title, strap_text, footer, plate_ls="-"):
    fig, ax = sheet(title)
    box(ax, 2, 46, 20, 10, "IEC inlet\nearth pin", "#f6dedb", fs=9)
    box(ax, 38, 46, 24, 10, "metal top plate", "#eef1f4", fs=9)
    box(ax, 38, 24, 24, 10, "ground post\n(star point)", "#fbeeb8", fs=9)
    box(ax, 2, 24, 20, 10, "arm shield wire\n(strip lug)", "#eef1f4", fs=9)
    box(ax, 2, 4, 20, 10, "sub-chassis\n(T-bar)", "#eef1f4", fs=9)
    box(ax, 78, 24, 20, 10, "amplifier\nground terminal", "#dcecdc", fs=9)
    box(ax, 78, 4, 20, 10, "left and right jacks:\nsleeves insulated", "#f7f7f7", fs=8.5)
    wire(ax, [(22, 51), (38, 51)], "#2e7d32")
    label(ax, 30, 51.8, "mains earth, ring lug", "#2e7d32", fs=8)
    wire(ax, [(50, 46), (50, 34)], GND)
    label(ax, 51, 40, "one link only", INK, ha="left", va="center", fs=8)
    wire(ax, [(22, 29), (38, 29)], GND)
    label(ax, 30, 29.8, "shield wire", INK, fs=8)
    wire(ax, [(22, 7), (58, 7), (58, 24)], GND)
    label(ax, 40, 7.8, "one ring lug", INK, fs=8)
    wire(ax, [(62, 29), (78, 29)], GND)
    label(ax, 70, 29.8, "one separate wire", INK, fs=8)
    label(ax, 70, 27.6, "test on and off", NOTE, va="top", fs=7.5)
    wire(ax, [(62, 9), (78, 9)], NOTE, UNSURE, lw=1.2)
    cross(ax, 70, 9)
    label(ax, 70, 11, "no wire from the sleeves", NOTE, fs=7.5)
    # the old strap
    wire(ax, [(17, 24), (17, 14)], ACCENT, UNSURE, lw=1.6)
    cross(ax, 17, 19)
    label(ax, 19, 19, strap_text, ACCENT, ha="left", va="center", fs=7.8)
    # springs
    wire(ax, [(2, 12), (0.8, 12), (0.8, 60), (50, 60), (50, 56)], NOTE, UNSURE, lw=1.0)
    label(ax, 26, 60.5, "springs: is the T-bar joined to the plate through them? row EL15", NOTE, fs=7.5)
    save_svg(fig, name, footer)


def ground_generic():
    ground_page("wiring-ground", "Ground, modded: one star point at the ground post",
                "old strap from the\nmetalwork to the audio\nshield: remove it",
                "Never lift mains earth to cure hum. Measure plate to shield before modifying, row IE2. If hum remains, change the amplifier ground lead, not the earth.")


def ground_xa():
    ground_page("xa-wiring-ground", "XA ground, modded: the stock strap comes out, the post goes in",
                "stock braided ground strap,\naudio cable to the suspension\n(service manual, p. 2): remove",
                "Stock strap: XA service manual, p. 2, audio output cable. Whether the stock plate is tied to the shield is open, row IE2: measure before modifying. Never lift mains earth.")


def ground_xb():
    ground_page("xb-wiring-ground", "XB ground, modded: one star point at the ground post",
                "any strap from the\nmetalwork to the audio\nshield: find and remove",
                "Drawing 119 shows no ground strap and does not say whether the plate is tied to the shield, row IE2: measure before modifying. Never lift mains earth.")


def ground_ar77xb():
    ground_page("ar77xb-wiring-ground", "AR77XB ground: XB pattern, to confirm on the table",
                "any strap from the\nmetalwork to the audio\nshield: find and remove",
                "No AR77XB source describes the stock grounding. Measure plate to shield and plate to T-bar before modifying, rows IE2 and EL15. Never lift mains earth.")


def wiring():
    power_generic()
    power_xa()
    power_xb()
    power_ar77xb()
    audio_generic()
    audio_xa()
    audio_xb()
    audio_ar77xb()
    ground_generic()
    ground_xa()
    ground_xb()
    ground_ar77xb()


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    mounting()
    hardware_set()
    overhang()
    grounding()
    wiring()
