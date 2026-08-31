# Slice 01: Implementation Surface Map

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice01-implementation-surface-map
status: proposed-done
opened-on: 2026-08-31
proposed-done-on: 2026-08-31
artifact-home: artifacts/
depends-on:
  - ../arc-plan.md
  - ../ledger.md
  - ../../arc04-breakout-architecture:closed-composed
  - ../../../project01-harmonise-paths:closed-and-completely-verified
blocks:
  - ../slice02-component-contract-file-plan
related:
  - ../../project-plan.md
  - ../../ledger.md
  - ../arc-plan.md
  - ../ledger.md
  - ../../arc04-breakout-architecture/closing-report.md
  - ../../arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/artifacts/operator-accepted-architecture.md
  - ../../arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/artifacts/arc05-implementation-inputs.md
```

## Goal

Map the exact implementation surfaces Arc05 must plan across before source
edits begin.

This slice produces an evidence-backed inventory of current source files,
current package/release behavior, README and `SKILL.md` routes, Makefile
package lists, templates, guide files, package-path exceptions, validation
commands, and CCDP boundaries. It connects each surface to the accepted Arc04
component architecture.

## Scope

In scope:

- Consume the accepted Arc04 architecture and Project01 source/package path
  contract.
- Inspect the current source checkout read-only.
- Identify every current source file relevant to the accepted component set.
- Identify current generated package roots and Makefile package surfaces.
- Identify README, `SKILL.md`, guide, template, and validation command surfaces.
- Map each accepted component to candidate source files and package/release
  surfaces.
- Map support assets, adapter material, component maintenance/version history,
  ontology/component-boundary guidance, memory-admission deferral, and CCDP
  separation.
- Produce Slice02-ready inputs.

Out of scope:

- Editing source files.
- Creating component directories in the source checkout.
- Finalizing component file plans.
- Editing README, `SKILL.md`, Makefile, package exceptions, guides, templates,
  generated zip artifacts, or CCDP files.
- Closing Arc05.

## Required Artifacts

Produce durable artifacts under `artifacts/`:

- `implementation-surface-inventory.md` - current source/release/package
  surface inventory.
- `accepted-component-source-map.md` - accepted component to current source
  file and package-surface mapping.
- `release-validation-surface-map.md` - Makefile, generated zip, validation,
  README, `SKILL.md`, and package-path gate inventory.
- `cross-cutting-concern-map.md` - support assets, adapters, version histories,
  source/package gates, component-boundary analysis, deferred memory admission,
  and CCDP separation.
- `slice02-component-file-plan-inputs.md` - concrete inputs and open questions
  for Slice02.

## Verification Approach

The slice verifies by checking that required artifacts exist, cite the accepted
Arc04 architecture, map all eight accepted components, preserve Project01
source/package constraints, name current source/release surfaces, preserve
planning-only boundaries, and leave the source checkout clean.

## Exit Criteria

- Accepted Arc04 architecture and Project01 path/package constraints are cited.
- All eight accepted components are mapped to current source files or explicit
  no-current-file/new-component status.
- README, top-level `SKILL.md`, current guides, templates, Makefile package
  lists, package-path exceptions, generated zip behavior, validation commands,
  and CCDP boundaries are inventoried.
- Support assets, adapters, component versioning, component-boundary analysis,
  and deferred memory admission are mapped.
- Slice02 receives component-file-plan inputs.
- No source files are edited.

## Delivered On 2026-08-31

Slice01 produced these durable artifacts under `artifacts/`:

- `implementation-surface-inventory.md`
- `accepted-component-source-map.md`
- `release-validation-surface-map.md`
- `cross-cutting-concern-map.md`
- `slice02-component-file-plan-inputs.md`

The close report is `closing-report.md`.

## Closure State

Slice01 is proposed-done by CC. CDC verification is pending. Source files
remain untouched, and implementation has not started.
