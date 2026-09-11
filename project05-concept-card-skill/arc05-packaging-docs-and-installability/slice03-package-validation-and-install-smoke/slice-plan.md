# Slice03 Plan: Package Validation And Install Smoke

```yaml
project: project05-concept-card-skill
arc: arc05-packaging-docs-and-installability
slice: slice03-package-validation-and-install-smoke
status: open
opened: 2026-09-10
depends-on:
  - slice01-package-targets-and-support-directories
  - slice02-docs-and-discoverability
```

## Goal

Run the package-local and install-oriented acceptance checks for
`document-extraction` and `concept-cards`, inspect the installed package shape,
and reconcile source/docs/package claims before Arc05 closes.

## In Scope

- Run `make check-package-paths` and disposition any hard failures or warnings
  relevant to the two new method-skill packages.
- Inspect generated package contents for both new skills after the package-path
  gate rebuilds them.
- Run an isolated install smoke with an explicit temporary `INSTALL_DIR`.
- Inspect the installed `document-extraction/` and `concept-cards/` directories
  for entrypoint, sibling history, guides, templates, examples, and
  `concept-cards/references/`.
- Reconcile README/docs package claims against generated zip and installed
  content evidence.
- Record explicit Arc06 closure inputs, including remaining project-level gates
  and any accepted warnings or deferrals.

## Out Of Scope

- New skill content, new docs discoverability, or new Makefile package wiring
  unless a validation failure requires a narrow correction.
- Runtime services, executable validators, JSON Schema, live-corpus
  extraction, graph/ontology databases, GraphRAG, CCDP services, memory
  runtime work, CI/release publishing, and old-root revival.

## Verification

- `make check-package-paths`
- `make check-skills`
- `make check-skill-versions`
- `make -s print-skill-zips`
- direct `unzip -l` or `unzip -Z1` inspection of both new generated packages
- isolated install smoke with `INSTALL_DIR=<temp> make install`
- direct installed-tree inspection for both new skills
- targeted grep over README/docs/source claims for stale package/install or
  runtime overclaims
- `git diff --check`
- `git status --short --untracked-files=all`

## Exit Criteria

This slice exits when package-path validation, generated zip inspection,
isolated install smoke, installed-content inspection, final package/docs
reconciliation, and Arc06 closure inputs are complete or explicitly
dispositioned. After CDC verification, Arc05 should proceed to formal arc
close.
