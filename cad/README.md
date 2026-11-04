# CAD models and drawings

[Home](../README.md) · [Part index](../parts/reproduction.md) · [Things to confirm](../TO-CONFIRM.md)

One OpenSCAD file per part, with a drawing and machine-ready exports built from it. Only parts with some documented dimensions are here. **None has been made or fit-tested.** Not sure what a part is for? See [What it is and where it goes](../docs/what-goes-where.md).

| Part | Status | Drawing | CNC file | Other files |
| --- | --- | --- | --- | --- |
| Standoff bushing, #1–#3 | Geometry complete | [#1](exports/headshell-standoff-bushing/headshell-standoff-bushing-1.pdf) · [#2](exports/headshell-standoff-bushing/headshell-standoff-bushing-2.pdf) · [#3](exports/headshell-standoff-bushing/headshell-standoff-bushing-3.pdf) | [Folder](exports/headshell-standoff-bushing/) | [Source](parts/headshell-standoff-bushing.scad) |
| Shim block, #1–#3 | Geometry complete | [#1](exports/headshell-shim-block/headshell-shim-block-1.pdf) · [#2](exports/headshell-shim-block/headshell-shim-block-2.pdf) · [#3](exports/headshell-shim-block/headshell-shim-block-3.pdf) | [Folder](exports/headshell-shim-block/), with 1:1 cutting DXF | [Source](parts/headshell-shim-block.scad) |
| Cartridge screw, #3-48, #1–#4 | Reference; buy it | [#1](exports/cartridge-screw-3-48/cartridge-screw-3-48-1.pdf) · [#2](exports/cartridge-screw-3-48/cartridge-screw-3-48-2.pdf) · [#3](exports/cartridge-screw-3-48/cartridge-screw-3-48-3.pdf) · [#4](exports/cartridge-screw-3-48/cartridge-screw-3-48-4.pdf) | Not for machining | [Source](parts/cartridge-screw-3-48.scad) |
| Set screw, #4-40 | Reference; buy it | [PDF](exports/set-screw-4-40/set-screw-4-40.pdf) | Not for machining | [Source](parts/set-screw-4-40.scad) |
| XA counterweight | Preliminary: 3 placeholders | [PDF](exports/xa-counterweight/PRELIMINARY-xa-counterweight.pdf) | [STEP](exports/xa-counterweight/PRELIMINARY-xa-counterweight.step) | [Source](parts/xa-counterweight.scad) |
| Overhang gauge | Preliminary: 5 placeholders; new design | [PDF](exports/overhang-gauge/PRELIMINARY-overhang-gauge.pdf) | [STEP](exports/overhang-gauge/PRELIMINARY-overhang-gauge.step), with 1:1 cutting DXF | [Source](parts/overhang-gauge.scad) |
| PMMA headshell, top-mount Grado Master4 | Concept: 21 placeholders; new design | [PDF](exports/headshell-pmma-top-mount/PRELIMINARY-headshell-pmma-top-mount.pdf) | [STEP](exports/headshell-pmma-top-mount/PRELIMINARY-headshell-pmma-top-mount.step) | [Source](parts/headshell-pmma-top-mount.scad) |

