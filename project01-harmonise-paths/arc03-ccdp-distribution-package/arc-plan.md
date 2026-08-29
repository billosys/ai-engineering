# Arc 03: CCDP Distribution Package

```yaml
arc: arc03-ccdp-distribution-package
status: active
project: project01-harmonise-paths
depends-on:
  - arc01-distribution-path-contract
  - arc02-skill-bundle-harmonisation
blocks:
  - arc04-release-and-adoption-hardening
related:
  - Makefile
  - README.md
  - protocols/ccdp/Makefile
  - protocols/ccdp/composite-cognition-dispatch-protocol.md
  - protocols/ccdp/src/
  - protocols/ccdp/json/
  - protocols/ccdp/visual-guide/
```

## Capability Statement

This arc gives CCDP a first-class distribution package and reader-facing entry
point so protocol users can consume the assembled specification, source
chapters, canonical JSON, examples, and supporting guide material without
repo-root path guessing.

The arc applies the same source/package path contract used for skill bundles,
but CCDP is not a skill bundle. The package shape should be designed from the
protocol consumer's workflow rather than forced into `SKILL.md + guides/`.

## Slice Breakdown

### Slice 01: CCDP Distribution Inventory

Status: verified/closed.

Scope: inventory the current CCDP source, build, generated spec, JSON corpus,
visual guide/reference, workbench/review material, README references, and any
path references that would become invalid in a standalone package. The slice
is diagnosis/design-input only; it should not implement the package target.

Load-bearing for: deciding the CCDP package contract before creating Makefile
targets or moving protocol materials.

### Slice 02: CCDP Package Contract Design

Status: verified/closed.

Expected scope: use Slice 01's inventory to choose package contents, archive
name, root directory, reader entrypoint, package-local path semantics, and
validation/checker integration.

### Slice 03: CCDP Package Implementation

Status: active/opened.

Expected scope: implement the selected Makefile packaging target and validation
path, update exceptions/backlog policy as needed, and prove the generated
CCDP package works zipped and unzipped.

### Slice 04: CCDP Reader Guidance

Status: stub.

Expected scope: update README or protocol-facing usage docs so source-clone and
package consumers know how to use CCDP without rediscovering file locations.
This may merge into Arc 04 if Slice 02 determines it belongs in release and
adoption hardening instead.

## Dependencies

Arc 03 consumes the distribution path contract from Arc 01 and the package-path
validation habit from Arc 02. The current root `Makefile` delegates `make ccdp`
to `protocols/ccdp/Makefile`; the CCDP Makefile already assembles
`protocols/ccdp/composite-cognition-dispatch-protocol.md` from
`protocols/ccdp/src/` via the Rust `ccdp-assembler`.

## Version History

### v1.0 - 2026-08-29

Initial Arc 03 plan opened after Arc 02 close. Slice 01 starts with inventory
because CCDP's distribution shape is protocol/package-specific and should not
be assumed to match the skill-bundle layout.

### v1.1 - 2026-08-29

Slice 01 marked verified/closed by CDC. The inventory confirmed that workbench
and prompts should be excluded by default, CCDP likely needs a `ccdp/` package
root with package-local entrypoint, and generated assembled-spec drift must be
an explicit contract decision.

### v1.2 - 2026-08-29

Slice 02 opened on CCDP package contract design after Slice 01 CDC
verification. The slice must decide package identity, contents, entrypoint,
read-only/rebuild-capable semantics, path transforms, validation/checker
strategy, and generated-output freshness before implementation.

### v1.3 - 2026-08-29

Slice 02 marked verified/closed by CDC. The accepted contract selects
`ccdp.zip` with root `ccdp/`, a generated package-local `ccdp/README.md`, one
rebuild-capable/read-only usable package, and a CCDP-specific package checker.
No repair slice is required before implementation, but generated assembled-spec
freshness must be an explicit Slice 03 gate.

### v1.4 - 2026-08-29

Slice 03 opened on CCDP package implementation. The slice must implement the
root package/check targets, staging, generated package README, required
contents/exclusions, zip/unzip validation, extracted-package assembly, and the
generated-output freshness reconciliation identified by Slices 01 and 02.
