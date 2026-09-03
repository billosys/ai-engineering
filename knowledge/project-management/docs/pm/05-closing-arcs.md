# Part V — Closing an arc, and bubbling up to the project

An arc closes when its last slice is CDC-closed. Arc close is a formal step
with its own document, because the arc is the scale at which you check
**composition** — whether the slices actually added up to the capability the
arc promised — and that check has no other home. A pile of individually-closed
slices is not a closed arc until someone has confirmed they compose.

### The arc closing-report — `arcNN-<slug>/closing-report.md`

When the last slice closes, create the arc-level `closing-report.md` (distinct
from the per-slice closing-reports one level down). It carries:

1. **The capability, restated** from `arc-plan.md`, and the verdict: did the
   arc deliver it?
2. **The slice walk.** Each slice in the arc, with its outcome — delivered,
   deferred, or dropped — mirroring the per-row walk one scale up. The slice
   count here must match the slice breakdown in `arc-plan.md`; a missing slice
   is an arc-scale silent drop.
3. **The composition check.** Do the slices *recompose* into the capability?
   This is the silent-drop diff at arc scale: arc-capability-as-specified
   versus arc-capability-as-delivered. Name anything the arc promised that no
   slice delivered. Concretely, this is the arc `ledger.md` composition rows
   being *reproduced* (an end-to-end demonstration run at arc scale) and walked
   to closure — see
   [`LEDGER-DISCIPLINE.md`](../../../work-verification/templates/LEDGER-DISCIPLINE.md) Section B.
   The project-level equivalent (arcs recomposing into the DoD) lives in the
   project `ledger.md` and is described in Section C.
4. **The accumulated arc-plan change log.** A pointer to (or summary of) the
   changes that bubbled into `arc-plan.md` from slice closes during the arc —
   so the arc's drift from its original plan is visible in one place.
5. **Bubble-up to the project** (the next subsection).

### The arc bubble-up report and check

The bubble-up to the project answers, in the arc `closing-report.md`:

1. **Did this arc deliver its capability as `project-plan.md` defined it?**
   Against the project roadmap, not in the abstract.
2. **What did this arc reveal that the project plan did not anticipate?** A new
   arc the project now needs; a re-sequencing of remaining arcs; a scope
   correction at project level; a capability deferred to a later arc.
3. **The silent-drop diff at arc scale**, rolled up to the project: anything
   the roadmap expected from this arc that did not land.

The **check** is independent verification (CDC, or a fresh context, or the
operator) that the arc composes and the bubble-up is honest — the same
independence ledger verification requires, applied one scale up. And the
decision the check forces is the project-level analogue of the slice-close
step: **if the arc (or its accumulated arc-plan changes) implies a
project-plan change, `project-plan.md` must be updated before the next arc is
planned in detail** — using the plan-change discipline below, recording which
arc surfaced the change and why.

### The plan-change discipline (make-a-change + version-history)

Both the slice → arc update and the arc → project update use one discipline.
A plan is a living spec, not a fixed contract; when the work reveals the plan
was wrong or incomplete, the plan changes — but the change is **tracked, never
silent**. This is spec-keeping applied to the plan itself, and it is the same
discipline the methodology and this document apply to their own revisions.

To make a tracked plan change:

1. **Change the body, distinguishing expansion from overwrite.** A reader
   must be able to tell what was *added* from what was *replaced*, without
   diffing against an old version. Mark superseded text as superseded (strike
   it, or note "was: …") rather than deleting it silently. Silent replacement
   destroys the history that makes drift visible.
2. **Add a dated Version History entry** to the plan recording: *what*
   changed, *which child surfaced it* (the slice number for an arc-plan
   change; the arc number for a project-plan change), and *why*. The "which
   child" field is what makes the change auditable — it ties every plan
   revision back to the concrete work that justified it.
3. **Bump the plan's version marker** so the change is countable and the
   plan's age is legible.

A plan whose Version History stops growing while the work keeps revealing
surprises is not a stable plan — it is a plan that has stopped being
maintained, and "a substrate that rots is worse than no substrate." The
bubble-up checks exist precisely to keep that from happening quietly.

### Why this mirrors decomposition and recomposition

The top-down planning (project → arc → slice) is **decomposition**; the
bottom-up closing (slice → arc → project) is **recomposition** plus the
**feedback** that recomposition surfaces. The two directions are the same
structure traversed opposite ways, and running both is what makes the plan a
closed loop rather than a one-way fiction. A project that only decomposes —
plans downward and never rolls up — cannot see whether its parts add back up
to the whole, which is exactly the historic failure this framework was built
to kill. (The `odm` tool mechanizes this loop directly: its `part_of` tree is
the decomposition, and its rollup / recomposition checks are the bubble-up.
This document is the discipline; `odm` is that discipline enforced by a tool.)

---
