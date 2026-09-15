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

## Observation 01e: Terra/High Iteration 04 And CDC Review

Date: 2026-09-14. CC commit 91c7f5f3; independent CDC review retains
changes-required and adds S1-4 to done S1-1/S1-6. This is a revision of the
same first monitored slice, not a second slice or duplicate heartbeat result.

### Observed Execution

New task "Read and follow prompt":
01a0a252-eaa7-72b3-b16b-44b8a4045daf; turn
01a0a253-7c68-71b3-a2ae-fd96e63a9b21.
The operator announced the same-model/high-effort trial. Actual turn_context
metadata at 2026-09-14T23:49:35.789Z confirms gpt-5.6-terra / high.
No compacted event was observed in the run. Read-only local metadata source:
`/Users/oubiwann/.codex/sessions/2026/09/14/rollout-2026-09-14T18-48-58-01a0a252-eaa7-72b3-b16b-44b8a4045daf.jsonl`.

Task history reports durationMs 738851 (about 12 minutes 19 seconds),
34 command executions and four nonzero command exits. One is an exploratory
jq syntax/quoting failure; three are failed or investigative replay invocations
before the final passing replay. These are not four independent semantic
failures. Final current block, structural blocks, 23 hashes and scoped commit
reproduce. No reliable token/cost/headroom measure was collected.

Dependencies still include the frozen inventory and transition, original
historical prompts, current templates/guides/synthetic examples, legacy
music/Erlang cards, generated candidates, past reviews and scoped Git endpoints.
Accepted historical reads were available for reuse; no new full-read requirement
was imposed. Retrieval truncation is not evidence of actual context loss.

### Quality Result

Concrete improvements relative to Iteration 03:
- Correct full Music/Erlang census values and four actual absent/null witnesses.
- Native symmetry and requested-versus-declared endpoint/revision objects,
  including negative controls, now reproduce rather than self-certify.
- Report/handoff distinguish real candidate extraction from synthetic examples
  and no-edge/future-CQ text from actual body relationship proposals.

Remaining explicit obligations:
- The requested teaching-rerun witness was omitted, and the aggregate card
  census still hides family differences.
- Observed presence was described as requiredness; one registry evidence role
  still conflicts with the corrected no-edge/future-CQ report.
- The published census replay checks selected anchors instead of the full
  tables, while the latest block omits the first two JSON result comparisons.
  Their correct native comparators survive in a historical block.
- The required structured-value/parser route was not followed for new cases;
  current bounded awk/grep values are correct but operation/replay integration
  still needs alignment.

This is progress, not a failed run with nothing retained. It also does not yet
meet the full completion contract. The recurring pattern is selective omission
and incomplete final integration after local repairs, alongside improved
substantive reasoning. More effort did not eliminate that pattern in this run.

### Interpretation And Next Trial

This actually exercised fresh Terra/high after fresh Terra/medium. More
detailed instructions, accumulated evidence and a shrinking remainder changed
too. No causal claim about high effort, model capability or internal cognitive
load follows; duration/iteration count is not a quality measure. Task sizing,
cross-document obligations, tool quoting friction and correction framing remain
plausible influences.

The operator reports friends' success with Luna/xhigh and offers that as the
next configuration if needed. This is external anecdotal motivation, not
Project08 evidence or a verified performance claim. Iteration 05 is model-neutral
and can be used for that operator-selected trial; no model/settings/task have
been changed or dispatched by CDC. If selected, both model and nominal effort
change relative to Terra/high, so judge completion of the bounded remaining
criteria, not an isolated model/effort effect or a cross-model ranking.

Measure the missing witness and family distinctions, accurate meaning/role
integration and a complete replay that reproduces all tables and four cases.
Preserve successes. If Iteration 05 is incomplete, require a concrete sizing
proposal instead of automatic Iteration 06 or reduced acceptance. Only one
slice has received independent review; the three-slice monitoring continues.

## Observation 01f: Luna/Xhigh Iteration 05

Date: 2026-09-14. CC commit 30d9815c; formal CDC review adds S1-2 and S1-5
to done S1-1/S1-4/S1-6. S1-3/S1-7 remain open. This is the same first monitored
slice, not another slice, and the earlier read-only heartbeat preview of this
commit is not a second execution or review.

### Observed Execution

New task "Read and follow CC prompt":
01a0a2bb-2c86-7170-af63-7c936e386ce1; turn
01a0a2bb-8976-7a11-b5d6-6258138cdbaa.
Local turn_context metadata confirms gpt-5.6-luna / xhigh at
2026-09-15T01:43:14.849Z and again at 02:09:57.536Z.
One compacted event is recorded at 02:09:57.535Z.
Read-only metadata source:
`/Users/oubiwann/.codex/sessions/2026/09/14/rollout-2026-09-14T20-42-50-01a0a2bb-2c86-7170-af63-7c936e386ce1.jsonl`.

