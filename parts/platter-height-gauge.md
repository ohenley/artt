# Platter height gauge

[Find your part](README.md) · [Part index](reproduction.md) · [CAD drawings](../cad/README.md) · [Things to confirm](../TO-CONFIRM.md#platter-bearings-and-suspension)

## What it is

A stepped block slid under the edge of the outer platter to check the suspension height: the low step must pass, the high step must not. The height is set with the three suspension nuts. Photo wanted: the gauge under an XB platter.

**Do not use the XB gauge on an XA.** The two tables sit at different heights: ⅜ in on the XB, ⅛ in on the XA.

## Versions

| Version | Fitted by AR to | Material | How to recognise it | Dimensions | Mass | Label and source |
| --- | --- | --- | --- | --- | --- | --- |
| XB gauge, this repository | Nobody. Checks the XB setting: outer platter ⅜ in ± ¹⁄₃₂ above the top plate (Factory, [drawing 119](../docs/drawings/xb-drawing-119.png), note 13) | Rigid plastic, printed or milled | Three steps and a handle | Steps ¹¹⁄₃₂, ⅜, ¹³⁄₃₂ in (8.73, 9.53, 10.32 mm) | About 10 g | Factory for the steps |
| XA gauge, this repository | Nobody. Checks the XA setting: with a heavy record on, the outer platter rides ⅛ in above the top plate at all points (Factory, [XA service manual, p. 2](../docs/originals/xa-service-manual.pdf)) | Same | One step and a handle | Step ⅛ in (3.18 mm). No tolerance is given | About 8 g | Factory for the step |

AR supplied no such gauge; both are new designs from the factory numbers.

## What fits what

| Version | XA | XB | XB1 | AR77XB | The AR Turntable and Legend | EB-101 | ES-1 | ETL-1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XB gauge | Does not fit: the XA platter rides ⅛ in (Factory, service manual p. 2) | Fits (Factory, drawing 119, note 13) | Unconfirmed | Unconfirmed: the [AR77XB page](../models/ar77xb/README.md#what-to-use-until-ar77xb-figures-exist) uses the XB figure as a starting point only | Unconfirmed | Unconfirmed | Unconfirmed | Unconfirmed |
| XA gauge | Fits (Factory, service manual p. 2) | Does not fit: the XB platter rides ⅜ in (Factory, drawing 119, note 13) | Unconfirmed | Unconfirmed | Unconfirmed | Unconfirmed | Unconfirmed | Unconfirmed |

## Drawings

| Version and material | Status | PDF | STEP | Source |
| --- | --- | --- | --- | --- |
| XB, plastic | Complete | [PDF](../cad/exports/platter-height-gauge-xb-plastic/platter-height-gauge-xb-plastic.pdf) | [STEP](../cad/exports/platter-height-gauge-xb-plastic/platter-height-gauge-xb-plastic.step) | [scad](../cad/parts/platter-height-gauge.scad), variant 1 |
| XA, plastic | Complete | [PDF](../cad/exports/platter-height-gauge-xa-plastic/platter-height-gauge-xa-plastic.pdf) | [STEP](../cad/exports/platter-height-gauge-xa-plastic/platter-height-gauge-xa-plastic.step) | same file, variant 2 |

## If you make or change it

**Keep:** the step heights. A printed part's first layer is often thicker than drawn: measure each step with calipers before use.

**Free:** the length, width, handle and material. Keep it narrow enough to pass between the platter edge and the arm.

**What else is affected:**

- **The suspension height** is what the gauge checks; adjust it with the three nuts (XB item 32, #10-24; XA item 17, part 1095). See [what goes where](../docs/what-goes-where.md#every-screw-by-job).
- **The arm spindle and cueing cylinder** must keep 0.050 in minimum clearance in the top plate hole on the XB (Factory, drawing 119, note 13); check it after any height change.
- **The belt:** a belt that is too tight pulls the subchassis toward the motor and tilts the platter.

## Check after fitting

1. XB: mat and one record on, or record what you did; drawing 119 does not say. XA: a heavy record on.
2. Slide the gauge under the platter edge at the front, the back, and both sides.
3. XB: the ¹¹⁄₃₂ step passes everywhere and the ¹³⁄₃₂ step passes nowhere. XA: the ⅛ step just passes everywhere.
4. If not, adjust the nearest suspension nut and go round again.
5. The case that fails: the low step passes at the front but not at the back. The platter is tilted: adjust, do not average.

## Still to measure

PL2 and PL3 in [TO-CONFIRM.md](../TO-CONFIRM.md#platter-bearings-and-suspension).

## Sources

Each link opens the copy kept in this repository.

- [XB drawing 119](../docs/drawings/xb-drawing-119.png), note 13. Factory.
- [XA service manual, p. 2](../docs/originals/xa-service-manual.pdf). Factory.
