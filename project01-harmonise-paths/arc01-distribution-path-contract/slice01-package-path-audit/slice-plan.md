# Slice 01: Package Path Audit

```yaml
slice: slice01-package-path-audit
status: open
project: project01-harmonise-paths
arc: arc01-distribution-path-contract
depends-on: []
blocks:
  - slice02-contract-gate-design
```

## Goal

Produce an evidence-backed package path audit and a proposed distribution path
contract for the ai-engineering repo. The result should let the next slice
design validation without guessing which path references are defects, repo-only
provenance, examples, or false positives.

## In Scope

- Inspect the current source packaging model in the top-level `Makefile`.
- Rebuild or inspect every generated skill zip named by `INSTALL_ZIPS`.
- Reproduce path-reference misses inside zip/unzipped package contexts.
- Classify misses by source category and intended fix type.
- Write a report in the implementation checkout under `workbench/` with the
  current inventory, classifications, recommended contract, and next-slice
  implications.
- Update this slice's ledger with attested evidence and write the close report
  when implementation completes.

## Out of Scope

- Bulk-editing mature language guides or `SKILL.md` files.
- Adding the final validation gate.
- Adding or changing CCDP package targets.
- Publishing a release.
- Changing project-management methodology files unless a bubble-up finding is
  explicitly routed for later methodology maintenance.

## Verification Approach

Use repository tools first: `make help`, the top-level `Makefile`, generated
zip contents, and `rg`. A small temporary script under `/private/tmp` is
acceptable for the audit scan if it is included in the report or reduced to
repeatable commands. Do not commit temporary scripts unless the slice
explicitly expands to tooling, which is out of scope for this slice.

## Expected Implementation Output

- `workbench/2026.08.29-package-path-audit.md` in the implementation checkout.
- Updated planning close set in this slice directory:
  - `ledger.md` with row dispositions and attested evidence.
  - `closing-report.md` with a per-row walk and bubble-up to Arc 01.

`cdc-verification.md` is written only by the independent verification pass.

## Exit Criteria

The slice is ready for CDC verification when:

- The audit covers every generated zip named by the current top-level
  `INSTALL_ZIPS`.
- The report includes a mismatch inventory with counts by zip and category.
- The report distinguishes source-valid/package-invalid references from
  intentionally repo-only/provenance references and parser false positives.
- The report recommends a concrete contract for path authoring, staging-time
  transforms, package layout, and validation policy.
- The report names exactly what Slice 02 should decide or implement next.
