# Arc 01: Distribution Path Contract Ledger

Capability: establish a repeatable inventory of package path failures and a
written path semantics contract that later implementation slices can apply.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice 01 closes with CDC verification or an explicit operator-accepted equivalent. | `test -f project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/cdc-verification.md` | correctness | arc-plan | done | attested: `slice01-package-path-audit/cdc-verification.md` verifies planning commit `a85f9fb` with all 7 rows reproduced. | Children-closed row; composition remains open until arc close. |
| A-2 | The current package path failure inventory covers all generated zips. | Inspect Slice 01 closing evidence for an archive scan over every `*.zip` named by `INSTALL_ZIPS`. | serious | arc-plan | open | | Composition row; reproduce at arc close. |
| A-3 | Every observed mismatch is classified as bundled-reference, source-clone-reference, repo-only/provenance, example-project path, external URL, or parser false positive. | Inspect the Slice 01 contract report and verify all unresolved hits carry one classification. | serious | arc-plan | open | | Classification names may change only if Slice 01 explains why. |
| A-4 | The contract identifies which later changes should be source edits, staging-time transforms, package layout changes, validation exceptions, or CCDP packaging work. | Inspect the Slice 01 contract report for a "Disposition by fix type" section. | correctness | arc-plan | open | | |
| A-5 | Slice 02 is either opened from the Slice 01 findings or explicitly deferred with re-entry conditions. | Inspect this arc plan's Version History after Slice 01 close. | correctness | arc-plan | open | | Bubble-up disposition row. |
