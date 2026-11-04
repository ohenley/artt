// XA/XB brass set screw from the cartridge hardware set. A part to buy.
// Thread and length are from the RDW hardware drawing, December 7, 2023:
// docs/originals/ar-headshell-hardware-rev-1.pdf
// Its location on the table and its tip dimensions are not established.
// License: CC BY-SA 4.0. See LICENSE at the repository root.
include <../lib/common.scad>

variant = 1;
flat = false;

P = [
    ["SS1", "Thread major diameter, #4-40", 0.112 * IN, "S", "in", "Unified #4 major diameter; thread called out on the RDW drawing"],
    ["SS2", "Overall length", 0.125 * IN, "C", "in", "RDW hardware drawing"],
    ["SS3", "Cone tip length", 0.8, "PH", "mm", "Calipers on an original; the drawing shows a cone with no dimensions"],
    ["SS4", "Flat diameter at the tip", 0.5, "PH", "mm", "Calipers or loupe on an original"],
];

d = pv(P, "SS1");
l = pv(P, "SS2");
tip = pv(P, "SS3");
flat_d = pv(P, "SS4");

module part() {
    cylinder(d1 = flat_d, d2 = d, h = tip);
    translate([0, 0, tip - EPS]) cylinder(d = d, h = l - tip + EPS);
}

emit(
    [
        ["id", "set-screw-4-40"],
        ["title", "XA/XB set screw, #4-40"],
        ["status", "REFERENCE"],
        ["scope", "One in the original-style hardware set. Where it fits is unconfirmed: TO-CONFIRM.md, HS3"],
        ["material", "Brass, per the drawing"],
        ["density", 8.5],
        ["make", "Buy. Do not machine. 1 per set"],
        ["views", ["front", "top", "right", "iso"]],
        ["notes", [
            "Thread is shown as a plain cylinder at major diameter. Specify #4-40 UNC when buying.",
            "Do not assume this is the counterweight locking screw.",
        ]],
    ],
    P,
    [
        ["front", "v", [d / 2, 0, 0], [d / 2, 0, l], 8, "SS2"],
        ["front", "h", [-d / 2, 0, l], [d / 2, 0, l], 8, "SS1", "Ø"],
        ["front", "v", [-d / 2, 0, 0], [-d / 2, 0, tip], -8, "SS3"],
        ["front", "h", [-flat_d / 2, 0, 0], [flat_d / 2, 0, 0], -8, "SS4", "Ø"],
    ]
);

if (flat) projection() part(); else part();
