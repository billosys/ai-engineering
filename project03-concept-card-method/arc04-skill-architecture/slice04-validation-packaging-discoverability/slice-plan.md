# Slice 04: Validation, Packaging, and Discoverability

```yaml
project: project03-concept-card-method
arc: arc04-skill-architecture
slice: slice04-validation-packaging-discoverability
status: open
depends-on:
  - ../slice01-architecture-input-inventory/cdc-verification.md
  - ../slice01-architecture-input-inventory/artifacts/arc04-decision-question-map.md
  - ../slice02-load-contract-ownership/cdc-verification.md
  - ../slice02-load-contract-ownership/artifacts/v40-load-contract.md
  - ../slice02-load-contract-ownership/artifacts/v40-ownership-routing-model.md
  - ../slice03-guide-template-example-architecture/cdc-verification.md
  - ../slice03-guide-template-example-architecture/artifacts/v40-guide-architecture.md
  - ../slice03-guide-template-example-architecture/artifacts/v40-template-architecture.md
  - ../slice03-guide-template-example-architecture/artifacts/v40-example-architecture.md
blocks:
  - ../slice05-architecture-synthesis
artifact-home: artifacts/
```

## Goal

Define the v4.0 concept-card method skill's validation, packaging,
discoverability, and maintenance architecture. The slice decides which checks
are deterministic enough to plan for later automation, which checks remain
semantic audit or human/operator review, what surfaces should be packaged or
only carried forward as planning inputs, how discoverability should describe
the skill, and which owners should maintain conceptual, package, README, and
validator alignment.

The slice consumes the verified load contract and the verified guide,
template, and example architecture. It must preserve the thin `SKILL.md`
routing posture, the concern-based guide split, the template surface classes,
the release-critical example set, and the five-agent default-recipe decision.

## Scope

In scope:

- Classify validation candidates as deterministic structural checks, semantic
  audit checks, human/operator review checks, or deferred runtime checks.
- Decide the package architecture at the level of surface category: guides,
  templates, examples, scripts, generated artifacts, validation candidates,
  and planning-only inputs.
- Decide README and skill-library discoverability promises without implying
  runtime services, graph infrastructure, memory infrastructure, or live
  extraction services.
- Decide maintenance ownership for conceptual-model updates, guide/template
  updates, example updates, package-list updates, README/library updates,
  validation-candidate changes, validator-code follow-up, and version history.
- Route exact source file layout, exact schema syntax, exact enum spelling,
  validator-code implementation, Makefile/package-list edits, README edits,
  generated zips, tests, release mechanics, and package updates to Arc05.
- Route final architecture composition, unresolved-decision synthesis, and
  Arc05 handoff material to Slice05.

Out of scope:

- Writing source `SKILL.md`, guide, template, example, README, Makefile,
  package-list, validator-code, schema, enum, test, generated-zip, or release
  files.
- Implementing deterministic validation scripts or choosing exact CLI/API
  behavior.
- Building graph database, GraphRAG, memory runtime, CCDP service, live
  extraction, or package release behavior.
- Re-deciding the Slice02 load contract or the Slice03 guide/template/example
  architecture except to route maintenance or packaging responsibilities.

## Required Artifacts

Write durable slice artifacts under `artifacts/`:

- `artifacts/v40-validation-architecture.md`
- `artifacts/v40-package-discoverability-model.md`
- `artifacts/v40-maintenance-ownership-model.md`

## Verification Approach

Verification is document-structural and source-backed:

- Confirm the open set exists before implementation close files are created.
- Confirm the three required artifacts exist under the slice-local artifact
  home.
- Grep the validation architecture for deterministic structural checks,
  semantic audit checks, human/operator review checks, deferred runtime checks,
  and validation candidates from the accepted architecture inputs.
- Grep the package/discoverability model for packaged surfaces, planning-only
  inputs, README/library discoverability, package behavior, package inclusion,
  generated artifacts, scripts, and no-runtime-service promises.
- Grep the maintenance ownership model for conceptual-model, guide, template,
  example, package, README/library, validation-candidate, validator-code, and
  version-history ownership.
- Confirm the artifacts preserve the verified load contract, thin `SKILL.md`
  posture, guide split, template surface classes, example set, and five-agent
  default-recipe decision.
- Confirm unresolved source-edit, exact layout, schema, enum, validator-code,
  Makefile, README, generated-zip, test, release, and package-update questions
  are routed to Slice05 or Arc05 rather than decided here.
- Confirm the source checkout remains clean and planning Markdown has no
  trailing-whitespace defects.

## Exit Criteria

- Slice05 has clear validation, packaging, discoverability, and maintenance
  inputs to compose with the verified load contract and guide/template/example
  architecture.
- Arc05 has bounded implementation-planning inputs for source edits, exact
  file layout, validator work, Makefile/package updates, README changes,
  generated zips, tests, and release gates.
- The slice does not imply a runtime service, executable validator, or
  released package before the architecture is accepted.
