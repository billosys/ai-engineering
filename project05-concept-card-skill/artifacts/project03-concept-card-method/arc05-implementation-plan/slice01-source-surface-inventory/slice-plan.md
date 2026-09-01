# Slice 01: Source Surface and Implementation Input Inventory

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice01-source-surface-inventory
status: open
opened-on: 2026-08-31
opened-by: Codex Desktop CDC planning pass
depends-on:
  - ../arc-plan.md
  - ../ledger.md
  - ../../arc04-skill-architecture/closing-report.md
  - ../../arc04-skill-architecture/slice05-architecture-synthesis/artifacts/arc05-implementation-planning-handoff.md
artifact-home: artifacts/
```

## Goal

Inventory the live source and planning surfaces Arc05 must understand before
it chooses the v4.0 concept-card method skill implementation layout. The slice
maps facts, current package conventions, and open implementation-planning
questions; it does not decide the final layout or edit source files.

## Scope

In scope:

- Inspect the current source checkout at
  `/Users/oubiwann/lab/billosys/ai-engineering`.
- Inventory existing knowledge-skill layouts under `knowledge/`, especially
  `SKILL.md`, `guides/`, source/provenance areas, templates/examples if
  present, and local README conventions.
- Inventory repository-level packaging and discoverability surfaces:
  `README.md`, `Makefile`, `package-path-exceptions.tsv`, generated archive
  conventions, ignored build outputs, and relevant check targets.
- Inventory accepted Arc04 implementation-planning inputs:
  `v40-skill-architecture.md`,
  `v40-architecture-decision-register.md`, and
  `arc05-implementation-planning-handoff.md`.
- Produce a source-surface inventory and an implementation-input question map
  for Slice02, Slice03, Slice04, and Slice05.

Out of scope:

- Editing source `SKILL.md`, guide, template, example, README, Makefile,
  package-list, package-path, schema, validator-code, generated-zip, or release
  files.
- Deciding final concept-card skill layout, exact filenames, schema syntax,
  enum spelling, validator-code language, Makefile targets, package-list
  changes, README/library prose, release gates, or generated-zip policy.
- Creating generated zips, released bundles, validator implementations,
  runtime services, GraphRAG, graph database, ontology database, memory runtime,
  CCDP service, or live extraction behavior.
- Closing Arc05 or Project03.

## Required Artifacts

Durable Slice01 outputs belong under `artifacts/`:

- `artifacts/source-surface-inventory.md`
- `artifacts/implementation-input-question-map.md`

## Verification Approach

The inventory should be verifiable by file existence, source-surface grep
coverage, Arc04 handoff coverage, explicit deferral language, and source
checkout cleanliness.

The slice should not make final architecture or implementation decisions. It
should identify candidate surfaces and questions for later slices.

## Exit Criteria

- The slice open set exists: `slice-plan.md`, `ledger.md`, `cc-prompt.md`, and
  `artifacts/`.
- The two required artifacts exist under `artifacts/`.
- The source-surface inventory covers source checkout, knowledge skills,
  `SKILL.md`, guides, README, Makefile, package-path exceptions, generated
  archive/build conventions, package checks, and ignored outputs.
- The source-surface inventory cites or names concrete live source paths, not
  only desired future paths.
- The question map covers Slice02 layout/content questions, Slice03 schema and
  validation questions, Slice04 packaging/discoverability/release questions,
  and Slice05 synthesis/project-close questions.
- The artifacts preserve accepted Arc04 inputs and name
  `v40-skill-architecture.md`, `v40-architecture-decision-register.md`, and
  `arc05-implementation-planning-handoff.md`.
- The artifacts keep source edits, final layout decisions, schema/enum
  decisions, validator implementation, Makefile/package edits, generated zips,
  release readiness, and runtime systems out of scope for Slice01.
- The artifacts identify known source implementation surfaces for later work:
  `knowledge/`, `README.md`, `Makefile`, `package-path-exceptions.tsv`, package
  targets, skill checks, package-path checks, generated archives, and version
  history obligations.
- The source checkout remains clean.
- New and modified Slice01 Markdown is ASCII-clean and has no trailing
  whitespace.

## Bubble-up Expectations

At close, report whether Slice01 found any source-surface fact that requires
Arc05 re-sequencing, a new slice, or a scope correction. If no such finding is
found, say so explicitly.

Slice01 should prepare Slice02 to choose source layout and content sequence,
but it must not choose that layout itself.
