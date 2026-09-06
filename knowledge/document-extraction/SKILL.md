---
name: document-extraction
description: |
  Prepare PDF, EPUB, HTML, converted Markdown, and converter-produced source
  bundles for indexing, reading, source review, analysis, or concept-card
  extraction. Use when sources need Markdown extraction, structure mapping,
  media repair, locators, manifests, or readiness and caveat reports. Does not
  own concept-card semantics or ordinary analysis of already usable sources.
license: MIT
metadata:
  version: 1.0.0
  hermes:
    tags: [document-extraction, source-preparation, markdown, provenance]
    category: method-skills
---

# Document Extraction

Prepare sources that a reader or downstream workflow can inspect and trace
back to the preserved input. This is a standalone capability for indexing,
reading, source review, and analysis; `concept-cards` is one downstream
consumer of its upstream provenance.

## Trigger Signals

Load when a task needs to:

- extract usable Markdown from PDF, EPUB, or HTML;
- inspect or repair converter-produced Markdown, metadata, and media bundles;
- map document structure, choose section boundaries, or preserve locators;
- prepare a source manifest, readiness report, or conversion caveat record.

## Do Not Load

Do not load solely to summarize or analyze an already usable source, create
concept cards from prepared evidence, or author a new PDF or EPUB. Load only
the preparation portion if one of those tasks reveals a source-quality gap.

## Ownership And Routing

This skill owns source preservation, preparation, structure and media mapping,
locators, and preparation evidence. It does not own card or claim semantics,
relationship edges, competency questions, reconciliation, or memory admission.
Route those requests to `concept-cards` when that skill is available, passing
the prepared snapshot and its provenance records. Its availability is not a
prerequisite for standalone document extraction.

Read before writing. Preserve raw inputs and converter output, work on derived
copies, and record changes. When structure, media, locators, or conversion
fidelity cannot be verified, stop the affected transformation and record the
uncertainty rather than silently guessing. Human-assisted and agent-direct
operation use the same output contract.

## Guide Map

| Need | Read |
| --- | --- |
| Decide whether to load and where ownership ends | [Load Contract](./guides/01-load-contract.md) |
| Inspect inputs and execute in either operating mode | [Workflow](./guides/02-workflow.md) |
| Define the prepared-source handoff and readiness evidence | [Output Contract](./guides/03-output-contract.md) |

The core contracts are available now. The following are planned routes for
later work, not yet implemented files; names are proposed until those guides
land. Do not try to load them as existing resources.

| Future route | Intended coverage |
| --- | --- |
| `guides/04-pdf-source-preparation.md` | PDF/Marker inspection, page mapping, OCR and conversion checks |
| `guides/05-epub-source-preparation.md` | EPUB/pandoc inspection, navigation, anchors, and media |
| `guides/06-html-and-converted-markdown.md` | HTML capture and converted-Markdown preparation |
| `guides/07-media-path-normalization.md` | Media inventory, path repair, and validation after splitting |
| `guides/08-structure-mapping-and-splitting.md` | Boundary decisions and stable chapter/section files |
| `guides/09-locator-model.md` | Page bases, anchors, headings, URI fragments, and snapshot-bound lines |
| `guides/10-validation-and-reports.md` | Detailed manifest, validation, readiness, and caveat procedures |
| Sibling `templates/` and `examples/` | Reusable records and worked PDF, EPUB, and downstream handoffs |

Detailed format procedures, templates, and examples remain later work. Package
targets, generated zips, and install integration are not yet provided for this
scaffold. Consult the [change record](./version-history.md) for its history.
