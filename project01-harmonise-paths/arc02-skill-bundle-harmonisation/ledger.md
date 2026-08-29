# Arc 02: Skill Bundle Harmonisation Ledger

Capability: burn down generated skill-bundle package-path warnings while
preserving source-clone usefulness and the Arc 01 path contract.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice 01 closes with CDC verification or an explicit operator-accepted equivalent. | `test -f project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice01-tooling-entrypoint-links/cdc-verification.md` | correctness | arc-plan | open | | Children-closed row. |
| A-2 | The package-path warning count for targeted tooling/simple skill entrypoints decreases without introducing hard failures. | From implementation checkout, compare Slice 01 baseline and close artifacts, then run `make check-package-paths`. | serious | arc-plan | open | | Composition row; reproduce at arc close. |
| A-3 | Source-clone skill entrypoints remain usable after path edits or transforms. | From implementation checkout, inspect targeted `knowledge/*/SKILL*.md` references and run `make check-skills`. | serious | arc-plan | open | | |
| A-4 | No mature guide prose, CCDP package target, or package layout expansion lands without explicit later-slice approval. | Inspect Slice 01 implementation diff/commit and close evidence. | correctness | arc-plan | open | | Boundary row. |
| A-5 | Slice 02 is either opened from Slice 01 findings or explicitly deferred with re-entry conditions. | Inspect this arc plan's Version History after Slice 01 close. | correctness | arc-plan | open | | Bubble-up disposition row. |
