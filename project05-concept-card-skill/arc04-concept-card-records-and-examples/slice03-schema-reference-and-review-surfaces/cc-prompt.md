# CC Prompt: Arc04 Slice03 Schema Reference And Review Surfaces

You are CC implementing Project05 Arc04 Slice03 in the source checkout
`/Users/oubiwann/lab/billosys/ai-engineering`.

Use the current repository instructions and current Project05 planning
authority. Historical Project03 paths are evidence, not live layout
instructions.

## Required Reading

Read these before editing:

- `AGENTS.md`
- `.worktrees/planning/project05-concept-card-skill/project-plan.md`
- `.worktrees/planning/project05-concept-card-skill/ledger.md`
- `.worktrees/planning/project05-concept-card-skill/arc04-concept-card-records-and-examples/arc-plan.md`
- `.worktrees/planning/project05-concept-card-skill/arc04-concept-card-records-and-examples/ledger.md`
- `.worktrees/planning/project05-concept-card-skill/arc04-concept-card-records-and-examples/slice02-representative-examples/cdc-verification.md`
- `.worktrees/planning/project05-concept-card-skill/arc04-concept-card-records-and-examples/slice03-schema-reference-and-review-surfaces/slice-plan.md`
- `.worktrees/planning/project05-concept-card-skill/arc04-concept-card-records-and-examples/slice03-schema-reference-and-review-surfaces/ledger.md`
- `knowledge/concept-cards/SKILL.md`
- `knowledge/concept-cards/version-history.md`
- all files under `knowledge/concept-cards/guides/`
- all files under `knowledge/concept-cards/templates/`
- all files under `knowledge/concept-cards/examples/`
- the `pack_skill` and `pack_component_skill` helper definitions in `Makefile`

Use these preserved Project03 artifacts as design evidence, translating stale
paths and names to current Project05 choices:

- `.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc05-implementation-plan/slice03-schema-validation-plan/artifacts/v40-schema-surface-plan.md`
- `.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc04-skill-architecture/slice04-validation-packaging-discoverability/artifacts/v40-validation-architecture.md`
- `.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc04-skill-architecture/slice05-architecture-synthesis/artifacts/v40-skill-architecture.md`

## Implement

Create sibling reference/review support under
`knowledge/concept-cards/references/`. Do not put this material under
`guides/`.

Required reference files:

- `README.md`
- `record-field-groups.md`
- `vocabulary.md`
- `structural-validation-candidates.md`
- `semantic-audit-boundaries.md`
- `operator-review-gates.md`

Update `knowledge/concept-cards/SKILL.md` to route the references as live
support material. Update `knowledge/concept-cards/version-history.md` with a
compatible minor version bump from `1.5.0`.

Update bounded availability/handoff wording in existing
`knowledge/concept-cards/guides/` files: templates, examples, schema/reference,
and validation-review support should be current after this slice lands. Arc05
package/docs/install boundaries must remain future.

Record the packaging handoff explicitly: current Makefile helper macros copy
`guides/`, `templates/`, and `examples/`, but not `references/`; Arc05 must
wire package support before claiming generated zip or installability.

## Do Not Implement

Do not implement package targets, generated zips, README/docs discoverability,
install behavior, executable validators, validation scripts, JSON Schema,
runtime graph services, GraphRAG, ontology databases, memory runtime
automation, CCDP services, live corpus extraction,
`knowledge/concept-card-method/`, or `knowledge/source-preparation/`.

## Validate

Run focused checks sufficient to close every Slice03 ledger row:

- `scripts/check-skill-description.sh knowledge/concept-cards/SKILL.md`
- `python3 /Users/oubiwann/.codex/skills/.system/skill-creator/scripts/quick_validate.py knowledge/concept-cards`
- `git diff --check`
- `make check-skills`
- `make check-skill-versions`
- a scoped local Markdown link/anchor check over `knowledge/concept-cards/`

Run `make check-package-paths` only if you change package surfaces. This slice
is not expected to do that.

## Commit Discipline

Commit source changes only from the source checkout and use explicit paths in
the commit command. Preserve unrelated work. Then update only this slice's
planning `ledger.md` and add `closing-report.md` in the planning worktree, and
commit those planning changes with explicit paths.

Both commits must include:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Leave the closing report status as CC proposed-done. Do not write
`cdc-verification.md`.
