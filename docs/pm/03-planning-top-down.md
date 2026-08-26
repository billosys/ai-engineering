# Part III — Planning, top-down

Planning runs from the project down to the slice. Each level produces one
plan-of-record and sets the context the level below plans against. The three
levels map onto SDLC steps 2–5.

### The project plan — `project-plan.md`

After research (SDLC step 1), project definition (step 2), and the design doc
(step 3) have established *what* is being built and *how the pieces fit*,
`project-plan.md` is the bridge into execution. It is the arc roadmap: the
ordered list of arcs, the capability each one delivers, and the dependencies
between them. It is the document a fresh session reads to understand **all the
arcs at once**, before opening any single `arc-plan.md`.

`project-plan.md` carries, at minimum:

1. **Definition of done and boundaries.** What the project delivers, and what
   it explicitly does not. A pointer to the design doc for the architecture;
   this file is the plan, not the design.
2. **The arc roadmap.** The arcs in dependency order, each with a one-line
   capability statement and its dependencies on earlier arcs. This is the
   project's decomposition — the `project → arc` edge made explicit.
3. **Current status.** Which arc is active, which are closed, which are not
   yet planned in detail. Detailed arc planning is deliberately deferred until
   an arc is near — see *plan late, plan deep* below.
4. **A project-ledger section.** The composition criteria that verify the DoD,
   stated up front as ledger rows — the project ledger from
   [`LEDGER-DISCIPLINE.md`](../../templates/LEDGER-DISCIPLINE.md)
   Section C. It opens here and closes (per-row walk) in the project's
   `closing-report.md`. This is what makes the DoD *checkable* rather than
   merely asserted.
5. **A Version History section.** The change log that receives bubble-ups from
   arc closes (see [`Closing arcs`](./05-closing-arcs.md)). It starts with the initial roadmap as v1.0 and grows
   one dated entry per change, each naming which arc surfaced the change and
   why (the [plan-change discipline](./05-closing-arcs.md#the-plan-change-discipline-make-a-change--version-history)).

`project-plan.md` is **not** a mega-file holding every arc's and slice's
detail — that is the anti-pattern in
[`Anti-patterns to refuse`](./07-anti-patterns.md). It holds the roadmap and the
change log; the detail lives in the per-arc and per-slice documents below it.

### The arc plan — `arc-plan.md`

When an arc becomes the active work, it is planned in detail (SDLC step 4:
arc-and-slice breakdown). `arc-plan.md` carries, at minimum:

1. **The capability statement.** The one coherent thing this arc delivers —
   the same line that appears in the project roadmap, expanded into a
   paragraph. This is what the arc's slices must *compose* into.
2. **The slice breakdown.** The slices in order, each with a one-line scope
   and which earlier slices (or arcs) it is load-bearing for. This is the
   `arc → slice` decomposition made explicit. Apply the sizing judgment
   (see [`The scales of work`](./01-scales-of-work.md)) here: each entry must be a body of work that fits one context with
   iteration headroom.
3. **Dependencies.** What this arc consumes from earlier arcs, and what it
   leaves for later ones.
4. **An arc-ledger section.** The composition criteria that verify the
   capability, stated up front as ledger rows — the arc ledger from
   [`LEDGER-DISCIPLINE.md`](../../templates/LEDGER-DISCIPLINE.md)
   Section B. It opens here and closes (per-row walk) in the arc's
   `closing-report.md`. This is what makes "the slices compose into the
   capability" *checkable* rather than merely asserted.
5. **A Version History section.** The change log that receives bubble-ups from
   slice closes (see [`Closing slices`](./04-closing-slices.md)) — one dated entry per change, each naming which
   slice surfaced it and why.

### The per-slice open set

When a slice becomes the next work, write its open set — `slice-plan.md`,
`ledger.md`, `cc-prompt.md` — fully, before CC starts. The `slice-plan.md`
states the goal, the in/out scope, the verification approach, and the exit
criteria; the `ledger.md` turns the exit criteria into grep-verifiable rows;
the `cc-prompt.md` is the assignment CC receives. The ledger is the contract:
its rows are what "done" means for this slice, and every row must reach a
final status before the slice advances.

### Plan late, plan deep

Plan each level in detail only when it is near. Write the full project roadmap
up front, but do not write every arc-plan on day one; write an arc's plan when
that arc is the active or next work, and write a slice's open set when that
slice is next. The reason is the same reason the bubble-up machinery exists:
**earlier work changes the plan for later work**, and detailed plans written
too far ahead are written against assumptions the earlier work will
invalidate. A project roadmap is cheap to keep current; ten detailed
arc-plans written in advance are ten documents that will silently rot. Plan
the shape early; plan the detail late.

---
