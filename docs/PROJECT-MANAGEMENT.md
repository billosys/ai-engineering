# Project Management — how the work is planned, tracked, and closed

> The operational home for the framework's project-management layer: the
> scales of work, the planning artifacts and where they live on disk, the
> protocol that stops a session inventing its own folders, and — the part
> that is new in v2.0 — the **top-down planning** and **bottom-up
> reporting** machinery that keeps a plan honest as the work reveals what
> the plan could not have known.
>
> This document is deliberately concrete. The companion
> [methodology](./AI-ENGINEERING-METHODOLOGY.md) names the *philosophy* —
> the three pillars, the 9-point SDLC, the anti-degradation disciplines.
> This document is where that philosophy becomes a set of files you create,
> reports you write, and checks you run, in an order you can follow without
> re-deriving it. When an instance of this framework has gone off the rails
> on a planning task, it has almost always been because it read the
> philosophy and improvised the mechanics. **Do not improvise the
> mechanics. They are written down here.**

## How to read this document

If you are about to **plan or close anything** — a project, an arc, or a
slice — you are required to read this document first, in full. The
[`collaboration-framework` skill](../SKILL.md) routes you here the moment
planning begins, and it says *MUST*, not *should*. The reason is empirical:
the abstract structure is easy to nod along to and easy to get subtly wrong,
and a subtly-wrong plan structure compounds silently across sessions exactly
the way a subtly-wrong design does.

The document has three movements:

1. **The units and the layout** (Parts I–II) — what the scales of work are,
   and where every planning artifact lives on disk. This is the *vocabulary*
   and the *filesystem*.
2. **Planning, top-down** (Part III) — how a project becomes arcs becomes
   slices, and the artifact each step produces: `project-plan.md`,
   `arc-plan.md`, the per-slice open set.
3. **Reporting and closing, bottom-up** (Parts IV–V) — how a slice closes
   and bubbles up to its arc, how an arc closes and bubbles up to the
   project, and the change-tracking discipline that records what each level
   learned and propagated upward. This is the machinery that makes the plan
   a living document rather than a fiction that drifts out of date.

Parts VI–VIII carry the confirmation protocol, the anti-patterns to refuse,
and the maintenance rules. Part IX is a worked example — the `odm` rebuild —
grounding every abstraction in a real run.

---

## Notes for Codex

For Codex, read every "Claude session" below as any fresh Codex Desktop,
Codex CLI, or other LLM session entering the project without the full prior
context. **CC** is Codex CLI in the IC implementation role; **CDC** is Codex
Desktop in the planning/review/QA role. Keep the canonical filenames
(`project-plan.md`, `arc-plan.md`, `slice-doc.md`, `ledger.md`,
`cc-prompt.md`, `closing-report.md`, `cdc-verification.md`) unless the
operator explicitly changes the project convention — renaming them inside one
project recreates the parallel-convention drift this document exists to
prevent.

This document guides planning craft and the quality floor; it does not
override Codex's standing system, developer, tool, safety, sandbox, or user
instructions. If a conflict appears, name the tension and follow the
governing instruction stack rather than forcing the methodology to fit.

---

## Part I — The scales of work

Every project decomposes along three scales. The names are constant across
every project, team, and session, because the failure mode this section
exists to kill is re-inventing the vocabulary each time — so that the same
idea is a "phase" in one project, a "chunk" in the next, and a "milestone" in
a third. Constant names are what let a plan written for one project be picked
up and read, without translation, by anyone starting the next.

The three scales, largest to smallest:

**Project.** The whole effort — the thing with a name, a goal, and a
definition of done. A project is approached through the first three SDLC
steps: research, project definition, design doc. Its output is not code but
boundaries and architecture: what we are building, what we are explicitly
not, and how the pieces fit. A project is planned by breaking it into arcs,
and that plan-of-record lives in **`project-plan.md`** (Part III).

