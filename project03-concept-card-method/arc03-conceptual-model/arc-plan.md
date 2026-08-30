# Arc 03: Conceptual Model

```yaml
project: project03-concept-card-method
arc: arc03-conceptual-model
status: active
depends-on:
  - ../arc02-method-inventory/closing-report.md
blocks:
  - ../arc04-skill-architecture
related:
  - ../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc02-synthesis.md
  - ../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc03-conceptual-model-inputs.md
```

## Capability

Arc03 defines the v4.0 conceptual model for the concept-card method. It turns
the Arc02 inventory and gap analysis into a bounded ontology of cards, claims,
source spans, evidence grades, relationships, competency questions, extraction
runs, verifier roles, reconciliation, and memory admission.

The arc does not choose the final skill layout, package behavior, deterministic
validator implementation, README integration, or source edits. Those remain
later-arc responsibilities.

## Slice Breakdown

### Slice 01: Construct Boundaries

Directory: `slice01-construct-boundaries`

Status: open.

Scope: classify the Arc02 candidate constructs into v4.0 conceptual-model
roles, decide which boundaries are accepted or provisional, preserve open
questions, and route each construct to later Arc03 slices.

Blocks: Slice02.

Durable model outputs belong under the slice-local `artifacts/` directory.

### Slice 02: Evidence and Lifecycle Semantics

Directory: `slice02-evidence-lifecycle`

Status: placeholder.

Expected scope: define how extraction confidence, source support, evidence
grade, verification state, reconciliation state, and memory-admission state
relate without flattening them into one confidence field.

Detailed planning is deferred until Slice01 closes.

### Slice 03: Relationship, CQ, and Run Semantics

Directory: `slice03-graph-cq-run-semantics`

Status: placeholder.

Expected scope: define graph-native relationship/edge semantics, competency
question coverage semantics, extraction-run traceability, and how
reconciliation operates across cards, claims, relationships, and runs.

Detailed planning is deferred until Slice02 closes.

### Slice 04: Model Synthesis and Acceptance

Directory: `slice04-model-synthesis`

Status: placeholder.

Expected scope: compose the prior slices into the accepted v4.0 conceptual
model, record operator-facing open decisions, and produce the handoff packet
for skill architecture planning.

Detailed planning is deferred until Slice03 closes.

## Dependencies

Consumes:

- Closed Arc02 method inventory and gap analysis.
- The Arc02 synthesis and Arc03 conceptual-model input packet.
- Project03's v4.0 target framing.

Leaves for later arcs:

- An accepted v4.0 conceptual model for the concept-card method.
- Explicit boundaries between conceptual model, skill architecture, and
  implementation mechanics.
- Inputs for planning the loadable knowledge skill without prematurely
  choosing file layout or package behavior.

## Version History

### v1.0 - 2026-08-30

Arc03 opened after Arc02 formal close. The arc is scoped to conceptual-model
definition only; skill architecture and implementation planning remain
deferred to later arcs.

