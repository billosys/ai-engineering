# Operator-Accepted Source Preparation Architecture

```yaml
project: project05-concept-card-skill
artifact: operator-accepted-src-prep-arch
status: operator-accepted planning input
accepted_on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
```

## Purpose

This artifact preserves the operator-accepted architecture for PDF and EPUB
source-preparation instructions discovered during Project05 anticipation work.
The operator accepted the recommendation to treat source preparation as a
standalone upstream capability that concept-card generation consumes, rather
than placing PDF/EPUB preparation inside the concept-card method itself.

The source-preparation capability should prepare raw or converter-produced
text sources for downstream use by concept-card extraction, full-text
indexing, source review, and ordinary analysis. Concept-card generation remains
an important downstream consumer, but it is not the only consumer.

## Source Inputs

The current source-preparation prompts are preserved in the planning checkout:

- `old/dev/concept-cards/0011-prompt-prepare-pdf-converted-source-for-indexing-v2.md`
- `old/dev/concept-cards/0012-prompt-prepare-epub-converted-source-for-indexing-v2.md`

The PDF prompt prepares Marker-converted PDF sources by normalizing image
references, reading `metadata.json` table-of-contents data, mapping chapter
boundaries, splitting `book.md`, and validating PDF page mappings.

The EPUB prompt prepares pandoc-converted EPUB sources by normalizing media
references, deriving structure from Markdown headings, splitting `book.md`,
and validating heading-to-file mappings where fixed page numbers are not
available.

## Architecture Decision

Create a separate method or operational skill source root for source
preparation after the Project04 knowledge-library reorganization closes or
after the operator explicitly authorizes an interim compatible layout.

Planned source root:

```text
knowledge/source-preparation/
```

Do not place this material under `knowledge/concept-card-method/`. The
concept-card method should depend on and route to source preparation when the
operator task begins with PDF, EPUB, or other raw source normalization.

## Ownership Boundary

`source-preparation` owns:

- preserving raw source files under `knowledge/<kb>/sources/pdf/`,
  `knowledge/<kb>/sources/epub/`, or later accepted source-format roots;
- converting or preparing `book.md` and associated media for source review;
- normalizing media and image references;
- mapping source structure from converter metadata, EPUB navigation, Markdown
  headings, or source-specific structure;
- splitting monolithic converted text into stable chapter or section files;
- recording source locators such as PDF pages, Markdown line numbers, anchors,
  headings, URI fragments, or other source-specific locators;
- producing source-preparation manifests, structure maps, validation reports,
  and caveat records;
- declaring whether the prepared source is ready for concept-card extraction,
  full-text indexing, or standalone analysis.

`concept-card-method` owns:

- concept-card, claim, source-support, source-span, relationship, competency
  question, extraction-run, validation-result, verification-result,
  reconciliation-result, preservation-decision, and memory-admission
  semantics;
- source-faithful extraction from prepared source snapshots;
- evidence grade, extraction confidence, verification state, reconciliation
  state, and memory-admission decisions;
- concept-card templates, examples, validation boundaries, and lifecycle
  result records.

`concept-card-method` should treat prepared source files and source-preparation
reports as upstream inputs and provenance, not as concept-card records.

## Proposed Source Layout

The first implementation should use a thin entrypoint plus focused guides:

```text
knowledge/source-preparation/
├── SKILL.md
├── guides/
│   ├── 01-load-contract.md
│   ├── 02-operator-workflow.md
│   ├── 03-pdf-source-preparation.md
│   ├── 04-epub-source-preparation.md
│   ├── 05-media-path-normalization.md
│   ├── 06-structure-mapping-and-splitting.md
│   ├── 07-validation-and-reports.md
│   └── reference/
│       ├── source-layout.md
│       ├── locator-model.md
│       └── converter-notes.md
├── templates/
│   ├── source-prep-manifest.md
│   ├── structure-map.md
│   └── validation-report.md
├── examples/
│   ├── pdf-prep-report.md
│   └── epub-prep-report.md
└── tools/
    └── optional future generic helpers
```

If Project04's final package contract requires package-compatible support
documents under `guides/`, Project05 may place templates and examples under
`guides/templates/` and `guides/examples/` instead. The Project05 plan should
record whichever layout Project04 makes canonical.

## Dual-Mode Use

The revised material should support two use modes.

Human-assisted mode:

- guide the operator through required inputs, path checks, conversion state,
  structure inspection, and validation;
- explain what choices the human must make when source structure is ambiguous;
- produce clear final reports that let the operator decide whether the source
  is ready for downstream extraction, indexing, or review.

