// AR XA/XB headshell in PMMA, with top-access slots for a Grado Master4.
//
// CONCEPT ONLY. No dimensioned drawing of the AR shell has been found, so its
// body, neck, thread, pins, and key are all placeholders here. The layout comes
// from the exploded view on p. 4 of the XA service manual: a box open underneath,
// a round rear neck with contact pins, a knurled retaining nut on the arm, and
// a curved finger lift on one side wall near the front (item 20). Do not
// order this until the PH rows are measured.
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
    ["GR13", "Stylus tip position from body center, at the factory overhang", -11.0, "PH", "mm", "Set from GR8 on the Master4 and the arm's 0.688 in overhang. Toward the front is negative"],
    ["GR5", "Slot center behind the stylus tip", 0.375 * IN, "DV", "in", "Villchur 1962, Part 1, p. 69: the arm is factory-set for a cartridge with 3/8 in between mounting centers and needle tip, so the slot centers sit 3/8 in behind the tip. Verify: GR8 on the Master4, then the overhang gauge on the finished shell"],
    ["GR6", "Pocket width: must clear the Grado body", 21.0, "PH", "mm", "Calipers on the Master4. Sized from the Opus3's 20.1 mm; Grado says the Master4 housing was reshaped. Must be at least HD27"],

    // Shell body.
    ["HD1", "Body length", 40, "PH", "mm", "Original shell, but the pocket must clear the Master4. Opus3 is 29.6 mm with pins; Master4 unpublished"],
    ["HD2", "Body width", 25, "PH", "mm", "Original shell, but must clear the Master4. Opus3 is wider than some headshells; Master4 unpublished"],
    ["HD3", "Body height", 16, "PH", "mm", "Calipers on an original shell"],
    ["HD4", "Top thickness above the pocket", 3.5, "PH", "mm", "Screw length minus thread engagement in the Grado body"],
    ["HD5", "Front wall thickness", 2.5, "PH", "mm", "Keep at least 1 mm in PMMA; confirm with the maker"],
    ["HD6", "Rear wall thickness, carries the neck", 6.0, "PH", "mm", "Set by pin and neck construction"],
    ["HD7", "Body corner radius", 2.0, "PH", "mm", "Design freedom"],
    ["HD8", "Pocket corner radius: milling tool radius", 1.5, "D", "mm", "Design choice for a milled inside corner"],
    ["HD27", "Inside width, lower bound", 0.805 * IN, "DV", "in", "The 0.805 in shim block (community drawing, RDW 2023) lies across the inside of the original shell, so the inside is at least that wide. Verify: calipers on an original shell"],

    // Neck and connector: all must come from an original shell.
    ["HD10", "Neck outside diameter", 10, "PH", "mm", "Micrometer on an original neck"],
    ["HD11", "Neck length from the rear face", 12, "PH", "mm", "Calipers on an original neck"],
    ["HD12", "Neck axis height above the underside", 8, "PH", "mm", "Critical. Sets the mounting plane relative to the arm axis"],
    ["HD13", "Contact-pin circle diameter", 5.5, "PH", "mm", "Measure on the arm-end socket and an original shell"],
    ["HD14", "Contact-pin hole diameter", 1.6, "PH", "mm", "Set from the pins chosen"],

    // Finger lift.
    // An arc in plan, constant thickness in Z, so it is cut in the top setup.
    ["HD17", "Finger-lift width", 6, "PH", "mm", "Calipers on an original shell"],
    ["HD18", "Finger-lift thickness", 2.5, "PH", "mm", "PMMA is brittle; a thin tab can snap"],
    ["HD22", "Lift arc inner radius", 10, "PH", "mm", "Trace the lift of an original shell in plan"],
    ["HD23", "Lift root position from the front face", 4, "PH", "mm", "Calipers on an original shell"],
    ["HD24", "Lift arc sweep angle", 70, "PH", "deg", "Trace the lift of an original shell in plan"],
    ["HD25", "Lift side: +1 or -1", 1, "D", "", "Outer side, away from the platter. Right wall when facing the front on an XA. Confirm on an original shell"],
];

spacing = pv(P, "GR0");
slot_w = pv(P, "GR1");
rec_w = pv(P, "GR2");
rec_d = pv(P, "GR3");
slot_c = pv(P, "GR4");
stylus_x = pv(P, "GR13");
slot_x = stylus_x + pv(P, "GR5");   // the studs sit behind the stylus, toward the neck
pocket_w = pv(P, "GR6");
assert(pocket_w >= pv(P, "HD27"), "GR6 is narrower than the shim block, HD27");

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

