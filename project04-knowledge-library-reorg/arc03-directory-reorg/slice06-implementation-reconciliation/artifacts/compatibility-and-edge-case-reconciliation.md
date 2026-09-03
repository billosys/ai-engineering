# Compatibility and Edge-Case Reconciliation

Date: 2026-09-02
Slice: Arc03 Slice06 implementation reconciliation

## Top-Level Compatibility Surfaces

The implementation reconciliation preserved these top-level surfaces:

- top-level SKILL.md
- AGENTS.md
- CLAUDE.md -> AGENTS.md
- README.md
- Makefile
- package-path-exceptions.tsv
- docs/ORIGINS.md
- templates/GUIDE.md

`CLAUDE.md` remains a symlink to `AGENTS.md`.

## Biome

Biome remains under `knowledge/biome` and preserves the accepted
multi-entrypoint package behavior:

- `biome-js-linter.zip`
- `biome-linter.zip`

Both generated zips contain the shared `guides/js-linter/` and
`guides/web-linter/` payload with distinct entrypoint files.

## CCDP

CCDP remains under `protocols/ccdp` as a separate protocol distribution.
`ccdp.zip` is built by `make ccdp-package` and checked by
`make check-ccdp-package`. It is not listed in `INSTALL_ZIPS`, which remains
the installable skill package list.

## Package-Path Exception Policy

The package-path exception policy remains unchanged:

- package-path exception rows: 8 total
- warning rows: 5
- explicit exception rows: 3
- hard failures: 0
- no broad exception added

Operator gate: any new accepted warning, broader exception pattern, or
persistent warning promotion remains outside Slice06 authority and requires
explicit operator approval.

## Arc04 and Arc05 Boundaries

Arc03 did not silently fold later-arc scope into implementation reconciliation:

- Arc04 still owns README decomposition and focused end-user documentation.
- Arc05 still owns final public skill-kind and atomic/composite vocabulary.

Slice06 did not rewrite README.md, docs/ORIGINS.md, public vocabulary, or
end-user docs. Its role was composition evidence for the directory
reorganization implementation.

## Compatibility Verdict

Compatibility and edge-case reconciliation is sufficient for Arc03 close
readiness. Remaining warnings are visible existing debt, not hidden Arc03
composition failures.
