# CC Prompt: Arc02 Slice02 Format Preparation Guides

You are working in the `ai-engineering` repository.

## Role

You are CC for Project05 Arc02 Slice02. Implement the PDF/Marker and
EPUB/pandoc preparation guides for the live `document-extraction` skill.

## Worktrees

- Source checkout:
  `/Users/oubiwann/lab/billosys/ai-engineering`
- Planning checkout:
  `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`
- Project05 directory:
  `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill`
- Slice directory:
  `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc02-document-extraction-skill/slice02-format-preparation-guides`

## Required Context

Read, in this order:

1. `/Users/oubiwann/lab/billosys/ai-engineering/AGENTS.md`
2. `/Users/oubiwann/.codex/skills/collaboration-framework/SKILL.md`
3. `/Users/oubiwann/.codex/skills/project-management/SKILL.md`
4. `/Users/oubiwann/.codex/skills/project-management/guides/README.md`
5. `/Users/oubiwann/.codex/skills/work-verification/SKILL.md`
6. Project05 open context:
   - `project-plan.md`
   - `ledger.md`
   - `arc02-document-extraction-skill/arc-plan.md`
   - `arc02-document-extraction-skill/ledger.md`
   - `arc02-document-extraction-skill/slice01-source-scaffold-and-load-contract/cdc-verification.md`
   - `arc02-document-extraction-skill/slice02-format-preparation-guides/slice-plan.md`
   - `arc02-document-extraction-skill/slice02-format-preparation-guides/ledger.md`
7. Project05 accepted architecture inputs:
   - `artifacts/operator-accepted-project05-reorientation.md`
   - `artifacts/operator-accepted-src-prep-arch.md`
8. Preserved PDF/EPUB prompt provenance:
   - `old/dev/concept-cards/0011-prompt-prepare-pdf-converted-source-for-indexing-v2.md`
   - `old/dev/concept-cards/0012-prompt-prepare-epub-converted-source-for-indexing-v2.md`
9. Current `document-extraction` scaffold:
   - `knowledge/document-extraction/SKILL.md`
   - `knowledge/document-extraction/version-history.md`
   - `knowledge/document-extraction/guides/01-load-contract.md`
   - `knowledge/document-extraction/guides/02-workflow.md`
   - `knowledge/document-extraction/guides/03-output-contract.md`

## Source Status Caution

The source checkout may contain unrelated unstaged edits from concurrent work.
Read the current instructions, inspect source status before editing, preserve
all pre-existing unrelated changes, and exclude them from your source commit
unless the operator explicitly instructs otherwise.

## Implementation Scope

Create and update only the source files needed for this slice:

```text
/Users/oubiwann/lab/billosys/ai-engineering/knowledge/document-extraction/
  SKILL.md
  version-history.md
  guides/
    04-pdf-source-preparation.md
    05-epub-source-preparation.md
```

Update `SKILL.md` so the PDF and EPUB guide map entries are live links to the
new files. Keep the later HTML/converted Markdown, media normalization,
structure splitting, locator, validation/reporting, template, and example
routes marked as future work.

Update the skill version metadata and sibling history for the new guides. Do
not add guide-local version histories or duplicate current skill-version prose.

The new guides must be reusable instructions, not copied one-off prompts. They
must support both:

- human-assisted operation, where the operator supplies conversion results,
  observations, or bounded manual checks; and
- agent-direct operation, where the assistant can inspect files and run local
  tools.

Both guides must preserve raw inputs, inspect before editing, work on derived
outputs, record converter lineage, validate media and locators, support
idempotent regeneration where practical, and stop with caveats when structure,
media identity, locator basis, or conversion fidelity cannot be verified.

## PDF/Marker Guide Requirements

`guides/04-pdf-source-preparation.md` must cover:

- expected inputs such as preserved raw PDF, Marker-style `book.md`,
  `metadata.json`, and `images/`;
- first-pass inspection of raw/converter inputs before edits;
- image reference normalization and validation after splitting;
- use of `metadata.json` table-of-contents data when present, without treating
  it as infallible;
- detecting and recording whether converter page identifiers are zero-based,
  one-based, physical-page-based, or document-label-based;
- spot-checking chapter starts against the raw PDF when possible;
- structure mapping for chapters, parts, appendices, front/back matter, and
  unusual headings;
- splitting decisions and metadata/frontmatter expectations at a contract
  level, without creating a source-specific helper script in this slice;
- OCR, layout, table, image, and conversion caveats;
- readiness outcomes for indexing, reading/source review, analysis, and
  downstream `concept-cards` provenance.

## EPUB/Pandoc Guide Requirements

`guides/05-epub-source-preparation.md` must cover:

- expected inputs such as preserved raw EPUB, pandoc-style `book.md`, and
  extracted `media/`, including common `media/media/` nesting;
- first-pass inspection of converted Markdown, inline TOC material,
  navigation anchors, heading attributes, HTML IDs, and media paths;
- media reference normalization and validation after splitting;
- no fixed page-number assumption for reflowable EPUB content;
- line, heading, anchor, resource path, and URI-fragment locator handling;
- structure mapping for numbered chapters, parts, appendices, prefaces,
  unnumbered sections, inline TOCs, and duplicate headings;
- preserving pandoc div markers, heading attributes, anchors, and raw
  HTML/SVG unless a later cleanup step is explicitly scoped;
- splitting decisions and metadata/frontmatter expectations at a contract
  level, without creating a source-specific helper script in this slice;
- conversion caveats and readiness outcomes for indexing, reading/source
  review, analysis, and downstream `concept-cards` provenance.

## Out Of Scope

Do not:

- create or edit source-specific helper scripts;
- run a real document conversion;
- create `knowledge/document-extraction/templates/` or
  `knowledge/document-extraction/examples/`;
- add shared HTML/converted-Markdown, media, structure, locator,
  validation/readiness, caveat, template, or example guides reserved for later
  Arc02 slices;
- change `Makefile`, `README.md`, `docs/`, release notes, generated zips, or
  install behavior;
- create `knowledge/source-preparation/`;
- create or edit `knowledge/concept-cards/`;
- claim `document-extraction.zip` exists yet.

## Validation

Before closing, run:

```sh
cd /Users/oubiwann/lab/billosys/ai-engineering
scripts/check-skill-description.sh knowledge/document-extraction/SKILL.md
python3 /Users/oubiwann/.codex/skills/.system/skill-creator/scripts/quick_validate.py knowledge/document-extraction
git diff --check
git status --short --untracked-files=all
```

Also inspect the changed local Markdown links directly: the new PDF and EPUB
guide links must resolve, and planned future routes must remain code spans or
clearly non-live future text.

Compare pre-edit source status, source commit file list, and post-commit
status. The source commit must use explicit path names and include only the
Slice02 `knowledge/document-extraction/` files, leaving unrelated pre-existing
changes unstaged/uncommitted.

Do not run package gates unless you changed package machinery, which this
slice should not do.

## Close And Commit

Update the Slice02 ledger row by row. Write
`slice02-format-preparation-guides/closing-report.md` with:

- source files changed;
- source commit hash or `pending until committed`;
- planning files changed;
- validation results;
- row walk;
- artifact inventory;
- bubble-up to Arc02, including whether Arc02's plan needs changes.

Commit the source files and planning close files. Use explicit file names in
the commit command; preserve unrelated changes.

Use the required trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```
