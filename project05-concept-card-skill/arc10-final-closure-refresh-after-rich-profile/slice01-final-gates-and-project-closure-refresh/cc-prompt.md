# CC Prompt: Arc10 Slice01 Final Gates And Project Closure Refresh

You are CC implementing Project05 Arc10 Slice01 in Expedited Mode.

## Planning Authority

Read these files first:

- `project05-concept-card-skill/project-plan.md`
- `project05-concept-card-skill/ledger.md`
- `project05-concept-card-skill/arc10-final-closure-refresh-after-rich-profile/arc-plan.md`
- `project05-concept-card-skill/arc10-final-closure-refresh-after-rich-profile/ledger.md`
- `project05-concept-card-skill/arc10-final-closure-refresh-after-rich-profile/slice01-final-gates-and-project-closure-refresh/slice-plan.md`
- `project05-concept-card-skill/arc10-final-closure-refresh-after-rich-profile/slice01-final-gates-and-project-closure-refresh/ledger.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/closing-report.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice04-package-gates-and-arc-closure-inputs/cdc-verification.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice04-package-gates-and-arc-closure-inputs/artifacts/arc-closure-inputs.md`

Treat Arc08 as the post-UAT closure baseline and Arc09 as the closed rich-card
profile refinement. The current task is to refresh final Project05 closure
after Arc09, not to reopen source-skill design unless a final gate exposes a
narrow blocking defect.

## Objective

Rerun final repository-local gates after Arc09, inspect current generated
packages, reconcile Project05 ledger rows P-1 through P-13, record final
deferrals/follow-on boundaries, and prepare refreshed Project05 closure
artifacts.

## Required Boundaries

- Do not defer `document-extraction` or `concept-cards`.
- Do not generate additional concept cards.
- Do not perform or claim operator card acceptance.
- Do not claim independent semantic verification, reconciliation,
  preservation, memory admission, retrieval quality, full-book extraction,
  graph/RAG/MCP implementation, import automation, or runtime ingestion.
- Do not treat Arc09's synthetic rich-profile example as real-source warrant.
- Do not treat historical comparison cards as current generated output.
- Treat those items as future/follow-on boundaries unless the operator
  explicitly expands scope.

## Required Checks

Run or reproduce:

- `make check-skills`
- `make check-skill-versions`
- `make check-package-paths`
- `make all` if needed to ensure fresh generated archives for inspection
- generated package inspection for `document-extraction.zip` and
  `concept-cards.zip`
- `git diff --check`
- source and planning `git status --short --untracked-files=all`

Record warnings and accepted warning dispositions. If a gate fails, fix only
the narrow defect required for Project05 closure and rerun the affected gate.

## Deliverables

- Update source only if a final gate exposes a narrow blocking defect.
- Update planning ledgers and closeout artifacts:
  - Arc10 Slice01 `ledger.md`
  - Arc10 `ledger.md`
  - Project05 `ledger.md`
  - Project05 `closing-report.md`
  - Slice01 `closing-report.md`
  - any durable evidence under Slice01 `artifacts/`
- Expected Slice01 artifacts:
  - `artifacts/final-gate-evidence.md`
  - `artifacts/package-inspection.md`
  - `artifacts/project-ledger-reconciliation.md`
  - `artifacts/final-boundary-and-caveat-review.md`
  - `artifacts/project-closeout-inputs.md`
- Keep source and planning commits scoped with explicit pathspecs.

## Closing Report Requirements

The Slice01 closing report must walk all six slice rows, list validation
evidence, inventory durable artifacts, and bubble up to Arc10 and Project05. It
must state clearly whether Project05 is proposed-done, blocked by a reproduced
defect, or requires an operator decision.

If Project05 is proposed-done, preserve the distinction between implemented
skills, package/install evidence, real-corpus UAT candidates, rich-profile
skill guidance, operator card acceptance, semantic verification, memory
admission, and runtime/RAG/MCP delivery.
