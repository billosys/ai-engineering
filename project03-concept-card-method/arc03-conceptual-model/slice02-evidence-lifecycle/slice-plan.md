# Slice 02: Evidence and Lifecycle Semantics

```yaml
project: project03-concept-card-method
arc: arc03-conceptual-model
slice: slice02-evidence-lifecycle
status: open
artifact-home: artifacts/
opened-on: 2026-08-30
```

## Goal

Define the v4.0 evidence and lifecycle semantics for the concept-card method.
The slice separates the overloaded v3.2 confidence field into distinct method
concerns: extraction confidence, source support, evidence grade, verification
state/result, reconciliation state/result, and memory admission.

The output is conceptual-model material for Arc03. It should be precise enough
for later synthesis, but it must not choose final schema syntax, package
layout, deterministic validator implementation, or source edits.

## Inputs

- `../slice01-construct-boundaries/cdc-verification.md`
- `../slice01-construct-boundaries/artifacts/v40-construct-boundary-model.md`
- `../slice01-construct-boundaries/artifacts/v40-construct-decision-register.md`
- `../../arc02-method-inventory/closing-report.md`
- `../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc02-synthesis.md`
- `../../arc02-method-inventory/slice03-inventory-synthesis/artifacts/arc03-conceptual-model-inputs.md`

## In Scope

- Define the conceptual differences between extraction confidence, source
  support, evidence grade, verification state, verification result,
  reconciliation state, reconciliation result, and memory admission.
- Decide where each concern attaches: concept card, claim, source span,
  claim-source support relationship, extraction run, verifier role, result
  record, or lifecycle gate.
- Define the lifecycle flow from extracted candidate to durable semantic
  memory candidate, including what may advance before verification and what
  must wait for reconciliation or human/operator acceptance.
- Preserve v3.2 carry-forward strengths: source-faithful synthesis,
  provenance, confidence signalling, validation checks, re-extraction
  discipline, and preservation of unique prior-card value.
- Record accepted, provisional, deferred, and open decisions for Slice04 model
  synthesis and later implementation planning.

## Out of Scope

- Final schema syntax, exact enum spelling, YAML template shape, validator
  language, deterministic scripts, package behavior, README integration,
  Makefile changes, generated zips, or source edits.
- Relationship or edge semantics except where evidence attachment points must
  be reserved for Slice03.
- Competency-question semantics except where verification or memory admission
  depends on CQ coverage.
- Extraction-run trace schema except where lifecycle evidence must reference
  an extraction run or verification/reconciliation result.
- Reconciliation algorithms, graph databases, GraphRAG runtime, memory
  runtime, ontology database, or CCDP service design.

## Required Artifacts

Durable artifacts belong under `artifacts/`:

- `artifacts/v40-evidence-lifecycle-model.md` - conceptual model for the
  distinct evidence/lifecycle concerns, their attachment points, and their
  lifecycle flow.
- `artifacts/v40-evidence-state-decision-register.md` - decision register for
  state/grade/result constructs, including rationale, dependencies, status,
  downstream routing, and open questions.

## Verification Approach

The slice ledger uses grep-verifiable rows for artifact existence, conceptual
separation, attachment-point coverage, lifecycle routing, scope fences, and
source-checkout cleanliness. CC should update the ledger with attested
evidence and write a closing report. CDC will independently reproduce the
ledger rows before the slice can be treated as closed.

## Exit Criteria

- The two required artifacts exist under `artifacts/`.
- The lifecycle model explicitly separates extraction confidence, source
  support, evidence grade, verification state/result, reconciliation
  state/result, and memory admission.
- The model identifies attachment points for the relevant constructs rather
  than flattening all status into the card or one confidence field.
- The decision register records accepted/provisional/deferred status,
  rationale, dependencies, open questions, and downstream routing.
- Later work remains fenced: schema syntax, final enum spelling, graph/CQ/run
  semantics, skill architecture, package behavior, and source edits are not
  performed in this slice.
- The source checkout remains clean.
