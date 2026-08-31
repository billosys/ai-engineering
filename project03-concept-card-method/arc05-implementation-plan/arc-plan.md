# Arc 05: Implementation Plan

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
status: active
depends-on:
  - ../arc04-skill-architecture/closing-report.md
related:
  - ../arc04-skill-architecture/slice05-architecture-synthesis/artifacts/v40-skill-architecture.md
  - ../arc04-skill-architecture/slice05-architecture-synthesis/artifacts/v40-architecture-decision-register.md
  - ../arc04-skill-architecture/slice05-architecture-synthesis/artifacts/arc05-implementation-planning-handoff.md
```

## Capability

Arc05 converts the accepted v4.0 concept-card method skill architecture into
a source-edit implementation plan. It decides the exact repository layout,
guide/template/example file set, schema and enum choices, validator-code
scope, README/library discoverability updates, Makefile/package-list changes,
generated artifact policy, release gates, and source version-history
obligations needed to create the concept-card method skill in a later
implementation effort.

The arc remains planning-only. It does not edit source `SKILL.md` files,
guides, templates, examples, README, Makefile, package lists, validator code,
schema files, generated zips, released bundles, or runtime services.

## Slice Breakdown

### Slice 01: Source Surface and Implementation Input Inventory

Directory: `slice01-source-surface-inventory`

Status: verified-closed on 2026-08-31.

Scope: inventory the live source checkout surfaces Arc05 may need to plan
against: existing knowledge skills, README/library text, Makefile/package
targets, package-path exceptions, generated-artifact conventions, and the
accepted Arc04 handoff. This slice maps facts and open implementation
questions; it does not decide final layout or edit source files.

Blocks: Slice02, Slice03, Slice04, and Slice05.

Durable planning artifacts belong under the slice-local `artifacts/`
directory.

### Slice 02: Skill Source Layout and Content Sequence

Directory: `slice02-source-layout-content-plan`

Status: planned.

Scope: decide the target source layout for the v4.0 concept-card method skill:
thin `SKILL.md`, guide files, template files, example files, validation
documentation, cross-links, file naming, and source-edit sequencing. This
slice plans the content surfaces and edit order, while leaving schema/validator
mechanics and package/release gates to later slices.

Blocks: Slice03, Slice04, and Slice05.

Durable planning artifacts belong under the slice-local `artifacts/`
directory.

### Slice 03: Schema, Enum, and Validation Plan

Directory: `slice03-schema-validation-plan`

Status: planned.

Scope: decide the implementation-plan treatment for concept-card schemas,
claim/source-support records, source-span locators, edge/CQ/run/result
records, enum spelling, deterministic validation candidates, validator-code
scope, tests, failure-output expectations, and semantic/human review
boundaries. This slice plans validation and schema work; it does not implement
validators.

Blocks: Slice04 and Slice05.

Durable planning artifacts belong under the slice-local `artifacts/`
directory.

### Slice 04: Packaging, Discoverability, and Release Gates

Directory: `slice04-packaging-release-plan`

Status: planned.

Scope: decide README and library discoverability text requirements,
Makefile/package-list updates, package-path validation, generated-zip policy,
generated-artifact handling, release gates, CI/check target expectations, and
source version-history obligations. This slice plans package and release
mechanics without producing generated zips or release artifacts.

Blocks: Slice05.

Durable planning artifacts belong under the slice-local `artifacts/`
directory.

### Slice 05: Implementation Plan Synthesis and Project Close Input

Directory: `slice05-implementation-plan-synthesis`

Status: planned.

Scope: compose the verified Arc05 planning slices into the accepted
implementation plan: source edit sequence, verification gate matrix,
implementation-slice recommendations, deferral register, and Project03 close
input. This slice prepares the project for closure or for a separate
implementation effort; it does not perform source edits.

Blocks: Arc05 close and Project03 close.

Durable planning artifacts belong under the slice-local `artifacts/`
directory.

## Dependencies

Consumes:

- Closed Arc04 skill architecture and arc close report.
- Accepted v4.0 skill architecture, architecture decision register, and Arc05
  implementation-planning handoff.
- Current source checkout layout, package behavior, Makefile targets,
  README/library surfaces, and package-path conventions.
- Project03's planning-only source-edit boundary.

Leaves for later work:

- An accepted source-edit plan for creating the v4.0 concept-card method
  skill.
- A verification matrix for implementation work, including skill checks,
  package-path checks, generated artifact checks, source-history checks, and
  release-readiness gates.
- A Project03 close input showing whether the project definition of done is
  satisfied without source edits.

## Version History

### v1.0 - 2026-08-31

Arc05 opened after Arc04 formal close. The arc is scoped to implementation
planning only: inventory source surfaces, decide source layout and content
sequence, plan schema/validation work, plan packaging/discoverability/release
gates, and synthesize a bounded implementation plan before Project03 close.

### v1.1 - 2026-08-31

Slice01 opened for source-surface and implementation-input inventory. The
slice is scoped to mapping live repository facts, package/discoverability
surfaces, and Arc04 handoff inputs before later slices decide layout, schema,
validation, packaging, release gates, or implementation sequencing.

### v1.2 - 2026-08-31

Slice01 marked verified-closed after CDC reproduced all ten slice ledger rows.
No Arc05 re-sequencing, new slice, or scope correction is required before
Slice02. The package-behavior constraint surfaced by Slice01 remains an input:
the current generic skill package path copies the selected `SKILL.md` plus
sibling `guides/`, so assets outside `guides/` must be planned deliberately by
later Arc05 slices.
