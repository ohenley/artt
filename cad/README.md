# CAD models and drawings

[Home](../README.md) · [Part index](../parts/reproduction.md) · [Things to confirm](../TO-CONFIRM.md#cad-dimensions-needed)

One OpenSCAD file per part, with a drawing and exports built from it. For what each part does, see [What it is and where it goes](../docs/what-goes-where.md).

| Part | Status | Drawing | CNC file | Source |
| --- | --- | --- | --- | --- |
| Standoff bushing, #1–#3 | Geometry complete | [Folder](exports/headshell-standoff-bushing/) | STEP in folder | [scad](parts/headshell-standoff-bushing.scad) |
| Shim block, #1–#3 | Geometry complete | [Folder](exports/headshell-shim-block/) | STEP and 1:1 cutting DXF in folder | [scad](parts/headshell-shim-block.scad) |
| Cartridge screw, #3-48, #1–#4 | Reference; buy it | [Folder](exports/cartridge-screw-3-48/) | Not for machining | [scad](parts/cartridge-screw-3-48.scad) |
| Set screw, #4-40 | Reference; buy it | [PDF](exports/set-screw-4-40/set-screw-4-40.pdf) | Not for machining | [scad](parts/set-screw-4-40.scad) |
| XA counterweight | Preliminary: 3 placeholders | [PDF](exports/xa-counterweight/PRELIMINARY-xa-counterweight.pdf) | [STEP](exports/xa-counterweight/PRELIMINARY-xa-counterweight.step) | [scad](parts/xa-counterweight.scad) |
| Overhang gauge | Preliminary: 5 placeholders; new design | [PDF](exports/overhang-gauge/PRELIMINARY-overhang-gauge.pdf) | [STEP](exports/overhang-gauge/PRELIMINARY-overhang-gauge.step), with 1:1 cutting DXF | [scad](parts/overhang-gauge.scad) |
| [PMMA headshell](../models/xa/mods/headshell-top-mount.md), top-mount Grado Master4 | Concept: 21 placeholders; new design | [PDF](exports/headshell-pmma-top-mount/PRELIMINARY-headshell-pmma-top-mount.pdf) | [STEP](exports/headshell-pmma-top-mount/PRELIMINARY-headshell-pmma-top-mount.step) | [scad](parts/headshell-pmma-top-mount.scad) |

Files for a part with placeholders start with `PRELIMINARY-`. Every placeholder is a row in [TO-CONFIRM.md](../TO-CONFIRM.md#cad-dimensions-needed).

## Reading a drawing

Page 1 is the drawing, in **third-angle projection**: top above front, right to the right, left to the left. Sections and an isometric view sit in the right-hand column. Page 2 is the dimension register, with the evidence for each value and how to check it.

- **Black** dimensions come from a cited source.
- **Red** dimensions tagged **PH** are placeholders, chosen only so the model has a shape.
- The ID after each dimension (`CW3`, `HD10`) matches the register and TO-CONFIRM.md.

No source gives tolerances, so the drawings state none. Agree them with the maker.

## Ordering a part

Order only when the drawing has no red dimensions.

1. Upload the **STEP** file. [JLCCNC's guide](https://jlccnc.com/blog/how-to-prepare-cad-files-for-cnc-machining) takes STEP, IGES, Parasolid, or native CAD, and advises against STL for machining. Keep the STL for 3D printing.
2. Attach the **PDF**. Threads are drawn plain, at major diameter or as a tap drill, so call each one out.
3. For a flat part, include the 1:1 DXF.
4. State the material and quantity.

`-drawing.dxf` is the drawing sheet at drawing scale. `-flat-1to1.dxf` is a true-size cutting outline.

## Not modeled

| Part | What exists | Missing |
| --- | --- | --- |
| Tonearm rest | One installed height: 39 mm | Yoke shape, stem, thread, material |
| XB hinge and bracket | Hole pattern on [drawing 114](../models/xb/README.md#cover-dimensions-and-clearance) | The hinge itself |
| Plinth, dust cover, top plate | XA overall envelope | Walls, hole patterns, thickness |
| Arm tube, pivot block, spindle, bearings | Assembly views, part numbers | All part dimensions |
| Platter, T-bar, pulley, motor brackets | Assembly views, part numbers | All part dimensions |
| Springs, grommets, belts | Part numbers, suppliers | Dimensions, material specifications |

## Changing a value

Edit the row in the table `P` at the top of the part file: change its value and its evidence code, for example from `PH` to `M`, and record the result in TO-CONFIRM.md. The dimension turns black on the next build.

Codes: `F` factory, `O` owner report, `C` community drawing, `S` industry standard, `D` design choice, `M` measured, `PH` placeholder.

## Rebuilding

The exports are committed. To rebuild, you need OpenSCAD 2021.01 and Python:

```text
python3 -m venv venv
venv/bin/pip install -r cad/tools/requirements.txt
venv/bin/python cad/tools/build.py              # all parts
venv/bin/python cad/tools/build.py xa-counterweight
venv/bin/python cad/tools/build.py --check      # every placeholder is logged
```

The script ([MIT License](tools/LICENSE)) rebuilds OpenSCAD's CSG tree as an OpenCASCADE solid, because OpenSCAD cannot export STEP. A build stops if the solid is invalid, or if its volume differs from OpenSCAD's mesh by more than 1%. Part files must use cubes, cylinders, cones, extrusions, and boolean operations.

## Record for each model

Creator: AR turntable restoration reference contributors. Version: revision A. License: [CC BY-SA 4.0](../LICENSE). Fit test: none. The intended model and material are in each drawing's title block.
