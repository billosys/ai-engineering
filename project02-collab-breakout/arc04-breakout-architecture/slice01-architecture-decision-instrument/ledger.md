# Slice 01: Architecture Decision Instrument

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Slice01 artifacts cite closed Arc02 and Arc03 evidence as inputs | `test -f ../../arc02-conceptual-analysis/closing-report.md && test -f ../../arc03-functional-analysis/closing-report.md && test -f ../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-conceptual-model.md && test -f ../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc04-operator-decision-register.md && test -f ../../arc03-functional-analysis/slice04-functional-synthesis/artifacts/arc03-functional-model.md && test -f ../../arc03-functional-analysis/slice04-functional-synthesis/artifacts/arc04-architecture-inputs.md && rg -n "Arc02|conceptual model|boundary and naming|operator decision register|Arc03|functional model|scenario coverage|functional fit|architecture inputs|closing report|input contract" artifacts/*.md` | correctness-grade | slice-plan | done | attested: Verify command passed from this slice directory on 2026-08-31; artifacts cite closed Arc02 and Arc03 evidence as inputs. | |
| F-2 | Architecture decision method defines Arc04 classification vocabulary and decision rubric | `rg -n "architecture decision method|classification vocabulary|candidate component|component family|support asset|adapter|constraint|package/release gate|non-component|reason-to-load|direct-load|go / adjust / defer|evidence grade|operator acceptance" artifacts/architecture-decision-method.md` | correctness-grade | slice-plan | done | attested: Verify command passed on 2026-08-31; `artifacts/architecture-decision-method.md` defines the classification vocabulary and decision rubric. | |
| F-3 | Component contract schema defines mandatory fields for later candidate evaluation | `rg -n "component-contract schema|component name|purpose|owned problem|boundary|dependency|wayfinding|support asset|adapter|source path|package path|package-local|zip root|release gate|maintenance owner|version history" artifacts/component-contract-schema.md` | correctness-grade | slice-plan | done | attested: Verify command passed on 2026-08-31; `artifacts/component-contract-schema.md` defines mandatory fields for later candidate evaluation. | |
| F-4 | Candidate architecture worklist seeds all major candidates and non-component categories from Arc02 and Arc03 | `rg -n "collaborative-posture|engineering-methodology|ledger-verification|project-management|code-audit|coverage-hardening|delegation-policy|contribution|top-level composer|agent adapter|support asset|constraint|package/release gate|deferred|non-component|ontology critique|component-maintenance" artifacts/candidate-architecture-worklist.md` | correctness-grade | slice-plan | done | attested: Verify command passed on 2026-08-31; `artifacts/candidate-architecture-worklist.md` seeds major candidates and non-component categories from Arc02 and Arc03. | |
| F-5 | Operator decision and risk register carries D-01 through D-12 and OQ-01 through OQ-09, or records explicit merged rows | `rg -n "D-01|D-02|D-03|D-04|D-05|D-06|D-07|D-08|D-09|D-10|D-11|D-12|OQ-01|OQ-02|OQ-03|OQ-04|OQ-05|OQ-06|OQ-07|OQ-08|OQ-09|operator decision|operator question|risk|acceptance" artifacts/operator-decision-and-risk-register.md` | serious | slice-plan | done | attested: Verify command passed on 2026-08-31; `artifacts/operator-decision-and-risk-register.md` carries D-01 through D-12 and OQ-01 through OQ-09 with risks and acceptance checks. | |
| F-6 | Project01 path/package constraints and non-final architecture boundary are preserved | `rg -n "Project01|project01-harmonise-paths|source/package|package-local|zip root|release surface|component contract|CCDP|make check-package-paths|package/release gate|non-final|not accepted architecture|does not decide|operator acceptance required" artifacts/*.md` | correctness-grade | slice-plan | done | attested: Verify command passed on 2026-08-31; Project01 path/package constraints and non-final architecture boundary are preserved. | |
| F-7 | Required artifacts exist under artifacts/ and source checkout remains clean | `test -f artifacts/architecture-input-register.md && test -f artifacts/architecture-decision-method.md && test -f artifacts/component-contract-schema.md && test -f artifacts/candidate-architecture-worklist.md && test -f artifacts/operator-decision-and-risk-register.md && git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | correctness-grade | slice-plan | done | attested: Verify command passed on 2026-08-31; required artifacts exist under `artifacts/` and source checkout tracked diff is clean. | |
| F-8 | Close report walks all ledger rows and bubbles findings up to Arc04 | `test -f closing-report.md && rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|Silent-Drop Diff|Bubble-Up To Arc04|Rows: 8" closing-report.md` | correctness-grade | slice-plan | done | attested: Verify command passed on 2026-08-31; `closing-report.md` walks F-1 through F-8 and bubbles findings up to Arc04. | Checked at slice close. |

## What Worked

- Closed Arc02 and Arc03 reports provided a clean input boundary, so Slice01
  could build an instrument without reopening earlier analysis.
- Keeping operator decisions and functional operator questions as separate
  source rows made the later acceptance path easier to audit.
- Encoding Project01 source/package constraints directly into the contract
  schema kept package/release gates visible before package paths are accepted.

## Closure

Proposed close on 2026-08-31 by CC. Verified by: pending CDC.

Rows: 8. Done: 8. Deferred: 0. No-op: 0.
