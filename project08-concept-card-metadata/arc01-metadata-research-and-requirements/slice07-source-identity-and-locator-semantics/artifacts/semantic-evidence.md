# Slice07 Semantic Evidence

Legacy Accent Types records source The Complete Musician, source_slug
complete-musician, authors Steven G. Laitz, chapter Pulse Rhythm and Meter,
chapter_number 2, section Accent in Music and pdf_page 33. The author string is
observed attribution, not parsed people. Its body cites pages 43-46, so the
frontmatter page is not silently treated as the same page basis.

Current source-locator template has null address components and empty mapping/
prepared lists: representability, not populated evidence. Its body and
concept-cards extraction guide distinguish source/snapshot/resource,
locator type/value, page ordinal/printed label/converter index, and original
versus prepared coordinates. document-extraction locator model separately
defines resource URI, anchors, source/output lines and range conventions.
A resolving address is not source support. Arc07 generated card references
prepared-source records; this is populated generated-reference evidence, not
proof of original mapping or support.

Consequences: titles/slugs are not editions or snapshots; authors are not
automatically person records; null coordinate/reference is not automatic
inapplicability. Preserve basis, resource and mapping evidence separately.
No source conversion, page-offset inference, mapping verification or migration
equivalence is claimed.

## Iteration 01 contextual distinctions

Frozen inventory is afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b.
CDC-reproduced census distinguishes 390 music from 1,664 Erlang cards: music
pdf_page is numeric in 390; Erlang has 224 numeric and 1,440 null. Erlang
chapter_number is 1,108 numeric and 556 null; section is null in 48 music and
13 Erlang records. These are present shapes, not inapplicability judgments.

Field meanings: authors attribute as observed text; source is a title and
source_slug a local lookup label, neither an edition/snapshot. chapter is a
heading while chapter_number is its observed ordinal; section is a finer label;
pdf_page requires declared basis. Locator resource names the addressed file/URI,
representation names its form, locator_type/value identify the address,
numbering_basis and range_convention interpret sequence/endpoints, and
context_hint supplies non-authoritative context. source_ref/snapshot_ref name
source and bytes/capture; original/prepared locator refs name counterpart
records; mapping_evidence_refs supports correspondence rather than being an
address; prepared_source_refs retain preparation provenance.

Synthetic pdf-marker-handoff (fab43b7e88e444c5784fadab49df4923c125e8d0ee0ae0efa9c04e7a7b737bbe)
Locators distinguishes converter index unknown base, physical PDF page 2,
printed label 1 and output lines 13-20. Synthetic epub-pandoc-handoff
(196a63786e2da73fa63522d0df5c8f10aec2d10e46c133dc55ca395f793df3ea)
uses resource-scoped anchor and output ranges. Arc07 locator-map
(837bc861e8b6e558e64ad7666bb88b24fb338d4451fa9ed93e459d82a8a6fd6f)
has loc-ch01-emergence for chapter-01.md lines 53-57, one-based inclusive.
These are synthetic conventions/external map evidence, not standalone locator
frontmatter, successful conversion, or source-support verification.
