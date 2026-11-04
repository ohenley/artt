// XA/XB cartridge shim block, thicknesses #1 to #3.
// All dimensions are from the RDW hardware drawing, December 7, 2023:
// docs/originals/ar-headshell-hardware-rev-1.pdf
// License: CC BY-SA 4.0. See LICENSE at the repository root.
include <../lib/common.scad>

variant = 1;   // 1, 2, or 3
flat = false;  // true exports the 1:1 cutting outline

thicknesses = [0.045, 0.080, 0.125];

P = [
    ["SH1", "Length", 0.805 * IN, "C", "in", "RDW hardware drawing"],
    ["SH2", "Width", 0.230 * IN, "C", "in", "RDW hardware drawing"],
    ["SH3", "Thickness for this size", thicknesses[variant - 1] * IN, "C", "in", "RDW hardware drawing: 0.045, 0.080, 0.125 in"],
];

l = pv(P, "SH1");
w = pv(P, "SH2");
t = pv(P, "SH3");

module part() {
    translate([-l / 2, -w / 2, 0]) cube([l, w, t]);
}

emit(
    [
        ["id", "headshell-shim-block"],
        ["title", "XA/XB cartridge shim block"],
        ["status", "GEOMETRY COMPLETE"],
        ["scope", "Original-style XA/XB hardware set. Community drawing, not an AR factory drawing"],
        ["material", "Cardboard, per the drawing"],
        ["density", 0.7],
        ["make", "Cut from sheet. 1 of each thickness per set"],
        ["flat", true],
        ["variants", [[1, "#1, 0.045 in"], [2, "#2, 0.080 in"], [3, "#3, 0.125 in"]]],
        ["views", ["front", "top", "right", "iso"]],
        ["notes", [
            "AR sheet L-1591: the shim block goes under the front of the cartridge where its table calls for one.",
        ]],
    ],
    P,
    [
        ["top", "h", [-l / 2, 0, 0], [l / 2, 0, 0], 9, "SH1"],
        ["top", "v", [l / 2, -w / 2, 0], [l / 2, w / 2, 0], 9, "SH2"],
        ["front", "v", [l / 2, 0, 0], [l / 2, 0, t], 9, "SH3"],
    ]
);

if (flat) projection() part(); else part();
