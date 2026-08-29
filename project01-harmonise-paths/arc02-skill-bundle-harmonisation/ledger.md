# Arc 02: Skill Bundle Harmonisation Ledger

Capability: burn down generated skill-bundle package-path warnings while
preserving source-clone usefulness and the Arc 01 path contract.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice 01 closes with CDC verification or an explicit operator-accepted equivalent. | `test -f project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice01-tooling-entrypoint-links/cdc-verification.md` | correctness | arc-plan | done | `slice01-tooling-entrypoint-links/cdc-verification.md` exists; CDC verified Slice 01 closed on 2026-08-29. | Children-closed row; evidence strength reproduced at slice scale. |
| A-2 | The package-path warning count for targeted tooling/simple skill entrypoints decreases without introducing hard failures. | From implementation checkout, compare Slice 01 baseline and close artifacts, then run `make check-package-paths`. | serious | arc-plan | done | CDC reproduced `make check-package-paths`: hard failures 0, warnings 406; Slice 01 artifact records targeted warnings 20 -> 0 and total warnings 426 -> 406. | Composition row; re-check at arc close. |
| A-3 | Source-clone skill entrypoints remain usable after path edits or transforms. | From implementation checkout, inspect targeted `knowledge/*/SKILL*.md` references and run `make check-skills`. | serious | arc-plan | done | CDC reproduced no targeted `knowledge/(deno|biome|tailwindcss|cobalt)/guides` matches and `make check-skills` passed. | Re-check source/package usability at arc close. |
| A-4 | No mature guide prose, CCDP package target, or package layout expansion lands without explicit later-slice approval. | Inspect Slice 01 implementation diff/commit and close evidence. | correctness | arc-plan | done | CDC inspected source commit `09d1550`: changes are inherited Arc 01 gate files plus targeted Slice 01 entrypoint and exception-file edits. | Boundary row; no mature guide prose or CCDP/package layout changes found. |
| A-5 | Slice 02 is either opened from Slice 01 findings or explicitly deferred with re-entry conditions. | Inspect this arc plan's Version History after Slice 01 close. | correctness | arc-plan | open | | Bubble-up disposition row. |
