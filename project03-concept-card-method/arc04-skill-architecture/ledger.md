# Arc 04: Skill Architecture

## Arc Ledger

Capability: define the v4.0 concept-card method skill architecture: load
contract, guide split, template/example set, validation candidates, package
behavior, README integration, maintenance ownership, and Arc05 implementation
handoff.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice01 closes with an architecture input inventory verified by CDC | `test -f slice01-architecture-input-inventory/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice01-architecture-input-inventory/cdc-verification.md` | correctness-grade | arc-plan | done | Attested by pointer to `slice01-architecture-input-inventory/cdc-verification.md`; spot-checked by CDC on 2026-08-30. | Children-closed row. |
| A-2 | Slice02 closes with a load contract and ownership model verified by CDC | `test -f slice02-load-contract-ownership/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice02-load-contract-ownership/cdc-verification.md` | correctness-grade | arc-plan | done | Attested by pointer to `slice02-load-contract-ownership/cdc-verification.md`; spot-checked by CDC on 2026-08-31. | Children-closed row. |
| A-3 | Slice03 closes with a guide, template, and example architecture verified by CDC | `test -f slice03-guide-template-example-architecture/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice03-guide-template-example-architecture/cdc-verification.md` | correctness-grade | arc-plan | done | Attested by pointer to `slice03-guide-template-example-architecture/cdc-verification.md`; spot-checked by CDC on 2026-08-31. | Children-closed row. |
| A-4 | Slice04 closes with validation, packaging, and discoverability decisions verified by CDC | `test -f slice04-validation-packaging-discoverability/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice04-validation-packaging-discoverability/cdc-verification.md` | correctness-grade | arc-plan | done | Attested by pointer to `slice04-validation-packaging-discoverability/cdc-verification.md`; spot-checked by CDC on 2026-08-31. | Children-closed row. |
| A-5 | Slice05 closes with architecture synthesis and Arc05 handoff verified by CDC | `test -f slice05-architecture-synthesis/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice05-architecture-synthesis/cdc-verification.md` | correctness-grade | arc-plan | done | Attested by pointer to `slice05-architecture-synthesis/cdc-verification.md`; spot-checked by CDC on 2026-08-31. | Children-closed row. |
| A-6 | The architecture defines load contract, problem ownership, dependency direction, package behavior, and maintenance ownership | `rg -n "load contract|reason to load|problem ownership|dependency direction|package behavior|maintenance ownership" slice*/artifacts arc-plan.md` | serious | arc-plan | open | | Composition row; reproduce at arc close. |
| A-7 | The architecture maps the accepted conceptual model to skill surfaces without collapsing distinct constructs | `rg -n "concept card|claim|source support|evidence grade|verification|validation result|reconciliation|competency question|extraction run|memory admission|guide|template|example" slice*/artifacts arc-plan.md` | serious | arc-plan | open | | Composition row; reproduce at arc close. |
| A-8 | The architecture records source-edit, validator-code, README, Makefile, package, and generated-zip work as Arc05 implementation-planning inputs | `rg -n "Arc05|source edit|validator code|README|Makefile|package|generated zip|implementation-planning|implementation planning" slice*/artifacts arc-plan.md` | serious | arc-plan | open | | Composition row; reproduce at arc close. |

## Closure

Arc remains open.
