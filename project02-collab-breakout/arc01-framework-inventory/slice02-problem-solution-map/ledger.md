# Slice 02: Problem-Solution Map

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Slice 01 verified-close evidence is consumed as the starting point | `test -f ../slice01-source-inventory/cdc-verification.md && rg -n "status: verified-closed|Rows: 7|Done: 7|Slice 02" ../slice01-source-inventory/cdc-verification.md artifacts/problem-solution-map.md artifacts/problem-solution-findings.md` | serious | slice-plan | open | | |
| F-2 | Problem-solution map covers the required historical and functional problem classes | `rg -n "domain knowledge|tooling|drift|duplication|orphan|context|generalization|silent drop|deferral|spec-softening|partial adoption|sycophancy|deference|path|package|release surface|human|LLM" artifacts/problem-solution-map.md` | serious | slice-plan | open | | |
| F-3 | Each problem row maps to mechanism(s), source evidence, fit assessment, and next question or disposition | `rg -n "Problem class|Current mechanism|Source evidence|Fit assessment|Question|Disposition" artifacts/problem-solution-map.md` | correctness-grade | slice-plan | open | | |
| F-4 | Mechanism coverage matrix includes every non-final candidate label from Slice 01 | `rg -n "repository-orientation-and-distribution|protocol-distribution-guidance|framework-entrypoint-and-routing|agent-adapter-and-routing|collaborative-posture-and-ethics|engineering-methodology-and-process|verification-methodology|project-management-wayfinder|project-management-scale-model|planning-worktree-and-layout|planning-open-set-mechanics|slice-close-and-bubble-up|arc-project-composition-close|planning-confirmation-protocol|planning-anti-patterns-and-repair|framework-maintenance-discipline|project-management-examples|project-management-provenance|ledger-verification-protocol|code-audit-discipline|evidence-backed-modernization|coverage-hardening-discipline|delegation-policy|contribution-style-and-voice|contribution-ticket-template|path-contract-constraints" artifacts/mechanism-coverage-matrix.md` | serious | slice01-source-inventory | open | | Labels remain non-final. |
| F-5 | Critical findings identify overlaps, duplication, underfit, overfit, mislabel candidates, improper merge/split candidates, and missing solution areas | `rg -n "overlap|duplication|underfit|overfit|mislabel|improper merge|improper split|missing solution" artifacts/problem-solution-findings.md` | serious | slice-plan | open | | |
| F-6 | Project01 source/package path constraints are represented as functional release-surface constraints | `rg -n "Project01|project01-harmonise-paths|source/package|package-local|zip|release surface|make check-package-paths|path contract" artifacts/problem-solution-map.md artifacts/problem-solution-findings.md` | correctness-grade | project01 constraint | open | | |
| F-7 | Durable outputs live under `artifacts/` and no source files are edited | `test -f artifacts/problem-solution-map.md && test -f artifacts/mechanism-coverage-matrix.md && test -f artifacts/problem-solution-findings.md && git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | serious | project-management v2.5 | open | | |
| F-8 | Open questions for Slice 03, Arc 02, and operator discussion are recorded | `rg -n "Open Questions|Slice 03|Arc 02|operator discussion|decision needed" artifacts/problem-solution-map.md artifacts/problem-solution-findings.md` | correctness-grade | slice-plan | open | | |

## Closure

Slice remains open.