**Arc.** A set of related slices with a beginning and an end — the body of
work that delivers one coherent capability. An arc is the unit at which you
check that the slices *compose*: that together they add up to the capability
and that none is missing. It is approached through arc-and-slice breakdown
(SDLC step 4): decide which slices the arc needs, what order they land in,
and which are load-bearing for which. An arc is too big to hold in one branch
or one context — it is a planning unit, not an execution unit. Its
plan-of-record lives in **`arc-plan.md`** (Part III).

**Slice.** The unit of execution — the work that lands in a single branch as
one mergeable diff. A slice does one thing, end to end, and is sized to be
*held in a single model context with headroom to spare* — research,
implementation, tests, and self-review all carried without compaction, plus
slack for the fix-iterations the review process will surface. The slice is
where ledger discipline attaches — one slice, one ledger — and where the work
actually gets written, tested, and reviewed. If a slice will not fit in one
context, it was two slices.

Two more words name things *inside* a slice, not scales of their own:

**Step.** A single item in a slice's implementation plan — the fine-grained
unit of work, and what the ledger's rows verify. Steps are how a slice is
planned and tracked; they do not cross slice boundaries.

**Iteration.** A refinement pass on a slice whose delivery does not yet meet
its acceptance criteria. The word is reserved for this and only this — the
fix loop on an in-progress slice, never a unit of planning. The budget is
five iterations per slice (see [ledger
discipline](../templates/LEDGER-DISCIPLINE.md)); needing more is a signal the
slice was too large or under-specified, not a licence to keep grinding.

Read together: *a project bends through several arcs; each arc is cut into
slices; a slice is planned as a handful of steps, and if its delivery misses
spec it is refined over a bounded number of iterations.*

For collaborators arriving with Agile or Scrum habits, the rough translation
is: project ≈ epic, arc ≈ feature, slice ≈ the branch-scale unit those
frameworks never named cleanly. The translation is a courtesy for onboarding,
not an adoption of those frameworks.

### The fundamental unit, and what it rests on

Every project-management system has an atom — the smallest chunk it plans,
reviews, and merges as a whole. What that atom *rests on* is the quiet
assumption that shapes everything above it.

Agile's atom — the story, realised as a branch or PR — is calibrated to
**human cognition**: small enough that one reviewer can hold the change in
working memory and find its bugs in a single sitting. The familiar "keep a PR
under ~500 lines" heuristic is a proxy for *human review attention*, not a
property of the work itself. The unit is sized to the reviewer.

Our atom — the slice — is calibrated to a different bottleneck: the **model's
context window, minus the headroom the work needs to recover from its own
mistakes**. A slice is well-sized when a single context can carry it end to
end — read the substrate, plan the steps, write the code, run the tests,
review itself — *without compaction*, and still leave room for the
fix-iterations the ledger and the review process will surface. The binding
constraint is **coherence held in one context**, not reviewer fatigue.

Two consequences follow. First, a slice can be *larger in raw diff* than an
Agile PR and still be correctly sized: a coherent end-to-end capability that
would span several "stories" can be one slice, because the limit is
coherence-in-context, not lines-a-human-will-read. (We keep the ~500-line
figure only as a translation courtesy.) Second, the headroom is not optional
slack: the five-iteration budget *lives inside* the context budget. A slice
sized to fill the whole window leaves nowhere to stand when delivery misses
spec — which is exactly when the context is most needed. Size to the
comfortable two-thirds, not the ceiling.

### Sizing is a judgment call

Where an arc ends and its slices begin is **a judgment call, not a formula**
— a piece of back-of-napkin token arithmetic against the context budget, made
fresh for each arc. The tension to balance is real: arcs are sized to land a
*coherent capability* (the thing worth shipping together), while slices are
sized to *fit one context with iteration headroom* (the thing one execution
pass can hold). The two pulls do not always agree, and resolving them is part
of the design work, not a step that can be mechanised.

