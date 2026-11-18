// Shared helpers for the AR turntable part models.
//
// Every part file holds a parameter table P. Each row is:
//   [id, description, value_mm, evidence, display_unit, source_or_how_to_check]
//
// Evidence codes:
//   F  factory document          O  owner report
//   C  community drawing         S  industry standard
//   D  design choice             M  measured for this repository
//   DV derived from cited sources, not yet verified on a part. The source
//      column holds the derivation: the formula, each input with its source,
//      and how to verify. Drawn in blue. Needs a row in TO-CONFIRM.md whose
//      value starts with "Derived:". Change to M once measured.
//   PH placeholder: chosen only so the model has a shape. It is NOT a
//      measurement. Drawn in red. Replace it, and change the code, once it
//      is measured.
//
// Every part file also emits metadata naming the part page, the part, the
// version, the material and the tables it fits, each fit with its evidence:
//   ["part", "parts/counterweight.md"], ["part_name", "Counterweight"],
//   ["version", "XA brass weight, 1961 to 1979"], ["material", "Brass"],
//   ["fits", [["XA", "Fitted by AR", "XA service manual p. 4"], ["XB", "Unconfirmed", ""]]]
// The fit word is one of: Fitted by AR, Fits, Fits with a change, Does not
// fit, Unconfirmed. build.py prints these in the title block and writes the
// drawings table of cad/README.md from them.
// License: CC BY-SA 4.0. See LICENSE at the repository root.

IN = 25.4;      // one inch, in mm. All model geometry is in mm.
EPS = 0.01;     // overlap so boolean cuts do not leave zero-thickness skins
$fa = 2;
$fs = 0.1;

// Value of parameter `id` in table t.
function pv(t, id) = t[search([id], t)[0]][2];

// Print part data for cad/tools/build.py, which reads it from the console.
module emit(meta, params, dims = []) {
    echo(META = meta);
    for (row = params) echo(PARAM = row);
    for (row = dims) echo(DIM = row);
}

// Rounded rectangle prism: centered in XY, from z = 0 to z = h.
module rr_prism(l, w, h, r) {
    translate([-l / 2 + r, -w / 2, 0]) cube([l - 2 * r, w, h]);
    translate([-l / 2, -w / 2 + r, 0]) cube([l, w - 2 * r, h]);
    for (sx = [-1, 1], sy = [-1, 1])
        translate([sx * (l / 2 - r), sy * (w / 2 - r), 0]) cylinder(r = r, h = h);
}

// Slot along X: `c` is the distance between end-radius centers.
module slot_prism(c, w, h) {
    translate([-c / 2, -w / 2, 0]) cube([c, w, h]);
    for (sx = [-1, 1]) translate([sx * c / 2, 0, 0]) cylinder(d = w, h = h);
}