Agent-direct mode:

- let a capable assistant perform the preparatory steps directly when the
  filesystem, tools, and source files are available;
- require explicit read-before-write inspection of raw source, converted
  source, media paths, converter metadata, and generated chapter files;
- preserve raw source files and avoid destructive edits to original inputs;
- produce durable manifests and validation reports instead of only chat
  summaries;
- stop and report uncertainty when chapter boundaries, locator semantics, or
  media paths cannot be verified.

## Output Contract

The source-preparation skill should define a reusable output contract:

- raw source remains preserved under `knowledge/<kb>/sources/<format>/<SourceSlug>/`;
- converted Markdown lives under `knowledge/<kb>/sources/md/<SourceSlug>/`;
- split files live directly under the converted source directory unless a
  later accepted layout changes that convention;
- media references are relative to the split files that contain them;
- preparation evidence lives under
  `knowledge/<kb>/extraction-metadata/<SourceSlug>/` or another accepted
  provenance home;
- each preparation run records converter identity, command or tool source,
  raw-source checksum when practical, generated file list, structure map,
  locator model, known caveats, and validation outcome.

The output contract should explicitly state whether the prepared source is:

- ready for concept-card extraction;
- ready for full-text indexing;
- ready for standalone reading or review;
- blocked or caveated pending manual inspection.

## PDF-Specific Improvements

The PDF guide should preserve the existing v2 logic while generalizing it:

- handle Marker-style `book.md`, `metadata.json`, and `images/` outputs;
- treat `metadata.json` TOC data as a primary source for PDF page locators when
  it is present and useful;
- detect and record whether converter page identifiers appear 0-based,
  1-based, physical-page-based, or document-page-label-based;
- spot-check several chapter starts against the raw PDF when possible;
- preserve OCR and conversion caveats;
- record page-number uncertainty explicitly instead of silently flattening it
  into a single `pdf_page` field;
- validate image references after splitting.

## EPUB-Specific Improvements

The EPUB guide should preserve the existing v2 logic while generalizing it:

- handle pandoc-style `book.md` and extracted `media/` outputs;
- inspect headings, inline table of contents material, navigation anchors, and
  available HTML IDs;
- support chapter, part, appendix, preface, and unnumbered-section structures;
- preserve EPUB anchors and HTML attributes as locators when useful;
- use Markdown line numbers as one locator type, not as a substitute for PDF
  page numbers;
- validate media references after splitting, including pandoc's common
  `media/media/` nesting.

## Shared Improvements

Both guides should be rewritten from copy-paste prompts into reusable
instructions with:

- clear load triggers and negative triggers;
- prerequisites and required inputs;
- first-pass inspection steps before any file edit;
- source-format-specific decision points;
- idempotence and regeneration guidance;
- validation report requirements;
- explicit downstream routing to concept-card extraction, indexing, or
  standalone review;
- caveat handling for ambiguous structure, missing metadata, broken media
  references, long filenames, duplicate headings, and conversion artifacts.

The existing per-source helper-script pattern can remain as a documented first
step. A later improvement may replace per-source scripts such as
`fix-<SourceSlug>-images.py` and `split-<SourceSlug>.py` with generic helpers,
but the first implementation should not promise a mature executable tool
unless the Project05 plan explicitly scopes and verifies it.

## Project05 Integration Requirements

Project05 should incorporate this architecture into its plan, ledger, and
opening implementation-readiness work. At minimum Project05 should:

- treat `source-preparation` as an operator-accepted sibling method skill or
  operational skill, not as a subdirectory of `concept-card-method`;
- add Project04 layout confirmation for `knowledge/source-preparation/`;
- add a Project05 arc or slice that turns the PDF and EPUB v2 prompts into the
  source-preparation skill surfaces;
- add a Project05 arc or slice that updates `concept-card-method` to route
  source-preparation tasks to the new skill;
- preserve the original PDF and EPUB v2 prompts as provenance;
- define validation gates for source-preparation guidance, examples, templates,
  package inclusion, installability, Markdown hygiene, and source/version
  history;
- keep runtime conversion tooling, generic source-prep CLIs, GraphRAG,
  database, memory runtime, and live extraction services out of scope unless
  later explicitly authorized.

## Definition Of Done Addition

Project05 should not be considered complete unless the accepted
source-preparation architecture is either implemented in the post-Project04
canonical layout or explicitly deferred by operator decision with a durable
reason. A silent omission is not acceptable.
