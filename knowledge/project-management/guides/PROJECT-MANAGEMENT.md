# Project Management

> Wayfinder for the framework's project-management layer: the scales of work,
> planning artifacts and where they live on disk, the confirmation protocol,
> top-down planning, bottom-up close/bubble-up, and the maintenance discipline
> that keeps those mechanics from drifting.

This file is deliberately short. The operational detail used to live here as
one long document; it is now split into focused files in this `guides/`
directory.
Start here, choose the section that matches the job, and load only the detailed
files the job requires.

The companion [methodology](../../engineering-methods/guides/01-engineering-methodology.md) names the
philosophy: the three pillars, the 9-point SDLC, and the anti-degradation
disciplines. The project-management files are where that philosophy becomes
specific artifacts, filesystem layout, reports, and close checks. Do not
improvise those mechanics from the methodology summary.

## Notes for Codex

For Codex, read every "Claude session" in the linked files as any fresh Codex
Desktop, Codex CLI, or other LLM session entering the project without the full
prior context. For the canonical **CC**, **CDC**, and **Operator** role
definitions, read
[`01-engineering-methodology.md#notes-for-codex`](../../engineering-methods/guides/01-engineering-methodology.md#notes-for-codex).
Keep the canonical filenames (`project-plan.md`, `arc-plan.md`,
`slice-plan.md`, per-scale `ledger.md`, `cc-prompt.md`,
`closing-report.md`, `cdc-verification.md`) and the default slice
`artifacts/` home unless the operator explicitly changes the project
convention.

This wayfinder and the linked files guide planning craft and the quality floor;
they do not override Codex's standing system, developer, tool, safety, sandbox,
or user instructions. If a conflict appears, name the tension and follow the
governing instruction stack rather than forcing the methodology to fit.

## Required Load Set

If you are about to **plan or close anything** -- a project, an arc, or a slice
-- read this wayfinder first, then read the detailed file or files for the
operation at hand. For full project-management context, read the files below in
order.

| Job | Read |
| --- | --- |
| Understand the vocabulary and sizing model | [`guides/01-scales-of-work.md`](./01-scales-of-work.md) |
| Create or inspect planning directories, filenames, metadata, per-scale document sets, or slice artifact homes | [`guides/02-canonical-planning-worktree.md`](./02-canonical-planning-worktree.md) |
| Write a `project-plan.md`, `arc-plan.md`, per-scale `ledger.md`, or per-slice open set | [`guides/03-planning-top-down.md`](./03-planning-top-down.md) |
| Close a slice and bubble findings up to the arc | [`guides/04-closing-slices.md`](./04-closing-slices.md) and [`guides/05-closing-arcs.md`](./05-closing-arcs.md#the-plan-change-discipline-make-a-change--version-history) |
| Close an arc, check composition, and bubble findings up to the project | [`guides/05-closing-arcs.md`](./05-closing-arcs.md) |
| Confirm a layout before creating planning directories or filenames | [`guides/06-confirmation-protocol.md`](./06-confirmation-protocol.md) |
| Detect or refuse recurring bad planning shapes | [`guides/07-anti-patterns.md`](./07-anti-patterns.md) |
| Update this project-management spec | [`guides/08-maintenance.md`](./08-maintenance.md) and [`version-history.md`](../version-history.md) |
| Ground the project-management flow in a real run | [`guides/09-worked-example-odm.md`](./09-worked-example-odm.md) |

## Expedited Mode

For tighter, more temporally efficient implementation cycles, the operator may
opt into **Expedited Mode**. When engaged, the LLMs must adhere to the
following:

- Have CC commit after his changes, even before CDC review. Because other
  processes may be working on the same branch and staging their own files, CC
  commit instructions must explicitly list the files to be committed.
- Have CDC commit after CDC changes or reviews, and provide the operator with
  concise reports.
- As soon as the evidence is in place for a full close of a slice, close it.
- After a slice is closed, open the next slice immediately and give the
  operator the prompt-file path for CC, relative to the project directory.
- After the last slice of an arc is closed, automatically continue to formal
  arc close, then open the next arc and its first slice, complete with CC
  prompt, when the project roadmap provides one.

Expedited Mode only changes the explicit commit, close, and advance behaviors
listed above. Expedited Mode means no shortcuts, no skipped validation, no
weaker evidence or review, no inferred source scope and no reduction or other
change in scope, no timeline interpretation, and no override of explicit
operator approval gates recorded in a plan or prompt.

Guardrail phrases for source and package validation: no shortcuts; no skipped validation; no weaker evidence or review; no inferred source scope and no reduction or other change in scope; no timeline interpretation; operator approval gates are not overridden.

## Split Files

The old monolith split along its original part boundaries:

1. [`guides/01-scales-of-work.md`](./01-scales-of-work.md) -- project, arc,
   slice, step, iteration, sizing, and the context-window basis for a slice.
2. [`guides/02-canonical-planning-worktree.md`](./02-canonical-planning-worktree.md)
   -- default planning worktree, `planning` branch, `projectNN-<slug>`,
   metadata, naming rules, dedicated project/arc/slice ledger files, and the
   per-slice document set plus the default slice `artifacts/` home.
3. [`guides/03-planning-top-down.md`](./03-planning-top-down.md) -- project
   roadmaps, arc plans, per-slice open sets, and plan-late/plan-deep.
4. [`guides/04-closing-slices.md`](./04-closing-slices.md) -- slice
   `closing-report.md`, `cdc-verification.md`, and slice-to-arc bubble-up.
5. [`guides/05-closing-arcs.md`](./05-closing-arcs.md) -- arc
   `closing-report.md`, composition checks, arc-to-project bubble-up, and the
   plan-change discipline.
6. [`guides/06-confirmation-protocol.md`](./06-confirmation-protocol.md) -- when
   to confirm, how to ask, and what to record after the operator answers.
7. [`guides/07-anti-patterns.md`](./07-anti-patterns.md) -- planning layouts and
   habits to refuse or surface before adopting.
8. [`guides/08-maintenance.md`](./08-maintenance.md) -- when to update the spec
   itself.
9. [`guides/09-worked-example-odm.md`](./09-worked-example-odm.md) -- a concrete
   example of the project-management flow.
10. [`version-history.md`](../version-history.md) -- version history for
    the project-management guide.

## Minimum Context Shortcuts

Use these only when context is tight and the operation is narrow:

- **Starting a new planning layout:** read
  [`guides/02-canonical-planning-worktree.md`](./02-canonical-planning-worktree.md)
  and [`guides/06-confirmation-protocol.md`](./06-confirmation-protocol.md).
- **Planning an active arc or slice:** read
  [`guides/01-scales-of-work.md`](./01-scales-of-work.md),
  [`guides/02-canonical-planning-worktree.md`](./02-canonical-planning-worktree.md),
  and [`guides/03-planning-top-down.md`](./03-planning-top-down.md).
- **Closing a slice:** read
  [`guides/04-closing-slices.md`](./04-closing-slices.md) and the plan-change
  discipline in
  [`guides/05-closing-arcs.md`](./05-closing-arcs.md#the-plan-change-discipline-make-a-change--version-history).
- **Closing an arc:** read [`guides/05-closing-arcs.md`](./05-closing-arcs.md).

When in doubt, prefer reading the split files in order. The split reduces
context load; it does not relax the requirement to use the written mechanics.

## Version History

The detailed project-management version history lives in
[`version-history.md`](../version-history.md). Current version: **2.8**
(`2026-09-04`), which moves project-management history beside the component
entrypoint and clarifies that Expedited Mode changes only the listed process
mechanics without weakening scope, evidence, validation, review, timing, or
operator approval gates.

---

_The project-management guide is a living spec. This wayfinder: 2.8,
2026-09-04._
