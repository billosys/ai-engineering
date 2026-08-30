# Slice 03: Arc 01 Synthesis

```yaml
project: project02-collab-breakout
arc: arc01-framework-inventory
slice: slice03-arc01-synthesis
status: verified-closed
proposed-done-on: 2026-08-30
verified-closed-on: 2026-08-30
artifact-home: artifacts/
depends-on:
  - slice01-source-inventory:verified-closed
  - slice02-problem-solution-map:verified-closed
blocks:
  - arc02-conceptual-analysis
related:
  - ../slice01-source-inventory/cdc-verification.md
  - ../slice01-source-inventory/artifacts/framework-source-inventory.md
  - ../slice01-source-inventory/artifacts/source-to-concept-map.md
  - ../slice01-source-inventory/artifacts/project01-path-contract-notes.md
  - ../slice02-problem-solution-map/cdc-verification.md
  - ../slice02-problem-solution-map/artifacts/problem-solution-map.md
  - ../slice02-problem-solution-map/artifacts/mechanism-coverage-matrix.md
  - ../slice02-problem-solution-map/artifacts/problem-solution-findings.md
```

## Goal

Synthesize Arc 01 into a compact, source-backed handoff for Arc 02 conceptual
analysis.

This slice should turn the verified source inventory and problem-solution map
into explicit Arc 02 inputs: current component clusters, candidate component
boundaries, suspected mislabels, suspected improper merges and splits,
cross-cutting constraints, package/path constraints inherited from Project01,
and operator questions that must be answered before component boundaries are
selected.

## Scope

In scope:

- Consume verified Slice 01 and Slice 02 close evidence and artifacts.
- Produce a synthesis of current mechanisms, candidate components, constraints,
  risks, and open questions for Arc 02.
- Distinguish candidate components from support assets, dependency edges,
  adapters, constraints, and package/release-surface gates.
- Preserve candidate labels as non-final analysis handles unless the synthesis
  explicitly marks them as "recommended for Arc 02 analysis," not as accepted
  architecture.
- Identify which questions require operator discussion before Arc 02 can close
  a conceptual model.
- Confirm whether Arc 01 can close after this slice or whether a remediation
  slice is required.

Out of scope:

- Deciding final component boundaries.
- Opening Arc 02 or writing its detailed arc plan.
- Editing source `SKILL.md`, `README.md`, framework docs, templates, Makefiles,
  package scripts, generated zips, or package exceptions.
- Re-running Slice 01 source inventory or Slice 02 problem mapping except as
  needed to resolve a synthesis inconsistency.
- Treating Project01 path constraints as a user-facing component.

## Required Artifacts

Produce these durable artifacts under `artifacts/`:

- `arc01-synthesis.md` - concise synthesis of what Arc 01 established, what it
  did not decide, and whether Arc 01 is ready for close.
- `candidate-component-inputs.md` - candidate component, support asset,
  dependency, adapter, and constraint inputs for Arc 02, with source evidence.
- `arc02-question-register.md` - operator and Arc 02 questions grouped by
  conceptual boundary, functional/package constraint, naming/mislabel risk, and
  maintenance implication.

## Verification Approach

The slice verifies by checking that the synthesis artifacts exist under the
standard artifact home, consume both verified prior slices, carry forward all
major Slice 02 findings and Project01 constraints, keep architecture decisions
non-final, and provide enough explicit inputs for Arc 02 to begin detailed
conceptual analysis.

## Exit Criteria

- Slice 01 and Slice 02 verified-close evidence is consumed and cited.
- `artifacts/arc01-synthesis.md` states what Arc 01 established, what remains
  undecided, and whether Arc 01 is ready to close or needs remediation.
- `artifacts/candidate-component-inputs.md` covers every major candidate label
  or grouped candidate from Slice 02 and classifies it as candidate component,
  support asset, dependency edge, adapter, constraint, or package/release gate.
- `artifacts/arc02-question-register.md` records operator and Arc 02 questions
  with decision owner, why it matters, and source evidence.
- The synthesis carries forward suspected mislabels, improper merge/split
  candidates, underfit/missing solution areas, overlap/duplication risks,
  monolithic load-cost concerns, and Project01 path/package constraints.
- No source files are edited.
