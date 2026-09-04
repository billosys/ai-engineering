# Version-History Normalization Map

Source commit: `657f156c7ad8048e60727275c2eed0d910de7f45`

## Normalization Summary

| Component | Normalized sibling history | Embedded history disposition | `SKILL.md` version after edit | Result |
|-----------|----------------------------|------------------------------|-------------------------------|--------|
| `work-verification` | `knowledge/work-verification/version-history.md` | Moved/reconciled the `templates/LEDGER-DISCIPLINE.md` embedded version history into the sibling history. The template now has a `## Component History` pointer to `../version-history.md`. | `1.0.1` | sibling history created |
| `testing` | `knowledge/testing/version-history.md` | No embedded history existed. Seeded the sibling history from current component lineage and Slice05 normalization. | `1.0.1` | sibling history created |
| `code-auditing` | `knowledge/code-auditing/version-history.md` | Moved/reconciled the `guides/CODE-AUDIT.md` embedded version history into the sibling history. The guide now has a `## Component History` pointer to `../version-history.md`. | `1.0.1` | sibling history created |
| `agent-coordination` | `knowledge/agent-coordination/version-history.md` | No embedded history existed. Seeded the sibling history from current component lineage and Slice05 normalization. | `1.0.1` | sibling history created |
| `contribution-style` | `knowledge/contribution-style/version-history.md` | No embedded history existed. Seeded the sibling history from current component lineage and Slice05 normalization. | `1.0.1` | sibling history created |

## No Guide-Local Component History

The post-edit source tree has no `guides/version-history.md` or
`templates/version-history.md` file for the five remaining components. The only
new history files are sibling files at the component roots:

- `knowledge/work-verification/version-history.md`
- `knowledge/testing/version-history.md`
- `knowledge/code-auditing/version-history.md`
- `knowledge/agent-coordination/version-history.md`
- `knowledge/contribution-style/version-history.md`

`knowledge/collaboration-framework/SKILL.md` was bumped to `1.5.2` and
`knowledge/collaboration-framework/version-history.md` records the package
content update because the collaboration-framework package now includes these
five sibling histories.

## Explicit Exceptions

No component needed an exception to the sibling-history rule. All five
remaining framework components now have sibling `version-history.md` files.
