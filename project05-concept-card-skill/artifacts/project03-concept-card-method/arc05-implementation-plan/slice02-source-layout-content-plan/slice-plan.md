# Slice 02: Skill Source Layout and Content Sequence

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice02-source-layout-content-plan
status: open
opened-on: 2026-08-31
opened-by: Codex Desktop CDC planning pass
depends-on:
  - ../arc-plan.md
  - ../ledger.md
  - ../slice01-source-surface-inventory/cdc-verification.md
  - ../slice01-source-surface-inventory/artifacts/source-surface-inventory.md
  - ../slice01-source-surface-inventory/artifacts/implementation-input-question-map.md
  - ../../arc04-skill-architecture/slice05-architecture-synthesis/artifacts/v40-skill-architecture.md
  - ../../arc04-skill-architecture/slice05-architecture-synthesis/artifacts/arc05-implementation-planning-handoff.md
artifact-home: artifacts/
```

## Goal

Plan the source layout and content sequence for implementing the v4.0
concept-card method skill. The slice should decide where the future skill
source files belong, which content surfaces are required, how those surfaces
link together, and how implementation should edit them in an incremental
sequence.

This is still planning work. It does not edit the source checkout.

## Scope

In scope:

- Decide the target source home for the concept-card method skill and the
  exact planned paths for `SKILL.md`, guides, templates, examples, validation
  documentation, and any package-compatible support documents.
- Decide whether templates, examples, schema notes, and validation guidance
  should live under `guides/` to match the current package contract, or whether
  later packaging work must deliberately change package behavior.
- Plan the thin `SKILL.md` content sequence: reason to load, positive load
  triggers, negative load triggers, problem ownership, dependency direction,
  operator workflow routing, and guide routing.
- Plan guide, template, and example filenames, boundaries, cross-links, and
  first implementation edit order.
- Preserve accepted Arc04 decisions and the Slice01 package-behavior
  constraint while routing unresolved schema, validation, package, release, and
  version-history questions to later Arc05 slices.

Out of scope:

- Editing source `SKILL.md`, guide, template, example, README, Makefile,
  package-list, package-path, schema, validator-code, generated-zip, or release
  files.
- Choosing exact schema syntax, enum spelling, validator-code language,
  failure-message format, deterministic validation implementation, tests,
  package target names, package list edits, package-path exception rows,
  generated zip policy, release gates, or source version-history text.
- Creating generated zips, released bundles, validator implementations,
  runtime services, GraphRAG, graph database, ontology database, memory runtime,
  CCDP service, or live extraction behavior.
- Closing Arc05 or Project03.

## Required Artifacts

Durable Slice02 outputs belong under `artifacts/`:

- `artifacts/v40-source-layout-plan.md`
- `artifacts/v40-content-sequence-plan.md`
- `artifacts/v40-surface-routing-decision-register.md`

## Verification Approach

The slice should be verifiable by file existence, concrete planned source
paths, explicit guide/template/example coverage, preserved Arc04 inputs,
package-contract routing, later-slice routing, and source checkout cleanliness.

The artifacts should distinguish accepted Slice02 decisions from questions
deferred to Slice03, Slice04, Slice05, or a later implementation effort.

## Exit Criteria

- The slice open set exists: `slice-plan.md`, `ledger.md`, `cc-prompt.md`, and
  `artifacts/`.
- The three required artifacts exist under `artifacts/`.
- The source layout plan names the planned source home and exact planned paths
  for `SKILL.md`, guides, templates, examples, validation documentation, and
  support documents.
- The source layout plan preserves the Slice01 package-behavior constraint:
  current generic skill packaging copies the selected `SKILL.md` plus sibling
  `guides/`, or else it explicitly routes any needed package behavior change to
  Slice04.
- The content sequence plan covers thin `SKILL.md` load contract, reason to
  load, positive load, negative load, problem ownership, dependency direction,
  operator workflow, guide routing, and source edit sequencing.
- The content sequence plan names planned guide files, template files, example
  files, cross-links, and first implementation edit order.
- The decision register records accepted, deferred, and no-op decisions with
  owners or later-slice routing, and preserves accepted Arc04 decisions.
- The artifacts route schema syntax, enum spelling, validator-code scope,
  deterministic validation, tests, package targets, package lists,
  package-path exceptions, generated zip policy, release gates, and source
  version-history obligations to later Arc05 slices.
- The artifacts keep source edits, source implementation, runtime services,
  generated zips, package release, and release readiness out of scope.
- The source checkout remains clean.
- New and modified Slice02 Markdown is ASCII-clean and has no trailing
  whitespace.

## Bubble-up Expectations

At close, report whether Slice02 found any layout or content-sequencing fact
that requires Arc05 re-sequencing, a new slice, or a scope correction. If no
such finding is found, say so explicitly.

Slice02 should prepare Slice03 to plan schema and validation work against a
stable file layout, and Slice04 to plan packaging and discoverability against
known source surfaces.
