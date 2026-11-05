# CAD models and drawings

[Home](../README.md) · [Part index](../parts/reproduction.md) · [Things to confirm](../TO-CONFIRM.md#cad-dimensions-needed)

| Part | Status | Drawing | Files |
| --- | --- | --- | --- |
| Standoff bushing, #1–#3 | Complete | [Folder](exports/headshell-standoff-bushing/) | [scad](parts/headshell-standoff-bushing.scad) |
| Shim block, #1–#3 | Complete | [Folder](exports/headshell-shim-block/) | [scad](parts/headshell-shim-block.scad) |
| Cartridge screw, #3-48, #1–#4 | Reference; buy it | [Folder](exports/cartridge-screw-3-48/) | [scad](parts/cartridge-screw-3-48.scad) |
| Set screw, #4-40 | Reference; buy it | [PDF](exports/set-screw-4-40/set-screw-4-40.pdf) | [scad](parts/set-screw-4-40.scad) |
| XA counterweight | 3 placeholders | [PDF](exports/xa-counterweight/PRELIMINARY-xa-counterweight.pdf) | [STEP](exports/xa-counterweight/PRELIMINARY-xa-counterweight.step) · [scad](parts/xa-counterweight.scad) |
| Overhang gauge | 5 placeholders | [PDF](exports/overhang-gauge/PRELIMINARY-overhang-gauge.pdf) | [STEP](exports/overhang-gauge/PRELIMINARY-overhang-gauge.step) · [scad](parts/overhang-gauge.scad) |
| [XA plinth](../models/xa/mods/plinth-rebuild.md) | Concept: all placeholders | [Base](exports/xa-plinth/PRELIMINARY-xa-plinth-1.pdf) · [Panel](exports/xa-plinth/PRELIMINARY-xa-plinth-2.pdf) | [Folder](exports/xa-plinth/) · [scad](parts/xa-plinth.scad) |
| [PMMA headshell](../models/xa/mods/headshell-top-mount.md) | Concept: 23 placeholders | [PDF](exports/headshell-pmma-top-mount/PRELIMINARY-headshell-pmma-top-mount.pdf) | [STEP](exports/headshell-pmma-top-mount/PRELIMINARY-headshell-pmma-top-mount.step) · [scad](parts/headshell-pmma-top-mount.scad) |

Each folder holds the PDF drawing, STEP for machining, STL for printing, and DXF. A `PRELIMINARY-` file still has placeholders: do not order from it.

## Reading a drawing

- **Black** dimensions come from a cited source.
- **Red** dimensions tagged **PH** are placeholders, not measurements.
- The ID after each dimension (`CW3`, `HD10`) matches page 2 of the PDF and [TO-CONFIRM.md](../TO-CONFIRM.md#cad-dimensions-needed).
- No tolerances are given. Agree them with the maker.

## Changing a value

Edit the row in table `P` at the top of the part file: set the value, and change its code from `PH` to `M` once measured. Then rebuild.

## Rebuilding

Needs OpenSCAD 2021.01 and Python.

```text
python3 -m venv venv
venv/bin/pip install -r cad/tools/requirements.txt
venv/bin/python cad/tools/build.py              # all parts
venv/bin/python cad/tools/build.py xa-plinth    # one part
venv/bin/python cad/tools/build.py --check      # every placeholder is logged
```
