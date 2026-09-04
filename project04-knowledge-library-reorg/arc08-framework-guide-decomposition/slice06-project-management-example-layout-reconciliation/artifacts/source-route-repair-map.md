# Source Route Repair Map

Source commit: `df2c33e0d882aa89dbd42da3b87737a822903979`

## Repairs

| Surface | Change | Reason |
|---------|--------|--------|
| `knowledge/project-management/SKILL.md` | Bumped to `1.0.2`; changed the worked-example route to `./examples/01-worked-example-odm.md`. | Keeps the component entrypoint pointed at the accepted example path. |
| `knowledge/project-management/guides/PROJECT-MANAGEMENT.md` | Updated required-load and split-file index links from `./09-worked-example-odm.md` to `../examples/01-worked-example-odm.md`; updated current version note to `2.9`. | Keeps the wayfinder accurate while preserving the eight numbered guide routes. |
| `knowledge/project-management/version-history.md` | Added `Version 2.9` entry recording the example move and preserved guide layout. | Records the project-management component change in the sibling history. |
| `Makefile` `CF_FILES` | Replaced `knowledge/project-management/guides/09-worked-example-odm.md` with `knowledge/project-management/examples/01-worked-example-odm.md`. | Ensures the generated collaboration-framework package follows the accepted layout. |
| `knowledge/collaboration-framework/SKILL.md` | Bumped to `1.5.3`. | Records that the composer/package route surface changed. |
| `knowledge/collaboration-framework/version-history.md` | Added `Version 1.5.3` package-history entry. | Records the collaboration-framework package route update. |

## No-Op / Dispositioned Surfaces

- `README.md`: no direct worked-example path reference required repair.
- `docs/`: no direct worked-example path reference required repair.
- `AGENTS.md`: no direct worked-example path reference required repair.
- `workbench/release-notes/RELEASE-0.5.0.md`: no direct worked-example path reference required repair; final release-note reconciliation remains Slice12 scope.
- `scripts/`: no staging script needed code changes; the Makefile `CF_FILES` list drives the package contents.
- `assets/packaging/path-exceptions.tsv`: no exception update was required; package-path validation passed with zero hard failures.

Slice02 Expedited Mode guardrails and Slice03-Slice05 route/history changes
were preserved.
