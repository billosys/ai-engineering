---
name: project-management
description: |
  Project management in the collaboration framework. Use when planning or
  closing projects, arcs, or slices; issuing or executing slice iterations;
  inspecting planning worktree layout; applying Expedited Mode; or deciding
  whether bubble-up findings require a plan update.
license: MIT
metadata:
  version: "2.16.0"
  hermes:
    tags: [ai-engineering, project-management, planning, ledger]
    category: meta-skills
---

# Project Management

Use this component before planning or closing anything at project, arc, or
slice scale. Start with the wayfinder, then load the focused guide that matches
the operation.

For slice iterations, preserve issued prompts and create each follow-up as
`cc-prompt-iterationNN.md` beside the initial `cc-prompt.md` in the slice root.
Load the [filename contract](./guides/02-canonical-planning-worktree.md#slice-iteration-filenames-and-preservation)
and [handoff workflow](./guides/03-planning-top-down.md#issuing-and-executing-an-iteration)
before issuing or executing the assignment.

For Operator-mediated CRC-to-CDC escalations and CDC-to-CRC instructions, load
[design handoff filenames](./guides/02-canonical-planning-worktree.md#design-handoff-filenames-and-preservation)
and [the two-way handoff procedure](./guides/03-planning-top-down.md#design-escalation-and-return-handoffs).
Use the [workflow-specific verification records](./guides/02-canonical-planning-worktree.md#verification-records-by-workflow-and-scale):
CDC at slices by default, CRC at slices and both CRC/CDC at higher scales when
three contributors are enabled. Preserve historical paths under the
[compatibility rule](./guides/02-canonical-planning-worktree.md#verification-filename-compatibility).

Read first:

- [Project Management Guide README](./guides/README.md)

Focused guides:

- [Scales of Work](./guides/01-scales-of-work.md)
- [Canonical Planning Worktree](./guides/02-canonical-planning-worktree.md)
- [Planning Top Down](./guides/03-planning-top-down.md)
- [Closing Slices](./guides/04-closing-slices.md)
- [Closing Arcs](./guides/05-closing-arcs.md)
- [Confirmation Protocol](./guides/06-confirmation-protocol.md)
- [Anti-Patterns](./guides/07-anti-patterns.md)
- [Maintenance](./guides/08-maintenance.md)
- [Worked Example: ODM](./examples/01-worked-example-odm.md)
- [Version History](./version-history.md)

This is a component entrypoint for the collaboration framework. It is included
inside `collaboration-framework.zip` as routed dependency material and also
ships as the standalone `project-management.zip` package.
