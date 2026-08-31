# Slice 03: Package, README, And Validation Plan

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice03-package-readme-validation-plan
status: proposed-done
opened-on: 2026-08-31
artifact-home: artifacts/
depends-on:
  - ../arc-plan.md
  - ../ledger.md
  - ../slice01-implementation-surface-map:verified-closed
  - ../slice02-component-contract-file-plan:verified-closed
blocks:
  - ../slice04-implementation-sequence-synthesis
related:
  - ../../project-plan.md
  - ../../ledger.md
  - ../arc-plan.md
  - ../ledger.md
  - ../slice01-implementation-surface-map/cdc-verification.md
  - ../slice01-implementation-surface-map/artifacts/release-validation-surface-map.md
  - ../slice02-component-contract-file-plan/cdc-verification.md
  - ../slice02-component-contract-file-plan/artifacts/component-contract-matrix.md
  - ../slice02-component-contract-file-plan/artifacts/component-file-layout-plan.md
  - ../slice02-component-contract-file-plan/artifacts/package-source-contract-register.md
  - ../slice02-component-contract-file-plan/artifacts/source-to-component-migration-plan.md
  - ../slice02-component-contract-file-plan/artifacts/support-adapter-dependency-plan.md
  - ../slice02-component-contract-file-plan/artifacts/slice03-package-readme-validation-inputs.md
  - ../../arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/artifacts/operator-accepted-architecture.md
```

## Goal

Plan the release surface for the accepted component breakout before source
implementation begins.

This slice converts the verified component contracts and file layout into a
package, README, `SKILL.md`, Makefile, generated zip, package-path exception,
validation, and migration plan. It must preserve the daily-driver
`collaboration-framework` composer, support standalone component use, distinguish
source checkout, generated zip, unzipped/install, and installed skill reader
modes, and keep CCDP separate.

## Scope

In scope:

- Consume the verified Slice01 release validation surface map and verified
  Slice02 component contract/file-plan artifacts.
- Plan package names, package roots, generated zip behavior, install behavior,
  and package target/list impacts for all eight accepted components.
- Plan README guidance for composed `collaboration-framework` use, standalone
  component use, source checkout use, generated zip/unzipped use, installed
  skill use, component usefulness, migration notes, and CCDP separation.
- Plan top-level composer `SKILL.md` behavior and new component `SKILL.md`
  entrypoint validation coverage without writing final entrypoint prose.
- Plan package-local link strategy, source-clone link strategy, installed-skill
  route wording, and package-path exception policy.
- Plan validation commands and acceptance gates, including `make check-skills`,
  `make check-package-paths`, component package builds, `make all`, and CCDP
  package checks only when CCDP surfaces are touched.
- Plan compatibility/migration handling for old source paths and historical
  names without erasing provenance.
- Produce Slice04-ready implementation sequence inputs.

Out of scope:

- Editing source files.
- Creating component directories in the source checkout.
- Writing final README, `SKILL.md`, Makefile, package exception, guide,
  template, generated zip, or validation changes.
- Running package builds as proof of not-yet-written package changes.
- Closing Arc05.

## Required Artifacts

Produce durable artifacts under `artifacts/`:

- `package-target-plan.md` - proposed package roots, generated zip names,
  install behavior, Makefile target/list impacts, aggregate target behavior,
  generated artifact policy, and CCDP separation.
- `readme-wayfinding-plan.md` - README presentation plan for component
  usefulness, composed use, standalone use, source checkout reading,
  generated zip/unzipped reading, installed skill loading, migration notes, and
  CCDP separation.
- `skill-entrypoint-validation-plan.md` - top-level composer `SKILL.md` plan,
  component `SKILL.md` validation plan, description/frontmatter checks, route
  tables, and component versioning/version-history expectations.
- `package-path-link-exception-plan.md` - source/package link strategy,
  package-local links, installed-skill route wording, source-only/provenance
  references, exception policy, and accepted warning handling.
- `migration-compatibility-plan.md` - compatibility plan for old source paths,
  old prompt names, current top-level `SKILL.md`, historical version histories,
  generated package roots, and provenance-preserving migration.
- `slice04-implementation-sequence-inputs.md` - concrete inputs, risks,
  validation gates, ordered concerns, and open questions for Slice04 final
  implementation sequence synthesis.

## Verification Approach

The slice verifies by checking that required artifacts exist, cite verified
Slice01 and Slice02 inputs, cover all eight accepted components, plan package,
README, `SKILL.md`, Makefile, generated zip, package-path exception, validation,
migration, and CCDP surfaces, produce Slice04-ready inputs, and leave the source
checkout clean.

## Exit Criteria

- All eight accepted components have package and README route treatment.
- The daily-driver `collaboration-framework` composer remains supported.
- Standalone component use is documented as useful without deprecating the
  composer.
- Source checkout, generated zip, unzipped/install, and installed skill reader
  modes are distinguished.
- `SKILL.md` entrypoint validation and component version-history expectations
  are planned.
- Makefile, generated zip, package-path exception, package-local link, and
  validation command impacts are planned without editing source.
- CCDP separation is preserved.
- Compatibility/migration risks for old paths and old prompt names are
  dispositioned.
- Slice04 receives final implementation-sequence inputs.
- No source files are edited.

## Closure State

Slice03 is proposed-done as of 2026-08-31. Required artifacts are under
`artifacts/`, `closing-report.md` has been written, ledger rows F-1 through
F-9 have attested evidence, source files remain untouched, and implementation
has not started. CDC verification is still required before the slice is
verified/closed.
