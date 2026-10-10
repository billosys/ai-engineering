# Experiment01 — Source-grounded preparation and review pilot

Protocol revision 2, recorded 2026-10-10 before any treatment assignment.
Status: prepared; zero registered/executed treatment runs.

## Question, hypothesis and decision

Does a bundled change in preparation and review reduce recurring evidence and
interpretation defects in Project10 slices while preserving complete scope,
correctness, usable outputs and independent acceptance?

H1: worked examples plus inventory-first analysis and comprehensive verification
planning reduce repeated failure types and uncovered requirements in returned work.
H2: compact current records reduce avoidable maintenance work without losing
traceability. Contrary evidence includes recurring defects despite demonstrated
examples, missed scope, unsupported acceptance, weaker checks, or an increase in
preparation/review cost without a corresponding quality benefit.

Use results to retain, revise, or reject this **local bundle** and decide what
additional comparison would justify broader framework changes. Do not infer a
causal effect, an effect size, a particular component's benefit, or CRC efficacy
from two heterogeneous slices.

## Design and selection

This is a prospective two-case series with a retrospective comparator:
[Case01](../case01-colour-pipeline/case-study.md), initial plus three corrections,
through review `9a30f480`. The comparator remained open at its cutoff; never call
its four observed returns a completed time-to-acceptance baseline.

Register the next two newly opened Project10 slices after this protocol takes
effect, in normal roadmap/readiness order. The exact IDs, populations, source
pins, initial prompts and protocol commit are recorded in the [run register](run-register.md)
**before issuance**. Do not select on expected success or replace an inconvenient
run. If a selected slice is input-blocked, retain its blocked outcome. No new
slice is opened solely to make the trial look good; no oversized work is hidden
by splitting and reporting only the easier child. Record necessary decompositions
and their union as a change in comparability.

Current Arc02/Slice02 Iteration04 is already issued and apparently in progress.
It is excluded from treatment, continues under its existing instructions, and
may be appended later as observational follow-up. Never change its prompt,
requirements, or status retroactively to fit this trial.

## Intervention bundle

Apply in existing slice-plan/prompt/notes/review homes. Do not create extra roles
or a parallel acceptance tree.

1. **Author preparation:** inspect the actual inputs and choose two to four
   representative difficult cases, including a plausible wrong interpretation.
   Work through one complete local record or implementation path, its evidence,
   expected check and limitation. Label author examples as examples, not accepted
   CC results. For semantic work include original-versus-replacement, paired
   consistency, and unavailable evidence where applicable. Adapt to other work;
   do not force a claim schema on a coding or formatting task.
2. **Inventory before judgment:** define complete units and context/qualification
   boundaries before batch assessments. Keep literal subject, verdict, evidence
   applicability and proposed correction separate. An observed discrepancy can
   amend the inventory with explicit lineage; expected counts are not answers.
3. **Verification design:** for each promised property name the observable field
   or behavior, predicate/manual review and a plausible failure it discriminates.
   Check intermediate fields when claiming staged coverage. Distinguish mechanical
   integrity from semantic warrant. Reuse existing checks; any new helper needs
   a named gap, a small allowed home and a reproducible invocation.
4. **CC execution:** exercise the representative path before expanding to the
   batch, record the observation briefly, and apply it consistently. If it fails,
   diagnose before expansion. Proceed under existing authority when it succeeds;
   independent acceptance still occurs through the normal review.
5. **Reviewer method:** assess inventory coverage, literal proposition identity,
   evidence applicability, numerical/behavioral check coverage, handoff consistency
   and preservation together before issuing consolidated feedback. Check the
   reviewer's own comparison targets and examples. A new requirement or changed
   interpretation is recorded as such, not mislabeled as CC noncompliance.
6. **Recurrence response:** if a failure type remains after a correction expressly
   targeted it, record the failed approach and a small discriminating repair
   example before another bulk pass. Preserve existing iteration counts and gates;
   the response does not create a free retry or reset the five-iteration limit.
7. **Record economy:** keep a clearly identified current result/checker and pinned
   references to historical versions; avoid embedding predecessor datasets merely
   to prove preservation. Generate routine identity metadata where practical.
   Required reading, failed attempts and existing history-preservation rules remain.

CC receives concrete task instructions, not a target reduction in defects or a
request to make the intervention win. The hypothesis is visible to the research
reviewer; this pilot is not blinded. If CC reads it too, record that exposure.

## Constants, setup and accepted confounds

Keep Project10 scope, ledger criteria, source-readiness boundaries, role separation,
Operator relay and acceptance standard intact. Use the same task-relevant tools
and established checks where applicable. Preserve the source baseline where
possible; record changed inputs rather than pretending identical tasks.

At registration record: slice path and execution family, task kind, required
units and denominator basis, source/plan/prompt/protocol pins, available and
blocked inputs, output scope, tools/permissions, CDC/CC identities, model and
reasoning settings **only if observable**, session reuse and prior-case exposure.
Unknown settings remain unknown. Do not change models for the experiment without
Operator direction. Pin the issued contract; subsequent changes are deviations.

Different tasks, difficulty, learning/order effects, evolving installed guidance,
model/context differences, reviewer expectations, and a bundled intervention
limit attribution. Comparable denominators must be established before reporting
rates. Never normalize by JSONL row count merely because it is easy to count.

## Measures and coding rules

Use the host notes/closing report for CC observations and the independent review
for acceptance/findings. CDC copies concise references and measurements into the
run register; CC need not edit Project13. No fabricated time or token estimates.

