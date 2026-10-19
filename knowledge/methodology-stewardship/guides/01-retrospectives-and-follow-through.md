# Retrospectives and Follow-through

## Purpose and authority

A retrospective explains what helped or hindered the actual goal and what to
learn next. Start from the promised capability and delivered result, then
examine the work that produced them. A completed evidence packet can be a
legitimate intermediate outcome; it is not necessarily the final product.

In the Three-Contributor Workflow and Autonomous Mode, CDC performs this analysis at every slice,
arc and project close. CRC supplies the operational record through the existing
Operator relay and retains routine implementation review and slice acceptance.
CDC's role includes examining its own plans, examples and decisions. A separate
context provides useful distance, but a contributor's analysis of its own
method is not independent evidence that the method is effective.

In Autonomous Mode, the retrospective duty survives every contributor
reassignment. CDC gathers contributor/reviewer evidence directly under the
recorded authorization, examines its own implementation or coordination choices,
and completes the record at each closing scale. Independent code review is
still required; a retrospective cannot supply it. Apply the same evidence and
follow-through standards whether CRC is assigned or not.

Project-management owns record placement and closing mechanics; engineering-
methods owns contributor authority. This guide owns retrospective analysis.
Recommendations use the existing decision and handoff routes. A correctness or
scope defect discovered here goes promptly to the assigned reviewer; do not
leave it as a future learning item. Do not silently reverse an acceptance,
rewrite issued prompts, or introduce a new requirement through a retrospective.

## Observe during execution, synthesize at closure

Use existing notes for observations while work proceeds. Repeated failures or
lost checks deserve attention when discovered, not only after acceptance. At
closure, create or complete the owning `cdc-retrospective.md`; do not create
empty success records at opening. Read the governing plan, actual prompts,
returns, relevant evidence and review history, including failed attempts.

Identify the reviewed revision or bounded time window, author/context, outcome,
and material gaps in available evidence. Follow significant claims to their
source; self-reports and a green replay are different from independent review.
Read complete relevant passages and recover truncated output. Do not reproduce
an entire implementation audit merely to write a retrospective. Name what was
inspected, retained from prior review, sampled or unavailable.

Look for both adverse evidence and successful counterexamples. Account for
reviewer mistakes, changed requirements, unavailable inputs, and legitimate
exploration before interpreting correction rounds as avoidable rework. Do not
infer an unread instruction, bad intent, or a model limitation from an error
alone. Report exposure or effort as unknown where it was not observed.

## Questions at each scale

| Scale | Analysis | Recommendation destination |
|---|---|---|
| Slice | Which concrete difficulties occurred? What was already specified? Which repairs worked, recurred or broke something else? What did planning and review contribute? | Focused observations or changes for subsequent slice preparation/review, with the affected owner. |
| Arc | Which mechanisms repeat across slices, including successful exceptions? Were decomposition, dependencies, interfaces or prompting patterns responsible? Did earlier recommendations help? | Project-level prompting and workflow proposals; structural plan changes follow normal CDC/Operator authority. |
| Project | Which patterns repeat across arcs? Did accumulated process work help deliver the intended capability? Where does the evidence cease to generalize? | Scoped proposals for collaboration-framework or its owning component skills, including rationale, applicability limits and evaluation needs. |

Synthesize upward rather than concatenate child reports. Link the child evidence
that supports a pattern and explain what the higher-scale comparison adds.
Include difficult, blocked and unremarkable children; do not select only those
that support a favored explanation. Missing child observations are evidence
limits, not negative findings. Check earlier recommendations explicitly: adopted,
deferred, declined, not yet tried, or evaluated with a stated outcome.

## A compact, usable record

Use the following content, adapting headings and detail to the work:

1. **Outcome and scope:** intended capability, actual result, evidence cutoff,
   author/context and inspection limits.
2. **Observations:** concrete symptoms and successes with source paths and pins;
   distinguish the original requirement, attempted response and observed outcome.
3. **Interpretation:** suspected mechanism, alternative explanations, confidence,
   contrary evidence and what remains unknown.
4. **Recommendations and watch items:** a specific change or question, its owner
   or decision route, where it applies, and what later observation would support
   or contradict its usefulness.
5. **Follow-through:** decisions and observed effects of earlier recommendations,
   with links to their implementation or subsequent analysis.

A short “no material new pattern observed” is valid when it states the inspected
scope and follows up any outstanding watch items. No quota of findings, pages,
metrics, or changes applies. Stable local labels help only when a finding needs
to be tracked across scales; do not build a second ledger for ordinary notes.

Keep observations, explanations, recommendations and authorized decisions
visibly distinct. For example: “the same qualifier remained omitted after the
prompt named it” is an observation; “the example did not demonstrate a complete
multiline assertion” is a candidate explanation to check against that example;
“demonstrate the complete path and test transfer to another case” is a proposal,
not a proven cure or a new instruction to the active implementer.

## Symptoms worth investigating

These are diagnostic prompts, not proof of a cause or universal failure rules.

