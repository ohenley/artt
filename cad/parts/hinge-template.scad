// XB hinge drilling template, from the hinge detail on drawing 114, revision S.
//
// The hinged cover existed only between ECO 1135 (14 September 1976) and
// ECO 1315 (28 January 1977). Two templates: one for the cover, one for the
// base. Each is a card held in the rear corner of the part: its end against
// the end of the cover or base, its long edge against the cover's lower edge or
// the base's top edge. Mark through the two holes, then turn it over for the
// other end. The 2.20 in against 60.6 mm conflict (DM4) stays red.
// Parameter IDs match TO-CONFIRM.md.
// License: CC BY-SA 4.0. See LICENSE at the repository root.
include <../lib/common.scad>

variant = 1;   // 1: cover, 2: base
flat = false;  // true exports the 1:1 cutting outline

P = concat([
    ["HT1", "Spacing between the paired holes", 0.98 * IN, "F", "in", "Drawing 114, revision S, hinge detail: 0.98 in, also printed 25 mm"],
], variant == 1 ? [
    ["DM4", "End of cover to first cover hole", 2.20 * IN, "PH", "in", "Drawing 114 prints 2.20 in and 60.6 mm, which do not convert (2.20 in is 55.9 mm). Measure a hinged XB cover"],
    ["HT2", "Cover hole row to lower edge of cover", 0.57 * IN, "F", "in", "Drawing 114: 0.57 in, also printed 14.5 mm"],
    ["HT3", "Cover hole diameter", 0.15 * IN, "F", "in", "Drawing 114: 0.15 in, also printed 4 mm"],
] : [
    ["HT5", "End of base to first base hole", 2.28 * IN, "F", "in", "Drawing 114: 2.28 in, also printed 58 mm"],
    ["HT4", "Base hole row to top edge of base", 1.00 * IN, "F", "in", "Drawing 114: 1.00 in, also printed 25.5 mm"],
    ["HT6", "Base hole diameter", 0.11 * IN, "F", "in", "Drawing 114: 0.11 in, also printed 2.8 mm. Pilot for a wood screw"],
    ["HT7", "Base hole depth, for the drill stop", 0.37 * IN, "F", "in", "Drawing 114: 0.37 in, also printed 9.5 mm. Not a feature of the card"],
], [
    ["HT8", "Card width", 1.5 * IN, "D", "in", "Design choice: wider than the hole row offset"],
    ["HT9", "Card length", 4.0 * IN, "D", "in", "Design choice: past the second hole"],
    ["HT10", "Card thickness", 0.5, "D", "mm", "Design choice: card or thin plastic"],
]);

first = variant == 1 ? pv(P, "DM4") : pv(P, "HT5");
row = variant == 1 ? pv(P, "HT2") : pv(P, "HT4");
hole = variant == 1 ? pv(P, "HT3") : pv(P, "HT6");
pair = pv(P, "HT1");
cw = pv(P, "HT8");
cl = pv(P, "HT9");
ct = pv(P, "HT10");

// x = 0 is the end of the cover or base; y = 0 is the reference edge.
module part() {
    difference() {
        cube([cl, cw, ct]);
        for (x = [first, first + pair]) translate([x, row, -1]) cylinder(d = hole, h = ct + 2);
    }
}

emit(
    [
        ["id", variant == 1 ? "hinge-template-xb-cover-card" : "hinge-template-xb-base-card"],
        ["title", variant == 1 ? "Hinge drilling template, XB cover" : "Hinge drilling template, XB base"],
        ["status", "PRELIMINARY"],
        ["part", "parts/hinge-template.md"],
        ["part_name", "Hinge drilling template"],
        ["version", variant == 1 ? "XB hinged cover, September 1976 to January 1977: cover holes" : "XB hinged cover, September 1976 to January 1977: base holes"],
        ["scope", "The hinge detail of drawing 114 only. The hinge itself and the cover outline are not drawn"],
        ["material", "Card or thin plastic"],
        ["density", 0.7],
        ["fits", [["XB", "Fits", "drawing 114 revision S; the hinge was added by ECO 1135 and deleted by ECO 1315, drawing 119 revision block"],
                  ["XA", "Unconfirmed", ""], ["AR77XB", "Unconfirmed", ""]]],
        ["make", "Print the 1:1 DXF or cut the card to the dimensions. Prick the two hole centers"],
        ["flat", true],
        ["variants", [[1, "Cover"], [2, "Base"]]],
        ["views", ["front", "top", "iso"]],
        ["notes", concat(variant == 1 ? [
            "DM4 is red: the drawing gives 2.20 in and 60.6 mm for the end-to-first-hole distance, and they disagree by 4.7 mm. Do not drill until a hinged cover is measured.",
            "Hold the card's end (x = 0) against the end of the cover and its long edge (y = 0) against the cover's lower edge.",
        ] : [
            "Hold the card's end (x = 0) against the end of the base and its long edge (y = 0) against the base's top edge. Drill 0.11 in pilot holes 0.37 in deep.",
            "The two rows are 1.26 in apart with the cover closed, per the same detail. Check that against your cover before drilling the base.",
        ], [
            "Use the same card at both ends: turn it over for the other end.",
            "Revision S hardware for the hinge: four #6 x 0.375 in wood screws, four #4-40 x 0.375 in screws, four #4-40 dome nuts (drawing 113).",
        ])],
    ],
    P,
    [
        ["top", "h", [0, cw, 0], [first, cw, 0], 9, variant == 1 ? "DM4" : "HT5"],
        ["top", "h", [first, cw, 0], [first + pair, cw, 0], 16, "HT1"],
        ["top", "v", [cl, 0, 0], [cl, row, 0], 9, variant == 1 ? "HT2" : "HT4"],
        ["top", "d", [first + pair, row, 0], hole / 2, 9, variant == 1 ? "HT3" : "HT6", "Ø", 315],
        ["top", "h", [0, 0, 0], [cl, 0, 0], -9, "HT9"],
        ["top", "v", [0, 0, 0], [0, cw, 0], -9, "HT8"],
        ["front", "v", [cl, 0, 0], [cl, 0, ct], 9, "HT10"],
    ]
);

if (flat) projection() part(); else part();
