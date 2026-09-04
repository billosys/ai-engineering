# Slice 01: Confirm Split Map, Version-History Contract, and Expedited Wording

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Current monolith and history inventory records headings, embedded Version History sections, misplaced version-history files, Expedited Mode source surfaces, and framework component roots in scope | `rg -n "monolith|AI-CONSTITUTION-SUPPLEMENT|AI-ENGINEERING-METHODOLOGY|Version History|version-history.md|Expedited Mode|collaboration-framework/SKILL.md|component root|project-management" artifacts/current-monolith-and-history-inventory.md` | correctness-grade | slice-plan | done | artifacts/current-monolith-and-history-inventory.md (attested) | Source inventory before decomposition. |
| F-2 | Operator confirmation packet records approved collaboration-framework numbering, engineering-methods numbering, sibling version-history rule, and exact Expedited Mode wording target | `rg -n "operator confirmation|01-posture-and-ethics|02-structural-pulls|03-collaborative-rights|04-component-route-table|01-engineering-methodology|06-source-package-release-gates|sibling version-history|Expedited Mode|no shortcuts" artifacts/operator-confirmation-packet.md` | correctness-grade | slice-plan | done | artifacts/operator-confirmation-packet.md (attested) | Approval packet for operator review. |
| F-3 | Source impact and validation plan identifies source files, Expedited Mode route surfaces, Makefile/package surfaces, README/docs/AGENTS routes, package-path exceptions, release notes, and validation commands for later slices | `rg -n "source impact|Expedited Mode|PROJECT-MANAGEMENT.md|collaboration-framework/SKILL.md|Makefile|CF_FILES|ALL_SKILL_FILES|README|docs|AGENTS|package-path|release notes|check-skills|collab-framework|check-package-paths|install|ccdp" artifacts/source-impact-and-validation-plan.md` | serious | slice-plan | done | artifacts/source-impact-and-validation-plan.md (attested) | Later source-edit guardrails. |
| F-4 | Slice sequence and approval gate records that Slice02 cannot open until operator approval is recorded and that Expedited Mode does not override this gate | `rg -n "Slice02|operator approval|approval gate|must not open|Expedited Mode|does not override|source decomposition" artifacts/slice-sequence-and-approval-gate.md` | correctness-grade | slice-plan | done | artifacts/slice-sequence-and-approval-gate.md (attested) | Prevents auto-advance into source edits. |
| F-5 | Supporting artifacts are directly cited as planning support: operator-accepted architecture and component file layout plan | `rg -n "operator-accepted-architecture.md|component-file-layout-plan.md|accepted architecture|component file layout" artifacts/operator-confirmation-packet.md artifacts/source-impact-and-validation-plan.md` | serious | slice-plan | done | artifacts/operator-confirmation-packet.md and artifacts/source-impact-and-validation-plan.md (attested) | Ensures prior accepted split design controls this slice. |
| F-6 | Closing report walks all six rows and bubbles the operator confirmation decision to Arc08 | `test -f closing-report.md && rg -n "Rows: 6|Done:|Deferred:|No-op:|Bubble-Up to Arc08|operator confirmation|Slice02|proposed" closing-report.md` | serious | slice-plan | done | closing-report.md (attested) | Slice close evidence. |

## Closure

Slice is proposed-done pending CDC verification.

Rows: 6. Done: 6. Deferred: 0. No-op: 0.