Files for a part with placeholders start with `PRELIMINARY-` so they are not uploaded by accident. Every value that is still a placeholder is logged in [TO-CONFIRM.md](../TO-CONFIRM.md#cad-dimensions-needed).

## Reading a drawing

Page 1 is the drawing, in **third-angle projection**: top above front, right to the right, left to the left. Sections and an isometric view sit in the right-hand column. Page 2 is the dimension register, which lists every value with its evidence and how to check it.

- **Black** dimensions come from a cited source.
- **Red** dimensions tagged **PH** are placeholders, chosen only so the model has a shape. They are not measurements.
- The ID after each dimension (`CW3`, `HD10`) matches the register and TO-CONFIRM.md.

No source gives tolerances for any of these parts, so the drawings state none. Agree them with the maker, and keep a measurement of a worn part separate from an original tolerance.

## Ordering a part

Check that the drawing has no red dimensions first. Then:

1. Upload the **STEP** file. It has true cylinders and planes. [JLCCNC's guide](https://jlccnc.com/blog/how-to-prepare-cad-files-for-cnc-machining) says its portal takes STEP, IGES, Parasolid, or native CAD files, and advises against mesh formats like STL for machining. Keep the STL for 3D printing.
2. Attach the **PDF** so tolerances and notes go with the order. Threads are shown plain, at major diameter or as a tap drill, so call each one out as well; the same guide lists undefined thread specs as a common mistake.
3. For a flat part, include the 1:1 DXF, which that guide suggests for profiles.
4. State the material and quantity, and check the current order page, since these requirements can change.

`-drawing.dxf` is the drawing sheet at drawing scale. `-flat-1to1.dxf` is a true-size cutting outline.

## The PMMA headshell

It is meant for a [Grado Master4](https://gradolabs.com/products/master4), fixed by screws from the top. The slots are recessed for the screw heads, and the pocket underneath takes the cartridge. **It cannot be ordered yet**, because no drawing of the AR shell has been found. Its layout follows the exploded view on [p. 4 of the XA service manual](../docs/originals/xa-service-manual.pdf), but the neck, thread, pins, and body size are all placeholders.

Grado lists the Master4 at 9.6 g, with a 1.6–1.9 g tracking force and 20 µm/mN compliance. It publishes no body dimensions or screw details, and says the housing was reshaped for this generation. Until a Master4 is measured, the pocket is sized from a [review of the older Opus3](https://addictedtoaudio.co.nz/blogs/reviews/grado-timbre-series-opus3-cartridge): 20.1 mm wide, 16.3 mm tall, 25.3 mm deep, 29.6 mm with pins, and 18.3 mm from top to stylus tip. That review says the bolts "screw in from the top", and that the body is wider than the headshell it was fitted to.

Suggested order of work:

1. Measure an original shell, its retaining nut, and the Master4: rows GR and HD in [TO-CONFIRM.md](../TO-CONFIRM.md#cad-dimensions-needed).
2. Enter the values in the source file and rebuild.
3. **Print the STL in cheap plastic** and test the neck, pins, and screw length on the arm.
4. Only then order it in PMMA.

Known risks, **our assessment**:

- **Neck strength.** Pat's Audio advertises a reinforced neck with threads "that won't crack off", which suggests this is the weak point. PMMA is brittle, so a metal neck insert may be needed.
- **Chemical attack.** Threadlocker and solvents can craze PMMA. AR's factory notes call for Loctite on some screws, so do not carry that over.
- **Balance.** The model estimates about 10 g for the body, without pins or wires, and the Master4 adds 9.6 g. Check that the counterweight still balances. AR's mounting sheet already calls for extra counterweight with some cartridges.
- **Arm resonance.** Every extra gram of shell lowers it. With 20 µm/mN compliance, the usual estimate of 159 / √(mass × compliance) gives about 8 Hz at 20 g of total moving mass. The arm's own effective mass is not established here, so measure the finished shell, and keep it light.
- **Record clearance.** With a shallow pocket the stylus sits only a few millimeters below the shell's underside: 5.8 mm using the Opus3 figure. Check the shell clears the record at the arm's working angle.
- **Machining setups.** It needs work from the top, the bottom, and the neck end. Thin PMMA walls are also a concern: published minimums range from 0.5 to 1.0 mm, so 1.0 mm is the safer plan.

## Not modeled, and why

| Part | What exists | What is missing |
| --- | --- | --- |
| Tonearm rest | One installed height: 39 mm | Yoke shape, stem, thread, material |
| XB hinge and bracket | Hole pattern on [drawing 114](../models/xb/README.md#cover-dimensions-and-clearance) | The hinge itself. The pattern is tabulated on the XB page |
| Plinth, dust cover, top plate | XA overall envelope only | Walls, hole patterns, thickness |
| Arm tube, pivot block, spindle, bearings | Assembly views and part numbers | All part dimensions |
| Platter, T-bar, pulley, motor brackets | Assembly views and part numbers | All part dimensions |
| Springs, grommets, belts | Part numbers and suppliers | Dimensions and material specifications |

Each of these stays on the [part index](../parts/reproduction.md) until there are dimensions to model.

## Changing a value

Edit the row in the table `P` at the top of the part file. Change its value and its evidence code, for example from `PH` to `M` when measured, and record the result in TO-CONFIRM.md. The drawing turns that dimension black on the next build.

Codes: `F` factory, `O` owner report, `C` community drawing, `S` industry standard, `D` design choice, `M` measured, `PH` placeholder.

## Rebuilding

The exports are committed, so nobody needs these tools just to use a drawing. To rebuild, you need OpenSCAD 2021.01 and Python:

```text
python3 -m venv venv
venv/bin/pip install -r cad/tools/requirements.txt
venv/bin/python cad/tools/build.py              # all parts
venv/bin/python cad/tools/build.py xa-counterweight
venv/bin/python cad/tools/build.py --check      # every placeholder is logged
```

The script is under the [MIT License](tools/LICENSE). It rebuilds OpenSCAD's CSG tree as an OpenCASCADE solid, because OpenSCAD cannot export STEP itself. Each build stops if the solid is invalid, or if its volume disagrees with OpenSCAD's mesh by more than 1%. Part files must use cubes, cylinders, cones, and boolean operations; the script rejects anything it cannot convert.

## Record for each model

Creator: AR turntable restoration reference contributors. Version: revision A, 2026-11-04. License: [CC BY-SA 4.0](../LICENSE). Fit test: none. The intended model and material are in each drawing's title block.
