# IEC mains inlet in the plinth

[XA](../README.md) · [Mods](README.md) · [Home](../../../README.md)

## Purpose

Fit a detachable mains cord. This mod works on mains voltage. The idea also applies to the XB.

Building all three plinth mods at once: see the [plinth rebuild](plinth-rebuild.md).

## Stock situation

The manual's diagrams show a two-pin plug and no fuse: see [Historical capacitor values](../README.md#historical-capacitor-values) and the [XA service manual, p. 3](../../../docs/originals/xa-service-manual.pdf). The [XB parts list](../../xb/README.md#factory-component-identifiers) has no fuse item either.

## Parts

| Part | What is established |
| --- | --- |
| Fused IEC C14 inlet: Schurter KD series or equivalent | Fuse-links of 5 × 20 mm or 6.3 × 32 mm, 10 A, protection class I (Unconfirmed). Panel thickness depends on the part number; some versions include a switch |
| Fuse | Value TBC, from the motor's rated current |
| Mains cord with earth | To suit the inlet and your country |
| Earth wire, ring lug, and fixing to the top plate | Size TBC |

## Procedure

Unplug the table before starting. Have someone qualified check the work if you are not experienced with mains wiring.

1. Read the motor's rated current from its label. Choose the fuse from that.
2. Cut the window for the inlet. John's XA build used a template, a coping saw, and a file, working up to a snug fit because his socket had little lip.
3. Wire the line through the fuse to the stock switch circuit, keeping the capacitors as they were. Wire neutral to its stock point.
4. Bond the inlet's earth pin to the metal top plate.
5. Build the ground scheme below.
6. Cover every exposed mains terminal.

![Proposed ground scheme: one star point at the ground post, with mains earth bonded to the top plate](../../../docs/images/grounding-scheme.png)

## Gotchas

- **The stock XA has no fuse and a two-wire cord.** A three-pin inlet means mains earth must be bonded to the metal top plate.
- **It can add hum.** Your phono stage may have its own earth, which gives a second earth path through the signal ground. Check on your table whether the top plate is tied to signal ground.
- **Keep one star point.** Mains earth goes to the top plate, signal ground goes to the ground post, and one link joins the plate to the post. Nothing else is bridged.
- **Never lift mains earth to cure hum.** If hum remains, change the phono ground lead.
- **The capacitor across the switch sits on the mains.** See [Motor phase capacitor](motor-capacitor.md).

## Verification

1. With the table unplugged, check continuity from the inlet's earth pin to the top plate.
2. Check that line and neutral are not connected to the top plate.
3. Plug in, then run a hum check with the phono stage connected, with the ground lead on and then off. Keep whichever is quieter.

## Sources

Each link opens the copy kept in this repository; the copy names its original address.

- [XA service manual, p. 3](../../../docs/originals/xa-service-manual.pdf). Factory.
- [John's second XA restoration](../../../docs/archive/johns-weather/xa-restoration-2012.md). Owner report.
- [Gary Galo, "A Belt-Drive Turntable Upgrade", audioXpress](../../../docs/archive/audioxpress/galo-belt-drive-turntable-upgrade.pdf).
