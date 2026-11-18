// XA plinth with cutouts for an RCA jack plate, a ground post, and a fused
// IEC inlet, plus a bottom panel drilled for the terminal strip and feet.
//
// CONCEPT ONLY. No drawing of the AR base has been found. The outside size
// comes from the 1969 listing, which includes the cover; every other body
// dimension is a placeholder. Do not cut hardwood until the PH rows are measured.
//
// Axes: X along the front edge, Y front to back with the rear at +Y, Z up.
// z = 0 is the bottom face of the base. Origin at the base center in XY.
// Variant 1 is the base. Variant 2 is the bottom panel.
// License: CC BY-SA 4.0. See LICENSE at the repository root.
include <../lib/common.scad>

variant = 1;
flat = false;  // true exports the 1:1 cutting outline

P = [
    // Body.
    ["PL10", "Outside length", 16.75 * IN, "DV", "in", "The 16 3/4 in size is with the cover on (Audio 1969 directory; AR brochure); the base alone may be smaller. Verify: rule on an original base"],
    ["PL11", "Outside width", 12.75 * IN, "DV", "in", "The 12 3/4 in size is with the cover on (same two sources); the base alone may be smaller. Verify: rule on an original base"],
    ["PL12", "Base height, no feet", 110, "PH", "mm", "Calipers or rule on an original base"],
    ["PL13", "Wall thickness, front and rear", 19, "PH", "mm", "Calipers"],
    ["PL14", "Wall thickness, sides", 19, "PH", "mm", "Calipers"],
    ["PL15", "Top rebate depth", 3, "PH", "mm", "Calipers; the top plate thickness"],
    ["PL16", "Top rebate ledge width", 10, "PH", "mm", "Calipers"],
    ["PL17", "Bottom panel thickness; also its rebate width", 6, "PH", "mm", "Calipers on the bottom panel"],
    ["PL18", "Bottom panel rebate depth", 6, "PH", "mm", "Calipers"],
    ["PL19", "Corner block size", 25, "PH", "mm", "Calipers on an original corner brace"],
    ["PL20", "Corner block height", 60, "PH", "mm", "Calipers on an original corner brace"],
    ["PL21", "Foot hole diameter", 6, "PH", "mm", "From the feet chosen"],
    ["PL22", "Foot inset from each corner of the bottom panel", 30, "PH", "mm", "Rule on the original panel"],

    // RCA jack plate and ground post, in the rear wall.
    ["PL30", "RCA cutout: window width", 4.125 * IN, "O", "in", "Galo: a rectangular cutout about 1 3/8 x 4 1/8 in for his connector plate. Set from your plate"],
    ["PL31", "RCA cutout: window height", 1.375 * IN, "O", "in", "Galo: the same cutout. Set from your plate"],
    ["PL32", "RCA cutout: center X from base center", 100, "PH", "mm", "Clear of the T-bar swing and the motor"],
    ["PL33", "RCA cutout: center Z from bottom", 55, "PH", "mm", "Clear of the top plate parts and the bottom panel"],
    ["PL34", "Ground post hole diameter", 6.5, "PH", "mm", "From the post chosen"],
    ["PL35", "Ground post X from RCA window center", 70, "PH", "mm", "Clear of the plate and the corner block"],
    ["PL36", "Plate screw hole diameter", 3.2, "D", "mm", "Pilot or clearance for the plate screws chosen"],
    ["PL37", "Plate screw offset outside each window corner", 8, "D", "mm", "Set from the plate's screw pattern"],

    // Fused IEC inlet, in the rear wall.
    ["PL40", "IEC cutout width", 27.5, "PH", "mm", "A common fused C14 inlet figure; no datasheet is held (SR26). Set from the chosen part's datasheet"],
    ["PL41", "IEC cutout height", 31, "PH", "mm", "A common fused C14 inlet figure; no datasheet is held (SR26). Set from the chosen part's datasheet"],
    ["PL42", "IEC cutout center X from base center", -120, "PH", "mm", "Clear of the motor, switch, and capacitors"],
    ["PL43", "IEC cutout center Z from bottom", 55, "PH", "mm", "Clear of the top plate parts and the bottom panel"],
    ["PL44", "IEC mounting hole spacing", 40, "PH", "mm", "A common fused C14 inlet figure; no datasheet is held (SR26). Set from the chosen part's datasheet"],
    ["PL45", "IEC mounting hole diameter", 3.2, "PH", "mm", "From the inlet's datasheet and screws"],

    // Audio terminal strip, on the bottom panel.
    ["PL50", "Terminal strip position X", 0, "PH", "mm", "Under the arm wire exit; measure the stock strip"],
    ["PL51", "Terminal strip position Y, from the rear wall inside face", 30, "PH", "mm", "Rule on the original panel"],
    ["PL52", "Terminal strip mounting hole diameter", 2.5, "PH", "mm", "From the strip's screws"],
    ["PL53", "Terminal strip mounting hole spacing", 50, "PH", "mm", "Calipers on the strip"],
];

