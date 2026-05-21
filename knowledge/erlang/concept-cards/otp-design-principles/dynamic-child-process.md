---
# === CORE IDENTIFICATION ===
concept: Dynamic Child Process
slug: dynamic-child-process

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervisors
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Supervisor Behaviour"
chapter_number: null
pdf_page: null
section: "Adding a Child Process"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "dynamic child"
  - "dynamically added child"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor-behaviour
  - child-specification
extends: []
related:
  - simple-one-for-one-supervisor
  - starting-a-supervisor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a supervisor with child specifications?"
  - "How do workers and supervisors relate in a supervision tree?"
---

# Quick Definition

A dynamic child process is a child added to an existing supervisor at runtime using `supervisor:start_child/2`, as opposed to static children defined in the `init/1` callback.

# Core Definition

In addition to the static supervision tree defined by child specifications in `init/1`, dynamic child processes can be added to an existing supervisor by calling `supervisor:start_child(Sup, ChildSpec)` where `Sup` is the pid or name of the supervisor and `ChildSpec` is a child specification. Child processes added using `start_child/2` behave in the same way as other child processes, with one important exception: if a supervisor dies and is recreated, then all child processes that were dynamically added to the supervisor are lost. Any child process can be stopped via `supervisor:terminate_child(Sup, Id)` and its specification deleted via `supervisor:delete_child(Sup, Id)`. As with dynamic children, the effects of deleting a static child specification are lost if the supervisor itself restarts. (Source: sup_princ.md, "Adding a Child Process" and "Stopping a Child Process")

# Prerequisites

- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- Dynamic children are added to supervisors.
- **[Child Specification](/concept-cards/otp-design-principles/child-specification.md)** -- A child spec must be provided when adding a dynamic child.

# Key Properties

1. **Runtime addition**: Added via `supervisor:start_child(Sup, ChildSpec)` after the supervisor has started.
2. **Lost on supervisor restart**: If the supervisor dies and is recreated, dynamically added children are lost.
3. **Same behavior as static**: Once added, dynamic children behave identically to static children (restarted per restart strategy and restart type).
4. **Stoppable**: Any child (static or dynamic) can be stopped with `supervisor:terminate_child(Sup, Id)`.
5. **Deletable**: A stopped child's specification can be deleted with `supervisor:delete_child(Sup, Id)`.
6. **simple_one_for_one**: Under this strategy, all children are dynamic and added with `supervisor:start_child(Sup, List)`.

# Construction / Recognition

## To Construct/Create:
1. Call `supervisor:start_child(Sup, ChildSpec)` with a supervisor reference and child specification.
2. For `simple_one_for_one` supervisors, call `supervisor:start_child(Sup, List)` where `List` extends the template's arguments.

## To Identify/Recognize:
1. Children not listed in the `init/1` return value but present in the supervisor's child list.
2. Calls to `supervisor:start_child/2` in the codebase.

# Context & Application

Dynamic child processes enable supervisors to adapt to runtime needs. Common use cases include adding connection handlers as clients connect, spawning task-specific workers on demand, or adjusting the process structure based on configuration changes. The `simple_one_for_one` strategy is specifically designed for supervisors that exclusively use dynamic children.

# Examples

**Example 1** (sup_princ.md, "Adding a Child Process"): Adding a dynamic child:

```erlang
supervisor:start_child(Sup, ChildSpec)
```

**Example 2** (sup_princ.md, "Stopping a Child Process"): Stopping and deleting a child:

```erlang
supervisor:terminate_child(Sup, Id),
supervisor:delete_child(Sup, Id)
```

**Example 3** (sup_princ.md, "Simplified one_for_one Supervisors"): Adding a child to a simple_one_for_one supervisor:

```erlang
supervisor:start_child(Pid, [id1])
```

# Relationships

## Builds Upon
- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- Dynamic children are managed by supervisors.
- **[Child Specification](/concept-cards/otp-design-principles/child-specification.md)** -- A child spec defines how to start the dynamic child.

## Enables
- Runtime-adaptive supervision structures.

## Related
- **[Simple One-for-One Supervisor](/concept-cards/otp-design-principles/simple-one-for-one-supervisor.md)** -- A strategy designed exclusively for dynamic children.
- **[Starting a Supervisor](/concept-cards/otp-design-principles/starting-a-supervisor.md)** -- Static children are started during supervisor initialization.

## Contrasts With
- Static children defined in `init/1` are recreated when the supervisor restarts; dynamic children are not.

# Common Errors

- **Error**: Relying on dynamic children surviving supervisor restarts.
  **Correction**: Dynamic children are lost when the supervisor dies and is recreated. If children must survive restarts, define them statically in `init/1` or re-add them after supervisor restart.

# Common Confusions

- **Confusion**: Dynamic children cannot be restarted by the supervisor.
  **Clarification**: Dynamic children are fully managed by the supervisor once added. They are restarted according to the restart strategy and their restart type. The only difference is they are lost if the supervisor itself is restarted.

# Source Reference

sup_princ.md, "Adding a Child Process" and "Stopping a Child Process" sections.

# Verification Notes

- Definition source: Directly from sup_princ.md.
- Confidence rationale: High -- explicitly described.
- Uncertainties: None.
- Cross-reference status: References supervisor-behaviour, child-specification, simple-one-for-one-supervisor, starting-a-supervisor.
