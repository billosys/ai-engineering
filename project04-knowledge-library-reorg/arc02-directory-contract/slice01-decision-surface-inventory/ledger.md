# Slice 01: Decision Surface Inventory

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Target decision surface consumes Arc01 close and Slice04 readiness artifacts without treating them as source-edit authorization | `rg -n "Arc01|arc02-readiness-packet|directory-contract-requirements|arc01-synthesis-decision-register|Composition verdict: delivered|not source-edit authorization" artifacts/target-contract-decision-surface.md` | serious | slice-plan | open | | Must cite Arc01 handoff evidence and preserve the planning/source boundary. |
| F-2 | Target decision surface covers the required Arc02 decision areas from D-1 through D-12 | `rg -n "D-1|D-12|docs/|knowledge/|templates/|protocols/ccdp|README|SKILL.md|Makefile|package-path|operator decision" artifacts/target-contract-decision-surface.md` | serious | slice-plan | open | | Should be grouped for Slice02 selection work. |
| F-3 | Source-root option matrix separates source-root and package-root decisions and includes current edge cases | `rg -n "source root|package root|frontmatter|selected-file|knowledge/<component>|knowledge/framework|top-level|Biome|multi-entrypoint" artifacts/source-root-option-matrix.md` | serious | slice-plan | open | | Avoid one-root-one-package assumptions. |
| F-4 | Compatibility inventory covers validation commands, package/list surfaces, links, wrappers, and compatibility files | `rg -n "AGENTS.md|CLAUDE.md|Makefile|CF_FILES|ALL_SKILL_FILES|INSTALL_ZIPS|make check-skills|make check-package-paths|make all|make collab-framework|ccdp|wrapper|package-local" artifacts/compatibility-obligation-inventory.md` | serious | slice-plan | open | | Must prepare later implementation gates. |
| F-5 | Artifacts preserve authority levels, planned/live distinctions, re-entry conditions, and kind/topology independence | `rg -n "accepted fact|working hypothesis|operator decision required|re-entry condition|planned surface|not live source|skill kind|topology|atomic|composite|source-files-edited: false" artifacts/*.md` | correctness-grade | slice-plan | open | | Prevent tautological or premature public-taxonomy closure. |
| F-6 | Closing report walks all six rows, states source checkout remains untouched, and bubbles usable findings up to Arc02 | `test -f closing-report.md && rg -n "Rows: 6|Done: 6|source checkout remains untouched|Bubble-Up to Arc02|silent-drop" closing-report.md` | serious | slice-plan | open | | Close-set document; do not create before evidence exists. |

## Closure

Slice remains open.

Rows: 6. Done: 0. Deferred: 0. No-op: 0.
