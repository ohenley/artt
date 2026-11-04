// AR XA/XB headshell in PMMA, with top-access slots for a Grado Master4.
//
// CONCEPT ONLY. No dimensioned drawing of the AR shell has been found, so its
// body, neck, thread, pins, and key are all placeholders here. The layout comes
// from the exploded view on p. 4 of the XA service manual: a box open underneath,
// a round rear neck with contact pins, a knurled retaining nut on the arm, and
// a finger lift. Do not order this until the PH rows are measured.
//
// Axes: X along the shell with the neck at +X, Y across, Z up. z = 0 is the
// open underside of the body.
// License: CC BY-SA 4.0. See LICENSE at the repository root.
include <../lib/common.scad>

variant = 1;
flat = false;

P = [
    // Cartridge mounting. Slot width and head recess must suit the actual screw.
    ["GR0", "Cartridge mounting-hole spacing", 0.5 * IN, "S", "in", "Standard 1/2 in mount. Not stated on Grado's Master4 page; check on the cartridge"],
    ["GR1", "Slot width: clearance for the Grado screw", 2.8, "PH", "mm", "Gauge the supplied Grado screw. Reports conflict: 3-48, M2.6, about 2 mm, nonstandard"],
    ["GR2", "Head recess width", 5.0, "PH", "mm", "Calipers on the supplied Grado screw head, plus clearance"],
    ["GR3", "Head recess depth", 1.0, "PH", "mm", "Set so the screw reaches the body threads without bottoming"],
    ["GR4", "Slot length between end-radius centers", 6.0, "PH", "mm", "Enough travel to set the cartridge; check against the stylus position"],
    ["GR5", "Slot center from body center", -1.5, "PH", "mm", "From the Grado mounting holes to stylus and the 3/8 in factory setting"],
    ["GR6", "Pocket width: must clear the Grado body", 21.0, "PH", "mm", "Calipers on the Master4. Sized from the Opus3's 20.1 mm; Grado says the Master4 housing was reshaped"],

    // Shell body.
    ["HD1", "Body length", 40, "PH", "mm", "Original shell, but the pocket must clear the Master4. Opus3 is 29.6 mm with pins; Master4 unpublished"],
    ["HD2", "Body width", 25, "PH", "mm", "Original shell, but must clear the Master4. Opus3 is wider than some headshells; Master4 unpublished"],
    ["HD3", "Body height", 16, "PH", "mm", "Calipers on an original shell"],
    ["HD4", "Top thickness above the pocket", 3.5, "PH", "mm", "Screw length minus thread engagement in the Grado body"],
    ["HD5", "Front wall thickness", 2.5, "PH", "mm", "Keep at least 1 mm in PMMA; confirm with the maker"],
    ["HD6", "Rear wall thickness, carries the neck", 6.0, "PH", "mm", "Set by pin and neck construction"],
    ["HD7", "Body corner radius", 2.0, "PH", "mm", "Design freedom"],
    ["HD8", "Pocket corner radius: milling tool radius", 1.5, "D", "mm", "Design choice for a milled inside corner"],

    // Neck and connector: all must come from an original shell.
    ["HD10", "Neck outside diameter", 10, "PH", "mm", "Micrometer on an original neck"],
    ["HD11", "Neck length from the rear face", 12, "PH", "mm", "Calipers on an original neck"],
    ["HD12", "Neck axis height above the underside", 8, "PH", "mm", "Critical. Sets the mounting plane relative to the arm axis"],
    ["HD13", "Contact-pin circle diameter", 5.5, "PH", "mm", "Measure on the arm-end socket and an original shell"],
    ["HD14", "Contact-pin hole diameter", 1.6, "PH", "mm", "Set from the pins chosen"],

    // Finger lift.
    ["HD16", "Finger-lift length past the front", 12, "PH", "mm", "Calipers on an original shell"],
    ["HD17", "Finger-lift width", 6, "PH", "mm", "Calipers on an original shell"],
    ["HD18", "Finger-lift thickness", 2.5, "PH", "mm", "PMMA is brittle; a thin tab can snap"],
];

spacing = pv(P, "GR0");
slot_w = pv(P, "GR1");
rec_w = pv(P, "GR2");
rec_d = pv(P, "GR3");
slot_c = pv(P, "GR4");
slot_x = pv(P, "GR5");
pocket_w = pv(P, "GR6");

body_l = pv(P, "HD1");
body_w = pv(P, "HD2");
body_h = pv(P, "HD3");
top_t = pv(P, "HD4");
wall_f = pv(P, "HD5");
wall_r = pv(P, "HD6");
r_body = pv(P, "HD7");
r_pocket = pv(P, "HD8");

neck_d = pv(P, "HD10");
neck_l = pv(P, "HD11");
neck_z = pv(P, "HD12");
pin_c = pv(P, "HD13");
pin_d = pv(P, "HD14");

lift_l = pv(P, "HD16");
lift_w = pv(P, "HD17");
lift_t = pv(P, "HD18");

pocket_l = body_l - wall_f - wall_r;
pocket_x = (wall_f - wall_r) / 2;
pocket_h = body_h - top_t;

