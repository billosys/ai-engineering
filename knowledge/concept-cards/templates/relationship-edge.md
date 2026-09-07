---
record_type: relationship-edge
id: null
revision: null
relationship_type: null
from_ref: null
to_ref: null
endpoint_roles: {from_role: null, to_role: null}
direction: null
inverse_reading: null
symmetry: null
meaning: null
source_support_refs: []
run_refs: []
actor: {id: null, role: null, mode: null}
created_at: null
evidence_grade: {assessment: unassessed, rubric_ref: null, rationale: null}
extraction_confidence: {assessment: unassessed, rationale: null, scope: null}
graph_closure_state: unassessed
validation_refs: []
verification_state: unassessed
verification_refs: []
reconciliation_state: unassessed
reconciliation_refs: []
preservation_refs: []
memory_admission_ref: null
---

# Relationship Edge: <relation sentence>

Use the [template conventions](../SKILL.md#record-templates) and
[relationship procedure](../guides/06-graph-cq.md). Give the relation independent
identity when evidence, lifecycle, run provenance or conflict attaches to it.
Simple card-local reading navigation need not instantiate this record.

## Endpoints And Relation Meaning

<Name typed endpoint identities/revisions and roles, relation meaning and use
conditions. Preserve prerequisites, extends, related and contrasts_with:
if A lists B as a prerequisite, B -> A; if A extends B, A -> B. Related and
contrasts_with are symmetric. Explain any accepted subtype explicitly.
Record inverse/symmetric views without inventing a second independent claim.>

## Support And Warrant

<Compare the edge assertion to its own [source support](./source-support.md).
Valid or supported endpoints do not warrant the relation between them. Label
inference and its premises. Explain evidence grade and extraction confidence
separately, with actor, date and scope. Prepared-source caveats remain attached
through support; document-extraction owns source cleanup.>

## Closure, Conflicts And Revisions

<List unresolved endpoints, missing required reciprocal views, contradictory
copies and affected CQ coverage. Record bounded reference completeness separately
from semantic verification. Preserve prior edge/navigation identity, incoming
dependencies and result applicability after endpoint splits/merges or changes.
Record reconciliation and preservation decisions with re-entry conditions.>

## Handoff And Reliance Limits

<Report actual actor/run, output location, checks and unassessed matters.
Separate admission of this edge from admission of either endpoint. State direct
versus operator-reported observations, missing evidence and next work.
This record does not construct or operate a runtime graph/database.>
