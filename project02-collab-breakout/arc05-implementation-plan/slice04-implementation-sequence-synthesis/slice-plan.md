# Slice 04: Implementation Sequence Synthesis

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice04-implementation-sequence-synthesis
status: open
opened-on: 2026-08-31
artifact-home: artifacts/
depends-on:
  - ../arc-plan.md
  - ../ledger.md
  - ../slice01-implementation-surface-map:verified-closed
  - ../slice02-component-contract-file-plan:verified-closed
  - ../slice03-package-readme-validation-plan:verified-closed
blocks:
  - ../closing-report.md
  - source implementation work
related:
  - ../../project-plan.md
  - ../../ledger.md
  - ../arc-plan.md
  - ../ledger.md
  - ../slice01-implementation-surface-map/cdc-verification.md
  - ../slice01-implementation-surface-map/artifacts/implementation-surface-inventory.md
  - ../slice01-implementation-surface-map/artifacts/release-validation-surface-map.md
  - ../slice02-component-contract-file-plan/cdc-verification.md
  - ../slice02-component-contract-file-plan/artifacts/component-contract-matrix.md
  - ../slice02-component-contract-file-plan/artifacts/component-file-layout-plan.md
  - ../slice02-component-contract-file-plan/artifacts/source-to-component-migration-plan.md
  - ../slice02-component-contract-file-plan/artifacts/package-source-contract-register.md
  - ../slice02-component-contract-file-plan/artifacts/support-adapter-dependency-plan.md
  - ../slice03-package-readme-validation-plan/cdc-verification.md
  - ../slice03-package-readme-validation-plan/artifacts/package-target-plan.md
  - ../slice03-package-readme-validation-plan/artifacts/readme-wayfinding-plan.md
  - ../slice03-package-readme-validation-plan/artifacts/skill-entrypoint-validation-plan.md
  - ../slice03-package-readme-validation-plan/artifacts/package-path-link-exception-plan.md
  - ../slice03-package-readme-validation-plan/artifacts/migration-compatibility-plan.md
  - ../slice03-package-readme-validation-plan/artifacts/slice04-implementation-sequence-inputs.md
  - ../../arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/artifacts/operator-accepted-architecture.md
```

## Goal

Synthesize the verified Arc05 planning outputs into the final source-edit
roadmap for implementing the accepted collaboration-framework breakout.

This slice does not implement the breakout. It produces the ordered
implementation slices, risk register, validation matrix, acceptance gates,
source-implementation handoff packet, and Arc05 close-readiness assessment
needed before source work begins.

## Scope

In scope:

- Consume verified Arc05 Slice01 through Slice03 outputs and the
  operator-accepted Arc04 architecture.
- Produce the final ordered implementation sequence for all eight accepted
  components: `collaboration-framework`, `engineering-methods`,
  `project-management`, `work-verification`, `testing`, `code-auditing`,
  `agent-coordination`, and `contribution-style`.
- Decide sequencing for mechanical source moves, new component prose,
  compatibility handling, README route updates, component `SKILL.md`
  entrypoints, sibling `version-history.md` files, Makefile/package targets,
  package-path/link repairs, package exceptions, generated zip validation, and
  final source-cleanliness checks.
- Identify implementation risks, mitigation ordering, acceptance gates, and
  validation commands.
- Produce a handoff packet that can be used to open source implementation work
  without re-reading every Arc05 artifact.
- Assess whether Arc05 can close after this slice once CDC verification is
  complete.

Out of scope:

- Editing source checkout files.
- Creating component roots in the source checkout.
- Editing README, top-level `SKILL.md`, Makefile, source guides, templates,
  package-path exceptions, generated zips, or CCDP files.
- Closing Arc05 before this slice has CC close evidence and CDC verification.
- Authorizing source implementation without an explicit post-Arc05 transition.

## Required Artifacts

Produce durable artifacts under `artifacts/`:

- `implementation-sequence-roadmap.md` - ordered source-edit slices with
  dependencies, sequencing rationale, expected commit boundaries, and
  component coverage.
- `source-edit-risk-register.md` - implementation risks, affected surfaces,
  mitigation steps, and validation or acceptance evidence for each risk.
- `validation-matrix.md` - validation commands, when they run, what they prove,
  what would fail if the implementation drifted, and which gates are
  conditional on touched surfaces.
- `acceptance-gate-plan.md` - Arc05 and source-implementation acceptance gates,
  operator decision points, required proof, and non-go conditions.
- `implementation-prompt-packet.md` - compact source-implementation handoff
  for CC/CDC use, including source-edit slice order, explicit context packet
  requirements, commit-scope rules, and no-source-edit caveat for this slice.
- `arc05-close-readiness.md` - assessment of whether Arc05 can close after
  Slice04 verification, including remaining open questions, deferrals, and
  source files untouched evidence.

## Verification Approach

The slice verifies by checking that the artifacts exist, consume verified
Arc05 inputs, cover all eight accepted components, provide an ordered
implementation sequence, record risks and mitigations, define validation and
acceptance gates, prepare a source-implementation handoff packet, assess Arc05
close readiness, and leave source files untouched.

## Exit Criteria

- The final source-edit roadmap covers all eight accepted components and all
  cross-cutting package/source/release gates.
- The sequence separates mechanical moves, component prose creation, README
  and entrypoint route updates, Makefile/package changes, path repairs,
  exception review, validation, and acceptance checks.
- Compatibility choices for the top-level `SKILL.md` and old source/prompt
  names are explicitly sequenced.
- Package-local, installed-skill, source-checkout, generated zip, and
  provenance path strategies have a validation plan.
- CCDP separation remains explicit.
- Implementation risks are mitigated or carried forward with a named gate.
- The source-implementation handoff is usable without treating planning
  artifacts as source-edit authorization.
- Source files remain untouched.

## Closure State

Slice04 is open. It closes only after CC produces the required artifacts,
updates this slice ledger and plan, writes `closing-report.md`, commits the
explicit Slice04 file list, and CDC independently verifies the close packet.
