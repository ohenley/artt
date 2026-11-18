# Hinge drilling template

[Find your part](README.md) · [Part index](reproduction.md) · [XB cover dimensions](../models/xb/README.md#cover-dimensions-and-clearance) · [CAD drawings](../cad/README.md) · [Things to confirm](../TO-CONFIRM.md#motor-electrical-and-overall-size)

## What it is

Two cards that mark the hinge screw holes on an XB dust cover and base, from the hinge detail on the factory drawing (Factory, [drawing 114](../docs/drawings/xb-drawing-114.png), revision S). Photo wanted: a hinged XB cover.

**Do not drill the cover from this template yet.** The drawing gives the end-to-first-hole distance as both 2.20 in and 60.6 mm, which differ by 4.7 mm. That row stays red until a hinged cover is measured: DM4.

## Versions

| Version | Fitted by AR to | Material | How to recognise it | Dimensions | Mass | Label and source |
| --- | --- | --- | --- | --- | --- | --- |
| XB hinged cover | XB tables built between ECO 1135, 14 September 1976, and ECO 1315, 28 January 1977; the hinge was then deleted (Factory, [drawing 119](../docs/drawings/xb-drawing-119.png), revision block). Hardware: four #6 × 0.375 in wood screws, four #4-40 × 0.375 in screws, four #4-40 dome nuts (Factory, [drawing 113](../docs/drawings/xb-drawing-113.png)) | | Four 0.15 in holes along the cover's lower rear edge, four 0.11 in holes in the base's top rear edge | See the [XB page](../models/xb/README.md#cover-dimensions-and-clearance): all nine values as printed | | Factory |
| Cover template, this repository | Nobody. Marks the two holes at one end of the cover; turn it over for the other end | Card | Two holes | Holes 0.98 in apart, 0.57 in from the edge, 0.15 in diameter; first hole 2.20 in or 60.6 mm from the end, Conflict | | Factory values; DM4 red |
| Base template, this repository | Nobody. Marks the two holes at one end of the base | Card | Two holes | Holes 0.98 in apart, 1.00 in from the top edge, 0.11 in diameter and 0.37 in deep; first hole 2.28 in from the end | | Factory values |

Every dimension is kept in inches as printed, with the drawing's millimetre figure beside it in the register.

## What fits what

| Version | XA | XB | XB1 | AR77XB | The AR Turntable and Legend | EB-101 | ES-1 | ETL-1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Both templates | Unconfirmed: the XA cover had no hinge in any source read | Fits the hinged XB of September 1976 to January 1977 (Factory, drawing 114; drawing 119 revision block). Other XBs had no hinge | Unconfirmed | Unconfirmed | Unconfirmed | Unconfirmed | Unconfirmed | Unconfirmed |

## Drawings

| Version and material | Status | PDF | DXF | Source |
| --- | --- | --- | --- | --- |
| Cover template, card | Preliminary: DM4 is a placeholder | [PDF](../cad/exports/hinge-template-xb-cover-card/PRELIMINARY-hinge-template-xb-cover-card.pdf) | [1:1 outline](../cad/exports/hinge-template-xb-cover-card/PRELIMINARY-hinge-template-xb-cover-card-flat-1to1.dxf) | [scad](../cad/parts/hinge-template.scad), variant 1 |
| Base template, card | Preliminary: the card size is a design choice, the holes are sourced | [PDF](../cad/exports/hinge-template-xb-base-card/PRELIMINARY-hinge-template-xb-base-card.pdf) | [1:1 outline](../cad/exports/hinge-template-xb-base-card/PRELIMINARY-hinge-template-xb-base-card-flat-1to1.dxf) | same file, variant 2 |

## If you make or change it

**Keep:** the hole positions from the end and from the edge, the 0.98 in pair spacing, and the hole sizes. The two rows sit 1.26 in apart with the cover on (Factory, drawing 114); check that on your parts before drilling the base.

**Free:** the card's outline and material.

**What else is affected:**

- **The cover's clearance:** the assembled hinge shows 0.05 in (1.5 mm) between cover and base (Factory, drawing 114). A new [cover](../models/xa/mods/dust-cover.md) or [plinth](plinth.md) changes it.
- **The base's rear wall:** the base holes are 0.37 in deep pilot holes into the top edge; a thin rear wall or a new cutout nearby weakens them.

## Check after fitting

1. Measure a hinged cover and base first, and close DM4. Only then drill the cover.
2. Hold the base template in the rear corner: its end against the end of the base, its edge against the top edge. Prick the two holes. Turn it over for the other end.
3. Drill 0.11 in pilot holes 0.37 in deep.
4. Fit the hinges to the base, hang the cover, and check the 0.05 in clearance along the whole rear edge before drilling the cover.
5. The case that fails: the cover binds at one end. One row of holes is off; check the 2.20 in against 2.28 in offsets against your hinges before enlarging anything.

## Still to measure

DM4 in [TO-CONFIRM.md](../TO-CONFIRM.md#motor-electrical-and-overall-size).

## Sources

Each link opens the copy kept in this repository.

- [XB drawing 114](../docs/drawings/xb-drawing-114.png), revision S, sheet 2. Factory.
- [XB drawing 113](../docs/drawings/xb-drawing-113.png), revision S, sheet 1. Factory.
- [XB drawing 119](../docs/drawings/xb-drawing-119.png), revision block. Factory.
