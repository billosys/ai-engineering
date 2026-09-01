# Slice 05: Implementation Plan Synthesis and Project Close Input

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice05-implementation-plan-synthesis
status: open
opened-on: 2026-08-31
opened-by: Codex Desktop CDC planning pass
depends-on:
  - ../arc-plan.md
  - ../ledger.md
  - ../slice01-source-surface-inventory/cdc-verification.md
  - ../slice02-source-layout-content-plan/cdc-verification.md
  - ../slice03-schema-validation-plan/cdc-verification.md
  - ../slice04-packaging-release-plan/cdc-verification.md
  - ../slice02-source-layout-content-plan/artifacts/v40-source-layout-plan.md
  - ../slice03-schema-validation-plan/artifacts/v40-schema-surface-plan.md
  - ../slice03-schema-validation-plan/artifacts/v40-validation-review-plan.md
  - ../slice04-packaging-release-plan/artifacts/v40-package-update-plan.md
  - ../slice04-packaging-release-plan/artifacts/v40-release-gate-plan.md
artifact-home: artifacts/
```

## Goal

Synthesize verified Arc05 planning outputs into the accepted implementation
plan for the v4.0 concept-card method skill. The slice should produce the
future source edit sequence, verification gate matrix, implementation-slice
recommendations, deferral register, and Project03 close input.

This is the final Arc05 planning slice. It does not perform source edits,
release work, or Project03 closure.

## Scope

In scope:

- Compose Slice01 source-surface inventory, Slice02 source layout/content
  sequence, Slice03 schema/enum/validation plan, and Slice04
  packaging/discoverability/release-gate plan into one implementation plan.
- Define a source edit sequence for `knowledge/concept-card-method/`, README,
  Makefile, package lists, package-path behavior, package checks, generated zip
  verification, and source version-history obligations.
- Define a verification gate matrix for future implementation work.
- Recommend future implementation slices, including inputs, outputs, checks,
  source paths, and commit boundaries.
- Record a deferral register with explicit owners and re-entry conditions for
  work outside Project03 planning.
- Produce Project03 close input that states what Arc05 delivers, what remains
  deferred, and what evidence should be available for Arc05 and Project03
  close.

Out of scope:

- Editing source `SKILL.md`, guide, template, example, README, Makefile,
  package-list, package-path, validator-code, generated-zip, or release files.
- Implementing the concept-card method skill, Makefile targets, package list
  edits, package-path exception rows, README/library prose, tests, generated
  zips, package release, executable validator-code, release gates, CI changes,
  or source version-history text.
- Creating runtime services, GraphRAG, graph database, ontology database,
  memory runtime, CCDP service, or live extraction behavior.
- Closing Arc05 or Project03; this slice prepares close input only.

## Required Artifacts

Durable Slice05 outputs belong under `artifacts/`:

- `artifacts/v40-implementation-plan.md`
- `artifacts/v40-source-edit-sequence.md`
- `artifacts/v40-verification-gate-matrix.md`
- `artifacts/v40-implementation-slice-recommendations.md`
- `artifacts/v40-deferral-register.md`
- `artifacts/project03-close-input.md`

## Verification Approach

The slice should be verifiable by file existence, explicit synthesis of
Slice01 through Slice04 outputs, source edit sequence coverage, verification
gate coverage, implementation-slice recommendation coverage, deferral
register quality, Project03 close-input coverage, and source checkout
cleanliness.

The artifacts should distinguish implementation planning from implementation
evidence and release evidence.

## Exit Criteria

- The slice open set exists: `slice-plan.md`, `ledger.md`, `cc-prompt.md`, and
  `artifacts/`.
- The six required artifacts exist under `artifacts/`.
- The implementation plan composes verified Slice01, Slice02, Slice03, and
  Slice04 outputs and preserves accepted Arc03/Arc04 decisions.
- The source edit sequence covers `knowledge/concept-card-method/SKILL.md`,
  `guides/`, templates, examples, validation documentation, support documents,
  README, Makefile, package lists, package-path behavior, generated zip
  verification, and source version-history obligations.
- The verification gate matrix covers source checkout cleanliness, planning
  checkout hygiene, `make check-skills`, concept-card package build, generated
  zip listing, `make check-package-paths`, installability, documentation-only
  validator scope, README/library discoverability, and version-history checks.
- The implementation-slice recommendations split future source edit work into
  bounded slices with inputs, outputs, source paths, checks, and commit
  boundaries.
- The deferral register records deferred work, owners, rationale, and re-entry
  conditions for executable validator-code, runtime systems, package release,
  generated release artifacts, and any other out-of-scope work.
- The Project03 close input evaluates Project03 definition-of-done coverage,
  Arc05 close readiness, project-close readiness, remaining deferrals, and
  evidence needed for closure.
- The artifacts support Arc05 composition rows A-6, A-7, A-8, and A-9 without
  claiming source implementation or release readiness.
- The artifacts keep source edits, source implementation, generated zips,
  package release, executable validator-code, runtime services, and release
  readiness out of scope.
- The source checkout remains clean.
- New and modified Slice05 Markdown is ASCII-clean and has no trailing
  whitespace.

## Bubble-up Expectations

At close, report whether Slice05 found any implementation-planning fact that
requires Arc05 re-sequencing, a remediation slice, an arc-scope correction, or
Project03 roadmap correction. If no such finding is found, say so explicitly.

Because Slice05 is the last Arc05 slice, its close should state whether Arc05
is ready for formal arc close after CDC verification.
