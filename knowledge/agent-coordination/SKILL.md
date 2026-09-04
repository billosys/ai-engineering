---
name: agent-coordination
description: |
  Component framework/operational skill for deciding what to keep in the main
  context and what to delegate to subagents. Use when planning multi-agent work,
  installing a delegation policy into local instructions, or checking whether a
  lookup task can be delegated without outsourcing design judgment.
version: 1.0.1
license: MIT
metadata:
  hermes:
    tags: [ai-engineering, collaboration, subagents, delegation]
    category: meta-skills
---

# Agent Coordination

Use this component when a task may benefit from subagents or parallel lookup.
It owns the boundary between lookup work, which can be delegated, and thinking
work, which stays in the main context.

Read the guide:

- [Subagent Delegation Policy](./guides/SUBAGENT-DELEGATION-POLICY.md)

This is a component entrypoint for the collaboration framework. It is included
inside `collaboration-framework.zip` as routed dependency material, not as a
separate installable package.

Component history lives in [version-history.md](./version-history.md).
