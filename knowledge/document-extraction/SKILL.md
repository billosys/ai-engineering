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
  version: "1.4.1"
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
| Prepare PDF/Marker text, images, structure, and page locators | [PDF Source Preparation](./guides/04-pdf-source-preparation.md) |
| Prepare EPUB/pandoc text, media, navigation, and anchor locators | [EPUB Source Preparation](./guides/05-epub-source-preparation.md) |
| Prepare captured HTML or converted Markdown | [HTML And Converted Markdown](./guides/06-html-and-converted-markdown.md) |
| Inventory media and repair references from each output location | [Media Path Normalization](./guides/07-media-path-normalization.md) |
| Map sections and choose complete split units | [Structure Mapping And Splitting](./guides/08-structure-mapping-and-splitting.md) |
| Preserve typed source and output locations | [Locator Model](./guides/09-locator-model.md) |
| Validate the handoff and decide readiness with caveats | [Validation And Reports](./guides/10-validation-and-reports.md) |

The core contracts, format preparation, and shared procedures above are live.
Choose the format guide for the input, then the shared guides needed for its
preparation and handoff. Read only the relevant procedures.

## Templates And Examples

Copy the relevant fillable records into the accepted evidence home; a single
report may combine categories with stable references. Replace placeholders
with observations or explicit unknowns. Both operating modes use these records;
label operator reports and unverified storage when working from supplied text.
Examples are synthetic illustrations, not evidence of actual conversions.

| Record or task | Template | Representative example |
| --- | --- | --- |
| Identify preserved inputs, derived files and record paths | [Manifest](./templates/manifest.md) | [PDF/Marker](./examples/pdf-marker-handoff.md) |
| Account for sections and complete split units | [Structure Map](./templates/structure-map.md) | [EPUB/pandoc](./examples/epub-pandoc-handoff.md) |
| Track assets and file-relative references | [Media Report](./templates/media-report.md) | [EPUB/pandoc](./examples/epub-pandoc-handoff.md#media) |
| Preserve typed source and output locations | [Locator Map](./templates/locator-map.md) | [PDF page basis](./examples/pdf-marker-handoff.md#locators) |
| Record checks, coverage and per-use dispositions | [Validation And Readiness](./templates/validation-readiness.md) | [HTML/converted Markdown](./examples/html-markdown-handoff.md) |
| Attach uncertainty to affected content | [Caveat Record](./templates/caveat-record.md) | [PDF caveats](./examples/pdf-marker-handoff.md#caveats) |
| Pass upstream provenance to concept-cards when requested | [Concept-Card Handoff](./templates/concept-card-handoff.md) | [Downstream handoff](./examples/concept-card-handoff.md) |
| Specify a source-specific helper before implementation | [Helper-Script Plan](./templates/helper-script-plan.md) | [EPUB split and path case](./examples/epub-pandoc-handoff.md) |

These sibling templates and examples are live source support. The helper plan
is non-executable; no converter, splitter, helper or validator scripts ship
here. This skill has a Makefile package target that produces its generated zip.
Docs/discoverability and isolated install-smoke evidence remain later Arc05
work. Consult the [change record](./version-history.md) for source history.
