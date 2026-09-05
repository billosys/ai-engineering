# Source Route Repair Map

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice10-agent-coordination-guide-split
artifact: source-route-repair-map
source_commit: 9e2d5d055712efb53028ef250091d70487a257a0
```

## Repaired Source Routes

| Surface | Repair |
|---------|--------|
| `knowledge/agent-coordination/SKILL.md` | Bumped to `1.1.0`; routes to all four numbered guides and preserves CC/CDC/Operator role terms. |
| `knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md` | Moved with `git mv` to `knowledge/agent-coordination/guides/01-when-to-delegate.md`; no old-path file retained. |
| `knowledge/agent-coordination/guides/02-context-packets.md` | Added focused context-packet guide. |
| `knowledge/agent-coordination/guides/03-result-integration.md` | Added focused parent-context integration guide. |
| `knowledge/agent-coordination/guides/04-anti-patterns.md` | Added focused delegation anti-pattern guide. |
| `knowledge/agent-coordination/version-history.md` | Added `1.1.0` split/disposition entry. |
| `Makefile` `CF_FILES` | Replaced the old policy guide package entry with the four numbered agent-coordination guides. |
| `knowledge/collaboration-framework/SKILL.md` | Bumped to `1.5.7`; route table now lists the four agent-coordination guides. |
| `knowledge/collaboration-framework/guides/04-component-route-table.md` | Replaced the old delegation-policy route with four focused agent-coordination rows. |
| `knowledge/collaboration-framework/version-history.md` | Added `1.5.7` route-repair entry. |
| `knowledge/engineering-methods/guides/04-operational-routing.md` | Replaced the old delegation-policy route with the when-to-delegate guide and selective companion guidance. |
| `knowledge/engineering-methods/version-history.md` | Added `1.1.4` route-repair entry. |
| `docs/collaboration-framework.md` | Updated public navigation so Agent coordination starts at `01-when-to-delegate.md`. |
| `docs/ORIGINS.md` | Updated the sidebar link to the new when-to-delegate route. |
| `AGENTS.md` | Added standing agent-coordination route guidance and stated that the old path is not live. |
| `workbench/release-notes/RELEASE-0.5.0.md` | Added split guide routes and old-path rename/disposition text. |

## Package-Path Exceptions

`assets/packaging/path-exceptions.tsv` required no change. No old
agent-coordination exception existed, and the new guides did not introduce a
new explicit exception.

## Historical References

Historical mentions in version histories and old release notes were left intact
as lineage/disposition text, not live load routes.
