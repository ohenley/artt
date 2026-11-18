// AR tonearm counterweight: one parametric model, one drawing per version and material.
//
// The part is defined by its mass, not its outline. The model takes the target
// mass, the material density, the bore and the outside diameter, and computes
// the length:
//     length = mass / (density x pi/4 x (OD^2 - bore^2)),
// then adds the length that replaces the metal removed by the locking hole.
// Only the XA version is built, from one owner's report: parts/counterweight.md.
// XB and AR77XB versions are added when their masses are measured, not before.
// Parameter IDs match TO-CONFIRM.md.
// License: CC BY-SA 4.0. See LICENSE at the repository root.
include <../lib/common.scad>

variant = 1;   // 1 brass, 2 stainless steel, 3 aluminium
flat = false;

// [slug, material text, density g/cm3, density source]
materials = [
    ["brass", "Brass, alloy not established; the original is reported as brass",
     8.5, "Wikipedia Brass excerpt: 8.4 to 8.73 g/cm3 for brass; 8.5 used, inside that range"],
    ["stainless", "Stainless steel, 304 taken as the example",
     7.9, "Wikipedia SAE 304 stainless steel excerpt: 7,900 kg/m3"],
    ["aluminium", "Aluminium, 6061 taken as the example",
     2.70, "Wikipedia 6061 aluminium alloy excerpt: 2.70 g/cm3"],
];
mat = materials[variant - 1];

// Inputs. Each keeps its own evidence code in table P below.
mass = 98.8;            // CW1, g, with the set screw
od = 28;                // CW3, mm
bore = 0.375 * IN;      // CW5, 3/8 in entered as derived from the 9.5 mm report
rho = mat[2];           // CW15, g/cm3
lock_d = 2.0;           // CW8, placeholder
lock_x = 11;            // CW9, placeholder

// The formula. Volumes in mm3, density converted to g/mm3.
area = PI / 4 * (od * od - bore * bore);
len_plain = mass / (rho / 1000) / area;
lock_volume = PI / 4 * lock_d * lock_d * (od - bore) / 2;   // radial hole, surface to bore
len = round((len_plain + lock_volume / area) * 100) / 100;   // CW14, to 0.01 mm

P = [
    ["CW1", "Target mass, with the set screw", mass, "O", "g", "Owner report, one XA, parts/counterweight.md. The set screw is included: its own mass is CW2"],
    ["CW3", "Outside diameter", od, "O", "mm", "Owner report, one XA"],
    ["CW4", "Reported length along the bore, for comparison only", 22, "O", "mm", "Owner report, one XA. Not used by the model: compare with CW14"],
    ["CW5", "Bore diameter", bore, "DV", "in", "The reported 9.5 mm is within 0.03 mm of 3/8 in, and AR dimensioned in inches, so 3/8 in is entered. Verify: pin gauge on an original bore, and the arm stub diameter"],
    ["CW6", "Bore runs through and on center: assumed", len, "PH", "mm", "Inspect the part. Measure wall thickness around the bore"],
    ["CW8", "Locking-hole size, tap drill until thread is known", lock_d, "PH", "mm", "Gauge the set screw thread, then set the tap drill"],
    ["CW9", "Locking-hole position from the end face", lock_x, "PH", "mm", "Calipers, from one end of the weight"],
    ["CW15", "Density used", rho, "S", "g/cm3", mat[3]],
    ["CW14", "Length computed from the mass", len, "DV", "mm", str("CW1 / (CW15 x pi/4 x (CW3^2 - CW5^2)) = ", round(len_plain * 100) / 100, " mm, plus ", round(lock_volume / area * 100) / 100, " mm for the metal removed by the locking hole CW8. Verify: weigh the finished part; compare with CW4 on an original")],
];

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
        ["id", str("counterweight-xa-", mat[0])],
        ["title", str("Tonearm counterweight, XA mass, in ", mat[0] == "stainless" ? "stainless steel" : mat[0])],
        ["status", "PRELIMINARY"],
        ["part", "parts/counterweight.md"],
        ["part_name", "Counterweight"],
        ["version", variant == 1 ? "XA brass weight, 1961 to 1979" : str("XA weight remade in ", mat[0] == "stainless" ? "stainless steel" : mat[0], ": same mass, longer body")],
        ["material", mat[1]],
        ["density", rho],
        ["fits", variant == 1
            ? [["XA", "Fitted by AR", "XA service manual p. 4, item 22B part 952; brass per two owner reports"],
               ["XB", "Unconfirmed", ""], ["AR77XB", "Unconfirmed", ""]]
            : [["XA", "Fits with a change", str("the body is ", round(len * 10) / 10, " mm long instead of the reported 22 mm; whether the arm stub, arm rest and cover clear it is CW16 and CW17")],
               ["XB", "Unconfirmed", ""], ["AR77XB", "Unconfirmed", ""]]],
        ["scope", "One owner's XA. The XB and AR77XB counterweights differ and are not drawn"],
        ["make", "Turn, bore, cross-drill and tap. 1 off"],
        ["reference_mass_g", mass],
        ["formula", "length = mass / (density x pi/4 x (OD^2 - bore^2)), then add the length that replaces the metal removed by the locking hole"],
        ["final_check", "Final check is the scale: the finished part must weigh inside the range, whatever the drawing says."],
        ["variants", [[1, "XA mass in brass"], [2, "XA mass in stainless steel"], [3, "XA mass in aluminium"]]],
        ["views", ["front", "top", "right", "left", "iso"]],
        ["sections", [["A", "y", 0]]],
        ["notes", [
            "The part is defined by its mass. The 98.8 g value is one XA weight with its set screw; the range across originals is not known (CW11, CW12).",
            str("Model mass at ", rho, " g/cm3 is printed in the title block. It should equal CW1 within rounding; the difference is the set screw and the density guess."),
            "Bore fit, thread, and edge details are not established. 3/8 in is entered from a 9.5 mm owner value; it is not a fit on the arm stub.",
            variant == 1 ? "The computed length is 0.7 mm shorter than the reported 22 mm: the density is a range, and the set screw is in the 98.8 g." : "This is longer than the brass original. Check the arm stub length and the clearance to the arm rest and the cover before making it (CW16, CW17).",
            "Weigh the original with and without its screw before ordering: TO-CONFIRM.md, CW1 and CW2.",
        ]],
    ],
    P,
    [
        ["front", "h", [0, 0, 0], [len, 0, 0], -9, "CW14"],
        ["front", "v", [len, 0, -od / 2], [len, 0, od / 2], 10, "CW3", "Ø"],
        ["front", "h", [0, 0, od / 2], [lock_x, 0, od / 2], 9, "CW9"],
        ["front", "cl", [-4, 0, 0], [len + 4, 0, 0]],
        ["right", "d", [0, 0, 0], bore / 2, 9, "CW5", "Ø", 40],
        ["top", "d", [lock_x, 0, 0], lock_d / 2, 9, "CW8", "Ø", 60],
        ["A", "h", [0, 0, -bore / 2], [len, 0, -bore / 2], -9, "CW6", "THRU "],
    ]
);

if (flat) projection() part(); else part();
