# Things to confirm

[Home](README.md) · [Adding information](CONTRIBUTING.md) · [Part index](parts/reproduction.md) · [Sources to read](docs/sources-to-read.md)

Bench tasks: claims waiting for a measurement or an inspection.

**Status:** **Open** = not checked. **Conflict** = sources disagree. **Confirmed** = checked and matches. **Differs** = checked and does not match.

After a check, set the status and write the result, model, serial, and date in the Result column. Then update the page that uses the value. A differing result sits beside the earlier value.

## Measure or inspect on a table

### Counterweight and rest

Values now are from the [XA record](parts/xa-counterweight.md) (Owner report). Vinyl Nirvana lists brass for the XA, brass or stainless steel for the XB, and aluminum for the XB77, so record the model.

| ID | What to confirm | Value now | How to check | Status | Result |
| --- | --- | --- | --- | --- | --- |
| CW1 | Mass with set screw | 98.8 g | Balance, screw fitted | Open | |
| CW2 | Mass without set screw | Not recorded | Balance, screw removed | Open | |
| CW3 | Outside diameter | 28 mm | Calipers, at several points | Open | |
| CW4 | Length along bore | 22 mm | Calipers | Open | |
| CW5 | Bore diameter | 9.5 mm | Calipers or pin gauge; note wear | Open | |
| CW6 | Bore through or blind, centered or offset | Not recorded | Inspect; measure the wall around the bore | Open | |
| CW7 | Material | Brass | Inspect; compare density from CW2–CW6 | Open | |
| CW8 | Set screw thread, length, and tip | Not recorded; not the #4-40 in HS3 | Thread gauge, calipers | Open | |
| CW9 | Locking-hole position | Not recorded | Calipers, from one end | Open | |
| CW10 | Tonearm rest height | 39 mm, bottom of yoke to top of top plate | Calipers, installed | Open | |

### Headshell and screws

