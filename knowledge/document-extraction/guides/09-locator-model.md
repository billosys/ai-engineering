# Locator Model

Use typed locators to connect preserved source, converted snapshots, and
prepared outputs. They support standalone indexing, reading, source review,
and analysis, and provide upstream provenance for `concept-cards`. A locator
identifies a place; it does not establish that a claim is true or supported.
Use the [output contract](./03-output-contract.md) for the whole handoff.

## Record Identity Before Position

A locator record needs an ID, source identity, snapshot identity, resource
path/URI, locator kind, value/range, basis, and verification status/evidence.
For a range, record inclusive/exclusive endpoints and numbering conventions.
Record the observed original locator verbatim alongside any interpreted value.
Use separate fields or linked records for different kinds; do not collapse
them into an unexplained `page` or `line` field.

| Kind | Meaning and limits |
| --- | --- |
| Page index | Ordinal position with an explicit zero/one-based convention and sequence scope: full source or converted subset. |
| Physical PDF page | A particular page object/position in the preserved PDF. Identify it with a verified index and basis, separately from labels. |
| Displayed/document label | The viewer or printed label, potentially Roman, repeated, missing, or restarted. Record which label system was observed. |
| Source path/resource URI | The original file or captured resource, including archive-relative paths when applicable; retain capture identity with web URIs. |
| Heading | Original heading text plus hierarchy/order and resource identity. Repeated text is not a unique address. |
| Anchor/ID | A target within an identified source resource or converted snapshot; check existence and uniqueness in that scope. |
| URI fragment | Fragment spelling interpreted against its resource and format. Preserve the original; do not assume every fragment maps to a retained Markdown heading slug. |
| Source lines | Line/range in a specific preserved text snapshot, with base and endpoint convention. Rewrapping or cleanup can invalidate it. |
| Output lines | Line/range in a specific generated output snapshot, including generated headers as counted. Never substitute it for source lines without a mapping. |

Unknown basis is an explicit value/status, not a default to one-based physical
pages. Reflowable EPUB/HTML has no assumed fixed pagination. Screen positions
or page labels supplied by a reader do not become PDF physical-page locators.

## Build And Check Mappings

1. Retain the original locator and identify its source/snapshot/resource.
2. Find corresponding content in the converted snapshot using available
   structural evidence and surrounding text. A matching heading or quotation
   can help locate it but is not sufficient when it occurs more than once.
3. Record the input-to-output relation after normalization or splitting.
   Permit one-to-many/many-to-one relations when transformations justify them;
   do not force a single offset through reordered, deleted, or added content.
4. Check actual targets and intended content. For PDFs, apply the
   [page-basis procedure](./04-pdf-source-preparation.md#establish-the-pdf-page-basis).
   For EPUB/HTML, inspect resource paths, anchors, and available navigation.
   For lines, read the identified file snapshot with the declared convention.
5. Preserve discrepancies and the check scope. Mark records verified within
   that scope, inferred, unresolved, or unchecked, and attach evidence and
   caveat references. Do not upgrade inferred mappings because a consumer
   needs a confident citation.

Generated headings/IDs are useful output addresses, but remain generated.
Record their correspondence to source anchors rather than presenting them as
author-supplied. Broken anchors, duplicate IDs, missing resources, or ambiguous
fragment interpretation stop the affected mapping. Other verified locator
kinds can remain usable with explicit limits.

## Human-Assisted Operation

Request a specific source location and the corresponding converted/output
excerpt with file identity and line convention. For PDFs, ask for physical
position, displayed label, and matching opening content at several separated
locations. For anchors, ask for the resource path, exact ID/fragment, and
target context; screenshots alone generally cannot verify those bytes.

Record who observed what and which basis remains unverified. If the operator
cannot supply the needed original, retain a snapshot-bound derived locator
and explain why the original mapping remains unchecked.

## Agent-Direct Operation

Inspect source, conversion, and output files or viewers directly. Build the
typed records, test target existence/uniqueness, and compare selected content
at both ends of each claimed mapping. Record complete target checks separately
from sampled fidelity checks. Do not equate a successful search hit with an
exhaustively verified mapping.

When output is regenerated, identify its new snapshot and recheck affected
locators. If only a path is moved and bytes remain identical, record the path
mapping and evidence; do not silently mutate old records that downstream
consumers may already cite.

## Handoff And Lifecycle

Retain prior locator records with the snapshots they identify. Rewrapping,
inserting metadata, OCR repair, splitting, or reconversion may alter line
positions and anchors. Create revised mappings with links to the preceding
run rather than retroactively changing the meaning of an old locator ID.

Pass typed records and unresolved-basis caveats to the
[readiness report](./10-validation-and-reports.md). Distinguish usable output
navigation from verified original-source traceability. Downstream concept-card
work may consume these locators but owns source-support judgments and evidence
grading; preparation must not disguise unverified provenance as verification.
