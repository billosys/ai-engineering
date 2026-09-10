# Progress decision and required guidance

Date: 2026-09-10. Authority: operator correction during review of Q-03.
Status: hierarchical project/arc model accepted; detailed contract revision
and CDC verification remain outstanding. This supersedes draft 1's choice of
one flattened descendant-slice ratio as the project progress measure.

## Accepted project and arc calculation

Each planned arc has equal weight in the project's current roadmap by default.
Let p_i be an arc's progress as a fraction from zero to one and N the number
of arcs in that roadmap:

```text
project_progress = (p_1 + p_2 + ... + p_N) / N
```

An arc's slice-delivery fraction supplies its intermediate progress where the
slice inventory and assessments support that calculation. Thus the unit at
each level matters: a project aggregates arcs; an arc aggregates slices.
Do not flatten all slices across projects/arcs to obtain the headline project
percentage. Leaf counts can still be useful separately labeled statistics.

Four-arc examples supplied by the operator:

| Arc progress values | Project calculation | Project progress |
| --- | --- | --- |
| 1, 0, 0, 0 | (1 + 0 + 0 + 0) / 4 | 25% |
| 0.5, 0, 0, 0 | (0.5 + 0 + 0 + 0) / 4 | 12.5% |

An explicitly not-started planned arc contributes zero even if its slices are
not defined yet. Its presence in the roadmap gives it a weight now. Missing
slice decomposition is not the same as unknown arc progress: the former is
normal just-in-time planning; the latter cannot silently be assigned zero.

One arc does not become heavier than its peers merely because it has more
slices. Decomposing a later, not-started arc into slices must not change the
project percentage solely by expanding a global leaf denominator. Changes to
the actual arc roadmap or assessed progress can legitimately change the
percentage and must remain visible in the planning history.

This is an equal-weight structural progress measure, not a time/effort estimate.
It does not make independently verified closure or operator acceptance a
calculated state. Preserve Q-02's separate axes and the evidence behind arc
progress. A displayed percentage cannot close a ledger or discharge R-01.

## Coverage guidance required in the shipped skill

The operator explicitly requires this explanation and table in the
project-management SKILL.md or a routed guide. Prefer a focused guide linked
from the entrypoint/wayfinder, shipped in both skill packages. The table must
adapt its counted unit to the displayed level: arcs for an ordinary project,
slices for an arc. Do not bury it only in this planning artifact or JSON schema.

| Coverage | Meaning | Example presentation |
| --- | --- | --- |
| Complete | Every current unit in the stated population is represented | All four planned arcs contribute to the project calculation |
| Partial | Records deliberately cover only a subset | Progress for the three recorded arcs; project inventory incomplete |
| Unknown | We cannot establish whether the inventory is exhaustive | Known progress shown; overall project progress unavailable |

Document these adjacent distinctions in plain language with worked examples:

- Inventory completeness and known progress are separate. All four arc IDs
  can be known while one arc's progress is unassessed.
- An explicitly not-started arc is known zero. An unassessed arc is unknown.
- A complete current roadmap need not have every later arc decomposed into
  slices. Current completeness does not claim that no new arc will emerge.
- A partial-population fraction must name its subset; it is not an exhaustive
  project percentage. Unknown values must not be treated as zero or omitted
  from the denominator to inflate the remainder.
- No current children, unknown children, and not-yet-decomposed work are
  different situations. An empty slice array is not evidence of completion.
- Explain computed versus source-reported progress, evidence dates, and any
  inability to reconcile reports with detail. Rendering cannot refresh evidence.
- Separate delivery, verification and acceptance. Each percentage needs a
  label that tells the reader which progress predicate it actually uses.

## Bounded contract revision for CC

Revise the existing status contract/cases, preserving the draft-1 review as
history. Q-01, Q-02, Q-04, Q-05 and Q-06 recommendations were already accepted;
Q-03 now has this corrected design direction. R-01 remains an independent
required correction. Do not reopen settled decisions or implement source code.

Resolve the following detailed consequences in the revision, distinguishing
mechanical consequences from any new policy proposal needing review:

1. Define child weighting and the source of an arc's fraction, including
   explicit not-started/delivered assessments before or without child detail.
   Reconcile any disagreement between reported arc progress and known slices.
2. Specify partial/unknown propagation and the guards for empty populations.
   Keep denominator ownership and coverage explicit at each aggregation level.
3. Cover direct-slice projects and mixed arc/direct-slice projects without
   manufactured wrappers. The operator's four-arc example does not silently
   settle how unequal kinds should share weight in a mixed project; propose
   and document that policy. Similarly make any Saga project aggregation rule
   explicit, without introducing repository closure/acceptance semantics.
4. Revise the blanket prohibition on project percentages and slice-only
   Progress semantics. Display 12.5% faithfully; draft-1 whole-percent rounding
   cannot represent the operator's example. Define display precision separately
   from calculation precision and never use rounded values in parent roll-ups.
5. Retain all original acceptance cases, amending their expected results with
   rationale where flattening no longer applies. Add cases for both four-arc
   examples, differing slice counts per arc, later decomposition preserving
   project weight, unknown versus known-zero arcs, roadmap changes and rounding.
6. Include the coverage table and worked explanation in the implementation
   handoff as a required shipped-guide deliverable, with source/package checks.

The existing C-01 (one arc with one delivered slice, plus one direct slice in
progress) no longer suffices as the only numerical example. Its mixed-child
weighting needs the explicit policy above; add an ordinary multi-arc example.

## Version history

- 2026-09-10 v1.0: Recorded the operator's hierarchical progress correction and
  explicit requirement to ship coverage guidance. No source implementation or
  completed contract revision is claimed by this decision record.
