---
# === CORE IDENTIFICATION ===
concept: Simple One-for-One Supervisor
slug: simple-one-for-one-supervisor

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
section: "Simplified one_for_one Supervisors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "simple_one_for_one"
  - "simple one for one"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - restart-strategy
  - supervisor-behaviour
  - child-specification
extends:
  - one-for-one-strategy
related:
  - dynamic-child-process
contrasts_with:
  - one-for-one-strategy
  - one-for-all-strategy
  - rest-for-one-strategy

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do restart strategies affect child processes?"
  - "What is a restart strategy?"
---

# Quick Definition

A `simple_one_for_one` supervisor is a specialized variant where all child processes are dynamically added instances of the same process type, defined by a single child specification template.

# Core Definition

A supervisor with restart strategy `simple_one_for_one` is a simplified `one_for_one` supervisor, where all child processes are dynamically added instances of the same process. When started, the supervisor does not start any child processes. Instead, all child processes are added dynamically by calling `supervisor:start_child(Sup, List)` where `List` is appended to the arguments in the child specification's start MFA. The child is started by calling `apply(M, F, A++List)`. A child under a `simple_one_for_one` supervisor is terminated with `supervisor:terminate_child(Sup, Pid)` using the child's pid (not its id). Because it can have many children, it shuts them all down asynchronously. (Source: sup_princ.md, "Simplified one_for_one Supervisors")

# Prerequisites

- **[Restart Strategy](/concept-cards/otp-design-principles/restart-strategy.md)** -- `simple_one_for_one` is a variant of restart strategy.
- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- Requires a supervisor callback module.
- **[Child Specification](/concept-cards/otp-design-principles/child-specification.md)** -- Uses a single child spec as a template.

# Key Properties

1. **Single child spec template**: Only one child specification is provided; all children are instances of this template.
2. **No static children**: The supervisor starts with zero children. All children are added dynamically.
3. **Dynamic argument extension**: `supervisor:start_child(Sup, List)` appends `List` to the template's start arguments, calling `apply(M, F, A++List)`.
4. **Pid-based termination**: Children are terminated using their pid, not their id: `supervisor:terminate_child(Sup, Pid)`.
5. **Asynchronous shutdown**: Because it can have many children, shutdown is asynchronous -- children clean up in parallel with no defined order.
6. **Synchronous operations**: Starting, restarting, and manually terminating children are synchronous operations in the supervisor process context.

# Construction / Recognition

## To Construct/Create:
1. Set `strategy => simple_one_for_one` in supervisor flags.
2. Provide exactly one child specification as a template.
3. Add children dynamically using `supervisor:start_child(Sup, ExtraArgs)`.

## To Identify/Recognize:
1. Look for `strategy => simple_one_for_one` in the supervisor flags.
2. The `ChildSpecs` list will contain exactly one element serving as a template.

# Context & Application

Use `simple_one_for_one` when you need a pool or group of identical worker processes that are created dynamically at runtime. Common examples include connection handlers, session processes, or any scenario where an unbounded number of identical processes are spawned on demand.

# Examples

**Example 1** (sup_princ.md, "Simplified one_for_one Supervisors"): Callback module:

```erlang
-module(simple_sup).
-behaviour(supervisor).

-export([start_link/0]).
-export([init/1]).

start_link() ->
    supervisor:start_link(simple_sup, []).

init(_Args) ->
    SupFlags = #{strategy => simple_one_for_one,
                 intensity => 0,
                 period => 1},
    ChildSpecs = [#{id => call,
                    start => {call, start_link, []},
                    shutdown => brutal_kill}],
    {ok, {SupFlags, ChildSpecs}}.
```

**Example 2** (sup_princ.md, "Simplified one_for_one Supervisors"): Adding a child dynamically:

```erlang
supervisor:start_child(Pid, [id1])
```

This results in calling `apply(call, start_link, []++[id1])`, which is `call:start_link(id1)`.

# Relationships

## Builds Upon
- **[One-for-One Strategy](/concept-cards/otp-design-principles/one-for-one-strategy.md)** -- `simple_one_for_one` is a simplified variant of `one_for_one`.

## Enables
- **[Dynamic Child Process](/concept-cards/otp-design-principles/dynamic-child-process.md)** -- All children are dynamic under this strategy.

## Related
- **[Child Specification](/concept-cards/otp-design-principles/child-specification.md)** -- A single spec serves as the template for all children.

## Contrasts With
- **[One-for-One Strategy](/concept-cards/otp-design-principles/one-for-one-strategy.md)** -- Standard `one_for_one` supports static children and heterogeneous child specs.
- **[One-for-All Strategy](/concept-cards/otp-design-principles/one-for-all-strategy.md)** -- Restarts all children on failure, not just the failed one.
- **[Rest-for-One Strategy](/concept-cards/otp-design-principles/rest-for-one-strategy.md)** -- Restarts subsequent children on failure.

# Common Errors

- **Error**: Trying to terminate a child using its id instead of its pid.
  **Correction**: Use `supervisor:terminate_child(Sup, Pid)` with the child's pid. The id in the child spec is not used for termination under `simple_one_for_one`.

- **Error**: Expecting children to be started by the supervisor during `init`.
  **Correction**: A `simple_one_for_one` supervisor starts with zero children. All children must be added with `supervisor:start_child/2`.

# Common Confusions

- **Confusion**: The child spec `id` can be used to refer to individual children.
  **Clarification**: Since all children share the same spec template, the `id` is not meaningful for distinguishing individual children. Use pids instead.

- **Confusion**: Shutdown of children happens in order.
  **Clarification**: Because a `simple_one_for_one` supervisor can have many children, it shuts them all down asynchronously. The order of shutdown is not defined.

# Source Reference

sup_princ.md, "Simplified one_for_one Supervisors" section.

# Verification Notes

- Definition source: Directly quoted from sup_princ.md.
- Confidence rationale: High -- explicitly defined with full example.
- Uncertainties: None.
- Cross-reference status: References one-for-one-strategy, dynamic-child-process, child-specification.
