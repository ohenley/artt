# Adding information

[Home](README.md) · [Things to confirm](TO-CONFIRM.md)

Edit the model page, and give each value its label and source. Log anything still unmeasured in [TO-CONFIRM.md](TO-CONFIRM.md).

```text
Part/location:
Model, serial, and revision:
Value, with units:
Source: document + page/item, or your own measurement + photo
Label: Factory / Owner report / Maker claim / Unconfirmed
```

- Keep a factory value separate from a measurement of a worn part.
- Keep conflicting sources side by side. Do not average them.
- Say whether a part is original, a replacement, or a custom modification.
- Put scans under `docs/originals/`, and add their source URL, date, and SHA-256 to `docs/manifest.tsv`.
- A CAD change needs a [rebuild](cad/README.md#rebuilding).
- One addition or correction per commit.

Contributions are shared under [CC BY-SA 4.0](LICENSE); build-script changes under [MIT](cad/tools/LICENSE).
