# Source Change Summary

## Change

Source commit `081a891` (`Clarify Markdown citation resource preparation`)
updates the owning `document-extraction` skill only.

| File | Change |
| --- | --- |
| `knowledge/document-extraction/guides/06-html-and-converted-markdown.md` | Added a citation-resource audit for citation-bearing Markdown: inventory declared bibliography resources, available bibliography files, and in-scope cited keys; require direct lookup for a mapping and retain mismatches as caveats. |
| `knowledge/document-extraction/SKILL.md` | Bumped `metadata.version` from `1.4.3` to `1.4.4`. |
| `knowledge/document-extraction/version-history.md` | Added the matching `1.4.4` change record. |

## Rationale And Boundary

Slice02 discovered a concrete ambiguity: the source frontmatter named
`ccnlab.bib` while the repository inventory identified `references.bib`.
The existing guide covered links and resources generally, but did not direct
an operator to compare citation declarations, resource inventory, and required
keys before downstream extraction. The new procedure closes that guidance gap
without asserting that a bibliography mapping exists.

No `concept-cards` source, template, example, package list, runtime, graph,
retrieval system, MCP surface, or memory-admission behavior changed.
