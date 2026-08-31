# Arc 05: Implementation Plan

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
status: active
opened-on: 2026-08-31
depends-on:
  - arc04-breakout-architecture:closed-composed
  - project01-harmonise-paths:closed-and-completely-verified
blocks:
  - source implementation of collaboration-framework breakout
related:
  - ../project-plan.md
  - ../ledger.md
  - ../arc04-breakout-architecture/closing-report.md
  - ../arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/artifacts/operator-accepted-architecture.md
  - ../arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/artifacts/arc05-implementation-inputs.md
```

## Capability

Arc05 converts the accepted breakout architecture into a sliceable
implementation plan. It defines exact source-edit slices, component file
plans, README and `SKILL.md` route changes, package/build changes, validation
gates, migration notes, and closure evidence needed to perform the breakout
after planning closes.

Arc05 is planning-only. It does not edit source files, generated packages,
Makefile package targets, README, `SKILL.md`, guides, templates, or CCDP
artifacts.

## Accepted Architecture Input

Arc05 consumes the operator-accepted Arc04 architecture:

- `collaboration-framework`
- `engineering-methods`
- `project-management`
- `work-verification`
- `testing`
- `code-auditing`
- `agent-coordination`
- `contribution-style`

Cross-cutting requirements:

- `engineering-methods` owns source/package/release gates.
- Every component carries its own package/source contract.
- Every component is versioned through `SKILL.md` with sibling
  `version-history.md`.
- `agent-coordination` owns CC/CDC/operator terminology, delegation decisions,
  context-packet discipline, and result integration.
- `engineering-methods/guides/05-component-boundary-analysis.md` owns the
  reusable ontology/component-boundary analysis guide.
- Memory admission is deferred future research.
- CCDP remains a separate protocol distribution.

## Slice Breakdown

### Slice 01: Implementation Surface Map

Directory: `slice01-implementation-surface-map`

Status: open as of 2026-08-31.

Scope: inventory the exact current source and release surfaces that Arc05 must
plan across: source files, generated package roots, README routes, `SKILL.md`
entrypoints, Makefile package lists, templates, guide files, package-path
exceptions, validation commands, and CCDP boundaries. Produce the mapping that
later slices use; do not design final edits yet.

Blocks: Slice 02 component contract and file plan.

Durable analysis outputs belong under the slice-local `artifacts/` directory.

### Slice 02: Component Contract And File Plan

Directory: `slice02-component-contract-file-plan`

Status: placeholder.

Scope: convert the accepted architecture and Slice01 inventory into a
component-by-component file plan: entrypoints, guide names, version histories,
support assets, source-to-package movement/copy strategy, package-local links,
and deferred items. Do not write implementation files.

Blocks: Slice 03 package, README, and validation plan.

### Slice 03: Package, README, And Validation Plan

Directory: `slice03-package-readme-validation-plan`

Status: placeholder.

Scope: plan the release surface: README updates, top-level composer
wayfinding, component package targets, Makefile lists, generated zip behavior,
package-path exceptions, validation commands, accepted warnings, migration
notes, and CCDP separation.

Blocks: Slice 04 implementation sequence synthesis.

### Slice 04: Implementation Sequence Synthesis

Directory: `slice04-implementation-sequence-synthesis`

Status: placeholder.

Scope: synthesize the component file plan and release-surface plan into the
final source-implementation roadmap. Produce the ordered implementation
slices, source-edit risk register, validation matrix, acceptance gates, and
Arc05 close-readiness evidence.

Blocks: Arc05 close and source implementation work.

## Dependencies

Consumes:

- Closed Project01 path/package contract and validation constraints.
- Closed Arc04 accepted architecture and implementation inputs.
- Current source checkout as read-only evidence.

Leaves for later work:

- A detailed source-edit implementation plan.
- Component package/source contracts for all accepted components.
- README and `SKILL.md` wayfinding plan.
- Makefile/package target and generated zip plan.
- Validation gates and migration notes.
- Explicit source implementation slice order.

## Version History

### v1.0 - 2026-08-29

Placeholder opened with dependency on Arc 04 and Project 01 closure.

### v1.1 - 2026-08-31

Opened Arc05 after Arc04 closed/composed and Project01 closure evidence was
reproduced. Planned four implementation-planning slices and opened Slice01 for
implementation surface mapping.
