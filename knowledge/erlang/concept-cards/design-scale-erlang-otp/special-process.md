---
# === CORE IDENTIFICATION ===
concept: Special Process
slug: special-process

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: special-processes
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Special Processes and Your Own Behaviors"
chapter_number: 9
pdf_page: 260
section: "Special Processes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "special processes"
  - "OTP-compliant process"
  - "sys-compliant process"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervision-tree
extends: []
related:
  - proc-lib
  - special-process-system-messages
  - sys-trace-events
  - custom-behaviour
contrasts_with:
  - otp-behaviors
  - supervisor-bridge

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a special process?"
  - "What is a process skeleton?"
  - "How do I trace and inspect an OTP process with the sys module?"
---

# Quick Definition

A special process is a process that follows OTP design principles — started with `proc_lib`, linked to its parent, and able to handle system messages — so it can be added to a supervision tree and packaged in an application without being a standard behavior.

# Core Definition

A process that can be added to an OTP supervision tree and packaged in an application is called a *special process* (Cesarini & Vinoski, p. 242). For a process to be considered a special process it must: be started using the `proc_lib` module and link to its parent; be able to handle system messages, system events, and shutdown requests; and return the module list if running dynamic modules (p. 242). It is optional but useful for the process to also handle debug flags and generate trace messages. Special processes give the flexibility of pure Erlang while retaining the advantages of OTP — they follow a subset of the OTP design principles that the standard behaviors follow.

# Prerequisites

- **Supervision tree** — A special process exists to be attached to an OTP supervision tree.

# Key Properties

1. Started with the `proc_lib` module (not raw `spawn`/`spawn_link`) and linked to its parent.
2. Handles system messages, system events, and shutdown requests.
3. Returns its module list when running dynamic modules.
4. Optionally handles debug flags and generates trace messages.
5. Can be added to a supervision tree and packaged in an application — it is OTP compliant.
6. Offers pure-Erlang flexibility (e.g. selective receive) that standard behaviors do not.

# Construction / Recognition

## To Construct/Create:
1. Start the process with `proc_lib:start_link/3` and call `proc_lib:init_ack/1`.
2. Link to the parent and store the parent pid.
3. In the main loop, handle `{system, From, Msg}` via `sys:handle_system_msg/6` and `{'EXIT', Parent, Reason}`.
4. Export `system_continue/3` and `system_terminate/4`.

## To Identify/Recognize:
1. The process is started via `proc_lib`.
2. Its loop matches `{system, From, Msg}` and `{'EXIT', Parent, Reason}`.
3. It exports `system_continue/3` and `system_terminate/4`.

# Context & Application

- **Typical contexts**: Attaching non-standard-behavior processes to OTP supervision trees.
- **Common applications**: Performance-sensitive processes; processes needing selective receive; legacy proof-of-concept code made OTP compliant.
- **Historical/stylistic notes**: The book's example is a mutex (mutual-exclusion FSM) — an FSM that needs selective receive, which `gen_fsm` does not allow, so it is written as a special process (p. 242).

# Examples

**Example 1** (pp. 242-249): The `mutex` module — a two-state (`free`/`busy`) FSM implemented as a special process with selective receive.

**Example 2** (p. 250): The mutex started as a dynamic child of a `mutex_sup` supervisor via a child specification.

## Worked Example

Starting and initializing a special process (pp. 244-245):

```erlang
start_link(Name, DbgOpts) ->
    proc_lib:start_link(?MODULE, init, [self(), Name, DbgOpts]).

init(Parent, Name, DbgOpts) ->
    register(Name, self()),
    process_flag(trap_exit, true),
    Debug = sys:debug_options(DbgOpts),
    proc_lib:init_ack({ok,self()}),
    free(Name, Parent, Debug).
```

# Relationships

## Builds Upon
- *(none)*

## Enables
- **Custom behaviour** — Splitting a special process into generic and specific modules turns it into a user-defined behavior.

## Related
- **proc_lib** — Special processes must be started with `proc_lib`.
- **Special process system messages** — Special processes must handle `{system, From, Msg}` messages.
- **Sys trace events** — Special processes optionally generate trace events via the `sys` module.

## Contrasts With
- **OTP behaviour** — A standard behavior is a prebuilt generic/specific split; a special process is hand-written but still OTP compliant.
- **Supervisor bridge** — A bridge connects non-OTP-compliant processes; a special process *is* OTP compliant.

# Common Errors

- **Error**: Starting a special process with raw `spawn`/`spawn_link` instead of `proc_lib`.
  **Correction**: Use `proc_lib` so process info (name, ancestors, initial call) is stored and crash reports are generated.

- **Error**: Attaching a process that does not handle system messages as a supervisor child.
  **Correction**: The only check the supervisor makes is that `{ok, Pid}` is returned; a non-compliant child fails silently — make the process a true special process.

# Common Confusions

- **Confusion**: Thinking a special process must be a standard OTP behavior.
  **Clarification**: A special process is *not* a standard behavior — it is hand-written pure Erlang that follows the same `sys`/`proc_lib` principles, making it OTP compliant.

# Source Reference

Chapter 9: Special Processes and Your Own Behaviors, "Special Processes," pages 241-243; see also Chapter 7, "Adding non-OTP-compliant processes," p. 195.

# Verification Notes

- Definition source: Direct adaptation from p. 242 ("In order for a process to be considered a special process...").
- Confidence rationale: HIGH — explicitly defined with a complete worked mutex example.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