Task history reports durationMs 1776510 (29 minutes 36.510 seconds),
148 commandExecution records, ten numeric nonzero exits and no unknown exits
in that count. Path lookup, jq quoting/filter work and repeated isolation of
hash/replay failures contribute to those exits; they are not ten semantic
failures. The actual compaction is observable, but internal cognitive load
is not measured. No reliable token/cost/headroom measure was collected.

### Quality Result

Relative to the prior packet, CC supplied the mapped teaching original/copy,
the six-family census, malformed-input exclusion accounting, explicit
null-field body contrast, and all four native comparisons in one current
structured-value replay. Twenty-seven registered hashes and all six current
published blocks independently reproduce. Those are substantial retained
improvements, and two additional ledger rows now pass CDC.

Two residual problems remain:

- The report/handoff say historical requiredness is undocumented, despite
  explicit prerequisite and general template-conformance rules in the
  registered prompts. Corpus variation and unknown card lineage do not
  establish the absence of those rules.
- The current conditional support search conflates no match with command
  error. During execution, CC encountered a regex error and reasoned that the
  fallback still matched expected unavailability; the regex was corrected,
  but the failure-path assumption remained. CDC injected exit 2 and the
  native replay still passed. Normal current lookup outcomes do reproduce.

These are distinct from the earlier missing-family/incomplete-case wiring.
Do not flatten five iterations into an undifferentiated failure rate or discard
the accepted progress.

### Interpretation And Next Action

Both model and effort changed from Terra/high, while the prompt and retained
evidence changed too. A single sequential repair trial cannot isolate a
configuration effect or support a model ranking. One actual compaction,
command count and duration indicate execution burden, not a calibrated
measurement of cognitive load.

Reviewer framing is another plausible contributor: the preceding prompt
emphasized not inferring requiredness from observed variation, but did not
foreground the explicit positive historical rules. The next comparison should
show rule, observation, lineage and future applicability separately.

After the fifth ordinary corrective iteration, stop automatic repair and
present a bounded two-step sizing proposal. Preserve all five done rows.
Do not issue Iteration 06, open Slice02, lower criteria or transfer the 35
memberships as accepted. The proposal awaits operator decision; no task or
settings changed. Keeping Luna/xhigh for a smaller approved unit would reduce
one source of variation, not prove that configuration superior.

Only one distinct slice has received independent review in this observation
series. Continue the requested three-slice monitoring without counting the
heartbeat preview or successive revisions as additional slices.

## Observation 02: Slice12 Bounded Remediation

Date: 2026-09-15. CC commits b3ea7533 and 52aad9c6; CDC independently closes
Slice12 and recomposes original Slice01, with attributed documentation
restoration. This is the second distinct reviewed slice in the monitoring
series, but it repairs the first slice's existing work. It is not an independent
new-family replication or a second acceptance of the same 35 pairs.

### Observed Execution

Task "Read and follow CC prompt", id 01a0a2bb-2c86-7170-af63-7c936e386ce1,
was reused from Iteration 05. Slice12 turn:
01a0a369-c022-7831-b05e-98cca7ea1b7e.
Local turn_context at 2026-09-15T04:53:31.856Z confirms gpt-5.6-luna / xhigh.
No new compacted event appears in this turn; the previous turn's compaction
at 02:09:57.535Z remains historical context, not another Slice12 event.
Metadata source:
`/Users/oubiwann/.codex/sessions/2026/09/14/rollout-2026-09-14T20-42-50-01a0a2bb-2c86-7170-af63-7c936e386ce1.jsonl`.

Task history reports 1189831 ms (19 minutes 49.831 seconds), 106 command
executions and four nonzero exits: a jq exploration error, two partial replay
attempts and a commit-amend attempt. These are procedural observations, not
four semantic failures. Multiple initial plan/ledger reads are visible.
No reliable cost/token/headroom measurement was collected.

### Quality And Recommendation

Both targeted repairs passed independent review on this submission. Historical
positive rules are distinguished from corpus variation and unknown lineage.
The same revised lookup handles match/no-match/error, and CDC's additional
native-path injection exits 2. Exact census, hashes, projections and native
cases remain intact.

The handoff rewrite dropped previously accepted interface questions and left
a stale four-row count beside the correct two-row list. CDC restored the old
paragraphs verbatim and labeled their provenance/status; this was a minor
documentation-retention completion, not new semantic analysis or an unreported
CC correction. The close is therefore not an untouched perfect submission.

Scope reduction to two explicit defects, positive-authority framing and reuse
of proven replay components coincided with success. Model/effort stayed the
same as Iteration 05, but the task was much narrower and reused its context;
this does not isolate a causal model or prompt effect. A nominally shorter run
is not a direct measure of lower cognitive load.

