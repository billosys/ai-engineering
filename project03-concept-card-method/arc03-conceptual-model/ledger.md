# Arc 03: Conceptual Model

## Arc Ledger

Capability: define the v4.0 conceptual model for the concept-card method while
leaving skill architecture and implementation planning to later arcs.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice 01 closed with CDC verification | `test -f slice01-construct-boundaries/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice01-construct-boundaries/cdc-verification.md` | correctness-grade | arc-plan | done | Attested by pointer to `slice01-construct-boundaries/cdc-verification.md`; spot-checked by CDC on 2026-08-30. | Children-closed row. |
| A-2 | Slice 02 closed with CDC verification | `test -f slice02-evidence-lifecycle/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice02-evidence-lifecycle/cdc-verification.md` | correctness-grade | arc-plan | done | Attested by pointer to `slice02-evidence-lifecycle/cdc-verification.md`; spot-checked by CDC on 2026-08-30. | Children-closed row. |
| A-3 | Slice 03 closed with CDC verification | `test -f slice03-graph-cq-run-semantics/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice03-graph-cq-run-semantics/cdc-verification.md` | correctness-grade | arc-plan | done | Attested by pointer to `slice03-graph-cq-run-semantics/cdc-verification.md`; spot-checked by CDC on 2026-08-30. | Children-closed row. |
| A-4 | Slice 04 closed with CDC verification | `test -f slice04-model-synthesis/cdc-verification.md && rg -n "Rows:|Verified by:|reproduced" slice04-model-synthesis/cdc-verification.md` | correctness-grade | arc-plan | done | Attested by pointer to `slice04-model-synthesis/cdc-verification.md`; spot-checked by CDC on 2026-08-30. | Children-closed row. |
| A-5 | Conceptual model defines the required v4.0 constructs and construct boundaries from the Arc02 input packet | `rg -n "concept card|claim|source span|evidence grade|relationship|competency question|extraction run|verifier|reconciliation|memory admission|construct boundary|v4.0 conceptual model" slice*/artifacts arc-plan.md` | serious | arc-plan | done | Reproduced by CDC arc-close pass on 2026-08-30; matches found across the slice artifacts and `arc-plan.md`. | Reproduce at arc scale. |
| A-6 | Model separates extraction confidence, source support, evidence grade, verification state, reconciliation state, and memory admission | `rg -n "extraction confidence|source support|evidence grade|verification state|reconciliation state|memory admission|not one confidence field|lifecycle" slice*/artifacts` | correctness-grade | arc-plan | done | Reproduced by CDC arc-close pass on 2026-08-30; matches found across the slice artifacts. | Reproduce at arc scale. |
| A-7 | Model defines graph, competency-question, and extraction-run semantics without discarding v3.2 carry-forward material | `rg -n "relationship|edge|competency question|CQ|extraction run|traceability|carry forward|v3.2" slice*/artifacts` | serious | arc-plan | done | Reproduced by CDC arc-close pass on 2026-08-30; matches found across the slice artifacts. | Reproduce at arc scale. |
| A-8 | Arc03 leaves skill layout, package behavior, deterministic validators, README integration, and source edits to later arcs | `rg -n "does not choose|Out of scope|skill layout|package behavior|deterministic validator|README|source edits|later arcs|Arc04|Arc05" arc-plan.md slice*/slice-plan.md slice*/artifacts` | correctness-grade | arc-plan | done | Reproduced by CDC arc-close pass on 2026-08-30; scope-fence and downstream-routing matches found across the arc plan, slice plans, and artifacts. | Boundary row. |

## Closure

Closed on 2026-08-30 with composition verdict `delivered`.

Rows: 8. Done: 8. Deferred: 0. No-op: 0.
