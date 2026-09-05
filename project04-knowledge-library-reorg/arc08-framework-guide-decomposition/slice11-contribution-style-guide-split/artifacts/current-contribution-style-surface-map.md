# Current Contribution-Style Surface Map

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice11-contribution-style-guide-split
artifact: current-contribution-style-surface-map
created-by: CC
created-on: 2026-09-05
```

## Current Source Surface Before Editing

Before Slice11 source edits, the contribution-style component contained:

- `knowledge/contribution-style/SKILL.md`
- `knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md`
- `knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`
- `knowledge/contribution-style/version-history.md`

`CONTRIBUTION-STYLE.md` was the only guide. It mixed the maintainer-facing
voice and discipline contract with ticket shape, sizing, local drafting,
filing workflow, line-reference, blockquote-header, paste-boundary, and
cross-linking guidance.

`CONTRIBUTION-TICKET.md` already existed as a package-local authoring template
for confirmed bugs, additive feature requests, documentation fixes, and
unconfirmed questions.

## Current Route Surface Before Editing

The pre-edit route scan found live references to the old contribution-style
guide in:

- `knowledge/contribution-style/SKILL.md`
- `knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `knowledge/engineering-methods/guides/04-operational-routing.md`
- `docs/collaboration-framework.md`
- `Makefile` `CF_FILES`

`AGENTS.md` had standing route guidance for work-verification, testing,
code-auditing, and agent-coordination, but no contribution-style route guidance
yet.

## Package And History Surface Before Editing

`Makefile` packaged:

- `knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md`
- `knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`

`knowledge/contribution-style/version-history.md` recorded the component's
current state and explicitly deferred the broader guide decomposition into
contribution style and upstream ticket workflow.

`assets/packaging/path-exceptions.tsv` had no old contribution-style exception
that needed moving.
