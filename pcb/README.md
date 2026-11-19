# Wiring boards

[Home](../README.md)

Three small boards that replace the loose wiring inside an AR turntable. Each one screws flat to the inside face of a plinth wall, where the factory glued and stapled its wiring. The silkscreen on each board is the wiring diagram, so the board cannot be wired from memory or from a forum post.

Status of all three: **PRELIMINARY**, revision C. They pass the checks listed below. None has been built or fitted to a table yet.

## Gotchas

- **The power board carries mains voltage.** Unplug the table before touching it. It is an open design, not a safety certified product. Have the work checked if you are not experienced with mains wiring.
- **The boards are sized for a wall with 80 mm of free height. That figure is an assumption.** No source gives the plinth height (TO-CONFIRM row PL12). The tallest board is 70 mm. Measure your wall, from the underside of the top plate to the bottom panel, before ordering.
- **Parts stick out from the wall into the plinth.** The motor capacitor is the tallest. Add its height, the board (1.6 mm) and the spacer (6 mm), and check that against the distance from the wall to the nearest moving part: sub-chassis, motor, belt, platter.
- **Use spacers behind every board.** The solder joints stick out about 2 mm at the back and must not touch the wood. Behind the power board, also fit an insulating sheet.
- **The fuse value is not known.** It comes from the motor label (TO-CONFIRM row IE1). Do not guess it.
- **The power board circuit is the XA circuit.** It comes from the XA service manual, page 3. For the XB and the AR77XB the motor leads and capacitor values must be read on the table first.
- **One point in the 120 V circuit is a reading, not a printed fact.** The manual's 120 V drawing does not show where the white lead of winding 1 returns. The board sends it to neutral. Check that on an unmodified table before power. See [power-board](power-board/README.md#to-confirm-before-power).
- **Arm wires are soldered, never put in a screw terminal.** They are hair thin and a screw cuts them.

## The boards

| Board | What it does | Size, length x height | Where | Folder |
|---|---|---|---|---|
| Power board | Fuse, switch capacitor, motor capacitor, 120 V or 220 V links, screw terminals for mains in, switch, motor and top plate earth | 130 x 70 mm | Rear wall or a side wall, near the motor and the power inlet | [power-board](power-board/README.md) |
| Audio strip board | Replaces the audio terminal strip. Five solder pads for the arm wires, screw terminals to the two jacks and the ground post | 72 x 47 mm | Rear wall, right-hand end, next to the arm pivot stud | [audio-strip-board](audio-strip-board/README.md) |
| Rear jack panel | Bare fibreglass panel for two RCA jacks and the ground post. No copper, so the jacks cannot short to each other or to the metalwork | 135 x 60 mm | Inside of the rear wall, over a cutout | [rear-jack-panel](rear-jack-panel/README.md) |

Mains and audio are on separate boards on purpose. Put the power board at the far end from the audio strip board and keep mains wires away from the arm wires.

There is no panel for the power inlet yet: no inlet part is chosen and no datasheet is held (SR26).

## How every board mounts

1. The long edge is horizontal. Wires run along the wall, so the screw terminals are on the two ends of the board and the wires enter from the left and from the right.
2. Number 6 wood screws through the 3.5 mm holes, each through a nylon spacer 6 mm or longer, into the wall.
3. The power board and the audio strip board have their parts facing into the plinth. The rear jack panel has its printed face against the wood, showing through the cutout.

## How the three fit together

1. Power inlet (the standard computer power cord socket, with a fuse drawer or without) in the plinth rear wall. Its three wires go to J1 on the power board.
2. Power board: J2 to the turntable's own switch, J3 to the motor, J4 to a ring lug on the top plate.
3. Audio strip board next to the arm pivot stud. Arm wires soldered in. J6 and J8 by short twisted pairs to the two jacks, J7 to the ground post.
4. Rear jack panel over the plinth cutout, carrying the jacks and the ground post.
5. One separate wire from the ground post to the amplifier's ground terminal. The old strap from the metalwork to the audio shield is removed.

## Open the projects

Each folder is one KiCad project: open the `.kicad_pro` file. The files were written by KiCad 7.0.11. KiCad 8 and 9 open them and offer to save in their newer format.

The symbols are stored inside each schematic. The standard footprints are stored inside each board. The six project footprints are in [lib/artt.pretty](lib/artt.pretty), and each project's `fp-lib-table` points to that folder.

Each project folder holds:

| File or folder | Content |
|---|---|
| `*.kicad_pro`, `*.kicad_sch`, `*.kicad_pcb` | The KiCad project, schematic and board |
| `docs/` | Schematic as PDF, board previews as SVG and PNG (top and bottom) |
| `fab/` | Gerber and drill files for a board house. Zip this folder to order |
| `bom.csv` | Parts list |
| `drc-report.txt` | KiCad's design rule check report |

## What was checked

Run by `tools/check.py` on every board:

| Check | Result |
|---|---|
| Netlist exported from the schematic compared with the board, pad by pad | Power board: 23 pads on 8 nets agree. Audio strip board: 15 pads on 5 nets agree |
| KiCad design rule check | 0 errors and 0 unconnected pads on all three boards |
| The rule check itself, tested by breaking a copy of the power board | A raised clearance rule was reported, and a deleted track was reported as an unconnected pad |
| Smallest copper gap between two different mains nets, power board | 3.25 mm (rule: 2.5 mm) |
| Smallest copper gap between protective earth and any other net, power board | 4.5 mm (rule: 4.0 mm) |

The only warnings in the reports say that the standard KiCad footprint libraries were not installed in the user settings of the machine that ran the check. They do not appear on a normal KiCad install.

## What was not checked

- No board has been ordered, assembled or powered.
- The projects were loaded by KiCad's own command line tool and Python module, not opened in the KiCad window.
- Fit on the wall of any model: free height, free depth, and where the corner blocks are.
- Capacitor body sizes against the parts you will buy. The motor capacitor outline is 32 x 13 mm and the switch capacitor outline is 19 x 9 mm.
- The jack hole size against your jacks.

## Tools

| Script | Use |
|---|---|
| [tools/generate.py](tools/generate.py) | Wrote the three projects. Do not run it over a board you have edited in KiCad: it overwrites the files |
| [tools/check.py](tools/check.py) | Runs the checks above and exports `docs/` and `fab/`. Safe to run at any time |

Both need KiCad 7 or later with its Python module.

## Sources

Each link opens the copy kept in this repository.

- [XA service manual, pp. 3 and 4](../docs/originals/xa-service-manual.pdf). Factory. Motor circuit, capacitor values, audio terminal strip.
- [XB drawing 119](../docs/drawings/xb-drawing-119.png). Factory. XB terminal strip detail and part numbers.
- [RCA jacks in the plinth](../models/xa/mods/rca-jacks.md) and [IEC mains inlet in the plinth](../models/xa/mods/iec-inlet.md). Ground scheme, cutout size, ground post recipe.
