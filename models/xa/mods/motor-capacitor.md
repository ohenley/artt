# Motor phase capacitor

[XA](../README.md) · [Mods](README.md) · [Home](../../../README.md)

## Purpose

Replace the aged capacitor with a new film part of tighter tolerance. This works on mains voltage.

The XB has its own capacitor parts, 803002 and 803004, with no values on its drawing, so XA values do not transfer. Nothing is confirmed for the AR77XB.

## Stock situation

See [Historical capacitor values](../README.md#historical-capacitor-values) and [Motor identification](../README.md#motor-identification). The existing dielectric is to confirm on the part.

## Parts

A film capacitor with the value read from the old part, rated 600 V DC, from DigiKey or Mouser. Compare what you read with the block for your table.

**XA, 120 V circuit, from the service manual, p. 3:**

```text
C1, motor:         0.1 uF, 600 VDC
C2, across switch: 0.022 uF, 600 VDC
```

**XA, 220 V conversion, from the service manual, p. 3:**

```text
C1, motor:         0.39 uF, 600 VDC
C2, across switch: 0.01 uF, 600 VDC
```

**Early two-motor tables and replacement motors:** values are to confirm on the part. The manual's diagram does not cover them.

## Procedure

Unplug the table first.

1. Record the motor label, serial number, and mains voltage.
2. Record the motor's temperature after one hour and a strobe speed reading, as a baseline.
3. Read the old capacitor's markings. If they differ from the block above, stop and find out why, since the table may have been modified.
4. Note which wires go where. On XA176235 to XA204462 the motor's wire colors differ: see the manual, p. 3.
5. Fit the new part, using the existing strap or clamp. Insulate the joints.

## Gotchas

- **The value depends on motor variant and line voltage.** A wrong value makes the motor vibrate or run hot.
- **This is a phase-shift capacitor.** It is not an electrolytic, and it is not a power supply cap.
- **A DC rating is not an AC rating.** The 600 VDC figure is historical. **Our assessment:** check the new part's datasheet for continuous use on your mains voltage. C2 sits across the switch on the mains, so a safety-rated part is worth considering.
- **C1 and C2 are different parts.** Do not swap them.
- **The XA and XB values are not interchangeable.** Only XA values are documented here.

## Verification

1. Motor temperature after one hour should be no worse than your baseline.
2. Check speed with a strobe disc. The XA manual allows no more than ±21 dots per minute.
3. The motor should start cleanly and run without extra vibration.

## Sources

- [XA service manual, pp. 1 and 3](../../../docs/originals/xa-service-manual.pdf). Factory.
- [XB drawing 119](../../../docs/originals/xb-drawing-119.tif). Factory, part numbers only.
