# Slice03 Plan: Structure, Media, Locators, And Reports

```yaml
project: project05-concept-card-skill
arc: arc02-document-extraction-skill
slice: slice03-structure-media-locators-and-reports
status: open
opened: 2026-09-06
depends-on:
  - slice01-source-scaffold-and-load-contract
  - slice02-format-preparation-guides
```

## Goal

Implement the shared `document-extraction` guidance that turns format-specific
PDF/EPUB/HTML/converted-source preparation into consistent structure maps,
media records, locator records, validation/readiness reports, and caveat
records. These guides must remain standalone document-extraction guidance while
also producing upstream provenance that `concept-cards` can consume later.

## Scope

In scope:

- add `knowledge/document-extraction/guides/06-html-and-converted-markdown.md`;
- add `knowledge/document-extraction/guides/07-media-path-normalization.md`;
- add `knowledge/document-extraction/guides/08-structure-mapping-and-splitting.md`;
- add `knowledge/document-extraction/guides/09-locator-model.md`;
- add `knowledge/document-extraction/guides/10-validation-and-reports.md`;
- update `knowledge/document-extraction/SKILL.md` so guides 06 through 10 are
  live links, while sibling templates/examples and packaging remain future
  work;
- update `knowledge/document-extraction/guides/02-workflow.md` to remove the
  stale sentence that still treats shared structure/media/locator/reporting
  procedures as future after Slice02;
- inspect and update `knowledge/document-extraction/guides/03-output-contract.md`
  only where it needs live routing or terminology alignment with the new
  shared guides;
- update `knowledge/document-extraction/version-history.md` and
  `metadata.version` in `SKILL.md` under the current source version contract.

Out of scope:

- adding templates or examples; those are Slice04;
- adding package, Makefile, README, docs, generated zip, or install wiring;
  those remain Arc05 unless the operator explicitly expands this slice;
- creating conversion helper scripts or executable validators;
- implementing `concept-cards`;
- recreating `source-preparation` or moving support material under `guides/`
  merely for packaging convenience.

## Required Design Pressure

The new guides must be usable in both Human-Assisted and Agent-Direct
operation. They should tell an assistant how to perform the preparation
directly when files are available, and how to ask a human for bounded excerpts,
file inventories, screenshots, or spot checks when the files are not fully
accessible.

The guides must not collapse uncertain evidence into confident locators or
readiness claims. Unknown page basis, broken anchors, unsupported SVG/HTML,
missing media, duplicate headings, line-number drift, and lossy conversion must
be recorded explicitly.

## Exit Criteria

Slice03 is complete when:

- guides 06 through 10 exist and cover HTML/converted Markdown, media
  normalization, structure mapping/splitting, locator semantics, validation,
  readiness, and caveat reporting;
- `SKILL.md` routes to those guides as live links and leaves templates,
  examples, package targets, generated zips, and install integration clearly
  future work;
- `02-workflow.md` no longer contains the stale future-route sentence for
  shared procedures that Slice03 implements;
- `03-output-contract.md` remains accurate with the new shared guide set;
- version metadata and sibling history are updated with no guide-local version
  history;
- focused validators pass;
- source status is inspected before editing and after commit, and unrelated
  work remains excluded.

## Expected Artifacts

No separate durable planning artifacts are expected. Implementation output is
the source files listed above. Durable close evidence belongs in this slice's
`closing-report.md`, `ledger.md`, and later `cdc-verification.md`.
