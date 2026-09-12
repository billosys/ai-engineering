# Slice04 Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S4-1 | Expanded corpus coverage is declared before card generation. | Inspect `artifacts/coverage-plan.md` for corpus snapshot, included/excluded units, rationale, and stop conditions. | serious | Arc07 plan | open | | |
| S4-2 | Source-preparation evidence covers the declared scope. | Inspect manifest, structure/locator records, dependency audit, readiness/caveat report, and preserved snapshot identity. | serious | document-extraction | open | | |
| S4-3 | Citation, figure, and cross-reference dependencies are directly checked or explicitly caveated. | Inspect `dependency-audit.md`, source-support records, and caveat report. | correctness-grade | Slice03 refinement | open | | |
| S4-4 | Candidate concept-card records are generated with claim-specific support and lifecycle boundaries. | Inspect `candidate-cards/` and `extraction-run.md` for cards, claims, source support, evidence grade, extraction confidence, and unassessed lifecycle fields. | serious | concept-cards | open | | |
| S4-5 | Validation sampling tests source faithfulness, locator recovery, qualification retention, and boundary preservation. | Inspect `validation-sampling.md` for sample method, selected records, findings, failures, and limitations. | serious | UAT protocol | open | | |
| S4-6 | Review packet distinguishes candidates from operator-accepted or verified records. | Inspect `review-packet.md` for review tasks, decision states, and explicit non-admission boundaries. | serious | UAT protocol | open | | |
| S4-7 | New friction, stop conditions, or partial-coverage caveats are captured for Slice05. | Inspect `friction-log.md` and `coverage-and-caveat-report.md`. | serious | feedback loop | open | | |
| S4-8 | Scope and hygiene remain clean. | Run `git diff --check`; inspect source/planning status; confirm no unapproved runtime, memory admission, or source-skill edits occurred. | serious | repository hygiene | open | | |

Rows: 8. Open: 8. Done: 0. Deferred: 0. No-op: 0.
