# Slice01 Plan: Final Gates And Project Closure

```yaml
project: project05-concept-card-skill
arc: arc06-gate-evidence-and-project-closure
slice: slice01-final-gates-and-project-closure
status: cc-proposed-done
opened: 2026-09-11
depends-on:
  - arc05-packaging-docs-and-installability
```

## Goal

Run the final Project05 closure pass: validate the current repository state,
inspect the generated Project05 packages, reconcile the project ledger, record
accepted warnings and acceptable deferrals/no-ops, and prepare Project05 for
formal closure.

## In Scope

- Run final repository gates named by the project and arc plans.
- Inspect generated package contents for both new skills.
- Reconcile project ledger rows P-2 through P-8 using reproduced evidence from
  closed arcs and any final checks.
- Write a final Project05 closing report or closure draft that distinguishes
  delivered capabilities, accepted warnings, operational incidents, explicit
  deferrals/no-ops, and future work.
- Preserve the boundary that executable validators, runtime services,
  graph/ontology databases, GraphRAG integrations, CCDP services, memory
  runtime automation, CI expansion, and external release publishing are outside
  Project05 unless the operator explicitly expands scope.

## Out Of Scope

- Redesigning the delivered skills.
- Adding new skills beyond `document-extraction` and `concept-cards`.
- Adding executable validators, JSON Schema, runtime services, graph/ontology
  databases, GraphRAG integration, CCDP services, live-corpus extraction,
  memory runtime work, CI expansion, release publishing, or retired old roots.

Narrow source corrections are allowed only when a final gate exposes a
closure-blocking mismatch.

## Verification

- `make check-skills`
- `make check-skill-versions`
- `make check-package-paths`
- `make all`
- `make -s print-skill-zips`
- direct generated-package inspection for `document-extraction.zip` and
  `concept-cards.zip`
- targeted stale-name and runtime-overclaim scans
- `git diff --check`
- source and planning `git status --short --untracked-files=all`

## Exit Criteria

This slice exits when final gates pass, project ledger rows are reconciled, any
remaining deferrals/no-ops are explicit and acceptable, closure artifacts are
written, and both worktrees are clean after commits. CDC verification then
performs final Project05 closure.
