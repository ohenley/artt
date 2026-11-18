# Cueing height gauge

[Find your part](README.md) · [Part index](reproduction.md) · [CAD drawings](../cad/README.md) · [XB setup values](../models/xb/README.md#factory-setup-values)

## What it is

A two-step block that stands on the record to check how far the XB's cueing lift raises the stylus: ¼ to ⁷⁄₁₆ in above the record, with the mat and one record on (Factory, [drawing 119](../docs/drawings/xb-drawing-119.png), note 7). Photo wanted.

**Keep the stylus off the block.** Move the gauge under the raised arm; never swing the arm into it.

## Versions

| Version | Fitted by AR to | Material | How to recognise it | Dimensions | Mass | Label and source |
| --- | --- | --- | --- | --- | --- | --- |
| XB gauge, this repository | Nobody. Checks note 7 on the XB assembly | Rigid plastic, printed or milled | Two steps | ¼ and ⁷⁄₁₆ in (6.35 and 11.11 mm) | About 3 g | Factory for the steps |

AR supplied no such gauge.

## What fits what

| Version | XA | XB | XB1 | AR77XB | The AR Turntable and Legend | EB-101 | ES-1 | ETL-1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XB gauge | Does not fit: the XA has no cueing lever (Specialist, [model guide](../models/README.md#first-family-1961-to-1979)) | Fits (Factory, drawing 119, note 7) | Unconfirmed: the XB1 has the lever, its setting is not stated | Unconfirmed | Unconfirmed | Unconfirmed | Unconfirmed | Unconfirmed |

## Drawings

| Version and material | Status | PDF | STEP | Source |
| --- | --- | --- | --- | --- |
| XB, plastic | Complete | [PDF](../cad/exports/cueing-height-gauge-xb-plastic/cueing-height-gauge-xb-plastic.pdf) | [STEP](../cad/exports/cueing-height-gauge-xb-plastic/cueing-height-gauge-xb-plastic.step) | [scad](../cad/parts/cueing-height-gauge.scad) |

## If you make or change it

**Keep:** the two heights, measured from the face the block stands on. Measure them after printing.

**Free:** everything else. A soft plastic is kinder to a stylus than metal if they ever touch.

**What else is affected:**

- **The cueing lever's adjustment** on the XB is what the gauge checks: the lift must also let the stylus drop at least ¼ in below the record surface when lowered, and the descent takes 1 to 3 seconds (Factory, drawing 119, notes 7 and 8).
- **The platter height:** set it first with the [platter height gauge](platter-height-gauge.md), because the lift height is measured from the record.

## Check after fitting

1. Mat and one record on. Lift the arm with the cueing lever.
2. Stand the gauge on the record and slide it under the stylus, low step first: the stylus clears it.
3. Slide the high step under: the stylus does not clear it.
4. Lower the lever and time the descent: 1 to 3 seconds.
5. The case that fails: the stylus clears both steps. The lift is set too high; the stylus will drop from too far and the cueing is useless.

## Still to measure

Nothing on this part. Whether the XB1 and AR77XB share the setting is open on their pages.

## Sources

Each link opens the copy kept in this repository.

- [XB drawing 119](../docs/drawings/xb-drawing-119.png), notes 7 and 8. Factory.
- [Model guide](../models/README.md). Specialist, for which tables have a cueing lever.
