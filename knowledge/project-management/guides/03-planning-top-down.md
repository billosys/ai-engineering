# Part III — Planning, top-down

Planning runs from the project down to the slice. Each level produces one
plan-of-record and sets the context the level below plans against. The three
levels map onto SDLC steps 2–5.

### Planning authority

Use the [selected contributor workflow](../../engineering-methods/guides/01-engineering-methodology.md#workflow-selection-and-transitions).
CDC prepares project/arc plans and each arc's first slice with the Operator.
In the default Two-Contributor Workflow, CDC also prepares subsequent slices.
When explicitly enabled, CRC prepares those subsequent slices and iteration
prompts within the approved design. Detailing a planned slice is not authority
to re-scope it. Escalate architectural, scope, acceptance, or cross-arc changes
to CDC and the Operator, and record the decision before issuing affected work.

When the Operator selects the One-Contributor Workflow, the single contributor
handles planning with the Operator, without synthetic CC assignments or CRC
handoffs. The detailed artifact rules below apply to ledgered work, not as a
requirement to turn every bounded task into a project. Existing plans, evidence
requirements, and approvals remain binding.

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
4. **A sibling `ledger.md`.** The composition criteria that verify the DoD,
   stated up front as ledger rows — the project ledger from
   [`Ledger Discipline`](../../work-verification/guides/01-ledger-discipline.md)
   Section C. It opens beside the project plan and closes (per-row walk) in the
   project's `closing-report.md`. This is what makes the DoD *checkable* rather
   than merely asserted.
5. **A Version History section.** The change log that receives bubble-ups from
   arc closes (see [`Closing arcs`](./05-closing-arcs.md)). It starts with the initial roadmap as v1.0 and grows
   one dated entry per change, each naming which arc surfaced the change and
   why (the [plan-change discipline](./05-closing-arcs.md#the-plan-change-discipline-make-a-change--version-history)).
6. **Workflow and authority.** Record the selected contributor workflow,
   effective scope and authorization, role-to-context assignments, escalation
   boundaries, approval gates, and verification filename convention. Missing
   selection means the Two-Contributor Workflow, not permission to infer CRC.

`project-plan.md` is **not** a mega-file holding every arc's and slice's
detail — that is the anti-pattern in
[`Anti-patterns to refuse`](./07-anti-patterns.md). It holds the roadmap and the
change log; the detail lives in the per-arc and per-slice documents below it,
with durable slice-produced artifacts housed under the owning slice by default.

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
4. **A sibling `ledger.md`.** The composition criteria that verify the
   capability, stated up front as ledger rows — the arc ledger from
   [`Ledger Discipline`](../../work-verification/guides/01-ledger-discipline.md)
   Section B. It opens beside the arc plan and closes (per-row walk) in the
   arc's `closing-report.md`. This is what makes "the slices compose into the
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

If the slice will produce durable artifacts, the open set must also name the
artifact home. The default is `artifacts/` inside the slice directory. The
operator can override that default, but the override must be explicit in
`slice-plan.md` and repeated in `cc-prompt.md` so the implementing context does
not invent a second location. If no durable artifacts are expected, say so in
the slice plan; this prevents a missing `artifacts/` directory from reading as
an omission at close.

### Turn the slice into an implementation-ready assignment

Before issuing initial or corrective CC implementation work, the prompt author
must read engineering-methods' [From Slice to Implementation Prompt](../../engineering-methods/guides/07-implementation-prompt-authoring.md)
and apply its readiness check. This is the handoff from planning mechanics to
SDLC engineering: inspect source and tests, load the relevant domain guides,
resolve consequential choices, write the implementation recipe, and specify
observable test results. Record readiness in the existing slice plan or
assignment record with section pointers and any remaining held decisions.

The open set's existence is not evidence that this work was done. A list of
acceptance rows, reading links and commit commands is not an implementation
recipe. Exact supporting sections may carry detail, but the prompt must supply
a coherent current-slice implementation spine. Keep author/reviewer authority
and preserved-prompt rules unchanged; this adds no approval role. Evidence-only
assignments need precise inspection/evidence instructions, not invented code.

### Issuing and executing an iteration

When review finds unresolved acceptance criteria, the assigned reviewer keeps
the slice open and writes a new assignment using the
[iteration filename contract](./02-canonical-planning-worktree.md#slice-iteration-filenames-and-preservation).
Do not edit the issued `cc-prompt.md` or store the follow-up in `artifacts/`.

Maintain an **Assignment history** section in `slice-plan.md`, starting with
the initial handoff. Record each issued prompt's exact relative path, issue
date, predecessor, reason, and disposition (active, returned for review,
superseded, or accepted). Name the current assignment explicitly; a directory
listing, timestamp, or largest suffix does not establish which prompt was
issued. Update this record at handoff and review without erasing earlier
entries. Keep acceptance rows and evidence in the existing `ledger.md`.

Each iteration prompt must tell a fresh CC context:

- **Its assignment identity:** project/arc/slice, iteration number, its own
  path, and the preceding prompt path. State that CC is to execute this
  refinement pass and return evidence to the named reviewer (CDC or CRC).
- **What remains to do:** unresolved ledger row IDs, review findings with
  evidence pointers, required changes, and acceptance checks. Distinguish work
  already accepted from work still required; "see review comments" alone is
  not an executable assignment.
- **What still governs:** links to the current plans and ledger, scope and
  approval constraints, validation commands, expected outputs and their paths,
  and applicable commit instructions. Carry forward required constraints from
  earlier prompts; explicitly identify any authorized change. A new prompt
  does not itself authorize scope changes.
- **How to return results:** identify this prompt and iteration in the
  closing report, account for the assigned rows, and provide fresh evidence
  for the changes and affected checks. Earlier completion claims are context,
  not evidence that this assignment has been executed.

At handoff, give the operator the exact new prompt path as plain copy/paste
text relative to the project directory, including the arc/slice path. For
example: `arc02-example/slice01-example/cc-prompt-iteration01.md`. Identify the
pass as CC implementation work. This applies in normal and Expedited Mode.
Do not give the old prompt path with an instruction to reread its updates.

CC reads the named prompt from disk and checks it against the current
assignment in `slice-plan.md` before acting. A mismatch needs reconciliation;
do not guess from filenames. For a matching assignment, execute the remaining
work and validation before returning to the assigned reviewer. An earlier
closing report or "ready for review" statement does not cancel the new
assignment. If blocked, report the concrete blocker against the assigned work.

Numbered files preserve handoff history; they do not extend the five-iteration
fix-loop budget in [Scales of Work](./01-scales-of-work.md). Record actual
refinement passes in the assignment history; replacing an unstarted prompt
does not count as an executed pass. At the cap without convergence, surface
the need for re-scoping or an explicit operator decision rather than silently
issuing more work.

### Design escalation and return handoffs

When CRC encounters work outside its authority, stop the affected advancement
and create `crc-escalationNN.md` under the
[design handoff filename contract](./02-canonical-planning-worktree.md#design-handoff-filenames-and-preservation).
This is a decision request to CDC, not an instruction for CC to improvise.

The **CRC escalation report** includes:

- Owning project/arc/slice, report ID and path, current CC assignment, exact
  source state, and governing plan versions and ledger rows.
- The finding, reproduction/evidence pointers, uncertainty, and why the
  existing authority or acceptance contract cannot resolve it.
- Impact on architecture, scope, dependencies, acceptance, and previously
  accepted evidence; distinguish facts from hypotheses.
- Options, tradeoffs, CRC's recommendation, and the precise decisions or
  approvals requested. Do not present a recommendation as approved work.
- What is paused, what can proceed within existing authority, and who owns the
  next action. Preserve all unresolved findings and iteration accounting.

CRC gives the Operator the report's exact project-relative path as plain
copy/paste text, a concise summary of the decision needed, and the instruction
to pass the report to CDC. Supporting links may supplement, not replace, the
packet. Do not assume CDC can see CRC's conversation or will discover the report.

CDC reads the packet and canonical artifacts, resolves the design question with
the Operator, and writes **`cdc-directiveNN.md`**, explicitly referencing the
escalation. The directive includes:

- Its assignment identity, the report and prior directive it answers or
  supersedes, and the source/plan state on which the decision is based.
- A disposition for every requested decision: approved, rejected, deferred
  with re-entry conditions, or awaiting information/approval; include rationale
  and the Operator authorization required for any gated change.
- Exact instructions for CRC: permitted work, prohibited work, plan/ledger
  amendments and their owners, affected acceptance/reverification requirements,
  and whether to issue a new CC prompt. State what remains held.
- Expected return evidence, paths, and completion/escalation conditions. A
  deferred or unresolved decision is not an instruction to proceed past its gate.

CDC gives the Operator the directive's exact project-relative path as plain
copy/paste text, a short decision summary, and the instruction to pass it to
CRC. CDC must also use an explicit directive for CRC's initial assignment and
proactive changes to it; identify the initiating decision when no escalation
exists. Do not leave new constraints only in a separate conversation.

CRC reads the directive from disk, checks the cited state against the current
work, and acknowledges it in the owning plan's **Design handoff history** before
acting. Record packet paths, dates, predecessor, current status (awaiting CDC,
awaiting Operator, issued, acknowledged, implemented, or superseded), affected
rows, approval evidence, and next-action owner. Resolve stale or conflicting
instructions with CDC through the Operator rather than guessing. Apply the
authorized amendments, issue a distinct CC prompt when needed, and report the
result and evidence to the Operator, referencing the directive. If the directive
requires CDC follow-up, the Operator relays that report back to CDC before the
specified gate advances.

The Operator carrying a report between contexts is not blanket approval of its
contents. Explicit approvals, independent verification, and the original
quality floor still govern both directions of the exchange.

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
