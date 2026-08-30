# Slice 02: Current Workflow Evaluation

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice02-current-workflow-evaluation
status: proposed-done
opened-on: 2026-08-30
proposed-done-on: 2026-08-30
artifact-home: artifacts/
depends-on:
  - slice01-usage-surface-instrument:verified-closed
blocks:
  - slice03-standalone-composition-evaluation
related:
  - ../arc-plan.md
  - ../ledger.md
  - ../slice01-usage-surface-instrument/cdc-verification.md
  - ../slice01-usage-surface-instrument/artifacts/functional-analysis-method.md
  - ../slice01-usage-surface-instrument/artifacts/usage-surface-inventory.md
  - ../slice01-usage-surface-instrument/artifacts/scenario-matrix.md
  - ../slice01-usage-surface-instrument/artifacts/arc03-input-register.md
  - ../../arc02-conceptual-analysis/closing-report.md
  - ../../project-plan.md
```

## Goal

Evaluate how the current monolithic collaboration framework functions for the
usage surfaces and current-workflow scenarios defined by Slice01.

This slice should use the Slice01 method and scenario matrix to observe the
current framework as it exists today: its source-clone reading behavior,
packaged-skill reading behavior, LLM skill-loading path, session-start path,
planning path, execution/review/close path, audit path, coverage path,
delegation path, contribution path, source/package path behavior, and
role-language clarity.

## Scope

In scope:

- Consume Slice01's verified functional-analysis method, usage-surface
  inventory, scenario matrix, input register, and CDC verification.
- Evaluate the current monolithic framework against current-workflow scenarios,
  especially S-01 through S-07 from the Slice01 scenario matrix.
- Inspect current source files as read-only grounding for the workflow
  evaluation, including README, top-level `SKILL.md`, project-management
  docs, ledger discipline, audit, coverage, delegation, contribution style,
  contribution template, Make/package guidance, and CCDP contrast where needed.
- Record current load sets, dependency ordering, context-cost signals, routing
  friction, unclear handoffs, source/package behavior, role-language clarity,
  and missing functional goals.
- Produce friction and deficiency registers that later slices can compare
  against standalone and composed component scenarios.
- Carry Project01 source/package constraints forward as functional test
  surfaces and package/release gates.
- Keep outputs analytical and non-final; final architecture remains deferred
  to Arc04 after Arc03 closes.

Out of scope:

- Evaluating proposed standalone or composed component designs reserved for
  Slice03.
- Selecting final component boundaries, names, package paths, or source moves.
- Creating source files, new skills, README changes, Makefile/package changes,
  package exceptions, or generated zip artifacts.
- Editing planning artifacts outside Project02.

## Required Artifacts

Produce these durable artifacts under `artifacts/`:

- `current-workflow-evaluation.md` - scenario-by-scenario evaluation of the
  current monolithic framework against Slice01 current-workflow rows.
- `load-path-friction-register.md` - observed routing, load-set, context-cost,
  dependency-order, handoff, support-asset, and discoverability friction.
- `functional-deficiency-register.md` - functional gaps, under-served usage
  surfaces, missing entrypoints, over/under-loaded paths, and workflow failures
  to carry into Slice03/Slice04/Arc04.
- `source-package-role-language-notes.md` - focused notes on source/package
  mode behavior, package-local/zip/release surfaces, CCDP contrast, and
  CDC/CC/Claude/Codex/operator role-language clarity in the current monolith.

## Verification Approach

The slice verifies by checking that required artifacts exist under
`artifacts/`, cite Slice01 and Arc02 inputs, evaluate the current-workflow
scenario rows, cover expected current source surfaces, record friction and
deficiencies in the Slice01 vocabulary, carry Project01 path/package
constraints, preserve non-final architecture posture, and leave the
implementation source checkout unchanged.

## Exit Criteria

- Slice01's method, usage-surface inventory, scenario matrix, input register,
  and CDC verification are consumed and cited.
- `artifacts/current-workflow-evaluation.md` evaluates current-monolith
  scenarios S-01 through S-07 and records actor, entrypoint, trigger, inputs,
  expected outcome, load set, dependencies, friction signals, evidence
  collected, and downstream owner for each.
- The current workflow evaluation covers README/source-clone, packaged skill,
  LLM skill loading, session start, planning, execution, review, slice close,
  arc close, audit, coverage, delegation, contribution, source/package, and
  role-language surfaces.
- `artifacts/load-path-friction-register.md` records routing friction,
  context cost, dependency-order friction, unclear handoffs, support-asset
  discovery, source/package ambiguity, and role-language clarity issues.
- `artifacts/functional-deficiency-register.md` records functional
  deficiencies, missing functional goals, under-served surfaces, over-rich or
  over-thin load paths, hidden dependencies, output-location conflicts,
  inherited-composition risks, and underfit/overfit current behavior.
- `artifacts/source-package-role-language-notes.md` records Project01
  source/package, package-local, zip, release surface, CCDP contrast,
  `make check-package-paths`, component contract, package/release gate, and
  role-language clarity findings.
- Outputs remain analytical and non-final; final architecture remains deferred
  to Arc04 after Arc03 functional analysis and operator acceptance.
- No source files are edited.
