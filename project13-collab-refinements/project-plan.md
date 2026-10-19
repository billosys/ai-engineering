---
project: project13-collab-refinements
status: active-bootstrap
depends-on: []
blocks: []
related: [project10-design-foundations, "billosys/ai-engineering#6"]
---

# Collaboration Refinements

## Vision and provisional scope

Improve the CDC/CRC/CC planning and implementation methodology through observed
cases, explicit hypotheses, bounded trials, and comparison of outcomes. Improve
source-grounded preparation, implementation guidance, independent review and
handoffs while preserving correctness, complete scope and Operator authority.
Less avoidable rework is a desired result; a smaller iteration count alone is
not success.

This is a placeholder project plan, intentionally incomplete beyond the first
case and trial. Expand the roadmap as evidence accumulates. No framework-wide
method change or claim of general effectiveness is adopted by this bootstrap.
The vision covers CDC/CRC/CC; the first trial exercises the existing CDC + CC
workflow and cannot establish benefits for CRC or three-contributor workflows.

## Operator authority and layout

On 2026-10-10 the Operator requested this project, a project-level `artifacts/`
home with a case-study subdirectory, copied supporting evidence, an experimental
method adjustment, and measurements/comparison after one or two slices.
Planning stays on branch `planning` at `.worktrees/planning`.
The project-level artifact location is an explicit Operator override for these
cross-slice research records. Execution slices continue to own their normal
artifacts and acceptance records in Project10.

The request authorizes this bootstrap and bounded trial preparation. It does
not close Project10's current slice, rewrite issued prompts, authorize new source
work, or select a different contributor workflow. Project10's in-flight
Arc02/Slice02 correction continues under its issued contract. Its later results
are follow-up context, not a prospectively assigned treatment run.

## Evidence and first experiment

- [Case01: nonlinear colour-pipeline rework](artifacts/case01-colour-pipeline/case-study.md)
  preserves the initial return and Iterations01–03 through CDC review `9a30f480`.
- [Evidence manifest](artifacts/case01-colour-pipeline/evidence-manifest.json)
  identifies 50 immutable copies; [baseline measures](artifacts/case01-colour-pipeline/baseline-measures.json)
  distinguish mechanical observations, report classifications and unknowns.
- [Experiment01 protocol](artifacts/experiment01-methodology-pilot/protocol.md)
  predeclares the intervention, selection, measures, limits and review points.
- [Run register](artifacts/experiment01-methodology-pilot/run-register.md)
  records eligibility and outcomes: both T01/T02 independently closed after
  initial+four corrections, with full bounded host acceptance. The
  [final comparison](artifacts/experiment01-methodology-pilot/comparison.md)
  completes the two-run checkpoint at host closeb6acb22f; benefit remains
  inconclusive and the recommendation is to revise before another authorized test.
  The pilot ends; no third run or general adoption. The preserved
  [interim analysis](artifacts/experiment01-methodology-pilot/interim-analysis.md)
  retains its H2 cutoff; research acceptance/challenge remain pending.

The intervention bundles worked examples, inventory-first analysis, explicit
verification coverage, comprehensive reviewer checks, a response to recurring
failure types, and compact current records with preserved history. Test it on
the next two newly opened Project10 slices, registering each before its initial
prompt is issued. Review after the first and after the second. Do not choose
only favorable slices or discard blocked/failed runs. Treat this as a prospective
case series with a retrospective comparator, not a randomized or same-task A/B
test. The protocol defines how to end after one run if necessary.

## Operator concern: artifact accumulation and goal displacement

Recorded 2026-10-10 for observation, not immediate framework changes. The Operator
reports introducing artifact-directory support at project, arc and slice levels
within roughly the preceding three months (release/date not investigated here).
The benefit is substantial: preserved evidence supports reproducibility, process
comparisons over time and evaluations of frontier models. Preserve that benefit.

The concern has two parts: excessive data is deposited in artifacts, and the
artifact collection can become the perceived project, displacing its actual
purpose and deliverable. The provisional hypothesis is that producing and
maintaining evidence can become a substitute for advancing or verifying the
intended outcome. Volume alone does not establish that failure; a large necessary
archive can be useful, and a small ceremonial record can still distract.

In subsequent passes, examine concrete links between artifacts, decisions,
verification and actual project progress. Look for unused/duplicated payload,
maintenance without new evidentiary value, and completion claims about packets
that obscure unfinished deliverables. Also record counterexamples where retained
evidence prevented error, enabled independent review or made later science possible.
Apply the same scrutiny to Project13's own research outputs. Its expressly
requested frozen case-study copies are not presumed waste merely because they
are numerous; their utility and handling cost are questions to inspect.

The trial protocol adds this as a qualitative observation alongside evidence
burden. No cleanup, size cap, new acceptance gate, changed CC assignment or
framework/skill edit is authorized by recording it. If the evidence supports
later guidance on artifact use, investigate the owning specification and propose
a bounded change through normal review; do not assume its location or diagnosis.

