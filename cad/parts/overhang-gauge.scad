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
    ["GA7", "Tolerance on the overhang, marked as two scribed lines", 0.030 * IN, "F", "in", "XB drawing 119, note 10: 0.688 in +/- 0.030. The lines show the allowed band; the hole is the nominal"],
];

c = pv(P, "GA1");
sd = pv(P, "GA2");
nd = pv(P, "GA3");
pl = pv(P, "GA4");
pw = pv(P, "GA5");
pt = pv(P, "GA6");
tol = pv(P, "GA7");
mark_w = 0.3;   // scribed line width and depth, a design choice
mark_d = 0.3;

module part() {
    difference() {
        translate([c / 2, 0, 0]) rr_prism(pl, pw, pt, 3);
        translate([0, 0, -1]) cylinder(d = sd, h = pt + 2);
        translate([c, 0, -1]) cylinder(d = nd, h = pt + 2);
        // Tolerance marks: two lines across the plate at +/- GA7 from the needle hole.
        for (s = [-1, 1])
            translate([c + s * tol - mark_w / 2, -pw / 2 - 1, pt - mark_d]) cube([mark_w, pw + 2, mark_d + 1]);
    }
}

emit(
    [
        ["id", "overhang-gauge-new-pmma"],
        ["title", "Overhang template for the AR arm, new design"],
        ["status", "PRELIMINARY"],
        ["part", "parts/overhang-template.md"],
        ["part_name", "Overhang template"],
        ["version", "New design from the factory overhang; AR's own outline (XA part 914, XB P/N 402001) is not known"],
        ["scope", "New design. Critical dimension from the 1962 paper and XB drawing 119. Other dimensions are not AR's"],
        ["material", "Clear acrylic (PMMA) suggested"],
        ["density", 1.18],
        ["fits", [["XA", "Fits", "Villchur 1962, Part 1, p. 69: overhang 0.688 in on the AR arm"],
                  ["XB", "Fits", "drawing 119, note 10: 0.688 in +/- 0.030"],
                  ["AR77XB", "Unconfirmed", ""]]],
        ["make", "Mill or laser cut. 1 off"],
        ["flat", true],
        ["views", ["front", "top", "right", "iso"]],
        ["notes", [
            "Only the spindle-to-hole distance is functional. XB note 10 allows +/- 0.030 in; keep it far tighter on the gauge.",
            "The two scribed lines at +/- 0.030 in (GA7) show the XB tolerance band on the overhang. A stylus inside the band passes on an XB; the XA sets no tolerance.",
            "Set the overhang with the needle hole on the line from the spindle to the arm pivot.",
            "Not calibrated. Check the hole distance before treating it as a setup tool.",
        ]],
    ],
    P,
    [
        ["top", "h", [0, pw / 2, 0], [c, pw / 2, 0], 16, "GA1"],
        ["top", "h", [c, -pw / 2, 0], [c + tol, -pw / 2, 0], -16, "GA7", "±"],
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
