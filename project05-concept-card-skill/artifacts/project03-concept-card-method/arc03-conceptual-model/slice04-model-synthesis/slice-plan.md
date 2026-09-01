# Slice 04: Model Synthesis and Acceptance

```yaml
project: project03-concept-card-method
arc: arc03-conceptual-model
slice: slice04-model-synthesis
status: open
opened: 2026-08-30
artifact-home: artifacts/
depends-on:
  - ../slice01-construct-boundaries/cdc-verification.md
  - ../slice02-evidence-lifecycle/cdc-verification.md
  - ../slice03-graph-cq-run-semantics/cdc-verification.md
blocks:
  - arc03 formal close
  - ../arc04-skill-architecture
```

## Capability

Slice04 composes the verified Arc03 conceptual-model slices into the accepted
v4.0 conceptual model for the concept-card method. It resolves the model
decisions that can be accepted now, records provisional and deferred decisions
for later arcs, and prepares the Arc04 skill-architecture handoff without
choosing final skill layout or implementation mechanics.

## Required Reading

- `../slice01-construct-boundaries/artifacts/v40-construct-boundary-model.md`
- `../slice01-construct-boundaries/artifacts/v40-construct-decision-register.md`
- `../slice01-construct-boundaries/cdc-verification.md`
- `../slice02-evidence-lifecycle/artifacts/v40-evidence-lifecycle-model.md`
- `../slice02-evidence-lifecycle/artifacts/v40-evidence-state-decision-register.md`
- `../slice02-evidence-lifecycle/cdc-verification.md`
- `../slice03-graph-cq-run-semantics/artifacts/v40-graph-cq-run-semantics.md`
- `../slice03-graph-cq-run-semantics/artifacts/v40-reconciliation-traceability-decision-register.md`
- `../slice03-graph-cq-run-semantics/cdc-verification.md`
- `../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc03-conceptual-model-inputs.md`
- `../../arc02-method-inventory/closing-report.md`
- `../arc-plan.md`
- `../ledger.md`

## In Scope

- Compose an accepted v4.0 conceptual model across concept cards, claims,
  source spans/source support, evidence grades, relationships/edges,
  competency questions, extraction runs, verifiers, validation results,
  reconciliation states/results, and memory admission.
- Preserve the model boundaries established in prior Arc03 slices, including
  the separation between extraction confidence, source support, evidence
  grade, verification state/result, reconciliation state/result, and memory
  admission.
- State conceptual invariants and lifecycle flow for card creation,
  validation, reconciliation, verification, and memory-admission readiness.
- Record accepted, provisional, deferred, and out-of-scope decisions with
  rationale and downstream routing.
- Produce a handoff packet for Arc04 that names the skill-architecture inputs
  without selecting final `SKILL.md`, guide, template, script, package, or
  README layout.
- Leave concise Arc03 close input so the parent arc can be closed by
  composition, not by inheriting child closure.

## Out of Scope

- Editing source `SKILL.md`, `README.md`, `Makefile`, packaged skill lists,
  source concept-card docs, framework docs, or generated zips.
- Choosing final skill layout, package behavior, README integration, or exact
  guide/template names.
- Defining exact schema syntax, exact enum spelling, deterministic validator
  implementation, graph database/index behavior, GraphRAG runtime, memory
  runtime, ontology database, CCDP service, or live extraction behavior.
- Running a new extraction/re-extraction corpus.
- Closing Arc03; this slice produces the inputs needed for a later arc close
  pass and CDC verification.

## Required Artifacts

- `artifacts/v40-conceptual-model.md`
- `artifacts/v40-model-decision-register.md`
- `artifacts/arc04-skill-architecture-handoff.md`

## Done When

- The required artifacts exist under `artifacts/`.
- The conceptual model integrates the verified Slice01, Slice02, and Slice03
  outputs into one coherent v4.0 model.
- The decision register clearly separates accepted, provisional, deferred, and
  out-of-scope decisions.
- The Arc04 handoff identifies architecture inputs without making architecture
  decisions that belong to Arc04.
- The source checkout remains clean.
- Slice close remains proposed-done until independent CDC verification records
  the reproduced ledger evidence.
