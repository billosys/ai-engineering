# Arc 05: Implementation Plan

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
status: closed
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

Status: verified-closed on 2026-08-31.

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

Status: verified-closed on 2026-08-31.

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

Status: verified-closed on 2026-08-31.

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

Status: verified-closed on 2026-09-01.

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

### v1.3 - 2026-08-31

Slice02 opened for skill source layout and content sequence planning. The
slice will decide planned source paths, content boundaries, cross-links, and
first implementation edit order while routing schema, validation, package,
release, and version-history mechanics to later Arc05 slices.

### v1.4 - 2026-08-31

Slice02 marked verified-closed after CDC reproduced all eleven slice ledger
rows. The accepted source home is `knowledge/concept-card-method/`, with
`SKILL.md` at the root and guide, template, example, validation, and support
surfaces planned under sibling `guides/`. No re-sequencing, new slice, or scope
correction is required before Slice03.

### v1.5 - 2026-08-31

Slice03 opened for schema, enum, validation, validator-code scope, test scope,
failure-output expectation, and review-boundary planning. The slice consumes
the verified Slice02 layout and leaves README, Makefile, package, generated
zip, release, and source version-history mechanics to Slice04.

### v1.6 - 2026-08-31

Slice03 marked verified-closed after CDC reproduced all twelve slice ledger
rows. The accepted implementation-plan posture is Markdown records with YAML
frontmatter, lowercase snake_case controlled vocabulary, validation/review
boundaries, and documentation-only validator-code scope. No re-sequencing, new
slice, or scope correction is required before Slice04.

### v1.7 - 2026-08-31

Slice04 opened for packaging, discoverability, release-gate, generated
artifact, package-path, and source version-history planning. The slice consumes
the verified Slice02 layout and Slice03 documentation-only validator-code
scope, and leaves implementation-plan synthesis and Project03 close input to
Slice05.

### v1.8 - 2026-08-31

Slice04 marked verified-closed after CDC reproduced all twelve slice ledger
rows. Packaging, discoverability, release-gate, generated-artifact,
package-path, and source version-history obligations are now ready for Slice05
implementation-plan synthesis. No re-sequencing, new slice, or scope
correction is required before Slice05.

### v1.9 - 2026-08-31

Slice05 opened for implementation-plan synthesis, source edit sequence,
verification gate matrix, implementation-slice recommendations, deferral
register, and Project03 close input. This is the final Arc05 planning slice
before formal arc close.

### v1.10 - 2026-09-01

Slice05 marked verified-closed after CDC reproduced all thirteen slice ledger
rows. Arc05 is ready for formal arc close and arc-scale composition
verification before Project03 closure is considered.

### v1.11 - 2026-09-01

Arc05 formally closed with composition verdict `delivered`. The arc produced
the accepted implementation-planning package for future source edits while
preserving the planning-only boundary and leaving Project03 ready for formal
project close.