## Provisional roadmap and definition of done

| Candidate workstream | Outcome | Depends on |
|---|---|---|
| Case collection and diagnosis | Reproducible case studies with observations separated from explanations | Available committed evidence |
| Bounded methodology trials | Predeclared changes and complete run records, including regressions | A case, protocol and an eligible host project |
| Synthesis and adoption | Decide retain/revise/reject; propose narrowly justified framework changes | Comparative evidence and independent/Operator review |

These are roadmap placeholders, not opened arcs or issued CC assignments.
Create actual arcs/slices when a coherent implementation scope is ready. The
project's eventual completion requires evidence-backed recommendations, honest
limits, and accepted implementation/validation of any selected framework changes;
its final scope and release deliverables remain to be defined with the Operator.
The [ledger](ledger.md) records the currently known obligations without claiming
that this placeholder is a complete project definition of done.

## Workflow and measurement authority

Default Two-Contributor Workflow applies to implementation: CDC Sofie plans and
reviews; a separate CC context executes through Operator relay. No CRC is assigned.
CDC authors this research bootstrap and performs attributed self-checks; that is
not independent verification of the case analysis. A separate reviewer or the
Operator must challenge the comparison and recommendations before general adoption.
Project13 has no independent Expedited Mode selection. Project10 retains its
existing selection, with the trial checkpoints recorded in its plan.

Raw host-slice evidence remains authoritative. Project13 stores snapshots and
analyses, not competing acceptance verdicts. Preserve all issued prompts and
past records. Changes to a trial protocol after registration require a dated
amendment and a deviation record; do not rescore history silently. No current
skill/package or repository-wide AGENTS change is authorized by this bootstrap.

## Version History

- 1.8 (2026-10-19): Explicit issue6 implementation authorization, canonical
  standalone slice and pending external PR review; no old protocol or acceptance
  changes and no trial execution.

- 1.7 (2026-10-12): T02 independent host closure and final two-run comparison;
  pilot ends, comparative benefit inconclusive, revise-before-testing recommendation.
  Frozen evidence/research criteria retained; no third run/adoption/research acceptance.

- 1.6 (2026-10-12): Operator-requested interim analysis through T02 I02 return;
  no new host acceptance. Reproduced packet measurements and six competing
  registries, reconciled stale research summary, retained protocol/baseline and
  deferred final comparison/adoption until their evidence and gates are satisfied.

- 1.5 (2026-10-11): Recorded T02 first corrective return C1/H1, independent
  host4/9 cumulative acceptance and targeted persistence/recurrence witnesses.
  Iteration02 issued after bounded repair; frozen protocol/research gates retained.

- 1.4 (2026-10-11): Recorded T02 initial return/partial independent host review
  (one of nine accepted), consolidated correction and actual trial observations.
  Frozen protocol, research criteria and final comparison/adoption gates retained.

- 1.3 (2026-10-11): Prospectively registered and issued T02 for the next ready
  Project10 layout/measure concern after completed T01 checkpoint; frozen protocol
  unchanged, execution/research acceptance and final comparison remain pending.

- 1.2 (2026-10-11): Recorded T01 host closure and first meta-review checkpoint;
  mixed/inconclusive results, unchanged protocol and authorized second consecutive
  host run. No research acceptance or broad adoption inferred.


- 1.1 (2026-10-10): Recorded Operator concern about artifact accumulation and
  displacement of project goals; added prospective qualitative observation,
  preserving the benefits of evidence retention and deferring framework changes.

- 1.0 (2026-10-10): Operator-requested placeholder project, frozen Case01 and
  prospective Experiment01; local Project10 trial instructions added. Trial
  execution, measurements and general adoption remain pending.

## Operator-authorized issue6 implementation — 2026-10-19

The Operator separately authorizes implementing Autonomous Mode reliability and
research-record improvements from billosys/ai-engineering#6, committing/pushing a
dedicated branch and opening a PR. This new source authorization is bounded to
[slice01-autonomous-mode-reliability](slice01-autonomous-mode-reliability/slice-plan.md),
a single coherent guidance/package candidate, independent of the completed earlier
research pilot. It supersedes the bootstrap's no-source-edit restriction only for
this assignment; prior research findings, frozen records and five research gates
remain unchanged and unaccepted. No new prospective trial or general performance
claim is authorized.

Codex implements on codex/autonomous-mode-reliability from fetched main f2b1137a;
the Operator and two other GPT instances will independently review through the PR.
These are future actual reviews, not assumed approvals. Use the default
two-contributor separation with reviewers supplied by the Operator; no Autonomous
execution, new subagents or fictional author/reviewer identities. Candidate delivery
is distinct from integration, published release and accepted research effectiveness.

