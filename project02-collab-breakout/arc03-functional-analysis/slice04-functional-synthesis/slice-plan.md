# Slice 04: Arc03 Functional Synthesis

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice04-functional-synthesis
status: open
opened-on: 2026-08-30
artifact-home: artifacts/
depends-on:
  - slice01-usage-surface-instrument:verified-closed
  - slice02-current-workflow-evaluation:verified-closed
  - slice03-standalone-composition-evaluation:verified-closed
blocks:
  - arc03 close
  - arc04-breakout-architecture
related:
  - ../arc-plan.md
  - ../ledger.md
  - ../slice01-usage-surface-instrument/cdc-verification.md
  - ../slice01-usage-surface-instrument/artifacts/functional-analysis-method.md
  - ../slice01-usage-surface-instrument/artifacts/usage-surface-inventory.md
  - ../slice01-usage-surface-instrument/artifacts/scenario-matrix.md
  - ../slice01-usage-surface-instrument/artifacts/arc03-input-register.md
  - ../slice02-current-workflow-evaluation/cdc-verification.md
  - ../slice02-current-workflow-evaluation/artifacts/current-workflow-evaluation.md
  - ../slice02-current-workflow-evaluation/artifacts/load-path-friction-register.md
  - ../slice02-current-workflow-evaluation/artifacts/functional-deficiency-register.md
  - ../slice02-current-workflow-evaluation/artifacts/source-package-role-language-notes.md
  - ../slice03-standalone-composition-evaluation/cdc-verification.md
  - ../slice03-standalone-composition-evaluation/artifacts/standalone-scenario-evaluation.md
  - ../slice03-standalone-composition-evaluation/artifacts/composition-scenario-evaluation.md
  - ../slice03-standalone-composition-evaluation/artifacts/minimum-load-and-dependency-matrix.md
  - ../slice03-standalone-composition-evaluation/artifacts/component-dependency-adapter-findings.md
  - ../slice03-standalone-composition-evaluation/artifacts/arc03-functional-decision-inputs.md
  - ../../arc02-conceptual-analysis/closing-report.md
  - ../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-conceptual-model.md
  - ../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/boundary-and-naming-findings.md
  - ../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc04-operator-decision-register.md
  - ../../project-plan.md
```

## Goal

Synthesize Arc03's functional-analysis evidence into an Arc04-ready functional
model, scenario coverage assessment, component-fit and risk findings, operator
questions, and close-readiness assessment.

This slice should answer whether Arc03 has enough functional evidence for
Arc04 to design the breakout architecture, and it should identify any
remediation slice needed before Arc03 can close.

## Scope

In scope:

- Consume verified Slice01, Slice02, and Slice03 Arc03 outputs.
- Consume closed Arc02 conceptual-analysis outputs as candidate-boundary
  evidence, not accepted architecture.
- Synthesize usage-surface coverage across S-01 through S-14.
- Compare current monolith, standalone component, composed component, and
  top-level composer load paths.
- Consolidate functional inefficiencies, deficiencies, context-load problems,
  unclear handoffs, routing friction, missing functional goals, and
  source/package or role-language risks.
- Classify candidate component fit as strong, plausible, weak, support asset,
  dependency edge, adapter, constraint, package/release gate, or unresolved
  operator decision.
- Produce Arc04 architecture inputs and operator questions with go / adjust /
  defer posture.
- Assess Arc03 close readiness against the arc ledger and name any remediation
  slice if required.

Out of scope:

- Selecting final component boundaries, names, package paths, or source moves.
- Creating implementation plans; Arc05 owns implementation planning after
  Arc04.
- Closing Arc03; this slice may prepare close-readiness evidence, but formal
  arc close is separate after CDC verifies Slice04.
- Editing source `SKILL.md`, README, Makefile, package files, or generated zip
  artifacts.
- Editing planning artifacts outside Project02.

## Required Artifacts

Produce these durable artifacts under `artifacts/`:

- `arc03-functional-model.md` - the synthesized functional model of how the
  current framework and candidate components work across expected human and
  LLM usage patterns.
- `scenario-coverage-synthesis.md` - coverage of S-01 through S-14, including
  current monolith, standalone, composed, and top-level composer findings.
- `functional-fit-and-risk-synthesis.md` - consolidated functional fit,
  inefficiency, deficiency, context-load, handoff, source/package,
  role-language, and package/release risk findings.
- `arc04-architecture-inputs.md` - Arc04-ready component-fit signals,
  dependency edges, support assets, adapter requirements, constraints,
  package/release gates, and operator questions.
- `arc03-close-readiness.md` - assessment of whether Arc03 is ready for formal
  arc close, including arc-ledger row mapping and remediation-slice verdict.

## Verification Approach

The slice verifies by checking that required artifacts exist under
`artifacts/`, cite verified Arc03 inputs and closed Arc02 evidence, cover all
expected usage surfaces and S-01 through S-14 scenarios, synthesize functional
deficiencies and load-path risks, produce Arc04-ready inputs and operator
questions, assess Arc03 close readiness, carry Project01 source/package
constraints, and remain analytical and non-final.

## Exit Criteria

- Verified Slice01, Slice02, and Slice03 inputs plus closed Arc02 conceptual
  inputs are consumed and cited.
- `artifacts/arc03-functional-model.md` describes the functional model across
  direct source reading, source-clone, packaged skill, skill loading, human
  orientation, session start, planning, execution, review, audit, coverage,
  delegation, contribution, and combination workflows.
- `artifacts/scenario-coverage-synthesis.md` covers S-01 through S-14 and
  distinguishes current monolith, standalone, composed, and top-level composer
  scenarios.
- `artifacts/functional-fit-and-risk-synthesis.md` consolidates
  inefficiencies, deficiencies, context-load problems, unclear handoffs,
  routing friction, missing functional goals, under-served surfaces,
  source/package risks, role-language risks, and package/release risks.
- `artifacts/arc04-architecture-inputs.md` records Arc04-ready component-fit
  signals, strong/plausible/weak direct-load classifications, dependency
  edges, support assets, adapters, constraints, package/release gates,
  operator questions, and go / adjust / defer posture.
- `artifacts/arc03-close-readiness.md` maps Slice04 outputs to Arc03 ledger
  rows A-5 through A-9, states whether a remediation slice is required before
  Arc03 close, and preserves close-readiness evidence for the formal arc close.
- Project01 source/package, package-local, zip root, release surface,
  component contract, CCDP separation, and `make check-package-paths`
  constraints are carried into the synthesis.
- Outputs remain analytical and non-final; final breakout architecture remains
  deferred to Arc04 after Arc03 closes.
- No source files are edited.