module part() {
    difference() {
        union() {
            rr_prism(body_l, body_w, body_h, r_body);
            // Neck, overlapping into the rear wall.
            translate([body_l / 2 - 1, 0, neck_z])
                rotate([0, 90, 0]) cylinder(d = neck_d, h = neck_l + 1);
            // Finger lift at the front, flush with the top.
            translate([-body_l / 2 - lift_l, -lift_w / 2, body_h - lift_t])
                cube([lift_l + 1, lift_w, lift_t]);
        }
        // Cartridge pocket, open underneath.
        translate([pocket_x, 0, -1]) rr_prism(pocket_l, pocket_w, pocket_h + 1, r_pocket);
        // Screw slots and head recesses, machined from the top.
        for (sy = [-1, 1]) translate([slot_x, sy * spacing / 2, 0]) {
            translate([0, 0, pocket_h - 1]) slot_prism(slot_c, slot_w, top_t + 2);
            translate([0, 0, body_h - rec_d]) slot_prism(slot_c, rec_w, rec_d + 1);
        }
        // Contact-pin holes, through the rear wall and neck.
        for (a = [45, 135, 225, 315])
            translate([body_l / 2 - wall_r - 1, pin_c / 2 * cos(a), neck_z + pin_c / 2 * sin(a)])
                rotate([0, 90, 0]) cylinder(d = pin_d, h = wall_r + neck_l + 2);
    }
}

emit(
    [
        ["id", "headshell-pmma-top-mount"],
        ["title", "XA/XB headshell, PMMA, top-mount Grado Master4"],
        ["status", "CONCEPT"],
        ["scope", "New design for a Grado Master4. Layout from the XA service manual, p. 4. Not an AR dimension set"],
        ["material", "PMMA (acrylic), cast grade preferred"],
        ["density", 1.18],
        ["make", "Mill from two sides, plus the end face for the neck. Print a test piece first"],
        ["views", ["front", "top", "bottom", "right", "left", "iso"]],
        ["sections", [["A", "y", 6.35]]],
        ["notes", [
            "Neck thread, key, and pin style are not modeled because they are unknown. Measure an original shell and its retaining nut.",
            "Pat's Audio advertises a reinforced neck with threads that will not crack off, which suggests this is the weak point. A PMMA thread may not hold; consider a metal neck insert.",
            "Keep threadlockers, alcohol, and solvents away from PMMA: they can craze it. Tighten the screws gently.",
            "Grado lists the Master4 at 9.6 g, 1.6-1.9 g tracking force, 20 um/mN compliance. Confirm the counterweight still balances, and check arm resonance.",
            "Grado publishes no Master4 dimensions. Pocket sized from one review's Opus3 figures: 20.1 wide, 25.3 deep, 29.6 with pins, 18.3 top to stylus. Measure the Master4.",
            "With the Opus3 figure, the stylus sits 5.8 mm below the underside (18.3 - pocket depth). Check the shell clears the record at the arm's working angle.",
        ]],
    ],
    P,
    [
        ["front", "h", [-body_l / 2, 0, 0], [body_l / 2, 0, 0], -9, "HD1"],
        ["front", "v", [-body_l / 2, 0, 0], [-body_l / 2, 0, body_h], -9, "HD3"],
        ["front", "h", [body_l / 2, 0, neck_z], [body_l / 2 + neck_l, 0, neck_z], 9, "HD11"],
        ["front", "v", [body_l / 2 + neck_l, 0, 0], [body_l / 2 + neck_l, 0, neck_z], 9, "HD12"],
        ["front", "h", [-body_l / 2 - lift_l, 0, body_h], [-body_l / 2, 0, body_h], 9, "HD16"],
        ["front", "cl", [body_l / 2 - 3, 0, neck_z], [body_l / 2 + neck_l + 2, 0, neck_z]],
        ["top", "v", [body_l / 2, -body_w / 2, 0], [body_l / 2, body_w / 2, 0], 22, "HD2"],
        ["top", "v", [slot_x, -spacing / 2, 0], [slot_x, spacing / 2, 0], 9, "GR0"],
        ["top", "h", [slot_x - slot_c / 2, body_w / 2, 0], [slot_x + slot_c / 2, body_w / 2, 0], 9, "GR4"],
        ["top", "d", [slot_x + slot_c / 2, spacing / 2, 0], rec_w / 2, 13, "GR2", "W ", 50],
        ["top", "d", [slot_x - slot_c / 2, spacing / 2, 0], slot_w / 2, 13, "GR1", "W ", 135],
        ["top", "h", [0, -body_w / 2, 0], [slot_x, -body_w / 2, 0], -9, "GR5", "", "from body center"],
        ["bottom", "v", [body_l / 2, -pocket_w / 2, 0], [body_l / 2, pocket_w / 2, 0], 9, "GR6"],
        ["bottom", "h", [-body_l / 2, body_w / 2, 0], [-body_l / 2 + wall_f, body_w / 2, 0], -9, "HD5"],
        ["bottom", "h", [body_l / 2 - wall_r, body_w / 2, 0], [body_l / 2, body_w / 2, 0], -9, "HD6"],
        ["right", "d", [0, 0, neck_z], neck_d / 2, 9, "HD10", "Ø", 60],
        ["right", "d", [0, pin_c / 2 * cos(315), neck_z + pin_c / 2 * sin(315)], pin_d / 2, 9, "HD14", "Ø", 300],
        ["left", "h", [-lift_w / 2, 0, 0], [lift_w / 2, 0, 0], -9, "HD17"],
        ["A", "v", [body_l / 2, 0, pocket_h], [body_l / 2, 0, body_h], 9, "HD4"],
        ["A", "v", [-body_l / 2, 0, body_h - rec_d], [-body_l / 2, 0, body_h], -9, "GR3"],
    ]
);

if (flat) projection() part(); else part();
