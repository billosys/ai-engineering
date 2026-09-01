# Slice 05: Architecture Synthesis and Arc05 Handoff

```yaml
project: project03-concept-card-method
arc: arc04-skill-architecture
slice: slice05-architecture-synthesis
status: open
depends-on:
  - ../slice01-architecture-input-inventory/cdc-verification.md
  - ../slice01-architecture-input-inventory/artifacts/arc04-architecture-input-inventory.md
  - ../slice01-architecture-input-inventory/artifacts/arc04-decision-question-map.md
  - ../slice02-load-contract-ownership/cdc-verification.md
  - ../slice02-load-contract-ownership/artifacts/v40-load-contract.md
  - ../slice02-load-contract-ownership/artifacts/v40-ownership-routing-model.md
  - ../slice03-guide-template-example-architecture/cdc-verification.md
  - ../slice03-guide-template-example-architecture/artifacts/v40-guide-architecture.md
  - ../slice03-guide-template-example-architecture/artifacts/v40-template-architecture.md
  - ../slice03-guide-template-example-architecture/artifacts/v40-example-architecture.md
  - ../slice04-validation-packaging-discoverability/cdc-verification.md
  - ../slice04-validation-packaging-discoverability/artifacts/v40-validation-architecture.md
  - ../slice04-validation-packaging-discoverability/artifacts/v40-package-discoverability-model.md
  - ../slice04-validation-packaging-discoverability/artifacts/v40-maintenance-ownership-model.md
blocks:
  - ../../arc04-skill-architecture/closing-report.md
  - ../../../arc05-implementation-plan
artifact-home: artifacts/
```

## Goal

Compose the verified Arc04 slice outputs into an accepted v4.0 concept-card
method skill architecture and prepare a bounded handoff for Arc05
implementation planning.

The slice must show how the load contract, ownership model, guide
architecture, template architecture, example architecture, validation
architecture, package/discoverability model, and maintenance ownership model
fit together. It should record final architecture decisions, preserve
unresolved questions as explicitly routed implementation inputs, and leave
Arc04 ready for formal arc close.

## Scope

In scope:

- Synthesize the accepted v4.0 skill architecture across `SKILL.md`, guides,
  templates, examples, validation candidates, package behavior, README/library
  discoverability, and maintenance ownership.
- Record final Arc04 architecture decisions and unresolved decision routing.
- Confirm the architecture preserves the accepted conceptual model: concept
  card, claim, source span, source support, evidence grade, extraction
  confidence, relationship/edge, competency question/CQ, extraction run,
  validation result, verification result/state, reconciliation result/state,
  preservation decision, and memory admission.
- Preserve the load contract's positive/negative trigger boundary, problem
  ownership, dependency direction, thin `SKILL.md` entrypoint, and five-agent
  default-recipe decision.
- Preserve the package/discoverability promise boundary: no runtime GraphRAG,
  graph database, ontology database, memory runtime, CCDP service, live
  extraction, executable validator, generated zip, or package release is
  promised by Arc04.
- Produce the Arc05 implementation-planning handoff with exact work categories
  for source layout, source edits, guide/template/example files, schema,
  enums, validator-code, Makefile/package lists, README/library text,
  generated zips, tests, release gates, and source version histories.

Out of scope:

- Editing source `SKILL.md`, guide, template, example, README, Makefile,
  package-list, validator-code, schema, enum, test, generated-zip, release, or
  packaged skill files.
- Implementing the skill, validator, package, README integration, generated
  artifacts, runtime services, graph/database infrastructure, memory runtime,
  CCDP service, or live extraction behavior.
- Re-opening or re-deciding verified Slice02, Slice03, or Slice04 decisions
  except to name a bounded unresolved decision for Arc05.
- Writing the Arc04 arc-level `closing-report.md`; that belongs to formal
  Arc04 close after Slice05 is independently verified.

## Required Artifacts

Write durable slice artifacts under `artifacts/`:

- `artifacts/v40-skill-architecture.md`
- `artifacts/v40-architecture-decision-register.md`
- `artifacts/arc05-implementation-planning-handoff.md`

## Verification Approach

Verification is document-structural and composition-oriented:

- Confirm the open set exists before implementation close files are created.
- Confirm the three required artifacts exist under the slice-local artifact
  home.
- Grep the skill architecture for the final architecture surfaces:
  `SKILL.md`, guides, templates, examples, validation candidates, package
  behavior, README/library discoverability, and maintenance ownership.
- Grep the skill architecture for accepted conceptual-model constructs and
  no-flattening lifecycle distinctions.
- Grep the decision register for final decisions, unresolved decisions, owner
  routing, Slice02/Slice03/Slice04 preservation, and Arc05 routing.
- Grep the Arc05 handoff for source layout, source edits, guide/template/example
  files, schema, enum, validator-code, Makefile/package lists, README/library
  text, generated zips, tests, release gates, package updates, and source
  version history.
- Confirm the architecture preserves the thin `SKILL.md` load contract,
  positive/negative load triggers, problem ownership, dependency direction,
  package/discoverability promise boundary, and five-agent default-recipe
  decision.
- Confirm the architecture routes runtime GraphRAG, graph database, ontology
  database, memory runtime, CCDP service, live extraction, executable
  validator, generated zip, release, and package implementation to later
  owners rather than promising them in Arc04.
- Confirm the source checkout remains clean and planning Markdown has no
  trailing-whitespace defects.

## Exit Criteria

- Arc04 has a complete architecture synthesis ready for formal arc close and
  arc-ledger composition verification.
- Arc05 has a bounded implementation-planning handoff that can be turned into
  source-edit slices without re-reading the whole Arc04 history.
- No source implementation, package update, generated artifact, runtime
  service, or release claim is introduced by this planning slice.
