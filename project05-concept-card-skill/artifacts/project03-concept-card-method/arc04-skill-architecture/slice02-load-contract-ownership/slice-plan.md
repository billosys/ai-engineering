# Slice 02: Load Contract and Ownership Model

```yaml
project: project03-concept-card-method
arc: arc04-skill-architecture
slice: slice02-load-contract-ownership
status: open
depends-on:
  - ../slice01-architecture-input-inventory/cdc-verification.md
  - ../slice01-architecture-input-inventory/artifacts/arc04-architecture-input-inventory.md
  - ../slice01-architecture-input-inventory/artifacts/arc04-decision-question-map.md
blocks:
  - ../slice03-guide-template-example-architecture
  - ../slice04-validation-packaging-discoverability
  - ../slice05-architecture-synthesis
artifact-home: artifacts/
```

## Goal

Define the v4.0 concept-card method skill's load contract and ownership
model: when a session should load the skill, what problem the skill owns, what
it leaves to adjacent guidance, and how a thin `SKILL.md` should route an
operator toward later guide surfaces.

This slice decides the entrypoint boundary. It does not decide the final guide
split, template set, package behavior, validation implementation, or source
file edits.

## Scope

In scope:

- Define positive and negative load triggers for the concept-card method
  skill.
- Define the problem ownership boundary for concept-card extraction,
  re-extraction, evidence grading, reconciliation, competency-question use,
  and memory admission.
- Define dependency direction between this skill and adjacent framework,
  project-management, source-reading, implementation-planning, and
  domain-knowledge guidance.
- Define the operator workflow boundary that a thin `SKILL.md` should expose.
- Route unresolved guide, template, validation, package, README, and source
  implementation questions to later slices or Arc05.

Out of scope:

- Final guide architecture, final template architecture, or final example set.
- Package inclusion decisions, README integration, Makefile changes, generated
  zips, or released skill bundles.
- Exact schema syntax, exact enum spelling, validator-code implementation, or
  deterministic validation scripts.
- Graph database design, memory runtime design, CCDP service design, or live
  extraction behavior.
- Source checkout edits.

## Required Artifacts

Write durable slice artifacts under `artifacts/`:

- `artifacts/v40-load-contract.md`
- `artifacts/v40-ownership-routing-model.md`

## Verification Approach

Verification is document-structural and source-backed:

- Confirm the open set exists before implementation close files are created.
- Confirm the two required artifacts exist under the slice-local artifact
  home.
- Grep the load contract for positive/negative load triggers and thin
  `SKILL.md` routing.
- Grep the ownership model for problem ownership, dependency direction, and
  adjacent-guidance boundaries.
- Confirm operator workflow coverage across extraction, re-extraction,
  verification, reconciliation, competency questions, and memory admission.
- Confirm Arc03 conceptual distinctions are preserved and unresolved choices
  are routed to later slices or Arc05.
- Confirm the source checkout remains clean and planning Markdown has no
  trailing-whitespace defects.

## Exit Criteria

- The load contract is explicit enough for Slice03 to design guides and
  templates without broadening the skill's ownership.
- The ownership/routing model distinguishes what this skill owns, what it
  depends on, and what it leaves to adjacent guidance.
- Any unresolved architecture or implementation questions are routed to
  Slice03, Slice04, Slice05, or Arc05.
