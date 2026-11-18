# Troubleshooting

[Home](../README.md) · [Document index](README.md) · Service: [XA](../models/xa/service.md), [XB](../models/xb/service.md), [AR77XB](../models/ar77xb/service.md)

One table per symptom. Each row is a likely cause, how to check it, the fix, and the source.

**Order of the rows.** Where a source ranks the causes, the table says so. Otherwise the order is our assessment: the quickest and cheapest check first.

**Which tables.** Almost every source here is a first-family paper: the XA owner's manual, the XA service manual, the XB1 manual and the XB drawings. Do not carry a value from one model to another. For The AR Turntable, EB-101, ES-1 and ETL-1 no service document is held; the checks below are given for comparison only.

**Unplug the table before you open it.** Remove the mat, outer platter, shell and counterweight, brace the table on its side and tie the arm to its rest. Never turn it upside down (Factory, [XA service manual, p. 2](originals/xa-service-manual.pdf)).

## Hum

| Order | Likely cause | How to check | Fix | Source |
| --- | --- | --- | --- | --- |
| 1 | The cartridge picks up the magnetic field of a power transformer in the amplifier, tuner or other equipment | The hum gets louder and softer with the amplifier volume control | Move the turntable and that equipment apart, or change their positions | Factory, [XA owner's manual, p. 10](transcripts/xa-owners-manual.md); [XB1 manual, p. 9](transcripts/xb1-owners-manual.md) |
| 2 | A ground connection is broken or was never made | The hum is extremely loud | Find and remake the ground. On the XA, the braided ground strap of the audio cable goes to the turntable suspension | Factory, XA owner's manual, p. 10; [XA service manual, p. 2](originals/xa-service-manual.pdf), "Audio Output Cable" |
| 3 | The motor | Turn the motor off with its switch while the hum is present. No change means the motor is not the cause | If the hum stops with the motor, check the motor and its wiring: [XA service](../models/xa/service.md) | Factory, XA owner's manual, p. 10 |
| 4 | An unshielded cartridge, such as a Grado wood body | Hum appears only with that cartridge | Galo needed hum shielding to use an unshielded Grado Signature 10MR on his AR-based table | Owner report, [Galo](archive/audioxpress/galo-belt-drive-turntable-upgrade.pdf) |

The XA manual's own view: the turntable itself is a mechanical device and hardly ever the source of hum, because the cartridge signal goes straight to the amplifier whether the motor is on or off (Factory, XA owner's manual, p. 10).

## Slow start or wrong speed

Check speed with a strobe disc. AR's limit is no more than plus or minus 21 dots per minute on the strobe card (Factory, [XA service manual, p. 2](originals/xa-service-manual.pdf)); on the XB, ±7 dots in 20 seconds or ±21 dots per minute at 1.5 g stylus force (Factory, [XB drawing 119](drawings/xb-drawing-119.png), performance test A). See the [strobe disc](../parts/strobe-disc.md).

