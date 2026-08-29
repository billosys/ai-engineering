# Arc 01: Distribution Path Contract

```yaml
arc: arc01-distribution-path-contract
status: active
project: project01-harmonise-paths
depends-on: []
blocks:
  - arc02-skill-bundle-harmonisation
  - arc03-ccdp-distribution-package
related:
  - Makefile
  - SKILL.md
  - knowledge/*/SKILL*.md
  - protocols/ccdp
```

## Capability Statement

This arc establishes the path semantics for ai-engineering distribution
artifacts. By the end of the arc, the project has an evidence-backed inventory
of current package path failures, an accepted contract for how references are
written or transformed, and a validation design that later implementation
slices can apply consistently.

The arc intentionally starts with diagnosis and contract. It does not bulk-edit
mature language packs before the path categories and validation policy are
settled.

## Slice Breakdown

### Slice 01: Package Path Audit

Status: active.

Scope: reproduce the current mismatch between source-root references and
package-root bundle contents, classify each mismatch, and write a contract
proposal for path semantics.

Load-bearing for: all later slices. The classification vocabulary from this
slice becomes the language used by the validation gate and package rewrites.

### Slice 02: Contract Gate Design

Status: planned, not opened.

Expected scope: convert the accepted Slice 01 contract into concrete validation
requirements for Make/Bash-friendly tooling. Decide which classes are hard
failures, warning-only, or explicit allowlist entries.

This slice should be written after Slice 01 closes, incorporating any bubble-up
findings.

## Dependencies

This arc consumes the existing Makefile packaging behavior and the current zip
outputs. It leaves implementation changes to skill files, scripts, and CCDP
packaging for later arcs unless Slice 01 shows that a tiny enabling fix belongs
in the contract gate.

## Version History

### v1.0 - 2026-08-29

Initial arc opened with Slice 01 active and Slice 02 stubbed. Later slices are
deferred until the package-path inventory is known.
