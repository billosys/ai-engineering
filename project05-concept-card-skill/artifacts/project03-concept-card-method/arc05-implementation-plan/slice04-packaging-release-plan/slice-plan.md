# Slice 04: Packaging, Discoverability, and Release Gates

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice04-packaging-release-plan
status: open
opened-on: 2026-08-31
opened-by: Codex Desktop CDC planning pass
depends-on:
  - ../arc-plan.md
  - ../ledger.md
  - ../slice01-source-surface-inventory/cdc-verification.md
  - ../slice02-source-layout-content-plan/cdc-verification.md
  - ../slice03-schema-validation-plan/cdc-verification.md
  - ../slice02-source-layout-content-plan/artifacts/v40-source-layout-plan.md
  - ../slice03-schema-validation-plan/artifacts/v40-schema-surface-plan.md
  - ../slice03-schema-validation-plan/artifacts/v40-validator-scope-test-plan.md
artifact-home: artifacts/
```

## Goal

Plan the packaging, discoverability, generated-artifact policy, release gates,
package-path checks, and source version-history obligations for implementing
the v4.0 concept-card method skill.

This is planning work only. It does not edit the source checkout, build a
package, or claim release readiness.

## Scope

In scope:

- Decide README and library discoverability requirements for the future
  `knowledge/concept-card-method/` skill.
- Decide Makefile/package-list planning requirements for adding the concept
  card method skill to package, install, and skill-check surfaces.
- Decide package-path validation expectations and whether package-path
  exception rows should be avoided, required, or deferred.
- Decide generated zip policy, generated archive checks, install behavior,
  clean behavior, and release-gate evidence expectations.
- Decide source version-history obligations for `SKILL.md`, guides, templates,
  examples, validation documentation, support documents, README, Makefile, and
  package-path exception surfaces.
- Preserve the planning-only boundary, Slice02 package-compatible layout, and
  Slice03 documentation-only validator-code scope.

Out of scope:

- Editing source `SKILL.md`, guide, template, example, README, Makefile,
  package-list, package-path, validator-code, generated-zip, or release files.
- Implementing Makefile targets, package list edits, package-path exception
  rows, README/library prose, tests, generated zips, package release,
  executable validator-code, release gates, CI changes, or source
  version-history text.
- Creating runtime services, GraphRAG, graph database, ontology database,
  memory runtime, CCDP service, or live extraction behavior.
- Reopening Slice02 layout or Slice03 schema/validation decisions unless a
  packaging fact forces a documented Arc05 plan update.
- Closing Arc05 or Project03.

## Required Artifacts

Durable Slice04 outputs belong under `artifacts/`:

- `artifacts/v40-package-update-plan.md`
- `artifacts/v40-discoverability-plan.md`
- `artifacts/v40-release-gate-plan.md`
- `artifacts/v40-version-history-plan.md`

## Verification Approach

The slice should be verifiable by file existence, package-surface coverage,
discoverability coverage, release-gate coverage, source version-history
coverage, later-slice routing, and source checkout cleanliness.

The artifacts should distinguish accepted package/discoverability/release
planning decisions from source edits and release claims, which remain out of
scope until implementation.

## Exit Criteria

- The slice open set exists: `slice-plan.md`, `ledger.md`, `cc-prompt.md`, and
  `artifacts/`.
- The four required artifacts exist under `artifacts/`.
- The package update plan covers Makefile, package target names, package list
  edits, install behavior, clean behavior, generated archive behavior,
  package-path checks, package-path exceptions, and package update boundaries.
- The discoverability plan covers README, skill library text, skill
  description, tags/metadata, reason to load, promise boundary, adjacent-skill
  routing, and operator-facing package expectations.
- The release gate plan covers skill checks, package-path checks, generated
  zip checks, source checkout cleanliness, planning checkout hygiene, package
  installability, documentation-only validator scope, and release-readiness
  evidence.
- The version history plan names source version-history obligations for
  `SKILL.md`, guides, templates, examples, validation documentation, support
  documents, README, Makefile, and package-path exception surfaces.
- The artifacts preserve the Slice02 package-compatible `guides/` layout and
  the Slice03 documentation-only validator-code scope.
- The artifacts route implementation synthesis, implementation-slice
  recommendations, deferral register, and Project03 close input to Slice05.
- The artifacts keep source edits, source implementation, generated zips,
  package release, executable validator-code, runtime services, and release
  readiness out of scope.
- The source checkout remains clean.
- New and modified Slice04 Markdown is ASCII-clean and has no trailing
  whitespace.

## Bubble-up Expectations

At close, report whether Slice04 found any packaging, discoverability,
release-gate, generated-artifact, package-path, or version-history fact that
requires Arc05 re-sequencing, a new slice, or a scope correction. If no such
finding is found, say so explicitly.

Slice04 should prepare Slice05 to synthesize the full implementation plan and
Project03 close input from verified layout, schema, validation, packaging,
discoverability, and release-gate decisions.
