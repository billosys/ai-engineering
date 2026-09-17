# Independent Verification

Load this guide when assigning, performing, or reviewing the verifier role.
Ledger discipline depends on structural separation: the person or context that
closes a row is not the one that signs off that the evidence reproduces.

## The Separation Rule

In the Operator-selected One-Contributor Workflow, a bounded non-ledgered task
may finish with proportionate self-checks and a clear completion report. This
guide does not create an independent-review gate where none applies. Existing
ledgered acceptance and required review gates remain binding, however; the
single contributor cannot discharge them by calling self-review independent.

The doer reports dispositions. The verifier checks them against artifacts.
That rule is stable even when names shift by scale:

| Scale | Closer | Verifier |
|---|---|---|
| Slice | CC implements and writes the closing report. | Assigned reviewer: CDC by default; CRC in the explicitly enabled Three-Contributor Workflow. |
| Arc | CDC assembles closure by default; CRC assembles it in the three-contributor workflow. | Fresh independent context or Operator by default; CDC in the three-contributor workflow, with Operator gates unchanged. |
| Project | CDC assembles by default; CRC assembles in the three-contributor workflow. | Operator plus independent review (CDC when independent in the three-contributor workflow) gates the definition of done. |

Follow the [canonical workflow authority and transition rules](../../engineering-methods/guides/01-engineering-methodology.md#roles-and-shared-invariants).
If a reviewer implements a repair, another verifier must review that repair
and affected acceptance evidence. The same implementing context rerunning tests
is self-review, not independent acceptance, even after changing its role label.
Record its results as doer-attested and keep independent acceptance pending
until a fresh review context or the Operator verifies them. Model choice alone
does not establish independence; the verifier must inspect the actual work.

## Assigned Reviewer Slice Verification

CDC in the default workflow, or CRC when explicitly enabled, should:

1. Count rows.
2. Re-run every `done` verifier or a stronger equivalent.
3. Check deferral reasons and re-entry conditions.
4. Check no-op rationales.
5. Inspect source and planning diffs directly.
6. Validate durable artifact placement.
7. Confirm the slice bubble-up is honest against the arc plan.
8. Decide whether `arc-plan.md` must change before the next slice.
9. Escalate changes outside delegated authority rather than editing the
   acceptance contract to fit the implementation. CRC routes design and
   substantive plan changes to CDC and the Operator; CDC also needs the
   required Operator decision in the two-contributor workflow.

The result is `cdc-verification.md` in the Two-Contributor Workflow or
`crc-verification.md` in the Three-Contributor Workflow, not an edit to the
CC closing report. Follow
[filename compatibility](../../project-management/guides/02-canonical-planning-worktree.md#verification-filename-compatibility).
Identify the reviewer role/context, workflow, exact assignment and source
state, reproduced checks, unresolved findings, and verdict. A CC-authored close
remains proposed-done until this independent pass happens. A changed source
state needs review of the change and its affected evidence, not a copied verdict.

## Higher-Scale Gates

In the Three-Contributor Workflow, arcs and projects each carry both
`crc-verification.md` and `cdc-verification.md`. CRC records operational
coverage, child dispositions, and composition/acceptance evidence; CDC
independently verifies composition and design conformance against the actual
state and governing plan. CRC assembling a close does not independently verify
that assembly. CDC must reproduce higher-scale evidence rather than accept
CRC's verdict on trust. Record each author's evidence strength honestly; retain
explicit Operator acceptance at the project gate and other required approvals.
Both records must cover the same candidate before closure. Failed CDC review
keeps the unit open and returns an explicit directive through the Operator.
The Two-Contributor Workflow does not invent a CRC record; keep the existing
independent arc/project gate with its reviewer and evidence explicitly recorded.

At arc and project scale, a gate reviewer must verify composition rather than
only reading child close reports. Children-closed rows can be attested by
pointers to verified child ledgers; composition rows require reproduced
integration or acceptance evidence at the current scale.

Failed composition should create planned remediation work. Do not grind patches
across slices or arcs without changing the plan-of-record and its version
history.

## Sandbox And Approval Reality

A verifier command that needs escalation, network access, GUI access, or writes
outside the workspace can still be the right evidence. Run it through the
available approval flow. If it cannot be run, record the blocker, the exact
command, and the re-entry condition instead of pretending weaker evidence is
equivalent.

## What Independence Does Not Prove

Independent verification does not prove the ledger was the right ledger. It
does not defend against deliberately falsified evidence. It does not catch
systemic success patterns unless the close process records "What Worked" and
cross-scale trends. These are known limits, not reasons to weaken the
separation rule.

Component history lives in [`../version-history.md`](../version-history.md).
