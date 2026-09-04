# Part IX — A worked example: project-management flow

The mechanics in the project-management guide are easier to apply against a
real run. This is a historical snapshot from a rebuild project, not
documentation for the tool that project produced and not a current status report
for that project. Tool names below appear only where they identify the concrete
artifacts from the run; the lesson is the general project-management flow:
project roadmap, arc decomposition, slice close, bubble-up, and recomposition.

**Project level.** At the point captured here, after research (ODD-0011,
ODD-0014, ODD-0016) and a design doc (ODD-0013), the roadmap was six arcs in
dependency order: A1 substrate & node CRUD → A2 graph/gates/derived order → A3
rollup & orient → A4 index & cache → A5 reconciliation → A6 migrate +
self-host. The MVP boundary (A1–A3) and the explicit non-goals were the
project's definition of done. That roadmap is what a `project-plan.md` carries:
the arcs, each capability, the dependencies, and the current status.

**Arc level.** Arc 02's capability was a graph-oriented capability: build the
edges, cycle checks, gates, derived order, and commands needed to exercise the
graph end to end. Its `arc-plan.md` broke that into slices 01–07, in order,
each load-bearing for the next: detect a missing edge (02), evaluate status and
gates (03), persist typed edges (04), compute derived order (05), update the
check path (06), and then add the mutators (07) that let the capability be
demonstrated end to end.

**Slice close and bubble-up.** Slice 07 closed its ledger — but its
`cdc-verification.md` surfaced a real finding: one command accepted a rationale
from the operator and then dropped that rationale when persisting the change,
because the stored edge format had no rationale slot. That is exactly a
slice-close bubble-up: the slice delivered its assigned piece, *and*
implementing it revealed something the arc-plan had not anticipated. The
arc-plan was updated to add a follow-up, and — because the fix was a clean unit
of its own — it was routed not as "slice 07.1" (which would have been the
bisection anti-pattern the project exists to kill) but as a new slice in the
next arc. The "which slice surfaced it" field in the change log pointed back at
slice 07.

**Arc close and bubble-up.** Arc 02 closed when slice 07 was CDC-verified. The
composition check confirmed the slices added up to "a graph can be built and
advanced end-to-end through the CLI alone" — the capability the arc promised.
The bubble-up to the project confirmed that, at that point, the MVP roadmap
still held (A1–A3 unchanged) and carried the tear-rationale follow-up forward
into Arc 03's plan as its first slice. No project-plan change was forced,
because the arc delivered its capability as the roadmap defined it — which is
itself a valid, recorded bubble-up outcome, not a skipped step.

The lesson the example carries: every one of those findings was caught because
a close was also a bubble-up, and an independent context ran the check.
Without the bubble-up, the dropped tear-rationale would have been a silent gap
in an arc that *looked* closed — precisely the class of error that compounds.

---