The test is simple to state and requires estimation to apply: *does this body
of work fit one context, with room to recover?* If yes, it is a slice — and
if you were about to call it an arc, it was a slice all along. If no, it is an
arc, and the work of arc-and-slice breakdown is to cut it into slices that
each pass the test. The estimation is rough and will sometimes be wrong; that
is what the five-iteration budget and the "if it won't fit, it was two
slices" rule are for — they catch a mis-sized slice at execution time and
force the split.

A useful mnemonic comes from screenwriting, whose structure nests the same
way: **Act → Sequence → Scene → Beat**, each tier a self-contained unit that
advances the one above. **Project → Arc → Slice → Step** is the same shape —
which is why the breakdown *feels* like outlining a story rather than filling
a spreadsheet. (Above the Project sits, in principle, a *Saga* — a
multi-version vision spanning several Projects. We name it only to mark the
slot; we do not currently plan or track at that scale, so it carries no
operational weight here.)

---

## Part II — The canonical layout

In the absence of a project's own stated convention, lay the work out so the
structure is legible from the filesystem alone. This is the canonical layout.
It is the single source of truth for where planning artifacts live; the
[methodology](./AI-ENGINEERING-METHODOLOGY.md) used to carry an abridged copy
and now points here.

```
docs/design-vX.Y.Z/
  project-plan.md               ← the project's plan-of-record (the arc roadmap)
  arcNN-<slug>/
    arc-plan.md                 ← the arc's plan-of-record (the slice breakdown)
    closing-report.md           ← arc-level close + bubble-up, written at arc close
    sliceNN-<slug>/
      slice-doc.md              ← plan-of-record for this slice
      ledger.md                 ← grep-verifiable acceptance criteria (the steps)
      cc-prompt.md              ← the assignment the executing context receives
      closing-report.md         ← per-row walk + bubble-up, written at slice close
      cdc-verification.md       ← independent re-run + check, written at slice close
```

Three tiers of plan-of-record, one per scale: **`project-plan.md`** for the
project, **`arc-plan.md`** for each arc, and **`slice-doc.md`** for each
slice. Two tiers of closing-report: one per **slice** (the per-row walk) and
one per **arc** (the composition check). The per-slice `cdc-verification.md`
is the independent re-run that gates a slice closed. Their full roles are
defined in Parts III–V; their on-disk shape is fixed here.

Each scale is also **verified by a ledger** — the recomposition discipline in
[`../templates/LEDGER-DISCIPLINE.md`](../templates/LEDGER-DISCIPLINE.md). The
slice ledger is its own file (`ledger.md`); the **arc and project ledgers are
not separate files** — they open as a ledger *section* inside `arc-plan.md` /
`project-plan.md` (next to the capability / definition of done they verify) and
close as the per-row walk inside the matching `closing-report.md`. That doc owns
the ledger mechanics at all three scales; this one owns where the rows live.

### Naming rules

- **`X.Y.Z` is the project's design-doc version**, not its release version.
  Bumps mean "the design moved," not "we cut a release."
- **`NN` is two digits, zero-padded** (`arc01`, `slice03`) — sorts cleanly,
  reads consistently, and survives projects that grow past nine arcs.
- **`<slug>` is short, kebab-case, and descriptive in isolation** —
  `arc01-substrate`, not `arc01-thing`. Read aloud, the path should tell a
  reader what is in that directory without opening it.
- **When a body of work is one slice, not an arc**, skip the arc wrapper: the
  five per-slice documents live directly in one `NN-<slug>/` directory under
  `docs/design-vX.Y.Z/`, with no `arc-plan.md` or arc-level
  `closing-report.md` above them. That collapse is not a third case to
  choose; it is what you discover when the sizing judgment comes back "one
  slice, not an arc." A project that is genuinely a single slice may also skip
  `project-plan.md` — but the moment a second arc is conceivable, write it.

