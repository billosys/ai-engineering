# Method And Template Ownership Record

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice04-component-method-template-ownership-moves
artifact: method and template ownership
source_commit: 873a5502acef9c087cefd78d468cf6d123a27341
source-files-edited: true
```

## Method Roots

`knowledge/concept-card-method/` remains reserved. The source checkout did not
contain already-authorized live Project03 or Project05 material at that root
when checked with:

```text
test -d /Users/oubiwann/lab/billosys/ai-engineering/knowledge/concept-card-method; echo $?
1
```

No concept-card-method source or generated package was created in this slice.
The planned method root remains a Project03/Project05 coordination item gated
by the accepted Project04 layout.

## Owner-Local Templates

| Template | Slice04 disposition | Evidence |
|----------|---------------------|----------|
| `LEDGER-DISCIPLINE.md` | Moved from transitional `knowledge/collaboration-framework/templates/` to owner root `knowledge/work-verification/templates/`. | Source commit `873a5502acef9c087cefd78d468cf6d123a27341`; package inspection shows `collaboration-framework/knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`. |
| `CONTRIBUTION-TICKET.md` | Moved from transitional `knowledge/collaboration-framework/templates/` to owner root `knowledge/contribution-style/templates/`. | Source commit `873a5502acef9c087cefd78d468cf6d123a27341`; package inspection shows `collaboration-framework/knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`. |
| `templates/GUIDE.md` | Retained as a top-level cross-cutting support exception. | `test -f /Users/oubiwann/lab/billosys/ai-engineering/templates/GUIDE.md; echo $?` returned `0`. No single owning component root was proven. |

## Exception Status

The top-level `templates/GUIDE.md` exception is evidence-backed and narrow:
it is the only file left in top-level `templates/`, and it describes the
cross-cutting template area rather than a single component-owned template.

No new broad `package-path-exceptions.tsv` entry was added. The existing
collaboration-framework exception for the code-audit source-clone placeholder
was updated from the old transitional path to
`knowledge/code-auditing/docs/CODE-AUDIT.md`.
