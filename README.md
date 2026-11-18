# ARTT: the open reference for Acoustic Research turntables

Every AR turntable, from the 1961 XA to the 1980s ETL-1, in one place: how to identify it, factory figures and documents, service, mods, parts and drawings. Every value names its source. Versioned with git, free, non-commercial, open to corrections and contributions.

| XA | XB | AR77XB | The AR Turntable |
| --- | --- | --- | --- |
| ![AR XA under a clear cover](docs/images/models/xa.jpg) | ![XB-pattern table with cueing lever, in a maple plinth](docs/images/models/xb.jpg) | ![AR77XB with its badge at the front left of the top plate](docs/images/models/ar77xb.jpg) | ![The AR Turntable, 1983 brochure photo](docs/images/models/the-ar-turntable.jpg) |
| 1961 to 1979. No cueing lever | From about 1972. Cueing lever and rocker switch | From 1977. AR77XB badge on the top plate; lever and switch with no panel | From late 1983. Arm on a black board |

| The Legend | EB-101 | ES-1 | ETL-1 |
| --- | --- | --- | --- |
| ![The Legend from above](docs/images/models/the-legend.jpg) | ![EB-101 from above](docs/images/models/eb-101.jpg) | No stock photo yet | ![ETL-1 in cherry](docs/images/models/etl-1.jpg) |
| The British name for The AR Turntable | The budget model, square-edged | Solid wood sides, sapphire bearing | The large one, sold without an arm |

Not sure which one you have? Use the [model guide](models/README.md). Photos: Gig Harbor Audio (XA), the repository owner's files (XB, AR77XB), Vinyl Nirvana (ETL-1), AR factory brochures (The AR Turntable, The Legend, EB-101). The XA and XB shown have new covers, and the XB a new plinth and top-plate colour; every arm is the original.

| Start here | |
| --- | --- |
| Does it perform? | [The evidence](docs/evidence/README.md): 0.05 percent speed error, the lowest a testing laboratory had met in a fixed-speed table (Period, *High Fidelity*, 1963); rumble −38 dB unweighted against a −35 dB broadcast standard (Period, *HiFi/Stereo Review*, 1963); 19 dB more gain before acoustic feedback than a direct-drive reference on the same bench, on the 1983 table (Period, *Audio*, 1984). The [weaknesses](docs/evidence/weaker.md) are on the same pages |
| Which model is it? | [Model guide](models/README.md): every model and variant, how to recognise it, dates, and published figures |
| Your model | [XA](models/xa/README.md) · [XB](models/xb/README.md) · [AR77XB](models/ar77xb/README.md) · [The AR Turntable and The Legend](models/the-ar-turntable/README.md) · [EB-101](models/eb-101/README.md) · [ES-1](models/es-1/README.md) · [ETL-1](models/etl-1/README.md). [Status of each](#status-by-model) |
| Upgrades | [XA mods](models/xa/mods/README.md) |
| Small parts explained | [What it is and where it goes](docs/what-goes-where.md) |
| A part in hand, or one you need | [Find your part](parts/README.md#find-your-part): its versions, which tables each fits, the drawing, and what to keep if you make one |
| Buying parts | [Parts and makers](parts/README.md#replacement-parts) |
| Making parts | [Part index](parts/reproduction.md) · [CAD drawings](cad/README.md) |
| Original documents | [Manuals and factory drawings](docs/README.md) |
| Archived articles | [Local copies of community and maker pages](docs/archive/README.md) |
| Open questions | [Things to confirm](TO-CONFIRM.md) |

## Status by model

The owner has an XA, an XB and an AR77XB on the bench. No other model has been inspected or measured for this reference.

| Model | Page | Bench-verified by the owner | Factory documents held | Wanted from owners |
| --- | --- | --- | --- | --- |
| XA | [Yes](models/xa/README.md) | Not yet: on the bench, checks open | Owner's manual, service manual, sheet L-1591, needle force gauge sheet, specification sheet, brochure, 1979 parts and price lists, Villchur's two design papers | Motor label and shaft by serial, capacitor markings, overall size and weight |
| TA | In the [model guide](models/README.md) | No. No table on hand | None | Any photo, label, serial and pulley |
| XB | [Yes](models/xb/README.md) | Not yet: on the bench, checks open | Factory drawings 112 to 119 | Capacitor markings, overall size and weight, a dated advert or price list |
| XB1 | Section of the [XB page](models/xb/README.md) | No. No table on hand | XB1 owner's manual | Underside labels, motor and capacitor markings |
| AR77XB | [Yes](models/ar77xb/README.md) | Not yet: on the bench, checks open | None | Any factory paper naming it, motor and capacitor markings, headshell material |
| The AR Turntable | [Yes](models/the-ar-turntable/README.md) | No. No table on hand | 1983 brochure, Hurst motor schematics 130 and 131 | Photos, motor label, serial, measurements |
| The Legend | Section of [The AR Turntable](models/the-ar-turntable/README.md) | No. No table on hand | British brochure | Photos, motor label, serial, measurements |
| EB-101 | [Yes](models/eb-101/README.md) | No. No table on hand | British brochure, EB101N schematics 148 and 149 | Photos, motor label, serial, measurements |
| ES-1 | [Yes](models/es-1/README.md) | No. No table on hand | None | A stock photo with the original arm, any factory paper |
| ETL-1 | [Yes](models/etl-1/README.md) | No. No table on hand | None | Any factory paper, photos of the speed control |

The [registry](docs/registry.md) collects owners' tables; the [bench sheets](docs/bench-sheets/README.md) list what to measure.

## How to read this reference

Each value carries one label and its source, in parentheses.

- **Factory**: a manufacturer document.
- **Owner report**: a firsthand restoration account or measurement.
- **Maker claim**: a supplier describing its own product.
- **Unconfirmed**: evidence is missing or contradictory.

Every source link opens a copy kept in this repository, so the reference still works when the original site is gone. The copy names its original address, and the [archive index](docs/archive/README.md) lists them all.

A measurement from one table stays tied to that table. Do not carry a value across models. Nothing is confirmed for the AR77XB unless its page gives a source. None of the mods or CAD parts has been built or fit-tested. Advice with no source is our assessment.

Last reviewed: 2026-11-18. To add or correct something, see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Text, models, and drawings: [CC BY-SA 4.0](LICENSE). Build script: [MIT](cad/tools/LICENSE). Scans under `docs/` are third-party material and keep their own rights. Not affiliated with Acoustic Research or Grado.
