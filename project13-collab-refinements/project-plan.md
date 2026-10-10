---
project: project13-collab-refinements
status: active-bootstrap
depends-on: []
blocks: []
related: [project10-design-foundations]
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
  records eligibility and eventual results. No trial has run yet.

The intervention bundles worked examples, inventory-first analysis, explicit
verification coverage, comprehensive reviewer checks, a response to recurring
failure types, and compact current records with preserved history. Test it on
the next two newly opened Project10 slices, registering each before its initial
prompt is issued. Review after the first and after the second. Do not choose
only favorable slices or discard blocked/failed runs. Treat this as a prospective
case series with a retrospective comparator, not a randomized or same-task A/B
test. The protocol defines how to end after one run if necessary.

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

- 1.0 (2026-10-10): Operator-requested placeholder project, frozen Case01 and
  prospective Experiment01; local Project10 trial instructions added. Trial
  execution, measurements and general adoption remain pending.
