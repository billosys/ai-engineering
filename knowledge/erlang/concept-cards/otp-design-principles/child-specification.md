---
# === CORE IDENTIFICATION ===
concept: Child Specification
slug: child-specification

# === CLASSIFICATION ===
category: applications-releases
subcategory: child-specs
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Supervisor Behaviour"
chapter_number: null
pdf_page: null
section: "Child Specification"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "child spec"
  - "child_spec()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor-behaviour
extends: []
related:
  - child-restart-type
  - shutdown-specification
  - significant-child
  - supervisor-flags
  - starting-a-supervisor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a child specification?"
  - "How do I define a supervisor with child specifications?"
  - "How do workers and supervisors relate in a supervision tree?"
---

# Quick Definition

A child specification is a map that tells a supervisor how to start, restart, and shut down a particular child process, including mandatory keys `id` and `start` and optional keys for restart type, shutdown, process type, and modules.

# Core Definition

The type definition for a child specification is a map with the following keys: `id` (mandatory) identifies the child internally by the supervisor; `start` (mandatory) defines the module-function-arguments tuple used to start the child; `restart` (optional, default `permanent`) defines when a terminated child is restarted; `significant` (optional) marks the child for automatic shutdown consideration; `shutdown` (optional, default `5000` for workers, `infinity` for supervisors) defines how the child is terminated; `type` (optional, default `worker`) specifies whether the child is a worker or supervisor; and `modules` (optional, defaults to `[M]` from start MFA) lists the callback module(s). (Source: sup_princ.md, "Child Specification")

# Prerequisites

- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- Child specifications are used within supervisor `init/1` callbacks.

# Key Properties

1. **`id`** (mandatory): Identifies the child specification internally by the supervisor. Occasionally called "name" in older documentation.
2. **`start`** (mandatory): An `{M, F, A}` tuple used as `apply(M, F, A)` to start the child. Must result in a call to `supervisor:start_link`, `gen_server:start_link`, `gen_statem:start_link`, `gen_event:start_link`, or a compliant function.
3. **`restart`** (optional, default `permanent`): One of `permanent`, `transient`, or `temporary`.
4. **`significant`** (optional, default `false`): Whether the child is significant for automatic shutdown.
5. **`shutdown`** (optional): Either `brutal_kill`, an integer timeout in milliseconds, or `infinity`. Default is `5000` for workers, `infinity` for supervisors.
6. **`type`** (optional, default `worker`): Either `worker` or `supervisor`.
7. **`modules`** (optional): A list with a single element -- the callback module name, or the atom `dynamic` for `gen_event` processes.

# Construction / Recognition

## To Construct/Create:
1. Create a map with at minimum `id` and `start` keys.
2. Set `start` to `{Module, Function, Args}` where the function starts an OTP-compliant process.
3. Add optional keys (`restart`, `shutdown`, `type`, `modules`, `significant`) as needed. Omitted keys use defaults.

## To Identify/Recognize:
1. Look for maps containing `id` and `start` keys within the `ChildSpecs` list in a supervisor's `init/1` return value.
2. The `start` value is always an `{M, F, A}` tuple.

# Context & Application

Child specifications are the primary mechanism for declaring what processes a supervisor manages. They appear in the list returned by `init/1` for static children, and can be passed to `supervisor:start_child/2` for dynamic children. The specification determines not just how a child starts, but its entire lifecycle within the supervision tree -- when it gets restarted, how it gets shut down, and whether it triggers automatic supervisor shutdown.

# Examples

**Example 1** (sup_princ.md, "Child Specification"): Full child specification for a worker:

```erlang
#{id => ch3,
  start => {ch3, start_link, []},
  restart => permanent,
  shutdown => brutal_kill,
  type => worker,
  modules => [ch3]}
```

**Example 2** (sup_princ.md, "Child Specification"): Simplified specification relying on defaults:

```erlang
#{id => ch3,
  start => {ch3, start_link, []},
  shutdown => brutal_kill}
```

**Example 3** (sup_princ.md, "Child Specification"): Specification for a gen_event child:

```erlang
#{id => error_man,
  start => {gen_event, start_link, [{local, error_man}]},
  modules => dynamic}
```

**Example 4** (sup_princ.md, "Child Specification"): Specification for a child supervisor:

```erlang
#{id => sup,
  start => {sup, start_link, []},
  restart => transient,
  type => supervisor} % will cause default shutdown=>infinity
```

# Relationships

## Builds Upon
- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- Child specs are used by supervisors to define their children.

## Enables
- **[Dynamic Child Process](/concept-cards/otp-design-principles/dynamic-child-process.md)** -- Dynamic children are added via `supervisor:start_child/2` with a child spec.
- **[Restart Strategy](/concept-cards/otp-design-principles/restart-strategy.md)** -- The restart strategy interacts with each child's restart type.

## Related
- **[Child Restart Type](/concept-cards/otp-design-principles/child-restart-type.md)** -- The `restart` key in the child spec.
- **[Shutdown Specification](/concept-cards/otp-design-principles/shutdown-specification.md)** -- The `shutdown` key in the child spec.
- **[Significant Child](/concept-cards/otp-design-principles/significant-child.md)** -- The `significant` key in the child spec.

## Contrasts With
- None directly; child specifications are unique to the supervisor behaviour.

# Common Errors

- **Error**: Omitting the mandatory `id` or `start` keys.
  **Correction**: Both `id` and `start` are required. The supervisor will refuse to start without them.

- **Error**: Setting `modules` to a bare atom instead of a list (e.g., `modules => ch3` instead of `modules => [ch3]`).
  **Correction**: The `modules` value must be a list with a single element, or the atom `dynamic` for gen_event processes.

# Common Confusions

- **Confusion**: The `id` field is the registered name of the child process.
  **Clarification**: The `id` is an internal identifier used by the supervisor to track child specifications. It is not the registered process name. The source notes that this identifier "occasionally has been called 'name'" but it is specifically an internal supervisor identifier.

- **Confusion**: Omitting optional keys causes an error.
  **Clarification**: All keys except `id` and `start` have sensible defaults: `restart` defaults to `permanent`, `shutdown` defaults to `5000` for workers and `infinity` for supervisors, `type` defaults to `worker`, and `modules` defaults to `[M]` from the start `{M,F,A}`.

# Source Reference

sup_princ.md, "Child Specification" section. Type definition: `child_spec()` map type.

# Verification Notes

- Definition source: Directly from sup_princ.md, "Child Specification" section including the type definition.
- Confidence rationale: High -- the child specification is explicitly defined with full type annotations.
- Uncertainties: None.
- Cross-reference status: References supervisor-behaviour, child-restart-type, shutdown-specification, significant-child, dynamic-child-process.
