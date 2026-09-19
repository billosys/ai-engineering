# CRC Escalation 02: Split The Retained Provenance Surface

Date: 2026-09-18. From: CRC. To: CDC through the Operator.
Owning project: `project08-concept-card-metadata`; owning arc:
`arc06-semantic-families-and-capability-requirements`. Originating slice:
`slice16-supporting-record-actor-mode-and-role` (closed). This is arc-level
design exchange 02 and follows the implemented decisions in
`cdc-directive01.md`. Current CC assignment: none. Do not send this packet to
CC.

## State And Evidence

- Planning acceptance commit: `3841734b`. Slice16 CC registry endpoint:
  `9c8ea3a228bc5991126b2a8daf2b1e0a154175fe`; independently selected replay
  recipe: `713b88607b86c92fbedb50461829f52b20939efe`.
- Source HEAD at independent review:
  `ce3f77103eff5e07b3533a03c65f158684fc1039`; no source edit was made. Both
  worktrees were clean after Slice16 acceptance.
- Governing versions: project plan 1.34, arc plan 1.22 and closed Slice16 plan
  1.2. Slice16 ledger S16-1 through S16-6 are done under its independent CRC
  verdict. Arc rows A6-1 through A6-10 and project rows P-1 through P-15 remain
  open.
- Current coverage is exactly 555 full / 220 accepted / 335 remaining / zero
  assigned. Slice16's twelve pairs entered accepted coverage once. The frozen
  transition register is unchanged.
- Arc `cdc-directive01.md` requires CRC to enumerate the remaining provenance
  pairs, resolve cross-family primary ownership and propose a bounded split to
  CDC before Slice17 opens. This report performs that sizing; it accepts and
  assigns no pair.

## Finding

The retained Slice17 description names several distinct semantic jobs rather
than one executable unit. An exact current-register projection finds **87
remaining provenance candidates** within that retained description:

| Candidate group | Pairs | Principal distinction |
| --- | ---: | --- |
| Extraction-run operation, inputs, method and time | 18 | What operation ran, against which source/preparation/method context |
| Extraction-run scope, workers and outputs | 22 | Planned versus actual work, worker topology and produced-record identity |
| Cross-record run references | 19 | Record-to-run linkage and nested target identity/path/revision |
| Cross-record creation time | 11 | Record creation assertion without inventing a global timestamp policy |
| Cross-record preparation and method references | 17 | Prepared representation and method linkage with component applicability |

The five groups are disjoint, all 87 pairs are currently remaining, and none
overlap the 220 accepted pairs. They leave 248 pairs under the existing
evidence/lifecycle, recomposition, research and requirements owners. The 87
are not automatically semantically equivalent merely because they share a
field prefix.

Native inputs make a single packet especially risky. The extraction-run
population has only three current records: one template and two synthetic
examples. The template uses nullable scalar operation/time/method fields,
mapping-valued `output_refs`, separate `agent_scope` and
`parallel_worker_count`, and list-valued `worker_outputs`. The synthetic
examples instead populate singular `input_source_ref` and
`prepared_source_ref`, sequence-valued `output_refs`, and nested
`worker_scope`; one lacks reference paths. These shape and applicability
differences are useful diagnostic evidence, but they prevent a safe
prefix-only interpretation.

Across other kinds, `run_refs`, `created_at`, `prepared_source_refs` and
`method_ref` cross claims, competency questions, cards and several supporting
or lifecycle records. Their authority, requiredness, inheritance and target
resolution cannot be inferred from the extraction-run record or from shared
`id/path/revision` spelling. Accepted identity, locator, support, relationship
and CQ findings remain evidence inputs, not substitute meanings.

## Exact Candidate Sets

These sets are a sizing proposal, not approved assignments.

### A. Run operation, inputs, method and time: 18

