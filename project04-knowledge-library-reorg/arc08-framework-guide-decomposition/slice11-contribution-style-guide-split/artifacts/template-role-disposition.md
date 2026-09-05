# Template Role Disposition

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice11-contribution-style-guide-split
artifact: template-role-disposition
created-by: CC
created-on: 2026-09-05
```

## Decision

`knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md` remains a
package-local authoring template, not a guide.

No source evidence forced a different disposition. The file is still the
copyable ticket skeleton for confirmed bugs, additive features, documentation
fixes, and unconfirmed questions.

## Link Repair

The template now points readers to:

- `../guides/01-contribution-style.md` for maintainer-facing voice and
  calibrated contribution discipline;
- `../guides/02-upstream-ticket-workflow.md` for draft, filing, line-reference,
  blockquote-header, paste-boundary, cross-linking, and template-use workflow.

The workflow guide points back to the template as the reusable ticket shape.

## Package Role

The generated `collaboration-framework.zip` retains the template at:

- `collaboration-framework/knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`

The template remains bundled beside the two guides so package readers can load
style, workflow, and copyable ticket shape separately.
