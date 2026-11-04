# Acoustic Research turntable restoration

A small, sourced workshop reference for the **XA, XB, and AR77XB**. Start with your model, then follow links to the original evidence or a parts maker.

| Model | Mechanical | Electrical |
| --- | --- | --- |
| [XA](models/xa/README.md) | [Dimensions, motor variants, bearings, screws](models/xa/README.md#mechanical) | [Capacitors and wiring](models/xa/README.md#electrical) |
| [XB](models/xb/README.md) | [Factory hardware and cover details](models/xb/README.md#mechanical) | [Factory parts and wiring changes](models/xb/README.md#electrical) |
| [AR77XB](models/ar77xb/README.md) | [Identification and fit questions](models/ar77xb/README.md#mechanical) | [What still needs a model-specific source](models/ar77xb/README.md#electrical) |

- [**What it is and where it goes:** screws, the overhang gauge, and plain definitions](docs/what-goes-where.md)
- [XA mods: upgrades, parts, and gotchas](models/xa/mods/README.md)
- [Parts, makers, and community](parts/README.md)
- [Part-by-part drawings and reproduction worklist](parts/reproduction.md)
- [CAD models, machinist drawings, and STEP files](cad/README.md)
- [Original documents and source index](docs/README.md)
- [Headshell drawings and mounting hardware](docs/headshells.md)
- [Villchur's design papers, in plain language](docs/design-notes.md)
- [Things to confirm, with status](TO-CONFIRM.md)
- [How to add a correction or measurement](CONTRIBUTING.md)

## How to read this reference

**Factory** means a manufacturer document was inspected. **Owner report** means a firsthand restoration account. **Maker claim** means a supplier describes its own replacement. **Unconfirmed** means evidence is missing or contradictory. These labels describe the evidence, not a guarantee that a part fits your particular table.

Record the model badge, serial number, motor label, mains voltage/frequency, and existing modifications before comparing specifications. A later replacement motor or headshell can change what fits.

## Where things live

```text
models/       One readable page per model: mechanical, electrical, open questions
parts/        Part drawing index, measurement records, suppliers, and community links
cad/          OpenSCAD models, with drawings and STEP/STL/DXF exports built from them
docs/         Source index, short Markdown notes, and original scans
```

This first pass is strongest on XA service information and XB factory drawings. AR77XB needs more primary documentation. Unknown dimensions and component ratings are left explicit so they are easy to fill in later.

Research date: **2026-11-04**. Documents are stored locally where retrieval succeeded; other entries link to the host. Supplier links record what was found on this date, without promising stock or quoting prices.

## License

This is a community reference. Everything written for this repository, including the Markdown pages, OpenSCAD models, and drawings and exports built from them, is licensed under [CC BY-SA 4.0](LICENSE). You may use, change, manufacture, and sell from it. Credit "AR turntable restoration reference contributors" and share your changes under the same license. The [build script](cad/tools/) is under the [MIT License](cad/tools/LICENSE).

This does not cover third-party material. Scans under `docs/originals/` and the combined drawing PDF keep their own rights, as described in the [document index](docs/README.md#preservation). Product names and brands belong to their owners. Nothing here is affiliated with Acoustic Research or Grado.
