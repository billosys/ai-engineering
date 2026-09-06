# CC Prompt: Slice03 Structure, Media, Locators, And Reports

You are CC implementing Project05 Arc02 Slice03 in the ai-engineering source
checkout. This slice is implementation work, not planning-only work.

## Start Here

Read, in this order:

1. `/Users/oubiwann/lab/billosys/ai-engineering/AGENTS.md`
2. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/project-plan.md`
3. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc02-document-extraction-skill/arc-plan.md`
4. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc02-document-extraction-skill/ledger.md`
5. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc02-document-extraction-skill/slice03-structure-media-locators-and-reports/slice-plan.md`
6. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc02-document-extraction-skill/slice03-structure-media-locators-and-reports/ledger.md`
7. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc02-document-extraction-skill/slice02-format-preparation-guides/cdc-verification.md`

Also inspect the current source files under
`/Users/oubiwann/lab/billosys/ai-engineering/knowledge/document-extraction/`,
especially:

- `SKILL.md`
- `version-history.md`
- `guides/01-load-contract.md`
- `guides/02-workflow.md`
- `guides/03-output-contract.md`
- `guides/04-pdf-source-preparation.md`
- `guides/05-epub-source-preparation.md`

## Implementation Scope

Implement Slice03 by adding the shared guides:

- `knowledge/document-extraction/guides/06-html-and-converted-markdown.md`
- `knowledge/document-extraction/guides/07-media-path-normalization.md`
- `knowledge/document-extraction/guides/08-structure-mapping-and-splitting.md`
- `knowledge/document-extraction/guides/09-locator-model.md`
- `knowledge/document-extraction/guides/10-validation-and-reports.md`

Update:

- `knowledge/document-extraction/SKILL.md`
- `knowledge/document-extraction/guides/02-workflow.md`
- `knowledge/document-extraction/guides/03-output-contract.md`, only if needed
  to keep the output contract accurate with the new shared guide set
- `knowledge/document-extraction/version-history.md`

Use `metadata.version: "1.2.0"` for this feature slice unless the current
source version history requires a different next version by the time you edit.
Keep the version authority in `SKILL.md` metadata and the changelog in sibling
`version-history.md`; do not create guide-local version histories or duplicate
current-version prose.

## Required Content

The new guides must make `document-extraction` usable as a standalone skill for
indexing, reading, source review, and analysis while also producing upstream
provenance for later `concept-cards` workflows.

Cover:

- HTML capture and converted-Markdown preparation, including preserved raw
  files, snapshots, heading/anchor/resource inspection, dynamic-content
  caveats, and source identity;
- media inventory and path normalization, including relative resolution from
  each split output file, nested media paths, missing or duplicate assets,
  alt/title/attribute preservation, and validation after splitting;
- structure mapping and splitting, including section inventories, front/back
  matter, duplicate headings, unnumbered sections, complete container
  boundaries, stable output names, and sidecar or embedded metadata;
- locator semantics, including page index, physical page, displayed label,
  source path, heading, anchor, URI fragment, snapshot-bound source lines,
  output lines, and unverified bases;
- validation/readiness/caveat reporting, including manifests,
  structure/media/locator records, per-use readiness statuses, caveat
  categories, and explicit no-automatic-readiness behavior.

Each guide needs to support both Human-Assisted Operation and Agent-Direct
Operation. When the assistant has direct file access, it should know what to do
itself. When it lacks access, it should know what bounded excerpts,
inventories, screenshots, or spot checks to request from the operator.

## Required Cleanup

Slice02 CDC found a stale sentence in
`knowledge/document-extraction/guides/02-workflow.md` that still treats shared
structure, media, locator, and reporting procedures as future routes after
Agent-Direct Operation. Remove or revise that sentence so it points accurately
to the newly live shared guides.

## Scope Boundaries

Do not add templates or examples; those are Slice04.

Do not add package, Makefile, README, docs, generated zip, or install wiring;
those remain Arc05 unless the operator explicitly expands this slice.

Do not add conversion helper scripts or executable validators.

Do not implement `concept-cards` in this slice.

Do not recreate `knowledge/source-preparation/`.

Do not move support material under `guides/` merely for packaging convenience;
Project04 established sibling support directories as the current layout.

## Verification

Before editing, inspect source status and preserve unrelated work. Use explicit
paths when staging and committing.

Run the ledger checks in
`slice03-structure-media-locators-and-reports/ledger.md`, including:

```text
scripts/check-skill-description.sh knowledge/document-extraction/SKILL.md
python3 /Users/oubiwann/.codex/skills/.system/skill-creator/scripts/quick_validate.py knowledge/document-extraction
git diff --check
make check-skills
make check-skill-versions
```

Only run package path checks if you change package surfaces.

Commit only the source changes for Slice03 in the source checkout, using
explicit path names. Include the required co-author trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Then update only this slice's planning ledger and add
`closing-report.md` in the planning worktree. Do not write
`cdc-verification.md`; CDC writes that after independent reproduction.
