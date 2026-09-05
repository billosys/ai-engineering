# Version History Placement Check

## Checks

Component roots checked:

- `knowledge/collaboration-framework`
- `knowledge/engineering-methods`
- `knowledge/project-management`
- `knowledge/work-verification`
- `knowledge/testing`
- `knowledge/code-auditing`
- `knowledge/agent-coordination`
- `knowledge/contribution-style`

Commands:

```sh
for d in collaboration-framework engineering-methods project-management work-verification testing code-auditing agent-coordination contribution-style; do
  test -f knowledge/$d/SKILL.md || echo missing-skill:$d
  test -f knowledge/$d/version-history.md || echo missing-history:$d
done

find knowledge/collaboration-framework knowledge/engineering-methods knowledge/project-management knowledge/work-verification knowledge/testing knowledge/code-auditing knowledge/agent-coordination knowledge/contribution-style \( -path '*/guides/version-history.md' -o -path '*/templates/version-history.md' -o -path '*/examples/version-history.md' \) -print
```

Results:

- All eight component roots have `SKILL.md`.
- All eight component roots have sibling `version-history.md`.
- The guide/template/example-local history scan returned no files.

## Verdict

Pass. Framework component version histories are siblings beside component
`SKILL.md` files. There are no guide-local, template-local, or example-local
`version-history.md` exceptions.
