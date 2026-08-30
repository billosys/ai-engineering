# Arc 03: Functional Analysis

## Arc Ledger

Capability: produce an evidence-backed functional analysis of the current
collaboration framework across expected human and LLM usage patterns,
including direct source reading, packaged skill reading, load paths,
standalone/composed component scenarios, context cost, routing friction,
source/package behavior, and unresolved functional decisions for Arc04.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice 01 closed with CDC verification | `test -f slice01-usage-surface-instrument/cdc-verification.md && rg -n "status: verified-closed|CDC verified|Ledger rows:|scenario matrix|usage surface|functional-analysis method" slice01-usage-surface-instrument/cdc-verification.md` | correctness-grade | arc-plan | done | Reproduced by CDC on 2026-08-30 in `slice01-usage-surface-instrument/cdc-verification.md`; planning commit `2ce787b` contained the proposed close set, and row-count/source-clean/scope checks reproduced. | Children-closed row. |
| A-2 | Slice 02 closed with CDC verification | `test -f slice02-current-workflow-evaluation/cdc-verification.md && rg -n "status: verified-closed|CDC verified|current workflow|friction|deficiency|source/package" slice02-current-workflow-evaluation/cdc-verification.md` | correctness-grade | arc-plan | done | Reproduced by CDC on 2026-08-30 in `slice02-current-workflow-evaluation/cdc-verification.md`; planning commit `470260f` contained the proposed close set, and row-count/source-clean/scope checks reproduced. | Children-closed row. |
| A-3 | Slice 03 closed with CDC verification | `test -f slice03-standalone-composition-evaluation/cdc-verification.md && rg -n "status: verified-closed|CDC verified|standalone|composition|minimum useful load|dependency ordering" slice03-standalone-composition-evaluation/cdc-verification.md` | correctness-grade | arc-plan | done | Reproduced by CDC on 2026-08-30 in `slice03-standalone-composition-evaluation/cdc-verification.md`; planning commit `4b5114b` contained the proposed close set, and row-count/source-clean/scope checks reproduced. | Children-closed row. |
| A-4 | Slice 04 closed with CDC verification | `test -f slice04-functional-synthesis/cdc-verification.md && rg -n "status: verified-closed|CDC verified|functional synthesis|Arc04|close readiness|remediation slice" slice04-functional-synthesis/cdc-verification.md` | correctness-grade | arc-plan | done | Reproduced by CDC on 2026-08-30 in `slice04-functional-synthesis/cdc-verification.md`; planning commit `3b16778` contained the proposed close set, and row-count/source-clean/scope checks reproduced. | Children-closed row. |
| A-5 | Arc03 covers all expected usage surfaces from the project plan | `rg -n "direct source|source-clone|packaged skill|skill loading|human orientation|session start|planning|execution|review|audit|coverage|delegation|contribution|combination" slice01-usage-surface-instrument slice02-current-workflow-evaluation slice04-functional-synthesis` | serious | arc-plan | open | | Reproduce at arc scale. |
| A-6 | Arc03 identifies functional inefficiencies, deficiencies, context-load problems, unclear handoffs, and missing goals | `rg -n "inefficiency|deficiency|context-load|context cost|unclear handoff|routing friction|missing functional goal|failure mode|under-served" slice02-current-workflow-evaluation slice04-functional-synthesis` | serious | arc-plan | open | | Reproduce at arc scale. |
| A-7 | Arc03 evaluates standalone and composed component usage without accepting final architecture | `rg -n "standalone|composed|composition|minimum useful load|dependency order|support asset|adapter|component family|not accepted architecture|non-final" slice03-standalone-composition-evaluation slice04-functional-synthesis` | serious | arc-plan | open | | Reproduce at arc scale. |
| A-8 | Arc03 carries Project01 path/package constraints through functional analysis | `rg -n "Project01|project01-harmonise-paths|source/package|package-local|zip|release surface|make check-package-paths|component contract|package/release gate" slice01-usage-surface-instrument slice02-current-workflow-evaluation slice03-standalone-composition-evaluation slice04-functional-synthesis` | correctness-grade | arc-plan | open | | Reproduce at arc scale. |
| A-9 | Arc03 produces Arc04-ready functional inputs and operator questions | `rg -n "Arc04|architecture input|operator question|operator decision|functional model|scenario coverage|friction register|deficiency register|go / adjust / defer" slice04-functional-synthesis` | correctness-grade | arc-plan | open | | Reproduce at arc scale. |

## Closure

Arc remains open.
