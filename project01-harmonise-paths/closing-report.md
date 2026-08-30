# Project 01 Closing Report: Harmonise Paths

```yaml
project: project01-harmonise-paths
status: closed
closed-by: CDC
closed-on: 2026-08-29
dod-verdict: met
gate: go
```

## Definition of Done Restated

Project 01 is done when humans and LLMs can use the ai-engineering materials
from either the cloned source tree or the generated zip/unzipped bundles
without having to rediscover where referenced files actually live.

## DoD Verdict

DoD verdict: met.

Gate: go.

The project closes with source/package validation reproduced at project scale,
Arc 01 through Arc 04 closed, and no remaining repair slice or remediation arc
required by current evidence.

## Arc Walk

### Arc 01: Distribution Path Contract

Outcome: delivered and closed.

Evidence:

- `arc01-distribution-path-contract/closing-report.md`

### Arc 02: Skill Bundle Harmonisation

Outcome: delivered and closed.

Evidence:

- `arc02-skill-bundle-harmonisation/closing-report.md`

### Arc 03: CCDP Distribution Package

Outcome: delivered and closed.

Evidence:

- `arc03-ccdp-distribution-package/closing-report.md`

### Arc 04: Release and Adoption Hardening

Outcome: delivered and closed.

Evidence:

- `arc04-release-and-adoption-hardening/closing-report.md`

## Project Ledger Walk

### P-1

Status: done.

Arc 01 closed with composition verdict delivered. Project close accepts that
path contract as the basis for the final package validation gates.

### P-2

Status: done.

Skill bundles use path references that resolve from source clone entrypoints
and generated zip/unzipped package entrypoints. CDC reproduced
`make check-package-paths`: 12 zips scanned, 171 Markdown files scanned, 0 hard
failures, 295 visible warnings, 3 explicit exceptions, and 656 skipped
external URLs.

### P-3

Status: done.

Repo-only, provenance-only, and example project paths are classified rather
than left as ambiguous missing package files. CDC reproduced
`scripts/check-package-paths --check-exceptions-only`, which passed with
`exception schema ok: package-path-exceptions.tsv`; remaining warnings stay
visible.

### P-4

Status: done.

Makefile packaging owns staging transforms and package-path validation. CDC
reproduced `make help`, `make all`, `make check-package-paths`, and
`make check-ccdp-package`, and confirmed release-surface grep coverage across
README, Makefile, package policy, and checker scripts.

### P-5

Status: done.

CCDP has a documented source and distributable package use path. CDC
reproduced `make ccdp-package`, `make check-ccdp-package`, and `make ccdp`.
`ccdp.zip` has one `ccdp/` package root and 122 entries; the CCDP package gate
reports 0 shape, README, and Markdown path failures.

### P-6

Status: done.

Release-facing docs explain cloned-source and zip/unzipped workflows. CDC
reproduced release-surface grep showing source clone, generated skill zip,
unzipped/install, package root, repo-only/provenance, `ccdp.zip`, and protocol
package wording across the release/adoption surface.

### P-7

Status: done.

Arc 02 closed with generated skill-bundle path harmonisation composed. Project
close reproduced the final skill-bundle package path gate, so this row is not
closed by inherited child evidence alone.

### P-8

Status: done.

Arc 03 opened from Arc 02 findings and the project-plan Version History records
the transition.

### P-9

Status: done.

Arc 03 closed with a delivered CCDP source/package distribution story. Project
close reproduced the CCDP package and `make ccdp` gates.

### P-10

Status: done.

Arc 04 opened from Arc 03 findings and the project-plan Version History records
the transition.

### P-11

Status: done.

Arc 04 closed with release/adoption hardening delivered. Its close report
walks A-1 through A-9, reproduces the final acceptance command set, and bubbles
no remediation requirement to Project 01.

## Project-Scale Evidence

From `/Users/oubiwann/lab/billosys/ai-engineering`:

- `make help`
  - passes and exposes skill bundle, install, package-path, CCDP, and CCDP
    package validation targets
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

## Bubble-up and Remediation

No remediation arc is required.

Remaining package-path warnings are intentionally visible and non-blocking at
this project boundary. They are not hidden broad suppressions; they are later
maintenance/backlog items while the package gates enforce 0 hard failures and
valid explicit exceptions.

Project 02 may proceed after the operator accepts this Project 01 close.

Silent-drop diff:

- Scope specified: cloned-source usability, generated zip/unzipped package
  usability, explicit classification for unbundled material, Makefile-owned
  staging/checking, CCDP distribution, and release-facing workflow guidance.
- Scope delivered: Arc 01 through Arc 04 compose into that definition of done,
  with project-scale acceptance gates reproduced at close.
- Silent drops: none found.

## What Worked

The project landed cleanly because each arc left a machine-checkable boundary:
path semantics, generated-skill package validation, CCDP package validation,
and release/adoption acceptance. The final close could therefore reproduce the
whole surface instead of re-arguing individual path references.
