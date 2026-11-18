# Adding information

[Home](README.md) · [Things to confirm](TO-CONFIRM.md) · [Owner registry](docs/registry.md) · [Other people's material](README.md#other-peoples-material)

You do not need to know git to add something. Pick the path that suits you. Whichever you use, send the same few lines:

```text
Part/location:
Model, serial, and revision:
Value, with units:
Source: document + page/item, or your own measurement + photo
Label: Factory / Owner report / Maker claim / Unconfirmed
```

## Three ways to send it

### 1. No GitHub account

Post it in the forum thread for this reference, with a photo if you have one. The owner adds it to the page and credits you by the name you post under. Forum thread: the owner will put its address here.

### 2. Editing in the browser

You need a free GitHub account. Nothing is installed on your computer.

1. Open the page you want to change on github.com and click the pencil icon at the top right of the file. GitHub makes your own copy of the repository, called a fork, the first time you do this.
2. Make the change in the editor. Keep the label and the source beside each value, as the rest of the page does.
3. Click **Commit changes**. In the box, say in plain words what you added, for example "Add XB motor label from serial 123456". GitHub saves it on a new branch of your copy.
4. GitHub then shows **Open pull request**. A pull request is a request to the owner to copy your change into the main reference. Click it, fill in the checklist that appears, and click **Create pull request**.
5. The owner reviews it. If something needs changing, the owner says so in the pull request, and you edit the same file again with the pencil icon: the pull request updates itself. When it is accepted, the change is merged and your name stays in the history.

You can also open an issue instead of editing: on the repository's **Issues** tab, click **New issue** and pick a form: report my table, report a measurement, correct something, or suggest a page to archive.

### 3. A normal fork

Fork, branch, commit, and open a pull request as usual. The rules below apply, and the pull request template carries the checklist.

## Rules

Edit the model page, and give each value its label and source. Log anything still unmeasured in [TO-CONFIRM.md](TO-CONFIRM.md).

- Keep a factory value separate from a measurement of a worn part.
- Keep conflicting sources side by side. Do not average them.
- Say whether a part is original, a replacement, or a custom modification.
- Write the fact itself on the page. Do not send the reader to a website for it.
- Cite the copy kept in this repository, not the live address. Save a web page under `docs/archive/` first, list it in the [archive index](docs/archive/README.md), and add it to `docs/manifest.tsv`.
- Put scans under `docs/originals/`, and add their source URL, date, and SHA-256 to `docs/manifest.tsv`.
- A CAD change needs a [rebuild](cad/README.md#rebuilding).
- One addition or correction per commit.

Pages and photos by other people are kept under the policy in [Other people's material](README.md#other-peoples-material): archive with credit, remove fast on request.

Contributions are shared under [CC BY-SA 4.0](LICENSE); build-script changes under [MIT](cad/tools/LICENSE).
