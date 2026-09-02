# Arc 02: Target Directory Contract and Migration Plan

## Arc Ledger

Capability: Arc02 defines an accepted target directory contract, source/package
root model, compatibility strategy, migration sequence, exception policy, and
implementation handoff for the Project04 docs/knowledge-library reorganization.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice01 closes with an Arc02 decision surface inventory, source-root option matrix, and compatibility obligation inventory | `test -f slice01-decision-surface-inventory/cdc-verification.md && rg -n "target-contract-decision-surface|source-root-option-matrix|compatibility-obligation-inventory|verified-closed" slice01-decision-surface-inventory/cdc-verification.md` | serious | arc-plan | done | attested: Slice01 `cdc-verification.md` records `status: verified-closed`; Verify command reproduced by CDC on 2026-09-02. | Child-slice closure evidence. |
| A-2 | Slice02 closes with an accepted directory contract and source/package root contract | `test -f slice02-accepted-directory-contract/cdc-verification.md && rg -n "accepted-target-directory-contract|source-package-root-contract|operator-decision-register|verified-closed" slice02-accepted-directory-contract/cdc-verification.md` | serious | arc-plan | done | attested: Slice02 `cdc-verification.md` records `status: verified-closed`; Verify command reproduced by CDC on 2026-09-02. | Child-slice closure evidence. |
| A-3 | Slice03 closes with migration sequence, validation matrix, compatibility plan, and package-path exception policy | `test -f slice03-migration-validation-plan/cdc-verification.md && rg -n "migration-sequence-plan|validation-and-compatibility-matrix|package-path-exception-policy|verified-closed" slice03-migration-validation-plan/cdc-verification.md` | serious | arc-plan | open | | Child-slice closure evidence. |
| A-4 | Slice04 closes with Arc03 implementation readiness and source-edit slice roadmap | `test -f slice04-implementation-handoff/cdc-verification.md && rg -n "arc03-readiness-packet|source-edit-slice-roadmap|arc02-decision-summary|verified-closed" slice04-implementation-handoff/cdc-verification.md` | serious | arc-plan | open | | Child-slice closure evidence. |
| A-5 | Arc02 composition demonstrates that target layout, path contract, migration plan, compatibility strategy, exception policy, source/package roots, and atomic/composite topology are reconciled for Arc03 | `rg -n "target layout|path contract|migration plan|compatibility|exception|source root|package root|atomic|composite|docs|knowledge|protocols|templates|Arc03" slice*/artifacts arc-plan.md` | serious | arc-plan | open | | Reproduce at arc close. |

## Closure

Arc remains open.

Rows: 5. Done: 2. Deferred: 0. No-op: 0.
