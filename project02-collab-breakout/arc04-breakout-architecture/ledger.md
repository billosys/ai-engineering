# Arc 04: Breakout Architecture

## Arc Ledger

Capability: produce an operator-accepted breakout architecture for the current
collaboration framework, including standalone/composable components,
component contracts, dependencies, support assets, adapters, source/package
behavior, package shape, release gates, and the top-level composition model.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice 01 closed with CDC verification | `test -f slice01-architecture-decision-instrument/cdc-verification.md && rg -n "status: verified-closed|CDC verified|architecture decision instrument|component-contract schema|candidate worklist|operator decision" slice01-architecture-decision-instrument/cdc-verification.md` | correctness-grade | arc-plan | open | | Children-closed row. |
| A-2 | Slice 02 closed with CDC verification | `test -f slice02-component-contract-evaluation/cdc-verification.md && rg -n "status: verified-closed|CDC verified|component contract|go / adjust / defer|support asset|adapter|constraint|package/release gate" slice02-component-contract-evaluation/cdc-verification.md` | correctness-grade | arc-plan | open | | Children-closed row. |
| A-3 | Slice 03 closed with CDC verification | `test -f slice03-target-composition-package-architecture/cdc-verification.md && rg -n "status: verified-closed|CDC verified|target architecture|component graph|top-level composer|package architecture|source/package" slice03-target-composition-package-architecture/cdc-verification.md` | correctness-grade | arc-plan | open | | Children-closed row. |
| A-4 | Slice 04 closed with CDC verification and operator acceptance evidence | `test -f slice04-operator-acceptance-architecture-synthesis/cdc-verification.md && rg -n "status: verified-closed|CDC verified|operator acceptance|accepted architecture|Arc05|implementation inputs" slice04-operator-acceptance-architecture-synthesis/cdc-verification.md` | correctness-grade | arc-plan | open | | Children-closed row. |
| A-5 | Arc04 consumes closed Arc02 conceptual evidence and closed Arc03 functional evidence without reopening analysis | `rg -n "Arc02|conceptual model|boundary and naming|operator decision register|Arc03|functional model|scenario coverage|functional fit|architecture inputs|closing report|input contract" slice01-architecture-decision-instrument slice02-component-contract-evaluation slice03-target-composition-package-architecture slice04-operator-acceptance-architecture-synthesis` | serious | arc-plan | open | | Reproduce at arc scale. |
| A-6 | Accepted architecture defines component names, purposes, contracts, boundaries, dependencies, wayfinding behavior, package shape, and top-level composition | `rg -n "accepted component|component name|purpose|contract|boundary|dependency|wayfinding|package shape|support asset|adapter|top-level composer|collaboration-framework composition" slice02-component-contract-evaluation slice03-target-composition-package-architecture slice04-operator-acceptance-architecture-synthesis` | correctness-grade | arc-plan | open | | Reproduce at arc scale. |
| A-7 | Architecture preserves Project01 source/package constraints and release gates | `rg -n "Project01|project01-harmonise-paths|source/package|package-local|zip root|release surface|README|SKILL.md|Makefile|make check-package-paths|package/release gate|component contract" slice01-architecture-decision-instrument slice02-component-contract-evaluation slice03-target-composition-package-architecture slice04-operator-acceptance-architecture-synthesis` | correctness-grade | arc-plan | open | | Reproduce at arc scale. |
| A-8 | Operator decisions and risks are explicitly dispositioned before Arc04 close | `rg -n "operator decision|operator question|operator acceptance|D-01|D-12|OQ-01|OQ-09|accepted|deferred|go / adjust / defer|risk disposition" slice01-architecture-decision-instrument slice04-operator-acceptance-architecture-synthesis` | correctness-grade | arc-plan | open | | Reproduce at arc scale. |
| A-9 | Arc04 produces Arc05-ready implementation-planning inputs without editing source | `rg -n "Arc05|implementation plan|source edits|README|SKILL.md|packaging|verification gate|make check-package-paths|source files remain untouched|no source edits" slice04-operator-acceptance-architecture-synthesis && git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` | correctness-grade | arc-plan | open | | Reproduce at arc scale. |

## Closure

Arc remains open.
