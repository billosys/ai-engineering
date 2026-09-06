# CC Prompt: Slice01 Current Layout Reconciliation

You are working in the `ai-engineering` repository.

## Role

You are CC for Project05 Arc01 Slice01. Your job is evidence gathering and
planning reconciliation only. Do not edit source implementation files.

## Worktrees

- Source checkout:
  `/Users/oubiwann/lab/billosys/ai-engineering`
- Planning checkout:
  `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`
- Project05 directory:
  `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill`
- Slice directory:
  `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc01-readiness-and-scope-lock/slice01-current-layout-reconciliation`
- Artifact home:
  `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc01-readiness-and-scope-lock/slice01-current-layout-reconciliation/artifacts`

## Required Context

Read, in this order:

1. `/Users/oubiwann/.codex/skills/collaboration-framework/SKILL.md`
2. `/Users/oubiwann/.codex/skills/project-management/SKILL.md`
3. `/Users/oubiwann/.codex/skills/project-management/guides/README.md`
4. The project, arc, and slice open set:
   - `project-plan.md`
   - `ledger.md`
   - `arc01-readiness-and-scope-lock/arc-plan.md`
   - `arc01-readiness-and-scope-lock/ledger.md`
   - `arc01-readiness-and-scope-lock/slice01-current-layout-reconciliation/slice-plan.md`
   - `arc01-readiness-and-scope-lock/slice01-current-layout-reconciliation/ledger.md`
5. Project05 artifact inputs:
   - `artifacts/README.md`
   - `artifacts/operator-accepted-project05-reorientation.md`
   - `artifacts/operator-accepted-src-prep-arch.md`
   - `artifacts/fresh-codex-project05-planning-prompt.md`
   - `artifacts/source-v32/`
   - `artifacts/project03-concept-card-method/`
   - `artifacts/release-context/`
6. Project04 evidence:
   - `../project04-knowledge-library-reorg/closing-report.md`
   - `../project04-knowledge-library-reorg/artifacts/operator-accepted-architecture.md`
   - `../project04-knowledge-library-reorg/artifacts/package-target-plan.md`
7. Current source surfaces relevant to skills and packages:
   - `README.md`
   - `docs/skill-library.md`
   - `docs/building-and-installing.md`
   - `Makefile`
   - `scripts/check-package-paths`
   - `scripts/check-skill-description.sh`
   - representative live skills such as `knowledge/scientific-methods/`,
     `knowledge/project-management/`, and `knowledge/work-verification/`
8. Historical PDF/EPUB source prompts:
   - `../old/dev/concept-cards/0011-prompt-prepare-pdf-converted-source-for-indexing-v2.md`
   - `../old/dev/concept-cards/0012-prompt-prepare-epub-converted-source-for-indexing-v2.md`

If any expected file is absent, record that as evidence. Do not invent its
contents.

## Operator Decisions To Preserve

- Project05 must implement at least two detailed live skills:
  `document-extraction` and `concept-cards`.
- `document-extraction` replaces the earlier name `source-preparation` and
  must stand alone for PDF, EPUB, HTML, converted Markdown, indexing, reading,
  source review, and downstream method use.
- `concept-cards` replaces the earlier name `concept-card-method`.
- `ontology-engineering` is a likely future composite skill and should be
  reserved, not accidentally collapsed into `concept-cards`.
- Sibling `templates/`, `examples/`, and similar support directories should
  be used when appropriate. Do not place them under `guides/` merely because
  old Project03 planning did.
- Readiness and inventory must not become a path to deferring the key skills.

## Deliverables

Create the following artifacts under the slice artifact home:

- `project05-current-source-surface-inventory.md`
- `project05-artifact-relevance-register.md`
- `project05-naming-and-scope-register.md`
- `project05-package-surface-requirements.md`
- `project05-implementation-roadmap-update.md`

Update the Slice01 ledger row by row with status and evidence. When the slice
is complete, write `closing-report.md` in the slice directory with a per-row
walk and bubble-up notes for Arc01. Do not write `cdc-verification.md`; that is
for CDC.

## Validation

At minimum:

- Check source checkout status before and after.
- Check planning checkout status before and after.
- Run Markdown/diff hygiene checks appropriate to planning-only changes.
- Do not run source package gates unless you change source/package files,
  which this slice should not do.

## Commit

Commit only explicit Project05 planning files from this slice. Preserve
unrelated staged or unstaged work.

Use the required trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```
