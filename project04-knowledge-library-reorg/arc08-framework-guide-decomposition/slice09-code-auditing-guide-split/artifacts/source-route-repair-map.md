# Source Route Repair Map

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice09-code-auditing-guide-split
artifact: source-route-repair-map
source_commit: 1eb10d789734d9cca5c2c0f7cdedb4257dfab1e6
```

## Repaired Source Routes

| Surface | Repair |
|---------|--------|
| `knowledge/code-auditing/SKILL.md` | Bumped to `1.1.0`; routes to all five numbered audit guides. |
| `knowledge/code-auditing/guides/CODE-AUDIT.md` | Moved with `git mv` to `knowledge/code-auditing/guides/01-audit-scope-and-map.md`; no old-path file retained. |
| `knowledge/code-auditing/guides/02-findings-and-severity.md` | Added focused report/finding/severity guide. |
| `knowledge/code-auditing/guides/03-scale-aware-auditing.md` | Added focused all-scale audit and hunt-list guide. |
| `knowledge/code-auditing/guides/04-modernization-synthesis.md` | Added focused modernization synthesis guide. |
| `knowledge/code-auditing/guides/05-audit-to-hardening-handoff.md` | Added focused diagnosis-to-hardening handoff guide. |
| `knowledge/code-auditing/version-history.md` | Added `1.1.0` split/disposition entry. |
| `Makefile` `CF_FILES` | Replaced the old `CODE-AUDIT.md` package entry with the five numbered audit guides. |
| `assets/packaging/path-exceptions.tsv` | Moved the source-clone placeholder exception from the old guide path to `01-audit-scope-and-map.md`. |
| `knowledge/collaboration-framework/SKILL.md` | Bumped to `1.5.6`; route table now lists the five code-auditing guides. |
| `knowledge/collaboration-framework/guides/04-component-route-table.md` | Replaced the old audit route with five focused code-auditing rows. |
| `knowledge/collaboration-framework/version-history.md` | Added `1.5.6` route-repair entry. |
| `knowledge/engineering-methods/SKILL.md` | Bumped to `1.1.3` because operational routing changed. |
| `knowledge/engineering-methods/guides/04-operational-routing.md` | Replaced the old audit route with the audit-scope-and-map guide and selective companion guidance. |
| `knowledge/engineering-methods/version-history.md` | Added `1.1.3` route-repair entry. |
| `knowledge/project-management/guides/08-maintenance.md` | Updated the CAP-style audit output-home cross-reference to the split audit-scope guide. |
| `knowledge/project-management/version-history.md` | Added `2.11` route-repair entry. |
| `docs/collaboration-framework.md` | Updated public navigation so Code audit starts at `01-audit-scope-and-map.md`. |
| `docs/ORIGINS.md` | Updated the historical audit-prompt link to the new audit-scope guide path. |
| `AGENTS.md` | Added standing code-auditing route guidance and stated that the old path is not live. |
| `workbench/release-notes/RELEASE-0.5.0.md` | Added split guide routes and old-path rename/disposition text. |

## No-Op Surfaces

- `knowledge/work-verification/`: no live `CODE-AUDIT.md` route was found.
- `knowledge/testing/`: no live `CODE-AUDIT.md` route was found.
- staging scripts: `scripts/stage-skill-entrypoint` routes by component root and
  required no change.

## Historical References

Historical mentions in component version histories and old release notes were
left intact as lineage/disposition text, not live load routes.
