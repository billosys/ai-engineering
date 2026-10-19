# CC implementation assignment: <slice and outcome>

Authoring aid for CDC/CRC. Read
[From Slice to Implementation Prompt](../guides/07-implementation-prompt-authoring.md)
first. Replace placeholders with source-grounded decisions before issuing;
omit inapplicable sections with a short reason where omission could be ambiguous.
This template's presence or length is not readiness evidence. Keep only the
detail the assignment needs; evidence work requires a concrete investigation
method, not artificial APIs or predetermined semantic conclusions.

## Assignment and authority

Project/arc/slice, initial pass or iteration, exact prompt path and predecessor.
Current assignment record, assigned author/reviewer and Operator relay.
Source checkout/branch/revision, relevant dirty state and drift handling.
Approved outcome, scope/non-goals, plan/design/ledger authority and exact sections.
State whether this is implementation, investigation or evidence-only work.
Name the user/downstream task, intended before/after result, integration destination
and promised delivery state (candidate, integrated/accepted, or released).
For Autonomous assignments, cite the Operator-approved role/model/provider,
selectable settings, expenditure/concurrency scope and fallback policy. Missing
approval blocks dispatch; proposed or inherited defaults are not authorization.
State external-action authority including automatic effects of pushes/CI.
For any investigation, including embedded diagnosis, cite the Operator agreement
on usefulness, applicability and budget. Name the decision consumer, agreed
question, resource limit and stop/re-entry conditions. If agreement is absent,
present a proposal for discussion, not an executable investigation assignment.
Do not invent source edits or conclusions to satisfy this template.

## Required reading and execution preflight

The author fills this manifest before issuing. The active prompt, slice plan
and slice ledger are required-full. For shared documents, name exact sections
and include definitions/dependencies; no silent narrowing by CC. Governing
reading obligations remain binding. List current authority separately from
historical background.

For predecessor examples, name the needed example and definitions as bounded
sections; do not require unrelated history merely to obtain a format or pattern.

| Order | Exact path and revision/state | Reading scope | Purpose / before which step |
| --- | --- | --- | --- |
| <order> | <resolvable path; qualify dirty inputs> | <required-full, required-section with exact bounds, required-data with query scope, conditional with trigger, or reference-only> | <contract it supplies and deadline> |

CC: before dependent work, load required text and inspect the declared data-query
results. Use bounded,
contiguous reads and recover every truncated or omitted portion. Grep hits,
headings, summaries, another context's reading, file hashes and successful shell
exit codes are not evidence that you received the full text. Record actual
loaded extents/source state and gaps in <author-named allowed evidence file or
execution log>; carry this record into the closing report.

For required-data, identify the pinned dataset, exact population/projection,
queries or query behavior, and expected output coverage. Record commands,
complete inspected results, denominators, exclusions and errors separately
from document reads. Identify full-body witnesses for semantic interpretation;
data projections cannot replace required prose or hide omitted records.

Then provide a brief source-cited contract readback connecting the consequential
requirements to implementation and tests, including exclusions and failure
behavior. Name the easily missed constraint that would invalidate plausible
code. Reconcile missing or conflicting instructions before affected edits;
otherwise proceed without asking for an additional approval. On context recovery,
revalidate state and reload required contracts no longer reliably available.
Receipts are attestation, not proof of comprehension or independent acceptance.