| Order | Likely cause | How to check | Fix | Source |
| --- | --- | --- | --- | --- |
| 1 | Oil or dirt on the belt, pulley or inner platter rim | The belt looks shiny or feels greasy; start-up chatters | Clean the belt with tissue soaked in methyl alcohol (wood alcohol), never rubbing alcohol. Wipe the pulley and the inner platter rim the same way. Dust the belt with talcum powder: without it the table will not start properly. Clean and powder once a year | Factory, XA owner's manual, p. 10; XB1 manual, p. 12 |
| 2 | Worn or stretched belt | Slow start, a chattering sound at start-up, or speed that drifts low | Replace the belt and clean the pulley. A new belt also cures speed error from slippage | Factory, XA service manual, p. 2 |
| 3 | A new replacement belt not yet run in | Speed slightly off in the first days with a new belt | Vinyl Nirvana says its belt takes about a week to stretch slightly and wear in | Maker claim, [belt listing](archive/vinyl-nirvana/products/replacement-ar-turntable-belt.md) |
| 4 | Belt on the wrong pulley step | 45 rpm when you want 33⅓, or the reverse | The upper, smaller step is 33⅓ rpm; the larger step is 45 rpm. Lift the outer platter and mat to move it | Factory, XA owner's manual, pp. 4, 11 |
| 5 | Wrong pulley for the mains frequency | The table runs steadily but at the wrong speed on every record. A 60 Hz table runs slow on 50 Hz | Fit the pulley for your mains. The 50 cycle pulley is visibly larger in diameter than the 60 cycle one | Factory, XA service manual, p. 1 |
| 6 | Wrong pulley for the motor | The pulley is loose on the shaft, or will not go on | Haydon and Philips pulleys are not interchangeable: Haydon shaft ⅛ in (3.2 mm), Philips ¹⁄₁₆ in (1.6 mm). Tell them apart by the bore. If a pulley is loose, crimp the bottom of its mounting bracket gently | Factory, XA service manual, pp. 1, 2. See [motor and pulley](../parts/motor-and-pulley.md) |
| 7 | Speed a little fast or slow with a good belt and the right pulley | Strobe outside ±21 dots per minute | A shim under the end of the motor nearest the rear of the table raises the speed; a shim near the screw nearest the platter lowers it | Factory, XA service manual, p. 2 |
| 8 | The motor | Slow start and chatter persist after a new belt and a clean pulley | The motor may be defective. Replace it and test it for speed and running noise | Factory, XA service manual, p. 2 |
| 9 | A seized or dry platter bearing | With the belt off, the inner platter does not spin freely by hand | Clean and oil the bearing: [platter bearing](../models/xa/mods/platter-bearing.md). Early XA bearings were cast Delrin that closed in and seized the spindle; later ones had steel-jacketed Babbitt inserts | Owner report, [Allison](archive/vinyl-nirvana/ar-turntable-history/acoustic-research-inc-the-golden-years-by-roy-allison.md); Specialist, [Vinyl Nirvana photo comparison](archive/vinyl-nirvana/ar-turntable-history/a-photo-comparison-of-a-new-and-old-ar-xa.md) |