~~~json
[
  ["finished_at","extraction-run"],
  ["input_source_ref","extraction-run"],
  ["input_source_ref.id","extraction-run"],
  ["input_source_ref.path","extraction-run"],
  ["input_source_ref.revision","extraction-run"],
  ["method_ref","extraction-run"],
  ["old_card_inputs","extraction-run"],
  ["operation","extraction-run"],
  ["prepared_source_ref","extraction-run"],
  ["prepared_source_ref.id","extraction-run"],
  ["prepared_source_ref.path","extraction-run"],
  ["prepared_source_ref.revision","extraction-run"],
  ["prepared_source_refs","extraction-run"],
  ["prior_run_refs","extraction-run"],
  ["prompt_ref","extraction-run"],
  ["settings","extraction-run"],
  ["source_snapshot_refs","extraction-run"],
  ["started_at","extraction-run"]
]
~~~

### B. Run scope, workers and outputs: 22

~~~json
[
  ["actual_coverage","extraction-run"],
  ["agent_scope","extraction-run"],
  ["intended_outputs","extraction-run"],
  ["intended_scope","extraction-run"],
  ["output_refs","extraction-run"],
  ["output_refs.cards","extraction-run"],
  ["output_refs.claims","extraction-run"],
  ["output_refs.cqs","extraction-run"],
  ["output_refs.edges","extraction-run"],
  ["output_refs.locators","extraction-run"],
  ["output_refs.source_support","extraction-run"],
  ["output_refs[]","extraction-run"],
  ["output_refs[].id","extraction-run"],
  ["output_refs[].record_type","extraction-run"],
  ["output_refs[].revision","extraction-run"],
  ["parallel_worker_count","extraction-run"],
  ["worker_outputs","extraction-run"],
  ["worker_scope","extraction-run"],
  ["worker_scope.mode","extraction-run"],
  ["worker_scope.roles","extraction-run"],
  ["worker_scope.roles[]","extraction-run"],
  ["worker_scope.worker_count","extraction-run"]
]
~~~

### C. Cross-record run references: 19

~~~json
[
  ["run_refs","claim"],
  ["run_refs","competency-question"],
  ["run_refs","concept-card"],
  ["run_refs","memory-admission"],
  ["run_refs","preservation-decision"],
  ["run_refs","reconciliation-result"],
  ["run_refs","relationship-edge"],
  ["run_refs","source-locator"],
  ["run_refs","source-support"],
  ["run_refs","validation-result"],
  ["run_refs","verification-result"],
  ["run_refs[]","concept-card"],
  ["run_refs[]","source-support"],
  ["run_refs[].id","concept-card"],
  ["run_refs[].id","source-support"],
  ["run_refs[].path","concept-card"],
  ["run_refs[].path","source-support"],
  ["run_refs[].revision","concept-card"],
  ["run_refs[].revision","source-support"]
]
~~~

### D. Cross-record creation time: 11

~~~json
[
  ["created_at","claim"],
  ["created_at","competency-question"],
  ["created_at","concept-card"],
  ["created_at","memory-admission"],
  ["created_at","preservation-decision"],
  ["created_at","reconciliation-result"],
  ["created_at","relationship-edge"],
  ["created_at","source-locator"],
  ["created_at","source-support"],
  ["created_at","validation-result"],
  ["created_at","verification-result"]
]
~~~

### E. Cross-record preparation and method references: 17

~~~json
[
  ["method_ref","concept-card"],
  ["method_ref","verification-result"],
  ["method_ref.id","concept-card"],
  ["method_ref.path","concept-card"],
  ["method_ref.revision","concept-card"],
  ["prepared_source_refs","claim"],
  ["prepared_source_refs","concept-card"],
  ["prepared_source_refs","source-support"],
  ["prepared_source_refs","verification-result"],
  ["prepared_source_refs[]","concept-card"],
  ["prepared_source_refs[]","source-support"],
  ["prepared_source_refs[].id","concept-card"],
  ["prepared_source_refs[].id","source-support"],
  ["prepared_source_refs[].path","concept-card"],
  ["prepared_source_refs[].path","source-support"],
  ["prepared_source_refs[].revision","concept-card"],
  ["prepared_source_refs[].revision","source-support"]
]
~~~

