# Arc 01: Repository Material Inventory and Classification

## Arc Ledger

Capability: Arc01 produces the source-backed evidence base for Project04 by
inventorying the live repository materials, integrating imported Project02 and
Project03 planning inputs, classifying skill kind and topology, and preparing
Arc02 directory-contract requirements.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice01 closes with current source surface, material-role, and validation-surface inventory artifacts | `test -f slice01-source-surface-inventory/cdc-verification.md && rg -n "current-source-surface-map|material-role-classification|source-validation-surface-map|verified-closed" slice01-source-surface-inventory/cdc-verification.md` | serious | arc-plan | done | attested: Slice01 `cdc-verification.md` records `status: verified-closed`; Verify command reproduced by CDC on 2026-09-01. | Child-slice closure evidence. |
| A-2 | Slice02 closes with imported Project02/Project03 architecture and prior-proposal integration evidence | `test -f slice02-imported-architecture-integration/cdc-verification.md && rg -n "Project02|Project03|operator-accepted architecture|prior proposal|conflict|verified-closed" slice02-imported-architecture-integration/cdc-verification.md` | serious | arc-plan | done | attested: Slice02 `cdc-verification.md` records `status: verified-closed`; Verify command reproduced by CDC on 2026-09-01. | Child-slice closure evidence. |
| A-3 | Slice03 closes with skill kind and atomic/composite topology classification evidence | `test -f slice03-skill-topology-classification/cdc-verification.md && rg -n "skill kind|atomic|composite|Rust|collaboration-framework|topology|verified-closed" slice03-skill-topology-classification/cdc-verification.md` | serious | arc-plan | open | | Child-slice closure evidence. |
| A-4 | Slice04 closes with Arc02 directory-contract readiness synthesis | `test -f slice04-arc01-synthesis/cdc-verification.md && rg -n "Arc02|directory contract|readiness|accepted facts|working hypotheses|unresolved decisions|verified-closed" slice04-arc01-synthesis/cdc-verification.md` | serious | arc-plan | open | | Child-slice closure evidence. |
| A-5 | Arc01 composition demonstrates that current repository material roles, imported architecture inputs, and skill-topology classifications are reconciled for Arc02 | `rg -n "docs|knowledge|templates|protocols|README|Makefile|package-path|atomic|composite|Project02|Project03|Arc02" slice*/artifacts arc-plan.md` | serious | arc-plan | open | | Reproduce at arc close. |

## Closure

Arc remains open.

Rows: 5. Done: 2. Deferred: 0. No-op: 0.
