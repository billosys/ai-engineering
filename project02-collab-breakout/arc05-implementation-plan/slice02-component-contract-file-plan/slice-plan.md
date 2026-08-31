# Slice 02: Component Contract And File Plan

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice02-component-contract-file-plan
status: open
opened-on: 2026-08-31
artifact-home: artifacts/
depends-on:
  - ../arc-plan.md
  - ../ledger.md
  - ../slice01-implementation-surface-map:verified-closed
blocks:
  - ../slice03-package-readme-validation-plan
related:
  - ../../project-plan.md
  - ../../ledger.md
  - ../arc-plan.md
  - ../ledger.md
  - ../slice01-implementation-surface-map/cdc-verification.md
  - ../slice01-implementation-surface-map/artifacts/implementation-surface-inventory.md
  - ../slice01-implementation-surface-map/artifacts/accepted-component-source-map.md
  - ../slice01-implementation-surface-map/artifacts/release-validation-surface-map.md
  - ../slice01-implementation-surface-map/artifacts/cross-cutting-concern-map.md
  - ../slice01-implementation-surface-map/artifacts/slice02-component-file-plan-inputs.md
  - ../../arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/artifacts/operator-accepted-architecture.md
```

## Goal

Convert the accepted Project02 breakout architecture and verified Slice01
surface map into a component-by-component contract and file plan.

This slice defines the target source layout, component entrypoint shape,
guide/template/example placement, version-history placement, source-to-target
movement or copy strategy, component package/source contract fields, support
asset ownership, adapter ownership, dependency edges, and deferred items for
all eight accepted components.

## Scope

In scope:

- Use `operator-accepted-architecture.md` as the authoritative component name
  source.
- Consume the verified Slice01 implementation surface map and Slice02 handoff
  inputs.
- Plan all eight accepted component contracts:
  `collaboration-framework`, `engineering-methods`, `project-management`,
  `work-verification`, `testing`, `code-auditing`, `agent-coordination`, and
  `contribution-style`.
- Define proposed target source paths, package roots, `SKILL.md` entrypoints,
  sibling `version-history.md` files, guide names, template/example placement,
  and dependency/route notes for each component.
- Map current source files to target component files or explicit new-prose,
  copied-support-asset, adapter, deferred, or non-component status.
- Preserve `engineering-methods` ownership of source/package/release gates
  while requiring package/source contract fields on every component.
- Preserve `agent-coordination` ownership of CC/CDC/operator terminology,
  delegation decisions, context-packet discipline, and result integration.
- Preserve CCDP separation and deferred memory-admission status.
- Produce Slice03-ready inputs for package, README, and validation planning.

Out of scope:

- Editing source files.
- Creating component directories in the source checkout.
- Writing final component `SKILL.md`, guide, template, README, Makefile,
  package exception, generated zip, or validation changes.
- Finalizing release-surface behavior that belongs to Slice03.
- Closing Arc05.

## Required Artifacts

Produce durable artifacts under `artifacts/`:

- `component-contract-matrix.md` - one row per accepted component, including
  contract, standalone use, composed use, dependencies, owned source, owned
  support assets, deferred items, and validation responsibilities.
- `component-file-layout-plan.md` - proposed target source tree for each
  component, including `SKILL.md`, sibling `version-history.md`, guides,
  templates, examples, and support assets.
- `source-to-component-migration-plan.md` - mapping from current source files
  to target component files, including move/copy/split/new-prose/defer
  decisions.
- `package-source-contract-register.md` - per-component source path, package
  root, package-local link, installed-skill route, README route, Makefile
  impact, generated-zip expectation, validation command, owner, and versioning
  contract.
- `support-adapter-dependency-plan.md` - support asset ownership, adapter
  placement, dependency edges, role terminology, context-packet/result
  integration boundaries, component-boundary-analysis placement, memory
  deferral, and CCDP separation.
- `slice03-package-readme-validation-inputs.md` - concrete non-final inputs
  and open questions for Slice03 package, README, and validation planning.

## Verification Approach

The slice verifies by checking that the required artifacts exist, cite the
verified Slice01 inputs, cover all eight accepted components, define the
component file plan and package/source contract fields, preserve cross-cutting
decisions, produce Slice03-ready inputs, and leave the source checkout clean.

## Exit Criteria

- All eight accepted components have explicit component contracts and file
  plans.
- Every component has planned `SKILL.md` and sibling `version-history.md`
  placement.
- Current source files are mapped to target component files or explicit
  new-prose, copied-support-asset, adapter, deferred, or non-component status.
- Per-component package/source contract fields are present without finalizing
  Slice03 release-surface edits.
- Support assets, adapters, dependencies, component-boundary analysis,
  deferred memory admission, and CCDP separation are explicitly dispositioned.
- Slice03 receives package, README, Makefile, generated zip, package-path
  exception, validation, migration, and open-question inputs.
- No source files are edited.

## Closure State

Slice02 is open. No close-set documents exist yet. Source files remain
untouched, and implementation has not started.
