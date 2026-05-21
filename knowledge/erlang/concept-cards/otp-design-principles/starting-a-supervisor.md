---
# === CORE IDENTIFICATION ===
concept: Starting a Supervisor
slug: starting-a-supervisor

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
section: "Starting a Supervisor"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "supervisor:start_link"
  - "supervisor startup"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor-behaviour
  - supervisor-flags
  - child-specification
extends: []
related:
  - dynamic-child-process
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a supervisor with child specifications?"
  - "What is a supervisor in OTP?"
---

# Quick Definition

Starting a supervisor involves calling `supervisor:start_link/2,3`, which spawns a new supervisor process that calls the `init/1` callback and synchronously starts all specified child processes in order.

# Core Definition

A supervisor is started by calling `supervisor:start_link/2` (unregistered) or `supervisor:start_link/3` (registered). This spawns and links to a new process. The first argument (or second in the 3-arity version) is the callback module name where `init/1` is located. The last argument is a term passed as-is to `init/1`. The new supervisor process calls `Module:init(Args)`, which must return `{ok, {SupFlags, ChildSpecs}}`. Subsequently, the supervisor starts its child processes according to the child specifications in start order. `supervisor:start_link/2,3` is synchronous -- it does not return until all child processes have been started. A name can be specified for registration using `{local, Name}` or `{global, Name}`. (Source: sup_princ.md, "Starting a Supervisor")

# Prerequisites

- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- Must implement the supervisor behaviour callback module.
- **[Supervisor Flags](/concept-cards/otp-design-principles/supervisor-flags.md)** -- Returned from `init/1` as part of the startup.
- **[Child Specification](/concept-cards/otp-design-principles/child-specification.md)** -- Returned from `init/1` to define static children.

# Key Properties

1. **Synchronous**: `start_link/2,3` does not return until all children have been started.
2. **Linked**: The supervisor is linked to the calling process.
3. **Callback**: Calls `Module:init(Args)` which must return `{ok, {SupFlags, ChildSpecs}}`.
4. **Registration optional**: Can be unregistered (use pid), locally registered, or globally registered.
5. **Start order**: Children are started in the order they appear in `ChildSpecs`.

# Construction / Recognition

## To Construct/Create:
1. Implement a callback module with `init/1`.
2. Call `supervisor:start_link(Module, Args)` for an unregistered supervisor.
3. Or call `supervisor:start_link({local, Name}, Module, Args)` for a registered supervisor.

## To Identify/Recognize:
1. Look for calls to `supervisor:start_link/2` or `supervisor:start_link/3`.
2. Look for `init/1` returning `{ok, {SupFlags, ChildSpecs}}`.

# Context & Application

Starting a supervisor is typically done from another supervisor's child specification or from an application's `start/2` callback. The synchronous nature ensures that the entire subtree is running before the parent considers the child started. This is important for ordered startup dependencies.

# Examples

**Example 1** (sup_princ.md, "Starting a Supervisor"): Unregistered supervisor:

```erlang
start_link() ->
    supervisor:start_link(ch_sup, []).
```

**Example 2** (sup_princ.md, "Starting a Supervisor"): The init callback:

```erlang
init(_Args) ->
    SupFlags = #{},
    ChildSpecs = [#{id => ch3,
                    start => {ch3, start_link, []},
                    shutdown => brutal_kill}],
    {ok, {SupFlags, ChildSpecs}}.
```

**Example 3** (sup_princ.md, "Starting a Supervisor"): Registered supervisor forms:

```erlang
supervisor:start_link({local, Name}, Module, Args)
supervisor:start_link({global, Name}, Module, Args)
```

# Relationships

## Builds Upon
- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- Starting is the lifecycle entry point for a supervisor.
- **[Child Specification](/concept-cards/otp-design-principles/child-specification.md)** -- Static children are started during supervisor initialization.

## Enables
- **[Dynamic Child Process](/concept-cards/otp-design-principles/dynamic-child-process.md)** -- After starting, dynamic children can be added.

## Related
- **[Supervisor Flags](/concept-cards/otp-design-principles/supervisor-flags.md)** -- Returned from `init/1` and applied during startup.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Expecting `supervisor:start_link` to return before all children are started.
  **Correction**: It is synchronous. Long-running child init functions will delay the supervisor's start_link return.

# Common Confusions

- **Confusion**: The supervisor can be started without linking.
  **Clarification**: `supervisor:start_link` always creates a link. This is by design for supervision tree integration.

# Source Reference

sup_princ.md, "Starting a Supervisor" section.

# Verification Notes

- Definition source: Directly from sup_princ.md, "Starting a Supervisor" section.
- Confidence rationale: High -- explicitly described with code examples.
- Uncertainties: None.
- Cross-reference status: References supervisor-behaviour, supervisor-flags, child-specification, dynamic-child-process.
