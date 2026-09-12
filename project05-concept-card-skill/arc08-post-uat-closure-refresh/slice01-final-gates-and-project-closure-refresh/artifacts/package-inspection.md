# Fresh Project05 Package Inspection

## Inspected Archives

The final `make all` output was inspected directly using `unzip -Z1`.

| Archive | Observed package shape |
| --- | --- |
| `target/skills/document-extraction.zip` | `SKILL.md`, `version-history.md`, ten `guides/` files, eight `templates/` files, and four `examples/` files under the `document-extraction/` package root. |
| `target/skills/concept-cards.zip` | `SKILL.md`, `version-history.md`, ten `guides/` files, twelve `templates/` files, eight `examples/` files, and six `references/` files under the `concept-cards/` package root. |

The document-extraction archive contains the live citation-bearing Markdown
audit guide refined by Arc07 Slice03. The concept-cards archive contains the
sibling `references/` review surface required by Arc04. Both packages preserve
the current sibling-directory layout rather than placing support material under
`guides/` for packaging convenience.

This inspection proves archive membership only. It is not a new isolated
install smoke, operator acceptance, candidate-card verification, or runtime
ingestion claim; Arc05 CDC's explicit temporary-install and byte-comparison
evidence remains the installation acceptance evidence.
