# Tonearm rewire

[XA](../README.md) · [Mods](README.md) · [Home](../../../README.md)

## Purpose

Replace the aged original wire. The usual failure point is where the wires pass through the top plate, from years of rubbing on the edge of the hole.

The XB uses a similar arrangement, with different wire colors on [drawing 119](../../../docs/originals/xb-drawing-119.tif). Nothing is confirmed for the AR77XB.

## Stock situation

See [Wire and audio cable](../README.md#wire-and-audio-cable). The arm carries four signal wires and a silver ground braid, according to Scott Hamrick's account.

## Parts

| Part | Gauge | Evidence |
| --- | --- | --- |
| Cardas Original tonearm wire | 33 AWG | Seller listing; used by Hamrick and John |
| Cardas Clear tonearm wire | 34 AWG | Seller listing |
| Zavfino 1877Phono 5LITZ-7 | 33 AWG | Seller listing |
| Zavfino 1877Phono LITZ-76 | 34 AWG | Seller listing |
| ConneX tonearm wire | 36 AWG in the listing found, so outside the 33 to 34 AWG range. To confirm on the part | Seller listing |

Also needed: cartridge clips, if yours are damaged, plus thin solder and a fifth thin wire for ground. Hamrick found that his first ground wire left a low buzz until he changed it.

## Procedure

This follows Hamrick's account. Expect about five hours.

1. Before cutting anything, write down which color goes to which headshell pin and which terminal post. Orient the receptacle by its red line. Record how the ground braid is routed.
2. Cut the wires where they pass through the top plate, then lift off the arm. Keep the small ball from the bearing well.
3. Remove the headshell, then ease the white plastic receptacle out of the arm tube. It is soft, tightly fitted, and held by two dimples and a little glue.
4. Solder the new wires to the receptacle's hollow pins. They move if overheated.
5. Thread the collar and washer onto the wires, feed the wires through the tube, and refit the receptacle.
6. Secure the wires in the channel under the pivot so they cannot rub on the joint. Keep the middle of the channel clear.
7. Refit the arm, run the wires through the top plate, and solder them to the posts, leaving a few inches of slack.
8. Write down the final color and pin map.

Use the block that matches what you find. Do not assume either one.

**AR's shell wire code, from AR sheet L-1591:**

```text
Red    right hot
Black  right ground
White  left hot
Green  left ground
```

**The modern cartridge code, used by Galo's Cardas wiring:**

```text
Red    right signal
Green  right ground
White  left signal
Blue   left ground
```

## Gotchas

- **Green means opposite things.** On AR's sheet, green is left ground. In the modern code, green is right ground. Check every pin with an ohmmeter instead of trusting a color.
- **The wire can kill the suspension.** The wire loop between the arm and the jacks must not restrain the subchassis. Too short or too stiff kills the suspension.
- **The wire can also pull the arm.** Hamrick warns that tension can impede tracking and cause a reverse anti-skate force.
- **Do not go thicker than 33 AWG.** Hamrick reports that 33 AWG is already slightly thicker than the original.
- **The small ball is easy to lose.** The arm runs badly without it: see [Service details](../README.md#service-details).

## Verification

1. Check each channel's signal and ground from cartridge clip to output, with no shorts between them or to ground.
2. Balance the arm so it floats, then tap the headshell from side to side. Hamrick's test: if the arm tends to return to a central position, adjust the wires.
3. Confirm the subchassis still moves freely.
4. Play a record, and check that left and right are correct and there is no hum.

## Sources

- [Scott Hamrick, "Rewiring an AR XA Tonearm", Vinyl Nirvana](https://vinylnirvana.com/ar-turntable-resources/ar-diy-do-it-yourself/rewiring-an-ar-xa-tonearm). Owner report.
- [AR sheet L-1591](../../../docs/originals/ar-cartridge-mount.jpg). Factory.
- [Gary Galo, "A Belt-Drive Turntable Upgrade", audioXpress](https://audioXpress.com/assets/upload/files/galo2931.pdf). Wiring key in Figure 1.
- [Parts Connexion tonearm wire](https://partsconnexion.com/tonearm-bulk-wire) and [Zavfino 5LITZ-7 kit](https://partsconnexion.com/products/1877phono-5litz-7-direct-wire-rewiring-kit-2m). Seller listings.
- [John's first XA restoration](https://www.johnsweather.com/Turntable1.html). Owner report using Cardas 4 × 33 shielded cable.
