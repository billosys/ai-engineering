---
# === CORE IDENTIFICATION ===
concept: Supervisor Behaviour
slug: supervisor-behaviour

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
section: "Supervision Principles"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "supervisor"
  - "OTP supervisor"
  - "supervisor process"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - behaviour
  - supervision-tree
extends:
  - behaviour
related:
  - child-specification
  - restart-strategy
  - supervisor-flags
  - starting-a-supervisor
contrasts_with:
  - gen-server
  - gen-statem
  - gen-event

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a supervisor in OTP?"
  - "How do workers and supervisors relate in a supervision tree?"
  - "What must I know before designing a supervision tree?"
---

# Quick Definition

A supervisor is an OTP behaviour process responsible for starting, stopping, and monitoring its child processes, keeping them alive by restarting them when necessary.

# Core Definition

A supervisor is responsible for starting, stopping, and monitoring its child processes. The basic idea of a supervisor is that it is to keep its child processes alive by restarting them when necessary. Which child processes to start and monitor is specified by a list of child specifications. The child processes are started in the order specified by this list, and are terminated in the reverse order. (Source: sup_princ.md, "Supervision Principles")

# Prerequisites

- **[Behaviour](/concept-cards/otp-design-principles/behaviour.md)** -- The supervisor is an OTP behaviour, requiring a callback module.
- **[Supervision Tree](/concept-cards/otp-design-principles/supervision-tree.md)** -- Supervisors are the structural backbone of supervision trees.

# Key Properties

1. **Child management**: Starts, stops, and monitors child processes.
2. **Restart capability**: Automatically restarts terminated child processes based on the configured restart strategy.
3. **Ordered startup**: Child processes are started in the order specified in the child specification list.
4. **Reverse termination**: Child processes are terminated in reverse start order during shutdown.
5. **Callback module**: Requires an `init/1` callback that returns `{ok, {SupFlags, ChildSpecs}}`.

# Construction / Recognition

## To Construct/Create:
1. Create a callback module with `-behaviour(supervisor)`.
2. Export `start_link/0` (or similar) and `init/1`.
3. Implement `init/1` to return `{ok, {SupFlags, ChildSpecs}}` where `SupFlags` is a map of supervisor flags and `ChildSpecs` is a list of child specifications.
4. Call `supervisor:start_link/2` or `supervisor:start_link/3` from `start_link`.

## To Identify/Recognize:
1. Look for `-behaviour(supervisor)` module attribute.
2. Look for `init/1` returning `{ok, {SupFlags, ChildSpecs}}`.
3. Look for calls to `supervisor:start_link/2,3`.

# Context & Application

Supervisors form the non-leaf nodes of supervision trees. They are used whenever you need fault-tolerant process management. Every OTP application typically has at least one top-level supervisor. Supervisors can supervise both worker processes (gen_server, gen_statem, gen_event, or special processes) and other supervisors, enabling hierarchical fault isolation.

# Examples

**Example 1** (sup_princ.md, "Example"): A supervisor callback module starting a gen_server child:

```erlang
-module(ch_sup).
-behaviour(supervisor).

-export([start_link/0]).
-export([init/1]).

start_link() ->
    supervisor:start_link(ch_sup, []).

init(_Args) ->
    SupFlags = #{strategy => one_for_one, intensity => 1, period => 5},
    ChildSpecs = [#{id => ch3,
                    start => {ch3, start_link, []},
                    restart => permanent,
                    shutdown => brutal_kill,
                    type => worker,
                    modules => [ch3]}],
    {ok, {SupFlags, ChildSpecs}}.
```

# Relationships

## Builds Upon
- **[Behaviour](/concept-cards/otp-design-principles/behaviour.md)** -- The supervisor is one of the standard OTP behaviours.

## Enables
- **[Supervision Tree](/concept-cards/otp-design-principles/supervision-tree.md)** -- Supervisors are the building blocks of supervision trees.
- **[Automatic Shutdown](/concept-cards/otp-design-principles/automatic-shutdown.md)** -- Supervisors can be configured to automatically shut down.

## Related
- **[Child Specification](/concept-cards/otp-design-principles/child-specification.md)** -- Defines which children the supervisor manages.
- **[Restart Strategy](/concept-cards/otp-design-principles/restart-strategy.md)** -- Determines how the supervisor responds to child failures.
- **[Supervisor Flags](/concept-cards/otp-design-principles/supervisor-flags.md)** -- Configuration map controlling supervisor behavior.

## Contrasts With
- **[gen_server](/concept-cards/otp-design-principles/gen-server.md)** -- A worker behaviour, not a supervisory one.
- **[Special Process](/concept-cards/otp-design-principles/special-process.md)** -- A non-behaviour OTP-compliant process.

# Common Errors

- **Error**: Forgetting to return `{ok, {SupFlags, ChildSpecs}}` from `init/1`.
  **Correction**: The `init/1` callback must return exactly `{ok, {SupFlags, ChildSpecs}}` where `SupFlags` is a map and `ChildSpecs` is a list.

- **Error**: Setting the same restart intensity values at all supervisor levels in a deep hierarchy.
  **Correction**: The total number of restarts before the top-level supervisor gives up is the product of intensity values at all levels. Use lower intensity at higher levels (e.g., 3 at top, 10 at lower levels).

# Common Confusions

- **Confusion**: A supervisor is just a regular process that monitors children.
  **Clarification**: A supervisor is specifically an OTP behaviour with well-defined restart strategies, child specifications, and integration with the OTP supervision tree framework. It provides structured fault recovery, not just monitoring.

# Source Reference

sup_princ.md, "Supervision Principles" and "Example" sections. See also `m:supervisor` in STDLIB.

# Verification Notes

- Definition source: Directly quoted from sup_princ.md, "Supervision Principles" section.
- Confidence rationale: High -- the supervisor behaviour is explicitly and thoroughly defined in the source.
- Uncertainties: None.
- Cross-reference status: References behaviour, supervision-tree, gen-server, gen-statem, gen-event as cross-module slugs.
