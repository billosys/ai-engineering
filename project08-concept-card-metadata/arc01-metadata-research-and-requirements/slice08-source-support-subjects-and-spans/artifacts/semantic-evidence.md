# Slice08 Semantic Evidence

## Five frozen roots and references

The frozen inventory has exactly five source-support roots: the current template
and four Project05 Arc07 pilot records. The template is deliberately
unpopulated: subject_ref and source/span targets are null, locator_refs is
empty, and source_support_status is unassessed. These are representational
placeholders, not missing successful support.

The actual concept-cards reference convention treats id, revision and path as
separate identity components: paths locate records, while IDs/revisions preserve
identity; unknown or inaccessible references remain explicit. It does not
specify a universal Markdown fragment resolver or let a root card revision
stand in for an embedded claim revision.

## Bounded reference matrix

| Ref kind and referring supports | Requested tuple | Target declaration / lookup | Result and consequence |
| --- | --- | --- | --- |
| subject_ref; all four supports | claim ID; revision 1; candidate-card path plus fragment; record_type claim | Each target card has matching Claim heading text and root record_type concept-card/revision 1. No target declares an embedded claim record revision or explicit fragment anchor. | Heading-text lookup finds the indicated assertion here; literal fragment resolution, claim type declaration, and claim revision remain unresolved. |
| source_ref; all four | ccn-book; e0c697b4; source-acquisition.md | Acquisition records full upstream commit e0c697b4d4... and sampled hashes, but no source-record ID ccn-book or source-record revision field. | Commit prefix correspondence is observed; requested source ID and revision declaration are unresolved. |
| source_snapshot_ref; all four | ps-ccn-book-pilot-20260911; revision 1; prepared-source-manifest.md | Manifest table declares precisely that prepared-source ID and revision 1, plus upstream input and representation/caveats. | ID/revision/path agree for a prepared-source record, but this neither makes every snapshot preparation-derived nor verifies upstream bytes. |
| locator_refs; all four | loc ID; revision 1; locator-map.md plus fragment | Locator IDs appear as table-cell IDs with resources/ranges; map has no explicit per-locator revision or named fragment anchors. | Row lookup by ID works. Literal fragment and requested revision are unresolved. |

The matrix is structural/reference evidence only. It neither repairs pilots nor
establishes that a selected span semantically warrants a claim.

The source-acquisition record identifies the upstream commit and sampled
chapter hashes; the prepared manifest identifies the directly inspected Markdown
representation and its caveats; the locator map supplies heading/resource and
one-based inclusive ranges. A manifest path or locator-map entry is upstream
provenance/address evidence, not immutable byte identity or semantic support.

## Selection and support comparisons

Model Data Constraints is a direct text-only selection, lines 37--45. Memory
Consolidation is text-only but candidate-supported-with-caveat: the selected
paragraph is qualified and its cited study/bibliography remains uninspected.
Emergent Explanation and Pattern Separation each select text plus an inspected
figure. In both, the body says the figure illustrates/corroborates the text and
is not independent proof. Thus text-plus-figure and text-only are both
represented without treating either as a stronger verification state.

Locator context is broader than selection: the map supplies address and hints,
whereas selection_boundaries restrict what was assessed (and can include a
figure outside a line range). This difference is intentional. Every pilot has
a paraphrase/description and says no quotation is retained; that is distinct
from absent content, copyright permission, or fidelity proof. Checksum/edition
notes point to hashes in acquisition/map records; they are not checksum fields.

source_support_status has only observed labels: unassessed in the template,
candidate-supported and candidate-supported-with-caveat in pilots. It is an
assertion-to-span relation label, not evidence grade, extraction confidence,
verification state, admission, or a closed vocabulary. All pilots retain
verification_state unassessed.

## Historical and synthetic boundaries

The inspected Accent Types card carries source metadata, a human-readable Source
Reference with pages 43--46, and Verification Notes naming direct source and
confidence rationale. The OTP Behaviour card carries a source/section reference
and notes a directly quoted definition, confidence rationale and cross-reference
status. These bodies carry readable citation and limited review notes; neither
supplies machine assertion IDs, selected span boundaries, quote policy,
source/snapshot tuples, or independent verification results.

The historical v3.2 guide provides provenance, Source Reference and Verification
Notes conventions. The bounded samples do not prove historical global absence
or query equivalence. Explicit subject/span mapping adds inspectable assertion
scope, selected boundaries and caveats; it still leaves independent verification
and source truth unresolved.

Synthetic claim, edge, and CQ examples show that source support can subject a
claim, relation assertion, or identifiable CQ coverage assertion. They are
conventions at fictional paths, not populated evidence or targets in the pilot.
