# Memory Admission

Memory admission is permission to rely on an identified construct as durable
semantic memory under the applicable evidence and acceptance requirements.
Use it only when a reliance decision is requested. Start with the
[operator workflow](./02-operator-workflow.md) and specify the target, revision,
intended use and decision authority before assessing eligibility.

Admission is not artifact retention, source support, evidence grade, extraction
confidence, validation, verification, reconciliation or preservation. It is
not a runtime write. This guide does not perform a memory-runtime write or
implement storage, retrieval, scheduling, synchronization or enforcement.

## Establish The Admission Scope

Identify whether the target is a card, claim, relationship edge or CQ-related
assertion. Specify exactly what future cognition would be permitted to rely
on. For a CQ, distinguish retaining a requirement from relying on a coverage
or answerability assertion; a question's existence does not admit its answer.

Record the target revision, source snapshot, relevant runs, dependencies and
the intended use and limits. A card-level decision must account for all claims
inside its declared reliance scope. If only a subset qualifies, name that
subset and exclusions explicitly; one supported claim cannot admit the rest
of the card, its edges or its CQ answers.

Identify the applicable evidence criteria and who may decide. Use the task's
accepted requirements rather than inventing universal grades, numeric thresholds
or mandatory human approval for every operation. Check whether required
human/operator acceptance already covers this target, revision and use. Do not
request it again when valid acceptance is already present. If a necessary
criterion or authority is unknown, record the uncertainty and defer the
dependent decision; independent evidence assessment can still proceed.

## Assemble The Evidence Packet

| Required input | Inspect and retain |
| --- | --- |
| Target and intended use | Exact identity/revision, reliance scope, source and dependency revisions, decision criteria and actor authority. |
| Source support | Actual claim/edge/coverage-to-span attachments and typed locators, with accessible content, relevant conditions, preparation caveats and known counterevidence. Bibliography alone is insufficient. |
| Evidence grade | Warrant and rationale on the actual assertion/support subject, assessed against the applicable criteria. Extraction confidence remains a separate extraction-act signal. |
| Validation result | Structural/reference checks, target revision, coverage, outcome and outstanding failures or omissions. Passing validation is not admission. |
| Verification result/state | Semantic checks, evidence, verifier identity/context, criteria, outcome and current applicability. Same-context, independent and operator-reported evidence retain their actual strength. |
| Reconciliation result/state | Conflicts examined, dispositions, unresolved issues and any applicability limits. If none apply, document the bounded basis for not applicable; absence of a record is not proof of no conflicts. |
| Preservation decisions | Prior value retained, superseded, rejected or unresolved, with destinations and implications for the target. Keeping an old admission record is not renewed permission. |
| Required acceptance | The actor, decision, target/use covered, conditions and evidence reference when acceptance is required; otherwise state why it is not required. |

Use [evidence lifecycle](./05-evidence-lifecycle.md),
[validation and verification](./08-validation-verification.md),
[reconciliation](./07-reconciliation.md), and
[preservation](./04-re-extraction-preservation.md) to supply missing assessments.
For edge and CQ targets, use the [relationship/CQ guide](./06-graph-cq.md).
Do not invent unavailable results to fill the packet.

## Evaluate The Gate

1. Check that every input applies to the target revision and intended use.
   A result about an earlier source, only one claim, or a narrower use cannot
   justify broader reliance without an explicit applicability assessment.
2. Compare support and evidence grade to the declared criteria. Identify
   partial support, conflicting evidence, damaged preparation, uncertainty
   and uninspected dependencies at their actual scope. High extraction
   confidence cannot compensate for missing warrant.
3. Inspect validation and verification outcomes separately. Correctness claims
   requiring independent review cannot be satisfied by same-context checking.
   A missing check, failed check or narrower review remains visible; do not
   recast it as successful because another lifecycle result is favorable.
