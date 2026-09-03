# Arc 06: Validation, Packaging, and Release Readiness

## Arc Ledger

Capability: Arc06 verifies the final Project04 repository layout as source
checkout, packaged skill library, installed Codex skill set, and CCDP protocol
package, with operator acceptance reconciled.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice01 closes with current validation surface map, package/install command matrix, CCDP freshness repair decision map, source-edit authorization register, and release-readiness risk register | `test -f slice01-validation-surface-inventory/cdc-verification.md && rg -n "validation surface|package/install command matrix|CCDP freshness|source-edit authorization|release-readiness risk|verified-closed" slice01-validation-surface-inventory/cdc-verification.md` | serious | arc-plan | done | Reproduced by CDC: `slice01-validation-surface-inventory/cdc-verification.md` records validation surface, package/install command matrix, CCDP freshness, source-edit authorization, release-readiness risk, and verified-closed status. | Read-only final validation inventory evidence. |
| A-2 | Package/path/install validation closes with package-path checks, package builds, generated package inspections, temporary install smoke, and any repairs reconciled | `test -f slice02-package-path-install-validation/cdc-verification.md && rg -n "check-package-paths|make all|package inspection|install smoke|temporary install|repairs reconciled|verified-closed" slice02-package-path-install-validation/cdc-verification.md` | correctness-grade | arc-plan | done | Reproduced by CDC: `slice02-package-path-install-validation/cdc-verification.md` records check-package-paths, make all, package inspection, install smoke, temporary install, repairs reconciled, and verified-closed status. | Final installable-skill behavior evidence. |
| A-3 | CCDP validation closes with ccdp freshness resolved or explicitly accepted, ccdp package checks, and protocol/package separation preserved | `test -f slice03-ccdp-package-validation/cdc-verification.md && rg -n "CCDP|freshness|make ccdp-package|make check-ccdp-package|protocol package|separation|verified-closed" slice03-ccdp-package-validation/cdc-verification.md` | correctness-grade | arc-plan | open | | Final CCDP package evidence. |
| A-4 | Release readiness closes with README/docs links, skill/package/install/CCDP gates, operator acceptance readiness, and final source/planning cleanliness reconciled | `test -f slice04-release-readiness-operator-acceptance/cdc-verification.md && rg -n "README|docs/|check-skills|check-package-paths|install|CCDP|operator acceptance|source checkout|planning checkout|verified-closed" slice04-release-readiness-operator-acceptance/cdc-verification.md` | correctness-grade | arc-plan | open | | Final operator acceptance evidence. |
| A-5 | Arc06 composition demonstrates final validation, packaging, installability, CCDP package separation, and operator acceptance reconciled | `test -f closing-report.md && rg -n "Composition verdict: delivered|check-skills|check-package-paths|install|ccdp|operator acceptance|reconciled" closing-report.md` | serious | arc-plan | open | | Reproduce at arc close. |

## Closure

Arc remains open. Slice01 and Slice02 are verified-closed; Slice03 is open.

Rows: 5. Done: 2. Deferred: 0. No-op: 0.
