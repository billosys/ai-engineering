---
record_type: source-support
id: null
revision: null
subject_ref: null
source_support_status: unassessed
source_spans:
  - span_id: null
    source_ref: null
    source_snapshot_ref: null
    locator_refs: []
    selection_boundaries: null
    content_or_description: null
    context: null
    quote_policy: null
    checksum_or_edition_note: null
prepared_source_refs: []
evidence_grade: {assessment: unassessed, rubric_ref: null, rationale: null}
extraction_confidence: {assessment: unassessed, rationale: null, scope: null}
actor: {id: null, role: null, mode: null}
created_at: null
run_refs: []
validation_refs: []
verification_state: unassessed
verification_refs: []
reconciliation_state: unassessed
reconciliation_refs: []
preservation_refs: []
memory_admission_ref: null
---

# Source Support: <assertion and evidence>

Use the [template conventions](../SKILL.md#record-templates) and
[evidence lifecycle](../guides/05-evidence-lifecycle.md). Set subject_ref to the
exact claim, edge or identifiable CQ coverage assertion and revision, including
its construct type. Do not limit support to claim records or use bibliography
as a substitute. Remove unused span placeholders; missing support stays explicit.

## Selected Source Spans

<Complete each embedded span value with its identity, source snapshot,
[locators](./source-locator.md), selection boundaries and necessary context.
Distinguish a quotation from a paraphrase/description; preserve omissions and
quote policy. Multiple spans are separate selections, not one invented quote.
If content is inaccessible, record that limit rather than fabricated text.>

## Assertion-To-Span Comparison

<State what each span supports, the inspected qualifiers and contrary context,
and what remains unsupported. Record observer, date and actual coverage.
Distinguish insufficient, partial, conflicting and unassessed support. For an
edge, evaluate the relation itself rather than just its endpoints; for a CQ,
evaluate the coverage assertion rather than merely matching a topic.>

## Assessments And Preparation Caveats

<Explain evidence grade as warrant and extraction confidence as an act signal,
with separate rationale, assessor and scope. Consume document-extraction
snapshots/manifests/maps/readiness/caveats as upstream provenance; route raw
PDF/EPUB/HTML or converted-source cleanup there. Prepared content and a valid
locator do not establish this support relationship.>

## Lifecycle And Handoff

<Link each scoped review/result, prior-value decision and admission if assessed.
Keep unperformed checks unassessed. Record revised source/subject applicability,
unresolved evidence, direct versus reported observations and next inspections.
This support record is neither automatic verification nor memory admission.>
