# Slice 01: Release Surface Audit

```yaml
project: project01-harmonise-paths
arc: arc04-release-and-adoption-hardening
slice: slice01-release-surface-audit
status: open
opened-on: 2026-08-29
artifact-home: artifacts/
depends-on:
  - arc01-distribution-path-contract
  - arc02-skill-bundle-harmonisation
  - arc03-ccdp-distribution-package
implementation-checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning-worktree: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
```

## Capability

Determine exactly what remains before Project 01 can close from a release and
adoption perspective.

This slice is diagnosis/design-input only. It should produce durable audit
artifacts under `artifacts/`, update this slice ledger, and write a
`closing-report.md`. It should not edit source files.

## Inputs

- `../../project-plan.md`
- `../../ledger.md`
- `../arc-plan.md`
- `../ledger.md`
- `../../arc01-distribution-path-contract/closing-report.md`
- `../../arc02-skill-bundle-harmonisation/closing-report.md`
- `../../arc03-ccdp-distribution-package/closing-report.md`
- implementation checkout `README.md`
- implementation checkout `Makefile`
- implementation checkout `package-path-exceptions.tsv`
- implementation checkout `scripts/check-package-paths`
- implementation checkout `scripts/check-ccdp-package`
- implementation checkout `protocols/ccdp/README.md`

## Scope

Audit the current release/adoption surface against Project 01's definition of
done:

- source-clone workflow visibility for collaboration framework, project
  management/SDLC docs, language skills, and CCDP;
- generated skill zip workflow visibility;
- unzipped/installed skill workflow visibility;
- CCDP package workflow visibility;
- Makefile help and target discoverability;
- package-path gate and CCDP package gate discoverability;
- remaining warning/exception policy and whether any warning class is
  release-blocking;
- whether the project ledger's remaining open rows can close as-is, need a
  repair slice, or need a project-level acceptance slice only.

## Out of Scope

- Source edits.
- Package checker implementation changes.
- Release publication, tagging, or remote upload.
- Broad mature language guide warning burn-down.
- CCDP protocol semantic changes.
- Moving or including workbench/prompts material.

## Artifact Requirements

Durable slice artifacts belong under:

```text
project01-harmonise-paths/arc04-release-and-adoption-hardening/slice01-release-surface-audit/artifacts/
```

Expected artifacts:

- `release-surface-inventory.md`: source files, docs, Makefile targets, zip
  surfaces, and package entrypoints inspected.
- `project-ledger-gap-map.md`: Project 01 open rows mapped to current evidence,
  repair needs, and close-readiness.
- `warning-release-disposition.md`: current `make check-package-paths`
  warnings and `package-path-exceptions.tsv` rows classified as
  release-blocking, non-blocking visible backlog, explicit exception, or later
  maintenance.
- `recommended-slice02-scope.md`: either a concrete repair-slice scope or an
  explicit no-op/acceptance-prep recommendation with rationale.
- command output captures for every verification command run.

## Verification Approach

Run from `/Users/oubiwann/lab/billosys/ai-engineering`:

```sh
make help
make check-package-paths
make check-ccdp-package
scripts/check-package-paths --check-exceptions-only
make all
make ccdp-package
make ccdp
git diff --check
git status --short --branch --untracked-files=all
```

Inspect:

```sh
rg -n "source clone|zip|unzipped|install|package root|repo-only|provenance|check-package-paths|check-ccdp-package|ccdp.zip|protocol package" README.md Makefile package-path-exceptions.tsv protocols/ccdp/README.md scripts/check-package-paths scripts/check-ccdp-package
```

Run from `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`:

```sh
git diff --check
find project01-harmonise-paths/arc04-release-and-adoption-hardening/slice01-release-surface-audit/artifacts -maxdepth 2 -type f -print
test -f project01-harmonise-paths/arc04-release-and-adoption-hardening/slice01-release-surface-audit/closing-report.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|Artifacts|Bubble-up to Arc 04" project01-harmonise-paths/arc04-release-and-adoption-hardening/slice01-release-surface-audit/closing-report.md
```

## Exit Criteria

- The audited release/adoption surface is documented with file/target-level
  evidence.
- Current source/package validation gates are reproduced and captured.
- Remaining Project 01 open ledger rows are mapped to evidence, needed repair,
  or project-close acceptance work.
- Remaining package-path warnings are classified for release impact.
- Slice 02 is recommended with concrete scope, or explicitly classified as
  unnecessary with a reason and re-entry condition.
- Durable artifacts live under this slice's `artifacts/` directory.
- The close report walks every ledger row and bubbles findings up to Arc 04.
