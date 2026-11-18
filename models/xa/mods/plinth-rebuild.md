# Plinth rebuild

[XA](../README.md) · [Mods](README.md) · [Drawing](../../../cad/exports/xa-plinth/PRELIMINARY-xa-plinth-1.pdf) · [Checklist](../../../TO-CONFIRM.md#plinth)

## Purpose

One hardwood plinth that carries the RCA jack plate, the ground post, the fused IEC inlet, and the stock-style audio terminal strip. It is built from one drawing, so every cutout is placed before any wood is cut.

## What it bundles

- [RCA jacks in the plinth](rca-jacks.md): the jack plate and ground post.
- [IEC mains inlet in the plinth](iec-inlet.md): the fused inlet and the earth scheme.
- [Tonearm rewire](tonearm-rewire.md): the arm wires and their pin map.
- [Hardwood plinth](hardwood-plinth.md): the wood, the profile, and the feet.

## Wiring plan

| Junction | Method | Why |
| --- | --- | --- |
| Arm wires to terminal strip | Solder | Service point when the T-bar comes out |
| Terminal strip to RCA jacks | Solder, short twisted pairs | No screw contacts on the phono signal |
| Shield to ground post | Solder to a ring lug, lug under the post nut | One ground point |
| IEC inlet to switch and capacitor | Insulated spade terminals or solder | Mains joints stay covered |
| IEC earth to top plate | Ring lug under a top plate screw, star washer | Bonds the plate to mains earth |

## Parts

| Part | What is established |
| --- | --- |
| Hardwood stock | Species and thickness TBC. Plywood for the test piece |
| RCA jacks | See the [jack table](rca-jacks.md#parts) |
| Ground post | Galo: 6-32 × ⅝ in machine screw, #6 lug, lock washer, hex nut, knurled thumbnut |
| IEC inlet | Fused C14. Cutout TBC from its datasheet |
| Terminal strip | The stock part, or a 5-post solder strip. Hole spacing TBC |
| Top plate fixings | TBC |
| Feet | Any stable foot. Hole size TBC |

## Procedure

1. Measure the original base, top plate off: the [plinth checklist](../../../TO-CONFIRM.md#plinth).
2. Enter the values in [xa-plinth.scad](../../../cad/parts/xa-plinth.scad).
3. [Rebuild](../../../cad/README.md#rebuilding). The [base](../../../cad/exports/xa-plinth/PRELIMINARY-xa-plinth-1.pdf) and [bottom panel](../../../cad/exports/xa-plinth/PRELIMINARY-xa-plinth-2.pdf) drawings should show no red dimensions.
4. Cut a plywood test plinth. Fit the top plate, jack plate, inlet, and strip.
5. Cut the hardwood one.

## Gotchas

- **No screw-clamp terminal block on the signal path.** Panel-style blocks are for amps, not microvolts, and they add mass under the T-bar.
- **Keep the rear cutouts clear of the T-bar swing.** Measure the closest approach of the subchassis and the motor to the rear wall first.
- **The wall is thicker than the jack thread.** The jacks go on a thin plate over the window.
- **Metal jacks on a metal plate short the grounds.** Use insulated jacks or nylon shoulder washers.
- **Keep one star point.** Mains earth to the top plate, signal ground to the ground post, one link between them.
- **Solid hardwood moves with humidity.** Use quartersawn or laminated stock, and keep the cutouts away from glue lines.

## Verification

1. The top plate sits flat with no rocking.
2. The subchassis moves freely in every direction, with no pull from the wires.
3. Unplugged: continuity from the inlet's earth pin to the top plate, and none from line or neutral to the plate.
4. Each jack ground is open to the plate and to the other channel before the arm is wired.
5. Hum check with the phono stage connected, ground lead on and then off.

## Sources

Each link opens the copy kept in this repository; the copy names its original address.

- [XA service manual, pp. 3 and 4](../../../docs/originals/xa-service-manual.pdf). Factory.
- [XB drawing 119](../../../docs/drawings/xb-drawing-119.png). Factory.
- [Gary Galo, "A Belt-Drive Turntable Upgrade", audioXpress](../../../docs/archive/audioxpress/galo-belt-drive-turntable-upgrade.pdf). Owner report.
- [John's second XA restoration](../../../docs/archive/johns-weather/xa-restoration-2012.md). Owner report.
