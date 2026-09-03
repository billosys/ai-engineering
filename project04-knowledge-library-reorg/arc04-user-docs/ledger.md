# Arc 04: README Decomposition and End-User Documentation

## Arc Ledger

Capability: Arc04 splits the top-level README into concise repository
orientation plus focused end-user documentation under `docs/`, while preserving
the `docs/` versus `knowledge/` distinction and leaving Arc05 vocabulary work
out of scope.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice01 closes with README source surface map, end-user docs decomposition plan, edit sequence, vocabulary boundary register, and validation command inventory | `test -f slice01-readme-docs-decomposition-map/cdc-verification.md && rg -n "README source surface|end-user docs decomposition|doc edit sequence|public language boundary|validation command inventory|verified-closed" slice01-readme-docs-decomposition-map/cdc-verification.md` | serious | arc-plan | done | Reproduced by CDC: `slice01-readme-docs-decomposition-map/cdc-verification.md` records README source surface, end-user docs decomposition, doc edit sequence, public language boundary, validation command inventory, and verified-closed status. | Read-only decomposition evidence. |
| A-2 | README orientation rewrite closes with concise top-level README and links to focused docs | `test -f slice02-readme-orientation-rewrite/cdc-verification.md && rg -n "README.md|orientation|concise|focused docs|docs/|knowledge/|build|install|verified-closed" slice02-readme-orientation-rewrite/cdc-verification.md` | correctness-grade | arc-plan | done | Reproduced by CDC: `slice02-readme-orientation-rewrite/cdc-verification.md` records `README.md`, orientation, concise scope, focused docs, `docs/`, `knowledge/`, build/install routing, and verified-closed status. | README source-edit evidence. |
| A-3 | Focused end-user guide set closes with docs that explain repository, skill library, collaboration framework, knowledge library, build/install, protocol, and contribution paths | `test -f slice03-focused-end-user-guide-set/cdc-verification.md && rg -n "repository|skill library|collaboration framework|knowledge library|build|install|protocol|contribution|verified-closed" slice03-focused-end-user-guide-set/cdc-verification.md` | correctness-grade | arc-plan | open | | Focused docs evidence. |
| A-4 | Documentation link and navigation reconciliation closes with README/docs links, package-path checks, and source/package validation green | `test -f slice04-doc-link-navigation-reconciliation/cdc-verification.md && rg -n "README links|docs links|navigation|package-path|make check|source checkout|validation green|verified-closed" slice04-doc-link-navigation-reconciliation/cdc-verification.md` | serious | arc-plan | open | | Documentation validation evidence. |
| A-5 | Arc04 composition demonstrates README orientation and focused docs compose into user-facing documentation about repository materials | `test -f closing-report.md && rg -n "Composition verdict: delivered|README|orientation|focused docs|end-user documentation|docs/|knowledge/|user-facing" closing-report.md` | serious | arc-plan | open | | Reproduce at arc close. |

## Closure

Arc remains open. Slice01 and Slice02 are verified-closed; Slice03 is open.

Rows: 5. Done: 2. Deferred: 0. No-op: 0.
