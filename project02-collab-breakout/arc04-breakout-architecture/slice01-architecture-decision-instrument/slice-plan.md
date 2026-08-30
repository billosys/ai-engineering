# Slice 01: Architecture Decision Instrument

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice01-architecture-decision-instrument
status: open
opened-on: 2026-08-30
artifact-home: artifacts/
depends-on:
  - ../arc-plan.md
  - ../../arc02-conceptual-analysis:closed
  - ../../arc03-functional-analysis:closed
blocks:
  - slice02-component-contract-evaluation
related:
  - ../../project-plan.md
  - ../../ledger.md
  - ../arc-plan.md
  - ../ledger.md
  - ../../arc02-conceptual-analysis/closing-report.md
  - ../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-conceptual-model.md
  - ../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/boundary-and-naming-findings.md
  - ../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc04-operator-decision-register.md
  - ../../arc03-functional-analysis/closing-report.md
  - ../../arc03-functional-analysis/slice04-functional-synthesis/artifacts/arc03-functional-model.md
  - ../../arc03-functional-analysis/slice04-functional-synthesis/artifacts/scenario-coverage-synthesis.md
  - ../../arc03-functional-analysis/slice04-functional-synthesis/artifacts/functional-fit-and-risk-synthesis.md
  - ../../arc03-functional-analysis/slice04-functional-synthesis/artifacts/arc04-architecture-inputs.md
  - ../../arc03-functional-analysis/slice04-functional-synthesis/artifacts/arc03-close-readiness.md
```

## Goal

Create the decision instrument Arc04 will use to turn the closed conceptual
and functional analyses into an operator-accepted breakout architecture.

This slice should define the architecture method, input register,
component-contract schema, candidate worklist, operator-decision worklist, and
risk/gate register. It should make later architecture choices falsifiable
without making those choices yet.

## Scope

In scope:

- Consume closed Arc02 conceptual-analysis evidence and closed Arc03
  functional-analysis evidence.
- Preserve the operator-provided soft layout sketch only as low-weight
  hypothesis evidence.
- Define the decision method Arc04 will use for component, family, support
  asset, adapter, constraint, package/release gate, and non-component
  classifications.
- Define the component-contract schema later slices must fill.
- Seed the candidate architecture worklist from Arc02 and Arc03 evidence.
- Carry forward operator decisions, operator questions, risks, and Project01
  path/package gates.
- Preserve go / adjust / defer posture for candidates whose final disposition
  belongs to later Arc04 slices.

Out of scope:

- Accepting final component boundaries, component names, package paths, source
  moves, or source/package layout.
- Producing the final target architecture.
- Producing the Arc05 implementation plan.
- Editing source `SKILL.md`, README, Makefile, framework docs, templates,
  package files, generated zip artifacts, or any source file.
- Editing planning artifacts outside Project02.

## Required Artifacts

Produce these durable artifacts under `artifacts/`:

- `architecture-input-register.md` - the closed Arc02/Arc03 evidence register
  for Arc04, including input role and source/package constraints.
- `architecture-decision-method.md` - the decision rubric, classification
  vocabulary, evidence grades, and go / adjust / defer rules for Arc04.
- `component-contract-schema.md` - the required fields for every candidate
  component contract, including dependency, support asset, adapter,
  source/package, release gate, and maintenance fields.
- `candidate-architecture-worklist.md` - the seeded candidate list for Slice02
  evaluation, preserving component, family, support asset, adapter,
  constraint, package/release gate, and deferred/non-component categories.
- `operator-decision-and-risk-register.md` - the D/OQ decisions, risks, gates,
  and acceptance questions that Arc04 must disposition before close.

## Verification Approach

The slice verifies by checking that required artifacts exist under
`artifacts/`, cite closed Arc02 and Arc03 evidence, define a decision method
and component-contract schema, seed the candidate worklist, carry operator
decisions and risks forward, preserve Project01 path/package gates, remain
non-final, and leave the implementation source checkout untouched.

## Exit Criteria

- Closed Arc02 and Arc03 inputs are consumed and cited as inputs.
- `artifacts/architecture-decision-method.md` defines the classification
  vocabulary and decision rubric for Arc04.
- `artifacts/component-contract-schema.md` defines mandatory contract fields
  for component names, purposes, boundaries, dependencies, wayfinding,
  support assets, adapters, source/package behavior, package paths, release
  gates, and maintenance ownership.
- `artifacts/candidate-architecture-worklist.md` seeds later evaluation with
  all major candidates, component families, support assets, adapters,
  constraints, package/release gates, and deferred/non-component concepts
  carried from Arc02 and Arc03.
- `artifacts/operator-decision-and-risk-register.md` carries D-01 through
  D-12 and OQ-01 through OQ-09, or explicitly explains any merged decision
  rows.
- Project01 source/package, package-local, zip root, release surface,
  component contract, CCDP separation, and `make check-package-paths`
  constraints are carried forward.
- Outputs remain a decision instrument, not accepted architecture.
- No source files are edited.
