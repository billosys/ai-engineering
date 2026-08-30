# Arc 01: Method Positioning and Project02 Aid

## Arc Ledger

Capability: open Project03 and deliver a compact concept-card-method aid that
Project02 Arc02 can consume before selecting collaboration-framework component
boundaries.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice 01 closed with verification evidence | `test -f slice01-project02-boundary-aid/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice01-project02-boundary-aid/cdc-verification.md` | correctness-grade | arc-plan | open | | |
| A-2 | Slice 02 closes with a Project02 acceptance handoff packet | `test -f slice02-project02-acceptance-handoff/cdc-verification.md && rg -n "Rows:|Verified by:|Project02 Arc02|acceptance handoff|v4.0" slice02-project02-acceptance-handoff/cdc-verification.md` | serious | arc-plan | open | | |
| A-3 | Arc 01 output gives Project02 Arc02 a boundary aid and acceptance handoff without deciding final Project02 architecture | `rg -n "Project02 Arc02|not decide|non-final|component boundary|reason to load|problem ownership" slice01-project02-boundary-aid/artifacts/project02-conceptual-boundary-aid.md && rg -n "Project02 Arc02|operator acceptance|go / adjust / defer|v3.2 baseline|v4.0" slice02-project02-acceptance-handoff/artifacts/project02-arc02-acceptance-handoff.md` | serious | arc-plan | open | | |
| A-4 | Project03 roadmap and project ledger exist and point to later inventory, conceptual-model, skill-architecture, and implementation-planning arcs | `test -f ../project-plan.md && test -f ../ledger.md && rg -n "Arc 02: Method Inventory|Arc 03: Conceptual Model|Arc 04: Skill Architecture|Arc 05: Implementation Plan" ../project-plan.md` | correctness-grade | arc-plan | open | | |

## Closure

Arc remains open.
