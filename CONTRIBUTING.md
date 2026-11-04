# Adding information

[Home](README.md)

Edit the relevant model page first. Shared suppliers belong in [parts](parts/README.md); originals and their provenance belong in [docs](docs/README.md). Add a new page only when an existing one becomes hard to read.

For a part intended for reproduction, update the [part index](parts/reproduction.md). Once usable dimensions or a drawing exist, give that part a short record beside the index, as with the [XA counterweight](parts/xa-counterweight.md). Keep unknown parts as index rows until there is evidence to record.

Log anything that still needs a measurement or a readable source in [the confirmation list](TO-CONFIRM.md), and update its status when it is checked.

## A useful entry

Keep each addition short and attach the evidence:

```text
Part/location:
Model, serial, and revision:
Specification or observation, with units:
Evidence: factory document + page/item, or firsthand measurement + photo
Status: factory / owner report / maker claim / unconfirmed
Date checked:
```

For a measured screw, include diameter, thread pitch, length convention, head style, quantity, and location. For a capacitor, include circuit position, capacitance, AC/DC rating, and markings. For a cover, distinguish internal clearance from external dimensions and record lip/hinge geometry. A measurement from one table stays tied to that table until broader applicability is established.

For a manufacturing drawing, also record material, units, datums, critical tolerances and fits, surface finish where it matters, and how the dimensions were established. Do not turn a worn-part measurement into an original factory tolerance. Keep a proposed replacement distinguishable from a made and fit-tested part. Prefer an editable CAD source plus a neutral STEP file and a dimensioned PDF when such files become available.

Keep **original specification**, **replacement part**, and **custom modification** explicit in the text. Preserve conflicting evidence with its scope; do not silently average dimensions or repair a source's serial-number gap.

## License

By contributing text, measurements, or models, you agree to share them under the repository's [CC BY-SA 4.0 license](LICENSE); changes to the build script go under its [MIT License](cad/tools/LICENSE). Only add third-party files under their own terms, with their source recorded as described below.

## Original files

Use readable filenames under `docs/originals/`. Add the source URL, retrieval date, SHA-256, and any changes to `docs/manifest.tsv`. Keep a clean original separate from OCR, crops, or edited drawings. Use short Markdown summaries with precise page/item references; check numbers visually before accepting OCR.

No CAD/STL file is treated as fit-tested merely because it opens or prints. Record the creator, license, version, material, intended model, and the table used for the fit check. Our own models live in [cad](cad/README.md), where each dimension carries its evidence and a placeholder is shown in red until it is measured.

## Git

Commit one understandable addition or correction at a time, for example `docs(xb): identify suspension adjustment thread`. Put large temporary OCR exports and full magazine issues outside the repository. This reference needs no website generator or build step; GitHub and ordinary Markdown viewers can navigate it directly. Only changing a CAD model needs the [build script](cad/README.md#rebuilding).
