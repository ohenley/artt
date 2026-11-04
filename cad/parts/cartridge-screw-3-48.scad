// XA/XB aluminum cartridge screw, lengths #1 to #4. A part to buy, not to machine.
// Thread and lengths are from the RDW hardware drawing, December 7, 2023:
// docs/originals/ar-headshell-hardware-rev-1.pdf
// Head size is not dimensioned there, so it is a placeholder.
// License: CC BY-SA 4.0. See LICENSE at the repository root.
include <../lib/common.scad>

variant = 1;   // 1, 2, 3, or 4
flat = false;

lengths = [0.183, 0.356, 0.462, 0.612];

P = [
    ["SC1", "Thread major diameter, #3-48", 0.099 * IN, "S", "in", "Unified #3 major diameter; thread called out on the RDW drawing"],
    ["SC2", "Length under head for this size", lengths[variant - 1] * IN, "C", "in", "RDW hardware drawing: 0.183, 0.356, 0.462, 0.612 in"],
    ["SC3", "Head diameter", 4.6, "PH", "mm", "Calipers on an original screw"],
    ["SC4", "Head height", 1.6, "PH", "mm", "Calipers on an original screw; note the head style and drive"],
];

d = pv(P, "SC1");
l = pv(P, "SC2");
hd = pv(P, "SC3");
hh = pv(P, "SC4");

module part() {
    translate([0, 0, -l]) cylinder(d = d, h = l + EPS);
    cylinder(d = hd, h = hh);
}

emit(
    [
        ["id", "cartridge-screw-3-48"],
        ["title", "XA/XB cartridge screw, #3-48"],
        ["status", "REFERENCE"],
        ["scope", "Original-style hardware. Reproduction shells may differ: Pat's Audio supplies M2.5"],
        ["material", "Aluminum, per the drawing"],
        ["density", 2.7],
        ["make", "Buy. Do not machine. 2 of each length per set"],
        ["variants", [[1, "#1, 0.183 in"], [2, "#2, 0.356 in"], [3, "#3, 0.462 in"], [4, "#4, 0.612 in"]]],
        ["views", ["front", "top", "right", "iso"]],
        ["notes", [
            "Thread is shown as a plain cylinder at major diameter. Specify #3-48 UNC when buying.",
            "The drive recess is not modeled.",
        ]],
    ],
    P,
    [
        ["front", "v", [d / 2, 0, -l], [d / 2, 0, 0], 8, "SC2"],
        ["front", "h", [-d / 2, 0, -l], [d / 2, 0, -l], -8, "SC1", "Ø"],
        ["front", "h", [-hd / 2, 0, hh], [hd / 2, 0, hh], 8, "SC3", "Ø"],
        ["front", "v", [-hd / 2, 0, 0], [-hd / 2, 0, hh], -8, "SC4"],
        ["front", "cl", [0, 0, -l - 0.4], [0, 0, hh + 0.4]],
    ]
);

if (flat) projection() part(); else part();