### The five per-slice documents

The five documents under each `sliceNN-<slug>/` are the artifact set that
attaches to one execution unit. They split into an **open set** (written when
the slice is planned, before any code) and a **close set** (written when the
slice finishes):

| Document | Set | Role |
|----------|-----|------|
| `slice-doc.md` | open | Plan-of-record: goal, scope (in/out), verification approach, exit criteria. |
| `ledger.md` | open | The acceptance criteria as grep-verifiable rows — the steps. Format and discipline in [`LEDGER-DISCIPLINE.md`](../templates/LEDGER-DISCIPLINE.md). |
| `cc-prompt.md` | open | The assignment the implementing context (CC) receives. |
| `closing-report.md` | close | The per-row walk written at slice close, plus the **bubble-up to the arc** (Part IV). |
| `cdc-verification.md` | close | The independent re-run that verifies the closing report against evidence, plus the **bubble-up check** (Part IV). |

Opening the close-set documents at slice start, or leaving the open-set
documents unfinished when handing off to CC, are both spec-keeping failures.
Write the open set fully before CC starts; write the close set only once
there is something to close.

---

## Part III — Planning, top-down

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
   [`../templates/LEDGER-DISCIPLINE.md`](../templates/LEDGER-DISCIPLINE.md)
   Section C. It opens here and closes (per-row walk) in the project's
   `closing-report.md`. This is what makes the DoD *checkable* rather than
   merely asserted.
5. **A Version History section.** The change log that receives bubble-ups from
   arc closes (Part V). It starts with the initial roadmap as v1.0 and grows
   one dated entry per change, each naming which arc surfaced the change and
   why (the plan-change discipline, Part V).

`project-plan.md` is **not** a mega-file holding every arc's and slice's
detail — that is the anti-pattern in Part VII. It holds the roadmap and the
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
   (Part I) here: each entry must be a body of work that fits one context with
   iteration headroom.
3. **Dependencies.** What this arc consumes from earlier arcs, and what it
   leaves for later ones.
4. **An arc-ledger section.** The composition criteria that verify the
   capability, stated up front as ledger rows — the arc ledger from
   [`../templates/LEDGER-DISCIPLINE.md`](../templates/LEDGER-DISCIPLINE.md)
   Section B. It opens here and closes (per-row walk) in the arc's
   `closing-report.md`. This is what makes "the slices compose into the
   capability" *checkable* rather than merely asserted.
5. **A Version History section.** The change log that receives bubble-ups from
   slice closes (Part IV) — one dated entry per change, each naming which
   slice surfaced it and why.

### The per-slice open set

When a slice becomes the next work, write its open set — `slice-doc.md`,
`ledger.md`, `cc-prompt.md` — fully, before CC starts. The `slice-doc.md`
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

## Part IV — Closing a slice, and bubbling up to the arc

A slice is not done when the code is written. It is done when its ledger is
closed *and* its outcome has been rolled up to the arc — because a slice that
delivered its diff but silently invalidated the arc's plan has not finished
its job; it has deferred a problem to whoever plans the next slice.

Two documents close a slice: `closing-report.md` (written by CC, the
implementer) and `cdc-verification.md` (written by CDC, the independent
reviewer). The ledger-row mechanics of both are defined in
[`LEDGER-DISCIPLINE.md`](../templates/LEDGER-DISCIPLINE.md). This section adds
the two things that make a close also a *bubble-up*.

### The slice closing-report — `closing-report.md`

CC writes the per-row walk: for every ledger row, the final status (`done` /
`deferred` / `no-op`) and the evidence, with no silent drops (the row count at
close must match the row count at open). Then CC adds a final section,
**Bubble-up to the arc**, answering three questions:

1. **Did this slice deliver the piece of the arc's capability the arc-plan
   assigned it?** State it against the arc-plan's slice breakdown, not in the
   abstract.