len_x = pv(P, "PL10");
wid_y = pv(P, "PL11");
height = pv(P, "PL12");
wall_fr = pv(P, "PL13");
wall_s = pv(P, "PL14");
top_d = pv(P, "PL15");
top_w = pv(P, "PL16");
panel_t = pv(P, "PL17");
panel_d = pv(P, "PL18");
block = pv(P, "PL19");
block_h = pv(P, "PL20");
foot_d = pv(P, "PL21");
foot_in = pv(P, "PL22");

rca_w = pv(P, "PL30");
rca_h = pv(P, "PL31");
rca_x = pv(P, "PL32");
rca_z = pv(P, "PL33");
post_d = pv(P, "PL34");
post_x = rca_x + pv(P, "PL35");
screw_d = pv(P, "PL36");
screw_off = pv(P, "PL37");

iec_w = pv(P, "PL40");
iec_h = pv(P, "PL41");
iec_x = pv(P, "PL42");
iec_z = pv(P, "PL43");
iec_c = pv(P, "PL44");
iec_d = pv(P, "PL45");

strip_x = pv(P, "PL50");
strip_y = wid_y / 2 - wall_fr - pv(P, "PL51");
strip_d = pv(P, "PL52");
strip_c = pv(P, "PL53");

in_x = len_x - 2 * wall_s;      // inside opening
in_y = wid_y - 2 * wall_fr;
panel_x = in_x + 2 * panel_t;   // bottom panel outline
panel_y = in_y + 2 * panel_t;
rear_y = wid_y / 2 - wall_fr;   // inside face of the rear wall
ledge_z = height - top_d;       // top plate ledge

// A box centered in XY, from z0 up.
module box(x, y, z0, h) {
    translate([-x / 2, -y / 2, z0]) cube([x, y, h]);
}

// A hole through the rear wall, along Y.
module rear_hole(x, z, d) {
    translate([x, rear_y - 1, z]) rotate([-90, 0, 0]) cylinder(d = d, h = wall_fr + 2);
}

// A rectangular window through the rear wall.
module rear_window(x, z, w, h) {
    translate([x - w / 2, rear_y - 1, z - h / 2]) cube([w, wall_fr + 2, h]);
}

module base() {
    difference() {
        union() {
            difference() {
                box(len_x, wid_y, 0, height);
                // Inside opening, through the top and the bottom.
                box(in_x, in_y, -1, height + 2);
            }
            // Corner blocks, top flush with the ledge.
            for (sx = [-1, 1], sy = [-1, 1])
                translate([sx * (in_x / 2 - block / 2), sy * (in_y / 2 - block / 2), 0])
                    box(block + 2, block + 2, ledge_z - block_h, block_h);
        }
        // Top rebate for the top plate.
        box(in_x + 2 * top_w, in_y + 2 * top_w, ledge_z, top_d + 1);
        // Bottom rebate for the bottom panel.
        box(panel_x, panel_y, -1, panel_d + 1);
        // RCA plate window and its four screw holes.
        rear_window(rca_x, rca_z, rca_w, rca_h);
        for (sx = [-1, 1], sz = [-1, 1])
            rear_hole(rca_x + sx * (rca_w / 2 + screw_off), rca_z + sz * (rca_h / 2 + screw_off), screw_d);
        // Ground post.
        rear_hole(post_x, rca_z, post_d);
        // IEC inlet window and its two mounting holes.
        rear_window(iec_x, iec_z, iec_w, iec_h);
        for (sx = [-1, 1]) rear_hole(iec_x + sx * iec_c / 2, iec_z, iec_d);
    }
}

