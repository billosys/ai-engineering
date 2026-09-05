# Source Route Repair Map

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice11-contribution-style-guide-split
artifact: source-route-repair-map
created-by: CC
created-on: 2026-09-05
```

## Source Repairs

| Source file | Repair |
|---|---|
| `knowledge/contribution-style/SKILL.md` | Bumped to `1.1.0`; routes to `01-contribution-style.md`, `02-upstream-ticket-workflow.md`, and `CONTRIBUTION-TICKET.md`. |
| `knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md` | Removed as a live path after semantic split. |
| `knowledge/contribution-style/guides/01-contribution-style.md` | Added as maintainer-facing voice and discipline guide. |
| `knowledge/contribution-style/guides/02-upstream-ticket-workflow.md` | Added as upstream ticket workflow guide. |
| `knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md` | Retained as template and relinked to both focused guides. |
| `knowledge/contribution-style/version-history.md` | Added `1.1.0` split and template-role disposition entry. |
| `Makefile` `CF_FILES` | Replaced old contribution-style guide package entry with the two numbered guide paths while retaining the ticket template. |
| `knowledge/collaboration-framework/SKILL.md` | Bumped to `1.5.8`; route table now lists contribution voice, upstream workflow, and retained ticket template separately. |
| `knowledge/collaboration-framework/guides/04-component-route-table.md` | Replaced old contribution-style route with focused style/workflow/template rows. |
| `knowledge/collaboration-framework/version-history.md` | Added `1.5.8` route-repair entry. |
| `knowledge/engineering-methods/guides/04-operational-routing.md` | Replaced old contribution-style route with style-first, workflow/template-next routing. |
| `knowledge/engineering-methods/version-history.md` | Added `1.1.5` route-repair entry and converted a historical old-path Markdown link to provenance text. |
| `docs/collaboration-framework.md` | Updated public navigation with contribution-style and upstream-ticket-workflow rows. |
| `AGENTS.md` | Added standing contribution-style route guidance and stated that the old path is not live. |
| `workbench/release-notes/RELEASE-0.5.0.md` | Added split guide route and template retention disposition. |

## Package-Path Exceptions

`assets/packaging/path-exceptions.tsv` required no change. No old
contribution-style exception existed, and the split introduced no new hard
package-path failures.

## Old-Path Scan

After source edits, `CONTRIBUTION-STYLE.md` remained only in explicit
disposition or historical provenance text:

- `AGENTS.md`
- `workbench/release-notes/RELEASE-0.5.0.md`
- `knowledge/collaboration-framework/version-history.md`
- `knowledge/engineering-methods/version-history.md`

No live route, package list, public navigation link, component entrypoint link,
template link, or operational route table uses the old path.
