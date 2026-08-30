# Arc 04 Closing Report: Release and Adoption Hardening

```yaml
project: project01-harmonise-paths
arc: arc04-release-and-adoption-hardening
status: closed
closed-by: CDC
closed-on: 2026-08-29
composition-verdict: delivered
```

## Capability Restated

Arc 04 hardens the release and adoption surface for Project 01. A human or LLM
arriving through the source checkout, generated skill zips, unzipped skill
bundles, or `ccdp.zip` should see the correct entrypoints, know which package
flow applies, and have repeatable validation commands before the project
closes.

## Composition Verdict

Composition verdict: delivered.

The three slices compose into the promised capability:

- Slice 01 audited the release/adoption surface and found no release-blocking
  source repair gap.
- Slice 02 converted that audit into an explicit no-repair decision, final
  acceptance command set, and Arc/Project close map.
- Slice 03 reproduced the final project-scale acceptance command set and
  prepared Arc 04 and Project 01 for formal close.

The final arc-scale demonstration builds and validates all skill bundles,
validates `ccdp.zip` zipped and unzipped, checks exception policy, confirms
release/adoption wording, preserves source `make ccdp`, and leaves the source
checkout free of tracked drift.

## Slice Walk

### Slice 01: Release Surface Audit

Outcome: delivered and CDC-verified.

Evidence:

- `slice01-release-surface-audit/cdc-verification.md`

### Slice 02: Acceptance Prep and No-Repair Decision

Outcome: delivered and CDC-verified.

Evidence:

- `slice02-acceptance-prep-no-repair/cdc-verification.md`

### Slice 03: Project Close Readiness

Outcome: delivered and CDC-verified.

Evidence:

- `slice03-project-close-readiness/cdc-verification.md`

## Arc Ledger Walk

### A-1

Status: done.

Slice 01 has CDC verification at
`slice01-release-surface-audit/cdc-verification.md`.

### A-2

Status: done.

CDC reproduced the final release-facing workflow from the source checkout:
`make help`, `make check-package-paths`, `make check-ccdp-package`,
`scripts/check-package-paths --check-exceptions-only`, `make all`,
`make ccdp-package`, `make ccdp`, release-surface grep, `git diff --check`,
and final source status all passed.

### A-3

Status: done.

The release/adoption surface distinguishes source clone, generated skill zip,
unzipped/installed skill, and `ccdp.zip` protocol-package workflows. Evidence
comes from Slice 03 `artifacts/release-surface-readiness.md`,
`artifacts/release-surface-grep.txt`, and CDC-reproduced grep output.

### A-4

Status: done.

Remaining package-path warnings are classified and release-acceptable. The
skill package gate exits 0 with 12 zips scanned, 171 Markdown files scanned,
0 hard failures, 295 visible warnings, 3 explicit exceptions, and 656 skipped
external URLs. The exception schema remains valid.

### A-5

Status: done.

Makefile/package checker ownership is discoverable. `make help`, README,
Makefile, and checker scripts expose `check-package-paths`,
`check-ccdp-package`, `ccdp-package`, install, zip, unzip, and package-root
language.

### A-6

Status: done.

Project close readiness is explicitly routed through Slice 03
`artifacts/close-recommendation.md` and this arc close. Project 01 can close
without a remediation arc under current evidence.

### A-7

Status: done.

Slice 02 was opened from Slice 01 findings and recorded in `arc-plan.md`
Version History v1.1.

### A-8

Status: done.

Slice 03 was opened from Slice 02 findings and recorded in `arc-plan.md`
Version History v1.2.

### A-9

Status: done.

Slice 03 has CDC verification at
`slice03-project-close-readiness/cdc-verification.md`.

## Arc-Scale Evidence

From `/Users/oubiwann/lab/billosys/ai-engineering`:

- `make help`
  - passes and exposes release/package targets
- `make check-package-paths`
  - passes with 12 zips, 171 Markdown files, 0 hard failures, 295 warnings,
    3 explicit exceptions, and 656 skipped external URLs
- `make check-ccdp-package`
  - passes with 42 Markdown files scanned, 14 package references checked,
    91 protocol-syntax skips, 4 external URLs skipped, 0 shape errors,
    0 README errors, and 0 Markdown path failures
  - extracted-package assembly succeeds
- `scripts/check-package-paths --check-exceptions-only`
  - passes
- `make all`
  - passes
- `make ccdp-package`
  - passes and produces `ccdp.zip` with one `ccdp/` root and 122 entries
- `make ccdp`
  - passes
- release-surface grep
  - passes and confirms source clone, zip, unzipped/install, package root,
    repo-only/provenance, package-check, and CCDP package wording
- `git diff --check`
  - passes
- `git status --short --branch --untracked-files=all`
  - `## main...origin/main [ahead 3]`

## Accumulated Arc-Plan Change Log

Arc 04 changed as its slices closed:

- v1.1: Slice 01 verified/closed; no release-blocking source gap found, so
  Slice 02 opened as acceptance-prep/no-repair rather than repair.
- v1.2: Slice 02 verified/closed; no-repair held under reproduced gates, so
  Slice 03 opened on project-close readiness.
- v1.3: Slice 03 verified/closed; final acceptance evidence reproduced, so
  Arc 04 closes and Project 01 can close without remediation.

## Bubble-up to Project 01

Arc 04 delivered the release/adoption hardening capability in the Project 01
roadmap.

Project impact:

- Project 01 rows P-2, P-3, P-4, and P-6 can close from the reproduced Slice
  03 and Arc 04 evidence.
- No project-plan expansion or remediation arc is required.
- Project 02 is no longer blocked by Project 01 once the Project 01 close
  report lands.

Silent-drop diff:

- Scope specified: release/adoption audit, no-repair/acceptance-prep decision,
  final project-scale acceptance evidence, release-surface clarity, Makefile
  and checker discoverability, warning/exception disposition, and project
  close readiness.
- Scope delivered: all specified items were delivered through Slice 01, Slice
  02, Slice 03, this arc ledger walk, and reproduced acceptance gates.
- Silent drops: none found.

## What Worked

Running the final project-scale command set once in Slice 03 and again during
CDC verification gave the arc a clear composition demonstration rather than a
stack of inherited child claims.
