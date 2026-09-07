---
record_type: claim
id: null
revision: null
statement: null
assertion_kind: null
card_ref: null
actor: {id: null, role: null, mode: null}
created_at: null
source_refs: []
prepared_source_refs: []
source_support_refs: []
run_refs: []
evidence_grade: {assessment: unassessed, rubric_ref: null, rationale: null}
extraction_confidence: {assessment: unassessed, rationale: null, scope: null}
validation_refs: []
verification_state: unassessed
verification_refs: []
reconciliation_state: unassessed
reconciliation_refs: []
preservation_refs: []
memory_admission_ref: null
---

# Claim: <short label>

Use the [template conventions](../SKILL.md#record-templates) and
[extraction procedure](../guides/03-extraction.md). This finer-grained assertion
can be a standalone record or an identifiable section within its card.

## Assertion And Scope

<Write the exact statement from frontmatter, or refer to that statement without
creating a second conflicting copy. Retain conditions, modality, units and
exceptions. Identify source statement, hypothesis, definition or inference;
for inference, give premises and reasoning without attributing it to the source.>

## Support And Counterevidence

<Map each substantive clause to [source support](./source-support.md) and its
selected spans. Explain partial, missing, inaccessible or conflicting evidence.
A source reporting an assertion does not establish its truth for every use.>

## Evidence Grade And Extraction Confidence

<Explain warrant, applicable rubric and assessed use separately from the
extractor's confidence in the extraction act. Identify assessor, date, target
revision, inspected scope and evidence behind each assessment. Do not average
conflicting support or invent numerical certainty.>

## Provenance And Lifecycle

<Identify the source/run and actual actor observations. Consume prepared
document-extraction records as upstream provenance; route raw PDF/EPUB/HTML or
converted-source cleanup there. Retain preparation caveats at this assertion.
Record each review/result's scope and revision applicability separately.
Preserve prior values and admissions without transferring them automatically.>

## Handoff And Remaining Work

<Name missing comparisons, review or acceptance where required, evidence access
limits and the next check. A saved claim is not an admitted memory.>
