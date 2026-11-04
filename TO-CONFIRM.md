# Things to confirm

[Home](README.md) · [How to add a measurement](CONTRIBUTING.md) · [Part index](parts/reproduction.md)

Claims still waiting for a measurement, an inspection, or a readable source. Started 2026-11-04.

**Status:** **Open** = not checked yet. **Conflict** = sources disagree. **Blocked** = the source could not be opened. **Confirmed** = checked and matches. **Differs** = checked and does not match.

When you check something, update its status and write the result, the model and serial, and the date in the Result column. Then update the page that uses the value. A measurement from one table stays tied to that table, and a differing result sits beside the earlier value instead of replacing it.

## Measure or inspect on a table

### Counterweight and rest

Counterweights differ by model. Vinyl Nirvana lists brass for the XA, brass or stainless steel for the XB, and aluminum for the XB77, so record which model yours came from.

| ID | What to confirm | Value now, and source | How to check | Status | Result |
| --- | --- | --- | --- | --- | --- |
| CW1 | Mass with set screw | 98.8 g; [owner report](parts/xa-counterweight.md) | Balance, with the screw fitted | Open | |
| CW2 | Mass without set screw | Not recorded | Balance, with the screw removed | Open | |
| CW3 | Outside diameter | 28 mm; owner report | Calipers, at several points | Open | |
| CW4 | Length along bore | 22 mm; owner report | Calipers | Open | |
| CW5 | Bore diameter | 9.5 mm; owner report | Calipers or pin gauge; note wear | Open | |
| CW6 | Bore through or blind, and centered or offset | Not recorded | Inspect and measure the wall thickness around the bore | Open | |
| CW7 | Material | Brass; owner report | Inspect; compare calculated density using CW2–CW6 | Open | |
| CW8 | Set screw thread, length, and tip | Not recorded; do not assume the #4-40 in HS3 | Thread gauge, calipers | Open | |
| CW9 | Locking-hole position | Not recorded | Calipers, from one end of the weight | Open | |
| CW10 | Tonearm rest height | 39 mm, bottom of yoke to top of top plate; owner report | Calipers, installed | Open | |

### Headshell and screws

