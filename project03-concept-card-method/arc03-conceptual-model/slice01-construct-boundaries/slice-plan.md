# Slice 01: Construct Boundaries

```yaml
project: project03-concept-card-method
arc: arc03-conceptual-model
slice: slice01-construct-boundaries
status: open
artifact-home: artifacts/
opened-on: 2026-08-30
depends-on:
  - ../../arc02-method-inventory/closing-report.md
  - ../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc03-conceptual-model-inputs.md
blocks:
  - ../slice02-evidence-lifecycle
```

## Goal

Define the first-pass v4.0 construct boundaries for the concept-card method:
which Arc02 candidate constructs are first-class concepts, which are fields,
statuses, roles, processes, or records, which remain provisional, and which
questions later Arc03 slices must settle.

## Inputs

- `../../arc02-method-inventory/closing-report.md`
- `../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc02-synthesis.md`
- `../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc03-conceptual-model-inputs.md`
- `../../arc02-method-inventory/slice02-v40-gap-analysis/artifacts/v40-gap-register.md`
- `../../arc02-method-inventory/slice02-v40-gap-analysis/artifacts/v32-to-v40-carry-forward-change-matrix.md`

## Scope

In scope:

- Classify each Arc02 candidate construct: concept card, claim, source span,
  evidence grade, relationship or edge, competency question, extraction run,
  verifier, reconciliation, and memory admission.
- Identify whether each construct is a first-class entity, value object,
  status, role, process, result record, field, or deferred concern.
- Record rationale, dependencies, open questions, and the later Arc03 slice
  that should resolve any remaining uncertainty.
- Preserve v3.2 carry-forward commitments, especially card atomicity,
  source-faithful synthesis, provenance, typed relationships, competency
  questions, source-primary re-extraction, and preservation.

Out of scope:

- Finalizing evidence-grade vocabulary, verification-state transitions,
  reconciliation algorithms, memory-admission policy, schema syntax, skill
  layout, package behavior, deterministic validator scripts, README changes,
  Makefile changes, or source edits.
- Designing the final v4.0 card template.
- Running live concept extraction.

## Required Artifacts

Durable construct-boundary artifacts belong under `artifacts/`:

- `artifacts/v40-construct-boundary-model.md`: first-pass construct boundary
  model, source-backed by Arc02 inputs and explicit about provisional areas.
- `artifacts/v40-construct-decision-register.md`: per-construct decision table
  listing classification, rationale, dependencies, open questions, and
  downstream Arc03 routing.

## Verification Approach

The ledger checks are grep-verifiable against the slice open set and produced
artifacts. CDC will independently reproduce the checks at slice close, confirm
that all Arc02 candidate constructs are covered, and confirm that later-arc
responsibilities remain deferred.

## Exit Criteria

- The open set exists and names the `artifacts/` home.
- Both required construct-boundary artifacts exist.
- All Arc02 candidate constructs are classified.
- The decision register records rationale, dependencies, open questions, and
  downstream routing for later Arc03 slices.
- The artifacts preserve v3.2 carry-forward commitments while framing v4.0
  changes as conceptual-model decisions.
- Later-arc and source-edit scope fences remain explicit.
- The source checkout remains unmodified.

