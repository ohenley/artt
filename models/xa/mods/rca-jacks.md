# RCA jacks in the plinth

[XA](../README.md) · [Mods](README.md) · [Home](../../../README.md)

## Purpose

Stop the stiff interconnect from loading the floating subchassis. Thin tonearm wire runs from the arm to jacks fixed in the plinth, so any interconnect can be used. The idea also applies to the XB, whose [cable and terminal parts](../../xb/README.md#factory-component-identifiers) differ.

## Stock situation

The stock cable leaves the base directly, and stock capacitance is known only for that cable: see [Wire and audio cable](../README.md#wire-and-audio-cable).

## Parts

Chassis-mount RCA jacks.

| Jack | Panel hole | Maximum panel | Insulated from the panel? |
| --- | --- | --- | --- |
| KLEI Copper Harmony, Parts Connexion SKU KLEI-86829 | M10 (Maker claim) | TBC | Listing mentions a high-temperature polymer, not isolation. TBC |
| KLEI Classic Harmony, Parts Connexion SKU KLEI-86827 | TBC | 7.0 mm (Unconfirmed). TBC | TBC |
| Neutrik NF2D-B-2 | TBC | TBC | "Red isolation washers" and a zinc die-cast shell (Maker claim). TBC |
| AECO ARJ-4045 | TBC | TBC | TBC |
| D.H. Labs CM-R1, used by Galo | ⅜ in, with its insulating washers | TBC | Galo used the supplied insulating washers. Availability TBC |

Also needed: a separate ground post next to the jacks. Galo's recipe is a 6-32 × ⅝ in machine screw, #6 ground lug, lock washer, hex nut, and knurled thumbnut. The insulated post adds a nylon shoulder washer and flat washer.

## Procedure

Measure the wall of your base first. Both routes come from other builds.

**Route A, jacks directly in the wood (Owner report, John's XA):**

1. On the inside of the wall, drill a ⅝ in counterbore about 5/16 in deep. Do not go all the way through.
2. Drill ⅜ in through the center of that hole.
3. Fit the jacks, then wire them from the inside.

**Route B, jacks on a plate (Galo):**

1. Cut a plate. Galo used 0.064 in brass, 2 in wide and 5⅜ in long.
2. Drill it for the jacks, ground posts, and a nylon cable clamp.
3. Cut a window in the wall. Galo's was about 1⅜ × 4⅛ in in his oak base.
4. Fix the plate with screws. Galo used five #6 × ⅝ in brass wood screws.

**Both routes:**

1. Record which arm wire goes where before cutting anything. See [Tonearm rewire](tonearm-rewire.md).
2. Solder the arm's signal pairs to the jacks, with the shield to the ground post.
3. Clamp the cable so no strain reaches the thin conductors.
4. Leave enough free wire that the subchassis moves without restraint.

## Gotchas

- **The wall is thicker than the jack thread.** Counterbore the inside of the wall, or mount the jacks on a thin plate in a cutout.
- **Metal jacks on a metal plate short the grounds.** Use insulated jacks or nylon shoulder washers.
- **Galo's turntable is not a stock XA.** It has a Merrill sub-chassis and a Grado arm, so his dimensions are examples.
- **Capacitance changes.** The stock figure of about 135 pF applies to the stock cable. The new total depends on your arm wire and interconnect.

## Verification

Before wiring the arm:

1. Check continuity between each jack ground and the plate. It should be open.
2. Check continuity between the left and right grounds. It should be open.

After wiring:

1. Check signal and ground on each channel with an ohmmeter, as Galo does.
2. Bounce the platter and confirm the subchassis moves freely, with no pull from the wire.
3. Play a record and listen for hum.

## Sources

- [Gary Galo, "A Belt-Drive Turntable Upgrade", audioXpress](https://audioXpress.com/assets/upload/files/galo2931.pdf).
- [John's first XA restoration](https://www.johnsweather.com/Turntable1.html) and [second restoration](https://www.johnsweather.com/Turntable.html). Owner report.
- [KLEI Copper Harmony](https://partsconnexion.com/klei-copper-harmony-rca-female-jacks-2) and [KLEI Classic Harmony](https://partsconnexion.com/klei-classic-harmony-rca-female-jacks-1), Parts Connexion. Maker claim.
- [Neutrik NF2D-B-2](https://www.neutrik.com/en/product/nf2d-b-2). Maker claim.
- [AECO ARJ-4045 seller listing](https://yeo.ro/conector-socket-rca-aeco-arj-4045-silver-plated/p/ad73d04678780ba3c161710a4825995f).
