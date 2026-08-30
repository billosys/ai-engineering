# Project Ledger Gap Map

Audit date: 2026-08-29

Project ledger inspected:

- `project01-harmonise-paths/ledger.md`

Current open Project 01 rows entering this audit:

- P-2
- P-3
- P-4
- P-6

Rows already marked done and relevant to Arc 04:

- P-5: CCDP documented source/package use path.
- P-9: Arc 03 closes with delivered CCDP distribution story.
- P-10: Arc 04 opens from Arc 03 findings.

## P-2

Criterion: skill bundles use path references that resolve from both source
clone entrypoints and generated zip/unzipped package entrypoints.

Current evidence:

- `artifacts/make-check-package-paths.txt` exits 0.
- It reports 12 zips scanned, 171 Markdown files scanned, 0 hard failures,
  295 warnings, 3 explicit exceptions, and 656 skipped external URLs.
- Arc 02 closing report records that remaining warnings are visible later work
  rather than ambiguous hard package failures.

Gap disposition: closeable at project close after project-scale reproduction of
`make check-package-paths`.

Repair need: none found in this audit.

## P-3

Criterion: repo-only, provenance-only, and example project paths are explicitly
classified instead of left as ambiguous missing package files.

Current evidence:

- `artifacts/check-package-paths-exceptions-only.txt` reports
  `exception schema ok: package-path-exceptions.tsv`.
- `package-path-exceptions.tsv` contains three explicit exceptions and five
  visible warning-policy rows.
- `artifacts/make-check-package-paths.txt` reports 3 explicit exceptions and
  no hard failures.

Gap disposition: closeable at project close after project-scale reproduction of
the exception-only check and package-path gate.

Repair need: none found in this audit.

## P-4

Criterion: Makefile packaging owns required staging transforms and package-path
validation.

Current evidence:

- `artifacts/release-surface-grep.txt` shows `Makefile` owns `all`, `skills`,
  `install`, `check-package-paths`, `ccdp-package`, and
  `check-ccdp-package`.
- `scripts/check-package-paths` owns generated skill zip path validation.
- `scripts/check-ccdp-package` owns CCDP package validation.
- Arc 02 and Arc 03 close reports record the staged-transform/package-checker
  composition evidence.

Gap disposition: closeable at project close after final inspection and command
reproduction.

Repair need: none found in this audit.

## P-6

Criterion: release-facing docs explain cloned-source and zip/unzipped
workflows.

Current evidence:

- `README.md` documents source loading, skill zip build/upload, unzipped
  install, `make check-package-paths`, and CCDP package commands.
- `protocols/ccdp/README.md` documents source protocol-root use and unzipped
  `ccdp/` package use.
- `artifacts/release-surface-grep.txt` records the matching source lines.

Gap disposition: closeable at project close after final inspection.

Repair need: none found in this audit.

## Arc 04 Rows

Arc 04 ledger rows A-2 through A-5 remain open because Arc 04 is still active,
not because this audit found source gaps. They can be closed at arc scale after
CDC verification of Slice 01 and the final project-close-readiness slice runs
the selected acceptance command set.

## Project-Close Readiness

Project 01 is not ready to close immediately from this slice alone because
Arc 04 has not closed and project-scale acceptance has not yet been performed.
However, this audit found no release-blocking source repair. The remaining
work is acceptance-prep/project-close evidence, not a source repair slice.