Retain Luna/xhigh provisionally for the next bounded family packet; no settings
are changed here. Prefer a fresh context for Slice02 so the growing correction
history does not dominate the new semantic task. Preserve unchanged handoff
sections by default and review deletions explicitly. Two distinct slices have
now received independent review; continue monitoring the next slice before
the final three-slice trend assessment.

## Observation 03: Slice02 Initial CQ Packet And Final Window Assessment

Date: 2026-09-15. CC commit 753bacb0; CDC outcome: changes required.
S2-1 and S2-5 independently pass. S2-2/S2-3/S2-4/S2-6 need bounded repair.
This is the third distinct reviewed slice, after Slice01 and its Slice12
remediation. It is only the second new semantic family, not three independent
new-family trials. This review does not duplicate a heartbeat observation.

### Observed Execution

Fresh task "Read competency prompt instructions":
01a0a38d-4b8a-72f3-b744-9528be501376; turn
01a0a38d-6ecc-7180-836c-4ebb6cf5337b.
Task-history duration: 1965663 ms (32 minutes 45.663 seconds).
There are 92 commandExecution items, 15 numeric nonzero exits: path/context
lookup, jq exploration, repeated partial replay failures and an initial commit
attempt. These are not 15 independent semantic failures. The final published
block passed CC and CDC at the submitted endpoint.

Local turn_context records gpt-5.6-luna / xhigh at
2026-09-15T05:32:30.582Z and again at 05:58:18.122Z.
One compacted event occurs at 05:58:18.120Z.
Read-only local provenance:
`/Users/oubiwann/.codex/sessions/2026/09/15/rollout-2026-09-15T00-32-21-01a0a38d-4b8a-72f3-b744-9528be501376.jsonl`.
Only public messages, tool metadata and context/event categories were used.
No private reasoning or reliable token/cost/remaining-headroom measurement
is part of this assessment.

### Outcome

Retained gains: exact scope and clean preservation, 25 matching evidence
hashes, real positive legacy reverse lookup, six-family reporting, distinctions
among reference identity, coverage and answerability, and useful concrete
research/interface questions. Scope and handoff rows pass independently.

Remaining defects are observable, not inferred from latency:
- The card total contradicts the six family rows; malformed exclusions name
  INDEX instead of the recognition card. The published census checks do not
  validate the full advertised table.
- A wrong-question control never uses its question; some claimed native case
  results are constants rather than observations. Normal parent-directory
  absence is mislabeled tool failure. This is not the old Slice01 exact bug,
  but it is another mismatch between operation and interpreted result.
- "Component target" leaves answer components versus referenced constructs
  ambiguous. The source guidance and null serialization need separate claims.
- Committed replay reads mutable plan/ledger files without revision pinning.
  Routine review then invalidates input hashes independently of corpus drift.

See the Slice02 CDC report for precise findings, retained evidence and the
bounded correction. Do not characterize the entire submission as empty or
collapse semantic, arithmetic, provenance and test-design problems together.

### Three-Slice Trend And Recommendation

The observation window is complete. The workload heartbeat was already PAUSED
when inspected on 2026-09-15; no new automation or settings change was made.

Across these slices, completion of exact scope and hashes is consistently
stronger than cross-document semantic/replay reconciliation. Increasing effort
and changing model coincided with substantial retained improvements, but did
not eliminate incomplete checks or unsupported interpretations. A genuinely
fresh Luna/xhigh session still produced these defects and compacted once.

The much narrower Slice12 fixed both named defects on its first submission,
with a disclosed CDC restoration of prior handoff text. That success supports
trying more explicit bounded execution and reuse; it does not isolate scope,
model, prompt, context or accumulated evidence as the cause. Slice01 repairs,
Slice12 remediation and Slice02 new-family work are not comparable benchmark
tasks. Internal cognitive load remains a hypothesis, not a measurement.

For the next repair, change the packet/execution structure rather than
automatically changing model or increasing effort: retain accepted work, use a
fresh session, sequence census, the one semantic clarification, native cases,
then final integration, and stop for sizing if headroom is inadequate.
This is a process recommendation grounded in these artifacts, not a claim
about general Luna capability or an official model ranking. No basis for
reducing effort is established by the incomplete acceptance results.

Before opening Slice03, explicitly size semantic analysis and shared replay
work separately. Its existing roadmap already permits a split. Stable
committed-authority reads, reusable query operations, structural JSON equality
and native-result negative controls should reduce recurrent incidental work;
they must still be independently tested rather than treated as accepted by
recommendation. Do not build that future framework inside this repair.

A later model trial may be useful if these bounded controls still fail.
Agree it with the operator, hold task/input/acceptance conditions as steady
as practicable, and record all attempts. The current observations do not
justify automatic model replacement, another effort increase, or relaxed
acceptance. Ordinary CDC review continues; extending the completed proactive
three-slice monitoring window would require a new operator request.
