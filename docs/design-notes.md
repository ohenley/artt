# Villchur's turntable design papers

[Home](../README.md) · [Document index](README.md)

Working notes on the two papers. They describe the early design, not each later revision.

## Part 1: September 1962

Edgar Villchur, **A New Turntable-Arm Design**, *Audio*, printed pp. 19–23, 68–69. [Local scan](originals/villchur-1962-part-1.pdf)

Villchur treats the platter bearing and tonearm as one mechanical system: what matters is unwanted motion between them. A common suspended frame isolates both from the surroundings and the motor. He also covers arm balance, warp-induced speed variation, bearing friction, and tracking geometry.

Page 69 gives the effective arm length, overhang, and output-cable capacitance, recorded on the [XA page](../models/xa/README.md). Assess a spring or arm modification against the complete moving assembly.

### Setup facts from Part 1

All Factory, from the [local scan](originals/villchur-1962-part-1.pdf). Printed page numbers.

- **Suspension resonance, p. 20.** The springs are chosen with the formula F = (10/D)^½, where F is the resonant frequency in cps and D is the static deflection of the spring in inches under its share of the load. For 3.5 cps the static deflection is 13/16 in (about 20.6 mm). With three springs, each is tested with one third of the suspended weight. Foam washers centre the springs and add light damping.
- **Shell material and mass, p. 22, "Tonearm Mass".** The first prototype had an aluminium cartridge shell, heavier than desired. Changing to "an acrylic plastic" reduced the weight "by more than half, to 7 grams", which also reduced the counterweight mass needed. This describes the design in 1962, not every later shell: see HS4 and HD21 in [TO-CONFIRM](../TO-CONFIRM.md).
- **Arm resonance and motor frequency, p. 22.** The drive motor's fundamental is 6⅔ cps (400 rpm). The arm resonance is "in the 10-cps region with typical stereo cartridges" and should not fall too close to it.
- **Damping release, p. 23, "Tonearm Pivot" and Fig. 6.** The arm drop is damped so the arm takes several seconds to reach the record. A stopper pin on a porous bronze shaft soaked in silicone fluid turns in a Delrin sleeve; the silicone gives the drag. Once the stylus is on the record the stopper hole and pin no longer touch, so the arm moves freely on its operating pivot (polished steel conical set screws in Delrin bearings) over a small vertical distance at the stylus. Lifting the arm by hand resets the mechanism. Horizontal motion is never damped. The drag is set by the pressure on a spring-loaded washer against the shaft, changed by turning the tonearm spindle relative to the arm. The free vertical distance is printed as a fraction the text layer cannot read: [illegible], see the scan.
- **Tracking error, pp. 23, 68, 69.** The turntable is factory-set for a cartridge with ⅜ in (9.5 mm) between the mounting-hole centres and the needle tip. For other cartridges the effective arm length is adjusted and checked with a plastic template over the spindle: with the needle in the template hole, the overhang is 0.688 in (17.48 mm). A 9 in (228.6 mm) arm designed for record radii of 5.7 in (144.8 mm) outside and 2.4 in (61.0 mm) inside has a maximum tracking error index of 0.32 degrees per inch. The largest tracking error on the record is at the outermost groove, 1.8 degrees. The offset angle is not printed. The arm tube is formed on a permanent die to hold the offset angle in production.

### Setup facts from the XA service manual

Factory, [XA service manual](originals/xa-service-manual.pdf). The 1969 scans on Vinyl Nirvana are the same revision: [comparison](transcripts/xa-service-manual-1969-comparison.md).

- **Shell and socket, p. 1.** Turning the shell while tightening the knurled retaining nut can deform the plastic receptacle at the end of the arm. Straighten the shell by hand while retightening the nut; if the deformation is large, the arm may need replacing.
- **Sideways force, p. 1.** AR's correction for the lack of an anti-skating device is to increase the tracking force by no more than ¼ gram. The thin wire cable leaving the rear of the arm, if not positioned as in the operating manual, can exert several tenths of a gram of sideways force. A gross difference in how far each pivot set screw is tightened into the coupler block can do the same.
- **Damping, p. 1.** A defective damping mechanism is the most common cause of skating complaints. The damping was omitted from serial XA236534. AR recommends disabling it on every XA.
- **Disabling the damping, p. 2, "Vertical Pivot Assembly".** Remove the vertical pivot screws and lift the arm off the pivot assembly. Clean and oil the spindle. Tighten the spindle into the pivot and pull out the small steel damping pin in the side of the brass bearing. Refit the arm with the pivot screws seated in the plastic bearing inserts.
- **Pivot screws, p. 2.** Tighten "just enough to allow a small amount of play in the pivot".
- **Arm spindle, p. 1.** Without the small ball bearing under the spindle, sideways pivot friction rises and the stylus skips or sticks. A small disc must be in the spindle well before the spindle goes in.
- **Speed, p. 2.** Check with a strobe disc: no more than plus or minus 21 dots per minute. Speed is raised with a shim under the end of the motor nearest the rear, lowered with a shim near the screw nearest the platter. Slow start or chattering at start-up: replace the belt and clean the pulley.
- **Suspension, p. 2.** With a heavy record in place, tighten the three suspension retaining nuts until the bottom of the outer platter is ⅛ in (3.2 mm) above the top plate at all points.
- **Before opening, p. 2.** Unplug the table. Remove the mat, outer platter, shell and counterweight. Brace the unit on its side and secure the arm to its rest. Do not turn it upside down.

### Setup facts from the owner's papers

Factory. Full text: [XA owner's manual](transcripts/xa-owners-manual.md), [needle force gauge sheet](transcripts/needle-force-gauge.md), [sheet L-1591](transcripts/ar-cartridge-mount-l-1591.md), [XB1 manual](transcripts/xb1-owners-manual.md).

- **Stylus force, XA manual p. 5 and gauge sheet.** Tighten the spindle until the arm front does not fall. Check that a light tap moves the arm equally freely both ways; if not, re-dress the arm cable. Force the arm down to roughly parallel with the record so the damping cannot affect the reading, then weigh the force on the AR gauge. Gauge weights are ¼, ½, 1 and 2 g; a U.S. penny serves as 3 g above 3¾ g. On the gauge, move the arm as far down as it goes to release the damping. If the gauge sticks at both ends, the pivot is tight.
- **Counterweight sensitivity, XA manual p. 5 and XB1 manual p. 6.** About 1/32 in (0.8 mm) of counterweight travel changes the stylus force by about ¼ g.
- **Lowest force, XA manual p. 5.** Any force down to ½ g may be used with the AR arm. Sheet L-1591 adds that no cartridge works satisfactorily below 1 g.
- **Damping rate, XA manual p. 7.** Unscrew the spindle a little at a time until the arm, lifted about 3 in above the record, takes two or three seconds to come down. Do not unscrew it further.

## Part 2: October 1962

Edgar Villchur, **A New Turntable-Arm Design**, *Audio*, printed pp. 34, 36, 38. [Local scan](originals/villchur-1962-part-2.pdf)

Covers synchronous motors, belt coupling, platter inertia, and the measurement of speed variation and rumble. Measurements made with different weighting, reference levels, or test conditions cannot be compared as raw numbers.

Record the test method with a restored table's speed, wow and flutter, or rumble results.
