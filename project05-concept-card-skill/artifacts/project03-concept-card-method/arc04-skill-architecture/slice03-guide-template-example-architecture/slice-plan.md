# Slice 03: Guide, Template, and Example Architecture

```yaml
project: project03-concept-card-method
arc: arc04-skill-architecture
slice: slice03-guide-template-example-architecture
status: open
depends-on:
  - ../slice01-architecture-input-inventory/cdc-verification.md
  - ../slice01-architecture-input-inventory/artifacts/arc04-architecture-input-inventory.md
  - ../slice01-architecture-input-inventory/artifacts/arc04-decision-question-map.md
  - ../slice02-load-contract-ownership/cdc-verification.md
  - ../slice02-load-contract-ownership/artifacts/v40-load-contract.md
  - ../slice02-load-contract-ownership/artifacts/v40-ownership-routing-model.md
blocks:
  - ../slice04-validation-packaging-discoverability
  - ../slice05-architecture-synthesis
artifact-home: artifacts/
```

## Goal

Define the v4.0 concept-card method skill's guide, template, and example
architecture. The slice decides which method concerns belong in guides, which
authoring and trace surfaces need templates, and which examples are needed for
the first v4.0 release.

The slice consumes the accepted load contract and ownership model. It must
preserve the Arc03 conceptual distinctions and the Slice02 decision that the
v3.2 five-agent workflow is a default recipe, not an invariant.

## Scope

In scope:

- Decide the guide architecture by method concern, including extraction,
  re-extraction, evidence lifecycle, graph/CQ semantics, reconciliation,
  validation/verification workflow, and memory admission.
- Decide the template architecture for user-authored surfaces and
  trace/result-record surfaces.
- Decide the example architecture for minimal, claim-backed, CQ coverage,
  relationship/edge, extraction-run, reconciliation, and memory-admission
  examples.
- Preserve the load contract's positive/negative trigger boundary and thin
  `SKILL.md` routing posture.
- Preserve the five-agent workflow as a default recipe while requiring
  extraction-run and parallel-worker provenance for the actual workflow used.
- Route validation determinism, package behavior, README integration,
  Makefile/source edits, generated zips, schema syntax, enum spelling, and
  release mechanics to later owners.

Out of scope:

- Validation candidate selection, deterministic validation script design, or
  validator-code implementation.
- Package inclusion decisions, README integration, Makefile changes,
  generated zips, released skill bundles, or source checkout edits.
- Exact schema syntax, exact enum spelling, graph database design, memory
  runtime design, CCDP service design, or live extraction behavior.
- Writing final skill source files, final guides, final templates, or final
  examples in the source checkout.

## Required Artifacts

Write durable slice artifacts under `artifacts/`:

- `artifacts/v40-guide-architecture.md`
- `artifacts/v40-template-architecture.md`
- `artifacts/v40-example-architecture.md`

## Verification Approach

Verification is document-structural and source-backed:

- Confirm the open set exists before implementation close files are created.
- Confirm the three required artifacts exist under the slice-local artifact
  home.
- Grep the guide architecture for required method concerns and thin
  entrypoint routing.
- Grep the template architecture for user-authored versus trace/result-record
  surfaces and the required Arc03 constructs.
- Grep the example architecture for the release-critical example classes.
- Confirm the artifacts preserve positive/negative load triggers, problem
  ownership, dependency direction, and the five-agent default-recipe decision.
- Confirm unresolved validation, package, README, Makefile, source-edit,
  schema, enum, and release questions are routed to Slice04, Slice05, or
  Arc05.
- Confirm the source checkout remains clean and planning Markdown has no
  trailing-whitespace defects.

## Exit Criteria

- Slice04 has clear inputs for validation, packaging, README/discoverability,
  and maintenance decisions.
- Slice05 has a guide/template/example architecture it can compose with the
  load contract and later validation/package decisions.
- The open questions left by this slice are explicitly routed and not silently
  treated as decisions.
