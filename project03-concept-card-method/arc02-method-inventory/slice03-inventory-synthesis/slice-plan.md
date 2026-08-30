# Slice 03: Inventory Synthesis

```yaml
project: project03-concept-card-method
arc: arc02-method-inventory
slice: slice03-inventory-synthesis
status: open
artifact-home: artifacts/
opened-on: 2026-08-30
depends-on:
  - ../slice01-v32-source-inventory/cdc-verification.md
  - ../slice02-v40-gap-analysis/cdc-verification.md
blocks:
  - ../closing-report.md
  - ../../arc03-conceptual-model
```

## Goal

Synthesize the verified v3.2 source inventory and verified v4.0 gap analysis
into the final Arc02 input set: what v3.2 keeps, what v4.0 must change, what
requires operator choice, what remains deferred or out of scope, and what
Arc03 must receive before it defines the v4.0 conceptual model.

## Inputs

- `../slice01-v32-source-inventory/cdc-verification.md`
- `../slice01-v32-source-inventory/artifacts/v32-source-inventory.md`
- `../slice01-v32-source-inventory/artifacts/v32-method-structure-map.md`
- `../slice01-v32-source-inventory/artifacts/v32-original-assessment.md`
- `../slice02-v40-gap-analysis/cdc-verification.md`
- `../slice02-v40-gap-analysis/artifacts/v40-gap-register.md`
- `../slice02-v40-gap-analysis/artifacts/v32-to-v40-carry-forward-change-matrix.md`

## Scope

In scope:

- Produce a concise Arc02 synthesis that composes Slice01 and Slice02 into the
  Arc02 close input.
- Preserve the difference between v3.2 carry-forward material, v4.0
  architectural changes, operator decisions, and deferred work.
- Produce a separate Arc03 input packet naming the conceptual-model constructs
  and open questions that Arc03 must decide.
- Keep the synthesis source-backed by the verified Slice01 and Slice02
  artifacts rather than by memory or redesign.

Out of scope:

- Designing the v4.0 conceptual model.
- Choosing the final skill layout, package behavior, Makefile changes, README
  integration, examples, scripts, or source file locations.
- Editing source files in the implementation checkout.
- Running live concept extraction against a new corpus.
- Reopening the v3.2 inventory or v4.0 gap analysis except to report a
  concrete defect for operator disposition.

## Required Artifacts

Durable synthesis artifacts belong under `artifacts/`:

- `artifacts/arc02-synthesis.md`: Arc02 composition input covering v3.2 keeps,
  v4.0 changes, operator choices, deferrals, and arc-close implications.
- `artifacts/arc03-conceptual-model-inputs.md`: Arc03 handoff packet listing
  candidate constructs, required distinctions, open questions, and boundaries
  that are not final design decisions.

## Verification Approach

The ledger checks are grep-verifiable against the open set and produced
artifacts. CDC will independently reproduce the checks at slice close, confirm
that the synthesis composes the verified Slice01 and Slice02 outputs, and
confirm that conceptual-model and skill-layout design remain deferred.

## Exit Criteria

- The open set exists and names the `artifacts/` home.
- Both required synthesis artifacts exist.
- The synthesis explicitly composes the Slice01 and Slice02 artifacts into
  Arc02 close input.
- The Arc03 handoff names the candidate conceptual-model constructs and open
  questions without deciding the final model.
- Scope fences preserve Arc03, Arc04, and implementation responsibilities.
- The source checkout remains unmodified.

