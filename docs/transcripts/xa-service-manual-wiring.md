# XA service manual, pages 3 and 4: the wiring in words

[Home](../../README.md) · [Document index](../README.md) · [XA wiring](../../models/xa/wiring.md)

- Source: [xa-service-manual.pdf](../originals/xa-service-manual.pdf), page 3 (two schematics and a drawing of the underside) and page 4 (the terminal strip detail in the exploded view). Read at the scan's full size, 2400 pixels wide for page 3 and 6000 pixels wide for page 4.
- Label: Factory.
- Date: not printed.
- Checked by a person: no.

Crops of the three pictures are kept in `docs/images/`: [the two schematics](../images/xa-wiring-schematic-factory.png), [the underside drawing](../images/xa-wiring-underside-factory.png) and [the terminal strip](../images/xa-terminal-strip-factory.png).

## The 120 volt schematic

Printed values: C-1 is 0.1 mfd at 600 VDC, C-2 is 0.022 mfd at 600 VDC.

The plug has two wires. Call them the line wire and the neutral wire; the schematic does not name them.

1. The line wire goes to a node. From that node the circuit goes through the switch to a second node. C-2 is drawn between the two nodes, so it sits across the switch.
2. From the second node a wire runs to a junction. The junction feeds two branches.
3. Branch one goes through C-1 to the motor lead marked RED. That lead is the lower end of the first winding. The upper end of the first winding is the lead marked WHT, at the top of the drawing.
4. Branch two goes straight to the motor lead marked WHT, the upper end of the second winding. The lower end of the second winding is the lead marked GRE.
5. The neutral wire runs along the bottom of the drawing to the GRE lead.
6. The four leads are drawn in this order from top to bottom: WHT, RED, WHT, GRE. A rectangle labelled "motor windings" is drawn round the two coils. Its left edge passes through the top WHT node and the GRE node, so the frame joins the top of the first winding to the neutral node. No separate return wire is drawn for the top WHT lead.

Reading: both windings return to the neutral node, the first through C-1 from the switched line and the second straight from the switched line. On the 220 volt schematic the same frame is drawn dashed, and the text says the dashed lines are the connections that were altered, which supports reading the frame as a conductor. The reading is still a reading, not a printed statement: row EL11 in [things to confirm](../../TO-CONFIRM.md#motor-electrical-and-overall-size).

Footnote on the page: for serial numbers XA176235 thru XA204462 inclusive, the wire colours are gray, blue, red, gray in order. In the order drawn, that is gray for the top WHT, blue for RED, red for the lower WHT, and gray for GRE.

## The 220 volt schematic

Printed values: C-1 is 0.39 mfd at 600 VDC, C-2 is 0.01 mfd at 600 VDC. The dashed lines are the altered connections.

1. The plug, the switch and C-2 are as at 120 volts.
2. The top WHT lead is now joined by a dashed line to the junction after the switch. C-1 still runs from that junction to the RED lead. So the first winding and C-1 are in parallel between the junction and the RED node.
3. The lower WHT lead is now joined by a dashed line to the RED node, not to the junction. So the second winding follows the first in series, and its GRE end still goes to the neutral wire.
4. The frame round the windings is dashed: the join between the top WHT lead and the neutral node is gone.

The text under the schematics says: a 0.01 microfarad capacitor must be substituted for the one wired across the switch; a 0.39 microfarad capacitor must be connected in place of the one wired to the motor; two wiring changes must be made as shown; the colours marked correspond to the coloured wires from the motor, which exit from the motor paired according to winding.

## The underside drawing

A view of the underside of the top plate with the bottom cover off. The power cord enters at the lower left through a clamp. A wire labelled YELLOW runs from the cord to the switch, which is the knurled lever at the lower left. A wire labelled GRAY runs from the switch to the right. The motor is drawn in the middle on its square plate and labelled HAYDON MOTOR. Three of its leads are labelled where they leave the motor: WHITE, going down and left to a crimp joint; RED, going right to the capacitor marked 0.1 MFD, which is held by a strap on the rear wall; and, at the bottom, GREEN and WHITE, each ending in a crimp joint near the cord. The labels HAYDON, WHITE, RED, GREEN and WHITE are printed with a line through them on this scan; the line does not hide them. The drawing names no joint by circuit position, so it cannot settle EL11 by itself.

## The terminal strip, page 4

The exploded view on page 4 shows the audio terminal strip as a bar with seven screws: a round-head screw at each end, which hold the strip, and five square-head screws between them, which are the lugs. Each lug has a solder tab on each side of the bar. Leaders on the left name the cable side: WHITE SHIELD, WHITE, RED, RED SHIELD, GRAY and BLACK. Leaders on the right name the arm side: GREEN; YELLOW, PINK or BLUE; RED; COPPER; and SHIELD.

Pairing as read, lug 1 at the top:

| Lug | Cable side | Arm side |
| --- | --- | --- |
| 1 | White shield: the loop from the white lead's braid | Green |
| 2 | White: the white lead's centre conductor | Yellow, pink or blue |
| 3 | Red: the red lead's centre conductor | Red |
| 4 | Red shield: the loop from the red lead's braid | Copper |
| 5 | Gray, and black | Shield: the large loop from the arm wire bundle |

The gray and black leaders both point at wires reaching the bottom of the strip, and the black wire also runs on downwards, out of the picture. Whether both land on lug 5 or one lands on a mounting screw cannot be told from the drawing. The drawing is an isometric sketch with crowded leaders, so the whole pairing is a reading: row EL13. The 220 volt text, the parts list and the rest of the manual do not mention the strip.
