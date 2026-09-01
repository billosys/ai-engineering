# Slice 01: Architecture Input Inventory

```yaml
project: project03-concept-card-method
arc: arc04-skill-architecture
slice: slice01-architecture-input-inventory
status: open
depends-on:
  - ../../arc03-conceptual-model/closing-report.md
blocks:
  - ../slice02-load-contract-ownership
  - ../slice03-guide-template-example-architecture
  - ../slice04-validation-packaging-discoverability
  - ../slice05-architecture-synthesis
artifact-home: artifacts/
```

## Goal

Create Arc04's input inventory: a source-backed map of accepted conceptual
model commitments, handoff inputs, candidate skill surfaces, architectural
decision axes, and open decision questions for the v4.0 concept-card method
skill.

The slice prepares the architecture problem. It does not choose the final
skill layout.

## Scope

In scope:

- Inventory accepted Arc03 commitments that Arc04 must preserve.
- Inventory candidate skill surfaces: `SKILL.md`, guides, templates,
  examples, validation candidates, package behavior, README integration, and
  maintenance ownership.
- Map architecture decisions by reason to load, problem ownership, dependency
  direction, package behavior, maintenance ownership, validation
  determinism, and operator workflow.
- Route decision questions to later Arc04 slices and Arc05 where appropriate.

Out of scope:

- Final skill architecture or final file layout.
- Writing source `SKILL.md`, guide, template, README, Makefile, package, or
  validator-code changes.
- Exact schema syntax, exact enum spelling, generated zips, released skill
  bundles, runtime services, live extraction, graph database design, memory
  runtime design, or CCDP service design.

## Required Artifacts

Write durable slice artifacts under `artifacts/`:

- `artifacts/arc04-architecture-input-inventory.md`
- `artifacts/arc04-decision-question-map.md`

## Verification Approach

Verification is document-structural and source-backed:

- Confirm the open set exists before implementation close files are created.
- Confirm required artifacts exist under the slice-local artifact home.
- Grep the input inventory for accepted Arc03 constructs and candidate skill
  surfaces.
- Grep the decision-question map for the required architecture decision axes
  and later-slice routing.
- Confirm scope fences keep source edits and final architecture decisions out
  of this slice.
- Confirm the source checkout remains clean and planning Markdown has no
  trailing-whitespace defects.

## Exit Criteria

- The two required artifacts exist and are usable as inputs for Slice02
  through Slice05.
- All slice ledger rows are addressed by the closing report and later
  reproduced by CDC.
- Any architecture questions not decided here are explicitly routed to a
  later slice or Arc05.
