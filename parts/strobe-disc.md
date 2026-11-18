# Strobe disc

[Find your part](README.md) · [Part index](reproduction.md) · [Motor and pulley](motor-and-pulley.md) · [CAD drawings](../cad/README.md) · [Things to confirm](../TO-CONFIRM.md#other-parts)

## What it is

A card disc with rings of black bars that stands still under a mains-powered lamp when the platter runs at the right speed. AR's own test used "a standard 216-line stroboscope card" (Factory, [AR spec sheet](../docs/archive/vinyl-nirvana/ar-turntable-history/1969-ar-xa-technical-specifications.md)). Photo wanted: the disc AR packed with the XA, if one survives; the owner's manual photograph shows "a round disc" among the packed items.

**A disc for the wrong mains frequency reads a wrong speed as right.** Print the one for your mains.

## Versions

Number of lines = 2 × mains frequency × 60 / speed in rpm. Each number below was recomputed for this page.

| Version | Fitted by AR to | Material | How to recognise it | Dimensions | Mass | Label and source |
| --- | --- | --- | --- | --- | --- | --- |
| 60 Hz disc, this repository | Any table on 60 Hz mains | Card | Outer ring 216 bars, inner ring 160 bars | 216 lines for 33⅓ rpm: also the figure on AR's spec sheet. 160 lines for 45 rpm: derived | About 4 g | Factory for 216; derived for 160 |
| 50 Hz disc, this repository | Any table on 50 Hz mains | Card | One ring of 180 bars, no 45 rpm ring | 180 lines for 33⅓ rpm: derived. For 45 rpm the formula gives 133.33, not a whole number, so that ring is not drawn | About 4 g | Derived |
| AR's own card | Packed with the XA: the manual lists "a round disc" among the parts (Factory, [XA owner's manual, scan p. 1](../docs/archive/vinyl-nirvana/ar-turntable-history/ar-xa-manual.md)); the service manual says to check speed "with a strobe disc" (Factory, [XA service manual, p. 1](../docs/originals/xa-service-manual.pdf)) | Unconfirmed | Unconfirmed | Unconfirmed: 216 lines if it was the standard card | Unconfirmed | Factory for its existence |

## What fits what

| Version | XA | XB | XB1 | AR77XB | The AR Turntable and Legend | EB-101 | ES-1 | ETL-1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 60 Hz disc | Fits: tested on a 216-line card to 21 lines a minute (Factory, spec sheet; service manual p. 1) | Fits: ±21 dots a minute at 1.5 g (Factory, [drawing 119](../docs/drawings/xb-drawing-119.png), test A) | Unconfirmed: a 220 to 240 V table whose mains frequency is not stated | Unconfirmed: speeds not stated for the AR77XB | Fits: 33⅓ and 45 rpm at 60 Hz (Factory, [1983 brochure](../docs/archive/vinyl-nirvana/ar-turntable-history/ar-the-turntable-brochure.md)) | Fits: 33⅓ and 45 rpm (Factory, [GB brochure](../docs/archive/vinyl-nirvana/ar-turntable-history/ar-legend-and-eb-101-brochure-from-great-britain.md)) | Unconfirmed | Unconfirmed: electronic speed control (Specialist) |
| 50 Hz disc | Fits: a 50 cycle pulley gives the same speeds on 50 Hz (Factory, service manual p. 1) | Unconfirmed | Unconfirmed | Unconfirmed | Fits: 50 Hz supply (Factory, 1983 brochure) | Fits (Factory, GB brochure) | Unconfirmed | Unconfirmed |

## Drawings

| Version and material | Status | PDF | DXF | Source |
| --- | --- | --- | --- | --- |
| 60 Hz, card | Preliminary: the spindle hole is a placeholder; the line counts are sourced or derived. Page 3 prints at 1:1 | [PDF](../cad/exports/strobe-disc-60hz-card/PRELIMINARY-strobe-disc-60hz-card.pdf) | [1:1 outline](../cad/exports/strobe-disc-60hz-card/PRELIMINARY-strobe-disc-60hz-card-flat-1to1.dxf) | [scad](../cad/parts/strobe-disc.scad), variant 1 |
| 50 Hz, card | Preliminary, as above | [PDF](../cad/exports/strobe-disc-50hz-card/PRELIMINARY-strobe-disc-50hz-card.pdf) | [1:1 outline](../cad/exports/strobe-disc-50hz-card/PRELIMINARY-strobe-disc-50hz-card-flat-1to1.dxf) | same file, variant 2 |

Print page 3 of the PDF at 100 percent and measure the check bar: it must be 100 mm.

## If you make or change it

**Keep:** the line counts, 216 and 160 at 60 Hz, 180 at 50 Hz, and bars of equal width to the gaps. The disc must be centred on the spindle: the spindle hole is SD3.

**Free:** the disc diameter, the ring widths, the card.

**What else is affected:** nothing on the table. The reading depends on the lamp: use an incandescent or fluorescent lamp on the mains, not an LED lamp or a flashlight, whose flicker is not the mains frequency or is absent.

## Check after fitting

1. Print at 100 percent. Measure the check bar: 100 mm.
2. Cut the disc out, cut the spindle hole, and lay it on the record.
3. Run the platter at 33⅓ under a mains lamp. The outer ring stands still, or creeps.
4. Count the lines that pass a fixed point in one minute. AR's limit is 21 (Factory, spec sheet; service manual p. 1), which is 0.29 percent of the 7,200 lines that pass in a minute at 33⅓ rpm. The XB test is at 1.5 g stylus force (Factory, drawing 119, test A); the spec sheet adds 5 g of extra stylus force to stand in for a dust brush.
5. Repeat at 45 rpm on the inner ring, on a 60 Hz disc.
6. The case that fails: the disc stands still at 33⅓ but the music is sharp. Then the lamp is not at the mains frequency, or the disc is for the other mains. Check the lamp first.

## Still to measure

SD1 to SD3 in [TO-CONFIRM.md](../TO-CONFIRM.md#other-parts).

## Sources

Each link opens the copy kept in this repository.

- [AR technical specifications sheet](../docs/archive/vinyl-nirvana/ar-turntable-history/1969-ar-xa-technical-specifications.md). Factory.
- [XA service manual, p. 1](../docs/originals/xa-service-manual.pdf). Factory.
- [XA owner's manual, scan p. 1](../docs/archive/vinyl-nirvana/ar-turntable-history/ar-xa-manual.md). Factory.
- [XB drawing 119](../docs/drawings/xb-drawing-119.png), performance test A. Factory.
- [1983 brochure](../docs/archive/vinyl-nirvana/ar-turntable-history/ar-the-turntable-brochure.md) and [GB brochure](../docs/archive/vinyl-nirvana/ar-turntable-history/ar-legend-and-eb-101-brochure-from-great-britain.md). Factory.
