---
name: project-management
description: |
  Project management in the collaboration framework. Use when planning or
  closing projects, arcs, or slices; issuing or executing slice iterations;
  inspecting planning worktree layout; applying Expedited Mode; or deciding
  whether bubble-up findings require a plan update.
license: MIT
metadata:
  version: "3.0.0"
  hermes:
    tags: [ai-engineering, project-management, planning, ledger]
    category: meta-skills
---

# Project Management

Use this component before planning or closing anything at project, arc, or
slice scale. Start with the wayfinder, then load the focused guide that matches
the operation.

When decomposing new work, apply [usable-increment planning](./guides/03-planning-top-down.md#plan-for-usable-increments):
name the first useful result, its delivery home and actual input dependencies.
Keep quality checks with delivery and supporting evidence tied to a decision,
deliverable or check. Research and audit outcomes remain valid when explicitly scoped.
Before starting or assigning any investigation, [agree its usefulness, applicability
and budget with the Operator](./guides/03-planning-top-down.md#agree-investigations-before-starting).
An LLM may propose the inquiry, but may not authorize or extend it itself.

Before authoring an initial or corrective CC implementation prompt, load
engineering-methods' [prompt-authoring guide](../engineering-methods/guides/07-implementation-prompt-authoring.md).
Project-management governs the open set and handoff; engineering-methods governs
the source-grounded design, implementation recipe and readiness check.

Before executing any CC assignment, apply its required-reading manifest and
engineering-methods' [intake contract](../engineering-methods/guides/07-implementation-prompt-authoring.md#required-reading-and-cc-intake).
Load required contents completely and record coverage plus a contract readback;
resolve missing or conflicting inputs before dependent implementation.

For slice iterations, preserve issued prompts and create each follow-up as
`cc-prompt-iterationNN.md` beside the initial `cc-prompt.md` in the slice root.
Load the [filename contract](./guides/02-canonical-planning-worktree.md#slice-iteration-filenames-and-preservation)
and [handoff workflow](./guides/03-planning-top-down.md#issuing-and-executing-an-iteration)
before issuing or executing the assignment.

For Operator-selected [Autonomous Mode](./guides/README.md#autonomous-mode),
load its canonical definition and execution rules before acting. Record the
arc-default authorization (or explicit project override), non-default source
branch, explicitly Operator-approved role/model/relevant settings and scope,
contributor arrangement and actual independent reviewer where required
(or the self-check convention for an eligible One-Contributor task). CDC may revise
staffing and use direct routine handoffs within that authorization; Operator
decisions, tool permissions and evidence gates remain binding. Retain useful
existing records and ledger traceability under the
[existing-record and supporting-artifact rules](./guides/02-canonical-planning-worktree.md#existing-records-and-supporting-evidence).

For Operator-mediated CRC-to-CDC escalations and CDC-to-CRC instructions, load
[design handoff filenames](./guides/02-canonical-planning-worktree.md#design-handoff-filenames-and-preservation)
and [the two-way handoff procedure](./guides/03-planning-top-down.md#design-escalation-and-return-handoffs).
Use the [workflow-specific verification records](./guides/02-canonical-planning-worktree.md#verification-records-by-workflow-and-scale):
CDC at slices by default, CRC at slices and both CRC/CDC at higher scales when
three contributors are enabled. Preserve historical paths under the
[compatibility rule](./guides/02-canonical-planning-worktree.md#verification-filename-compatibility).

In the Three-Contributor Workflow and Autonomous Mode, CDC performs a retrospective at every closing
scale. Read the [record and handoff contract](./guides/02-canonical-planning-worktree.md#retrospective-records-in-the-three-contributor-workflow)
and [methodology-stewardship](../methodology-stewardship/SKILL.md).

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
