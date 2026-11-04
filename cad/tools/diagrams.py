#!/usr/bin/env python3
"""Draw the plain-language diagrams used by docs/what-goes-where.md.

Run with the packages in requirements.txt. Output goes to docs/images/.
Only the hardware-set sizes are true to the source; the others are schematic.
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


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    mounting()
    hardware_set()
    overhang()
