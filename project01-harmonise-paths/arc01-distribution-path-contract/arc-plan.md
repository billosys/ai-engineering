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

Status: verified/closed.

Scope: reproduce the current mismatch between source-root references and
package-root bundle contents, classify each mismatch, and write a contract
proposal for path semantics.

Load-bearing for: all later slices. The classification vocabulary from this
slice becomes the language used by the validation gate and package rewrites.

Outcome: verified by CDC on 2026-08-29. The audit found 145 actionable
package-context misses across all 12 installable zip archives, with the Slice
01 vocabulary retained: bundled-reference, source-clone-reference,
repo-only/provenance, example-project path, external URL, and parser false
positive.

### Slice 02: Contract Gate Design

Status: verified/closed.

Scope: convert the verified Slice 01 contract into concrete validation
requirements for Make/Bash-friendly packaging workflow. Decide the package
path validation surface, failure policy, exception schema, parser behavior,
Makefile integration point, and the Slice 03 implementation boundary.

This is a design slice. It should not implement the final checker, rewrite
mature skill guides, or add CCDP packaging. It must carry forward two Slice 01
verification constraints: the final gate must be Markdown-aware rather than a
raw regex hard gate, and future evidence reports must not claim that filtered
CSV output contains classes that the scanner suppresses.

Outcome: verified by CDC on 2026-08-29. The design selects generated zips as
the authoritative validation surface, `make check-package-paths` as the
Makefile entry point, `scripts/check-package-paths` as a no-suffix Python
checker entry point, and `package-path-exceptions.tsv` as the exception
schema.

### Slice 03: Package Path Gate Implementation

Status: active/opened.

Scope: implement the accepted Slice 02 gate design, wire the
`check-package-paths` Make target, add the `scripts/check-package-paths`
checker, add the initial `package-path-exceptions.tsv` policy file if needed,
and produce reproducible evidence from real generated package surfaces.

Durable slice-produced evidence lives in
`slice03-package-path-gate-implementation/artifacts/`. Implementation files
remain in the source checkout.

## Dependencies

This arc consumes the existing Makefile packaging behavior and the current zip
outputs. It leaves implementation changes to skill files, scripts, and CCDP
packaging for later arcs unless Slice 01 shows that a tiny enabling fix belongs
in the contract gate.

## Version History

### v1.0 - 2026-08-29

Initial arc opened with Slice 01 active and Slice 02 stubbed. Later slices are
deferred until the package-path inventory is known.

### v1.1 - 2026-08-29

Slice 01 marked verified/closed from CDC verification. Slice 02 opened as a
contract gate design slice. Slice 03 stubbed for later implementation after
the gate design is accepted.

### v1.2 - 2026-08-29

Slice 02 marked verified/closed from CDC verification. Slice 03 marked ready,
not opened, with the Slice 02 design carrying forward generated-zip validation,
the Make/script entry points, the exception schema, and the no raw-regex gate
constraint.

### v1.3 - 2026-08-29

Slice 03 opened from the verified Slice 02 gate design. The slice records the
new default durable artifact home at
`slice03-package-path-gate-implementation/artifacts/` for implementation
evidence produced during the slice.
