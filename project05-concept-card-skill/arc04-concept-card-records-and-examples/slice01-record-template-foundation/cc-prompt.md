# CC Prompt: Arc04 Slice01 Record Template Foundation

You are CC implementing Project05 Arc04 Slice01 in the source checkout
`/Users/oubiwann/lab/billosys/ai-engineering`.

Use the current repository instructions and current Project05 planning
authority. Historical Project03 paths are evidence, not live layout
instructions.

## Required Reading

Read these before editing:

- `AGENTS.md`
- `.worktrees/planning/project05-concept-card-skill/project-plan.md`
- `.worktrees/planning/project05-concept-card-skill/ledger.md`
- `.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/closing-report.md`
- `.worktrees/planning/project05-concept-card-skill/arc04-concept-card-records-and-examples/arc-plan.md`
- `.worktrees/planning/project05-concept-card-skill/arc04-concept-card-records-and-examples/ledger.md`
- `.worktrees/planning/project05-concept-card-skill/arc04-concept-card-records-and-examples/slice01-record-template-foundation/slice-plan.md`
- `.worktrees/planning/project05-concept-card-skill/arc04-concept-card-records-and-examples/slice01-record-template-foundation/ledger.md`
- `knowledge/concept-cards/SKILL.md`
- `knowledge/concept-cards/version-history.md`
- all files under `knowledge/concept-cards/guides/`

Use these preserved Project03 artifacts as design evidence, translating stale
paths and names to current Project05 choices:

- `.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc04-skill-architecture/slice03-guide-template-example-architecture/artifacts/v40-template-architecture.md`
- `.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc05-implementation-plan/slice03-schema-validation-plan/artifacts/v40-schema-surface-plan.md`
- `.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc04-skill-architecture/slice04-validation-packaging-discoverability/artifacts/v40-validation-architecture.md`
- `.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc04-skill-architecture/slice05-architecture-synthesis/artifacts/v40-skill-architecture.md`

## Implement

Create sibling template support under `knowledge/concept-cards/templates/`.
Do not put templates under `guides/`.

Required template files:

- `concept-card.md`
- `claim.md`
- `source-locator.md`
- `source-support.md`
- `relationship-edge.md`
- `competency-question.md`
- `extraction-run.md`
- `validation-result.md`
- `verification-result.md`
- `reconciliation-result.md`
- `preservation-decision.md`
- `memory-admission.md`

Update `knowledge/concept-cards/SKILL.md` to route the templates as live
support material. Update `knowledge/concept-cards/version-history.md` with a
compatible minor version bump from `1.3.0`.

The templates should be usable Markdown records with YAML frontmatter plus
named sections. Preserve the Arc03 construct and lifecycle distinctions rather
than flattening them into a single confidence or status field. Keep source
cleanup routed to `document-extraction`; `concept-cards` templates should
consume prepared source outputs as upstream provenance.

## Do Not Implement

Do not implement examples, schema/reference support surfaces, validation-review
support surfaces, package targets, generated zips, README/docs discoverability,
install behavior, executable validators, validation scripts, runtime graph
services, GraphRAG, ontology databases, memory runtime automation, CCDP
services, live corpus extraction, `knowledge/concept-card-method/`, or
`knowledge/source-preparation/`.

## Validate

Run focused checks sufficient to close every Slice01 ledger row:

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
