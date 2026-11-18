// Cueing height gauge, XB: two steps that check how far the lift raises the stylus.
//
// Drawing 119, note 7: with the mat and one record on, the cueing lift raises
// the stylus 1/4 to 7/16 in above the record. The stylus must clear the low
// step and not the high step.
// Parameter IDs match TO-CONFIRM.md.
// License: CC BY-SA 4.0. See LICENSE at the repository root.
include <../lib/common.scad>

variant = 1;
flat = false;

P = [
    ["CG1", "Low step: the raised stylus must clear it", 1 / 4 * IN, "F", "in", "XB drawing 119, note 7"],
    ["CG2", "High step: the raised stylus must not clear it", 7 / 16 * IN, "F", "in", "XB drawing 119, note 7"],
    ["CG3", "Step length, each", 15, "D", "mm", "Design choice"],
    ["CG4", "Block width", 10, "D", "mm", "Design choice: narrow, so it sits on the record under the stylus"],
    ["CG5", "Base thickness under the steps", 0, "D", "mm", "None: the block stands on the record, so the steps are the heights above the record"],
];

lo = pv(P, "CG1");
hi = pv(P, "CG2");
sl = pv(P, "CG3");
w = pv(P, "CG4");

module part() {
    translate([0, -w / 2, 0]) cube([sl + EPS, w, lo]);
    translate([sl, -w / 2, 0]) cube([sl, w, hi]);
}

emit(
    [
        ["id", "cueing-height-gauge-xb-plastic"],
        ["title", "Cueing height gauge, XB"],
        ["status", "GEOMETRY COMPLETE"],
        ["part", "parts/cueing-height-gauge.md"],
        ["part_name", "Cueing height gauge"],
        ["version", "XB: steps at 1/4 and 7/16 in"],
        ["scope", "New setup tool from the XB factory setting. AR supplied no such gauge"],
        ["material", "Rigid plastic, printed or milled. Soft enough not to chip a stylus if touched"],
        ["density", 1.2],
        ["fits", [["XB", "Fits", "drawing 119, note 7"],
                  ["XA", "Does not fit", "the XA has no cueing lever: model guide"],
                  ["AR77XB", "Unconfirmed", ""]]],
        ["make", "Print or mill. Check both heights with calipers before use"],
        ["views", ["front", "top", "right", "iso"]],
        ["notes", [
            "Use: mat and one record on. Lift the arm with the cueing lever and swing it over the gauge standing on the record. The stylus must pass over the 1/4 in step and must not pass over the 7/16 in step.",
            "Keep the stylus clear of the block. Move the gauge, not the arm, when checking.",
            "Note 8 on the same drawing: the descent from full height to the record takes 1 to 3 seconds.",
        ]],
    ],
    P,
    [
        ["front", "v", [sl, 0, 0], [sl, 0, lo], -9, "CG1"],
        ["front", "v", [2 * sl, 0, 0], [2 * sl, 0, hi], 9, "CG2"],
        ["front", "h", [0, 0, 0], [sl, 0, 0], -9, "CG3"],
        ["top", "v", [2 * sl, -w / 2, 0], [2 * sl, w / 2, 0], 9, "CG4"],
    ]
);

if (flat) projection() part(); else part();