lift_w = pv(P, "HD17");
lift_t = pv(P, "HD18");
lift_r = pv(P, "HD22");
lift_x = pv(P, "HD23");
lift_a = pv(P, "HD24");
lift_side = pv(P, "HD25");

pocket_l = body_l - wall_f - wall_r;
pocket_x = (wall_f - wall_r) / 2;
pocket_h = body_h - top_t;

// Finger lift. Local frame: u along X, v outward from the side wall. The lift
// is an annular arc whose outer surface is tangent to the wall at the root and
// curls outward toward the front. Both inside corners at the root get a
// fillet of the cutter radius HD8.
lift_ys = -lift_side;                 // +1 side is the right wall seen from the front: model -Y
lift_ro = lift_r + lift_w;            // outer radius
lift_f = r_pocket;                    // root fillet radius
lift_u0 = -body_l / 2 + lift_x;       // root
lift_c = [lift_u0, lift_ro - EPS];    // arc center
lift_k = [-body_l / 2 + r_body, -r_body];   // body corner center
lift_out = lift_c[1] - lift_r * cos(min(lift_a, 90));   // farthest reach from the wall

function dist(a, b) = norm(a - b);
// The intersection of two circles that lies farther toward the front.
function meet(c1, r1, c2, r2) =
    let (d = dist(c1, c2), a = (r1 * r1 - r2 * r2 + d * d) / (2 * d),
         h = sqrt(r1 * r1 - a * a), u = (c2 - c1) / d,
         m = c1 + a * u, n = [-u[1], u[0]] * h)
    (m + n)[0] < (m - n)[0] ? m + n : m - n;

// Front fillet center: tangent to the lift and to the wall, or to the body's
// corner radius when the lift leaves the wall too close to the front.
lift_on_wall = lift_u0 - sqrt(pow(lift_ro + lift_f, 2) - pow(lift_c[1] - lift_f, 2));
lift_wall_case = lift_on_wall >= lift_k[0];
lift_fc = lift_wall_case ? [lift_on_wall, lift_f]
                         : meet(lift_k, r_body + lift_f, lift_c, lift_ro + lift_f);
// Fill between the lift and the body, as far as the fillet's tangent line.
lift_fill = [
    lift_wall_case ? [lift_on_wall, -1] : lift_k,
    lift_fc,
    lift_c + (lift_fc - lift_c) * (lift_ro - 1) / (lift_ro + lift_f),
    [lift_u0, -1],
];
// Angle of the front fillet's tangent point, from the root: it must lie on the lift.
lift_fa = atan2(lift_c[0] - lift_fc[0], lift_c[1] - lift_fc[1]);
assert(lift_fa < lift_a, "HD24 is too small for the root fillet");
assert(lift_f < lift_w, "HD8 must be smaller than HD17");

function lift_xy(p) = [p[0], lift_ys * (body_w / 2 + p[1])];
function lift_poly(pts) = lift_ys > 0 ? [for (p = pts) lift_xy(p)]
                                      : [for (i = [len(pts) - 1 : -1 : 0]) lift_xy(pts[i])];

module finger_lift() {
    translate([0, 0, body_h - lift_t]) {
        // The arc.
        translate(lift_xy(lift_c))
            rotate([0, 0, lift_ys > 0 ? 270 - lift_a : 90])
                rotate_extrude(angle = lift_a)
                    polygon([[lift_r, 0], [lift_ro, 0], [lift_ro, lift_t], [lift_r, lift_t]]);
        // Front fillet.
        difference() {
            linear_extrude(height = lift_t) polygon(lift_poly(lift_fill));
            translate(concat(lift_xy(lift_fc), [-1])) cylinder(r = lift_f, h = lift_t + 2);
        }
        // Rear fillet.
        difference() {
            linear_extrude(height = lift_t)
                polygon(lift_poly([[lift_u0 - 0.5, -1], [lift_u0 - 0.5, lift_f],
                                   [lift_u0 + lift_f, lift_f], [lift_u0 + lift_f, -1]]));
            translate(concat(lift_xy([lift_u0 + lift_f, lift_f]), [-1])) cylinder(r = lift_f, h = lift_t + 2);
        }
    }
}

