# Local coding model experiment protocol

Date: 2026-09-22

Status: proposed protocol; task fixtures, commissioning, and scored execution pending

Companion: [vLLM-Metal and LibreChat runbook](./vllm-metal-librechat-runbook.md)

## 1. Purpose, decision, and limits

Determine whether a local model on the Operator's M2 Ultra Mac Pro can perform
bounded Code Contributor assignments with acceptable correctness, instruction
compliance, completion time, and operator effort. A particular concern is
whether the model reads and applies linked instructions and coding examples
instead of assuming the active prompt is self-contained.

The hardware baseline is 24 CPU cores, 76 GPU cores, 192 GB unified memory,
8 TB installed SSD, and macOS 15.7, supplied by the Operator. LibreChat runs
on both the Mac Pro and MacBook Pro. The inference host is the Mac Pro; select
one LibreChat deployment for scored runs and hold it fixed. Commission the
other client separately. Do not run competing requests from the two clients
during a timed trial.

Decision: admit a candidate for supervised, bounded CC work, retain it for a
narrower task family, or reject/defer it pending repair or a different model.
This pilot cannot establish general equivalence to luna xhigh, autonomous
engineering reliability, or correctness across untested repositories.

The Operator approved standalone planning documents on 2026-09-22. No new
project/arc/slice or contributor handoff is opened. Model outputs are candidates
for evaluation, not accepted implementations. The authoring assistant's checks
of this protocol are self-checks, not independent experimental verification.

## 2. Method sources and distinct responsibilities

Apply the current [scientific-methods entrypoint](../../knowledge/scientific-methods/SKILL.md)
and its guides for [framing](../../knowledge/scientific-methods/guides/01-inquiry-framing.md),
[design](../../knowledge/scientific-methods/guides/02-experiment-design.md),
[controls](../../knowledge/scientific-methods/guides/03-controls-and-confounds.md),
[measures](../../knowledge/scientific-methods/guides/04-operational-measures.md),
[protocols](../../knowledge/scientific-methods/guides/05-protocol-and-prompt-design.md),
[evidence](../../knowledge/scientific-methods/guides/06-evidence-capture.md),
[comparison](../../knowledge/scientific-methods/guides/07-comparison-and-regression-testing.md),
[interpretation](../../knowledge/scientific-methods/guides/08-analysis-and-threats-to-validity.md),
and [anti-patterns](../../knowledge/scientific-methods/guides/09-anti-patterns.md).

The collaboration framework supplies intake, scope, evidence, and review
discipline. Scientific methods supplies controls and inference limits. Domain
skills supply language-specific design and review guidance when task fixtures
are authored. A generic task-family table below is not a substitute for those
source-grounded assignments.

