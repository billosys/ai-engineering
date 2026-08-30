# Arc 01: Framework Inventory and Problem Map

## Arc Ledger

Capability: establish the source-backed evidence base and problem map needed
for later conceptual and functional analysis of the collaboration-framework
breakout.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice 01 closed with CDC verification | `test -f slice01-source-inventory/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice01-source-inventory/cdc-verification.md` | correctness-grade | arc-plan | open | | attested by slice close |
| A-2 | Slice 02 closed with CDC verification | `test -f slice02-problem-solution-map/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice02-problem-solution-map/cdc-verification.md` | correctness-grade | arc-plan | open | | attested by slice close |
| A-3 | Slice 03 closed with CDC verification | `test -f slice03-arc01-synthesis/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice03-arc01-synthesis/cdc-verification.md` | correctness-grade | arc-plan | open | | attested by slice close |
| A-4 | Current framework sources are inventoried from actual files with source paths | `rg -n "Source Inventory|/Users/oubiwann/lab/billosys/ai-engineering|SKILL.md|README.md|AI-CONSTITUTION-SUPPLEMENT|AI-ENGINEERING-METHODOLOGY|PROJECT-MANAGEMENT|LEDGER-DISCIPLINE" slice01-source-inventory` | serious | arc-plan | open | | reproduce at arc scale |
| A-5 | Arc 01 output maps current mechanisms to historical or functional problems without deciding the final breakout | `rg -n "problem-solution|failure mode|candidate component|not final|conceptual analysis" slice02-problem-solution-map slice03-arc01-synthesis` | serious | arc-plan | open | | reproduce at arc scale |
| A-6 | Open questions for Arc 02 are recorded with enough specificity for operator discussion | `rg -n "Open Questions|operator discussion|decision needed|question" slice03-arc01-synthesis` | correctness-grade | arc-plan | open | | reproduce at arc scale |

## Closure

Arc remains open.
