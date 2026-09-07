# CC Prompt: Arc04 Slice02 Representative Examples

You are CC implementing Project05 Arc04 Slice02 in the source checkout
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
- `.worktrees/planning/project05-concept-card-skill/arc04-concept-card-records-and-examples/slice01-record-template-foundation/cdc-verification.md`
- `.worktrees/planning/project05-concept-card-skill/arc04-concept-card-records-and-examples/slice02-representative-examples/slice-plan.md`
- `.worktrees/planning/project05-concept-card-skill/arc04-concept-card-records-and-examples/slice02-representative-examples/ledger.md`
- `knowledge/concept-cards/SKILL.md`
- `knowledge/concept-cards/version-history.md`
- all files under `knowledge/concept-cards/guides/`
- all files under `knowledge/concept-cards/templates/`

Use this preserved Project03 artifact as design evidence, translating stale
paths and names to current Project05 choices:

- `.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc04-skill-architecture/slice03-guide-template-example-architecture/artifacts/v40-example-architecture.md`

## Implement

Create sibling examples under `knowledge/concept-cards/examples/`. Do not put
examples under `guides/`.

Required example files:

- `minimal-card.md`
- `claim-backed-card.md`
- `cq-coverage.md`
- `relationship-edge.md`
- `extraction-run-trace.md`
- `reconciliation.md`
- `memory-admission.md`
- `parallel-worker-default-recipe.md`

Update `knowledge/concept-cards/SKILL.md` to route the examples as live
support material. Update `knowledge/concept-cards/version-history.md` with a
compatible minor version bump from `1.4.0`.

Also update bounded availability/handoff wording in existing
`knowledge/concept-cards/guides/` files: templates and examples should no
longer be described as future or unavailable after this slice lands.
Schema/reference and validation-review support remain future until Slice03.

Examples may be synthetic; label them as synthetic when they are. Keep them
representative enough to show how an assistant or human operator should fill
the templates, preserve construct/lifecycle distinctions, and route raw source
cleanup to `document-extraction`.

## Do Not Implement

Do not implement schema/reference support surfaces, validation-review support
surfaces, package targets, generated zips, README/docs discoverability, install
behavior, executable validators, validation scripts, runtime graph services,
GraphRAG, ontology databases, memory runtime automation, CCDP services, live
corpus extraction, `knowledge/concept-card-method/`, or
`knowledge/source-preparation/`.

## Validate

Run focused checks sufficient to close every Slice02 ledger row:

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
