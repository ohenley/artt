# What it is and where it goes

[Home](../README.md) · [Document index](README.md) · [CAD drawings](../cad/README.md)

Plain answers about the small parts, for anyone with a table open on the bench.

## Why are there so many cartridge screws?

**You only fit two.** The other six stay in the bag.

AR sold the turntable without a cartridge, and cartridges came in different heights. So AR packed a hardware bag that could fit nearly any of them: screws in four lengths, plus spacers. A printed table, [AR sheet L-1591](originals/ar-cartridge-mount.jpg), told owners which pieces to use for their cartridge. The sheet says its combinations "must be used to obtain proper alignment of the cartridge in the shell."

![The AR hardware bag: four screw lengths, three bushings, three shim blocks, one set screw](images/hardware-set.png)

| In the bag | How many | What it does |
| --- | --- | --- |
| #3-48 aluminum screw, 4 lengths | 2 of each | Holds the cartridge to the shell. Pick **one length** and use 2 screws. |
| Standoff bushing, 3 heights | 2 of each | A spacer between the shell's stud and the cartridge. Many cartridges use none. |
| Shim block, 3 thicknesses | 1 of each | Goes under the front of the cartridge to tilt it, where the sheet calls for one. |
| #4-40 brass set screw | 1 | **Unconfirmed.** The sheet does not mention it, and neither source says where it goes. |

Counts come from the [community drawing](originals/ar-headshell-hardware-rev-1.pdf), which covers the XA and XB. AR's sheet confirms four screw sizes and three bushing sizes.

## Where do they go?

![Side views: the original AR mounting with screws from below, and the Grado Master4 plan with screws from the top](images/cartridge-mounting.png)

**The original way, on the left.** The shell has two threaded studs inside. Each screw passes through the cartridge's mounting ear, then through a bushing if one is needed, and into a stud.

1. Find your cartridge on [sheet L-1591](originals/ar-cartridge-mount.jpg). For example, the Shure M91 takes No. 1 standoffs and No. 1 screws. The Shure V15 Type II takes no standoffs and No. 3 screws.
2. Clip the shell's wires onto the cartridge pins first. The sheet gives the colors: red for right hot, black for right ground, white for left hot, green for left ground.
3. Fit the cartridge, turning any bushings onto the screws to hold them in place.
4. Tighten reasonably, but do not overtighten. The sheet warns that the studs can be stripped or broken off.

Some footnotes on the sheet are surprising. For certain cartridges, AR tells owners to **glue a U.S. penny inside the shell** to get the right needle force. Others need an extra counterweight section. Mass at the end of the arm has always mattered.

If your cartridge is not on the sheet, **our advice** is to use the shortest screw that fully engages the stud without bottoming out.

**A Grado Master4, on the right, uses none of this.** Its screws come from the top, through the shell, into the cartridge's own threaded body. It takes no AR screws, studs, or bushings, which is why the [PMMA shell concept](../cad/README.md#the-pmma-headshell) has slots instead of studs. The right-hand panel is a concept that has not been tested.

## What is an overhang gauge?

A small template that checks one distance: **how far the needle reaches past the record's center**. That distance is called overhang.

![Overhang is the distance by which the needle passes the spindle; the gauge has a big hole for the spindle and a small hole for the needle](images/overhang.png)

**Why it matters.** An arm swings in an arc, so the needle cannot stay perfectly in line with the groove. Getting this distance right keeps that error low across the record. For the AR arm, the [1962 design paper, p. 69](originals/villchur-1962-part-1.pdf) gives **0.688 in (17.48 mm)**. [XB drawing 119](originals/xb-drawing-119.tif), note 10, gives the same figure, ± 0.030 in.

**When you need it.** After fitting a new cartridge or shell. Each cartridge puts its needle in a slightly different place.

**How to use it.**

