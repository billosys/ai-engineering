# Source Route Repair Map

## Source Commit

Source commit:
`120c2ceaf26ca656068d9f2ec34c978eefaf04a5`

## Repaired Routes

| Surface | Repair |
|---|---|
| `knowledge/testing/SKILL.md` | Bumped to `1.1.0`; routes to testing discipline, coverage hardening, and validation gates. |
| `knowledge/testing/version-history.md` | Added `1.1.0` entry for the three-guide split and legacy coverage disposition. |
| `knowledge/testing/guides/CODE-COVERAGE.md` | Renamed with `git mv` to `knowledge/testing/guides/02-coverage-hardening.md`. |
| `knowledge/testing/guides/01-testing-discipline.md` | Added focused general testing-quality route. |
| `knowledge/testing/guides/03-validation-gates.md` | Added focused validation-gate route. |
| `Makefile` `CF_FILES` | Replaced the old coverage guide entry with the three numbered testing guides. |
| `knowledge/collaboration-framework/SKILL.md` | Bumped to `1.5.5`; route table now lists the three testing guides. |
| `knowledge/collaboration-framework/guides/04-component-route-table.md` | Replaced the old coverage route with three testing-guide routes. |
| `knowledge/collaboration-framework/version-history.md` | Added `1.5.5` package-history entry. |
| `knowledge/engineering-methods/SKILL.md` | Bumped to `1.1.2` because engineering-methods routing changed. |
| `knowledge/engineering-methods/guides/04-operational-routing.md` | Replaced the old testing route with the testing-discipline guide. |
| `knowledge/engineering-methods/version-history.md` | Added `1.1.2` route-repair entry. |
| `docs/collaboration-framework.md` | Updated public navigation so Testing points to `guides/01-testing-discipline.md`. |
| `AGENTS.md` | Added standing route guidance for the split testing guide set and stated that the old path is not live. |
| `workbench/release-notes/RELEASE-0.5.0.md` | Added detailed route bullets for the three testing guides and old-path rename. |

## Explicit Dispositions

- No project-management source references required repair.
- No work-verification source references required repair.
- No README route required repair in this slice.
- No package-path exception changes were required.
- No staging-script changes were required beyond the Makefile `CF_FILES`
  package list.
- Historical CODE-COVERAGE lineage remains as prose in version-history and
  disposition contexts, not as live routes.