| ID | What to confirm | Value now, and source | How to check | Status | Result |
| --- | --- | --- | --- | --- | --- |
| HS1 | Original shell thread | #3-48; [community drawing](docs/headshells.md#mounting-screws-and-spacers) | Thread gauge or a known #3-48 screw | Open | |
| HS2 | Screw lengths under the head | 0.183, 0.356, 0.462, 0.612 in; same drawing | Calipers, on original screws | Open | |
| HS3 | Where the #4-40 brass set screw goes | #4-40 × 0.125 in; same drawing, location not given | Find it on a table and gauge the thread | Open | |
| HS4 | Shell body material | "A light plastic"; [AR sheet L-1591](docs/originals/ar-cartridge-mount.jpg) | Inspect; record model and serial | Open | |
| HS5 | AR77XB shell material | Metal and plastic; the [Vinyl Nirvana page](models/ar77xb/README.md#mechanical) says both | Inspect an identified AR77XB | Conflict | |

### Platter, bearings, and suspension

| ID | What to confirm | Value now, and source | How to check | Status | Result |
| --- | --- | --- | --- | --- | --- |
| PL1 | Platter mass | 3.3 lb in Villchur, Part 2, p. 36, and the 1969 directory; 3.9 lb (1.8 kg) on Vinyl Nirvana | Balance; weigh inner and outer platter separately | Conflict | |
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
| EL1 | Motor and shaft by serial | [Serial table](models/xa/README.md#motor-identification); manual | Record serial, motor label, and shaft diameter | Open | |
| EL2 | Serial gap XA175235–XA176235 | The manual leaves this range unassigned; possibly a misprint | Report the motor on any table in that range | Conflict | |
| EL3 | XA 120 V capacitors | C1 0.1 µF, C2 0.022 µF, both 600 VDC; manual, p. 3 | Read the markings on an unmodified table | Open | |
| EL4 | XB capacitor ratings | Part numbers only; [drawing 119](models/xb/README.md#factory-component-identifiers) | Read the markings on items 44 and 46 | Open | |
| EL5 | AR77XB capacitors and motor | Not recorded | Read the markings and motor label | Open | |
| DM1 | XA size with cover | 16¾ × 12¾ × 5¼ in; [1969 directory](models/xa/README.md#dimensions-and-arm-geometry) | Tape or calipers | Open | |
| DM2 | XA complete weight | 13½ lb; same directory | Scale; note whether cover and mat are included | Open | |
| DM3 | XB and AR77XB overall size and weight | Not recorded | Tape or calipers, scale | Open | |
| DM4 | Hinge position on cover | 2.20 in and 60.6 mm on [drawing 114](models/xb/README.md#cover-dimensions-and-clearance), which do not convert | Measure a hinged XB cover | Conflict | |

## CAD dimensions needed

These are the placeholders in the [CAD models](cad/README.md). Each value is in the model's parameter table, and the drawing shows it in red until it is replaced. CW6, CW8, and CW9 above are placeholders too.

### Grado cartridge and top mounting

The target cartridge is the **Grado Master4**. [Grado's page](https://gradolabs.com/products/master4) gives its mass, tracking force, and compliance, but no dimensions or screw details, and says the housing was reshaped. The closest published figures are for the older Opus3: [Addicted to Audio](https://addictedtoaudio.co.nz/blogs/reviews/grado-timbre-series-opus3-cartridge) says its bolts "screw in from the top" and gives its body as 20.1 mm wide, 16.3 mm tall, 25.3 mm deep, and 29.6 mm with pins. [Positive Feedback](https://positive-feedback.com/reviews/hardware-reviews/grado-timbre-series-opus3-phono-cartridge/) describes threaded inserts in the wood body. Neither gives the thread. Search excerpts report 3-48, M2.5, M2.6, about 2 mm, and a nonstandard pitch for various Grado models; see SR13. None of this has been checked on a Master4 here.

| ID | What to confirm | Value now | How to check | Status | Result |
| --- | --- | --- | --- | --- | --- |
| GR1 | Slot width, from the Grado screw | 2.8 mm placeholder | Gauge the supplied screw, then add clearance | Open | |
| GR2 | Head recess width | 5.0 mm placeholder | Calipers on the screw head, plus clearance | Open | |
| GR3 | Head recess depth | 1.0 mm placeholder | Set with GR7 and HD4 so the screw does not bottom out | Open | |
| GR4 | Slot travel | 6.0 mm placeholder | Check against GR8 and the arm's own adjustment | Open | |
| GR5 | Slot position on the body | −1.5 mm placeholder | Work out from GR8 and HD1 | Open | |
| GR6 | Pocket width | 21.0 mm placeholder, from the Opus3's 20.1 mm body | Calipers on your cartridge body, plus clearance | Open | |
| GR7 | Master4 screw length and usable thread depth | Not recorded | Calipers; check depth gently, since wood threads can strip | Open | |
| GR8 | Mounting holes to stylus tip | Not recorded; AR's factory setting assumed ⅜ in (Villchur 1962, p. 69) | Calipers or a loupe with a scale | Open | |
| GR9 | Master4 mass, with and without screws | 9.6 g on Grado's page; 10 g on [one retailer's](https://soundapproach.com/grado-master4-timbre-series-turntable-phono-cartridge.html) | Balance | Conflict | |
| GR10 | Master4 body size, and top to stylus tip | Unpublished. Opus3 only: 20.1 × 16.3 × 25.3 mm, 29.6 mm with pins, 18.3 mm top to stylus | Calipers; sets the pocket and the record clearance | Open | |
| GR11 | Master4 mounting-hole spacing | ½ in assumed; not stated on Grado's page | Calipers, between hole centers | Open | |
| GR12 | Arm effective mass with the finished shell | Not established | Needed with the Master4's 20 µm/mN compliance to estimate resonance | Open | |

### Headshell body and connector

Measure an original shell and its retaining nut, and record the model and serial. Photos of the neck end and the arm socket would also help.

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
| HD12 | Neck axis to mounting plane | 8 mm placeholder from the underside | Critical. Measure with the shell level, and compare with the stylus height at the pivot plane | Open | |
| HD13 | Contact-pin circle | 5.5 mm placeholder | Loupe or calipers; shell and arm socket | Open | |
| HD14 | Contact-pin hole | 1.6 mm placeholder | Set from the pins chosen | Open | |
| HD15 | Neck thread for the knurled nut | Not modeled | Thread gauge; measure the nut too | Open | |
| HD16 | Finger-lift length | 12 mm placeholder | Calipers | Open | |
| HD17 | Finger-lift width | 6 mm placeholder | Calipers | Open | |
| HD18 | Finger-lift thickness | 2.5 mm placeholder | Calipers; must suit PMMA | Open | |
| HD19 | Neck key or locating feature | Not modeled; the exploded view shows a notched part, item 21a | Inspect and photograph | Open | |
| HD20 | Pin count, type, and spring travel | Four contacts in the arm receptacle, per Hamrick; four wires per AR sheet L-1591; Pat's Audio advertises spring-loaded pins on its shell | Inspect the shell and arm socket; find a source for pins | Open | |
| HD21 | Original shell mass, with hardware | Not recorded | Balance; needed to judge the counterweight | Open | |

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

Open items from the [XA mods](models/xa/mods/README.md). Each page also marks these "to confirm on the part".

| ID | What to confirm | Value now | How to check | Status | Result |
| --- | --- | --- | --- | --- | --- |
| RJ1 | Base wall thickness at the jack position | Not recorded | Calipers | Open | |
| RJ2 | Chosen jack: panel hole, maximum panel, and insulation | See the [RCA jacks page](models/xa/mods/rca-jacks.md#parts) | Datasheet, then check on the part | Open | |
| IE1 | Motor rated current and fuse value | Not recorded | Motor label, then choose the fuse | Open | |
| IE2 | Whether the stock top plate is tied to signal ground | Not stated in any source read | Ohmmeter from the arm braid to the plate, before modifying | Open | |
| RW1 | Your arm's color-to-pin map | AR sheet: green is left ground. Modern code: green is right ground | Ohmmeter from each pin to each post | Conflict | |
| VP1 | Jewel cup type, size, and fitting method | Not established | Inspect a converted arm, or ask a rebuilder | Open | |
| VP2 | Who currently offers the pivot service | Unconfirmed. Vinyl Nirvana's page does not list the XA | Ask directly | Open | |
| WD1 | Original base material on your table | Solid walnut, veneer, or vinyl, by era | Inspect; record the serial | Open | |
| MC1 | Existing capacitor markings and dielectric | Values on manual p. 3; dielectric unknown | Read the part; record motor and serial | Open | |
| MC2 | Replacement capacitor with a suitable AC rating | Not selected | Datasheet, for continuous mains use | Open | |
| TM1 | Master4 hum on the XA | Not stated by Grado | Listen at the inner groove with the motor running | Open | |
| TM2 | Counterweight balances the shell and Master4 | Not tested | Balance with the actual parts, before ordering | Open | |
| DC1 | JnB cover size, fixing, and clearance over the arm | Not published | Ask the maker, or measure one | Open | |

## Recheck a source

| ID | What to confirm | Why it is unconfirmed | Status | Result |
| --- | --- | --- | --- | --- |
| SR1 | [Reddit post](https://www.reddit.com/r/turntables/comments/1t5vqzh/ar_xa_tone_arm_counter_weight_tone_arm_rest/): the author, the CW and rest values, and the owner's own XA as the source | Blocked on 2026-11-04; values were only checked for consistency within this repo | Blocked | |
| SR2 | [diyAudio thread](https://www.diyaudio.com/community/threads/acoustic-research-ar77xb-search-for-new-headshell-bolts.407382/): 14 shells, whether they are "original", and the citation of posts 2 and 4 | Blocked on 2026-11-04; a search excerpt supports the 14 shells and #3-48 but not the word "original" | Blocked | |
| SR3 | Same thread: another poster reportedly says 4-40, then M2.5 | Seen only in a search excerpt, so not recorded on the model pages. Read it, then record the conflict with its scope | Blocked | |
| SR4 | [eBay headshell listing](https://www.ebay.com/itm/144937941911) by redcedarprints | HTTP 403; a search found no trace of the seller | Blocked | |
| SR5 | [Audiokarma AR77XB thread](https://audiokarma.org/forums/threads/ar77xb-questions.860919/) | HTTP 403; contents not read | Blocked | |
| SR6 | [Vinyl Engine AR77-XB entry](https://www.vinylengine.com/library/acoustic-research/ar77-xb.shtml) | HTTP 403; no manual contents verified | Blocked | |
| SR7 | [Radiomuseum AR77-XB entry](https://radiomuseum.org/r/acoustic_ar77_xb.html): about 16.4 × 5.5 × 15.6 in | Seen only in a search summary, so not used on the model page | Open | |
| SR8 | [XB1 manual](docs/originals/xb1-owners.pdf): full extraction | Only the cover has been inspected; the scan has no text layer | Open | |
| SR9 | [XA owner's manual scans](https://vinylnirvana.com/ar-turntable-resources/ar-turntable-history/ar-xa-manual): full extraction | Located, not transcribed | Open | |
| SR10 | [1969 service manual scans](https://vinylnirvana.com/ar-turntable-resources/ar-turntable-history/1969-ar-xa-service-manual): same revision as the local PDF? | Not compared | Open | |
| SR11 | [XA technical specifications](https://vinylnirvana.com/ar-turntable-resources/ar-turntable-history/1969-ar-xa-technical-specifications): transcribe the figures | Located, not transcribed | Open | |
| SR12 | AR's 1990 public-domain release of the drawings | Stated by [Audio Appraisal](https://audioappraisal.com/acoustic-research-drawings-archive/); not independently established | Open | |
| SR13 | Grado wood-body screw thread: [Vinyl Asylum](https://www.audioasylum.com/messages/vinyl/866913/psssst-hey-buddy-need-grado-cartridge-screws) (3-48), [Audiogon](https://forum.audiogon.com/discussions/grado-wood-bodies) (M2.6 or about 2 mm), and [a Reference Master thread](https://www.tapatalk.com/groups/daveyw/grado-reference-master-cartridge-fixing-t184.html) (2.5 mm) | HTTP 403 on 2026-11-04; seen only in search excerpts, none about the Master4, so GR1 stays a placeholder | Blocked | |
| SR14 | Grado Master4 body wood | American Osage on [Grado's page](https://gradolabs.com/products/master4); Australian Jarrah on [one retailer's](https://soundapproach.com/grado-master4-timbre-series-turntable-phono-cartridge.html). Grado's own page is the stronger source, and this affects mass more than fit | Conflict | |
| SR15 | AudioKarma threads on XA grounding and suspension | HTTP 403 on 2026-11-04, so not used for any value. Examples: [grounding problem](https://audiokarma.org/forums/threads/ar-xa-grounding-problem.787681/), [suspension spring upgrade](https://audiokarma.org/forums/threads/ar-xa-suspension-spring-upgrade.1102797/) | Blocked | |
| SR16 | Date of Galo's "A Belt-Drive Turntable Upgrade" | [The PDF](https://audioXpress.com/assets/upload/files/galo2931.pdf) footers say 2008, the last says June 2005, and a mirror labels it July 2008 | Conflict | |
