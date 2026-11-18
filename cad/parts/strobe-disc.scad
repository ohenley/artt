// Strobe disc for checking platter speed under a mains-frequency lamp.
//
// Number of lines = 2 x mains frequency x 60 / speed in rpm.
// 60 Hz: 216 lines for 33 1/3 rpm, 160 for 45 rpm. 50 Hz: 180 lines for 33 1/3 rpm;
// 45 rpm gives 133.33, not a whole number, so that ring is not drawn at 50 Hz.
// The third PDF page prints the disc at 1:1 with the bars filled.
// Parameter IDs match TO-CONFIRM.md.
// License: CC BY-SA 4.0. See LICENSE at the repository root.
include <../lib/common.scad>

variant = 1;   // 1: 60 Hz mains, 2: 50 Hz mains
flat = false;

hz = variant == 1 ? 60 : 50;
n33 = 2 * hz * 60 / (100 / 3);     // 216 at 60 Hz, 180 at 50 Hz
n45 = 2 * hz * 60 / 45;            // 160 at 60 Hz, 133.33 at 50 Hz
draw45 = abs(n45 - round(n45)) < 1e-6;

P = concat([
    ["SD1", "Lines on the 33 1/3 rpm ring", n33, variant == 1 ? "F" : "DV", "lines",
        variant == 1 ? "AR spec sheet: a standard 216-line stroboscope card. Also 2 x 60 Hz x 60 s / 33.333 rpm = 216"
                     : "2 x 50 Hz x 60 s / 33.333 rpm = 180. Verify: the pattern stands still on a table known to run true"],
], draw45 ? [
    ["SD2", "Lines on the 45 rpm ring", n45, "DV", "lines", "2 x 60 Hz x 60 s / 45 rpm = 160. Verify: the pattern stands still on a table known to run true"],
] : [], [
    ["SD3", "Spindle hole diameter", 7.3, "PH", "mm", "Micrometer on the spindle; the hole should be a close fit"],
    ["SD4", "Disc outside diameter", 100, "D", "mm", "Design choice: fits an A4 or letter sheet and the label area of a record"],
    ["SD5", "Ring width, each", 6, "D", "mm", "Design choice"],
    ["SD6", "Card thickness", 0.5, "D", "mm", "Design choice: print on card, or print on paper and glue to card"],
    ["SD7", "AR speed limit: lines of drift per minute", 21, "F", "lines", "AR spec sheet: +/- 0.3 percent, or 21 lines per minute on a 216-line card. XA service manual p. 1 and XB drawing 119 test A give the same 21 dots per minute"],
]);

sd = pv(P, "SD3");
od = pv(P, "SD4");
ring = pv(P, "SD5");
t = pv(P, "SD6");
bar_h = 0.2;    // raised bars on the model; on paper they are ink

// One ring of n bars as a single polygon: a gear whose teeth are the bars.
function ring_points(n, ro, ri) = [
    for (k = [0 : n - 1]) each
        let (a0 = k * 360 / n, a1 = a0 + 180 / n)
        [[ri * cos(a0), ri * sin(a0)], [ro * cos(a0), ro * sin(a0)],
         [ro * cos(a1), ro * sin(a1)], [ri * cos(a1), ri * sin(a1)]]
];
// The same bars as separate quads, for the filled 1:1 print page.
function ring_fills(n, ro, ri) = [
    for (k = [0 : n - 1])
        let (a0 = k * 360 / n, a1 = a0 + 180 / n)
        [[ro * cos(a0), ro * sin(a0)], [ro * cos(a1), ro * sin(a1)],
         [ri * cos(a1), ri * sin(a1)], [ri * cos(a0), ri * sin(a0)]]
];

ro33 = od / 2 - 1;
ri33 = ro33 - ring;
ro45 = ri33 - 2;
ri45 = ro45 - ring;

module part() {
    difference() {
        union() {
            cylinder(d = od, h = t);
            translate([0, 0, t - EPS]) linear_extrude(height = bar_h + EPS) polygon(ring_points(n33, ro33, ri33));
            if (draw45)
                translate([0, 0, t - EPS]) linear_extrude(height = bar_h + EPS) polygon(ring_points(round(n45), ro45, ri45));
        }
        translate([0, 0, -1]) cylinder(d = sd, h = t + bar_h + 2);
    }
}

