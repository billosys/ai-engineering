---
record_type: source-locator
id: null
revision: null
source_ref: null
source_snapshot_ref: null
resource: null
representation: null
locator_type: null
locator_value: null
numbering_basis: null
range_convention: null
context_hint: null
original_locator_ref: null
prepared_locator_ref: null
mapping_evidence_refs: []
prepared_source_refs: []
actor: {id: null, role: null, mode: null}
created_at: null
run_refs: []
validation_refs: []
---

# Source Locator: <source and location>

Use the [template conventions](../SKILL.md#record-templates) and
[locator guidance](../guides/03-extraction.md#capture-locators-spans-and-source-support).
This record addresses material. The selected source span belongs inside
[source support](./source-support.md); a resolving address alone is not support.

## Source Identity And Address

<Identify title/edition or capture, resource and snapshot identity, with a
checksum when practical. State unknown identities. Describe what locator_type
and locator_value mean in this representation. For a PDF distinguish physical
page ordinal/base, converter index and printed label; for EPUB/HTML identify
resource and fragment; for text or media identify line/time basis and range
end conventions. Repeat the record for distinct addresses rather than silently
equating their coordinates.>

## Original And Prepared Mapping

<Identify whether this is an original or prepared coordinate. Reference its
counterpart only when known, and cite mapping evidence. Preserve each snapshot
and any ambiguity; do not infer a page offset. When document-extraction outputs
exist, retain manifest, locator/structure/media maps, readiness and caveats as
upstream provenance. Route raw PDF/EPUB/HTML and converted-source cleanup to
document-extraction. Already usable sources need no invented preparation run.>

## Resolution Observations

<Record who inspected or reported the location, when, which content was
accessible, and any ambiguity or failed lookup. Link structural checks without
claiming semantic verification. This address need not contain the whole span
or its interpretive context; identify that separately in source support.>

## Handoff And Remaining Work

<Name missing original/prepared mapping, source access or context checks.
Retain old addresses on revision and identify downstream support that may
need reassessment. Distinguish direct observations from operator reports.>
