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

Status: verified-closed on 2026-08-30.

Scope: classify the Arc02 candidate constructs into v4.0 conceptual-model
roles, decide which boundaries are accepted or provisional, preserve open
questions, and route each construct to later Arc03 slices.

Blocks: Slice02.

Durable model outputs belong under the slice-local `artifacts/` directory.

### Slice 02: Evidence and Lifecycle Semantics

Directory: `slice02-evidence-lifecycle`

Status: verified-closed on 2026-08-30.

Scope: define how extraction confidence, source support, evidence grade,
verification state/result, reconciliation state/result, and memory-admission
state relate without flattening them into one confidence field. The slice
also records attachment points and lifecycle-gate decisions for Slice04
model synthesis.

Blocks: Slice03 and Slice04.

Durable model outputs belong under the slice-local `artifacts/` directory.

### Slice 03: Relationship, CQ, and Run Semantics

Directory: `slice03-graph-cq-run-semantics`

Status: verified-closed on 2026-08-30.

Scope: define graph-native relationship/edge semantics, competency-question
coverage semantics, extraction-run traceability, and reconciliation semantics
across cards, claims, relationships, CQs, and runs. The slice consumes
Slice02's reserved lifecycle attachment points and leaves final model
synthesis to Slice04.

Blocks: Slice04.

Durable model outputs belong under the slice-local `artifacts/` directory.

### Slice 04: Model Synthesis and Acceptance

Directory: `slice04-model-synthesis`

Status: verified-closed on 2026-08-30.

Scope: compose the verified construct-boundary, evidence/lifecycle, and
graph/CQ/run slices into the accepted v4.0 conceptual model, record
operator-facing open decisions, and produce the handoff packet for skill
architecture planning.

Blocks: Arc03 close and Arc04.

Durable model outputs belong under the slice-local `artifacts/` directory.

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

### v1.1 - 2026-08-30

Slice01 marked verified-closed after CDC reproduced all seven slice ledger
rows. Slice02 planning can proceed against the existing Arc03 sequence; the
bubble-up clarifies that Slice02 should focus on the lifecycle stack for
confidence, source support, evidence grade, verification state,
reconciliation state, and memory admission.

### v1.2 - 2026-08-30

Slice02 opened for evidence and lifecycle semantics. The slice is scoped to
the conceptual separation of extraction confidence, source support, evidence
grade, verification result/state, reconciliation result/state, and memory
admission, while final schema, graph/CQ/run semantics, skill architecture,
package behavior, and source edits remain deferred.

### v1.3 - 2026-08-30

Slice02 marked verified-closed after CDC reproduced all seven slice ledger
rows. Slice03 can now be planned against the reserved lifecycle attachment
points for reconciliation state/result, extraction run, relationship/edge,
and competency-question semantics; no arc sequencing change was required.

### v1.4 - 2026-08-30

Slice03 opened for relationship, competency-question, extraction-run, and
reconciliation semantics. The slice is scoped to graph/CQ/run conceptual
modeling only; final model synthesis, skill architecture, package behavior,
implementation algorithms, and source edits remain deferred.

### v1.5 - 2026-08-30

Slice03 marked verified-closed after CDC reproduced all eight slice ledger
rows. Slice04 can now be planned to synthesize construct boundaries, evidence
and lifecycle semantics, graph/CQ/run semantics, and remaining provisional
decisions into the accepted v4.0 conceptual model; no arc sequencing change
was required.

### v1.6 - 2026-08-30

Slice04 opened for model synthesis and acceptance. The slice is scoped to
Arc03 conceptual-model composition, decision registration, and Arc04 handoff
input while leaving final skill architecture, package behavior, validator
implementation, README integration, and source edits to later arcs.

### v1.7 - 2026-08-30

Slice04 marked verified-closed after CDC reproduced all eight slice ledger
rows. Arc03 is ready for formal arc close and arc-scale composition
verification; no new Arc03 slice, scope change, or sequencing change was
required.