fills = concat(ring_fills(n33, ro33, ri33), draw45 ? ring_fills(round(n45), ro45, ri45) : []);

emit(
    [
        ["id", str("strobe-disc-", hz, "hz-card")],
        ["title", str("Strobe disc, ", hz, " Hz mains")],
        ["status", "PRELIMINARY"],
        ["part", "parts/strobe-disc.md"],
        ["part_name", "Strobe disc"],
        ["version", str(hz, " Hz mains: outer ring 33 1/3 rpm", draw45 ? ", inner ring 45 rpm" : "; no 45 rpm ring, see note 1")],
        ["scope", "New. Line counts from the mains frequency and the speeds; AR's own card is not held"],
        ["material", "Card, or paper glued to card"],
        ["density", 0.7],
        ["fits", hz == 60
            ? [["XA", "Fits", "AR spec sheet: speed held to 21 lines a minute on a 216-line card; XA service manual p. 1"],
               ["XB", "Fits", "drawing 119, performance test A: +/- 21 dots per minute"],
               ["AR77XB", "Unconfirmed", ""],
               ["The AR Turntable and Legend", "Fits", "1983 brochure: 33 1/3 and 45 rpm at 60 Hz"],
               ["EB-101", "Fits", "GB brochure: 33 1/3 and 45 rpm"]]
            : [["XA", "Fits", "XA service manual p. 1: a 50-cycle pulley gives the same speeds on 50 Hz"],
               ["XB1", "Unconfirmed", ""],
               ["The AR Turntable and Legend", "Fits", "1983 brochure: 33 1/3 and 45 rpm at 50 Hz"],
               ["EB-101", "Fits", "GB brochure: 33 1/3 and 45 rpm"]]],
        ["make", "Print page 3 at 100 percent on card. Cut the outline and the spindle hole"],
        ["flat", true],
        ["print_1to1", true],
        ["print_fills", fills],
        ["print_notes", [
            str("Lines: ", n33, " on the outer ring for 33 1/3 rpm", draw45 ? str(", ", n45, " on the inner ring for 45 rpm") : str(". At ", hz, " Hz the 45 rpm count is ", n45, ", not a whole number, so that ring is not drawn")),
            "Light the disc with a lamp on the mains, not an LED or a flashlight. The pattern stands still at the right speed.",
            "AR's limit: no more than 21 lines of drift in a minute (AR spec sheet), which is 0.29 percent of the 7,200 lines that pass in a minute at 33 1/3 rpm.",
            "The spindle hole SD3 is a placeholder: measure your spindle first.",
        ]],
        ["variants", [[1, "60 Hz mains"], [2, "50 Hz mains"]]],
        ["views", ["front", "top"]],
        ["notes", [
            draw45 ? str("Lines = 2 x mains frequency x 60 / rpm: ", n33, " and ", n45, " at ", hz, " Hz.")
                   : str("Lines = 2 x mains frequency x 60 / rpm: ", n33, " at ", hz, " Hz for 33 1/3 rpm. For 45 rpm the result is ", n45, ", not a whole number: that ring is not drawn, because a rounded count would read a wrong speed as right."),
            "A 60 Hz disc read under a 50 Hz lamp, or the reverse, gives a wrong result. Use the disc for your mains.",
            "AR's limit is 21 lines of drift per minute: 0.29 percent of the 7,200 lines a minute at 33 1/3 rpm. The XB test is at 1.5 g stylus force; the spec sheet adds 5 g to stand in for a dust brush.",
            "Page 3 is the disc at 1:1 with the bars filled. The DXF outline is for engraving or cutting.",
        ]],
    ],
    P,
    [
        ["top", "d", [0, 0, 0], sd / 2, 9, "SD3", "Ø", 45],
        ["top", "d", [0, 0, 0], od / 2, 9, "SD4", "Ø", 135],
        ["front", "v", [od / 2, 0, 0], [od / 2, 0, t], 9, "SD6"],
        ["top", "h", [ri33, -od / 2, 0], [ro33, -od / 2, 0], -9, "SD5"],
    ]
);

if (flat) projection() part(); else part();