| Measure | Definition and collection | Baseline / interpretation |
|---|---|---|
| Returns and corrections | Count each returned CC assignment; count corrective assignments actually executed separately; list receipt-only commits without counting them as another assignment | Baseline: initial + 3 completed corrections, still open; compare fixed windows and explicitly censored endpoints |
| First-return acceptance | Independently accepted criteria / all governing criteria at first review; also report which criteria and their difficulty | Baseline 2/9; descriptive, not a comparable percentage of effort |
| Recurrent failure types | For each review, record type, specific defect, original requirement, evidence, predecessor finding, and whether an expressly targeted correction failed to remove it | Baseline chains C02/C03/C04/C06 are qualitative evidence; bundled F numbers are not atomic defect counts |
| Coverage and correctness | Reviewer lists omitted required units / declared units when a defensible denominator exists, wrong original propositions, unsupported warrants and contradictory handoff judgments | Baseline exact counts not reconstructed; unknown remains unknown; absence of findings is not proof of full coverage |
| Validation gaps and false passes | Record each promised property actually left unchecked and each supplied invalid specimen accepted by its claimed check; do not count several probes of the same gap as distinct defects | Baseline examples: XYZ/polar fields, RGB stages, fragments; property-level comparison required |
| Reviewer contribution | Record mistaken examples, changed interpretations, late requirements and own corrected findings separately from CC execution defects | Baseline C05 and receipt tightening in C06; do not attribute all rework to CC |
| Evidence burden and effort | Bytes of prompt/current outputs/notes, historical payload versus current working content; observed preparation, execution and review time/tokens only when available | Baseline JSON has bytes; complete effort unknown. Smaller files alone do not show improvement |
| Artifact utility and goal displacement | Relate significant artifact work to an actual deliverable, decision or verification need; record duplicated/unconsumed material, maintenance-only churn, and packet completion substituted for outcome progress, with concrete examples and counterexamples | Qualitative prospective observation added in revision 2; baseline burden alone does not establish displacement; no size threshold or retrospective score |
| Intervention adherence | For each of the seven components record used / partial / not applicable / not used, with a pointer and explanation | Distinguish a failed intervention from an intervention never applied; no composite score |
| Quality and authority gates | Scope retained, meaningful checks, honest unresolved inputs, independent acceptance, no unsupported closure | A failure prevents any clean improvement conclusion regardless of iteration count |

For finding classification use: coverage/context; proposition identity/history;
evidence applicability/consistency; validation coverage; replacement/handoff;
receipt/identity; link/format; reviewer-introduced requirement/error; other.
Assign one primary type and optional secondary tags. Distinguish persistence
(same unresolved defect), recurrence (same failure mechanism in another unit),
regression (previously correct/accepted behavior broken), and new discovery.
A recurrence count must include its cited finding pairs. New classes are allowed
but logged as exploratory additions; never silently recode the baseline.

### Artifact-use observation added before treatment

At each review/meta-review, ask what the artifact work enabled for the actual
project purpose, and whether its creation, navigation or upkeep displaced that
work. Distinguish necessary evidence production, legitimate research preservation,
useful reuse, justified awaiting-use material, and avoidable accumulation. A file
not yet consumed is not automatically waste. Cite the observed activity and its
consequence; unknown utility or cost remains unknown. Record benefits as well as
costs, including evidence that changed a decision or caught an error.

Use a short paragraph in the existing review/register, including Project13's own
research overhead where observable. Do not create a per-file bureaucracy to
measure bureaucracy. This is an observation addition, not a new treatment
component, retention policy, cleanup assignment or acceptance gate. The frozen
Case01 remains unchanged; any later reanalysis under this lens must be explicitly
labeled retrospective, not a predeclared baseline result.

## Review checkpoints, stopping and decision rule

After the first trial slice is independently closed **or reaches a recorded
blocked/escalation stop**, complete a short meta-review before issuing the next
trial prompt. Compare each observable measure to Case01, inspect costs and
regressions, and check adherence. After the second, write the final comparison
before extending the intervention or issuing a third slice under this trial.
These checkpoints are the Operator-requested measurement pauses within Project10's
Expedited cadence; they do not bypass normal closure/advancement gates.

Default is two runs. End after one only for an explicit Operator decision,
unresolved input/escalation preventing a second, or an observed quality/authority
regression requiring correction of the method. Record the reason and incomplete
sample. An unstarted or blocked run is not replaced. A protocol adjustment after
run one is recorded as a new revision and changed treatment, not pooled as the
same intervention. No automatic broad adoption follows a favorable first run.

Use three recommendation outcomes:

- **Retain locally for further testing:** observed repeat/gap patterns improve,
  quality gates hold, and measured costs show no material offsetting regression;
  if cost is unknown, qualify the recommendation and make no efficiency claim.
- **Revise or reject:** quality regresses, recurrence persists despite adherence,
  or observed preparation/maintenance costs outweigh the benefit. Explain the
  evidence rather than imposing an arbitrary aggregate threshold.
- **Inconclusive:** task differences, missing measures, mixed results or protocol
  deviations prevent a useful comparison. Specify the smallest next test.

The meta-review separates raw result, measured difference, interpretation and
decision. Include contrary examples and limits. CDC can prepare it, but a fresh
independent reviewer or Operator must challenge it before framework-wide adoption;
no such review is pre-recorded. Do not invent significance tests for n=1–2.

## Amendment history

- Revision 2 (2026-10-10): Before any treatment registration, added the Operator's
  artifact-utility/goal-displacement concern as a qualitative measure. No change
  to the seven-component intervention, selection, quality gates or frozen baseline.

- Revision 1 (2026-10-10): Prospectively defined before treatment registration.
