# Legacy Contribution-Style Disposition

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice11-contribution-style-guide-split
artifact: legacy-contribution-style-disposition
created-by: CC
created-on: 2026-09-05
```

## Disposition

`knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md` was moved with
`git mv` to the primary successor path:

- `knowledge/contribution-style/guides/01-contribution-style.md`

The guide was then semantically rewritten and paired with:

- `knowledge/contribution-style/guides/02-upstream-ticket-workflow.md`

Because the rewrite was substantive, Git recorded the committed source change
as a delete/add rather than a rename:

- deleted: `knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md`
- added: `knowledge/contribution-style/guides/01-contribution-style.md`
- added: `knowledge/contribution-style/guides/02-upstream-ticket-workflow.md`

## Live Route Decision

The old `CONTRIBUTION-STYLE.md` path is not a live source route after Slice11.
It is not retained as a support asset or compatibility stub.

Remaining old-path text is limited to explicit disposition or historical
provenance notes:

- `AGENTS.md` old path not live;
- `workbench/release-notes/RELEASE-0.5.0.md` split/disposition note;
- `knowledge/collaboration-framework/version-history.md` route-disposition
  note;
- `knowledge/engineering-methods/version-history.md` historical pre-split
  provenance text.

## Package Disposition

`collaboration-framework.zip` contains:

- `collaboration-framework/knowledge/contribution-style/guides/01-contribution-style.md`
- `collaboration-framework/knowledge/contribution-style/guides/02-upstream-ticket-workflow.md`
- `collaboration-framework/knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`

It does not contain:

- `collaboration-framework/knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md`

No package-path exception was needed for the old path.
