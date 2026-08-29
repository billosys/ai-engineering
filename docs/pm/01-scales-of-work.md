# Part I — The scales of work

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
and that plan-of-record lives in **`project-plan.md`** (see
[`Planning, top-down`](./03-planning-top-down.md)).

**Arc.** A set of related slices with a beginning and an end — the body of
work that delivers one coherent capability. An arc is the unit at which you
check that the slices *compose*: that together they add up to the capability
and that none is missing. It is approached through arc-and-slice breakdown
(SDLC step 4): decide which slices the arc needs, what order they land in,
and which are load-bearing for which. An arc is too big to hold in one branch
or one context — it is a planning unit, not an execution unit. Its
plan-of-record lives in **`arc-plan.md`** (see
[`Planning, top-down`](./03-planning-top-down.md)).

**Slice.** The unit of execution — the work that lands in a single branch as
one mergeable diff. A slice does one thing, end to end, and is sized to be
*held in a single model context with headroom to spare* — research,
implementation, tests, and self-review all carried without compaction, plus
slack for the fix-iterations the review process will surface. The slice is
where ledger discipline attaches — one slice, one ledger — and where the work
actually gets written, tested, and reviewed. Durable artifacts created by that
work belong to the slice by default, under the slice's `artifacts/` directory,
unless the operator records an override. If a slice will not fit in one context,
it was two slices.

Two more words name things *inside* a slice, not scales of their own:

**Step.** A single item in a slice's implementation plan — the fine-grained
unit of work, and what the ledger's rows verify. Steps are how a slice is
planned and tracked; they do not cross slice boundaries.

**Iteration.** A refinement pass on a slice whose delivery does not yet meet
its acceptance criteria. The word is reserved for this and only this — the
fix loop on an in-progress slice, never a unit of planning. The budget is
five iterations per slice (see [ledger
discipline](../../templates/LEDGER-DISCIPLINE.md)); needing more is a signal the
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
