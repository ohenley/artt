// Platter height gauge: a stepped block slid under the outer platter's edge.
//
// XB: the outer platter sits 3/8 in +/- 1/32 above the top plate (drawing 119,
// note 13), so the steps are 11/32, 3/8 and 13/32 in. The low step must pass
// under the platter and the high step must not.
// XA: 1/8 in with a heavy record on (XA service manual p. 2). No tolerance is
// given, so the XA gauge has one step at the nominal and a handle.
// Parameter IDs match TO-CONFIRM.md.
// License: CC BY-SA 4.0. See LICENSE at the repository root.
include <../lib/common.scad>

variant = 1;   // 1: XB, 2: XA
flat = false;

P = concat(variant == 1 ? [
    ["PG1", "Low step: must pass under the platter", 11 / 32 * IN, "F", "in", "XB drawing 119, note 13: 3/8 in minus 1/32"],
    ["PG2", "Nominal step", 3 / 8 * IN, "F", "in", "XB drawing 119, note 13"],
    ["PG3", "High step: must not pass", 13 / 32 * IN, "F", "in", "XB drawing 119, note 13: 3/8 in plus 1/32"],
] : [
    ["PG4", "Step: the platter rides this high with a heavy record on", 1 / 8 * IN, "F", "in", "XA service manual p. 2. No tolerance is given"],
], [
    ["PG5", "Step length, each", 20, "D", "mm", "Design choice"],
    ["PG6", "Block width", 15, "D", "mm", "Design choice: narrow enough to pass between the platter edge and the arm"],
    ["PG7", "Handle height", 20, "D", "mm", "Design choice"],
]);

steps = variant == 1 ? [pv(P, "PG1"), pv(P, "PG2"), pv(P, "PG3")] : [pv(P, "PG4")];
sl = pv(P, "PG5");
w = pv(P, "PG6");
hh = pv(P, "PG7");
n = len(steps);
total = (n + 1) * sl;

// Steps rise from x = 0; the handle is the last block.
module part() {
    for (i = [0 : n - 1])
        translate([i * sl, -w / 2, 0]) cube([sl + EPS, w, steps[i]]);
    translate([n * sl, -w / 2, 0]) cube([sl, w, hh]);
}

ids = variant == 1 ? ["PG1", "PG2", "PG3"] : ["PG4"];

emit(
    [
        ["id", variant == 1 ? "platter-height-gauge-xb-plastic" : "platter-height-gauge-xa-plastic"],
        ["title", variant == 1 ? "Platter height gauge, XB" : "Platter height gauge, XA"],
        ["status", "GEOMETRY COMPLETE"],
        ["part", "parts/platter-height-gauge.md"],
        ["part_name", "Platter height gauge"],
        ["version", variant == 1 ? "XB: steps at 11/32, 3/8 and 13/32 in" : "XA: one step at 1/8 in, no tolerance stated"],
        ["scope", "New setup tool from the factory setting of one table. AR supplied no such gauge"],
        ["material", "Rigid plastic, printed or milled; a stack of shim stock also works"],
        ["density", 1.2],
        ["fits", variant == 1
            ? [["XB", "Fits", "drawing 119, note 13"], ["XA", "Does not fit", "the XA platter rides 1/8 in, XA service manual p. 2"], ["AR77XB", "Unconfirmed", ""]]
            : [["XA", "Fits", "XA service manual p. 2"], ["XB", "Does not fit", "the XB platter rides 3/8 in, drawing 119 note 13"], ["AR77XB", "Unconfirmed", ""]]],
        ["make", "Print or mill. Check each step with calipers before use: a printer's first layer is often thick"],
        ["variants", [[1, "XB"], [2, "XA"]]],
        ["views", ["front", "top", "right", "iso"]],
        ["notes", variant == 1 ? [
            "Use: with the mat and a record on, slide the gauge under the outer platter's edge at several points. The 11/32 step must pass; the 13/32 step must not. Adjust the three suspension nuts (item 32) until it does all round.",
            "Drawing 119 does not say whether a record is on the platter for note 13. The XA manual says with a heavy record. Record what you did.",
        ] : [
            "Use: with a heavy record on, slide the 1/8 in step under the outer platter's edge at several points; it should just pass all round. Adjust the three suspension nuts until it does.",
            "No tolerance is given for the XA. Do not borrow the XB's 1/32 in.",
        ]],
    ],
    P,
    concat(
        [for (i = [0 : n - 1]) ["front", "v", [i * sl, 0, 0], [i * sl, 0, steps[i]], -9 - 8 * (n - 1 - i), ids[i]]],
        [
            ["front", "v", [total, 0, 0], [total, 0, hh], 17, "PG7"],
            ["front", "h", [0, 0, 0], [sl, 0, 0], -9, "PG5"],
            ["top", "v", [total, -w / 2, 0], [total, w / 2, 0], 9, "PG6"],
        ]
    )
);

if (flat) projection() part(); else part();