2. **What did implementing this slice reveal that the arc-plan did not
   anticipate?** A new slice the arc now needs; a re-sequencing; a scope
   correction; a discovered dependency; an item deferred to a later slice.
   This is the slice → arc feedback that keeps the arc-plan honest.
3. **The silent-drop diff at slice scale.** Scope-as-specified versus
   scope-as-delivered. Anything missing is disclosed, deferred-with-rationale,
   or a silent drop — and the third is the failure mode the whole discipline
   exists to eliminate.

### The slice bubble-up check — in `cdc-verification.md`

CDC verifies the closing report against evidence — re-running the reproducible
ledger rows, checking deferrals and no-ops — exactly as ledger discipline
requires. Then CDC verifies the **bubble-up** itself:

- Confirm the slice delivered its assigned piece, against the arc-plan.
- Confirm the silent-drop diff is complete and honest.
- **Decide whether the slice's findings require an arc-plan change.** If the
  slice surfaced anything in answer (2) above that changes the arc's slice
  breakdown, sequencing, or scope, then `arc-plan.md` **must be updated before
  the next slice is planned against it** — using the plan-change discipline
  (Part V). A stale arc-plan that the next slice plans against is how a small
  discovery in one slice becomes a structural error three slices later.

The bubble-up lives in the existing two close-set documents — a named section
in each — rather than in new files. Do not create a separate per-slice
bubble-up file; that is file proliferation, and it splits the close across
more documents than the slice needs.

### The slice-close arc-plan-update step (explicit)

To state the new required step plainly, because it is the one most easily
skipped: **at every slice close, after the closing-report and before planning
the next slice, ask: did implementing this slice uncover anything that should
change `arc-plan.md`?** If yes, update `arc-plan.md` now — make the change in
the body, and record it in that file's Version History with (a) what changed,
(b) which slice surfaced it, and (c) why. If no, that is a valid answer, but
it is an answer you arrive at by asking, not by skipping the question.

---

## Part V — Closing an arc, and bubbling up to the project

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
   slice delivered. Concretely, this is the arc ledger's composition rows being
   *reproduced* (an end-to-end demonstration run at arc scale) and walked to
   closure — see [`../templates/LEDGER-DISCIPLINE.md`](../templates/LEDGER-DISCIPLINE.md)
   Section B. The project-level equivalent (arcs recomposing into the DoD) is
   Section C.
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

## Part VI — The confirmation protocol

The layout in Part II is the *default*. The operator owns the actual layout
for their project. This protocol is the discipline that connects the two: the
executing context **confirms before adopting a layout and never invents one
mid-stream.** Apply it before creating any planning directory or filename.

### When the protocol triggers

At any of these moments, **stop and confirm with the operator before creating
directories or filenames**:

- Starting a new project that does not yet have a layout.
- Beginning the first arc or slice of a project where the layout was set up by
  prior work but is not obviously visible from an `ls`.
- Opening any artifact category not yet present in the repository and not
  covered by this document.
- Resuming a project after long elapse, where the layout you remember may no
  longer match the layout on disk.

### How to confirm

A short, specific question with a concrete proposal — *not* an open-ended
"what would you like?", which throws the work back to the operator. Quote the
default verbatim, name where it comes from, and offer the choice to accept,
adjust, or override:

> I'm about to create the slice artifact set for slice 1 of arc 1. The default
> layout from `docs/PROJECT-MANAGEMENT.md` is:
>
> ```
> docs/design-v0.1.0/
>   project-plan.md
>   arc01-<slug>/
>     arc-plan.md
>     slice01-<slug>/
>       slice-doc.md
>       ledger.md
>       cc-prompt.md
>       closing-report.md
>       cdc-verification.md
> ```
>
> The `<slug>`s I'd use are `<arc-slug>` and `<slice-slug>`. Want me to proceed
> with that, or adjust the layout / slugs?

