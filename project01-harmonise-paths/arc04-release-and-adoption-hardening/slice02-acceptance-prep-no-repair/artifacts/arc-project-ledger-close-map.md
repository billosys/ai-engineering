# Arc and Project Ledger Close Map

Decision date: 2026-08-29

Purpose: map Arc 04 and Project 01 open rows to the final acceptance evidence
that Slice 03 and project close should reproduce.

## Arc 04 Rows

### A-2

Criterion: final release-facing workflow is demonstrable from the source
checkout.

Close evidence:

- Run the source checkout command set in
  `artifacts/final-acceptance-command-set.md`.
- Required proof: all commands exit 0, package-path summary remains 0 hard
  failures, CCDP package summary remains 0 shape/README/Markdown path failures,
  and source status remains free of tracked drift.

Expected close: done at Arc 04 close after Slice 03 reproduces the command set.

### A-3

Criterion: release/adoption docs distinguish skill zips, unzipped installed
skills, source-clone use, and `ccdp.zip`.

Close evidence:

- Inspect `README.md`, `Makefile` help, `protocols/ccdp/README.md`, and
  release-surface grep output.
- Required proof: source clone, generated skill zip, unzipped/installed skill,
  and CCDP package workflows are all visible and context-labelled.

Expected close: done at Arc 04 close if the release-surface grep remains
consistent with Slice 01 and Slice 02 evidence.

### A-4

Criterion: remaining package-path warnings are classified as release-blocking,
non-blocking visible backlog, explicit exception, or later maintenance.

Close evidence:

- `make check-package-paths`
- `scripts/check-package-paths --check-exceptions-only`
- `package-path-exceptions.tsv`
- Slice 01 `warning-release-disposition.md`
- Slice 02 `no-repair-decision.md`

Required proof: 0 hard failures, 295 visible warnings, 3 explicit exceptions,
valid exception schema, and no newly discovered release-blocking warning class.

Expected close: done at Arc 04 close.

### A-5

Criterion: Makefile/package checker ownership is discoverable from
release-facing docs.

Close evidence:

- `make help`
- release-surface grep over `README.md`, `Makefile`, and checker scripts.

Required proof: `check-package-paths`, `check-ccdp-package`, `ccdp-package`,
`install`, and unzip/package language are discoverable.

Expected close: done at Arc 04 close.

### A-6

Criterion: Project close readiness is explicitly routed.

Close evidence:

- Slice 02 `slice03-readiness-scope.md`
- Slice 03 close report
- Arc 04 close report
- Project 01 plan/ledger updates made during project close, if needed.

Required proof: Slice 03 is scoped to project-close readiness and no repair
slice is required unless a re-entry condition fires.

Expected close: done after Slice 03 closes and Arc 04 bubbles readiness to
Project 01.

## Project 01 Rows

### P-2

Criterion: skill bundles use path references that resolve from both source
clone entrypoints and generated zip/unzipped package entrypoints.

Close evidence:

- `make check-package-paths`
- `make all`
- release-surface grep for skill zip/unzipped/install guidance.

Required proof: 12 generated skill zips scanned, 171 Markdown files scanned, 0
hard failures, accepted visible warning/exception baseline, and no tracked
source drift.

Expected close: done at Project 01 close after project-scale reproduction.

### P-3

Criterion: repo-only, provenance-only, and example project paths are explicitly
classified instead of left as ambiguous missing package files.

Close evidence:

- `make check-package-paths`
- `scripts/check-package-paths --check-exceptions-only`
- `package-path-exceptions.tsv`
- Slice 01 and Slice 02 warning/no-repair artifacts.

Required proof: explicit exceptions remain narrow and schema-valid; warnings
remain visible rather than hidden.

Expected close: done at Project 01 close after project-scale reproduction.

### P-4

Criterion: Makefile packaging owns required staging transforms and package-path
validation.

Close evidence:

- `make help`
- release-surface grep over `Makefile`, `scripts/check-package-paths`,
  `scripts/check-ccdp-package`, and `README.md`.
- `make check-package-paths`
- `make check-ccdp-package`

Required proof: public Make targets own package building/checking and delegate
to the checker scripts; both gates pass.

Expected close: done at Project 01 close.

### P-6

Criterion: release-facing docs explain cloned-source and zip/unzipped
workflows.

Close evidence:

- release-surface grep over `README.md`, `Makefile`,
  `protocols/ccdp/README.md`, and checker scripts.
- `make help`

Required proof: root README and CCDP README explain source clone, skill zip,
unzipped/installed skill, and `ccdp.zip` workflows.

Expected close: done at Project 01 close.

## Non-Inherited Composition Guard

Slice 03 should not close these rows solely by pointing at Slice 01 or Slice 02.
It should rerun the final acceptance command set, inspect the release-surface
grep output, and record the reproduced project-scale evidence in its own
artifacts.
