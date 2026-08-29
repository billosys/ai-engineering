# CCDP Package Contract Design

## Evidence Base

This design derives from the CDC-verified Slice 01 inventory:

- `slice01-ccdp-distribution-inventory/cdc-verification.md` verified Slice 01
  closed and confirmed Slice 02 could proceed without a repair slice.
- `ccdp-file-inventory.md` identified the tracked reader-facing/tooling surface:
  assembled spec, 22 source files, 62 JSON corpus files, 2 visual-guide files,
  1 template, 13 tool files, and the CCDP-local Makefile.
- `package-risk-map.md` separated 1,277 extracted references into full on-disk
  and reader-facing signals, with workbench/prompts excluded from the
  reader-facing subset.
- `candidate-package-contents.md` recommended a `ccdp/` root and separated
  read-only from rebuild-capable package contents.
- `excluded-material.md` identified workbench, prompts, local extraction prompts,
  Cargo target output, historical review notes, and the root README as default
  exclusions.
- `slice02-design-inputs.md` required decisions on archive identity, root,
  entrypoint, transforms, validation, and generated-output freshness.

## Contract Summary

Slice 03 should implement one rebuild-capable CCDP package:

- Archive: `ccdp.zip`
- Root: `ccdp/`
- Entrypoint: generated `ccdp/README.md`
- Package mode: rebuild-capable, while still usable read-only
- Public root target: `make ccdp-package`
- Public validation target: `make check-ccdp-package`
- Validator: `scripts/check-ccdp-package`

The package is not a skill bundle and must not be shaped as `SKILL.md +
guides/`. It is a protocol distribution containing the assembled spec, source
chapters, JSON corpus, visual guide, RFC template, and assembler source needed
to rebuild.

## Contents

Include:

- `composite-cognition-dispatch-protocol.md`
- `src/`
- `json/`
- `visual-guide/`
- `templates/draft-rfcxml-general-template-standard-00.xml-edited.md`
- `tools/ccdp-assembler/{Cargo.toml,Cargo.lock,src/**}`
- package-local `Makefile`
- generated package-local `README.md`

Exclude:

- `workbench/`
- `prompts/`
- `tools/ccdp-assembler/target/`
- root repository `README.md` as-is
- root repository `Makefile`

## Path Semantics

All package-local links must resolve after unzip from either their current
document location or the `ccdp/` package root.

- `ccdp/README.md` links to package-local CCDP files only.
- `src/README.md` may keep `../tools/` because tools ship in the selected
  rebuild-capable package.
- `json/MANIFEST.md` may keep `src/...` conceptual references if the validator
  treats them as `ccdp/src/...` package-root references from JSON corpus docs.
- JSON Pointers, slash-prefixed protocol paths, elision comments, and field
  paths are protocol syntax, not filesystem paths.
- External URLs are preserved but not liveness-checked in this arc.

## Generated Output Freshness

Packaging must not silently ship stale `composite-cognition-dispatch-protocol.md`.
Slice 03 must compare a temporary regenerated assembly output against the
committed assembled spec before building the package. If the diff is non-empty,
the Slice 03 implementation should update the committed assembled spec as a
named pre-package step, rerun the comparison, then package only from the clean
fresh committed state.

## Validation

`make check-ccdp-package` should verify:

- `ccdp.zip` exists and has exactly one `ccdp/` archive root;
- required contents are present;
- excluded material is absent;
- package-local Markdown links resolve after unzip;
- JSON Pointer/protocol slash syntax is not treated as filesystem paths;
- extracted package assembly works with temporary output;
- existing root `make ccdp` behavior remains available.

## Slice 03 Readiness

Slice 03 can proceed to package implementation. No separate repair slice is
required first, but generated-output freshness must be a first-class Slice 03
ledger row.
