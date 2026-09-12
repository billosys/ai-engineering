# CC Prompt: Arc08 Slice01 Final Gates And Project Closure Refresh

You are CC implementing Project05 Arc08 Slice01 in Expedited Mode.

## Planning Authority

Read these files first:

- `project05-concept-card-skill/project-plan.md`
- `project05-concept-card-skill/ledger.md`
- `project05-concept-card-skill/arc08-post-uat-closure-refresh/arc-plan.md`
- `project05-concept-card-skill/arc08-post-uat-closure-refresh/ledger.md`
- `project05-concept-card-skill/arc08-post-uat-closure-refresh/slice01-final-gates-and-project-closure-refresh/slice-plan.md`
- `project05-concept-card-skill/arc08-post-uat-closure-refresh/slice01-final-gates-and-project-closure-refresh/ledger.md`
- `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/closing-report.md`

Treat Arc06 as the pre-UAT closure baseline and Arc07 as the real-corpus UAT
closure evidence. The current task is to refresh final Project05 closure after
Arc07, not to reopen source-skill design unless a final gate exposes a narrow
blocking defect.

## Objective

Rerun final repository-local gates after Arc07, inspect current generated
packages, reconcile Project05 ledger rows P-2 through P-11, record final
deferrals/follow-on boundaries, and prepare refreshed Project05 closure
artifacts.

## Required Boundaries

- Do not defer `document-extraction` or `concept-cards`.
- Do not generate additional concept cards.
- Do not perform or claim operator card acceptance.
- Do not claim independent semantic verification, reconciliation,
  preservation, memory admission, retrieval quality, full-book extraction,
  graph/RAG/MCP implementation, import automation, or runtime ingestion.
- Treat those items as future/follow-on boundaries unless the operator
  explicitly expands scope.

## Required Checks

Run or reproduce:

- `make check-skills`
- `make check-skill-versions`
- `make check-package-paths`
- `make all`
- generated package inspection for `document-extraction.zip` and
  `concept-cards.zip`
- `git diff --check`
- source and planning `git status --short --untracked-files=all`

Record warnings and accepted warning dispositions. If a gate fails, fix only
the narrow defect required for Project05 closure and rerun the affected gate.

## Deliverables

- Update source only if a final gate exposes a narrow blocking defect.
- Update planning ledgers and closeout artifacts:
  - Arc08 Slice01 `ledger.md`
  - Arc08 `ledger.md`
  - Project05 `ledger.md`
  - Project05 `closing-report.md`
  - Slice01 `closing-report.md`
  - any durable evidence under Slice01 `artifacts/`
- Keep source and planning commits scoped with explicit pathspecs.

## Closing Report Requirements

The Slice01 closing report must walk all six slice rows, list validation
evidence, inventory durable artifacts, and bubble up to Arc08. It must state
clearly whether Project05 is proposed-done, blocked by a reproduced defect, or
requires an operator decision.
