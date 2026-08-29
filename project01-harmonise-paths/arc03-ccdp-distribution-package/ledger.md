# Arc 03: CCDP Distribution Package Ledger

Capability: give CCDP a first-class distribution package and reader-facing
entry point that works from the source clone and from zipped/unzipped package
contexts.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice 01 closes with a current CCDP distribution inventory and package-risk map. | `test -f project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory/cdc-verification.md` | correctness | arc-plan | done | `slice01-ccdp-distribution-inventory/cdc-verification.md` exists; CDC verified Slice 01 closed on 2026-08-29. | Children-closed row; evidence strength reproduced at slice scale. |
| A-2 | The CCDP package contract is designed from actual protocol consumer needs rather than copied from the skill-bundle layout. | Inspect Slice 02 plan/design artifact and Arc 03 close report. | serious | arc-plan | open |  | Composition row; design must distinguish CCDP from installable skills. |
| A-3 | A generated CCDP package can be built, inspected zipped, and inspected unzipped with package-local paths resolving from its entrypoint. | From implementation checkout, run the final CCDP package target and path validation commands selected by Slice 02. | serious | arc-plan | open |  | Reproduce at arc close. |
| A-4 | Existing CCDP assembly still works after distribution packaging changes. | From implementation checkout: `make ccdp` or `cd protocols/ccdp && make ccdp-rfc-strict`, as selected by slice scope. | serious | arc-plan | open |  | Preserve protocol source build. |
| A-5 | Arc 03 findings are routed before Arc 04 release/adoption hardening opens. | Inspect `arc-plan.md` Version History and this ledger after final slice close. | correctness | arc-plan | open |  | Bubble-up disposition row. |
| A-6 | Slice 02 is opened from Slice 01 findings or explicitly deferred with re-entry conditions. | Inspect this arc plan's Version History after Slice 01 close. | correctness | slice01 bubble-up | done | `slice02-ccdp-package-contract-design/{slice-plan.md,ledger.md,cc-prompt.md}` opened on 2026-08-29; arc-plan v1.2 records the Slice 01 -> Slice 02 disposition. | Bubble-up disposition row. |
| A-7 | Slice 02 closes with a concrete CCDP package contract and implementation inputs. | `test -f project01-harmonise-paths/arc03-ccdp-distribution-package/slice02-ccdp-package-contract-design/cdc-verification.md` | correctness | slice02 bubble-up | done | `slice02-ccdp-package-contract-design/cdc-verification.md` exists; CDC verified Slice 02 closed on 2026-08-29. | Children-closed row; evidence strength reproduced at slice scale. |
| A-8 | Slice 03 is opened from the Slice 02 contract or explicitly deferred with re-entry conditions. | Inspect this arc plan's Version History after Slice 02 close. | correctness | slice02 bubble-up | done | `slice03-ccdp-package-implementation/{slice-plan.md,ledger.md,cc-prompt.md}` opened on 2026-08-29; arc-plan v1.4 records the Slice 02 -> Slice 03 disposition. | Bubble-up disposition row. |
