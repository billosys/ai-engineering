# Project Management

> Wayfinder for the framework's project-management layer: the scales of work,
> planning artifacts and where they live on disk, the confirmation protocol,
> top-down planning, bottom-up close/bubble-up, and the maintenance discipline
> that keeps those mechanics from drifting.

This file is deliberately short. The operational detail used to live here as
one long document; it is now split into focused files under [`./pm/`](./pm/).
Start here, choose the section that matches the job, and load only the detailed
files the job requires.

The companion [methodology](./AI-ENGINEERING-METHODOLOGY.md) names the
philosophy: the three pillars, the 9-point SDLC, and the anti-degradation
disciplines. The project-management files are where that philosophy becomes
specific artifacts, filesystem layout, reports, and close checks. Do not
improvise those mechanics from the methodology summary.

## Notes for Codex

For Codex, read every "Claude session" in the linked files as any fresh Codex
Desktop, Codex CLI, or other LLM session entering the project without the full
prior context. **CC** is Codex CLI in the IC implementation role; **CDC** is
Codex Desktop in the planning/review/QA role. Keep the canonical filenames
(`project-plan.md`, `arc-plan.md`, `slice-plan.md`, per-scale `ledger.md`,
`cc-prompt.md`, `closing-report.md`, `cdc-verification.md`) unless the operator
explicitly changes the project convention.

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
| Understand the vocabulary and sizing model | [`pm/01-scales-of-work.md`](./pm/01-scales-of-work.md) |
| Create or inspect planning directories, filenames, metadata, or per-scale artifact sets | [`pm/02-canonical-planning-worktree.md`](./pm/02-canonical-planning-worktree.md) |
| Write a `project-plan.md`, `arc-plan.md`, per-scale `ledger.md`, or per-slice open set | [`pm/03-planning-top-down.md`](./pm/03-planning-top-down.md) |
| Close a slice and bubble findings up to the arc | [`pm/04-closing-slices.md`](./pm/04-closing-slices.md) and [`pm/05-closing-arcs.md`](./pm/05-closing-arcs.md#the-plan-change-discipline-make-a-change--version-history) |
| Close an arc, check composition, and bubble findings up to the project | [`pm/05-closing-arcs.md`](./pm/05-closing-arcs.md) |
| Confirm a layout before creating planning directories or filenames | [`pm/06-confirmation-protocol.md`](./pm/06-confirmation-protocol.md) |
| Detect or refuse recurring bad planning shapes | [`pm/07-anti-patterns.md`](./pm/07-anti-patterns.md) |
| Update this project-management spec | [`pm/08-maintenance.md`](./pm/08-maintenance.md) and [`pm/version-history.md`](./pm/version-history.md) |
| Ground the project-management flow in a real run | [`pm/09-worked-example-odm.md`](./pm/09-worked-example-odm.md) |

## Split Files

The old monolith split along its original part boundaries:

1. [`pm/01-scales-of-work.md`](./pm/01-scales-of-work.md) -- project, arc,
   slice, step, iteration, sizing, and the context-window basis for a slice.
2. [`pm/02-canonical-planning-worktree.md`](./pm/02-canonical-planning-worktree.md)
   -- default planning worktree, `planning` branch, `projectNN-<slug>`,
   metadata, naming rules, dedicated project/arc/slice ledger files, and the
   five per-slice documents.
3. [`pm/03-planning-top-down.md`](./pm/03-planning-top-down.md) -- project
   roadmaps, arc plans, per-slice open sets, and plan-late/plan-deep.
4. [`pm/04-closing-slices.md`](./pm/04-closing-slices.md) -- slice
   `closing-report.md`, `cdc-verification.md`, and slice-to-arc bubble-up.
5. [`pm/05-closing-arcs.md`](./pm/05-closing-arcs.md) -- arc
   `closing-report.md`, composition checks, arc-to-project bubble-up, and the
   plan-change discipline.
6. [`pm/06-confirmation-protocol.md`](./pm/06-confirmation-protocol.md) -- when
   to confirm, how to ask, and what to record after the operator answers.
7. [`pm/07-anti-patterns.md`](./pm/07-anti-patterns.md) -- planning layouts and
   habits to refuse or surface before adopting.
8. [`pm/08-maintenance.md`](./pm/08-maintenance.md) -- when to update the spec
   itself.
9. [`pm/09-worked-example-odm.md`](./pm/09-worked-example-odm.md) -- a concrete
   example of the project-management flow.
10. [`pm/version-history.md`](./pm/version-history.md) -- version history for
    the project-management guide.

## Minimum Context Shortcuts

Use these only when context is tight and the operation is narrow:

- **Starting a new planning layout:** read
  [`pm/02-canonical-planning-worktree.md`](./pm/02-canonical-planning-worktree.md)
  and [`pm/06-confirmation-protocol.md`](./pm/06-confirmation-protocol.md).
- **Planning an active arc or slice:** read
  [`pm/01-scales-of-work.md`](./pm/01-scales-of-work.md),
  [`pm/02-canonical-planning-worktree.md`](./pm/02-canonical-planning-worktree.md),
  and [`pm/03-planning-top-down.md`](./pm/03-planning-top-down.md).
- **Closing a slice:** read
  [`pm/04-closing-slices.md`](./pm/04-closing-slices.md) and the plan-change
  discipline in
  [`pm/05-closing-arcs.md`](./pm/05-closing-arcs.md#the-plan-change-discipline-make-a-change--version-history).
- **Closing an arc:** read [`pm/05-closing-arcs.md`](./pm/05-closing-arcs.md).

When in doubt, prefer reading the split files in order. The split reduces
context load; it does not relax the requirement to use the written mechanics.

## Version History

The detailed project-management version history lives in
[`pm/version-history.md`](./pm/version-history.md). Current version: **2.4**
(`2026-08-27`), which gives projects, arcs, and slices dedicated sibling
`ledger.md` files.

---

_The project-management guide is a living spec. This wayfinder: 2.4,
2026-08-27._
