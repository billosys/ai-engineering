# Biome and CCDP Edge-Case Validation

Date: 2026-09-02
Slice: Arc03 Slice05 package/link edge reconciliation

## Biome Multi-Entrypoint

The Biome package model remains intentionally multi-entrypoint:

- `biome-js-linter.zip`
- `biome-linter.zip`

`INSTALL_ZIPS` keeps both Biome packages in the installable package list, and
package inspection confirmed both generated zips contain their distinct package
roots and expected guide payloads:

- `biome-js-linter/SKILL-js-linter.md`
- `biome-js-linter/guides/js-linter/`
- `biome-js-linter/guides/web-linter/`
- `biome-linter/SKILL-web-linter.md`
- `biome-linter/guides/js-linter/`
- `biome-linter/guides/web-linter/`

Validation commands:

- `make check-skills`: pass
- `make check-package-paths`: pass
- `make all`: pass
- generated package inspection with `unzip -l biome-js-linter.zip`
- generated package inspection with `unzip -l biome-linter.zip`

Outcome: Biome multi-entrypoint behavior is preserved.

## CCDP Separate Protocol Package

CCDP remains a separate protocol package under `protocols/ccdp/`, not an
installable skill package in `INSTALL_ZIPS`.

Makefile surfaces reviewed:

- `CCDP_NAME := ccdp`
- `CCDP_ZIP := ccdp.zip`
- `ccdp`
- `ccdp-package`
- `check-ccdp-package`

`make ccdp-package` initially failed because
`protocols/ccdp/composite-cognition-dispatch-protocol.md` was stale. Running
`make ccdp` refreshed the assembled spec. The repair was committed as source
commit `9b6d5d83d9c8debd977609aa1118004e89e2c895`.

Post-repair CCDP validation commands:

- `make ccdp-package`: pass
- `make check-ccdp-package`: pass

Package inspection confirmed `ccdp.zip` keeps a separate protocol package root:

- `ccdp/README.md`
- `ccdp/composite-cognition-dispatch-protocol.md`
- `ccdp/src/`
- `ccdp/json/`
- `ccdp/visual-guide/`
- `ccdp/templates/`
- `ccdp/tools/ccdp-assembler/`

Outcome: CCDP separation is preserved.

## INSTALL_ZIPS Review

`INSTALL_ZIPS` includes installable skill packages, including the two Biome
entrypoints, and continues to exclude `ccdp.zip`.

No package-list change was required for Biome or CCDP after the CCDP freshness
repair.
