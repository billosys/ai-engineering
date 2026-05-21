---
# === CORE IDENTIFICATION ===
concept: Supervisor Bridge
slug: supervisor-bridge

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Supervisors"
chapter_number: 7
pdf_page: 188
section: "Supervisor bridges"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "supervisor_bridge"
  - "supervision bridge"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor
  - supervision-tree
extends:
  - otp-behaviors
related:
  - special-process
contrasts_with:
  - supervisor

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a supervisor?"
  - "How do supervisors relate to the worker processes they manage?"
---

# Quick Definition

A supervisor bridge is an OTP behavior that connects a set of non-OTP-compliant processes into a supervision tree, acting like a supervisor toward its parent while starting and stopping its children through plain start/stop functions.

# Core Definition

The supervisor bridge is a behavior that allows you to connect a non-OTP-compliant set of processes to a supervision tree (Cesarini & Vinoski, p. 194). It behaves like a supervisor toward its own supervisor, but interacts with its child processes using predefined start and stop functions. It is started with `supervisor_bridge:start_link/2,3`, which calls the `init(Args)` callback in which you start your Erlang process subtree (all processes linked together); on success `init/1` returns `{ok, Pid, State}`. If `Pid` terminates, the bridge terminates with the same reason, invoking `terminate/2`, where the non-OTP-compliant processes are shut down (pp. 194-195).

# Prerequisites

- **Supervisor** — A supervisor bridge plays the supervisor role toward its parent; understanding supervisors is required.
- **Supervision tree** — The bridge exists to attach foreign processes into a supervision tree.

# Key Properties

1. Acts like a supervisor toward its parent, but manages children via plain start/stop functions.
2. Started with `supervisor_bridge:start_link(NameScope, Mod, Args)`.
3. `Mod:init(Args)` starts the foreign subtree and returns `{ok, Pid, State}`, `ignore`, or `{error, Reason}`.
4. `Mod:terminate(Reason, State)` shuts down the non-OTP-compliant processes.
5. The bridge handles `sys`-module debug options, but the processes it connects have no code-upgrade or debug functionality.
6. If the bridge receives a `shutdown` from its supervisor, `terminate/2` is also called.

# Construction / Recognition

## To Construct/Create:
1. Create a callback module with `-behavior(supervisor_bridge).`
2. Implement `init/1` to start the linked foreign subtree and return `{ok, Pid, State}`.
3. Implement `terminate/2` to shut down those processes.
4. Start it with `supervisor_bridge:start_link/2,3`.

## To Identify/Recognize:
1. The module uses the `supervisor_bridge` behavior.
2. It exports `init/1` returning `{ok, Pid, State}` and `terminate/2`.

# Context & Application

- **Typical contexts**: Integrating legacy or non-OTP code into an OTP supervision tree.
- **Common applications**: Wrapping a pre-OTP process group so a release can be OTP compliant.
- **Historical/stylistic notes**: The book recounts that early-1990s Ericsson systems predated OTP; the `supervisor_bridge` behavior was created so such systems could attach to OTP supervision trees without a full rewrite (p. 194).

# Examples

**Example 1** (pp. 194-195): A supervision tree where the right-hand side is OTP behaviors and the left-hand side connects non-OTP-compliant processes through a supervisor bridge (Figure 8-11).

## Worked Example

The supervisor bridge API and callbacks (p. 195):

```erlang
supervisor_bridge:start_link(NameScope, Mod, Args) ->
    {ok, Pid} | ignore | {error, {already_started,Pid}}

Mod:init(Args) -> {ok,Pid,State} | ignore | {error,Reason}
Mod:terminate(Reason, State) -> term()
```

# Relationships

## Builds Upon
- **OTP behaviour** — `supervisor_bridge` is one of the standard OTP behaviors.

## Enables
- *(none)*

## Related
- **Special process** — An alternative way to make a process OTP-compliant; bridges suit groups of non-compliant processes.

## Contrasts With
- **Supervisor** — A true supervisor manages OTP behaviors with restart strategies; a bridge manages a non-OTP subtree via plain start/stop functions and offers limited supervision.

# Common Errors

- **Error**: Expecting code-upgrade and debug support for the processes behind a bridge.
  **Correction**: The bridge supports `sys` debug options itself, but the foreign processes it connects have no upgrade or debug functionality.

# Common Confusions

- **Confusion**: Thinking a supervisor bridge gives non-OTP processes full supervision.
  **Clarification**: Supervision is limited to what the foreign subtree implements; the bridge only connects it and restarts the whole subtree on failure.

# Source Reference

Chapter 7: Supervisors, "Non-OTP-Compliant Processes" / "Supervisor bridges," pages 194-195. See Figure 8-11 (Supervisor bridges) and Table 8-2.

# Verification Notes

- Definition source: Direct adaptation from pp. 194-195.
- Confidence rationale: HIGH — explicitly defined with the API/callback listing and a figure.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
