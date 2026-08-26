# Part IX — A worked example: the `odm` rebuild

The abstractions above are easier to apply against a real run. `odm` — a
markdown/git-native planning substrate — was rebuilt under exactly this
process, and it is a useful exemplar because the project's *subject* is the
mechanization of this very document, so the structure is unusually visible.

**Project level.** After research (ODD-0011, ODD-0014, ODD-0016) and a design
doc (ODD-0013), the roadmap was six arcs in dependency order: A1 substrate &
node CRUD → A2 graph/gates/derived order → A3 rollup & orient → A4 index &
cache → A5 reconciliation → A6 migrate + self-host. The MVP boundary (A1–A3)
and the explicit non-goals were the project's definition of done. That roadmap
is what a `project-plan.md` carries: the arcs, each capability, the
dependencies, and the current status.

**Arc level.** Arc 02's capability was "build the graph engine: edges, cycles,
gates, derived order, and the CLI mutators to drive it." Its `arc-plan.md`
broke that into slices 01–07, in order, each load-bearing for the next: tear
detection (02) before status/gates (03) before the typed-edge frontmatter (04)
before derived order (05) before `check` v2 (06) before the CLI mutators (07)
that let a graph be built end-to-end.

**Slice close and bubble-up.** Slice 07 (CLI graph-mutators) closed its ledger
— but its `cdc-verification.md` surfaced a real finding: `odm tear --because`
validated the rationale and then *dropped it on persist*, because the `tears`
frontmatter field had no rationale slot. That is exactly a slice-close
bubble-up: the slice delivered its assigned piece, *and* implementing it
revealed something the arc-plan had not anticipated. The arc-plan was updated
to add a follow-up, and — because the fix was a clean unit of its own — it was
routed not as "slice 07.1" (which would have been the bisection anti-pattern
the project exists to kill) but as a new slice in the next arc. The "which
slice surfaced it" field in the change log pointed back at slice 07.

**Arc close and bubble-up.** Arc 02 closed when slice 07 was CDC-verified. The
composition check confirmed the slices added up to "a graph can be built and
advanced end-to-end through the CLI alone" — the capability the arc promised.
The bubble-up to the project confirmed the MVP roadmap still held (A1–A3
unchanged) and carried the tear-rationale follow-up forward into Arc 03's plan
as its first slice. No project-plan change was forced, because the arc
delivered its capability as the roadmap defined it — which is itself a valid,
recorded bubble-up outcome, not a skipped step.

The lesson the example carries: every one of those findings was caught because
a close was also a bubble-up, and an independent context ran the check.
Without the bubble-up, the dropped tear-rationale would have been a silent gap
in an arc that *looked* closed — precisely the class of error that compounds.

---