That is it. The default is named, the substitutions are named, and the
operator's three options (proceed / adjust / override) are explicit.

For asset categories **not** covered by this document — project-scoped prompts
that outlive a slice, upstream contribution drafts, scratch notes — the same
protocol applies, but **without a default to quote**: name the category,
propose what you would otherwise have chosen on autopilot, and let the
operator pick.

### What to do after the operator answers

- **"Proceed"** — record the chosen layout in the project's `CLAUDE.md` (or
  equivalent local instruction file) so the next session does not re-confirm.
  One line is enough: *"Planning artifacts live under
  `docs/design-vX.Y.Z/…`, per `docs/PROJECT-MANAGEMENT.md`."* If no `CLAUDE.md`
  exists, raise it as a follow-up — but do **not** silently start scattering
  files.
- **"Adjust"** — apply the adjustment, then record the adjusted layout in the
  project's `CLAUDE.md`. If the adjustment diverges meaningfully from the
  default, briefly say *why* (team convention, prior tool output, a fork in
  scale) — spec-keeping for the layout itself.
- **"Override entirely"** — adopt the operator's layout verbatim, record it the
  same way, and add a one-line note that this project does not use the default.

### What this protocol prevents

It prevents the one failure mode this part exists to address: the next session
arriving and *inventing*. Once the protocol has been applied once per project,
the layout is written where the next session will see it, and no inventing is
necessary — or permitted.

---

## Part VII — Anti-patterns to refuse

The following layouts and habits are recognisable enough that a session should
refuse to adopt them on autopilot and propose the canonical structure instead,
via the confirmation protocol. If one is *already present* from earlier work,
name the dissonance to the operator before adopting or migrating it — silent
migration of an in-flight project's layout is its own failure mode.

- **`tasks/`, `work/`, `progress/`, or `reports/` at the project root.** The
  most common inventions; they conflict with the `project → arc → slice`
  vocabulary and route artifacts away from the scale they belong to.
- **`milestones/` for ledgers.** The level-1 ledger-bearing unit is **slice**,
  not milestone; the ledger lives inside the slice directory as `ledger.md`,
  not under a top-level `milestones/` tree.
- **A mega-file `PLAN.md` at the project root holding every arc, slice, and
  ledger.** The artifact set is per-scale for a reason: each document is a
  coherent unit that can be independently verified, closed, and re-read.
  Merging them across scales prevents all three. `project-plan.md` holds the
  *roadmap*, not the detail.
- **Per-author or per-session subdirectories** (`claude-a/`,
  `session-2026-06-18/`). The artifact is owned by the slice or arc it belongs
  to, not by who or when wrote it. Authorship belongs in the file header, not
  the path.
- **Closing a slice without bubbling up.** A `closing-report.md` with a per-row
  walk but no *Bubble-up to the arc* section is a half-closed slice — it
  verified the diff and skipped the question of what the diff did to the plan.
- **Closing an arc by fiat.** Declaring an arc done because its last slice
  merged, with no arc-level `closing-report.md` and no composition check, skips
  the one check the arc scale exists to provide.
- **A plan that never changes.** An `arc-plan.md` or `project-plan.md` whose
  Version History never grows while slices and arcs keep surfacing surprises is
  not stable — it is unmaintained, and the bubble-up checks are being skipped.
- **Detailed plans written far ahead.** Ten arc-plans authored on day one
  (see *plan late, plan deep*, Part III). They are written against assumptions
  the earlier arcs will invalidate, and they rot.

---

## Part VIII — When to update this document

Treat updates to this document like methodology updates: dated, disclosed,
with the rationale preserved — *spec-keeping for the spec itself.* Update it
when:

- The scales of work, the canonical layout, or the planning/closing process
  changes. This document owns all three now; keep the
  [methodology](./AI-ENGINEERING-METHODOLOGY.md)'s summary in sync when the
  vocabulary itself moves.
