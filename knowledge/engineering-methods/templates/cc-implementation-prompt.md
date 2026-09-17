# CC implementation assignment: <slice and outcome>

Authoring aid for CDC/CRC. Read
[From Slice to Implementation Prompt](../guides/07-implementation-prompt-authoring.md)
first. Replace placeholders with source-grounded decisions before issuing;
omit inapplicable sections with a short reason where omission could be ambiguous.
This template's presence or length is not readiness evidence.

## Assignment and authority

Project/arc/slice, initial pass or iteration, exact prompt path and predecessor.
Current assignment record, assigned author/reviewer and Operator relay.
Source checkout/branch/revision, relevant dirty state and drift handling.
Approved outcome, scope/non-goals, plan/design/ledger authority and exact sections.
State whether this is implementation, investigation or evidence-only work.

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
- compatibility, feature/dependency constraints and downstream obligations.

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

## Behavioral tests and validation

| Acceptance row / contract | Setup and action | Exact expected observation | Incorrect behavior rejected |
| --- | --- | --- | --- |
| <row> | <fixture/input/entrypoint> | <value/error/sequence/invariant> | <credible failure mode> |

Include relevant negative, boundary, compatibility and feature cases; identify
existing fixtures to extend. List repository-native commands, working directory,
prerequisites, expected result, known baseline failures and evidence filenames.
Blocked or failing required gates remain visible; do not weaken acceptance.

## Scope, stop conditions and return

List permitted source/evidence paths, prohibited changes, exact artifact home,
commit authority and required staging discipline from the governing plan.
State escalation triggers and who resolves each. Include source mismatch,
invalid design assumptions and changes to API, scope or acceptance.

Return the exact assignment/source state, changed paths, per-row evidence,
command outcomes including failed/unrun attempts, self-review, deviations,
remaining blockers and bubble-up findings. CC evidence remains proposed-done
until the assigned independent reviewer accepts it under the selected workflow.

For an iteration, distinguish accepted work from required repairs and specify
the affected regression checks. Preserve previous prompts and identify the
current assignment; a previous completion report is not fresh execution.

## Author readiness record

Before issuing, record in the existing slice plan or assignment record where
this packet satisfies the six readiness checks: source-grounded,
design-complete, guideline-applied, executable, falsifiable, coherent/portable.
Resolve material gaps first. This is author self-review, not independent
acceptance or a new Operator approval gate.