| ID | What to confirm | Value now, and source | How to check | Status | Result |
| --- | --- | --- | --- | --- | --- |
| HS1 | Original shell thread | #3-48; [community drawing](docs/what-goes-where.md#why-are-there-so-many-cartridge-screws) | Thread gauge or a known #3-48 screw | Open | |
| HS2 | Screw lengths under the head | 0.183, 0.356, 0.462, 0.612 in; same drawing | Calipers, on original screws | Open | |
| HS3 | Where the #4-40 brass set screw goes | #4-40 × 0.125 in; same drawing, location not given | Find it on a table; gauge the thread | Open | |
| HS4 | Shell body material | "A light plastic"; [AR sheet L-1591](docs/originals/ar-cartridge-mount.jpg) | Inspect; record model and serial | Open | |
| HS5 | AR77XB shell material | Metal and plastic; the [Vinyl Nirvana page](models/ar77xb/README.md#mechanical) says both | Inspect an identified AR77XB | Conflict | |

### Platter, bearings, and suspension

| ID | What to confirm | Value now, and source | How to check | Status | Result |
| --- | --- | --- | --- | --- | --- |
| PL1 | Platter mass | 3.3 lb in Villchur, Part 2, p. 36, and the 1969 directory; 3.9 lb (1.8 kg) on Vinyl Nirvana | Balance; inner and outer platter separately | Conflict | |
| PL2 | XA platter clearance | ⅛ in with a heavy record; [XA service manual, p. 2](docs/originals/xa-service-manual.pdf) | Measure on an adjusted XA | Open | |
| PL3 | XB platter clearance | ⅜ in ± ¹⁄₃₂; [drawing 119, note 13](models/xb/README.md#factory-setup-values) | Measure on an adjusted XB | Open | |
| PL4 | Arm thrust disc material | Teflon on p. 1 and nylon on p. 4 of the XA service manual | Inspect the disc; record the serial | Conflict | |
| PL5 | Arm bearing ball diameter | Not recorded | Micrometer | Open | |
| PL6 | Main bearing ball diameter | Not recorded | Micrometer | Open | |
| PL7 | Suspension stud thread and length | XB nut is #10-24 on drawing 119; stud length not recorded | Thread gauge, calipers | Open | |
| PL8 | Belt length, width, and thickness | Not recorded | Measure a new belt, flat and unstretched; note the supplier | Open | |

### Motor, electrical, and overall size

| ID | What to confirm | Value now, and source | How to check | Status | Result |
| --- | --- | --- | --- | --- | --- |
| EL1 | Motor and shaft by serial | [Serial table](models/xa/README.md#motor-identification); manual | Record serial, motor label, shaft diameter | Open | |
| EL2 | Serial gap XA175235–XA176235 | Unassigned in the manual; possibly a misprint | Report the motor on any table in that range | Conflict | |
| EL3 | XA 120 V capacitors | C1 0.1 µF, C2 0.022 µF, both 600 VDC; manual, p. 3 | Read the markings on an unmodified table | Open | |
| EL4 | XB capacitor ratings | Part numbers only; [drawing 119](models/xb/README.md#factory-component-identifiers) | Read the markings on items 44 and 46 | Open | |
| EL5 | AR77XB capacitors and motor | Not recorded | Read the markings and motor label | Open | |
| DM1 | XA size with cover | 16¾ × 12¾ × 5¼ in; [1969 directory](models/xa/README.md#dimensions-and-arm-geometry) | Tape or calipers | Open | |
| DM2 | XA complete weight | 13½ lb; same directory | Scale; note whether cover and mat are included | Open | |
| DM3 | XB and AR77XB overall size and weight | Not recorded | Tape or calipers, scale | Open | |
| DM4 | Hinge position on cover | 2.20 in and 60.6 mm on [drawing 114](models/xb/README.md#cover-dimensions-and-clearance), which do not convert | Measure a hinged XB cover | Conflict | |

## CAD dimensions needed

Placeholders in the [CAD models](cad/README.md), shown in red on each drawing. CW6, CW8, and CW9 above are placeholders too.

### Grado cartridge and top mounting

Target cartridge: the Grado Master4. Published figures and the Opus3 stand-in are on the [headshell page](models/xa/mods/headshell-top-mount.md#new-shell).

| ID | What to confirm | Value now | How to check | Status | Result |
| --- | --- | --- | --- | --- | --- |
| GR1 | Slot width, from the Grado screw | 2.8 mm placeholder | Gauge the supplied screw, add clearance | Open | |
| GR2 | Head recess width | 5.0 mm placeholder | Calipers on the screw head, plus clearance | Open | |
| GR3 | Head recess depth | 1.0 mm placeholder | Set with GR7 and HD4 so the screw does not bottom out | Open | |
| GR4 | Slot travel | 6.0 mm placeholder | Check against GR8 and the arm's own adjustment | Open | |
| GR5 | Slot position on the body | −1.5 mm placeholder | Work out from GR8 and HD1 | Open | |
| GR6 | Pocket width | 21.0 mm placeholder, from the Opus3's 20.1 mm body | Calipers on the cartridge body, plus clearance | Open | |
| GR7 | Master4 screw length and usable thread depth | Not recorded | Calipers; check depth gently, since wood threads can strip | Open | |
| GR8 | Mounting holes to stylus tip | Not recorded; AR's factory setting assumed ⅜ in (Villchur 1962, p. 69) | Calipers or a loupe with a scale | Open | |
| GR9 | Master4 mass, with and without screws | 9.6 g on Grado's page; 10 g on [one retailer's](https://soundapproach.com/grado-master4-timbre-series-turntable-phono-cartridge.html) | Balance | Conflict | |
| GR10 | Master4 body size, and top to stylus tip | Unpublished. Opus3 only: 20.1 × 16.3 × 25.3 mm, 29.6 mm with pins, 18.3 mm top to stylus | Calipers | Open | |
| GR11 | Master4 mounting-hole spacing | ½ in assumed | Calipers, between hole centers | Open | |
| GR12 | Arm effective mass with the finished shell | Not established | Needed with the Master4's 20 µm/mN compliance to estimate resonance | Open | |

### Headshell body and connector

Measure an original shell and its retaining nut, and record the model and serial. Photos of the neck end and the arm socket help.

| ID | What to confirm | Value now | How to check | Status | Result |
| --- | --- | --- | --- | --- | --- |
| HD1 | Body length | 40 mm placeholder, sized to clear the Opus3 | Calipers on the original, then check against GR10 | Open | |
| HD2 | Body width | 25 mm placeholder, sized to clear the Opus3 | Calipers on the original, then check against GR10 | Open | |
| HD3 | Body height | 16 mm placeholder | Calipers | Open | |
| HD4 | Top thickness above the pocket | 3.5 mm placeholder | Calipers on the original; then set from GR7 | Open | |
| HD5 | Front wall thickness | 2.5 mm placeholder | Calipers | Open | |
| HD6 | Rear wall thickness | 6.0 mm placeholder | Calipers | Open | |
| HD7 | Body corner radius | 2.0 mm placeholder | Radius gauge, or choose freely | Open | |
| HD10 | Neck outside diameter | 10 mm placeholder | Micrometer | Open | |
| HD11 | Neck length | 12 mm placeholder | Calipers | Open | |
| HD12 | Neck axis to mounting plane | 8 mm placeholder from the underside | Critical. Measure with the shell level; compare with the stylus height at the pivot plane | Open | |
| HD13 | Contact-pin circle | 5.5 mm placeholder | Loupe or calipers; shell and arm socket | Open | |
| HD14 | Contact-pin hole | 1.6 mm placeholder | Set from the pins chosen | Open | |
| HD15 | Neck thread for the knurled nut | Not modeled | Thread gauge; measure the nut too | Open | |
| HD17 | Finger-lift width | 6 mm placeholder | Calipers | Open | |
| HD18 | Finger-lift thickness | 2.5 mm placeholder | Calipers; must suit PMMA | Open | |
| HD19 | Neck key or locating feature | Not modeled; the exploded view shows a notched part, item 21a | Inspect and photograph | Open | |
| HD20 | Pin count, type, and spring travel | Four contacts in the arm receptacle, per Hamrick; four wires per AR sheet L-1591; Pat's Audio advertises spring-loaded pins | Inspect the shell and arm socket; find a source for pins | Open | |
| HD21 | Original shell mass, with hardware | Not recorded | Balance; needed to judge the counterweight | Open | |
| HD22 | Lift arc inner radius | 10 mm placeholder | Trace the original lift in plan | Open | |
| HD23 | Lift root position from the front face | 4 mm placeholder | Calipers | Open | |
| HD24 | Lift arc sweep angle | 70° placeholder | Trace the original lift in plan | Open | |
| HD25 | Lift side | +1 design choice: outer side, away from the platter; right wall when facing the front on an XA | Inspect an original shell | Open | |

### Other parts

| ID | What to confirm | Value now | How to check | Status | Result |
| --- | --- | --- | --- | --- | --- |
| SC3 | #3-48 screw head diameter | 4.6 mm placeholder | Calipers on an original screw | Open | |
| SC4 | #3-48 screw head height | 1.6 mm placeholder | Calipers; note head style and drive | Open | |
| SS3 | #4-40 set screw cone length | 0.8 mm placeholder | Calipers | Open | |
| SS4 | #4-40 set screw tip flat | 0.5 mm placeholder | Loupe with a scale | Open | |
| GA2 | Overhang gauge spindle hole | 7.3 mm placeholder | Micrometer on the spindle | Open | |
| GA3 | Overhang gauge needle hole | 1.2 mm placeholder | Test on a spare or a pin first | Open | |
| GA4 | Overhang gauge length | 40 mm placeholder | Design freedom | Open | |
| GA5 | Overhang gauge width | 18 mm placeholder | Design freedom | Open | |
| GA6 | Overhang gauge thickness | 3 mm placeholder | Check the spindle shoulder and arm height | Open | |

## XA mods

Open items from the [XA mods](models/xa/mods/README.md), marked TBC on each page.

| ID | What to confirm | Value now | How to check | Status | Result |
| --- | --- | --- | --- | --- | --- |
| RJ1 | Base wall thickness at the jack position | Not recorded | Calipers | Open | |
| RJ2 | Chosen jack: panel hole, maximum panel, and insulation | See the [RCA jacks page](models/xa/mods/rca-jacks.md#parts) | Datasheet, then check on the part | Open | |
| IE1 | Motor rated current and fuse value | Not recorded | Motor label, then choose the fuse | Open | |
| IE2 | Whether the stock top plate is tied to signal ground | Not stated in any source | Ohmmeter from the arm braid to the plate, before modifying | Open | |
| RW1 | Your arm's color-to-pin map | AR sheet: green is left ground. Modern code: green is right ground | Ohmmeter from each pin to each post | Conflict | |
| VP1 | Jewel cup type, size, and fitting method | Not established | Inspect a converted arm, or ask a rebuilder | Open | |
| VP2 | Who currently offers the pivot service | Vinyl Nirvana's page does not list the XA | Ask directly | Open | |
| WD1 | Original base material on your table | Solid walnut, veneer, or vinyl, by era | Inspect; record the serial | Open | |
| MC1 | Existing capacitor markings and dielectric | Values on manual p. 3; dielectric unknown | Read the part; record motor and serial | Open | |
| MC2 | Replacement capacitor with a suitable AC rating | Not selected | Datasheet, for continuous mains use | Open | |
| TM1 | Master4 hum on the XA | Not stated by Grado | Listen at the inner groove with the motor running | Open | |
| TM2 | Counterweight balances the shell and Master4 | Not tested | Balance with the actual parts, before ordering | Open | |
| DC1 | JnB cover size, fixing, and clearance over the arm | Not published | Ask the maker, or measure one | Open | |
| TB1 | Stock T-bar mass, thickness, spring and bearing positions | Not recorded | Balance and calipers | Open | |
| SK1 | Kit stud length against plinth depth | 2 in listed; one report of other studs too long for a stock plinth | Measure the plinth depth | Open | |
| BP1 | Machined pulley for Haydon or Philips motors | None found; the listed one is Hurst only | Ask suppliers | Open | |
| PB1 | XA main bearing parts and their positions | Parts 996 and 1092 are listed, positions unclear | Inspect during the clean | Open | |
| MG1 | A suitable motor grommet, and whether it helps | No part found, no measurement found | Compare the same test before and after | Open | |
| TD1 | Whether top plate damping helps | Owner reports only | Compare the same test before and after | Open | |

## Sources not yet read

- https://audiokarma.org/forums/threads/ar-xa-overhaul-time.1112265/
- https://audiokarma.org/forums/threads/ar-xa-pivot-bearing-parts.1053357/
- https://audiokarma.org/forums/threads/ar-xa-other-marc-morin-tips-hints-instruction.967048/
- https://www.diyaudio.com/community/threads/acoustic-research-arxb-main-bearing-has-alot-of-grey-grease-in-there-i-thought-it-was-supposed-to-be-thin-oil.409524/latest
- https://www.diyaudio.com/community/threads/ar-xa-w-custom-mods.368650/
- https://datasheets.globalspec.com/ds/Schurter/kd/f2b002c3-9424-4f27-9f5d-cd0383e9044e
- https://www.audiophonics.fr/en/rca-sockets/klei-harmony-classic-rca-plugs-silver-plated-copper-pair-p-14423.html
- https://www.vinylengine.com/library/acoustic-research.shtml
