---
# === CORE IDENTIFICATION ===
concept: Supervisor
slug: supervisor

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Supervisors"
chapter_number: 7
pdf_page: 188
section: "Supervision Trees"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "supervisor behavior"
  - "supervisor behaviour"
  - "supervisor module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervision-tree
  - child-specification
extends:
  - otp-behaviors
related:
  - restart-strategy
  - supervisor-specification
  - worker-process
  - dynamic-children
contrasts_with:
  - worker-process
  - supervisor-bridge

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a supervisor?"
  - "What distinguishes a supervisor from a worker process?"
  - "How do supervisors relate to the worker processes they manage?"
  - "How do I write a supervisor and define its child specifications?"
---

# Quick Definition

A supervisor is an OTP process whose only task is to start, monitor, and manage child processes, restarting them according to a configured strategy when they terminate abnormally. It is implemented by the generic `supervisor` behavior plus a callback module that exports `init/1`.

# Core Definition

Supervisors are processes whose only task is to monitor and manage children. They spawn processes and link themselves to these processes; by trapping exits and receiving EXIT signals, they can take appropriate action when something unexpected occurs — restarting a child, not restarting it, terminating some or all children, or terminating themselves (Cesarini & Vinoski, p. 170). In OTP the supervisor behavior is implemented in the `supervisor` library module; the callback module supplies the nongeneric code, exporting a single callback, `init/1`, used at startup to configure and start the subset of the tree handled by that supervisor (p. 175). The behavior handles monitoring, restart strategies, race conditions, and borderline cases "in a deterministic and consistent manner" (p. 169).

# Prerequisites

- **Supervision tree** — A supervisor exists to be a node in a supervision tree; understanding the tree gives the supervisor its purpose.
- **Child specification** — A supervisor is configured by the list of child specifications it returns from `init/1`.

# Key Properties

1. A supervisor's sole responsibility is monitoring and managing children — it contains no business logic.
2. It traps exits and receives EXIT signals from its linked children.
3. The callback module exports `init/1`, which returns `{ok, {SupFlags, [ChildSpec]}}` or `ignore`.
4. Supervisors are started with `supervisor:start_link/2,3` — there is no `start/2,3`, forcing a link to the parent.
5. Supervisors expose no built-in stop function; they are stopped by their own supervisor or when the node terminates.
6. Children must be OTP-compliant behaviors (or special processes / supervisor bridges) that handle system messages.

# Construction / Recognition

## To Construct/Create:
1. Create a callback module with `-behavior(supervisor).`
2. Export and define `start_link/0`, calling `supervisor:start_link({local,?MODULE}, ?MODULE, [])`.
3. Export and define `init/1` to return `{ok, {SupFlags, ChildSpecList}}`.
4. Build each child specification (tuple or map) describing how to start and manage a child.

## To Identify/Recognize:
1. The module includes `-behavior(supervisor).`
2. It exports `init/1` returning a supervisor specification.
3. It calls `supervisor:start_link/2,3` rather than `start/2,3`.

# Context & Application

- **Typical contexts**: Every node in a supervision tree; the top-level process an OTP application starts.
- **Common applications**: Restarting crashed workers; isolating failures; managing dynamically added children.
- **Historical/stylistic notes**: The book contrasts the OTP `supervisor` with a hand-written `my_supervisor`, concluding that *all* of `my_supervisor` is generic code — the specific parts (which children, dependencies, name) are passed as data (Table 8-1, p. 172).

# Examples

**Example 1** (p. 175): The `frequency_sup` callback module — `start_link/0` calls `supervisor:start_link({local,?MODULE},?MODULE,[])` and `init/1` returns a `rest_for_one` spec with `freq_overload` and `frequency` children.

**Example 2** (pp. 184-186): `phone_sup` — an empty supervisor that dynamically starts and monitors phone FSMs.

## Worked Example

The `frequency_sup` supervisor callback module (p. 175):

```erlang
-module(frequency_sup).
-behavior(supervisor).
-export([start_link/0, init/1]).
-export([stop/0]).

start_link() ->
    supervisor:start_link({local,?MODULE},?MODULE, []).

stop() ->
    exit(whereis(?MODULE), shutdown).

init(_) ->
    ChildSpecList = [child(freq_overload), child(frequency)],
    {ok,{{rest_for_one, 2, 3600}, ChildSpecList}}.

child(Module) ->
    {Module, {Module, start_link, []},
     permanent, 2000, worker, [Module]}.
```

# Relationships

## Builds Upon
- **OTP behaviour** — The supervisor is one of the standard OTP behaviors, splitting generic and specific code.

## Enables
- **Supervision tree** — Supervisors are the nodes from which trees are built.
- **Dynamic children** — Supervisors provide `start_child`, `terminate_child`, `restart_child`, `delete_child`.

## Related
- **Restart strategy** — Configured in the supervisor specification.
- **Supervisor specification** — The value `init/1` returns to configure the supervisor.
- **Worker process** — The leaf processes a supervisor manages.

## Contrasts With
- **Worker process** — Workers do business logic; supervisors only monitor and restart.
- **Supervisor bridge** — A bridge connects non-OTP-compliant processes; a true supervisor manages OTP behaviors.

# Common Errors

- **Error**: Attaching a plain Erlang process (not a behavior) as a supervisor child.
  **Correction**: Children must be OTP behaviors, special processes, or supervisor bridges that handle system messages; no warning is given otherwise.

- **Error**: Doing heavy work in `init/1`, blocking the synchronous startup sequence.
  **Correction**: Minimize work in `init/1`; defer noncritical initialization (e.g. with a `0` timeout or a message to `self()`).

# Common Confusions

- **Confusion**: Thinking a supervisor "handles errors" by inspecting them.
  **Clarification**: Supervisors do not diagnose failures; they restart children per a fixed strategy and escalate when restarts do not help.

- **Confusion**: Expecting a supervisor to export a `stop` function.
  **Clarification**: Supervisors expose no built-in stop; they are terminated by their parent or the node. A `stop/0` can only simulate a higher supervisor's shutdown.

# Source Reference

Chapter 7: Supervisors, "OTP Supervisors" / "The Supervisor Behavior" / "Starting the Supervisor," pages 169-178. See Table 8-1 (generic vs. specific code) and Figures 8-3 to 8-5.

# Verification Notes

- Definition source: Direct adaptation from p. 170 and p. 175.
- Confidence rationale: HIGH — supervisor is explicitly defined, with the `supervisor` module named and full callback-module examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
