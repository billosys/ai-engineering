# Slice 03: Arc 01 Synthesis

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Slice 01 and Slice 02 verified-close evidence is consumed as the starting point | `test -f ../slice01-source-inventory/cdc-verification.md && test -f ../slice02-problem-solution-map/cdc-verification.md && rg -n "Slice 01|Slice 02|verified-closed|Rows: 7|Rows: 8|Done: 7|Done: 8" artifacts/arc01-synthesis.md artifacts/candidate-component-inputs.md artifacts/arc02-question-register.md` | serious | slice-plan | open | | |
| F-2 | Arc 01 synthesis states what Arc 01 established, what remains undecided, and whether Arc 01 is ready to close or needs remediation | `rg -n "Arc 01 established|Undecided|Ready to close|remediation|not decided|not final" artifacts/arc01-synthesis.md` | serious | slice-plan | open | | |
| F-3 | Candidate component inputs classify every major Slice 02 candidate or grouped candidate | `rg -n "candidate component|support asset|dependency edge|adapter|constraint|package/release gate|repository-orientation-and-distribution|framework-entrypoint-and-routing|collaborative-posture-and-ethics|engineering-methodology-and-process|ledger-verification-protocol|code-audit-discipline|coverage-hardening-discipline|delegation-policy|contribution-style-and-voice|path-contract-constraints" artifacts/candidate-component-inputs.md` | serious | slice-plan | open | | Labels may be grouped, but no major Slice02 class may silently disappear. |
| F-4 | Mislabels, improper merge/split candidates, overlaps, duplication, underfit, missing solutions, and monolithic load cost are carried forward | `rg -n "mislabel|improper merge|improper split|overlap|duplication|underfit|missing solution|monolithic load cost|component boundary" artifacts/arc01-synthesis.md artifacts/candidate-component-inputs.md artifacts/arc02-question-register.md` | serious | slice02 findings | open | | |
| F-5 | Project01 path/package constraints are carried forward as cross-cutting gates, not user-facing components | `rg -n "Project01|project01-harmonise-paths|source/package|package-local|zip|release surface|make check-package-paths|cross-cutting|not a component|gate" artifacts/arc01-synthesis.md artifacts/candidate-component-inputs.md artifacts/arc02-question-register.md` | correctness-grade | project01 constraint | open | | |
| F-6 | Arc02 question register records owner, decision need, rationale, and source evidence for each question group | `rg -n "Owner:|Decision needed:|Why it matters:|Source evidence:|Operator|Arc 02" artifacts/arc02-question-register.md` | correctness-grade | slice-plan | open | | |
| F-7 | The synthesis remains analytical and does not select final architecture | `rg -n "non-final|not final|not accepted architecture|not selected|Arc 02 analysis|operator discussion" artifacts/arc01-synthesis.md artifacts/candidate-component-inputs.md artifacts/arc02-question-register.md` | serious | arc-plan | open | | |
| F-8 | Durable outputs live under `artifacts/` and no source files are edited | `test -f artifacts/arc01-synthesis.md && test -f artifacts/candidate-component-inputs.md && test -f artifacts/arc02-question-register.md && git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | serious | project-management v2.5 | open | | |

## Closure

Slice remains open.
