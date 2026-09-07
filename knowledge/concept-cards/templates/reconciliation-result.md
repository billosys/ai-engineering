---
record_type: reconciliation-result
id: null
revision: null
conflict_class: null
affected_refs: []
reconciler: {id: null, role: null, mode: null}
created_at: null
run_refs: []
source_support_refs: []
evidence_refs: []
decision: unassessed
resulting_refs: []
state_effects: []
preservation_refs: []
validation_refs: []
verification_refs: []
memory_admission_refs: []
prior_result_refs: []
reentry_condition: null
---

# Reconciliation Result: <conflict>

Use the [template conventions](../SKILL.md#record-templates) and
[reconciliation](../guides/07-reconciliation.md). Name the conflict and affected
construct revisions before proposing a winner or changing records.

## Conflict Scope And Alternatives

<Describe duplicate concepts, competing definitions, slug/taxonomy drift,
conflicting support, relationship asymmetry, CQ coverage, preservation or worker
disagreement as applicable. Identify each alternative, source/run/worker scope,
unique prior value and dependencies. Separate conflicts with different bases.>

## Source Comparison

<Inspect the relevant source spans and competing interpretations, preserving
qualifiers, source revisions and unavailable evidence. Record direct versus
operator-reported observations. Structural validity, newer prose and worker
majority do not choose a winner. Prepared document-extraction output identifies
upstream provenance, not warrant; route source cleanup to that skill.>

## Disposition And Rationale

<State the scoped decision, supporting evidence and alternatives retained or
rejected. Distinguish a proposed change from an applied one. Record unresolved
or deferred conflicts honestly, with re-entry conditions. Give each state_effects
entry a target/revision, prior and proposed/resulting reconciliation state,
basis and whether applied. The result does not resolve every conflict in a set.>

## Preservation And Lifecycle Effects

<Map unique prior value to [preservation decisions](./preservation-decision.md):
preserved/superseded/rejected/unresolved, with destinations. Record changed
references, edges/CQ dependents, needed structural checks and semantic review.
State implications for memory admission without performing that decision here.
Reconciliation state/result does not replace validation or verification.>

## Handoff And Remaining Work

<Report result and output locations/revisions, actor/run, unresolved alternatives,
uninspected dependencies, missing required acceptance and next comparisons.
Preserve earlier results and their applicability; state storage/access limits.
Do not claim a reconciliation runtime or a completed whole-corpus review.>
