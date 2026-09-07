---
record_type: verification-result
id: null
revision: null
target_refs: []
verifier: {id: null, role: null, mode: null}
created_at: null
review_context: null
independence_basis: null
method_ref: null
method_and_settings: null
criteria: null
requested_scope: null
actual_coverage: null
source_snapshot_refs: []
prepared_source_refs: []
source_support_refs: []
evidence_refs: []
run_refs: []
observations: []
outcome: unassessed
state_effects: []
prior_result_refs: []
applicability: null
---

# Verification Result: <assertion and review scope>

Use the [template conventions](../SKILL.md#record-templates) and
[semantic verification](../guides/08-validation-verification.md#perform-semantic-verification).
A result records observations; verification state is a scoped summary grounded
in applicable results. Neither is evidence grade or extraction confidence.

## Verifier, Criteria And Evidence Access

<Identify reviewer, role, actual evidence access and context shared with the
producer. Distinguish same-context checks, independent reproduction, direct
human review, operator-reported observations and tool/process evidence. A fresh
context, different label or worker agreement alone does not prove independence.
Specify the claim/support/edge/CQ assertion tested and intended use.>

## Semantic Observations And Rationale

<For each observation identify target revision, criterion, selected spans,
support comparison, source qualifications, counterevidence, observer and outcome.
Distinguish faithful representation of what a source says from warrant that its
claim is true. Name uninspected material and incomplete coverage. Consume
document-extraction records as upstream provenance with preparation caveats;
route damaged/raw source cleanup there, without silently replacing snapshots.>

## Outcome And State Effects

<Explain supported-within-scope, partial, contradicted, unsupported or unresolved
outcomes as appropriate; inaccessible evidence does not establish falsity.
For each state_effects entry name target/revision, prior and proposed/resulting
verification state, basis in this result and whether the update was applied.
An empty list makes no state claim. Keep required independent review pending
after same-context checking when it has not occurred.>

## Caveats, Revision Applicability And Handoff

<Retain prior results and state why they do or do not apply after revision.
Name missing expertise, evidence and next checks, direct versus reported work
and storage limits. Refer conflicts, prior value and reliance decisions to
separate reconciliation, preservation and admission records. A favorable
verification outcome is not automatic memory admission or runtime storage.>