module part() {
    difference() {
        union() {
            rr_prism(body_l, body_w, body_h, r_body);
            // Neck, overlapping into the rear wall.
            translate([body_l / 2 - 1, 0, neck_z])
                rotate([0, 90, 0]) cylinder(d = neck_d, h = neck_l + 1);
            // Finger lift on a side wall, flush with the top.
            finger_lift();
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
        ["id", "headshell-top-mount-pmma"],
        ["title", "Headshell, top-mount for a Grado Master4, PMMA"],
        ["status", "CONCEPT"],
        ["part", "parts/headshell.md"],
        ["part_name", "Headshell"],
        ["version", "Top-mount shell for a Grado Master4: this repository's design, not an AR part"],
        ["scope", "New design for a Grado Master4. Layout from the XA service manual, p. 4. Not an AR dimension set"],
        ["material", "PMMA (acrylic), cast grade preferred"],
        ["density", 1.18],
        ["fits", [["XA", "Unconfirmed", ""], ["XB", "Unconfirmed", ""], ["AR77XB", "Unconfirmed", ""]]],
        ["target_mass_g", 7],
        ["target_mass_source", "Villchur 1962, Part 1, p. 23: the acrylic shell weighed 7 g"],
        ["make", "Mill from the top, the bottom, and the neck end. The lift is cut in the top setup. Print a test piece first"],
        ["views", ["front", "top", "bottom", "right", "left", "iso"]],
        ["sections", [["A", "y", 6.35]]],
        ["notes", [
            "Nothing fits any table yet: the neck, pins and mounting height (HD10 to HD14) are placeholders. Pat's Audio sells one shell for the XA and XB, so one neck may serve both; that is a maker claim, not a measurement.",
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
        ["front", "cl", [body_l / 2 - 3, 0, neck_z], [body_l / 2 + neck_l + 2, 0, neck_z]],
        ["top", "v", [body_l / 2, -body_w / 2, 0], [body_l / 2, body_w / 2, 0], 22, "HD2"],
        ["top", "v", [slot_x, -spacing / 2, 0], [slot_x, spacing / 2, 0], 9, "GR0"],
        ["top", "h", [slot_x - slot_c / 2, body_w / 2, 0], [slot_x + slot_c / 2, body_w / 2, 0], 9, "GR4"],
        ["top", "d", [slot_x + slot_c / 2, spacing / 2, 0], rec_w / 2, 13, "GR2", "W ", 50],
        ["top", "d", [slot_x - slot_c / 2, spacing / 2, 0], slot_w / 2, 13, "GR1", "W ", 135],
        // Stylus position and slot offset, under the front view, below HD1.
        ["front", "h", [stylus_x, 0, 0], [slot_x, 0, 0], -19, "GR5", "", "stylus to slot"],
        ["front", "h", [0, 0, 0], [stylus_x, 0, 0], -25, "GR13", "", "center to stylus"],
        ["front", "cl", [stylus_x, 0, -2], [stylus_x, 0, 6]],
        ["front", "cl", [0, 0, -2], [0, 0, 4]],
        // Lift, in plan. Labels sit to the front of the arc center, clear of the other dimensions.
        ["top", "r", concat(lift_xy(lift_c), [0]), lift_r, lift_ys > 0 ? 270 - lift_a / 4 : 90 + lift_a / 4, "HD22", -17, -lift_ys * 3.5, "right"],
        ["top", "a", concat(lift_xy(lift_c), [0]), lift_r - 3, lift_ys > 0 ? 270 - lift_a : 90, lift_ys > 0 ? 270 : 90 + lift_a, "HD24", -17, 0, "right"],
        ["top", "h", [-body_l / 2, lift_ys * body_w / 2, 0], [lift_u0, lift_ys * body_w / 2, 0], lift_ys * 9, "HD23"],
        ["bottom", "v", [body_l / 2, -pocket_w / 2, 0], [body_l / 2, pocket_w / 2, 0], 9, "GR6"],
        ["bottom", "h", [-body_l / 2, body_w / 2, 0], [-body_l / 2 + wall_f, body_w / 2, 0], -9, "HD5"],
        ["bottom", "h", [body_l / 2 - wall_r, body_w / 2, 0], [body_l / 2, body_w / 2, 0], -9, "HD6"],
        ["right", "d", [0, 0, neck_z], neck_d / 2, 9, "HD10", "Ø", 60],
        ["right", "d", [0, pin_c / 2 * cos(315), neck_z + pin_c / 2 * sin(315)], pin_d / 2, 9, "HD14", "Ø", 300],
        ["right", "h", [0, lift_ys * body_w / 2, body_h], [0, lift_ys * (body_w / 2 + lift_w), body_h], 16, "HD17"],
        ["right", "v", [0, lift_ys * (body_w / 2 + lift_out), body_h - lift_t], [0, lift_ys * (body_w / 2 + lift_out), body_h], lift_ys * 9, "HD18"],
        ["A", "v", [body_l / 2, 0, pocket_h], [body_l / 2, 0, body_h], 9, "HD4"],
        ["A", "v", [-body_l / 2, 0, body_h - rec_d], [-body_l / 2, 0, body_h], -9, "GR3"],
    ]
);

if (flat) projection() part(); else part();