Keep the current preflight compact by linking complete records: actual source
and dirty inputs, protected paths, current prompt/ledger, applicable instruction
revisions, mutation/index owner, independent verifier, approved model/spend scope for Autonomous work,
real prerequisites, gates and evidence home. Revalidate changes on recovery.
Serialize mutations and checks that traverse their inputs; name explicit Make
targets and actual shells/executable/config paths. Derive test/scan populations
and distinguish zero selected tests, loading failure or timeout from a pass.
Use the [durable observation contract](../../project-management/guides/02-canonical-planning-worktree.md#evidence-batches-and-research-records)
for original commands/results and generated facts. This index does not replace
the required reading manifest, contract readback or ledger.

## Source reconnaissance

| File and symbol at baseline | Observed behavior or reusable facility | Required change and integration consequence |
| --- | --- | --- |
| <verified source location> | <observation, not assumption> | <concrete delta> |

State dependency/API checks, existing callers and tests, unresolved assumptions,
and the owner/stop condition for any uncertainty that affects implementation.
Identify useful existing behavior, teaching and examples to preserve, plus any
deliberate replacements. Scope dependencies to the accepted inputs this work
actually needs, with their revisions and applicability; retain whole-release gates.

## Applied engineering guidance

Name the accessible skill and chapter load paths for CC. Record the guidance
the author actually read and applied, with project-specific reasoning:

| Guide/section or verified pattern ID and strength | Decision and rationale | Target symbol and proof |
| --- | --- | --- |
| <source> | <applied rule; exception if justified> | <implementation/test> |

## Design decisions and implementation contract

Label binding decisions, recommended shapes and local discretion. Give the
reason for consequential choices, including rejected alternatives. Resolve:

- public signatures, types, visibility, invariants and ownership;
- control/data flow, mutation order, state transitions and determinism;
- errors, partial failure, panic/rollback boundaries;
- resource lifecycle, concurrency and capacity where applicable;
- compatibility, feature/dependency constraints and downstream obligations;
- transitions during multi-step work: what completes, stops, advances and is
  returned, including API versus direct shared-state changes where applicable;
- immutable inputs, authorized replacements and consequent hash/range/revision
  updates, with preservation of historical evidence.

Name exact supporting sections when detailed design lives elsewhere. Include
the current slice's decision summary here, clearly excluding future designs.
No dependent implementation proceeds on unresolved consequential choices.

## Implementation sequence

For each substantive change give the actual file/symbol, what changes, how it
uses existing code, why this ordering matters and the observable result.
Include representative signatures, algorithms or code/pseudocode for difficult
parts. Label sketches and their verification status. Cover construction,
registration, exports, feature wiring and docs as applicable.
Include routes/package wiring needed to use this increment. For a novel or
error-prone batch, use a difficult representative case through the complete output
path within the agreed scope before scaling up; do not add a pilot phase by
default. Obtain Operator agreement before any investigation to settle the method.
For error-prone evidence representations, include a source-grounded example
linking a claim to one atomic, applicable witness in the actual output schema.

State which local mechanics CC may adapt and which deviations require the
assigned reviewer or CDC/Operator before coding.

For investigation/evidence work, specify population, exact field paths and
constructs, contextual witnesses, comparisons, output representation and
unresolved-result policy. Separate documented, observed, inferred and unresolved
statements. Derive observations from inputs; a predeclared expected result is
not an observation or permission to invent semantic policy.

## Behavioral tests and validation

| Acceptance row / contract | Real check, setup and action | Exact expected observation | Incorrect behavior rejected / coverage limits |
| --- | --- | --- | --- |
| <row> | <existing command/test/inspection and fixture/input/entrypoint> | <value/error/sequence/invariant> | <credible failure mode; what remains unproved> |

Apply testing's [Proportionate Proof](../../testing/guides/03-validation-gates.md#proportionate-proof)
rule. Use existing adequate checks first. If new verification machinery is
needed, name the otherwise unproved requirement and bound its scope here.
Retain mandatory gates; supporting tools are not implicit additional products.

Walk multi-step cases through available APIs, ownership and observation points;
name integration/inline test locations and their feature coverage where needed.
Choose fixtures that force the old or rejected behavior to differ from the
expected result, including intermediate observations when claiming ordering.
Negative validator cases must exercise the same predicate as valid inputs.

Include relevant negative, boundary, compatibility and feature cases; identify
existing fixtures to extend. List repository-native commands, working directory,
prerequisites, expected result, known baseline failures and evidence filenames.
State the actual target and property coverage of reused validators, including
any predecessor-only checks and how current-slice gaps are resolved.
Blocked or failing required gates remain visible; do not weaken acceptance.
Include positive preservation checks and exercise applicable quality requirements
at the point of use. Reuse suitable fixtures and applicable accepted evidence;
reserve final integration for composition and remaining gaps, not first use.

## Scope, stop conditions and return

List permitted source/evidence paths, prohibited changes, exact artifact home,
commit authority and required staging discipline from the governing plan.
State escalation triggers and who resolves each. Include source mismatch,
invalid design assumptions and changes to API, scope or acceptance.
Stop an investigation at its agreed limit and report what was learned; discuss
extensions or changed questions with the Operator before continuing it.

Return the exact assignment/source state, changed paths, per-row evidence,
command outcomes including failed/unrun attempts, intake/readback evidence,
self-review, deviations,
remaining blockers and bubble-up findings. CC evidence remains proposed-done
until the assigned independent reviewer accepts it under the selected workflow.
Separate observed results from interpretation. Leave unsupported claims open;
do not report a described or planned check as executed.
Identify the usable improvement and actual integration state, or the answered
question and enabled decision. Name the next-action owner for undelivered work.

For an iteration, distinguish accepted work from required repairs and specify
the defect, prescribed repair, invalidated evidence and affected regression
checks. Identify evidence proposed for retention under work-verification's
[correction review rule](../../work-verification/guides/05-independent-verification.md#evidence-during-correction-review).
Preserve previous prompts and identify the current assignment; a previous
completion report is not fresh execution or independent acceptance.
For recurring defects, state what changed in the diagnosis or repair method and
how the correction will be demonstrated; repeating instructions alone is inadequate.

## Author readiness record

Before issuing, record in the existing slice plan or assignment record where
this packet satisfies the six readiness checks: source-grounded,
design-complete, guideline-applied, executable, falsifiable, coherent/portable.
Include reading/query scope, context budget and the CC preflight contract.
Check rule interactions, viable test sequences, discriminating oracles, validator
scope and preservation exceptions where applicable; point to the concrete
decisions above rather than repeating generic readiness claims.
Resolve material gaps first. This is author self-review, not independent
acceptance or a new Operator approval gate.
