# Overhang template

[Find your part](README.md) · [Part index](reproduction.md) · [What is an overhang gauge?](../docs/what-goes-where.md#what-is-an-overhang-gauge) · [CAD drawings](../cad/README.md) · [Things to confirm](../TO-CONFIRM.md#other-parts)

## What it is

A flat template that drops over the spindle; when the stylus rests in its small hole the overhang is right, 0.688 in (17.48 mm) past the spindle on the AR arm (Factory, [Villchur 1962, Part 1, p. 69](../docs/originals/villchur-1962-part-1.pdf)). Photo wanted: AR's own template, marked "AIM TOWARD PIVOT".

## Versions

| Version | Fitted by AR to | Material | How to recognise it | Dimensions | Mass | Label and source |
| --- | --- | --- | --- | --- | --- | --- |
| XA template, part 914 | XA, packed with every table: "Overhang Template, 914" in the accessories list (Factory, [XA service manual, p. 4](../docs/originals/xa-service-manual.pdf)); sold as 1400011-7 "Overhang Adjustment Template" in 1979 (Factory, [price list](../docs/archive/vinyl-nirvana/ar-turntable-history/1979-xa-price-list.md)) | Plastic: "a plastic template that fits over the spindle" (Factory, Villchur p. 69) | "The plastic guide supplied with the turntable marked AIM TOWARD PIVOT" (Factory, [XA owner's manual, scan p. 4](../docs/archive/vinyl-nirvana/ar-turntable-history/ar-xa-manual.md)) | Hole distance 0.688 in. The outline is not known | Unconfirmed | Factory |
| XB gauge, P/N 402001 | XB: "overhang 0.688 ± 0.030 in, gauge P/N 402001" (Factory, [drawing 119](../docs/drawings/xb-drawing-119.png), note 10) | Unconfirmed | Unconfirmed | Hole distance 0.688 in; the outline is not known | Unconfirmed | Factory |
| New design, this repository | Nobody. A template for tables that have lost theirs | Clear acrylic suggested | A 40 × 18 mm plate with a spindle hole, a stylus hole and two scribed tolerance lines | Hole distance 0.688 in; the rest is design freedom with placeholders | About 2 g | Design, [drawing](../cad/exports/overhang-gauge-new-pmma/PRELIMINARY-overhang-gauge-new-pmma.pdf) |

## What fits what

| Version | XA | XB | XB1 | AR77XB | The AR Turntable and Legend | EB-101 | ES-1 | ETL-1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XA template, 914 | Fitted by AR (Factory, service manual p. 4) | Unconfirmed: same 0.688 in, but AR gave the XB its own number | Unconfirmed | Unconfirmed | Does not fit: the 1983 arm's overhang is ¹⁹⁄₃₂ in (15 mm) (Factory, [1983 brochure](../docs/archive/vinyl-nirvana/ar-turntable-history/ar-the-turntable-brochure.md)) | Does not fit: overhang 16 mm (Factory, [GB brochure](../docs/archive/vinyl-nirvana/ar-turntable-history/ar-legend-and-eb-101-brochure-from-great-britain.md)) | Does not fit: ¹⁹⁄₃₂ in (Specialist, [VN ES-1](../docs/archive/vinyl-nirvana/ar-models/ar-es-1.md)) | Unconfirmed: sold without an arm |
| XB gauge, 402001 | Unconfirmed: same 0.688 in | Fitted by AR (Factory, drawing 119, note 10) | Unconfirmed | Unconfirmed | Does not fit (as above) | Does not fit (as above) | Does not fit (as above) | Unconfirmed |
| New design | Fits (Factory, Villchur p. 69: 0.688 in) | Fits (Factory, drawing 119, note 10: 0.688 ± 0.030 in) | Unconfirmed | Unconfirmed | Does not fit (as above) | Does not fit (as above) | Does not fit (as above) | Unconfirmed |

## Drawings

| Version and material | Status | PDF | STEP | Source |
| --- | --- | --- | --- | --- |
| New design, acrylic | Preliminary: 5 placeholders (the two hole sizes and the plate), with a 1:1 cutting DXF | [PDF](../cad/exports/overhang-gauge-new-pmma/PRELIMINARY-overhang-gauge-new-pmma.pdf) | [STEP](../cad/exports/overhang-gauge-new-pmma/PRELIMINARY-overhang-gauge-new-pmma.step) | [scad](../cad/parts/overhang-gauge.scad) |
| XA 914 and XB 402001 | No drawing. Missing: AR's outline, from a surviving template with a rule beside it | | | |

## If you make or change it

**Keep:** the distance between the two holes, 0.688 in. Only that is functional. The XB allows ±0.030 in on the overhang (Factory, drawing 119, note 10); the drawing scribes two lines at that distance either side of the stylus hole, and the hole itself should be made far tighter than the tolerance.

**Free:** the outline, the thickness as long as it clears the spindle shoulder and the arm at cueing height, the material, the colour.

**What else is affected:**

- **The arm's effective length.** On the XA the overhang is set by loosening the overhang set screw, item 21J, part 1123, sliding the arm tube, and retightening (Factory, service manual p. 4; the method is Villchur p. 69: "the effective arm length is adjusted").
- **The stylus force.** Moving the arm tube moves mass; reset the [counterweight](counterweight.md) and check the force again.
- **The [headshell](headshell.md) and cartridge:** a cartridge whose stylus is not ⅜ in in front of its mounting centres, the factory setting (Factory, Villchur p. 69), needs the adjustment.

## Check after fitting

1. Drop the template over the spindle with the small hole on the line from the spindle to the arm's pivot.
2. Lower the stylus gently. It should land in the small hole, or between the two scribed lines on an XB.
3. If not, adjust the arm length and try again.
4. Measure the template's hole distance with calipers before trusting it: 0.688 in, as close as you can make it.

## Still to measure

GA2 to GA6 in [TO-CONFIRM.md](../TO-CONFIRM.md#other-parts).

## Sources

Each link opens the copy kept in this repository.

- [Villchur 1962, Part 1, p. 69](../docs/originals/villchur-1962-part-1.pdf). Factory.
- [XA service manual, p. 4](../docs/originals/xa-service-manual.pdf) and [1979 price list](../docs/archive/vinyl-nirvana/ar-turntable-history/1979-xa-price-list.md). Factory.
- [XA owner's manual, scan p. 4](../docs/archive/vinyl-nirvana/ar-turntable-history/ar-xa-manual.md). Factory.
- [XB drawing 119](../docs/drawings/xb-drawing-119.png), note 10. Factory.
- [1983 brochure](../docs/archive/vinyl-nirvana/ar-turntable-history/ar-the-turntable-brochure.md) and [GB brochure](../docs/archive/vinyl-nirvana/ar-turntable-history/ar-legend-and-eb-101-brochure-from-great-britain.md). Factory.
- [Vinyl Nirvana ES-1](../docs/archive/vinyl-nirvana/ar-models/ar-es-1.md). Specialist.
