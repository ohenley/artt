// AR XA tonearm counterweight.
// Size, bore, material, and mass come from one owner's report on one XA:
// parts/xa-counterweight.md. Parameter IDs match TO-CONFIRM.md.
// License: CC BY-SA 4.0. See LICENSE at the repository root.
include <../lib/common.scad>

variant = 1;
flat = false;

P = [
    ["CW3", "Outside diameter", 28, "O", "mm", "Owner report, parts/xa-counterweight.md"],
    ["CW4", "Length along bore", 22, "O", "mm", "Owner report, parts/xa-counterweight.md"],
    ["CW5", "Bore diameter", 9.5, "O", "mm", "Owner report; a nominal value, not a fit against the arm stub"],
    ["CW6", "Bore runs through and on center: assumed", 22, "PH", "mm", "Inspect the part. Measure wall thickness around the bore"],
    ["CW8", "Locking-hole size, tap drill until thread is known", 2.0, "PH", "mm", "Gauge the set screw thread, then set the tap drill"],
    ["CW9", "Locking-hole position from the end face", 11, "PH", "mm", "Calipers, from one end of the weight"],
];

od = pv(P, "CW3");
len = pv(P, "CW4");
bore = pv(P, "CW5");
lock_d = pv(P, "CW8");
lock_x = pv(P, "CW9");

// Axis along X so the top view shows the weight as it sits on the arm.
module part() {
    difference() {
        rotate([0, 90, 0]) cylinder(d = od, h = len);
        translate([-1, 0, 0]) rotate([0, 90, 0]) cylinder(d = bore, h = len + 2);
        translate([lock_x, 0, 0]) cylinder(d = lock_d, h = od);
    }
}

emit(
    [
        ["id", "xa-counterweight"],
        ["title", "XA tonearm counterweight"],
        ["status", "PRELIMINARY"],
        ["scope", "One owner's XA. XB and AR77XB counterweights differ"],
        ["material", "Brass, alloy not established (owner report)"],
        ["density", 8.5],
        ["make", "Turn, bore, cross-drill and tap. 1 off"],
        ["reference_mass_g", 98.8],
        ["views", ["front", "top", "right", "left", "iso"]],
        ["sections", [["A", "y", 0]]],
        ["notes", [
            "Reported mass 98.8 g includes the set screw. Compare with the estimate in the title block.",
            "Bore fit, thread, and edge details are not established. A nominal 9.5 mm owner value is not a fit.",
            "Weigh the original with and without its screw before ordering: TO-CONFIRM.md, CW1 and CW2.",
        ]],
    ],
    P,
    [
        ["front", "h", [0, 0, 0], [len, 0, 0], -9, "CW4"],
        ["front", "v", [len, 0, -od / 2], [len, 0, od / 2], 10, "CW3", "Ø"],
        ["front", "h", [0, 0, od / 2], [lock_x, 0, od / 2], 9, "CW9"],
        ["front", "cl", [-4, 0, 0], [len + 4, 0, 0]],
        ["right", "d", [0, 0, 0], bore / 2, 9, "CW5", "Ø", 40],
        ["top", "d", [lock_x, 0, 0], lock_d / 2, 9, "CW8", "Ø", 60],
        ["A", "h", [0, 0, -bore / 2], [len, 0, -bore / 2], -9, "CW6", "THRU "],
    ]
);

if (flat) projection() part(); else part();
