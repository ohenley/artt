# CAD models and drawings

[Home](../README.md) · [Find your part](../parts/README.md) · [Part index](../parts/reproduction.md) · [Things to confirm](../TO-CONFIRM.md#cad-dimensions-needed)

Each drawing names the part, the version, the material, and the tables it fits, in its title block. The table below is written by the build script from the same metadata, so the drawings and the part pages cannot disagree. Each export folder is named by part, version and material.

<!-- drawings table: written by cad/tools/build.py from the part files. Do not edit by hand. -->
| Part | Version | Material | Fits | Status | Drawing | Files |
| --- | --- | --- | --- | --- | --- | --- |
| [Base or plinth](../parts/plinth.md) | XA rebuild with new rear cutouts: this repository's design, not an AR part | Hardwood or plywood for the test piece | XA: unconfirmed; XB: unconfirmed; AR77XB: unconfirmed | Concept: 25 placeholders, 2 derived | [Base](exports/plinth-xa-rebuild-hardwood/PRELIMINARY-plinth-xa-rebuild-hardwood-1.pdf) · [Bottom panel](exports/plinth-xa-rebuild-hardwood/PRELIMINARY-plinth-xa-rebuild-hardwood-2.pdf) | [Folder](exports/plinth-xa-rebuild-hardwood/) · [scad](parts/xa-plinth.scad) |
| [Cartridge screws, bushings and shims](../parts/cartridge-hardware.md) | XA and XB hardware set, screw lengths #1 to #4 | Aluminum, per the drawing | XA: fitted by AR; XB: fitted by AR; AR77XB: unconfirmed | Reference; buy it | [#1, 0.183 in](exports/cartridge-screw-xa-xb-aluminium/cartridge-screw-xa-xb-aluminium-1.pdf) · [#2, 0.356 in](exports/cartridge-screw-xa-xb-aluminium/cartridge-screw-xa-xb-aluminium-2.pdf) · [#3, 0.462 in](exports/cartridge-screw-xa-xb-aluminium/cartridge-screw-xa-xb-aluminium-3.pdf) · [#4, 0.612 in](exports/cartridge-screw-xa-xb-aluminium/cartridge-screw-xa-xb-aluminium-4.pdf) | [Folder](exports/cartridge-screw-xa-xb-aluminium/) · [scad](parts/cartridge-screw-3-48.scad) |
| [Cartridge screws, bushings and shims](../parts/cartridge-hardware.md) | XA and XB hardware set, thicknesses #1 to #3 | Cardboard, per the drawing | XA: fitted by AR; XB: fitted by AR; AR77XB: unconfirmed | Complete | [#1, 0.045 in](exports/shim-block-xa-xb-cardboard/shim-block-xa-xb-cardboard-1.pdf) · [#2, 0.080 in](exports/shim-block-xa-xb-cardboard/shim-block-xa-xb-cardboard-2.pdf) · [#3, 0.125 in](exports/shim-block-xa-xb-cardboard/shim-block-xa-xb-cardboard-3.pdf) | [Folder](exports/shim-block-xa-xb-cardboard/) · [scad](parts/headshell-shim-block.scad) |
| [Cartridge screws, bushings and shims](../parts/cartridge-hardware.md) | XA and XB hardware set, heights #1 to #3 | Soft plastic, grade not established | XA: fitted by AR; XB: fitted by AR; AR77XB: unconfirmed | Complete | [#1, 0.050 in](exports/standoff-bushing-xa-xb-plastic/standoff-bushing-xa-xb-plastic-1.pdf) · [#2, 0.100 in](exports/standoff-bushing-xa-xb-plastic/standoff-bushing-xa-xb-plastic-2.pdf) · [#3, 0.150 in](exports/standoff-bushing-xa-xb-plastic/standoff-bushing-xa-xb-plastic-3.pdf) | [Folder](exports/standoff-bushing-xa-xb-plastic/) · [scad](parts/headshell-standoff-bushing.scad) |
| [Cartridge screws, bushings and shims](../parts/cartridge-hardware.md) | XA and XB hardware set, the one set screw | Brass, per the drawing | XA: unconfirmed; XB: unconfirmed; AR77XB: unconfirmed | Reference; buy it | [PDF](exports/set-screw-xa-xb-brass/set-screw-xa-xb-brass.pdf) | [STEP](exports/set-screw-xa-xb-brass/set-screw-xa-xb-brass.step) · [scad](parts/set-screw-4-40.scad) |
| [Counterweight](../parts/counterweight.md) | XA brass weight, 1961 to 1979 | Brass, alloy not established; the original is reported as brass | XA: fitted by AR; XB: unconfirmed; AR77XB: unconfirmed | 3 placeholders, 2 derived | [PDF](exports/counterweight-xa-brass/PRELIMINARY-counterweight-xa-brass.pdf) | [STEP](exports/counterweight-xa-brass/PRELIMINARY-counterweight-xa-brass.step) · [scad](parts/counterweight.scad) |
| [Counterweight](../parts/counterweight.md) | XA weight remade in stainless steel: same mass, longer body | Stainless steel, 304 taken as the example | XA: fits with a change; XB: unconfirmed; AR77XB: unconfirmed | 3 placeholders, 2 derived | [PDF](exports/counterweight-xa-stainless/PRELIMINARY-counterweight-xa-stainless.pdf) | [STEP](exports/counterweight-xa-stainless/PRELIMINARY-counterweight-xa-stainless.step) · [scad](parts/counterweight.scad) |
| [Counterweight](../parts/counterweight.md) | XA weight remade in aluminium: same mass, longer body | Aluminium, 6061 taken as the example | XA: fits with a change; XB: unconfirmed; AR77XB: unconfirmed | 3 placeholders, 2 derived | [PDF](exports/counterweight-xa-aluminium/PRELIMINARY-counterweight-xa-aluminium.pdf) | [STEP](exports/counterweight-xa-aluminium/PRELIMINARY-counterweight-xa-aluminium.step) · [scad](parts/counterweight.scad) |
| [Cueing height gauge](../parts/cueing-height-gauge.md) | XB: steps at 1/4 and 7/16 in | Rigid plastic, printed or milled. Soft enough not to chip a stylus if touched | XB: fits; XA: does not fit; AR77XB: unconfirmed | Complete | [PDF](exports/cueing-height-gauge-xb-plastic/cueing-height-gauge-xb-plastic.pdf) | [STEP](exports/cueing-height-gauge-xb-plastic/cueing-height-gauge-xb-plastic.step) · [scad](parts/cueing-height-gauge.scad) |
| [Headshell](../parts/headshell.md) | Top-mount shell for a Grado Master4: this repository's design, not an AR part | PMMA (acrylic), cast grade preferred | XA: unconfirmed; XB: unconfirmed; AR77XB: unconfirmed | Concept: 23 placeholders, 2 derived | [PDF](exports/headshell-top-mount-pmma/PRELIMINARY-headshell-top-mount-pmma.pdf) | [STEP](exports/headshell-top-mount-pmma/PRELIMINARY-headshell-top-mount-pmma.step) · [scad](parts/headshell-pmma-top-mount.scad) |
| [Hinge drilling template](../parts/hinge-template.md) | XB hinged cover, September 1976 to January 1977: cover holes | Card or thin plastic | XB: fits; XA: unconfirmed; AR77XB: unconfirmed | 1 placeholder | [PDF](exports/hinge-template-xb-cover-card/PRELIMINARY-hinge-template-xb-cover-card.pdf) | [STEP](exports/hinge-template-xb-cover-card/PRELIMINARY-hinge-template-xb-cover-card.step) · [scad](parts/hinge-template.scad) |
| [Hinge drilling template](../parts/hinge-template.md) | XB hinged cover, September 1976 to January 1977: base holes | Card or thin plastic | XB: fits; XA: unconfirmed; AR77XB: unconfirmed | 0 placeholders | [PDF](exports/hinge-template-xb-base-card/PRELIMINARY-hinge-template-xb-base-card.pdf) | [STEP](exports/hinge-template-xb-base-card/PRELIMINARY-hinge-template-xb-base-card.step) · [scad](parts/hinge-template.scad) |
| [Overhang template](../parts/overhang-template.md) | New design from the factory overhang; AR's own outline (XA part 914, XB P/N 402001) is not known | Clear acrylic (PMMA) suggested | XA: fits; XB: fits; AR77XB: unconfirmed | 5 placeholders | [PDF](exports/overhang-gauge-new-pmma/PRELIMINARY-overhang-gauge-new-pmma.pdf) | [STEP](exports/overhang-gauge-new-pmma/PRELIMINARY-overhang-gauge-new-pmma.step) · [scad](parts/overhang-gauge.scad) |
| [Platter height gauge](../parts/platter-height-gauge.md) | XB: steps at 11/32, 3/8 and 13/32 in | Rigid plastic, printed or milled; a stack of shim stock also works | XB: fits; XA: does not fit; AR77XB: unconfirmed | Complete | [PDF](exports/platter-height-gauge-xb-plastic/platter-height-gauge-xb-plastic.pdf) | [STEP](exports/platter-height-gauge-xb-plastic/platter-height-gauge-xb-plastic.step) · [scad](parts/platter-height-gauge.scad) |
| [Platter height gauge](../parts/platter-height-gauge.md) | XA: one step at 1/8 in, no tolerance stated | Rigid plastic, printed or milled; a stack of shim stock also works | XA: fits; XB: does not fit; AR77XB: unconfirmed | Complete | [PDF](exports/platter-height-gauge-xa-plastic/platter-height-gauge-xa-plastic.pdf) | [STEP](exports/platter-height-gauge-xa-plastic/platter-height-gauge-xa-plastic.step) · [scad](parts/platter-height-gauge.scad) |
| [Strobe disc](../parts/strobe-disc.md) | 60 Hz mains: outer ring 33 1/3 rpm, inner ring 45 rpm | Card, or paper glued to card | XA: fits; XB: fits; AR77XB: unconfirmed; The AR Turntable and Legend: fits; EB-101: fits | 1 placeholder, 1 derived | [PDF](exports/strobe-disc-60hz-card/PRELIMINARY-strobe-disc-60hz-card.pdf) | [STEP](exports/strobe-disc-60hz-card/PRELIMINARY-strobe-disc-60hz-card.step) · [scad](parts/strobe-disc.scad) |
| [Strobe disc](../parts/strobe-disc.md) | 50 Hz mains: outer ring 33 1/3 rpm; no 45 rpm ring, see note 1 | Card, or paper glued to card | XA: fits; XB1: unconfirmed; The AR Turntable and Legend: fits; EB-101: fits | 1 placeholder, 1 derived | [PDF](exports/strobe-disc-50hz-card/PRELIMINARY-strobe-disc-50hz-card.pdf) | [STEP](exports/strobe-disc-50hz-card/PRELIMINARY-strobe-disc-50hz-card.step) · [scad](parts/strobe-disc.scad) |
<!-- end of drawings table -->

Each folder holds the PDF drawing, STEP for machining, STL for printing, and DXF. A `PRELIMINARY-` file still has placeholders: do not order from it. A `DERIVED-` file has no placeholders but still has derived values: print it for a fit test, do not order it in final material.

## Reading a drawing

Three kinds of dimension, told apart by colour:

| Colour | Tag | Meaning | What to do |
| --- | --- | --- | --- |
| Black | none | From the cited source: a factory document, an owner report, a community drawing, a standard, a design choice, or a measurement made for this repository | Use it |
| Blue | DV | Derived: worked out from cited sources, not yet verified on a real part. The register on page 2 gives the derivation and how to verify it | Fit-test it; verify it on an original before ordering in final material |
| Red | PH | Placeholder: chosen only so the model has a shape. Not a measurement | Measure it first |

A value may be derived in only three ways: arithmetic on sourced values, such as a unit conversion, a sum, or a density times a volume; a fit constraint, where one sourced part must fit inside or onto another; or scaling from a photograph, only when a sourced dimension lies in the same plane of the same photo, with the reference, the photo, and an error estimate stated. Scaling is the weakest kind and the row says so. No dimension is ever read off a factory drawing with a ruler: the sheets say "do not scale".

- The ID after each dimension (`CW3`, `HD10`) matches page 2 of the PDF and [TO-CONFIRM.md](../TO-CONFIRM.md#cad-dimensions-needed), which has a row for every DV and PH value.
- No tolerances are given. Agree them with the maker.
- Sheets with a third page are meant to be printed at 100%: measure the check bar after printing.

## Status of a sheet

| Status | Meaning |
| --- | --- |
| Complete | Every dimension from the cited source |
| Reference | A part to buy, drawn for identification only |
| Derived | No placeholder left, at least one DV left. Prototype and fit test only |
| Preliminary | Placeholders left. Not for manufacture |
| Concept | A new layout with placeholders. Not for manufacture |

## Changing a value

Edit the row in table `P` at the top of the part file: set the value, and change its code to `M` once measured. When a DV value is measured, close its row in `TO-CONFIRM.md` as Confirmed or Differs; if it differs, the Result cell keeps both numbers. Then rebuild.

## Rebuilding

Needs OpenSCAD 2021.01 and Python.

```text
python3 -m venv venv
venv/bin/pip install -r cad/tools/requirements.txt
venv/bin/python cad/tools/build.py                # all parts, and rewrite the table above
venv/bin/python cad/tools/build.py counterweight  # one part file
venv/bin/python cad/tools/build.py --check        # every PH and DV row is logged; the table is current
```
