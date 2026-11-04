// XA/XB cartridge standoff bushing, sizes #1 to #3.
// All dimensions are from the RDW hardware drawing, December 7, 2023:
// docs/originals/ar-headshell-hardware-rev-1.pdf
// License: CC BY-SA 4.0. See LICENSE at the repository root.
include <../lib/common.scad>

variant = 1;   // 1, 2, or 3
flat = false;

heights = [0.050, 0.100, 0.150];

P = [
    ["BU1", "Inside diameter", 0.100 * IN, "C", "in", "RDW hardware drawing"],
    ["BU2", "Outside diameter", 0.180 * IN, "C", "in", "RDW hardware drawing"],
    ["BU3", "Height for this size", heights[variant - 1] * IN, "C", "in", "RDW hardware drawing: 0.050, 0.100, 0.150 in"],
];

id_ = pv(P, "BU1");
od = pv(P, "BU2");
h = pv(P, "BU3");

module part() {
    difference() {
        cylinder(d = od, h = h);
        translate([0, 0, -1]) cylinder(d = id_, h = h + 2);
    }
}

emit(
    [
        ["id", "headshell-standoff-bushing"],
        ["title", "XA/XB cartridge standoff bushing"],
        ["status", "GEOMETRY COMPLETE"],
        ["scope", "Original-style XA/XB hardware set. Community drawing, not an AR factory drawing"],
        ["material", "Soft plastic, grade not established"],
        ["density", 1.1],
        ["make", "Turn or cut from tube. 2 of each size per set"],
        ["variants", [[1, "#1, 0.050 in"], [2, "#2, 0.100 in"], [3, "#3, 0.150 in"]]],
        ["views", ["front", "top", "right", "iso"]],
        ["sections", [["A", "y", 0]]],
        ["notes", [
            "AR sheet L-1591: bushings turn onto the screws, which hold them in place. ID 0.100 in against a #3 screw is a close fit.",
            "Only the bushing set for a given cartridge is used. See the selection table on L-1591.",
        ]],
    ],
    P,
    [
        ["front", "h", [-od / 2, 0, 0], [od / 2, 0, 0], -9, "BU2", "Ø"],
        ["front", "v", [od / 2, 0, 0], [od / 2, 0, h], 9, "BU3"],
        ["front", "cl", [0, 0, -0.2], [0, 0, h + 0.2]],
        ["top", "d", [0, 0, 0], id_ / 2, 9, "BU1", "Ø", 50],
    ]
);

if (flat) projection() part(); else part();
