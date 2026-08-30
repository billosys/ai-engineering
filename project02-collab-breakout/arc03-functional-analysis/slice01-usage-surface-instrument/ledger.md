# Slice 01: Usage Surface Instrument

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Closed Arc02 inputs exist and are cited by the Slice01 artifacts | `test -f ../../arc02-conceptual-analysis/closing-report.md && test -f ../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-conceptual-model.md && test -f ../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/boundary-and-naming-findings.md && test -f ../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc04-operator-decision-register.md && test -f ../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-close-readiness.md && rg -n "Arc02|conceptual model|boundary and naming findings|operator decision register|close-readiness|closed/composed" artifacts/functional-analysis-method.md artifacts/usage-surface-inventory.md artifacts/scenario-matrix.md artifacts/arc03-input-register.md` | correctness-grade | slice-plan | done | attested: Verify command passed from this slice directory on 2026-08-30; Arc02 close inputs exist and all four artifacts cite the closed/composed Arc02 evidence. | |
| F-2 | Functional-analysis method defines the required vocabulary and row fields | `rg -n "usage surface|load path|entrypoint|trigger|actor|minimum useful load set|dependency order|context cost|routing friction|functional deficiency|source/package mode|role-language clarity|evidence grade|non-final" artifacts/functional-analysis-method.md` | serious | slice-plan | done | attested: Verify command passed on 2026-08-30; `artifacts/functional-analysis-method.md` defines all required terms and fields. | |
| F-3 | Usage-surface inventory covers all project-plan usage surfaces and standalone/composed use | `rg -n "direct source|source-clone|packaged skill|LLM skill loading|human orientation|session start|planning|execution|review|slice close|arc close|audit|coverage|delegation|contribution|standalone|composed|combination" artifacts/usage-surface-inventory.md` | serious | slice-plan | done | attested: Verify command passed on 2026-08-30; `artifacts/usage-surface-inventory.md` covers all required usage surfaces. | |
| F-4 | Scenario matrix records the required evaluation fields for later slices | `rg -n "Scenario ID|Actor|Entrypoint|Trigger|Inputs|Expected outcome|Load set|Dependencies|Friction signals|Evidence to collect|Downstream owner|current monolith|standalone component|composed component|source/package|role-language" artifacts/scenario-matrix.md` | correctness-grade | slice-plan | done | attested: Verify command passed on 2026-08-30; `artifacts/scenario-matrix.md` contains the required row fields and scenario classes. | |
| F-5 | Arc02 risks and operator decisions are carried forward as functional questions | `rg -n "conceptual risk|operator decision|Arc04|functional question|posture/methodology|PM granularity|ledger versus PM|top-level composer|agent-adapter|coverage|audit|contribution|maintenance|ontology critique" artifacts/arc03-input-register.md artifacts/scenario-matrix.md` | serious | slice-plan | done | attested: Verify command passed on 2026-08-30; Arc02 risks and operator decisions are carried forward as Arc03 functional questions. | |
| F-6 | Project01 path/package constraints are carried as functional test surfaces | `rg -n "Project01|project01-harmonise-paths|source/package|package-local|zip|release surface|make check-package-paths|component contract|package/release gate" artifacts/functional-analysis-method.md artifacts/usage-surface-inventory.md artifacts/scenario-matrix.md artifacts/arc03-input-register.md` | correctness-grade | slice-plan | done | attested: Verify command passed on 2026-08-30; all artifacts carry Project01 path/package constraints as functional test surfaces. | |
| F-7 | Outputs remain analytical and do not select final breakout architecture | `rg -n "non-final|not final|not accepted architecture|does not decide|analytical|operator acceptance|Arc04|architecture deferred" artifacts/functional-analysis-method.md artifacts/usage-surface-inventory.md artifacts/scenario-matrix.md artifacts/arc03-input-register.md` | correctness-grade | slice-plan | done | attested: Verify command passed on 2026-08-30; outputs remain analytical and defer architecture to Arc04 after Arc03 and operator acceptance. | |
| F-8 | Required artifacts exist under artifacts/ and source checkout remains clean | `test -f artifacts/functional-analysis-method.md && test -f artifacts/usage-surface-inventory.md && test -f artifacts/scenario-matrix.md && test -f artifacts/arc03-input-register.md && git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | correctness-grade | slice-plan | done | attested: Verify command passed on 2026-08-30; required artifacts exist under `artifacts/` and source checkout tracked diff is clean. | |

## What Worked

- Arc02's conceptual model made usage-surface construction concrete without
  accepting architecture.
- Treating Project01 package constraints as functional test surfaces kept
  source/package behavior visible before implementation planning.
- Separating current-monolith, standalone component, and composed component
  scenarios gives later slices a reusable matrix instead of a prose checklist.

## Closure

Proposed close on 2026-08-30 by CC. Verified by: pending CDC.

Rows: 8. Done: 8. Deferred: 0. No-op: 0.
