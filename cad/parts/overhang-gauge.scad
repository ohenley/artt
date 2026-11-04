// Overhang gauge for the AR arm: a new design from one factory dimension.
// It is not a copy of AR's gauge (XA part 914, XB P/N 402001), whose outline
// has not been found. Villchur, Audio, Sept 1962, p. 69: the template fits over
// the spindle, and with the needle in its small hole the overhang is correct.
// License: CC BY-SA 4.0. See LICENSE at the repository root.
include <../lib/common.scad>

variant = 1;
flat = false;  // true exports the 1:1 cutting outline

P = [
    ["GA1", "Spindle center to needle hole", 0.688 * IN, "F", "in", "Villchur 1962, p. 69; XB drawing 119, note 10: 0.688 in +/- 0.030"],
    ["GA2", "Spindle hole diameter", 7.3, "PH", "mm", "Micrometer on your spindle; the hole must fit without play"],
    ["GA3", "Needle hole diameter", 1.2, "PH", "mm", "Choose so a stylus tip seats without touching the cantilever"],
    ["GA4", "Plate length", 40, "PH", "mm", "Design freedom; the original outline is unknown"],
    ["GA5", "Plate width", 18, "PH", "mm", "Design freedom; the original outline is unknown"],
    ["GA6", "Plate thickness", 3, "PH", "mm", "Check it clears the spindle shoulder and the arm's cueing height"],
];

c = pv(P, "GA1");
sd = pv(P, "GA2");
nd = pv(P, "GA3");
pl = pv(P, "GA4");
pw = pv(P, "GA5");
pt = pv(P, "GA6");

module part() {
    difference() {
        translate([c / 2, 0, 0]) rr_prism(pl, pw, pt, 3);
        translate([0, 0, -1]) cylinder(d = sd, h = pt + 2);
        translate([c, 0, -1]) cylinder(d = nd, h = pt + 2);
    }
}

emit(
    [
        ["id", "overhang-gauge"],
        ["title", "AR arm overhang gauge"],
        ["status", "PRELIMINARY"],
        ["scope", "New design. Critical dimension from the 1962 paper and XB drawing 119. Other dimensions are not AR's"],
        ["material", "Clear acrylic (PMMA) suggested"],
        ["density", 1.18],
        ["make", "Mill or laser cut. 1 off"],
        ["flat", true],
        ["views", ["front", "top", "right", "iso"]],
        ["notes", [
            "Only the spindle-to-hole distance is functional. XB note 10 allows +/- 0.030 in; keep it far tighter on the gauge.",
            "Set the overhang with the needle hole on the line from the spindle to the arm pivot.",
            "Not calibrated. Check the hole distance before treating it as a setup tool.",
        ]],
    ],
    P,
    [
        ["top", "h", [0, pw / 2, 0], [c, pw / 2, 0], 16, "GA1"],
        ["top", "h", [c / 2 - pl / 2, 0, 0], [c / 2 + pl / 2, 0, 0], -9, "GA4"],
        ["top", "v", [c / 2 + pl / 2, -pw / 2, 0], [c / 2 + pl / 2, pw / 2, 0], 9, "GA5"],
        ["top", "d", [0, 0, 0], sd / 2, 7, "GA2", "Ø", 125],
        ["top", "d", [c, 0, 0], nd / 2, 7, "GA3", "Ø", 65],
        ["top", "cl", [0, -pw / 2 - 2, 0], [0, pw / 2 + 2, 0]],
        ["top", "cl", [c, -pw / 2 - 2, 0], [c, pw / 2 + 2, 0]],
        ["front", "v", [c / 2 + pl / 2, 0, 0], [c / 2 + pl / 2, 0, pt], 9, "GA6"],
    ]
);

if (flat) projection() part(); else part();
