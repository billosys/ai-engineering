# Anti-Patterns

Use this guide when delegation or multi-agent work starts to erode quality. It
names the failure modes the agent-coordination component is meant to prevent.

For the positive decision rule, load
[`01-when-to-delegate.md`](./01-when-to-delegate.md). For packet design, load
[`02-context-packets.md`](./02-context-packets.md). For reintegration, load
[`03-result-integration.md`](./03-result-integration.md).

## Thinking Delegation

Shape:

- "Implement this."
- "Review this diff."
- "Decide the architecture."
- "Write the final prose."

Why it fails:

The delegated context lacks the full conversation, loaded skills, project
conventions, and accountability for the integrated outcome. It can produce a
plausible answer while missing the constraint that mattered.

Correction:

Keep edit, design, review, synthesis, and acceptance judgment in the main
context. Delegate only lookup work with checkable evidence.

## Vague Handoffs

Shape:

- "Look into this."
- "Summarize the repo."
- "Find anything relevant."

Why it fails:

The task has no clear stop condition and no evidence contract. The result tends
to be broad summary, not usable evidence.

Correction:

Send a context packet with exact paths, searches, exclusions, and output shape.

## Summary Trust

Shape:

The parent accepts a returned summary without checking the cited files,
commands, or artifacts.

Why it fails:

The summary may be stale, overgeneralized, or wrong. Even when true, it often
compresses away the detail needed for correct implementation.

Correction:

Inspect primary evidence before using the result for design, edit, review, or
closure.

## Speed Over Quality On The Thinking Path

Shape:

Subagents are used to make reasoning feel faster: several agents each make
partial judgments, then the parent stitches them together.

Why it fails:

The work becomes coordination instead of thought. Coherence drifts, and no one
context owns the final argument.

Correction:

Use parallelism for lookup only. Keep the thinking path serial and accountable
in the parent context.

## Buried Delegation Boundaries

Shape:

The task plan says "use subagents as needed" without saying what may and may
not be delegated.

Why it fails:

Under time pressure, vague permission expands into delegated judgment.

Correction:

State the boundary directly:

```text
Thinking/edit/review judgment stays here. Lookup and evidence enumeration may
be delegated or parallelized.
```

## Context Starvation

Shape:

The delegated task requires project history, accepted architecture, local
instructions, or a quality bar that was not included in the packet.

Why it fails:

The subagent fills missing context with generic assumptions.

Correction:

Either include the needed context in the packet or keep the work in the parent
context.

## Acceptance By Formatting

Shape:

A returned table, checklist, or confident narrative is treated as reliable
because it looks organized.

Why it fails:

Format is not evidence.

Correction:

Require source-backed outputs and verify against primary artifacts.