## Cross-Family Ownership Boundary

This proposal keeps the other 248 remaining pairs with their established
owners. In particular:

- evidence-grade and extraction-confidence fields remain Slice04 work;
- validation and verification states/results/references remain Slice05 work;
- reconciliation fields/references remain Slice06 work;
- preservation fields/references remain Slice07 work;
- admission, reliance and operator-authority fields remain Slice08 work;
- identity, locator, source-support, relationship and CQ meanings already
  accepted are not reassigned;
- Slice09-11 still own recomposition, research and requirements/P-15 handoff.

For competency questions, this proposal assigns only the remaining
`run_refs` and `created_at` pairs to the provenance sequence. CQ evidence,
confidence and lifecycle references stay with their semantic family owners.
CDC should confirm that boundary explicitly because `cdc-directive01.md`
names remaining CQ provenance interfaces without enumerating them.

## Options And Tradeoffs

1. **One 87-pair Slice17.** Minimizes handoffs but combines five semantic
   questions, mixed shapes and many record kinds. This recreates the oversized
   packet pattern the prior directive rejected and leaves poor review headroom.
2. **Five bounded units using Sets A-E.** Keep Slice17 for Set A, then use
   Slice18 through Slice21 for Sets B-E in that order. Each unit has one
   operational question, an exact pair boundary and room for native controls.
   It costs more handoffs but makes field-shape conflicts and cross-kind
   requiredness inspectable. Later units can reuse accepted evidence without
   inheriting meanings.
3. **Two or three broader units.** Combine A+B as extraction-run provenance
   and C-E as cross-record provenance, or combine D+E. This reduces handoffs,
   but creates 40- and 47-pair units or a 28-pair mixed time/reference unit.
   Those are larger than recent successful semantic packets and are likely to
   increase correction load.

CRC recommends Option 2 as the starting architecture. Recent Slice16 behavior
is encouraging: with the improved prompt-authoring guide, twelve contextual
pairs required one focused correction rather than the earlier multi-iteration
pattern. That is useful workload evidence, not proof that an 18-22 pair unit
will pass first time or a reason to lower review effort. The five-way split
retains semantic cohesion while leaving enough recovery space.

## Decisions Requested Of CDC

1. Approve, reject or revise the 87-pair provenance boundary and the exact
   primary ownership of each set. Confirm that the other 248 pairs remain with
   Slices04-11 as summarized above.
2. Approve, reject or revise the five-unit split and numbering. If approved,
   confirm Slice17=A, Slice18=B, Slice19=C, Slice20=D and Slice21=E, with each
   later unit still requiring fresh CRC readiness before opening.
3. Confirm the CQ boundary: `run_refs` and `created_at` are provenance work;
   evidence/confidence and lifecycle CQ references remain with Slices04-08.
4. State whether CRC may update the arc/project roadmap, assign Set A and issue
   its prompt after directive acknowledgement and fresh native/full-context
   author reconnaissance, or whether CDC requires another pre-opening return.
5. Preserve P-15: none of these units may adopt global reference requiredness,
   timestamp policy, actor inheritance, schema form or normative vocabulary.

## Hold And Return

Paused: creating or opening Slice17-21, assigning any of the 87 pairs, editing
source/schema/runtime/package/memory/UAT surfaces, or issuing a CC prompt. CRC
may perform read-only readiness work, but cannot treat the proposed grouping as
approved scope.

CDC owns the next design decision. The Operator should pass this exact path to
CDC:

`arc06-semantic-families-and-capability-requirements/crc-escalation02.md`

CDC returns the preserved arc-level `cdc-directive02.md` or records an explicit
unresolved/Operator gate. CRC then checks the directive against current state,
records acknowledgement in the arc Design Handoff History, applies only the
authorized amendments and issues a distinct CC prompt if permitted. Slice16's
acceptance and all earlier evidence remain unchanged unless new contradictory
evidence is surfaced explicitly.
