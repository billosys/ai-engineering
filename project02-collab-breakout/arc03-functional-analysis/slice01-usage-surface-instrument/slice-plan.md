# Slice 01: Usage Surface Instrument

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice01-usage-surface-instrument
status: open
opened-on: 2026-08-30
artifact-home: artifacts/
depends-on:
  - arc02-conceptual-analysis:closed-composed
blocks:
  - slice02-current-workflow-evaluation
related:
  - ../arc-plan.md
  - ../ledger.md
  - ../../project-plan.md
  - ../../ledger.md
  - ../../arc02-conceptual-analysis/closing-report.md
  - ../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-conceptual-model.md
  - ../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/boundary-and-naming-findings.md
  - ../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc04-operator-decision-register.md
  - ../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-close-readiness.md
```

## Goal

Create Arc03's functional-analysis instrument: the method, usage-surface
inventory, and scenario matrix that later slices will apply to the current
framework and candidate component set.

This slice should transform the closed Arc02 conceptual model into functional
questions. It should define what counts as a usage surface, a load path, a
minimum useful load set, a context-cost signal, a routing failure, a packaging
failure, and a successful standalone or composed component scenario.

## Scope

In scope:

- Consume Arc02 close evidence and required Arc02 synthesis artifacts.
- Define the Arc03 functional-analysis method, vocabulary, evidence grades,
  and scenario-evaluation fields.
- Inventory expected usage surfaces for humans and LLMs, including direct
  source-clone reading, packaged skill reading, LLM skill loading, human
  orientation, session start, planning, execution, review, slice close, arc
  close, audit, coverage, delegation, upstream contribution, and combinations
  of two or more components.
- Build a scenario matrix that later slices can apply to the current monolith
  and to candidate standalone/composed components.
- Carry Arc02 conceptual risks and operator-decision questions forward as
  functional questions where they need usage evidence.
- Carry Project01 source/package constraints forward as functional test
  surfaces and package/release gates.
- Keep all outputs analytical and non-final; final architecture remains
  deferred to Arc04 after Arc03 closes.

Out of scope:

- Evaluating every scenario against the current monolithic framework.
- Selecting final component boundaries or package paths.
- Creating source files, new skills, README changes, Makefile/package changes,
  package exceptions, or generated zip artifacts.
- Editing planning artifacts outside Project02.

## Required Artifacts

Produce these durable artifacts under `artifacts/`:

- `functional-analysis-method.md` - Arc03 method, vocabulary, evidence grades,
  and scenario-evaluation fields.
- `usage-surface-inventory.md` - inventory of human and LLM usage surfaces,
  entrypoints, load paths, expected success signals, and likely failure modes.
- `scenario-matrix.md` - scenario rows to be applied by later slices,
  including current-monolith, standalone-component, composed-component,
  source/package, and role-language scenarios.
- `arc03-input-register.md` - explicit record of the Arc02 inputs, Project01
  constraints, and functional questions carried forward into Arc03.

## Verification Approach

The slice verifies by checking that the required artifacts exist under
`artifacts/`, cite the closed Arc02 inputs, define the functional-analysis
method and scenario fields, cover the expected usage surfaces, carry Project01
path/package constraints, preserve non-final architecture posture, and leave
the implementation source checkout unchanged.

## Exit Criteria

- Arc02 close evidence and required Arc02 synthesis artifacts are consumed and
  cited.
- `artifacts/functional-analysis-method.md` defines usage surface, load path,
  entrypoint, trigger, actor, minimum useful load set, dependency order,
  context cost, routing friction, functional deficiency, source/package mode,
  role-language clarity, evidence grade, and non-final posture.
- `artifacts/usage-surface-inventory.md` covers direct source-clone reading,
  packaged skill reading, LLM skill loading, human orientation, session start,
  planning, execution, review, slice close, arc close, audit, coverage,
  delegation, contribution, standalone use, and composed use.
- `artifacts/scenario-matrix.md` records scenario rows with actor, entrypoint,
  trigger, inputs, expected outcome, load set, dependencies, friction signals,
  evidence to collect, and downstream owner.
- `artifacts/arc03-input-register.md` carries Arc02 conceptual risks, Arc04
  operator decisions, and Project01 path/package constraints forward as
  functional-analysis inputs.
- Outputs remain analytical and non-final; final architecture remains deferred
  to Arc04 after Arc03 functional analysis and operator acceptance.
- No source files are edited.
