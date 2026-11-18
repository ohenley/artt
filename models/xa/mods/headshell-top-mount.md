# Headshell with top mounting holes

[XA](../README.md) · [Mods](README.md) · [CAD](../../../cad/README.md) · [Things to confirm](../../../TO-CONFIRM.md#cad-dimensions-needed)

## Purpose

Fit a Grado Master4 to the stock arm. Its screws enter from the top, into the cartridge's wood body. Pat's Audio sells one shell for both the XA and XB, so the connector appears to be shared.

## Stock shell

| Item | What is known |
| --- | --- |
| Body | "A light plastic" with threaded mounting studs (Factory, AR sheet L-1591) |
| Layout | Headshell, item 20, part 1175: a box open underneath, a round rear neck with contact pins, a finger lift on one side near the front. Knurled retaining nut, item 21C, on the arm (Factory, XA service manual, p. 4) |
| XB part number | Cartridge-shell assembly 404003 (Factory, drawing 119) |
| Contacts | Four in the arm's receptacle (Owner report, Hamrick); four wires (Factory, sheet L-1591) |
| Mounting hardware | [Screws, bushings, and shims](../../../docs/what-goes-where.md#why-are-there-so-many-cartridge-screws) |
| Body, neck, locking, and pin dimensions | Unconfirmed. No drawing or CAD file found |

## New shell

A shell in clear acrylic (PMMA) with two recessed slots on top and a pocket underneath for the cartridge. [Drawing](../../../cad/exports/headshell-pmma-top-mount/PRELIMINARY-headshell-pmma-top-mount.pdf) · [STEP](../../../cad/exports/headshell-pmma-top-mount/PRELIMINARY-headshell-pmma-top-mount.step) · [Source](../../../cad/parts/headshell-pmma-top-mount.scad). 23 dimensions are placeholders: rows GR and HD in the confirmation list.

| Item | Value |
| --- | --- |
| Master4 mass | 9.6 g (Maker claim, Grado) |
| Master4 tracking force | 1.6–1.9 g (Maker claim, Grado) |
| Master4 compliance | 20 µm/mN (Maker claim, Grado) |
| Master4 body size and screws | Not published. Grado says the housing was reshaped |
| Stand-in body, Grado Opus3 | 20.1 mm wide, 16.3 mm tall, 25.3 mm deep, 29.6 mm with pins, 18.3 mm top to stylus tip; bolts "screw in from the top" (Addicted to Audio review) |
| Slot spacing | 12.7 mm, the standard ½ in mount. Not stated by Grado |
| Shell mass, model estimate | About 10 g, without pins or wires |
| Stylus below the shell underside | 5.8 mm, using the Opus3 figure |
| Arm resonance estimate | About 8 Hz at 20 g total moving mass, from 159 / √(mass × compliance). The arm's own effective mass is Unconfirmed |

## Procedure

1. Measure a stock shell, its retaining nut, and the Master4: rows GR and HD.
2. Enter the values in the source file and [rebuild](../../../cad/README.md#rebuilding). No red dimensions should remain.
3. Print the STL in cheap plastic. Test the neck, pins, and screw length on the arm.
4. Order the shell in PMMA.
5. Wire it, then set the overhang with the slots: see [What is an overhang gauge?](../../../docs/what-goes-where.md#what-is-an-overhang-gauge)

## Gotchas

- **The neck is the weak point.** Pat's Audio advertises a reinforced neck with threads "that won't crack off" (Maker claim). PMMA is brittle, so a metal neck insert may be needed.
- **Confirm the balance before buying.** The counterweight must balance the shell and the Master4 together. AR's sheet already calls for an extra counterweight section with some cartridges.
- **Weight lowers arm resonance.** Measure the finished shell, and keep it light.
- **Threadlocker and solvents craze PMMA.** Skip the factory's Loctite here.
- **Do not overtighten.** A review of the Opus3 warns that wood bodies may not take many cycles of screw insertion.
- **Check record clearance.** The stylus sits only a few millimeters below the shell's underside.
- **A thin acrylic finger lift breaks.** Measure the stock lift, and make the new one thicker.
- **The finger lift is flat in plan with an outward arc, not swept downward like the original.** A downward sweep is a 3D contour and costs a second CNC setup.
- **Grados can pick up hum.** Galo needed hum shielding for an unshielded Grado Signature 10MR. Grado's Master4 page does not cover this.
- **It needs three machining setups:** the top, the bottom, and the neck end. Published minimum PMMA walls range from 0.5 to 1.0 mm; plan for 1.0 mm.

## Verification

1. All four pins connect correctly, with no shorts, before the cartridge goes on.
2. The arm balances, and reaches 1.6 to 1.9 g tracking force.
3. Overhang checks at 0.688 in with a gauge.
4. The mounting plane is parallel to the record. XB note 10 allows ±1°.
5. No hum at the inner groove with the motor running.
6. The shell clears the record at the arm's working angle.

## Sources

Each link opens the copy kept in this repository; the copy names its original address.

- [XA service manual, p. 4](../../../docs/originals/xa-service-manual.pdf). Factory.
- [AR sheet L-1591](../../../docs/originals/ar-cartridge-mount.jpg). Factory.
- [XB drawing 119](../../../docs/drawings/xb-drawing-119.png). Factory.
- [Scott Hamrick, "Rewiring an AR XA Tonearm"](../../../docs/archive/vinyl-nirvana/ar-diy-do-it-yourself/rewiring-an-ar-xa-tonearm.md). Owner report.
- Grado's own Master4 page. Maker claim. No copy is kept, because the shop limits automated requests; its address is in the [archive index](../../../docs/archive/README.md#not-archived). The same specifications are in a retailer's listing: [Sound Approach](../../../docs/archive/sound-approach/grado-master4.md).
- [Pat's Audio XA/XB headshell](../../../docs/archive/pats-audio/ar-xa-xb-headshell.md). Maker claim.
- [Gary Galo, "A Belt-Drive Turntable Upgrade", audioXpress](../../../docs/archive/audioxpress/galo-belt-drive-turntable-upgrade.pdf).
- [Addicted to Audio: Grado Opus3](../../../docs/archive/addicted-to-audio/grado-opus3-review.md).
- [Positive Feedback: Grado Opus3](../../../docs/archive/positive-feedback/grado-opus3-review.md).
