# Bench method: measuring an AR so that it sits beside a lab figure

[The evidence](README.md) · [Factory](factory.md) · [Period tests](period-tests.md) · [Owner tests](owner-tests.md) · [Against the reference tables](compared.md) · [Where the AR is weaker](weaker.md)

The AR column in the [table of current lab results](compared.md#c-one-current-method-the-hi-fi-news-lab-reports) is empty because no AR has been measured by that method. This page says how to measure one at home so that the result can be written in that column, and how to repeat the three older tests that anyone can run. Each requirement is tied to the document that defines it. Where the held documents leave a detail open, that is said, and the detail goes in the report rather than being guessed.

## The method of the current lab reports

Every held *Hi-Fi News* lab report prints the same captions and the same result rows, which together describe the method (Period, for example the [Linn Majik LP12 report](../archive/hifinews/linn-majik-lp12-krane-turntable-package-lab-report.md)):

| Row in the lab report | What it says of the method |
| --- | --- |
| Wow and flutter graph | "Wow and flutter re. 3150Hz tone at 5cm/sec (plotted ±150Hz, 5Hz per minor division)" |
| Peak Wow/Flutter | "(Peak wtd)": wow and flutter reported separately, each as a peak-weighted figure |
| Turntable speed error at 33.33rpm | The measured speed and its error in percent, from the same tone |
| Rumble (silent groove, DIN B wtd) | Through the stylus in an unmodulated groove, DIN B weighting, relative to 1 kHz at 5 cm/sec |
| Rumble (through bearing, DIN B wtd) | Directly through the spindle, same weighting and reference |
| Hum & Noise (unwtd, rel. to 5cm/sec) | Unweighted residual noise, same reference |
| Time to audible stabilisation | Seconds from start until the pitch is steady |

What the held pages do not state: which standard defines the "peak weighted" wow and flutter figure, what coupler is used for the through-bearing rumble, which test record carries the 3,150 Hz tone, and the software. A home result must name all four, so that a reader can judge how close it sits to the lab's column. Until the lab's own description of those items is held, a home result goes in table C with that note beside it, not as an equal.

## What to do

1. **Test record.** One with a 3,150 Hz tone recorded at 5 cm/sec, and an unmodulated silent groove. The 1983 *Audio* review of the Linn used the B & K 2010 record for its 3,150 Hz tone (Period, [held](../archive/gamma-electronics/audio-1983-11-linn-lp12.md)); the filmed XA test used the CBS STR-100 for its 1 kHz band (Owner report, [held](../archive/youtube/zillch-2018-ar-xa-tested.md)). Record which one.
2. **Chain.** Cartridge, arm as fitted, the table's own phono lead, a phono preamplifier, and an analogue-to-digital converter at 96 kHz or more. Record which cartridge, its tracking force, and the preamplifier, because the through-groove rumble includes the arm and cartridge resonance: Long's 1983 Linn figure was dominated by it (Period, same review).
3. **Speed error.** Record the 3,150 Hz tone for at least one minute, with the stylus in the groove so that its drag is included, as Villchur's load test and the filmed test both do. Report the average frequency and the error as a percentage of 3,150 Hz. State the mains frequency at the time if it can be read, since a synchronous motor follows it (Factory, [AR spec sheet](../archive/vinyl-nirvana/ar-turntable-history/1969-ar-xa-technical-specifications.md)).
4. **Wow and flutter.** From the same recording, report peak wow and peak flutter separately, with the weighting the software applies named, and keep the spectrum plot to ±150 Hz around the tone as the lab does, so that a reader can see the sidebands the lab describes in words.
5. **Rumble through the groove.** Record the silent groove at the same gain as the 3,150 Hz tone. Report the DIN B weighted level relative to 1 kHz at 5 cm/sec. The record's own rumble is in this figure; that is why the lab also measures through the bearing.
6. **Rumble through the bearing.** A coupler on the spindle carries the bearing's motion to the cartridge without a record. The Boston Audio Society used the Thorens Rumpelmesskoppler on the 1983 AR (Period, [*Audio*, July 1984](../archive/gamma-electronics/audio-1984-07-ar-turntable.md)). Name the coupler. Without one, leave this cell empty rather than fill it with a groove figure.
7. **Report.** Add the row to the [owner tests](owner-tests.md#adding-a-result) page in its format, with the serial number, what is original and what is replaced, and the date.

The repository owner has an XA, an XB and an AR77XB. The first result from any of them fills the empty column; a result from each shows whether the three differ. Owners of the reference tables can be asked, in the forum threads where the AR is discussed, to run the same record through the same software, and each answer is added as an Owner report with its serial number.

## The load test with coins

Villchur's test, repeatable with no instrument but a stroboscope card (Factory, [Villchur 1962, Part 2](../originals/villchur-1962-part-2.pdf), p. 36):

1. Set the stylus force to 2½ g and play the outer grooves of a record under a strobe card with 216 lines for 33⅓ rpm.
2. Place a U.S. penny on the cartridge shell: 3 g added. Count the lines drifting past a fixed point for one minute. 21 lines a minute is 0.3 percent, the NAB limit.
3. Replace the penny with a nickel: 5 g added. Count again.
4. Report both counts. The AR spec sheet guarantees the 5 g case inside 21 lines a minute.

Villchur's five tables are in [comparison A](compared.md#a-speed-under-added-load-one-method-one-tester). A result here can be set beside them, since the method is the same.

## The feedback test with a speaker

Two versions exist in the held sources, and both can be repeated.

- **Gain before howl**, the Boston Audio Society's version: the table 1 m from a full-range speaker, the preamplifier's volume raised until a low-frequency howl starts; then the same with a second table in the same spot, and the difference in gain noted (Period, *Audio*, July 1984). The result is a difference in dB between two tables on one bench, which is why it can be tabled: [comparison B](compared.md#b-gain-before-acoustic-feedback-one-lab-one-bench).
- **On top of the speaker**, Milder's 1963 version, repeated on film in 2018: the table placed directly on a playing wide-range speaker at full volume, listening for howl and for distortion short of howl (Period, [AR brochure, p. 9](../archive/vinyl-nirvana/images/ar-brochure-2.jpg); Owner report, [filmed test](../archive/youtube/zillch-2018-ar-xa-tested.md) at 32:07). The result is pass or fail, so it is a list entry, not a table row.

## The hammer test

The 1963 reports struck the motorboard with a hammer during play and listened for a thump and watched for a groove jump, at 1 g tracking force (Period, [*HiFi/Stereo Review*, March 1963](../originals/hifi-stereo-review-1963-03-hirsch-ar-pp33-34.pdf); [*High Fidelity*, March 1963](../originals/high-fidelity-1963-03-ar-report-pp59-60.pdf)). The filmed test repeats it at 28:15. It demonstrates the suspension; it produces no number, and it can damage a stylus on a table that fails it.

## Older methods named in the sources, for reading old figures

| Method | Where it is defined for this reference | What it means for a figure |
| --- | --- | --- |
| NAB, March 1964 | AR spec sheet; XB1 manual p. 2 | Rumble at least 35 dB below 1 cm/sec at 100 cps, meter ballistics and playback equalisation as specified; wow and flutter 0.1 percent combined; speed ±0.3 percent |
| NAB as used by United States Testing Company in 1963 | [*High Fidelity*, May 1963, p. 51](../originals/high-fidelity-1963-05-rumble-method-p51.pdf) | Unweighted rumble against a 100 cps tone at 1.4 cm/sec peak; the magazine's earlier weighted figures ran 10 to 15 dB better for the same table |
| NARTB | Hirsch, 1963 | The −35 dB broadcast standard he set his −38 and −40 dB readings against |
| DIN 45507 and DIN 45539B | [1983 brochure](../archive/vinyl-nirvana/ar-turntable-history/ar-the-turntable-brochure.md); *Audio*, July 1984 | Weighted wow and flutter, and B-weighted rumble, as used for the second family and for the Linn in 1983 |
| DIN B, re 1 kHz at 5 cm/sec; peak-weighted wow and flutter | *Hi-Fi News* lab reports | The current method, above |
| AR's own weighted indices | Villchur 1962, Part 2, p. 38; AR spec sheet | DataService Corp. FM-3 meter in production testing; never published, because no standard existed to compare them with |

A figure from one row cannot be placed beside a figure from another. That is the whole reason for this page.
