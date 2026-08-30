# Arc 04: Release and Adoption Hardening

```yaml
arc: arc04-release-and-adoption-hardening
status: active
project: project01-harmonise-paths
depends-on:
  - arc01-distribution-path-contract
  - arc02-skill-bundle-harmonisation
  - arc03-ccdp-distribution-package
blocks:
  - project01-harmonise-paths close
related:
  - README.md
  - Makefile
  - package-path-exceptions.tsv
  - scripts/check-package-paths
  - scripts/check-ccdp-package
  - protocols/ccdp/README.md
```

## Capability Statement

This arc hardens the release and adoption surface for Project 01. A human or
LLM arriving through the source checkout, generated skill zips, unzipped skill
bundles, or `ccdp.zip` should see the correct entrypoints, know which package
flow applies, and have a repeatable validation command set before the project
closes.

The arc is not a broad content-rewrite pass. It exists to make the already
implemented source/package path contract visible, documented, and acceptable
at project scale.

## Slice Breakdown

### Slice 01: Release Surface Audit

Status: verified/closed.

Scope: inventory the current release/adoption-facing surface, compare it to
the Project 01 definition of done and project ledger, and identify the smallest
repair or close-readiness work still needed. This is diagnosis/design-input
only; it should not edit source files.

Load-bearing for: deciding whether Slice 02 is a documentation/gate repair
slice, a no-op acceptance-prep slice, or a narrower remediation slice.

### Slice 02: Acceptance Prep and No-Repair Decision

Status: verified/closed.

Scope: record the CDC-verified no-repair decision from Slice 01, select the
final acceptance command set for Slice 03 and Project 01 close, map remaining
Arc 04 and Project 01 ledger rows to that evidence, and leave source unchanged
unless a concrete defect appears.

### Slice 03: Project Close Readiness

Status: active/opened.

Scope: reproduce the final project-scale acceptance command set, capture
release/adoption evidence under the slice-local `artifacts/` directory, walk
Arc 04 rows A-2 through A-6 and Project 01 rows P-2, P-3, P-4, and P-6 with
fresh evidence, and identify whether Arc 04 and Project 01 can proceed to
formal close or need remediation.

## Dependencies

Arc 04 consumes the executable path contract from Arc 01, the skill-bundle
harmonisation and remaining warning baseline from Arc 02, and the CCDP package
and reader guidance from Arc 03.

The current known baseline entering Arc 04 is:

- skill bundles: `make check-package-paths` exits 0 with 12 zips, 171 Markdown
  files scanned, 0 hard failures, 295 visible warnings, and 3 explicit
  exceptions;
- CCDP package: `make check-ccdp-package` exits 0 with 42 Markdown files
  scanned, 14 package references checked, and 0 shape, README, or Markdown
  path failures;
- root release guidance exists in `README.md`, with CCDP protocol guidance in
  `protocols/ccdp/README.md`.

## Boundaries

In scope:

- release/adoption documentation in the root README and protocol README;
- Makefile help and validation target discoverability;
- final package inventory and source/package workflow clarity;
- final classification of remaining warnings as release-blocking,
  non-blocking visible backlog, explicit exceptions, or later maintenance;
- project-scale acceptance evidence.

Out of scope:

- rewriting mature language guide prose for style or substance;
- eliminating every visible package-path warning solely to reach zero warnings;
- changing CCDP protocol semantics or runtime behavior;
- including CCDP `workbench/` or `prompts/` in `ccdp.zip`;
- publishing a GitHub release, pushing tags, or changing remote release state
  unless the operator explicitly opens that work.

## Version History

### v1.0 - 2026-08-29

Initial Arc 04 plan opened after Arc 03 close. Slice 01 starts with a release
surface audit so final repairs are based on the project DoD, current package
checks, and actual release-facing docs rather than assumption.

### v1.1 - 2026-08-29

Slice 01 marked verified/closed by CDC. The audit found no release-blocking
source gap, so Slice 02 was opened as an acceptance-prep/no-repair decision
slice rather than the originally stubbed repair slice.

### v1.2 - 2026-08-29

Slice 02 marked verified/closed by CDC. The no-repair decision held under
reproduced source/package gates, so Slice 03 opens directly on project-close
readiness instead of a repair iteration.
