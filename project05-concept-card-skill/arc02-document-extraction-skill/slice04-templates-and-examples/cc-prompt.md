# CC Prompt: Slice04 Templates And Examples

You are CC implementing Project05 Arc02 Slice04 in the ai-engineering source
checkout. This slice is implementation work, not planning-only work.

## Start Here

Read, in this order:

1. `/Users/oubiwann/lab/billosys/ai-engineering/AGENTS.md`
2. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/project-plan.md`
3. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc02-document-extraction-skill/arc-plan.md`
4. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc02-document-extraction-skill/ledger.md`
5. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc02-document-extraction-skill/slice04-templates-and-examples/slice-plan.md`
6. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc02-document-extraction-skill/slice04-templates-and-examples/ledger.md`
7. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc02-document-extraction-skill/slice03-structure-media-locators-and-reports/cdc-verification.md`

Also inspect the current source files under
`/Users/oubiwann/lab/billosys/ai-engineering/knowledge/document-extraction/`.

## Operator-Surfaced Historical Evidence

The operator surfaced historical helper scripts as v1-era extraction evidence:

- `/Users/oubiwann/lab/music-comp/ai-music-theory/scripts/split-neo-riemannian.py`
- `/Users/oubiwann/lab/music-comp/ai-music-theory/scripts/fix-neo-riemannian-images.py`
- `/Users/oubiwann/lab/music-comp/ai-music-theory/scripts/process-epub.sh`
- `/Users/oubiwann/lab/music-comp/ai-music-theory/scripts/process-pdf.sh`

Use these only as evidence for why source-specific helpers need an auditable
template. Do not copy them into the public skill as canonical scripts. Do not
add executable scripts in this slice.

## Implementation Scope

Add sibling support directories and source files under:

- `knowledge/document-extraction/templates/`
- `knowledge/document-extraction/examples/`

Templates must cover:

- manifest;
- structure map;
- media record/report;
- locator record/map;
- validation/readiness report;
- caveat record;
- downstream concept-card handoff;
- non-executable per-extraction helper-script planning.

Examples must cover:

- PDF/Marker handoff;
- EPUB/pandoc handoff;
- HTML/converted-Markdown handoff;
- downstream concept-card handoff.

Update:

- `knowledge/document-extraction/SKILL.md`
- `knowledge/document-extraction/guides/01-load-contract.md`
- `knowledge/document-extraction/guides/03-output-contract.md`, only where
  template/example routing needs alignment
- `knowledge/document-extraction/guides/04-pdf-source-preparation.md`
- `knowledge/document-extraction/guides/05-epub-source-preparation.md`
- `knowledge/document-extraction/guides/10-validation-and-reports.md`, only
  where template/example routing needs alignment
- `knowledge/document-extraction/version-history.md`

Use `metadata.version: "1.3.0"` for this feature slice unless the current
source version history requires a different next version by the time you edit.
Keep the version authority in `SKILL.md` metadata and the changelog in sibling
`version-history.md`; do not create guide-local version histories or duplicate
current-version prose.

## Required Cleanup

Slice03 CDC found residual caller text:

- the final paragraphs of `guides/04-pdf-source-preparation.md` and
  `guides/05-epub-source-preparation.md` still group shared reporting with
  later templates/examples;
- `guides/01-load-contract.md` has a future-oriented format-route footer.

Revise those passages so shared guides are treated as live and templates/examples
are treated as live source support after this slice. Package/docs/install
wiring must still be described as future Arc05 work.

## Scope Boundaries

Do not add executable conversion, splitting, helper, or validation scripts.

Do not add package, Makefile, README, docs, generated zip, or install wiring;
those remain Arc05.

Do not implement `concept-cards` in this slice.

Do not recreate `knowledge/source-preparation/`.

Do not move support material under `guides/` for packaging convenience;
Project04 established sibling support directories as the current layout.

## Verification

Before editing, inspect source status and preserve unrelated work. Use explicit
paths when staging and committing.

Run the ledger checks in
`slice04-templates-and-examples/ledger.md`, including:

```text
scripts/check-skill-description.sh knowledge/document-extraction/SKILL.md
python3 /Users/oubiwann/.codex/skills/.system/skill-creator/scripts/quick_validate.py knowledge/document-extraction
git diff --check
make check-skills
make check-skill-versions
```

Also run or document a local Markdown link/anchor check across
`knowledge/document-extraction/`.

Only run package path checks if you change package surfaces.

Commit only the source changes for Slice04 in the source checkout, using
explicit path names. Include the required co-author trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Then update only this slice's planning ledger and add `closing-report.md` in
the planning worktree. Do not write `cdc-verification.md`; CDC writes that
after independent reproduction.
