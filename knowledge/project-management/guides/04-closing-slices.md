# Part IV — Closing a slice, and bubbling up to the arc

A slice is not done when the code is written. It is done when its ledger is
closed *and* its outcome has been rolled up to the arc — because a slice that
delivered its diff but silently invalidated the arc's plan has not finished
its job; it has deferred a problem to whoever plans the next slice.

Two documents close a slice: `closing-report.md` (written by CC, the
implementer) and the assigned independent reviewer's record:
`cdc-verification.md` in the Two-Contributor Workflow, or `crc-verification.md`
in the Three-Contributor Workflow. Existing records are preserved per
[filename compatibility](./02-canonical-planning-worktree.md#verification-filename-compatibility).
The ledger-row mechanics of both are defined in
[`Row Closure`](../../work-verification/guides/03-row-closure.md). This section adds
the two things that make a close also a *bubble-up*.

### When review requires another iteration

A failed review keeps the slice open. The assigned reviewer records the
unresolved rows and issues the next slice-root prompt through
[Issuing and executing an iteration](./03-planning-top-down.md#issuing-and-executing-an-iteration).
CC executes that assignment before returning for review; existing close-set
files are evidence of earlier attempts, not permission to skip the new work.

Keep `closing-report.md` and the selected reviewer record as the canonical
close-set files. On subsequent attempts, preserve earlier findings and results
in dated, iteration-labelled sections and state the current verdict explicitly. Each
attempt identifies the exact prompt path and the source revision or working
tree state it assessed. Do not erase failed review evidence or silently carry
an earlier verdict forward over changed work.

### The slice closing-report — `closing-report.md`

CC writes the per-row walk: for every ledger row, the final status (`done` /
`deferred` / `no-op`) and the evidence, with no silent drops (the row count at
close must match the row count at open). The report also includes a
slice-artifact inventory: durable artifacts produced by the slice live under
`artifacts/` by default, or under the operator-recorded override; if the slice
produced none, say so explicitly. First-class slice documents, including every
issued iteration prompt, stay in the slice root and are excluded from the
supporting-artifact inventory. Identify the assignment being closed and check
its work against the ledger. Then CC adds a final section,
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

### The slice bubble-up check — in the verification record

The assigned reviewer verifies the closing report against evidence: re-running
the reproducible ledger rows and checking deferrals and no-ops, as ledger discipline
requires. Then the reviewer verifies the **bubble-up** itself:

- Confirm the slice delivered its assigned piece, against the arc-plan.
- Confirm the silent-drop diff is complete and honest.
- Confirm the reviewed assignment matches the current prompt recorded in
  `slice-plan.md`, its unresolved work is accounted for, and all issued prompts
  remain preserved at their recorded paths. Apply the recorded legacy-path
  disposition where relevant; do not silently move historical prompts.
- Confirm the artifact inventory is complete: every durable slice-produced
  supporting artifact is under `artifacts/`, or under the explicit override
  recorded in the slice plan and prompt; "none" is checked against the actual
  diff and outputs.
- **Decide whether the slice's findings require an arc-plan change.** If the
  slice surfaced anything in answer (2) above that changes the arc's slice
  breakdown, sequencing, or scope, then `arc-plan.md` **must be updated before
  the next slice is planned against it** — using the plan-change discipline
  (see the [plan-change discipline](./05-closing-arcs.md#the-plan-change-discipline-make-a-change--version-history)).
  A stale arc-plan that the next slice plans against is how a small
  discovery in one slice becomes a structural error three slices later.

CRC may record routine status and evidence updates, but must escalate changes
to architecture, scope, acceptance, or the arc's structural plan to CDC and the
Operator. CDC in the two-contributor workflow must likewise record decisions
and obtain required approval rather than changing the contract during review.
Do not advance against the revised plan until its amendments are authorized.

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
it is an answer you arrive at by asking, not by skipping the question. This
maintenance requirement does not grant amendment authority to its author.

---
