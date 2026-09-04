# Independent Verification

Load this guide when assigning, performing, or reviewing the verifier role.
Ledger discipline depends on structural separation: the person or context that
closes a row is not the one that signs off that the evidence reproduces.

## The Separation Rule

The doer reports dispositions. The verifier checks them against artifacts.
That rule is stable even when names shift by scale:

| Scale | Closer | Verifier |
|---|---|---|
| Slice | CC implements and writes the closing report. | CDC verifies rows against source, artifacts, and commands. |
| Arc | CDC assembles the arc close from verified slices. | Fresh context, operator, or delegated gate reviewer checks composition. |
| Project | Planner assembles project close from closed arcs. | Operator plus independent context gates the definition of done. |

If the same Codex surface performs both roles because of tooling constraints,
preserve as much separation as possible: re-read the original ledger, rerun
verifiers, inspect the diff, and treat the closing report as a claim to test,
not a summary to trust. Prefer a fresh context or human review when available.

## CDC Slice Verification

CDC should:

1. Count rows.
2. Re-run every `done` verifier or a stronger equivalent.
3. Check deferral reasons and re-entry conditions.
4. Check no-op rationales.
5. Inspect source and planning diffs directly.
6. Validate durable artifact placement.
7. Confirm the slice bubble-up is honest against the arc plan.
8. Decide whether `arc-plan.md` must change before the next slice.

The result is `cdc-verification.md`, not an edit to the CC closing report. A
CC-authored close remains proposed-done until this independent pass happens.

## Higher-Scale Gates

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
