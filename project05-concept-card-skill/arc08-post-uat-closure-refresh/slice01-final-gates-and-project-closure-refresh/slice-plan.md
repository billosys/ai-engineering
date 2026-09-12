# Slice01 Plan: Final Gates And Project Closure Refresh

```yaml
project: project05-concept-card-skill
arc: arc08-post-uat-closure-refresh
slice: slice01-final-gates-and-project-closure-refresh
status: cc-proposed-done
opened: 2026-09-11
depends-on:
  - arc07-real-corpus-uat-and-feedback
```

## Goal

Refresh Project05 final closure after real-corpus UAT. This slice reruns the
final repository gates, inspects current generated packages, reconciles the
project ledger through Arc07, records final follow-on boundaries, and writes
the refreshed Project05 closeout without overclaiming candidate-card review,
runtime ingestion, retrieval quality, graph/MCP implementation, or memory
admission.

## Artifact Home

Durable Slice01 artifacts live under:

```text
arc08-post-uat-closure-refresh/slice01-final-gates-and-project-closure-refresh/artifacts/
```

Expected artifact groups:

- final gate evidence;
- package inspection evidence;
- project ledger reconciliation notes;
- final deferral/follow-on boundary notes;
- project closeout inputs.

## In Scope

- Run or reproduce final repository-local gates after Arc07.
- Inspect generated `document-extraction` and `concept-cards` packages and
  confirm current support-directory shapes.
- Reconcile Project05 ledger rows P-2 through P-11, especially P-8 after
  Arc07 closes P-9 through P-11.
- Update final project closure artifacts, including accepted warnings,
  operational incidents, no-ops/deferrals/follow-ons, and UAT boundary
  summaries.
- Keep candidate-card review, semantic verification, reconciliation,
  preservation, memory admission, full-book extraction, runtime/RAG/graph/MCP
  implementation, and retrieval evaluation as explicit future boundaries
  unless the operator separately expands scope.

## Out Of Scope

- Generating or revising additional concept cards.
- Performing operator acceptance or semantic verification of candidate cards.
- Implementing graph/RAG/MCP/runtime/import/retrieval infrastructure.
- Changing Project05's accepted skill architecture unless a final gate exposes
  a narrow blocking defect.
- Publishing a release outside repository-local gates.

## Verification

- Run `make check-skills`.
- Run `make check-skill-versions`.
- Run `make check-package-paths`.
- Run `make all`.
- Inspect generated package contents for both Project05 skills.
- Inspect and update the project ledger and final project closeout.
- Run `git diff --check`.
- Inspect source and planning `git status --short --untracked-files=all`.

## Exit Criteria

This slice exits when Project05 either closes with reproduced final evidence
and explicit follow-on boundaries, or records a blocking defect with a concrete
re-entry condition. It must not defer `document-extraction` or
`concept-cards`, and it must not convert the Arc07 candidate handoff into a
runtime or admitted-memory claim.
