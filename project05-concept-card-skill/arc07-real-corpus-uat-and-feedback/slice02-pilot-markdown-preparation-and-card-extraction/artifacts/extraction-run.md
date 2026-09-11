---
record_type: extraction-run
id: run-arc07-s02-pilot
revision: 1
run_status: complete-with-caveats
actor: {id: codex-cc, role: extractor, mode: agent-direct}
started_at: 2026-09-11
completed_at: 2026-09-11
prepared_source_refs:
  - {id: ps-ccn-book-pilot-20260911, revision: 1, path: "prepared-source-manifest.md"}
output_refs:
  - {id: candidate-card-packet, revision: 1, path: "candidate-cards/README.md"}
---

# Extraction Run: Arc07 Slice02 Pilot

## Scope And Method

The run inspected only the declared Chapter 1 and Chapter 7 units from the
pinned source. It used the preparation manifest, structure map, and locators
to create four candidate cards and four source-support records. No source text
was copied into planning artifacts beyond short descriptive references, and no
whole-corpus extraction occurred.

## Candidate Output

| Candidate | Source support | Dependency disposition |
| --- | --- | --- |
| `cc-model-data-constraints` | `support-model-data-constraints` | No candidate-dependent figure, citation, or cross-reference selected |
| `cc-emergent-explanation` | `support-emergent-explanation` | Gear figure directly inspected |
| `cc-pattern-separation` | `support-pattern-separation` | Pattern-separation figure directly inspected; `@Marr71` and Executive Function reference caveated |
| `cc-memory-consolidation` | `support-memory-consolidation` | Citation key identified; cited work and bibliography entry unresolved |

## Lifecycle Summary

All cards have `candidate-requires-operator-review` status. All verification
and reconciliation states are `unassessed`; no preservation decision or memory
admission record exists. Evidence grades are limited to what the inspected
text reports, and extraction-confidence assessments are separately scoped to
the direct extraction act.

## Stop-Condition Check

No stop condition fired. The pinned source was acquired, candidate claims were
locatable, and dependencies were either directly inspected or kept caveated.
The run stopped at the declared four-card scope rather than widening into
bibliography resolution, figure review, or whole-corpus generation.
