# source-edit authorization register

## Slice01 Authorization State

source-edit authorization: none.

Slice01 is read-only against the source checkout. It created only planning
artifacts under
`arc06-validation-release/slice01-validation-surface-inventory/`.

## Later Slice Path Permissions

| Later slice | Path permission | Allowed only if | Notes |
| --- | --- | --- | --- |
| Slice02 package/path/install validation | `README.md`, `docs/**`, `SKILL.md`, `knowledge/**`, `package-path-exceptions.tsv`, `Makefile`, `scripts/check-package-paths`, `scripts/stage-skill-entrypoint`, package-related helper surfaces | package/path/install validation exposes a defect and the slice prompt explicitly authorizes a narrow repair | Generated zips and `build/` remain validation outputs, not committed source. |
| Slice03 CCDP package validation | `protocols/ccdp/**`, source `Makefile` CCDP targets, `scripts/check-ccdp-package` | CCDP freshness or package validation requires repair and the slice prompt explicitly authorizes protocol/package edits | Preserve protocol/package separation; do not repackage CCDP as an installable skill. |
| Slice04 release readiness/operator acceptance | README/docs/release-readiness planning surfaces; source only if the Slice04 prompt explicitly authorizes acceptance-note or final narrow fixes | final acceptance reconciliation exposes a defect | Do not reopen Arc02-Arc05 decisions without new evidence and operator authorization. |

## No-Edit Surfaces Without Explicit Operator Gate

| Surface | Default disposition |
| --- | --- |
| `protocols/ccdp/**` | no-edit in Slice01 and Slice02; only Slice03 may repair or disposition CCDP freshness unless operator overrides |
| package root renames | no-edit in Arc06 unless a validation failure proves a release blocker |
| `package-path-exceptions.tsv` | no-edit unless `make check-package-paths` introduces hard failures or accepted warnings need reclassification |
| source `Makefile` installable skill target list | no-edit unless package/install validation shows target drift |
| generated `*.zip` files | no commit; ignored validation outputs |
| `build/` | no commit; temporary staging output |
| `concept-card-method` source/package implementation | out of Project04 Arc06 scope |
| Arc02 directory contract, Arc03 moves, Arc04 docs decomposition, Arc05 vocabulary decisions | no reopen without new evidence and operator authorization |

## Operator Gate Register

| Gate | Required before |
| --- | --- |
| Explicit source-edit authorization for Slice02 | any package/path/install source repair |
| Explicit `protocols/ccdp/**` authorization for Slice03 | refreshing or otherwise changing CCDP assembled spec/package behavior |
| Explicit operator acceptance or waiver | final release readiness if CCDP freshness remains unrepaired |
| Explicit generated-artifact release instruction | committing generated skill zips or `ccdp.zip` |

## Current No-Op Confirmations

- No source files were edited in Slice01.
- No generated artifact was staged or committed.
- No `protocols/ccdp/**` refresh was attempted.
- No package-path exception was changed.
- No README/docs/SKILL source wording was changed.
