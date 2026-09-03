# Arc 05: Skill Vocabulary, Atomicity, and Public Positioning

## Arc Ledger

Capability: Arc05 settles accepted public language for skill kinds, support
surfaces, and topology distinctions without collapsing kind into topology or
overclaiming planned/unimplemented source surfaces.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice01 closes with current public-language surface inventory, evidence synthesis, decision-question register, source-edit impact map, and validation command inventory | `test -f slice01-public-language-surface-inventory/cdc-verification.md && rg -n "public language surface|evidence synthesis|decision-question register|source-edit impact|validation command inventory|verified-closed" slice01-public-language-surface-inventory/cdc-verification.md` | serious | arc-plan | open | | Read-only vocabulary inventory evidence. |
| A-2 | Accepted vocabulary and positioning decision closes with terms, examples, avoid-list, re-entry conditions, and source-edit authorization boundaries | `test -f slice02-accepted-vocabulary-positioning/cdc-verification.md && rg -n "accepted vocabulary|skill kind|topology|atomic|composite|avoid-list|re-entry|source-edit authorization|verified-closed" slice02-accepted-vocabulary-positioning/cdc-verification.md` | correctness-grade | arc-plan | open | | Vocabulary decision evidence. |
| A-3 | Public wording implementation closes with README/docs/SKILL/package-facing wording updated only where authorized | `test -f slice03-public-wording-implementation/cdc-verification.md && rg -n "README|docs/|SKILL.md|package-facing|authorized|skill kind|atomic|composite|source checkout|verified-closed" slice03-public-wording-implementation/cdc-verification.md` | correctness-grade | arc-plan | open | | Source wording evidence. |
| A-4 | Vocabulary reconciliation closes with public wording, package checks, and docs/SKILL/README consistency validated | `test -f slice04-vocabulary-reconciliation/cdc-verification.md && rg -n "vocabulary reconciliation|README|docs/|SKILL.md|package-path|make check|consistency|validation green|verified-closed" slice04-vocabulary-reconciliation/cdc-verification.md` | serious | arc-plan | open | | Final vocabulary validation evidence. |
| A-5 | Arc05 composition demonstrates accepted public skill vocabulary and wayfinding for kind and topology distinctions | `test -f closing-report.md && rg -n "Composition verdict: delivered|domain|tooling|framework|operational|method|protocol|support|atomic|composite|wayfinding" closing-report.md` | serious | arc-plan | open | | Reproduce at arc close. |

## Closure

Arc remains open. Slice01 is open.

Rows: 5. Done: 0. Deferred: 0. No-op: 0.
