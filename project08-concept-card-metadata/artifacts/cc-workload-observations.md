# CC Workload Observations

Purpose: operator-requested tracking across the next three Arc06 slices,
including their repairs, to inform model/effort and slice-sizing decisions.
This is an observational record, not a performance benchmark or a direct
measurement of internal cognitive load. Do not change CC settings without
operator approval. Each slice counts once toward the three-slice trend;
iterations remain visible rather than counted as independent trials.

## Observation 01: Arc06 Slice01 Initial Submission

Date: 2026-09-14. CC commit: 400b847a. CDC outcome: changes required.
Scope: 35 pairs crossing legacy lists, card references and current edges.
Review: [Slice01 CDC report](../arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/cdc-verification.md).

Observed execution task: "Read metadata research instructions",
task ID 01a095ed-ccbc-76d0-a743-ec4b88872dfd.
Turn ID 01a0a066-9748-7c11-a28e-e56f71af6ad5.
Task-history tools reported durationMs 600507 (about ten minutes), 25
commandExecution items and three nonzero command exits. Final published
structural recipes pass independent replay.

Local turn metadata records gpt-5.6-terra at medium effort at
2026-09-14T14:51:13.514Z and after a compacted event at
2026-09-14T14:56:14.956Z. Model/effort were read from turn_context metadata,
not report formatting. Evidence location:
`/Users/oubiwann/.codex/sessions/2026/09/12/rollout-2026-09-12T09-03-04-01a095ed-ccbc-76d0-a743-ec4b88872dfd.jsonl`.
Only metadata/event categories and observable tool calls inform this record;
no private reasoning content is needed or reproduced. This external session
path is local diagnostic provenance, not a portable semantic acceptance input.

### Observations

- Exact scope and preservation were maintained.
- Three replay failures concerned null-byte/awk handling and membership tests;
  subsequent repairs passed. This is mechanical friction with successful
  correction, not evidence that relationship interpretation improved.
- The attempted corpus filter used literal record_kind == untyped. The raw
  legacy records omit that key; the frozen membership index normalizes it.
  CDC finds 2,054 eligible legacy mappings versus zero literal-untyped records.
- The run compacted once in an existing long-running task. That establishes
  a context event, not whether essential information was lost.
- Final artifacts omit the required actual census, named contextual comparisons
  and executed query outcomes, despite complete-looking row attestations.
- A substantive overgeneralization treats legacy typed links as not being
  relationship assertions. Source-support uncertainty does not justify that.
- No reliable per-run token/cost or remaining-context-budget measurement has
  been collected. Elapsed time alone cannot diagnose effort adequacy.

### Interpretation And Next Decision

Working hypothesis: inherited context and verification friction may have
contributed to attention being spent on structural completion while substantive
analysis remained thin. Confidence is limited; sparse synthetic current data,
scope interpretation and ordinary execution mistakes are alternatives.
Do not treat this as proof of overload or of inadequate model capability.

Recommended next step: fresh-context, evidence-first correction at unchanged
settings; record actual settings again. Keep existing passing checks and focus
on census, concrete targets, native query behavior and corrected meanings.
If comparable omissions recur despite that reset, discuss increased effort,
a different model or further slicing with the operator. Equally, consistently
strong later results may justify a lower-effort trial. Change one relevant
factor at a time where feasible; a repair with more guidance is not a controlled
model comparison. No setting change has been performed.

Subsequent observations should distinguish first-pass coverage, substantive
corrections, mechanical corrections and review outcomes. Retain failed attempts.
Only one slice has been reviewed so far; no multi-slice trend is established.

## Observation 01b: Arc06 Slice01 Iteration 01

Date: 2026-09-14. CC commit: 904a5a0d. CDC outcome: changes required.
This is a second attempt within the first monitored slice, not slice two.

Task remains "Read metadata research instructions",
01a095ed-ccbc-76d0-a743-ec4b88872dfd. Repair turn:
01a0a080-3be1-7c02-b066-7124404ca01c.
Task-history snapshot reports durationMs 303526 (about five minutes), twelve
commandExecution items and one nonzero exit (jq syntax error, followed by a
simpler successful census). Local turn_context at 2026-09-14T15:19:13.966Z
records gpt-5.6-terra / medium. No compacted event appears in the repair's
2026-09-14T15:19:13 through 15:24:18 UTC interval in the same rollout path
registered above. Same task plus continuing history is observed; a genuinely
fresh-session comparison did not occur.

### Gains And Remaining Signals

- Population classification now includes all 2,054 legacy mappings.
- Visible census execution and seven additional registered inputs improve the
  initial packet; reported counts and all fourteen hashes reproduce.
- The shared meaning and handoff now preserve legacy typed assertions.
- Generated/anomalous witnesses and available endpoint declarations remain
  unexamined in the packet; selected prompt reads are represented as full reads.
- Native diagnostic outputs are authored but not recomputed by the published
  assertions. A changed JSON shape breaks an older published verifier.
- A support ID from a separate example becomes an invented filename lookup
  associated with the rich card. This is a reference-ownership error, not
  merely a missing citation or an overlong task.
- The repair added a section but retained stale surrounding claims and member
  interpretations. Final integration/self-review remains a concern.

### Assessment And Next Adjustment

There is progress and less visible command friction than the initial run,
but persistent incomplete evidence and premature done attestations. No new
compaction occurred; these results do not support an explanation based only
on an active-turn context limit. Inherited context, a narrow patching approach,
insufficient substantive review, task interpretation and effort allocation
remain plausible alternatives. Internal cognitive load is not observable here.

The proposed fresh-context control was not exercised. Next recommendation:
use a NEW task/session, not another message or history-bearing fork, with
unchanged model/effort and the bounded Iteration 02 packet. Work through
contextual witnesses, computed native diagnostics, then final reconciliation.
Do not infer a failed model trial from a reset that never occurred.

If omissions persist after that actual reset, discuss a higher-effort trial
or smaller execution scope before another broad repair; model changes remain
operator-controlled. Lower effort is not supported by these incomplete results.
Extra repair guidance and repeated exposure remain confounds, so this is not
a controlled model/effort comparison. No settings were changed. No reliable
per-run tokens, cost or remaining-context-budget measurement was collected.
