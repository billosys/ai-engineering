# Slice02 Finding Disposition

## Decision Summary

| Finding | Disposition | Basis | Slice03 outcome |
| --- | --- | --- | --- |
| F-1 | checked no-op | `document-extraction/guides/09-locator-model.md` already requires snapshot/resource identity, line basis, range convention, target checks, and revised mappings after changed output. | The pilot's hash + heading + line convention is an application of current guidance, not a new rule. |
| F-2 | accepted refinement | `document-extraction/guides/06-html-and-converted-markdown.md` previously covered links/resources but not a citation-bearing Markdown audit for bibliography declarations, available resources, and in-scope keys. | Added the direct-lookup/caveat procedure in source commit `081a891`; `document-extraction` is now `1.4.4`. |
| F-3 | checked no-op | `concept-cards/guides/03-extraction.md` requires inspection of captions and figure context and says an image path is insufficient; it also requires unsupported assertions to remain unresolved. | The pilot's direct figure inspection and caveated dependencies follow existing guidance. |
| F-4 | checked no-op | `concept-cards/guides/03-extraction.md` requires one concept per card, separate concepts when a summary obscures identity, and explicit unresolved boundary choices. | The pattern-separation boundary question belongs in operator review/reconciliation, not a new example or automatic split rule. |
| F-5 | checked no-op | `concept-cards/guides/03-extraction.md` requires retention of conditions, modality, scope, and exceptions and prohibits strengthening or erasing a limiting condition. | The consolidation candidate's qualified phrasing is an application of the live rule; operator review still decides acceptance. |
| F-6 | checked no-op | `concept-cards/guides/02-operator-workflow.md` requires source snapshots/preparation records as inputs, bounded evidence requests, actor separation, and a handoff naming unresolved work. | The pinned checkout plus review packet implements the existing review boundary; no new review runtime is warranted. |
| F-7 | checked no-op | `concept-cards/guides/10-maintenance-packaging.md` explicitly excludes GraphRAG, runtime services, retrieval indexes, and memory automation while requiring evidence claims at their actual scope. | The existing boundary is sufficient; retrieval evaluation remains outside Project05 rather than an untracked defect. |

Every finding has exactly one disposition. These dispositions assess the skill
guidance, not the truth or operator acceptance of any Slice02 candidate card.

## Accepted Refinement

F-2 is the sole accepted refinement. The new Markdown audit requires an actor
to inventory frontmatter bibliography declarations, available bibliography
files, and keys needed by the requested scope; it permits a mapping only after
direct key lookup and retains mismatches or missing resources as caveats. It
does not resolve `ccnlab.bib` versus `references.bib` for the pilot, because
that would exceed the requested scoped preparation.