| Symptom | Inspect before concluding |
|---|---|
| A targeted correction returns unresolved | Compare the exact requirement, worked example, original input and actual output. Was the method demonstrated, misunderstood, partly applied, or inadequate? |
| More detailed instructions without better results | Determine whether the added detail resolves a real ambiguity and reaches the final consumed output; examples may demonstrate only an easier subproblem. |
| Inventory or field counts pass while meaning is missing | Check complete assertions and qualifiers, actual comparison objects, and whether the expected population was derived from the same incomplete result. |
| A checker passes an unusable deliverable | Inspect the entire consumed artifact and composed output, not just copied fields or the first parsed block. Test a plausible wrong result through the actual checking route. |
| A repair loses previously working checks | Compare the previous and current checks and their failure cases. Distinguish a new defect from recurrence or regression. More negative specimens do not necessarily cover more properties. |
| Iteration ends in receipt-only corrections | Check whether identity data can be derived reliably, whether a stale current summary misleads, and whether reviewer instructions created unnecessary duplication. Preserve truthful provenance. |
| Reviews repeatedly discover foreseeable problems late | Inspect author preparation, review coverage, feedback consolidation and whether already available findings reached the next assignment. Include CDC/CRC errors. |
| Evidence grows faster than useful decisions | Trace significant artifacts to a deliverable, decision, verification or preservation need. Look for conflicting current authorities and unconsumed duplicate payload. |
| Fewer corrections are presented as success | Check comparable scope, task difficulty, retained quality gates, total preparation/review effort and censoring. An unfinished baseline is not a completed time-to-acceptance comparator. |

Use recurrence terms precisely: persistence is the same unresolved defect;
recurrence is the same mechanism in another instance; regression breaks
previously working behavior; new discovery was not previously established.
Cite the related instances instead of counting bundled review labels as defects.

## Evidence economy and goal alignment

Link to existing records and Git revisions rather than copying entire datasets
into retrospectives. Keep one clearly identified current analysis; preserve
superseded interpretations with dates or revision references. Do not accumulate
competing current conclusions. A new supporting artifact needs a concrete use
that existing evidence cannot adequately serve; preserve necessary raw evidence.

Assess utility, not size alone. Large archives can support reproducibility;
small ceremonial reports can waste attention. An artifact awaiting its planned
consumer is not automatically unused waste. Track whether later implementation,
review or research actually consumes accepted handoffs before claiming goal
displacement. Observe the cost of this retrospective work too. Avoid per-file
bureaucracy, arbitrary caps, or cleanup based solely on volume.

### Research usefulness and reconstruction

Improvements to execution or evidence handling must preserve full ledger
coverage, independent verification, original observations and long-term research
value. Use the canonical
[record contract](../../project-management/guides/02-canonical-planning-worktree.md#evidence-batches-and-research-records)
for inputs/instructions, source/environment and model/settings provenance,
commands/results, failed attempts, decisions and original/superseding references.
A batch index and concise current view supplement the mandatory per-scale records.

At an agreed evaluation point, ask a fresh reviewer to reconstruct an actual
failed attempt, its repair, the accepted candidate and decision reasons from the
retained authorized records, including independent review and remaining gates.
Record missing inputs, access/redaction limits and unresolved identities. Check
portability beyond local paths and expiring hosted links; a short trial cannot
establish multi-year durability. Preserve earlier observations and record
corrections or migrations with explicit mapping/provenance.

For a bounded Operator-approved trial, predeclare the question, consumer, scope,
budget, quality invariants and stopping condition. Observe row completeness,
traceability/reconstruction quality, actual Operator interruptions, coordination
failures, correction causes and repeated checks. Record available time/usage by
role and requested/observed model configuration; unavailable is not zero. Separate
necessary validation, justified new scope and avoidable rework. Fewer corrections,
files or tokens alone cannot establish success. Changes of staffing/model or task
scope are confounds unless intentionally studied; follow scientific-methods for
comparisons and do not start a trial merely because guidance recommends one.

## From recommendation to evaluated change

Recommend the smallest change justified by the evidence and name its likely
costs and failure modes. Local prompting improvements belong in subsequent
assignments through their author; project-level changes need the existing plan
and decision record; framework proposals identify the owning skill and actual
behavior to change. A retrospective does not enact any of these automatically.

For comparative effectiveness claims or a new trial, use scientific-methods:
state the hypothesis, comparison, measures and limitations before execution.
Keep scope and quality fixed where possible; separate contexts alone do not
remove task difficulty, learning, exposure or model-setting confounds. Do not
prescribe a model or estimate unobserved time/tokens. Record improvements,
regressions and inconclusive outcomes, including changes that were not adopted.

At the next relevant close, revisit the recommendation against its predicted
observation. Retain, revise or retire it explicitly. Wider adoption should be
challenged by the Operator or an appropriate fresh reviewer, especially when CDC
helped design the method under study. A single project can justify a proposal
without establishing a universal rule.