module bottom_panel() {
    difference() {
        box(panel_x, panel_y, 0, panel_t);
        // Terminal strip.
        for (sx = [-1, 1])
            translate([strip_x + sx * strip_c / 2, strip_y, -1]) cylinder(d = strip_d, h = panel_t + 2);
        // Feet.
        for (sx = [-1, 1], sy = [-1, 1])
            translate([sx * (panel_x / 2 - foot_in), sy * (panel_y / 2 - foot_in), -1])
                cylinder(d = foot_d, h = panel_t + 2);
    }
}

module part() {
    if (variant == 1) base(); else bottom_panel();
}

common_notes = [
    "All body dimensions are placeholders until a base is measured. The 16 3/4 x 12 3/4 in outside size (PL10, PL11) is the listed size with the cover on: the base alone may be smaller.",
];

base_meta = [
    ["views", ["front", "top", "rear", "right", "iso"]],
    ["view_scales", [["rear", 0.4]]],
    ["sections", [["A", "x", rca_x]]],
    ["notes", concat(common_notes, [
        "Place the rear cutouts clear of the T-bar swing. Measure the closest approach of the subchassis and the motor to the rear wall before cutting.",
        "IEC cutout dimensions must come from the chosen inlet's datasheet.",
    ])],
];

panel_meta = [
    ["views", ["front", "top", "iso"]],
    ["notes", concat(common_notes, [
        str("Panel outline is derived: the inside opening plus PL17 on every side, ", panel_x, " x ", panel_y, " mm with these values."),
        "PL51 is measured from the inside face of the rear wall, which lies PL17 inside the panel's rear edge.",
    ])],
];

// In the rear view +X is on the left.
base_dims = [
    ["front", "v", [-len_x / 2, 0, 0], [-len_x / 2, 0, height], -9, "PL12"],
    ["top", "h", [-len_x / 2, wid_y / 2, 0], [len_x / 2, wid_y / 2, 0], 9, "PL10"],
    ["top", "v", [len_x / 2, -wid_y / 2, 0], [len_x / 2, wid_y / 2, 0], 9, "PL11"],
    ["top", "h", [-len_x / 2, -wid_y / 2, 0], [-len_x / 2 + wall_s, -wid_y / 2, 0], -9, "PL14"],
    ["top", "h", [in_x / 2 - block, -wid_y / 2, 0], [in_x / 2, -wid_y / 2, 0], -9, "PL19"],

    ["rear", "h", [rca_x - rca_w / 2, 0, height], [rca_x + rca_w / 2, 0, height], 16, "PL30"],
    ["rear", "h", [0, 0, height], [iec_x, 0, height], 9, "PL42"],
    ["rear", "h", [iec_x - iec_w / 2, 0, height], [iec_x + iec_w / 2, 0, height], 16, "PL40"],
    ["rear", "h", [rca_x, 0, 0], [post_x, 0, 0], -9, "PL35"],
    ["rear", "h", [0, 0, 0], [rca_x, 0, 0], -9, "PL32"],
    ["rear", "h", [iec_x - iec_c / 2, 0, 0], [iec_x + iec_c / 2, 0, 0], -9, "PL44"],
    ["rear", "v", [len_x / 2, 0, 0], [len_x / 2, 0, rca_z], -9, "PL33"],
    ["rear", "v", [len_x / 2, 0, rca_z - rca_h / 2], [len_x / 2, 0, rca_z + rca_h / 2], -15, "PL31"],
    ["rear", "v", [-len_x / 2, 0, 0], [-len_x / 2, 0, iec_z], 9, "PL43"],
    ["rear", "v", [-len_x / 2, 0, iec_z - iec_h / 2], [-len_x / 2, 0, iec_z + iec_h / 2], 15, "PL41"],
    ["rear", "d", [post_x, 0, rca_z], post_d / 2, 9, "PL34", "Ø", 75],
    ["rear", "d", [iec_x - iec_c / 2, 0, iec_z], iec_d / 2, 9, "PL45", "Ø", 300],
    ["rear", "cl", [rca_x, 0, -3], [rca_x, 0, height + 3]],
    ["rear", "cl", [iec_x, 0, -3], [iec_x, 0, height + 3]],
    ["rear", "cl", [0, 0, -3], [0, 0, height + 3]],

    ["A", "h", [0, rear_y, 0], [0, wid_y / 2, 0], -9, "PL13"],
    ["A", "h", [0, -rear_y - panel_t, 0], [0, -rear_y, 0], -9, "PL17"],
    ["A", "h", [0, rear_y, height], [0, rear_y + top_w, height], 9, "PL16"],
    ["A", "v", [0, -wid_y / 2, ledge_z], [0, -wid_y / 2, height], -9, "PL15"],
    ["A", "v", [0, wid_y / 2, 0], [0, wid_y / 2, panel_d], 19, "PL18"],
    ["A", "v", [0, -wid_y / 2, ledge_z - block_h], [0, -wid_y / 2, ledge_z], -15, "PL20"],
];