Do not start the table without the outer platter in place, or the belt is likely to come off (Factory, XA owner's manual, p. 11).

## Motor starts backwards

| Order | Likely cause | How to check | Fix | Source |
| --- | --- | --- | --- | --- |
| 1 | Two-motor XA, up to serial XA66866: the starter motor is not doing its job | Lift the outer platter. Two motors show under it. The drive motor is a permanent-magnet synchronous motor that runs either way, depending on which way it is first pushed. The second, smaller motor is there to start it in the right direction | The original two-motor parts have not been available for years. AR's fix was a Haydon conversion kit to a single motor | Factory, [Villchur 1962, Part 2, p. 36](originals/villchur-1962-part-2.pdf); [XA service manual, p. 1](originals/xa-service-manual.pdf) |
| 2 | A single-motor table | No held source gives a cause. Record the serial, the motor label, the capacitor markings and the wiring, and compare them with the [XA wiring diagrams](originals/xa-service-manual.pdf), p. 3 | Unconfirmed, [EL10](../TO-CONFIRM.md#motor-electrical-and-overall-size) | None |

A drive motor "that often ran backward" is named among the early faults of the original table that were "soon corrected" (Period, [*Audio*, July 1984](archive/gamma-electronics/audio-1984-07-ar-turntable.md)).

## Arm skips or sticks

The XA service manual ranks the first cause: a defective damping mechanism is "the most common cause" of complaints about skating distortion (Factory, [XA service manual, p. 1](originals/xa-service-manual.pdf)). The rest of the order is our assessment.

| Order | Likely cause | How to check | Fix | Source |
| --- | --- | --- | --- | --- |
| 1 | XA only: defective arm damping, so pivot friction makes the tracking force fluctuate | The arm drags as it moves; the gauge acts as if it sticks | AR recommends disabling the damping on every XA: [XA service](../models/xa/service.md). It was omitted from serial XA236534 | Factory, XA service manual, pp. 1, 2 |
| 2 | Pivot set screws too tight, or their tips deformed | The arm is sluggish over its small vertical free play. On the XA, the pin in the slot on the platter side of the pivot housing does not move up and down | Loosen or replace the screws. They are sealed with Loc-Tite; MEK (methyl ethyl ketone) may be needed to break them loose. On the XA, adjust only the outside screw, until the pin visibly moves in its slot | Factory, XA service manual, p. 1; XA owner's manual, p. 12; XB1 manual, p. 11 |
| 3 | The small ball bearing under the arm spindle is missing | Lift the arm assembly off; look in the spindle well | Fit the ball, with the small disc in the well first. Without the ball, sideways pivot friction rises and the stylus skips or sticks in one groove | Factory, XA service manual, p. 1 |
| 4 | The arm cable at the back of the arm is not dressed as in the manual | Tap the shell very lightly from each side: it should move equally freely both ways | Re-form the wire as in the manual photographs. A misplaced cable can push the arm sideways by several tenths of a gram | Factory, XA owner's manual, pp. 2, 4; XA service manual, p. 1 |
| 5 | The two pivot set screws tightened very unevenly into the coupler block | Compare how far each screw goes in | Even them up. A gross difference causes the same sideways force as a misplaced cable | Factory, XA service manual, p. 1 |
| 6 | Stylus force too low for the cartridge | Weigh it with the gauge, damping released | Set the force from the cartridge table. AR's correction for skating is at most ¼ g more force. No cartridge works satisfactorily below 1 g | Factory, XA owner's manual, pp. 5, 6; XA service manual, p. 1; [sheet L-1591](transcripts/ar-cartridge-mount-l-1591.md) |
| 7 | Floor or shelf movement | Skips when someone walks past; the base rocks | Put the table on a flat, sturdy surface so the base does not rock. On a creaky floor, a wall-mounted shelf usually cures it | Factory, XA owner's manual, p. 10 |

## Arm will not lower

| Order | Likely cause | How to check | Fix | Source |
| --- | --- | --- | --- | --- |
| 1 | XA: damping set too stiff | Lift the arm about 3 in (76 mm) above the record and let go: it should take two or three seconds to come down | Unscrew the arm spindle a little at a time until it does. Do not unscrew further, or the damping release is degraded | Factory, [XA owner's manual, p. 7](transcripts/xa-owners-manual.md) |
| 2 | XA: damping mechanism binding | The arm hangs even with the spindle adjusted | Disable the damping: tighten the spindle into the pivot and pull out the small steel damping pin in the side of the brass bearing. Steps: [XA service](../models/xa/service.md) | Factory, XA service manual, p. 2 |
| 3 | XB, XB1 and AR77XB: cueing descent too slow | Lower the cue lever: from full height the arm should reach the record in 1 to 3 seconds | Turn the cue cylinder cap under the pivot assembly no more than ½ turn at a time: clockwise for a faster descent, counterclockwise for slower. The damping medium inside the cylinder is Unconfirmed ([CU3](../TO-CONFIRM.md#cueing-lift-and-arm-damping)) | Factory, [XB1 manual, p. 11](transcripts/xb1-owners-manual.md); [XB drawing 119](drawings/xb-drawing-119.png), note 8. AR77XB: the XB value, for comparison only |
| 4 | XB pattern: cue height set too high | With the lever down, the stylus should be free to drop at least ¼ in (6.4 mm) below the record surface | Turn the knurled cap on top of the cue plunger about ⅛ turn at a time: clockwise lowers it, counterclockwise raises it | Factory, XB1 manual, p. 11; XB drawing 119, note 7 |
| 5 | Pivot set screws too tight | See "Arm skips or sticks", row 2 | Same fix | Factory, XA owner's manual, p. 12 |

## Rumble

Compare a rumble reading only with one taken the same way: weighting, reference level and test record change the number (see [design notes](design-notes.md)). The period figures were about −38 dB unweighted for the XA (Period, [evidence](evidence/period-tests.md)). The order below is our assessment.

| Order | Likely cause | How to check | Fix | Source |
| --- | --- | --- | --- | --- |
| 1 | Dry or dirty platter bearing | Lift the inner platter straight up about 2 in (51 mm) and look at the spindle | A few drops of #10 machine oil without additives, such as Golden Shell 10W, once a year. On the XB, 3 drops after cleaning | Factory, XA owner's manual, p. 11; XB drawing 119, note 11 |
| 2 | Motor running noise | Listen with the platter off; compare after a motor change | AR tests a replacement motor for speed and running noise | Factory, XA service manual, p. 2, "Drive Motor", step 7 |
| 3 | Arm resonance with your cartridge | A low-frequency peak that moves when you change cartridge | USTC found a 17 cps arm resonance on its test table and took it for the main rumble component. Villchur gives the 10 cps region with typical cartridges of 1962. It depends on the cartridge: change the cartridge, not the table | Period, [*High Fidelity*, March 1963](originals/high-fidelity-1963-03-ar-report-pp59-60.pdf); Factory, [Villchur 1962, Part 1, p. 22](originals/villchur-1962-part-1.pdf) |
| 4 | Something touching the subchassis: a stiff signal cable, the transit bolt, the base | Press the platter down gently: it should bob freely and evenly | Free it. Galo found a heavy tonearm cable hard to dress without interfering with the suspension and moved it to RCA jacks on the base: [RCA jacks mod](../models/xa/mods/rca-jacks.md) | Owner report, Galo; Factory, XB1 manual, p. 3 |

## Platter rubs the top plate

| Order | Likely cause | How to check | Fix | Source |
| --- | --- | --- | --- | --- |
| 1 | Suspension set too low, or unevenly | With a heavy record on, measure the gap between the bottom of the outer platter and the top plate at several points | Tighten the three suspension nuts until the gap is right at all points. XA: ⅛ in (3.2 mm). XB: ⅜ in ± ¹⁄₃₂ (9.5 ± 0.8 mm) | Factory, XA service manual, p. 2; XB drawing 119, note 13. See the [platter height gauge](../parts/platter-height-gauge.md) |
| 2 | Belt too tight | The subchassis sits pulled toward the motor | Fit a belt of the right size. Vinyl Nirvana says an overly tight belt most often pulls the whole suspension toward the motor | Maker claim, [belt listing](archive/vinyl-nirvana/products/replacement-ar-turntable-belt.md) |
| 3 | A stiff signal cable pulling the subchassis | Unplug the cable at the amplifier: the platter recentres | Dress the cable so it does not pull, or move to jacks on the base | Owner report, Galo |
| 4 | Spring washers flattened | Under each spring the foam has taken the shape of the coil | Replace the foam washers or fit a [suspension kit](../models/xa/mods/suspension-kit.md) | Owner report, [John's Weather 2012](archive/johns-weather/xa-restoration-2012.md) |
| 5 | XB pattern: arm spindle or cue cylinder touching the edge of its hole in the top plate | Look around both through the top plate | Recentre the subchassis. The factory minimum clearance is 0.050 in (1.3 mm) | Factory, XB drawing 119, note 13 |

## One channel dead

| Order | Likely cause | How to check | Fix | Source |
| --- | --- | --- | --- | --- |
| 1 | Shell clips off the cartridge pins, or on the wrong pins | Look under the shell | Left: white, with green as its ground. Right: red, with black as its ground. On a mono cartridge use white and green | Factory, [XA owner's manual, p. 3](transcripts/xa-owners-manual.md). The modern colour code differs: [RW1](../TO-CONFIRM.md#xa-mods) |
| 2 | Plugs in the wrong amplifier sockets, or one plug loose | Swap the plugs at the amplifier: the dead side moves if the fault is after the table | The red-banded plug goes to the right channel | Factory, XA owner's manual, p. 9 |
| 3 | Broken or frayed wire inside the arm | Ohmmeter from each shell contact to its terminal post | Rewire the arm: [tonearm rewire](../models/xa/mods/tonearm-rewire.md). Frayed or broken arm wire is a common problem on aging XA tables; one restorer found a short and only one working channel | Owner report, [Hamrick on Vinyl Nirvana](archive/vinyl-nirvana/ar-diy-do-it-yourself/rewiring-an-ar-xa-tonearm.md); [John's Weather 2009](archive/johns-weather/xa-restoration-2009.md) |
| 4 | Faulty audio output cable | Ohmmeter along each lead, plug to terminal strip | Replace it, connecting the braided ground strap to the suspension | Factory, XA service manual, p. 2 |
| 5 | The cartridge | Try a known good cartridge in the same shell | Replace the stylus or cartridge | Our assessment |

## Suspension tilts

| Order | Likely cause | How to check | Fix | Source |
| --- | --- | --- | --- | --- |
| 1 | The three nuts set unevenly | Measure the platter-to-top-plate gap all round | Adjust the nuts until the gap is equal all round, at the factory height for your model (see "Platter rubs the top plate"). One restorer then locked the nuts with nail polish | Factory, XA service manual, p. 2; Owner report, John's Weather 2012 |
| 2 | XB pattern: the transit bolt is still fitted | Look for a wing-nut bolt, perhaps with a red CAUTION tag, holding the suspension to the top plate | Unscrew it completely and keep it for shipping | Factory, [XB1 manual, pp. 2–3](transcripts/xb1-owners-manual.md) |
| 3 | Belt too tight | The tilt is toward the motor | See "Platter rubs the top plate", row 2 | Maker claim, belt listing |
| 4 | Stiff signal cable | The tilt is toward the cable exit | See "Platter rubs the top plate", row 3 | Owner report, Galo |
| 5 | A tired spring or a flattened foam washer | One corner sits low however the nut is set | Replace springs and washers as a set: [suspension kit](../models/xa/mods/suspension-kit.md) | Owner report, John's Weather 2012 |
| 6 | The surface under the table | The base rocks | Place it on a flat, sturdy surface | Factory, XA owner's manual, p. 10 |

## Sources

Each link opens the copy kept in this repository.

- [XA owner's manual, written out](transcripts/xa-owners-manual.md), from the Vinyl Nirvana scans. Factory.
- [XB1 manual, written out](transcripts/xb1-owners-manual.md), and the [scan](originals/xb1-owners.pdf). Factory.
- [XA service manual](originals/xa-service-manual.pdf). Factory.
- [XB drawing 119](drawings/xb-drawing-119.png), revision T. Factory.
- [Villchur 1962, Part 1](originals/villchur-1962-part-1.pdf) and [Part 2](originals/villchur-1962-part-2.pdf). Factory.
- [*High Fidelity*, March 1963](originals/high-fidelity-1963-03-ar-report-pp59-60.pdf). Period.
- [*Audio*, July 1984, Peter W. Mitchell](archive/gamma-electronics/audio-1984-07-ar-turntable.md). Period.
- [Roy Allison, The Golden Years](archive/vinyl-nirvana/ar-turntable-history/acoustic-research-inc-the-golden-years-by-roy-allison.md). Owner report.
- [Gary Galo, A Belt-Drive Turntable Upgrade](archive/audioxpress/galo-belt-drive-turntable-upgrade.pdf). Owner report.
- [John's Weather, XA restoration 2009](archive/johns-weather/xa-restoration-2009.md) and [2012](archive/johns-weather/xa-restoration-2012.md). Owner report.
- [Scott Hamrick, rewiring an XA tonearm](archive/vinyl-nirvana/ar-diy-do-it-yourself/rewiring-an-ar-xa-tonearm.md). Owner report.
- [Vinyl Nirvana belt listing](archive/vinyl-nirvana/products/replacement-ar-turntable-belt.md). Maker claim.
- [Vinyl Nirvana photo comparison of an old and new XA](archive/vinyl-nirvana/ar-turntable-history/a-photo-comparison-of-a-new-and-old-ar-xa.md). Specialist.