The [required-reading and CC intake contract](../../knowledge/engineering-methods/guides/07-implementation-prompt-authoring.md#required-reading-and-cc-intake)
is binding for framework-style test packets: complete required content,
lossless recovery of truncation, separate text/data coverage, a source-cited
readback, and no inference of comprehension from receipts alone.

## 3. Research questions and falsifiable hypotheses

| ID | Question / provisional claim | Contrary evidence | Decision use |
| --- | --- | --- | --- |
| H1 | With working tools and a packet that fits, the candidate loads and applies linked binding examples before dependent work. | Missing reads, unrecovered truncation, incorrect example-dependent behavior, or invented read claims. | Whether normal CC prompt packets are usable. |
| H2 | Next 4-bit retains useful coding quality relative to Next 8-bit while improving resource use. | Material correctness/compliance regressions or no useful operational gain. | Quantization selection. |
| H3 | The local workflow is useful relative to the Operator's luna xhigh workflow on matched bounded tasks. | Too many failures, materially greater intervention, or unacceptable latency. | Which assignments to route locally. |

H2 and H3 are operational comparisons, not claims of statistical equivalence.
Tune commissioning on practice tasks. Freeze the protocol before exposing
scored tasks to a candidate. Findings discovered during scored runs are
exploratory unless they were predeclared here or in the frozen task manifest.

## 4. Conditions

| Label | Model / workflow | Initial settings |
| --- | --- | --- |
| N8 | `mlx-community/Qwen3-Coder-Next-8bit` through vLLM-Metal and LibreChat | Temperature 1.0, top-p 0.95, top-k 40; single request; 32K server context |
| N4 | `mlx-community/Qwen3-Coder-Next-4bit`, same runtime and agent | Same as N8 |
| C30 | `mlx-community/Qwen3-Coder-30B-A3B-Instruct-8bit` | Optional later condition; commission and freeze separately |
| LUNA | Operator's existing luna xhigh workflow | Record exact model/profile identity and actual tools/settings |

Record model revision, tokenizer/chat template identity, quantization metadata,
runtime packages, parser, request parameters, agent instructions, and tool
schemas. The runbook supplies source-grounded candidate information; it does
not supply measured performance.

N8 versus N4 isolates quantized deployment as closely as practical. Community
conversions may differ in more than bit width: compare their base-model
provenance, tokenizer, templates, and conversion metadata before calling it a
pure quantization experiment. If they differ, disclose a deployment-bundle
comparison or normalize the differing components and recommission.

LUNA is a whole-workflow reference unless model access, tools, task inputs,
context, and budgets can be held equivalent. Do not infer a public API model
name or transferable reasoning parameter from the UI/profile label.

## 5. Readiness gates before scored runs

1. Complete the runbook's API, tool execution, tool-result return, and streaming
   checks on the selected LibreChat deployment. Record the actual version/image.
2. Demonstrate a transcript/trace that preserves complete delivered tool results,
   including errors and truncation. A model-written file list is insufficient.
3. Freeze source, prompt packet, framework/domain material, dependencies, and
   validation commands. Separate committed and dirty/untracked input identities.
4. Build and verify each task's behavioral oracles. A known-correct implementation
   must pass; the baseline or a plausible wrong implementation must fail for
   the intended reason. Keep those outputs as evaluator evidence.
5. Ensure the whole packet plus tool schemas, source reads, history, and output
   fits the configured context. Never fix a scored overflow by silently dropping
   a required file. Revise the packet or context before the experiment begins.
6. Predeclare run order, stopping limits, scoring, evaluator, and exclusions.
7. Validate the baseline build. Record inherited failures separately. A broken
   baseline must not masquerade as a model regression.

Current state: these are pending execution gates. This document designs the
experiment; it does not claim that a compiled ten-task suite already exists.

## 6. Task packet contract

Each task gets a frozen identity and an execution copy in the selected tool
environment. The physical corpus/evidence root on the target host is chosen
at commissioning and recorded once. The following names describe packet
contents, not a new planning tree or issued production prompt:

```text
cc-prompt.md             active task plus required-reading manifest
slice-plan.md            bounded task contract
ledger.md                criterion IDs and acceptance checks
design/                 linked binding design, if needed
examples/               actual coding examples used by the task
guides/                 exact required domain/framework sections
src/                    relevant frozen source inputs
```

Preserve the prompt's compact implementation spine while leaving detailed
linked examples in their designated files. Do not repeat all example-specific
answers in the prompt, which would remove the behavior being tested. Every
required dependency must still be discoverable and explicitly identified.

Each manifest records reading order; packet-relative path; source repository,
revision and content identity; full/section/data/conditional/reference-only
scope; why it matters; and which implementation steps depend on it. Enumerate
known normative dependencies and distinguish historical examples from current
authority. Record any path rewriting needed to make an existing assignment
portable; preserve the original packet as provenance.

Keep expected patches, evaluator-only tests, rubrics with condition labels,
other runs, and review conclusions outside the model's allowed roots. All
behavioral expectations must follow the visible contract; held-out tests must
not impose undisclosed requirements.

## 7. Experiment A: linked-file compliance diagnostic

Use N8 first. Choose one small real coding task whose result depends on a linked
example. Run five fresh conversations in each of these five conditions:

| Condition | Intervention | Correct outcome |
| --- | --- | --- |
| A-inline | Binding content is supplied directly in the task input. | Satisfy the same behavioral contract without claiming external reads. |
| A-linked | Same binding content in manifest-linked files. | Read complete required content, give coherent readback, produce compliant output. |
| A-missing | One required dependency is absent. | Report the exact missing dependency and stop affected implementation. |
| A-conflict | Two active binding documents specify incompatible behavior, with no precedence rule resolving it. | Identify the specific conflict and stop affected implementation. |
| A-long | Same linked contract, with a required code example late in a longer coherent document. | Load/recover the entire required scope and apply the example's constraint. |

Total: **25 scheduled attempts**. Five repeats reveal failure patterns; they
do not establish broad reliability. Rotate the five condition orders across
repetition blocks, recording the schedule before execution.

This is 25 attempts per candidate. Repeat the same diagnostic for N4 before
applying the same instruction-compliance admission threshold to it: **50 total
diagnostic attempts** if both candidates advance. These are separate from the
60 coding attempts in Experiment B. Do not transfer N8's expected-stop results
to N4 or leave an untested N4 control marked passed.

Inline/linked holds semantic content constant but necessarily changes delivery
and tool use. The long-document case also changes length/position and is a
stress test, not a pure single-variable contrast with inline. Missing/conflict
are expected-stop controls; do not pool them into code-production success rates.

### Concrete example-dependent behavior to build into the fixture

Use a bounded selection function with entries carrying `id`, `name`, and
`enabled`. The task's design chooses the enabled entry with the smallest
numeric ID. The linked example establishes failure and tie behavior: duplicate
enabled IDs are rejected before selection, disabled entries are excluded, and
input order is preserved. The prompt identifies this example as binding but
does not duplicate its detailed cases.

Predeclare these observable cases in evaluator material:

| Input | Expected observation |
| --- | --- |
| Enabled `(id=2, name=z)` and `(id=9, name=a)` | Select ID 2; rejects name sorting. |
| Disabled ID 1 and enabled ID 2 | Select ID 2; rejects ignoring `enabled`. |
| Two enabled entries with ID 2 | The specified duplicate-ID error; rejects first/last-wins selection. |
| One enabled ID 2 and one disabled ID 2 | Select the enabled entry; rejects checking duplicates before filtering. |
| No enabled entries | The specified no-selection result. |
| Original input inspected after success or error | Same order and contents; rejects in-place sorting/mutation. |

Before implementation, the packet author must choose one language, inspect its
domain skill, supply exact types/signatures/error representations and a real
coding example, and compile the fixture/oracles. Those language/API choices
are not delegated to the model under test. The table above is an experiment
stimulus design, not a completed CC implementation assignment.

For A-conflict, change the active design's rule to largest numeric ID while
the binding example still specifies smallest. Record that intervention as a
new packet identity. For A-missing, remove the linked example file. For A-long,
use legitimate surrounding design content; do not insert secret marker words
or unrelated padding as a supposed comprehension test.

### Diagnostic outcomes

For positive conditions record independently: full content delivery, coherent
contract readback, and behavior-test success. For expected-stop controls record:
correct blocker identity, no fabricated reads/results, and no dependent patch.
Unrelated work is not forbidden if it is explicitly independent, but the test
task should be small enough that this does not obscure the expected stop.

An inline pass plus linked failure suggests intake/tool/context problems; it
does not by itself identify which layer failed. Complete reads plus incorrect
behavior suggests retention/interpretation/implementation failure. Inspect raw
traces before assigning a cause. If the harness cannot preserve full results,
classify the observation as insufficient evidence.

## 8. Experiment B: coding and quantization pilot

Use ten bounded tasks, two each in Rust, Go, C++, TypeScript, and JavaScript.
Prefer small realistic repository changes over algorithm trivia. Choose tasks
before seeing any candidate's performance on them; do not select only tasks on
which a familiar reference model already succeeded.

| Language | Two proposed task families | Example discriminating properties |
| --- | --- | --- |
| Rust | Parser repair; stateful API change | Boundary errors, ownership, state preserved on rejected operation |
| Go | Cancellation; error propagation | Blocked operations terminate, worker cleanup, error identity preserved |
| C++ | Resource ownership; bounded parsing | Cleanup on failure, lifetime correctness, sanitizer findings |
| TypeScript | Runtime validation; state transitions | Absent/null/empty distinctions, invalid transitions, exhaustive handling |
| JavaScript | Async ordering; input handling | Rejection propagation, specified ordering, mutation/coercion behavior |

This table is the corpus selection plan. Each task needs an exact source
baseline, implementation contract, linked examples, domain-guided authored
packet, meaningful tests, and fixed toolchain commands before admission.
Do not claim generic commands such as `cargo test` or `npm test` cover a task
without inspecting that repository's actual targets and feature matrix.

Design:

- Conditions: N8 and N4.
- Tasks: ten.
- Repeats: three fresh conversations per task per condition.
- Denominator: **60 scheduled attempts**, 30 per model, six per language/model.
- Same task packet, filesystem tools, agent configuration, and source state.
- Same configured sampling, output cap, context cap, and stop rules.
- Independent disposable checkout for applying each patch and evaluating it.
- No access to previous run outputs, old conversations, memory, or other
  installed skill versions unless included in the frozen packet.

Balance first/second model order across the 30 task-repetition pairs: 15 N8
first and 15 N4 first. Generate and save the schedule before scored execution.
If model switching is expensive, predeclare balanced blocks rather than running
all N8 trials before all N4 trials. Record load/warm-up boundaries and background
load; do not include model loading in only one condition's task timer.

### Practice calibration and stopping rules

Use two practice tasks excluded from the scored corpus to test these initial
limits: 20 minutes elapsed active task time, 40 tool calls, and 4,096 maximum
output tokens per model response. Revise limits only during practice and then
record the final values. No hidden overall token budget is assumed; record
cumulative input/output tokens when exposed and report missing telemetry.

Any time/call/output cap reached during a scored attempt remains a recorded
outcome. Stop for unrecoverable missing inputs, contradictions, server crashes,
or context overflow, with the reason retained. Do not retry until success and
report only the successful attempt. A repeat after diagnosis gets a new ID
linked to the original; the original remains in its denominator.

Start with 32K only if the qualified packets fit. A change to 64K is a new
configuration applied to both comparison conditions before starting or to a
separate study phase. Cache behavior, speculative decoding, and concurrency
must remain fixed. No performance tuning during scored runs.

## 9. Exact run procedure

1. Select the next scheduled ID. Verify the pinned input and runtime identities.
   Record hardware/OS, client/backend, startup settings, and background load.
2. Start a fresh conversation with the frozen agent and correct tools. Ensure
   no previous conversation, model memory, retrieval corpus, or result is
   being inherited. Warm-up may use only a fixed unrelated practice input.
3. Send the frozen entry prompt below with only run identity and packet root
   substituted. Begin timing at task submission; log queue delay separately
   when available. Do not tell the model which condition should win.
4. Let the model perform intake and produce its patch or justified blocker.
   Do not rescue a skipped read with an informal reminder. Record any operator
   intervention and classify that attempt as assisted.
5. Preserve the raw messages, tool calls/results, and final output before
   inspecting or repairing the patch. Save finish/stop reason and timing.
6. In a fresh disposable checkout at the pinned baseline, save the raw patch,
   run `git apply --check` on it, then apply it if valid. Invalid patch format
   is an output failure; do not silently normalize it and score it as first-pass.
7. Inspect the resulting diff against allowed paths. Run the task's fixed
   build/test/static-analysis commands and evaluator tests, retaining exits and
   complete logs. A failed check must not be hidden by a subsequent exit zero.
8. Review semantic correctness, linked-example compliance, test quality, and
   scope. An implementer's tests alone do not establish acceptance.
9. Score the first attempt before offering any repair feedback. Report tests
   run by the Operator separately from tests claimed by the candidate.
10. Optionally run one predeclared repair round with the same public validation
    feedback policy for both conditions. Do not disclose evaluator-only answers.
    Preserve both candidates and score repaired success separately.

Entry prompt for patch-output trials:

> Run ID: `<RUN_ID>`. The active assignment is `<PACKET_ROOT>/cc-prompt.md`.
> Use only this task packet and the enabled tools. Read the assignment and its
> required inputs completely according to the manifest; give a source-cited
> contract readback before dependent implementation. Do not use earlier trial
> results or other installed instruction versions. Return a unified diff against
> the supplied baseline, a concise criterion-to-change mapping, and remaining
> uncertainty. No shell/compiler tool is available in this trial: distinguish
> checks you propose from checks actually executed. Missing or contradictory
> required inputs block dependent work; identify them precisely.

For the inline condition, replace the opening file instruction with the same
packet content supplied directly and remove only file-read obligations that
the delivery intervention makes inapplicable. Preserve the binding behavior.
Save both exact prompt variants before running; do not improvise them per run.

## 10. Measures and scoring rules

### Primary hard gates

| Measure | Operational rule | Evidence |
| --- | --- | --- |
| Required-content delivery | Every required text extent was returned before dependent work; required-data queries have their own coverage record. | Tool trace and manifest reconciliation |
| Contract comprehension proxy | Readback correctly connects consequential rules to intended behavior and checks. | Source-cited readback plus reviewer assessment |
| Behavioral correctness | All task-required behavioral tests and required build/static gates pass. | Reproduced commands, exits, and resulting source |
| Linked-example compliance | Every binding example-derived behavior is present. | Discriminating tests and code review |
| Scope control | No change outside allowed paths or authorized behavior. | Full diff, including tests/configuration |
| Evidence honesty | No unsupported claim of reading, execution, or passing validation. | Claim-to-trace/log reconciliation |
| Review findings | No unresolved critical/major defect in the proposed output. | Reviewer finding with source and consequence |

For code-production trials, **hard-gate success means all applicable gates
pass**. If evidence is unavailable, mark the gate unknown, not passed. For
missing/conflicting-input controls, correct stopping replaces code correctness
as the expected outcome. Do not penalize a legitimate stop as missing code.

Reading receipts are attestation. Traces establish delivered content, not
attention or understanding. A fluent readback is a useful proxy, not proof.
Behavioral tests and independent review remain necessary.

### Secondary measures

- Task completion time: submission to final patch/blocker; report load and
  warm-up separately. Also report evaluation and operator time separately.
- Time to first token, prompt throughput, output throughput, token counts:
  record only when observable; mark unavailable rather than inventing values.
- Resource use: startup and peak observed memory, memory-pressure state, swap
  before/after, other active loads. Process RSS alone is not total unified-memory
  consumption. Use the same measurement method and interval for both conditions.
- Operator effort: count interventions and repair rounds; record minutes and
  whether intervention supplied new semantic guidance or only repaired transport.
- Defect counts: retain individual critical/major/minor findings and affected
  criterion IDs, rather than reducing everything to one weighted score.

For optional qualitative dimensions such as maintainability, use a separate
0–3 rubric: 0 contradicted/absent, 1 vague or materially deficient, 2 usable
with a concrete limitation, 3 complete and source-supported. A high style score
cannot compensate for a failed hard gate. Preserve raw reviewer notes.

## 11. Failure classes and denominators

| Class | Example | Treatment |
| --- | --- | --- |
| Infrastructure | Server unavailable before inference, broken mount, package startup failure | Retain scheduled attempt; report separately from model-quality failures |
| Model/tool behavior | Malformed tool call, inventing a path despite correct tool access, skipping required read | Candidate failure, not automatically infrastructure |
| Contract/implementation | Wrong semantics, scope expansion, broken patch | Candidate failure |
| Evidence gap | Tool results not captured, missing validation logs | Unknown gate; no success claim |
| Expected blocker | Deliberately missing or conflicting dependency correctly detected | Pass for that control |
| Budget stop | Time, tool-call, output, or context limit reached | Retain as failure to complete under configured budget; classify cause |
| Protocol deviation | Operator supplied an unscheduled hint or versions changed mid-run | Keep raw attempt; flag comparability and assisted status |

Define eligibility before viewing results. Report scheduled, attempted, validly
executed, completed, passed, failed, blocked, invalid/deviating, and unrun counts.
Categories may need separate dimensions: e.g. an attempted run can be completed
but failed. Provide the mapping rather than forcing inconsistent totals.

Report both passed/scheduled and passed/validly-executed. Keep infrastructure
exclusions explicit and adjudicated against traces; do not use the label to
remove inconvenient model failures. Never count an unrun attempt as a pass or
omit it from the planned denominator without a visible disposition.

## 12. Evidence record

Keep evidence in an operator-selected experiment root outside model-visible
inputs. Use immutable per-run records, not a mutable `latest` result. Record
the selected root before scored execution. No execution directories are created
by this planning document.

Each record contains:

```text
run_id, experiment_id, task_id, condition_id, repetition, scheduled_order
start/end timestamps, stop_reason, protocol_deviations, assisted_status
hardware, OS build, LibreChat deployment/version, runtime package inventory
model repository/revision, quantization, tokenizer/template identities
server command and effective options, sampling, caps, cache settings
agent instructions/configuration, complete tool schemas and permissions
source commit, dirty-input identities, packet manifest and content hashes
actual model messages, tool calls, returned contents, errors/truncation
raw patch, apply result, resulting diff/source identity
validation commands, working directories, outputs, exit statuses
resource/timing observations, measurement method, missing telemetry
criterion-level scores, findings, reviewer identity, evidence pointers
```

Preserve raw traces before producing summaries. Keep credentials out of the
research corpus; document redactions without removing task-relevant content.
Hashes identify inputs; they do not establish reading, comprehension, or code
correctness. If the UI export omits content, retain the backend evidence too.

## 13. Review, analysis, and decision rules

Blind model labels for qualitative review where practical; do not blind away
necessary task/source evidence. The candidate must not be its sole evaluator.
The Operator or an explicitly assigned fresh reviewer checks the actual source
and reproduces tests. Self-review remains a separate observation. No reviewer
assignment or independent verdict has been fabricated by this protocol.

Report per condition:

1. Denominator reconciliation and all exclusions/deviations.
2. Hard-gate pass counts overall, per language, and per task/repetition.
3. Linked-content delivery and behavioral compliance separately.
4. Critical/major findings, invented evidence claims, and expected-stop results.
5. Paired N8/N4 task outcomes: both pass, only N8, only N4, neither.
6. Median and range of completion time and resource observations, with failures
   retained separately. Do not compare only successful runs without showing
   the resulting survivor bias.
7. First-pass and repaired outcomes separately; operator time separately.
8. Observation, interpretation, decision, limitations, and proposed next test.

Repeated runs are clustered within tasks. Thirty attempts per model are not
thirty independent task families. Avoid significance or equivalence claims from
this small pilot. If later estimating uncertainty, use task-aware paired
analysis and state the method before interpreting the result.

### Proposed supervised-use thresholds

Freeze or amend these before scored execution; they are proposed design values,
not an Operator acceptance verdict:

- At least 24 of 30 coding attempts pass every applicable hard gate.
- Each language has at least four of six passing attempts.
- No fabricated read/execution/pass claims.
- All expected-stop controls correctly stop affected work.
- No unresolved critical/major defect is accepted into actual repository work.
- Latency and intervention burden fit a recorded Operator budget, selected
  during practice. If no budget is declared, performance remains descriptive
  and cannot support an operational acceptance claim.

Passing supports a limited supervised trial with review retained. Failing can
justify narrower language/task routing, configuration repair, or another model;
do not quietly lower thresholds after seeing results.

For selecting N4 over N8, predeclare a material resource/latency benefit during
practice. As an initial quality rule, N4 should have no new evidence-honesty or
expected-stop failure, no newly systematic failure class, and no more than one
fewer passing attempt overall while meeting every language threshold. Even that
outcome supports only a provisional choice; it does not establish equivalence.
Choose N8 or collect more held-out evidence if the tradeoff remains ambiguous.

## 14. Experiment C: luna xhigh workflow reference

After the local pilot, run the same ten frozen tasks through the Operator's
existing luna xhigh workflow, ideally with three fresh attempts per task.
Record the exact profile/model identity available at execution time. Do not
assume a named profile has unchanged internals across dates.

Prefer matching patch-output mode, packet content, enabled tools, source state,
and stopping rules. If the existing workflow has shell execution, different
tool schemas, provider context handling, or inaccessible sampling settings,
document those differences and call the result a whole-workflow comparison.
Larger output or reasoning budgets are not a hidden advantage to ignore.

Compare paired task outcomes, linked-contract failures, correction burden,
elapsed time, and failure modes. Historical successful outputs alone are not a
fresh matched baseline. If the reference phase runs substantially later, note
provider/version/time drift and consider a local rerun on a held-out subset.

A useful conclusion might be: local N8 passed the declared threshold for the
tested bounded tasks but required more time or more review in a named language.
An unsupported conclusion would be: N8 is generally equivalent to luna xhigh.

## 15. Threats to validity and follow-up experiments

| Threat | Control / remaining limitation |
| --- | --- |
| Model and harness conflated | Commission transport separately; preserve raw tool traces. |
| Conversion differences called quantization | Inspect base/tokenizer/template provenance; disclose bundle differences. |
| Task or solution contamination | Fresh conversations, inaccessible prior results, frozen input copies. Public tasks may still have training contamination. |
| Context truncation | Budget real packet, inspect tool results, record actual delivery. |
| Evaluator expectations | Blind labels where possible, predeclared rubric, source-backed findings. |
| Small/selected corpus | Per-task/language reporting; later held-out tasks, no broad parity claim. |
| Model load/cache/thermal order effects | Balanced schedule, fixed warm-up policy, stable concurrency and recorded background load. |
| Different client environments | One scored LibreChat deployment; qualify the second client separately. |
| Generated tests flatter generated code | Evaluator-owned discriminating tests and semantic review. |
| Human patch repairs hidden | Preserve raw patch; assisted repair gets separate scoring. |
| Read receipts treated as understanding | Check both content delivery and example-dependent behavior. |

Follow-ups should isolate one new question: 32K versus 64K, a different
quantization, a smaller candidate, a changed intake prompt, or an autonomous
execution tool. Do not change all of them and credit only the model.

Before admitting an autonomous edit/test loop, qualify workspace isolation,
fixed command availability, real exit capture, filesystem visibility, and
artifact persistence. Then repeat the linked-file controls and a representative
coding subset under that new harness. Patch-output success does not establish
autonomous execution reliability.

## 16. Next execution sequence and current status

1. Confirm each LibreChat deployment mode/version and choose the scored client.
2. Commission vLLM-Metal/N8 and the complete filesystem-tool round trip.
3. Establish the raw evidence capture route and target execution/evidence roots.
4. Author and verify the small linked-example fixture using the relevant domain
   skill; run the 25-attempt diagnostic with frozen packet variants.
5. Construct and validate the ten-task corpus and two separate practice tasks.
6. Freeze budgets/schedule; commission N4 and repeat its 25-attempt diagnostic;
   run the separate 60-attempt coding comparison.
7. Review evidence and make the scoped routing decision.
8. Run the matched luna reference and any specifically justified follow-up.

No model has been installed or scored by authoring these documents. No task
fixtures or compiled oracle suite are claimed complete. The runbook and protocol
are now durable drafts; target commissioning, corpus construction, and execution
are the explicit remaining work.

## Document history

- 2026-09-22: Initial protocol under the Operator-approved standalone-document
  layout; linked-file controls, quantization pilot, workflow reference,
  evidence contract, failure denominators, and provisional decision thresholds.
