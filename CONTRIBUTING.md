# Adding information

[Home](README.md) · [Things to confirm](TO-CONFIRM.md) · [Part index](parts/reproduction.md)

Edit the model page first. Suppliers go in [parts](parts/README.md), originals in [docs](docs/README.md), and open measurements in [TO-CONFIRM.md](TO-CONFIRM.md). A part gets its own record, like the [XA counterweight](parts/xa-counterweight.md), once it has usable dimensions.

## A useful entry

```text
Part/location:
Model, serial, and revision:
Specification or observation, with units:
Evidence: factory document + page/item, or firsthand measurement + photo
Label: Factory / Owner report / Maker claim / Unconfirmed
Date checked:
```

- Screw: diameter, thread pitch, length convention, head style, quantity, location.
- Capacitor: circuit position, capacitance, AC/DC rating, markings.
- Cover: internal clearance, external dimensions, lip and hinge geometry.

Say whether a part is an original specification, a replacement, or a custom modification. Keep conflicting evidence with its scope. Do not average dimensions or repair a source's serial-number gap.

## Drawings and original files

- A usable drawing has dimensions, units, datums, material, critical fits and finish, model and revision, and the evidence for each value.
- Keep a factory value separate from a measurement of an aged part. A worn-part measurement is not a factory tolerance.
- Record a fit result once a replacement has been made. For third-party CAD, record the creator, license, version, material, intended model, and the table used for the fit check.
- Prefer an editable CAD source with a STEP file and a dimensioned PDF. The repository's own models are in [cad](cad/README.md).
- Put originals under `docs/originals/` with readable filenames. Add the source URL, retrieval date, SHA-256, and any changes to `docs/manifest.tsv`.
- Keep a clean original separate from OCR, crops, and edits. Check numbers visually before accepting OCR.

## Git

Commit one addition or correction at a time, for example `docs(xb): identify suspension adjustment thread`. Keep temporary OCR exports and full magazine issues outside the repository. Only a CAD change needs the [build script](cad/README.md#rebuilding).

## License

Contributions are shared under [CC BY-SA 4.0](LICENSE), and build-script changes under the [MIT License](cad/tools/LICENSE). Add third-party files only under their own terms.
