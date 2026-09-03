# Arc 03: Directory Reorganization Implementation

## Arc Ledger

Capability: Arc03 executes accepted file moves and link updates while
preserving source history, minimizing prose changes, and keeping package/build
validation green after each slice.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice01 closes with source status impact map, validation command inventory, and source-edit authorization register | `test -f slice01-preflight-source-status-impact-map/cdc-verification.md && rg -n "source-status-impact-map|validation-command-inventory|source-edit-authorization-register|verified-closed" slice01-preflight-source-status-impact-map/cdc-verification.md` | serious | arc-plan | done | Reproduced by CDC: `slice01-preflight-source-status-impact-map/cdc-verification.md` records `source-status-impact-map`, `validation-command-inventory`, `source-edit-authorization-register`, and `verified-closed`. | Child-slice closure evidence. |
| A-2 | Top-level compatibility decision closes with validated shim, replacement route, or explicit no-shim path | `test -f slice02-top-level-compatibility-decision/cdc-verification.md && rg -n "top-level SKILL.md|validated shim|replacement route|no-shim|make check-skills|make collab-framework|verified-closed" slice02-top-level-compatibility-decision/cdc-verification.md` | serious | arc-plan | done | Reproduced by CDC: `slice02-top-level-compatibility-decision/cdc-verification.md` records top-level `SKILL.md`, no-shim, `make check-skills`, `make collab-framework`, and `verified-closed`. | Gating source-edit decision. |
| A-3 | Mechanical source moves close with accepted knowledge roots, source-prose preservation, and package behavior preserved | `rg -n "verified-closed|mechanical move|knowledge/collaboration-framework|knowledge/<component>|concept-card-method|templates|source-prose preservation|package behavior" slice03-*/*verification.md slice04-*/*verification.md` | serious | arc-plan | done | Reproduced by CDC: Slice03 and Slice04 `cdc-verification.md` files record `verified-closed`, mechanical move evidence, `knowledge/collaboration-framework`, `knowledge/<component>`, `concept-card-method`, templates, source-prose preservation, and package behavior. | Child-slice closure evidence for move slices. |
| A-4 | Package, link, Biome, CCDP, and exception reconciliation closes with validation evidence | `test -f slice05-package-link-edge-reconciliation/cdc-verification.md && rg -n "make check-skills|make check-package-paths|make all|Biome|CCDP|package-local link repair|package-path exception|operator approval|verified-closed" slice05-package-link-edge-reconciliation/cdc-verification.md` | serious | arc-plan | open | | Package and edge-case closure evidence. |
| A-5 | Slice06 closes with implementation reconciliation evidence for moved layout, links, package roots, compatibility surfaces, and validation gates | `test -f slice06-implementation-reconciliation/cdc-verification.md && rg -n "moved layout|README links|package roots|compatibility surfaces|validation gates|source checkout|verified-closed" slice06-implementation-reconciliation/cdc-verification.md` | serious | arc-plan | open | | Reconciliation child-slice closure evidence. |
| A-6 | Arc03 composition demonstrates file moves, README links, package-path checks, and build/package validation compose | `test -f closing-report.md && rg -n "Composition verdict: delivered|file moves|README links|package-path|make check|source history|mechanical moves|validation green" closing-report.md` | serious | arc-plan | open | | Reproduce at arc close. |

## Closure

Arc remains open. Slice01, Slice02, Slice03, and Slice04 are verified-closed;
Slice05 is open.

Rows: 6. Done: 3. Deferred: 0. No-op: 0.
