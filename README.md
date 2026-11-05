# Acoustic Research turntable restoration

A sourced workshop reference for the **XA, XB, and AR77XB**.

| Model | Mechanical | Electrical |
| --- | --- | --- |
| [XA](models/xa/README.md) | [Dimensions, motors, bearings](models/xa/README.md#mechanical) | [Capacitors and wiring](models/xa/README.md#electrical) |
| [XB](models/xb/README.md) | [Factory hardware and cover](models/xb/README.md#mechanical) | [Factory parts and wiring changes](models/xb/README.md#electrical) |
| [AR77XB](models/ar77xb/README.md) | [Identification](models/ar77xb/README.md#mechanical) | [Open questions](models/ar77xb/README.md#electrical) |

- [What it is and where it goes](docs/what-goes-where.md): screws, the overhang gauge, definitions
- [XA mods](models/xa/mods/README.md)
- [Parts and makers](parts/README.md)
- [Part index for reproduction](parts/reproduction.md)
- [CAD models and drawings](cad/README.md)
- [Original documents](docs/README.md) and [Villchur's design papers](docs/design-notes.md)
- [Things to confirm](TO-CONFIRM.md) and [sources to read](docs/sources-to-read.md)
- [Adding information](CONTRIBUTING.md)

## How to read this reference

Each value carries one evidence label and its source, in parentheses.

- **Factory**: a manufacturer document.
- **Owner report**: a firsthand restoration account or measurement.
- **Maker claim**: a supplier describing its own product.
- **Unconfirmed**: evidence is missing or contradictory.

A label describes the evidence, not whether a part fits your table. A measurement from one table stays tied to that table. Do not carry a value across models. Nothing is confirmed for the AR77XB unless its page gives a source. None of the mods or CAD parts has been built or fit-tested. Advice with no source is our assessment.

Before comparing specifications, record the model badge, serial number, motor label, mains voltage and frequency, and existing modifications.

Last reviewed: 2026-11-04.

## Where things live

```text
models/   One page per model, plus the XA mods
parts/    Part index, measurement records, suppliers
cad/      OpenSCAD models, drawings, STEP/STL/DXF exports
docs/     Source index, notes, original scans
```

## License

Everything written for this repository, including the Markdown pages, OpenSCAD models, drawings, and exports, is licensed under [CC BY-SA 4.0](LICENSE). You may use, change, manufacture, and sell from it. Credit "AR turntable restoration reference contributors" and share your changes under the same license. The [build script](cad/tools/) is under the [MIT License](cad/tools/LICENSE).

Scans under `docs/originals/` and the combined drawing PDF are third-party material and keep their own rights. Product names and brands belong to their owners. Nothing here is affiliated with Acoustic Research or Grado.
