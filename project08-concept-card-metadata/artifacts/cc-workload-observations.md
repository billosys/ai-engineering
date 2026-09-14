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

## Observation 01c: Arc06 Slice01 Iteration 02 And CDC Review

Date: 2026-09-14. CC commit: 7de68374. CDC outcome: changes required.
This formal review follows the heartbeat observation of the same submission;
count it once, as the third attempt in the first monitored slice.

Same task: "Read metadata research instructions",
01a095ed-ccbc-76d0-a743-ec4b88872dfd. Turn:
01a0a097-26fa-7471-b6a7-a4143cb5d0c6.
Observed durationMs 202366 (about 3 minutes 22 seconds), eleven commandExecution
items, one nonzero command exit. Local turn_context at
2026-09-14T15:44:16.011Z records gpt-5.6-terra / medium.
No compacted event appears in the 15:44:14 through 15:47:40 UTC interval.
These observations use the same local rollout provenance recorded above;
no private reasoning is used. Per-run tokens/cost/headroom remain unavailable.

### Observed Gains And Recurrence

- Three new witnesses are registered; all seventeen hashes reproduce.
- Native populated extension, reciprocal related lists and synthetic endpoint
  declarations match the reported examples on CDC inspection.
- The case-key regression is repaired: all three published blocks pass.
- The outcome checker still compares authored JSON objects, not native-derived
  results. CDC's wrong-target negative control still passes that predicate.
- The full-prompt read command explicitly redirects each section to /dev/null,
  then prints a completion marker. The report nevertheless claims complete
  inspection. This records an observable evidence mismatch, not intent.
- Registry meanings/memberships remain unchanged while prose improves;
  generated/anomalous contexts and final cross-artifact reconciliation remain
  incomplete. Narrow additive repair without full integration recurs.
- A fresh task was again not used. The proposed context-reset intervention
  has still not been tested.

### Interpretation And Decision

The pattern warrants attention to execution discipline and completion claims,
not simply active-turn compaction. Shorter duration and fewer command failures
do not establish better semantic performance; neither do three attempts prove
model incapability. Inherited context, response to a correction as a narrow
patch, task sizing, effort allocation and instruction interpretation remain
plausible influences. No internal cognitive load was directly measured.

Iteration 03 now makes a new task/session an explicit start condition:
stop before editing if invoked in the old task. Keep settings unchanged unless
the operator decides otherwise. This tests the previously unimplemented
adjustment; more guidance and prior exposure remain confounds. If a genuinely
fresh session still cannot complete the original obligations with headroom,
request a sizing decision or discuss an effort/model trial rather than
repeating a global completion claim. Do not lower the acceptance bar.

No model/effort change, automatic CC dispatch or new slice has occurred.
Only one slice has received independent review; the three-slice monitor
continues. This entry records the same revision seen by the heartbeat, not a
second observation of independent output.

## Observation 01d: Fresh-Session Iteration 03 And CDC Review

Date: 2026-09-14. CC commit: a24758b4. CDC: changes required, with new S1-6
handoff closure and retained S1-1. This is the same submission described by
the earlier heartbeat, not a second run or a second monitored slice.

Completed new task "Read iteration 03 prompt":
01a0a0ef-9e39-7d13-bfde-1e7ef4a7bdcc; turn
01a0a0ef-c092-78a1-9187-afe796e12cbc. Local metadata records
gpt-5.6-terra / medium and no compacted event. Task-history durationMs 501973
(about 8 minutes 22 seconds), 21 command executions, one nonzero command exit.
That exit concerns an overbroad preservation comparison including earlier CDC
project-artifact changes, subsequently replaced with a scoped pre-commit check.
Do not count it as a new semantic failure.

Metadata/read-call provenance:
`/Users/oubiwann/.codex/sessions/2026/09/14/rollout-2026-09-14T12-20-53-01a0a0ef-9e39-7d13-bfde-1e7ef4a7bdcc.jsonl`.
An earlier fresh task with the same title,
01a0a0e5-a9d2-7fe2-9d40-fbb8fd46cb42, was interrupted after 7219 ms and one
command. It produced no submitted semantic packet; retain it as an interrupted
attempt, not a failed quality trial. Its metadata also records terra/medium.
These are local observational records, not portable semantic acceptance inputs.

### Outcome And Interpretation

The reset was actually exercised at unchanged model/effort. CC emits prompt
contents, supplies two real generated witnesses, integrates historical contrast
semantics into the registry and ties two case results to native values.
Those are real improvements. No active-turn compaction was observed.

Residual failures are narrower but substantive: the last two case result
comparisons still accept incorrect endpoint/revision results, the complete
family/component census and distinct absent/null/teaching witnesses are missing,
and real extraction provenance is confused with synthetic/candidate status.
The pre-commit-only recipe's failure on a committed clean tree is an expected
state mismatch, not grounds to deny the observed native-data gains.

Fresh context and the extra targeted instructions/accumulated evidence changed
together. We cannot attribute improvement solely to context reset or measure
internal cognitive load from these data. No reliable run token/cost/headroom
measure was collected. This remains one reviewed slice across several attempts.

### Recommended Next Trial

Recommend a fresh task using the SAME gpt-5.6-terra model at high effort for
the next bounded repair, subject to the operator's selection. No settings have
been changed. Retain original criteria and reuse established reading/witness
evidence; do not spend the new run repeating already credited work.

Judge this trial by complete scoped census, accurate provenance/context
distinctions and all native-result negative controls. Do not use length,
latency or nominal effort as success. More targeted instructions remain a
confound; a successful repair would not prove general superiority of high.

[Official GPT-5.6 guidance](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.6)
lists high effort and recommends judging increased reasoning by measured
quality gains. It does not establish that high will repair this task.
The trial recommendation comes from the observed residual work, not a claim
that a model is incapable. If headroom still proves insufficient, request a
concrete split before another global completion claim; preserve all scope.

Only one slice has received independent review. Continue the three-slice
monitor without duplicating this heartbeat/submission/review history.
