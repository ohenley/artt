# Headshell with top mounting holes

[XA](../README.md) · [Mods](README.md) · [Home](../../../README.md)

## Purpose

Fit a Grado wood-body cartridge, Master series, to the stock arm. The screws of these cartridges enter from the top.

Pat's Audio sells its own shell for both the XA and XB, so the connector appears to be shared. Fit on the AR77XB is unconfirmed.

## Stock situation

See [Screws and replacements](../README.md#screws-and-replacements) and the [headshell reference](../../../docs/headshells.md). No dimensioned drawing of the stock shell has been found.

## Parts

| Part | What is established |
| --- | --- |
| Shell in crystal clear acrylic (PMMA) | [Concept model and drawing](../../../cad/README.md#the-pmma-headshell). 21 dimensions are placeholders |
| Slots at 12.7 mm spacing | The standard ½ in mount. Check it on the cartridge; Grado's Master4 page does not state it |
| Four contact pins | Hamrick describes four contacts in the arm's receptacle. Type and size to confirm on the part |
| Grado screws | Supplied with the cartridge. Thread to confirm on the part |
| Grado Master4 | Maker lists 9.6 g, 1.6 to 1.9 g tracking force, 20 µm/mN compliance |

## Procedure

1. Measure a stock shell and your cartridge, using the [confirmation list](../../../TO-CONFIRM.md#cad-dimensions-needed).
2. Copy the stock connector bore and mounting plane height, then enter the values in the model.
3. Rebuild the model, and check that no red dimensions remain.
4. Print a test piece and fit it to the arm.
5. Order the shell in acrylic.
6. Wire it, then set the overhang with the short slots: see [What is an overhang gauge?](../../../docs/what-goes-where.md#what-is-an-overhang-gauge).

## Gotchas

- **Confirm the balance before buying.** The counterweight must balance the Grado and the shell together. AR's own sheet already calls for an extra counterweight section with some cartridges.
- **A thin acrylic finger lift breaks.** Make it thicker than stock. Measure the stock lift first.
- **Grados can pick up hum.** Galo describes the Grado Signature 10MR as unshielded, and needed hum shielding for it. Grado's Master4 page does not cover this, so check for motor hum at the inner groove.
- **The neck is the weak point.** Pat's Audio advertises threads "that won't crack off", which suggests the problem is known. Acrylic is brittle, so a metal insert may be needed.
- **Threadlocker and solvents can craze acrylic.** Do not carry over the factory's Loctite habit here.
- **Do not overtighten.** A review of the Opus3 warns that wood bodies may not take many cycles of screw insertion.
- **Weight affects arm resonance.** Every gram of shell lowers it: see the [CAD notes](../../../cad/README.md#the-pmma-headshell).

## Verification

1. All four pins connect correctly, with no shorts, before the cartridge goes on.
2. The arm balances, and reaches 1.6 to 1.9 g tracking force on the Master4.
3. Overhang checks at 0.688 in with a gauge.
4. The mounting plane is parallel to the record. XB note 10 allows ±1°.
5. Check for hum at the inner groove with the motor running.
6. The shell clears the record at the arm's working angle.

## Sources

- [XA service manual, p. 4](../../../docs/originals/xa-service-manual.pdf). Factory layout.
- [AR sheet L-1591](../../../docs/originals/ar-cartridge-mount.jpg). Factory.
- [Scott Hamrick, "Rewiring an AR XA Tonearm"](https://vinylnirvana.com/ar-turntable-resources/ar-diy-do-it-yourself/rewiring-an-ar-xa-tonearm). Owner report.
- [Grado Master4](https://gradolabs.com/products/master4). Maker page.
- [Pat's Audio XA headshell](https://www.patsaudioparts.com/single-post/AR-XA-XB-Headshell). Maker claim.
- [Gary Galo, "A Belt-Drive Turntable Upgrade", audioXpress](https://audioXpress.com/assets/upload/files/galo2931.pdf).
- [Positive Feedback: Grado Opus3](https://positive-feedback.com/reviews/hardware-reviews/grado-timbre-series-opus3-phono-cartridge/). Review of a related model.
