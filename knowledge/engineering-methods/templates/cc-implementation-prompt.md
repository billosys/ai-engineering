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

## Required reading and execution preflight

The author fills this manifest before issuing. The active prompt, slice plan
and slice ledger are required-full. For shared documents, name exact sections
and include definitions/dependencies; no silent narrowing by CC. Governing
reading obligations remain binding. List current authority separately from
historical background.

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

## Source reconnaissance

| File and symbol at baseline | Observed behavior or reusable facility | Required change and integration consequence |
| --- | --- | --- |
| <verified source location> | <observation, not assumption> | <concrete delta> |

State dependency/API checks, existing callers and tests, unresolved assumptions,
and the owner/stop condition for any uncertainty that affects implementation.

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

State which local mechanics CC may adapt and which deviations require the
assigned reviewer or CDC/Operator before coding.

For investigation/evidence work, specify population, exact field paths and
constructs, contextual witnesses, comparisons, output representation and
unresolved-result policy. Separate documented, observed, inferred and unresolved
statements. Derive observations from inputs; a predeclared expected result is
not an observation or permission to invent semantic policy.

## Behavioral tests and validation

| Acceptance row / contract | Setup and action | Exact expected observation | Incorrect behavior rejected |
| --- | --- | --- | --- |
| <row> | <fixture/input/entrypoint> | <value/error/sequence/invariant> | <credible failure mode> |

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

## Scope, stop conditions and return

List permitted source/evidence paths, prohibited changes, exact artifact home,
commit authority and required staging discipline from the governing plan.
State escalation triggers and who resolves each. Include source mismatch,
invalid design assumptions and changes to API, scope or acceptance.

Return the exact assignment/source state, changed paths, per-row evidence,
command outcomes including failed/unrun attempts, intake/readback evidence,
self-review, deviations,
remaining blockers and bubble-up findings. CC evidence remains proposed-done
until the assigned independent reviewer accepts it under the selected workflow.

For an iteration, distinguish accepted work from required repairs and specify
the affected regression checks. Preserve previous prompts and identify the
current assignment; a previous completion report is not fresh execution.

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
