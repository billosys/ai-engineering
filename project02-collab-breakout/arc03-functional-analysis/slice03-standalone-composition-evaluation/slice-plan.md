# Slice 03: Standalone And Composition Scenario Evaluation

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice03-standalone-composition-evaluation
status: proposed-done
opened-on: 2026-08-30
proposed-done-on: 2026-08-30
artifact-home: artifacts/
depends-on:
  - slice01-usage-surface-instrument:verified-closed
  - slice02-current-workflow-evaluation:verified-closed
blocks:
  - slice04-functional-synthesis
related:
  - ../arc-plan.md
  - ../ledger.md
  - ../slice01-usage-surface-instrument/cdc-verification.md
  - ../slice01-usage-surface-instrument/artifacts/functional-analysis-method.md
  - ../slice01-usage-surface-instrument/artifacts/scenario-matrix.md
  - ../slice02-current-workflow-evaluation/cdc-verification.md
  - ../slice02-current-workflow-evaluation/artifacts/current-workflow-evaluation.md
  - ../slice02-current-workflow-evaluation/artifacts/load-path-friction-register.md
  - ../slice02-current-workflow-evaluation/artifacts/functional-deficiency-register.md
  - ../slice02-current-workflow-evaluation/artifacts/source-package-role-language-notes.md
  - ../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-conceptual-model.md
  - ../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/boundary-and-naming-findings.md
  - ../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc04-operator-decision-register.md
  - ../../project-plan.md
```

## Goal

Evaluate candidate standalone and composed component usage scenarios against
the current-monolith baseline from Slice02.

This slice should test whether candidate components have real direct load
moments, whether composed use reduces or increases context cost, which
dependency edges are functionally required, which support assets must travel
with their owning components, and where role-language or source/package adapter
behavior must be preserved for standalone use.

## Scope

In scope:

- Consume Slice01's functional-analysis method and scenario matrix.
- Consume Slice02's verified current-workflow evaluation, load-path friction
  register, functional-deficiency register, and source/package role-language
  notes as the current-monolith baseline.
- Consume Arc02's conceptual model, boundary and naming findings, and operator
  decision register as candidate-boundary evidence, not accepted architecture.
- Evaluate standalone component scenarios S-08 through S-11 from the scenario
  matrix.
- Evaluate composed component scenarios S-12 through S-14 from the scenario
  matrix.
- Compare current monolith, standalone, and composed load sets for context
  cost, over-rich and over-thin paths, dependency order, support-asset travel,
  role-language clarity, source/package behavior, and package/release gates.
- Identify candidate concepts that lack a real functional load path or should
  remain dependency edges, adapters, support assets, constraints, or
  package/release gates.
- Produce Slice04-ready findings and Arc04 decision inputs without accepting
  final component names, source moves, package paths, or architecture.

Out of scope:

- Selecting final component boundaries, names, package paths, or source moves.
- Creating or editing source `SKILL.md`, README, Makefile, package, or zip
  artifacts.
- Producing implementation plans; Arc05 owns implementation planning after
  Arc04 architecture.
- Closing Arc03; Slice04 owns functional synthesis and arc close readiness.
- Editing planning artifacts outside Project02.

## Required Artifacts

Produce these durable artifacts under `artifacts/`:

- `standalone-scenario-evaluation.md` - scenario-by-scenario evaluation of
  standalone component usage, especially S-08 through S-11.
- `composition-scenario-evaluation.md` - scenario-by-scenario evaluation of
  composed component usage, especially S-12 through S-14.
- `minimum-load-and-dependency-matrix.md` - comparative matrix of current
  monolith, standalone, and composed load sets, including context cost,
  dependency order, and over-rich/over-thin risk.
- `component-dependency-adapter-findings.md` - findings on component-family
  behavior, dependency edges, support-asset travel, role-language adapters,
  source/package constraints, and package/release gates.
- `arc03-functional-decision-inputs.md` - Slice04 and Arc04 inputs, including
  functional fit signals, concepts lacking direct load paths, unresolved
  operator questions, and go / adjust / defer posture.

## Verification Approach

The slice verifies by checking that the artifacts exist under `artifacts/`,
cite the verified Slice01/Slice02 and Arc02 inputs, evaluate standalone and
composed scenario rows from the scenario matrix, compare current monolith
against candidate standalone/composed load paths, identify dependency and
adapter findings, preserve Project01 source/package constraints, and remain
analytical and non-final.

## Exit Criteria

- Slice01 and Slice02 verified inputs plus Arc02 conceptual inputs are consumed
  and cited.
- `artifacts/standalone-scenario-evaluation.md` evaluates S-08 through S-11
  and records actor, entrypoint, trigger, inputs, expected outcome, load set,
  dependencies, friction signals, evidence collected, and downstream owner.
- Standalone evaluation covers coverage hardening, delegation policy,
  contribution guidance, posture/methodology, PM, ledger, audit, agent-adapter,
  and ontology-critique load moments where relevant.
- `artifacts/composition-scenario-evaluation.md` evaluates S-12 through S-14
  and records PM+ledger, top-level composer, role-language adapter, and other
  necessary composed flows.
- `artifacts/minimum-load-and-dependency-matrix.md` compares current monolith,
  standalone, and composed paths for context cost, dependency order, over-rich
  and over-thin behavior, minimum useful load, and Slice02 LPF/FD baselines.
- `artifacts/component-dependency-adapter-findings.md` records dependency
  direction, component-family behavior, support-asset travel, role-language
  clarity, source/package constraints, package-local links, zip roots, release
  surfaces, `make check-package-paths`, and package/release gates.
- `artifacts/arc03-functional-decision-inputs.md` preserves non-final posture,
  identifies concepts lacking real functional load paths, routes findings to
  Slice04, Arc04, or Arc05, and records go / adjust / defer signals without
  accepting final architecture.
- No source files are edited.

## Proposed Close Summary

Proposed done by CC on 2026-08-30. The slice produced all five required
durable artifacts under `artifacts/`, updated the slice ledger with attested
evidence, and wrote `closing-report.md`.

No source files were edited. No Arc03 plan change is required before Slice04
opens; the existing Slice04 placeholder already owns Arc03 functional
synthesis, Arc04 architecture inputs, and close-readiness.
