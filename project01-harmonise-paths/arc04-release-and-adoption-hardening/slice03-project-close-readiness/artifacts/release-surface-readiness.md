# Release Surface Readiness

Run date: 2026-08-29

Evidence:

- `make-help.txt`
- `release-surface-grep.txt`
- `make-check-package-paths.txt`
- `make-check-ccdp-package.txt`
- `check-package-paths-exceptions-only.txt`

## Verdict

The release/adoption surface is ready for Arc 04 formal close.

It distinguishes source-clone use, generated/installable skill zips,
unzipped/installed skill use, `ccdp.zip` protocol package use, and
repo-only/provenance/excluded material.

## Source Clone Use

Ready.

The root README includes source-clone orientation for project-management and
skill use. The release-surface grep captured source-facing references in
`README.md` and source-only/provenance labels in both the root README and
protocol README.

## Generated Skill Zips

Ready.

`README.md` and `Makefile` expose the skill package targets:

- `make skills`
- `make collab-framework`
- per-domain zip targets
- `make all`
- `make check-package-paths`

`make check-package-paths` rebuilt and scanned 12 generated skill zips with 0
hard failures.

## Unzipped or Installed Skill Use

Ready.

`README.md` distinguishes uploaded skill zips from unzipped installed skills,
and `make help` exposes `make install` and `make uninstall`. The release grep
captures the install/unzip language in `README.md` and `Makefile`.

## CCDP Protocol Package Use

Ready.

`README.md`, `Makefile`, and `protocols/ccdp/README.md` distinguish
`ccdp.zip` from installable skill bundles. `make help` exposes
`make ccdp`, `make ccdp-package`, and `make check-ccdp-package`.

`make check-ccdp-package` validated `ccdp.zip` zipped and unzipped, found 0
shape, README, or Markdown path failures, and rebuilt the assembled protocol
from the extracted package.

## Repo-only, Provenance-only, and Excluded Material

Ready.

`package-path-exceptions.tsv` keeps the three explicit exceptions narrow and
schema-valid. The release surface and CCDP README identify `workbench/` and
`prompts/` as provenance/review/prompt material intentionally excluded from
`ccdp.zip` and not package entrypoints.

The remaining 295 package-path warnings stay visible as non-blocking backlog
or later maintenance; they are not hidden by broad exceptions.

## Readiness Finding

No release-facing ambiguity was found that would require a source repair
before Arc 04 or Project 01 close.
