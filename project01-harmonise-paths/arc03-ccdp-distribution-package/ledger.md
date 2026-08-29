# Arc 03: CCDP Distribution Package Ledger

Capability: give CCDP a first-class distribution package and reader-facing
entry point that works from the source clone and from zipped/unzipped package
contexts.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice 01 closes with a current CCDP distribution inventory and package-risk map. | `test -f project01-harmonise-paths/arc03-ccdp-distribution-package/slice01-ccdp-distribution-inventory/cdc-verification.md` | correctness | arc-plan | open |  | Children-closed row. |
| A-2 | The CCDP package contract is designed from actual protocol consumer needs rather than copied from the skill-bundle layout. | Inspect Slice 02 plan/design artifact and Arc 03 close report. | serious | arc-plan | open |  | Composition row; design must distinguish CCDP from installable skills. |
| A-3 | A generated CCDP package can be built, inspected zipped, and inspected unzipped with package-local paths resolving from its entrypoint. | From implementation checkout, run the final CCDP package target and path validation commands selected by Slice 02. | serious | arc-plan | open |  | Reproduce at arc close. |
| A-4 | Existing CCDP assembly still works after distribution packaging changes. | From implementation checkout: `make ccdp` or `cd protocols/ccdp && make ccdp-rfc-strict`, as selected by slice scope. | serious | arc-plan | open |  | Preserve protocol source build. |
| A-5 | Arc 03 findings are routed before Arc 04 release/adoption hardening opens. | Inspect `arc-plan.md` Version History and this ledger after final slice close. | correctness | arc-plan | open |  | Bubble-up disposition row. |