4. Inspect reconciliation and preservation dependencies. Reconciliation should
   be complete for the reliance scope, explicitly not applicable with rationale,
   or deferred only under applicable accepted conditions. A deferral requiring
   operator acceptance must retain that acceptance and a re-entry condition.
   It does not resolve the conflict or override insufficient source support.
5. Determine whether unresolved issues block the proposed use. If a narrower
   scope is defensible, state it as a separate bounded decision; do not quietly
   change the original request. Record any required acceptance still missing.
   Acceptance expresses permission under the criteria, not factual proof or
   a substitute for failed verification.
6. Choose an outcome and record the basis. Keep all component results intact
   rather than replacing them with one approval/confidence flag.

## Record Admit, Reject Or Defer

- **Admit:** the evidence and applicable acceptance requirements support the
  exact reliance scope. Record permitted use, exclusions, caveats, dependencies
  and conditions that trigger renewed review. Conditional admission must be
  allowed by the applicable criteria and make its limits explicit; a caveat
  cannot hide a failed mandatory requirement.
- **Reject:** the inspected evidence shows the target does not qualify for the
  proposed reliance. Record the failed criteria and whether correction, new
  support or a changed use could permit re-entry. Rejection for admission does
  not require deleting the artifact or declaring every assertion false.
- **Defer:** necessary evidence, review, reconciliation, preservation disposition
  or required acceptance is unavailable or unfinished. Record the exact gap
  and re-entry condition. A deferred admission grants no new reliance permission.

If admission is outside the requested operation, mark it unassessed or not
applicable with rationale rather than manufacturing a decision. These outcome
descriptions do not finalize a storage schema or enum set.

Give the decision a recoverable identity, actor/role, date, method and relevant
run references; name the target revision, criteria, evidence/result pointers,
acceptance evidence where required, outcome, rationale, caveats, remaining work
and prior decision superseded or retained. Admission state must refer to this
decision and scope. An admitted artifact may still be absent from any runtime;
a stored or retrieved artifact may still lack admission.

## Reassess On Revision Or New Evidence

Preserve the old decision with the revision it assessed. A change in claim
meaning, source support, edge endpoints/direction, CQ requirements, known
counterevidence, review outcome or intended use can invalidate applicability.
Name the affected target and dependents, record that the prior permission no
longer establishes current eligibility, and reopen the necessary checks.

Do not automatically carry admission to a new revision. Even an editorial
change needs a recorded basis for continued applicability if the decision is
reused. Re-entry identifies changed and unchanged inputs, updates affected
assessments, checks acceptance scope and issues a new or explicitly reaffirmed
decision. Retain the rejection/deferral and revision trail. Recording revoked
or stale applicability does not remove data from a memory system; any actual
runtime change requires its own authorized workflow and evidence.

## Human-Assisted Operation

Request the bounded evidence packet and any required acceptance record.
Attribute operator-reported checks and distinguish them from inspected source
excerpts. When the assistant lacks authority or required evidence, return the
assessment and proposed decision with remaining dependencies. Do not imply
that a proposal, pasted card or operator statement establishes independent
verification or a completed storage action. State delivery limits explicitly.

## Agent-Direct Operation

Inspect accessible target and result revisions, check applicability and record
the decision only within the authority already provided. Preserve older
records and reopen authorized written output to confirm its evidence links.
Report same-context review as such. Stop the admission decision at any missing
mandatory evidence or acceptance while completing other supported assessments.
Do not write to a memory runtime as a side effect of producing the decision.

## Handoff

Report the decision identity/location, target revision, permitted or requested
use, outcome and rationale, source support and evidence grade, each lifecycle
result/state, preservation implications and acceptance basis. List exclusions,
unassessed matters, conditions, revision triggers, re-entry work and affected
dependents. Distinguish a recorded decision from a recommendation awaiting an
authorized decider, and both from any separately evidenced runtime action.

Refer future support or integration requests to
[maintenance and package boundaries](./10-maintenance-packaging.md). Completing
this workflow does not claim a corpus was installed as memory or that future
consumers automatically enforce its decisions.
