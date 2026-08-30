# Arc 01: Framework Inventory and Problem Map

## Arc Ledger

Capability: establish the source-backed evidence base and problem map needed
for later conceptual and functional analysis of the collaboration-framework
breakout.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice 01 closed with CDC verification | `test -f slice01-source-inventory/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice01-source-inventory/cdc-verification.md` | correctness-grade | arc-plan | done | `slice01-source-inventory/cdc-verification.md` exists; CDC verified Slice 01 closed on 2026-08-29 with Rows: 7, Done: 7, Deferred: 0, No-op: 0. | Children-closed row; evidence strength reproduced at slice scale. |
| A-2 | Slice 02 closed with CDC verification | `test -f slice02-problem-solution-map/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice02-problem-solution-map/cdc-verification.md` | correctness-grade | arc-plan | done | `slice02-problem-solution-map/cdc-verification.md` exists; CDC verified Slice 02 closed on 2026-08-29 with Rows: 8, Done: 8, Deferred: 0, No-op: 0. | Children-closed row; evidence strength reproduced at slice scale. |
| A-3 | Slice 03 closed with CDC verification | `test -f slice03-arc01-synthesis/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice03-arc01-synthesis/cdc-verification.md` | correctness-grade | arc-plan | done | `slice03-arc01-synthesis/cdc-verification.md` exists; CDC verified Slice 03 closed on 2026-08-30 with Rows: 8, Done: 8, Deferred: 0, No-op: 0. | Children-closed row; evidence strength reproduced at slice scale. |
| A-4 | Current framework sources are inventoried from actual files with source paths | `rg -n "Source Inventory|/Users/oubiwann/lab/billosys/ai-engineering|SKILL.md|README.md|AI-CONSTITUTION-SUPPLEMENT|AI-ENGINEERING-METHODOLOGY|PROJECT-MANAGEMENT|LEDGER-DISCIPLINE" slice01-source-inventory` | serious | arc-plan | done | Reproduced at arc scale on 2026-08-30: Slice01 inventory artifacts contain actual source paths for the required framework sources, including README, SKILL, Constitution, Methodology, PM, PM split files, and ledger discipline. | Composition row; reproduced at arc scale. |
| A-5 | Arc 01 output maps current mechanisms to historical or functional problems without deciding the final breakout | `rg -n "problem-solution|failure mode|candidate component|not final|conceptual analysis" slice02-problem-solution-map slice03-arc01-synthesis` | serious | arc-plan | done | Reproduced at arc scale on 2026-08-30: Slice02 and Slice03 contain problem-solution, failure-mode, candidate-component, not-final, and conceptual-analysis routing language. | Composition row; final architecture remains undecided. |
| A-6 | Open questions for Arc 02 are recorded with enough specificity for operator discussion | `rg -n "Open Questions|operator discussion|decision needed|question" slice03-arc01-synthesis` | correctness-grade | arc-plan | done | Reproduced at arc scale on 2026-08-30: Slice03 records operator and Arc02 questions with owner, decision need, rationale, and source evidence; the question register contains 15 questions. | Composition row; reproduced at arc scale. |

## Closure

Closed on 2026-08-30 by CDC.

Composition verdict: delivered.

Rows: 6. Done: 6. Deferred: 0. No-op: 0.