panel_dims = concat([
    ["top", "h", [strip_x - strip_c / 2, panel_y / 2, 0], [strip_x + strip_c / 2, panel_y / 2, 0], 9, "PL53"],
    ["top", "v", [panel_x / 2, strip_y, 0], [panel_x / 2, rear_y, 0], 9, "PL51"],
    ["top", "h", [-panel_x / 2, -panel_y / 2, 0], [-panel_x / 2 + foot_in, -panel_y / 2, 0], -9, "PL22"],
    ["top", "v", [-panel_x / 2, -panel_y / 2, 0], [-panel_x / 2, -panel_y / 2 + foot_in, 0], -9, "PL22"],
    ["top", "d", [panel_x / 2 - foot_in, -panel_y / 2 + foot_in, 0], foot_d / 2, 9, "PL21", "Ø", 300],
    ["top", "d", [strip_x - strip_c / 2, strip_y, 0], strip_d / 2, 9, "PL52", "Ø", 135],
    ["top", "cl", [strip_x, strip_y - 12, 0], [strip_x, strip_y + 12, 0]],
    ["front", "v", [panel_x / 2, 0, 0], [panel_x / 2, 0, panel_t], 9, "PL17"],
], strip_x == 0 ? [] : [
    ["top", "h", [0, -panel_y / 2, 0], [strip_x, -panel_y / 2, 0], -9, "PL50", "", "from panel center"],
]);

emit(
    concat([
        ["id", "plinth-xa-rebuild-hardwood"],
        ["title", "Plinth, XA rebuild with RCA plate, ground post and IEC inlet"],
        ["status", "CONCEPT"],
        ["part", "parts/plinth.md"],
        ["part_name", "Base or plinth"],
        ["version", "XA rebuild with new rear cutouts: this repository's design, not an AR part"],
        ["scope", "New design. No AR base drawing exists. Outside size from the 1969 listing"],
        ["material", "Hardwood or plywood for the test piece"],
        ["density", 0.65],
        ["fits", [["XA", "Unconfirmed", ""], ["XB", "Unconfirmed", ""], ["AR77XB", "Unconfirmed", ""]]],
        ["make", "Woodworking or CNC router. Cut the plywood test piece first"],
        ["flat", true],
        ["variants", [[1, "Base"], [2, "Bottom panel"]]],
    ], variant == 1 ? base_meta : panel_meta),
    P,
    variant == 1 ? base_dims : panel_dims
);

if (flat) projection() part(); else part();
