# Dependency Audit

| Dependency class | Scope observation | Disposition |
| --- | --- | --- |
| Figures | Slice02 directly inspected `fig_gears.png` and `fig_patsep_clr.png`; Chapter 7 also references anatomy, CLS, and learning-rate figures. | Only the two inspected assets may be described as directly viewed; other figures are contextual/caveated and not independent support. |
| Citations | Selected Chapter 7 spans contain `@Marr71`, `@OReillyMcClelland94`, `@McClellandMcNaughtonOReilly95`, `@NormanOReilly03`, and other keys. Frontmatter declares `ccnlab.bib` while repository inventory identified `references.bib`. | The new `document-extraction` 1.4.4 rule was applied: no mapping was invented and cited works were not promoted to direct support. |
| Cross-references | Selected text names Executive Function, Perception and Attention, Learning, and Language. | Destination chapters were not included; references are contextual caveats, not support. |

No candidate depends on uninspected bibliography content, a cross-chapter
destination, or an uninspected figure for its source-reported statement.
