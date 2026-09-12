# Slice01 Plan: Final Gates And Project Closure Refresh

```yaml
project: project05-concept-card-skill
arc: arc10-final-closure-refresh-after-rich-profile
slice: slice01-final-gates-and-project-closure-refresh
status: cdc-verified
opened: 2026-09-12
depends-on:
  - arc09-rich-concept-card-profile
```

## Goal

Refresh Project05 final closure after the rich concept-card profile refinement.
This slice reruns the final repository gates, inspects current generated
packages, reconciles the project ledger through Arc09, records final
follow-on boundaries, and writes the refreshed Project05 closeout without
overclaiming candidate-card review, runtime ingestion, retrieval quality,
graph/MCP implementation, semantic verification, or memory admission.

## Artifact Home

Durable Slice01 artifacts live under:

```text
arc10-final-closure-refresh-after-rich-profile/slice01-final-gates-and-project-closure-refresh/artifacts/
```

Expected artifact groups:

- final gate evidence;
- package inspection evidence;
- project ledger reconciliation notes;
- final boundary and caveat review;
- project closeout inputs.

## In Scope

- Run or reproduce final repository-local gates after Arc09.
- Inspect generated `document-extraction` and `concept-cards` packages and
  confirm current support-directory shapes, including Arc09 rich-profile
  surfaces.
- Reconcile Project05 ledger rows P-1 through P-13, especially P-8 after
  Arc09 closes P-12 and P-13.
- Update final project closure artifacts, including accepted warnings,
  operational incidents, no-ops/deferrals/follow-ons, UAT boundaries, and
  rich-profile boundaries.
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
- Run `make all` if fresh generated archives are not already produced by the
  package gates.
- Inspect generated package contents for both Project05 skills.
- Inspect and update the project ledger and final project closeout.
- Run `git diff --check`.
- Inspect source and planning `git status --short --untracked-files=all`.

## Exit Criteria

This slice exits when Project05 either closes with reproduced final evidence
and explicit follow-on boundaries, or records a blocking defect with a concrete
re-entry condition. It must not defer `document-extraction` or `concept-cards`,
and it must not convert Arc07 candidate-card or Arc09 rich-profile evidence
into a runtime, accepted-card, semantic-verification, or admitted-memory claim.

## CDC Outcome

CDC verified this slice on 2026-09-12 by independently reproducing the final
repository gates, archive integrity, archive-content inspection, whitespace
checks, status hygiene, P-8 no-deferral conclusion, and final caveat boundary.
Arc10 and Project05 close from this verification.
