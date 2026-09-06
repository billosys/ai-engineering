# Slice02 Plan: Format Preparation Guides

```yaml
project: project05-concept-card-skill
arc: arc02-document-extraction-skill
slice: slice02-format-preparation-guides
status: open
opened: 2026-09-06
artifact-home: none expected
```

## Goal

Modernize the preserved PDF/Marker and EPUB/pandoc preparation prompts into
reusable `document-extraction` guides. These guides should be useful to an
assistant working directly on accessible files and to a human operator being
guided through the same preparation workflow.

## In Scope

- Add `knowledge/document-extraction/guides/04-pdf-source-preparation.md`.
- Add `knowledge/document-extraction/guides/05-epub-source-preparation.md`.
- Update `knowledge/document-extraction/SKILL.md` so the PDF and EPUB guide
  map entries become live links instead of future-only code spans.
- Update `knowledge/document-extraction/version-history.md` and the
  entrypoint metadata version for the new guides.
- Preserve the core Slice01 ownership boundary: `document-extraction` prepares
  source snapshots, manifests, structure/media/locator evidence, readiness
  decisions, and caveats; `concept-cards` owns card semantics and downstream
  extraction decisions.
- Rewrite the old prompts as general skill instructions, not one-off
  copy/paste prompts. Keep the preserved prompts as provenance, not as current
  source files.
- Include both human-assisted and agent-direct procedures.
- Include inspection-before-editing, raw input preservation, idempotence,
  regeneration, validation, and caveat requirements.
- For PDF/Marker, cover `book.md`, `metadata.json`, `images/`, TOC/page
  mapping, PDF page-basis uncertainty, chapter/section splitting decisions,
  image-reference validation, OCR/conversion caveats, and raw PDF
  preservation.
- For EPUB/pandoc, cover `book.md`, extracted `media/` including common
  `media/media/` nesting, heading/TOC/navigation/anchor inspection, no fixed
  page-number assumption, line/anchor locators, chapter/part/appendix and
  unnumbered structures, media-reference validation, and raw EPUB
  preservation.

## Out Of Scope

- Creating or editing source-specific helper scripts.
- Running an actual PDF, EPUB, Marker, or pandoc conversion on a real source.
- Adding HTML/converted-Markdown shared guidance beyond references needed to
  distinguish it from PDF/EPUB work.
- Adding shared media normalization, structure splitting, locator, readiness,
  caveat, template, or example files reserved for later Arc02 slices.
- Creating `knowledge/document-extraction/templates/` or
  `knowledge/document-extraction/examples/`.
- Changing `Makefile`, `README.md`, `docs/`, release notes, generated zips, or
  install behavior.
- Creating `knowledge/source-preparation/`.
- Creating or editing `knowledge/concept-cards/`.
- Claiming `document-extraction.zip` exists yet.

## Durable Artifacts

No planning artifacts are expected beyond the slice close set. Source files
created or updated in `knowledge/document-extraction/` are the implementation
output.

## Verification Approach

Use direct source inspection and focused validation:

- confirm the source checkout status before edits and preserve all unrelated
  pre-existing changes;
- inspect the two new guides and entrypoint/history updates;
- run `scripts/check-skill-description.sh knowledge/document-extraction/SKILL.md`;
- run `python3 /Users/oubiwann/.codex/skills/.system/skill-creator/scripts/quick_validate.py knowledge/document-extraction`;
- run `git diff --check` in the source checkout;
- confirm local Markdown links added or changed by this slice resolve;
- confirm the source commit uses explicit path names and excludes all
  pre-existing unrelated source changes;
- confirm the planning checkout receives only Slice02 open-set files and any
  CDC/status updates from closing Slice01;
- do not run package gates unless this slice changes package machinery.

## Exit Criteria

- PDF and EPUB preparation guides exist as reusable `document-extraction`
  guides.
- The guides preserve the useful logic of the old v2 prompts while removing
  one-off prompt shape, stale names, stale routing, and source-specific script
  assumptions.
- The guides support both human-assisted and agent-direct operation.
- PDF guidance handles Marker metadata, page-basis uncertainty,
  OCR/conversion caveats, and media validation.
- EPUB guidance handles pandoc media paths, navigation/anchor evidence,
  heading-derived structure, locator limits, and media validation.
- The entrypoint guide map links to the new guides without claiming later
  Slice03/Slice04 routes are implemented.
- Version metadata and sibling history are updated without guide-local version
  histories.
- No superseded `knowledge/source-preparation/` or adjacent
  `knowledge/concept-cards/` root is created.
