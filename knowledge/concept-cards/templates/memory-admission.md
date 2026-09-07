---
record_type: memory-admission
id: null
revision: null
target_refs: []
intended_use: null
reliance_scope: null
criteria_ref: null
decision_authority_ref: null
actor: {id: null, role: null, mode: null}
created_at: null
run_refs: []
source_support_refs: []
evidence_grade_summary: {assessment: unassessed, basis_refs: [], rationale: null}
validation_refs: []
validation_summary: unassessed
verification_refs: []
verification_state_summary: unassessed
reconciliation_refs: []
reconciliation_state_summary: unassessed
preservation_refs: []
preservation_summary: unassessed
operator_acceptance:
  required: null
  basis: null
  decision: unassessed
  actor_ref: null
  evidence_ref: null
memory_admission: unassessed
decision_stage: draft
prior_decision_refs: []
reentry_condition: null
---

# Memory Admission: <target and intended reliance>

Use the [template conventions](../SKILL.md#record-templates) and
[admission procedure](../guides/09-memory-admission.md). This record assesses
permission for durable semantic reliance, not artifact retention or storage.
It does not perform a memory-runtime write or enforce consumer behavior.

## Target, Use And Decision Authority

<Identify exact target revisions, dependencies, intended use, reliance scope,
criteria and authorized decider. Distinguish a card, particular claims, an edge,
a CQ requirement and a CQ coverage/answerability assertion. One supported claim
cannot admit the rest of a card. State exclusions and proposed versus issued
decision_stage explicitly; copying this template grants no permission.>

## Evidence And Gate Assessment

<Compare source support, warrant/evidence grade, validation results, verification
results/state, reconciliation results/state and preservation decisions against
the applicable criteria for each target. Keep summaries tied to exact result
revisions and coverage. Extraction confidence is not a substitute for warrant.
Prepared document-extraction outputs are upstream provenance, not support or
admission. Explain missing or inapplicable inputs and blocking failures.>

## Acceptance, Outcome And Rationale

<Record required acceptance, its actor/evidence, target/use and conditions.
Reuse applicable existing acceptance; unknown requirements stay unresolved.
Acceptance is not factual proof or a replacement for failed mandatory evidence.
Record admit, reject or defer with rationale only after assessing the gate.
Deferred admission grants no new reliance. If outside scope, leave unassessed
or explain not applicable; neither means admitted.>

## Caveats, Revision Applicability And Re-Entry

<State permitted use, exclusions, unresolved dependencies and review triggers.
Preserve old decisions with their target/source revisions. Identify when changed
meaning, support, relations, CQs, evidence or use invalidates applicability and
which checks/acceptance must be renewed. Retention of a prior decision does not
transfer its permission; record any reaffirmation basis explicitly.>

## Handoff

<Report actor, output location/revision, direct versus reported observations,
outcome/stage, missing evidence or acceptance, next work and access/storage
limits. Distinguish a recorded decision, recommendation awaiting a decider and
any separately authorized/evidenced runtime action.>
