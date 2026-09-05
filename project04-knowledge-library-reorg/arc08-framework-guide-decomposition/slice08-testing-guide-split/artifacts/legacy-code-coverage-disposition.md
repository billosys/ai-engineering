# Legacy CODE-COVERAGE Disposition

## Disposition

`knowledge/testing/guides/CODE-COVERAGE.md` was renamed with `git mv` to:

- `knowledge/testing/guides/02-coverage-hardening.md`

No copy of the old path was retained.

## Rationale

The old file's primary load reason was hard coverage-threshold work. That
material is now the accepted `02-coverage-hardening.md` guide. The companion
guides extract general testing discipline and validation-gate material without
leaving the legacy path as a stale live route.

## Package Disposition

The rebuilt `target/skills/collaboration-framework.zip` contains:

- `collaboration-framework/knowledge/testing/guides/01-testing-discipline.md`
- `collaboration-framework/knowledge/testing/guides/02-coverage-hardening.md`
- `collaboration-framework/knowledge/testing/guides/03-validation-gates.md`

It does not contain:

- `collaboration-framework/knowledge/testing/guides/CODE-COVERAGE.md`

Historical references to CODE-COVERAGE.md remain only as lineage/disposition
prose, not as live Markdown links or package entries.