- An anti-pattern recurs across more than one project. Add it to Part VII with
  a name and a recognisable shape, so the next session refuses it on sight.
- A deferred asset category (project-scoped prompts, upstream contribution
  drafts, coverage reports, scratch) acquires a settled default. Add it with
  the same shape as the layout in Part II.

Two cross-references that are settled today and should not be re-invented:
CAP-style audit reports have a home in [`./CODE-AUDIT.md`](./CODE-AUDIT.md)
(`workbench/<YYYY.MM.DD>-audit-results-<slug>.md` plus a top-level index);
per-slice prompts live as `cc-prompt.md` inside the slice directory, not in a
separate prompts tree.

---

## Part IX — A worked example: the `odm` rebuild

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

## Version History

### Version 2.1 — June 2026

Synchronised with `LEDGER-DISCIPLINE.md` v2.0, which extended ledger discipline
from slice-only to all three scales. Added the **ledger section** to the
required contents of `arc-plan.md` (the arc ledger's composition rows, Part III)
and `project-plan.md` (the project ledger's DoD rows, Part III); noted in the
canonical layout (Part II) that the arc and project ledgers live as sections in
those plan docs and close in the matching `closing-report.md` (Option A — no new
files); and tied the arc composition check (Part V) to the arc/project ledger
closure. The bubble-up/close machinery is unchanged; this rev names the
verification rigor that now backs it at each scale.

### Version 2.0 — June 2026

Renamed from `ASSET-ORGANISATION.md` (v1, which covered only the slice/arc
layout and the confirmation protocol) and substantially expanded into the
framework's full project-management home. v1's scope note had **deferred**
project- and epic-level organisation "pending in-flight work on epic- and
project-level dependency tracking" — that work is the `odm` rebuild, which has
now matured through three arcs and informs this revision. v2.0 lands the
deferred layer:

- **Absorbed the scales-of-work, fundamental-unit, sizing, and default-layout
  detail extracted from [`AI-ENGINEERING-METHODOLOGY.md`](./AI-ENGINEERING-METHODOLOGY.md)**
  (which now keeps a summary and points here). The vocabulary
  (project/arc/slice/step/iteration) and the context-window basis for sizing a
  slice now live in Part I; the canonical layout in Part II.
- **Added `project-plan.md`** as the project-level plan-of-record (the arc
  roadmap), and formalized `arc-plan.md`'s required contents (Part III).
- **Added the top-down / bottom-up framing** and *plan late, plan deep*
  (Part III).
- **Added the slice bubble-up report and check** (Part IV), including the
  explicit slice-close arc-plan-update step, carried in the existing
  `closing-report.md` / `cdc-verification.md` rather than new files.
- **Added the formal arc-close process** (Part V): an arc-level
  `closing-report.md`, the composition check, the arc bubble-up report and
  check, and the project-plan-update decision it forces.
- **Added the plan-change discipline** (make-a-change + version-history,
  Part V) generalizing spec-keeping to the plan documents themselves.
- **Extended the anti-patterns** (Part VII) with closing-without-bubbling-up,
  closing-an-arc-by-fiat, never-changing plans, and far-ahead detailed plans.
- **Added a worked example** (Part IX, the `odm` rebuild).

The confirmation protocol (Part VI) and the anti-pattern core (Part VII) carry
forward from v1 with the layout references updated to this file and to the new
`project-plan.md` / arc-close artifacts.

### Version 1 — June 2026 (as `ASSET-ORGANISATION.md`)

Established the operational companion to the methodology's *A default layout*:
the slice/arc tree, the five per-slice documents, and the **confirmation
protocol** (quote the default, name the substitutions, give the operator
proceed / adjust / override, record the choice in the project's `CLAUDE.md`).
Broader project- and epic-level organisation was deferred. Shipped bundled in
the `collaboration-framework` skill.

---

_This document is a living spec. This version: 2.1, 2026-06-26._
