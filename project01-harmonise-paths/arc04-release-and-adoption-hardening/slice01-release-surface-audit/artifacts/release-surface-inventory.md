# Release Surface Inventory

Audit date: 2026-08-29

Implementation checkout: `/Users/oubiwann/lab/billosys/ai-engineering`

Planning slice:
`project01-harmonise-paths/arc04-release-and-adoption-hardening/slice01-release-surface-audit`

## Source Files Inspected

- `README.md`
- `Makefile`
- `package-path-exceptions.tsv`
- `protocols/ccdp/README.md`
- `scripts/check-package-paths`
- `scripts/check-ccdp-package`

Primary grep evidence:

- `artifacts/release-surface-grep.txt`

## Command Surface

`make help` exposes the release/adoption targets needed by Project 01:

- `make all`: builds every per-domain skill zip plus the collaboration
  framework zip.
- `make skills`: builds the per-domain skill zips.
- `make collab-framework`: builds `collaboration-framework.zip`.
- `make install`: installs skill zips under the configured skill directory.
- `make check-package-paths`: validates Markdown paths inside generated skill
  zips.
- `make ccdp`: assembles the CCDP protocol document.
- `make ccdp-package`: builds `ccdp.zip` as a protocol package.
- `make check-ccdp-package`: validates `ccdp.zip` zipped and unzipped.

Evidence:

- `artifacts/make-help.txt`
- `artifacts/release-surface-grep.txt`

## Workflow Visibility

### Source Clone

Visible and acceptable.

The root README describes loading the collaboration framework from the source
checkout, links its project-management, ledger, audit, coverage, delegation,
and contribution documents, lists the `knowledge/<domain>/` source layout, and
points CCDP readers at `protocols/ccdp/README.md` and the source-clone CCDP
entrypoints.

Evidence:

- `artifacts/release-surface-grep.txt`

### Generated Skill Zips

Visible and acceptable.

The root README describes skill zips as installable skill bundles, lists the
per-domain and collaboration-framework Make targets, and states that the zips
upload directly to Claude Desktop / claude.ai.

Evidence:

- `artifacts/make-help.txt`
- `artifacts/make-all.txt`
- `artifacts/make-check-package-paths.txt`

### Unzipped / Installed Skills

Visible and acceptable.

The root README documents `make install`, the default install location, and the
fact that unzipped skill bundles work with Codex from the installed skills
tree. The Makefile help repeats install/uninstall discoverability.

Evidence:

- `artifacts/release-surface-grep.txt`
- `artifacts/make-help.txt`

### CCDP Package

Visible and acceptable.

The root README distinguishes CCDP from installable skill zips, documents
`make ccdp-package` and `make check-ccdp-package`, and tells package consumers
to start at `ccdp/README.md`. `protocols/ccdp/README.md` uses links that work
both in the source protocol root and in the unzipped `ccdp/` package root.

Evidence:

- `artifacts/release-surface-grep.txt`
- `artifacts/make-ccdp-package.txt`
- `artifacts/make-check-ccdp-package.txt`

## Generated Package Surfaces

Skill bundle packages are validated by `make check-package-paths`, which
rebuilds the 12 configured skill zips and scans package-context Markdown paths.

Observed result:

- zips scanned: 12
- Markdown files scanned: 171
- hard failures: 0
- warnings: 295
- explicit exceptions: 3
- skipped external URLs: 656

CCDP is validated separately by `make check-ccdp-package`, which rebuilds
`ccdp.zip`, scans package Markdown, and rebuilds from an extracted package.

Observed result:

- Markdown files scanned: 42
- package references checked: 14
- protocol syntax skipped: 91
- external URLs skipped: 4
- shape errors: 0
- README errors: 0
- Markdown path failures: 0

## Release Surface Verdict

No source repair is required by this audit.

The release/adoption surface now distinguishes source clone, generated skill
zip, unzipped/installed skill, and CCDP protocol package workflows. The
validation commands are discoverable through both README guidance and Makefile
help. Remaining skill-package warnings are visible and classified rather than
hidden, and the current accepted gates exit 0.