1. Drop the big hole over the spindle, and swing the gauge so the small hole lies on the line toward the arm's pivot.
2. Lower the needle gently. If it lands in the small hole, you are done.
3. If not, adjust and try again. AR's paper says "the effective arm length is adjusted". The XA parts list has an "overhang set screw", item 21J, on the arm's center block, so **our reading** is: loosen it, slide the arm tube, and retighten. Confirm this on your own arm first.

**Do you need to make one?** Not if you have yours. AR supplied one with the table: "Overhang Template", part 914, on the XA, and P/N 402001 on the XB. The [model in this repository](../cad/exports/overhang-gauge/PRELIMINARY-overhang-gauge.pdf) is only for tables that have lost it. Only the distance between the two holes matters.

## Every screw, by job

**Sources:** the XA column comes from the [XA service manual](originals/xa-service-manual.pdf). The XB column comes from [drawing 119](originals/xb-drawing-119.tif), revision T, read from its numbered callouts.

**AR77XB:** no model-specific document has been inspected, so nothing is confirmed. Use the XB column as a comparison, and check your own table.

"Not stated" means the source names the part but gives no thread or size.

| Job | XA | XB, revision T |
| --- | --- | --- |
| Cartridge to shell | #3-48, 2 of 8 in the bag | #3-48, 2 of 8 in the bag |
| Shell to arm | Knurled nut, item 21C. Not a screw. The manual warns that twisting the shell while tightening can deform the arm's socket | Knurled end shown on the arm, part of arm assembly 404014 |
| Lock the counterweight | Set screw, item 22A, part 942. Size not stated | Set screw, item 6, part 501008. Size not stated |
| Arm's up-and-down pivot | 2 pivot screws, item 21H, part 918, with Loc-Tite. Size not stated | Pivot screws in the arm assembly, with Loctite. Setting in note 9 |
| Set the overhang | Overhang set screw, item 21J, part 1123. Size not stated | Not shown on this drawing |
| Hold the motor | 2 screws. Size not stated | 2 × #4-48 × ⅛ in, item 18, part 501009 |
| Suspension height | 3 nuts, item 17, part 1095. Size not stated | 3 × #10-24 nuts, item 32, part 502006, on threaded studs, item 33 |
| Tonearm rest | Rest with its nut, item 10, part 907 | #5-40 nut, item 60, and #5 star washer, item 61 |
| Cueing lever | The XA has no cueing lever | 2 × #8-32 nuts, item 28, with lockwashers, item 58. 1 × #4-40 screw, item 62 |
| Top badge | Not stated | 2 push nuts, item 27, part 500015 |
| Audio terminal strip | Not stated | Wood screw, item 24, part 501007 |
| Brackets, clamps, and capacitor straps | Not stated | #8 × ⅜ in, item 37, part 501012; 12 in all. Pitch and head not stated |
| Bottom panel | 3 Phillips screws, or a staple | Staples, item 36 |
| Shipping bolt | Not listed | Item 8, part 501011, with nylon washer, item 7. **Remove before use**; a label says so |

Unknown sizes are logged in [TO-CONFIRM.md](../TO-CONFIRM.md). Do not take a thread from one row and assume it for another.

## Words used in this repository

| Word | Meaning |
| --- | --- |
| Cartridge | The part that holds the needle and makes the signal |
| Stylus, needle | The diamond tip in the groove |
| Shell, headshell | The holder at the end of the arm that the cartridge bolts to |
| Counterweight | The weight at the back of the arm that balances it |
| Tracking force, needle force | How hard the needle presses on the record, in grams |
| Spindle | The pin at the center of the platter |
| Pivot | The point the arm swings on |
| T-bar, tee bar | The sprung metal frame that carries both the platter and the arm |
| Top plate | The metal panel you see on top of the wooden base |
| Standoff bushing | A small tube used as a spacer |
| Shim block | A thin block used to raise or tilt something |
| Set screw | A small screw with no head, tightened into a part to lock it |
| ECO | Engineering change order: a factory record of a design change |
