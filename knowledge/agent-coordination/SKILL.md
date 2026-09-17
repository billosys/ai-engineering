---
name: agent-coordination
description: |
  Component framework/operational skill for deciding what to keep in the main
  context and what to delegate to subagents. Use when planning multi-agent work,
  installing a delegation policy into local instructions, or checking whether a
  lookup task can be delegated without outsourcing design judgment.
license: MIT
metadata:
  version: "1.2.0"
  hermes:
    tags: [ai-engineering, collaboration, subagents, delegation]
    category: meta-skills
---

# Agent Coordination

Use this component when a task may benefit from subagents, parallel lookup, or
explicit multi-agent coordination. It owns the boundary between lookup work,
which can be delegated, and thinking/edit/review judgment, which stays in the
main context.

CC implements; CDC coordinates design and, by default, review. CRC owns routine
review and subsequent slice preparation only in the explicitly Operator-enabled
Three-Contributor Workflow. These are assigned contributor contexts, not
permission to outsource judgment to lookup subagents. For canonical roles,
authority, and transitions, read the
[methodology](../engineering-methods/guides/01-engineering-methodology.md#roles-and-shared-invariants).
The Operator-selected One-Contributor Workflow keeps design, implementation,
and self-review in one context without fictional role handoffs or automatic
delegation. Existing independent-review requirements still apply.

Read only the guide needed for the work:

- [When To Delegate](./guides/01-when-to-delegate.md) - the
  thinking-versus-lookup boundary, serial thinking, parallel lookup, and
  delegation decision rule.
- [Context Packets](./guides/02-context-packets.md) - self-contained lookup
  packets that gather evidence without smuggling design decisions into the
  delegated task.
- [Result Integration](./guides/03-result-integration.md) - parent-context
  inspection, evidence checking, contradiction handling, and final integration.
- [Anti-Patterns](./guides/04-anti-patterns.md) - thinking delegation, vague
  handoffs, summary trust, speed-over-quality pressure, buried boundaries,
  context starvation, and acceptance by formatting.

This is a component entrypoint for the collaboration framework. It is included
inside `collaboration-framework.zip` as routed dependency material and also
ships as the standalone `agent-coordination.zip` package.

Component history lives in [version-history.md](./version-history.md).
