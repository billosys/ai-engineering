---
# === CORE IDENTIFICATION ===
concept: proc_lib Module
slug: proc-lib

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
section: "Starting Special Processes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "proc_lib"
  - "proc_lib:start_link"
  - "proc_lib:init_ack"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - special-process
extends: []
related:
  - special-process-system-messages
  - custom-behaviour
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a special process?"
  - "How do I trace and inspect an OTP process with the sys module?"
---

# Quick Definition

`proc_lib` is the OTP library module used to start special processes; instead of the raw `spawn`/`spawn_link` BIFs it stores process metadata, supports synchronous startup with an init-acknowledgment phase, and enables SASL crash reports.

# Core Definition

When starting special processes, you use the start and spawn functions defined in the `proc_lib` library module instead of Erlang's standard `spawn` and `spawn_link` BIFs (Cesarini & Vinoski, p. 243). The `proc_lib` functions store the process's name, identity, parent, ancestors, and initial function call in the process dictionary; if the process terminates abnormally, SASL crash reports are generated. The recommended start call is `proc_lib:start_link(Mod, Fun, Args)`, which synchronously spawns a process and waits for it to call `proc_lib:init_ack(Value)`; `Value` becomes the return value of `start_link`. There are also asynchronous `spawn`/`spawn_link`/`spawn_opt` variants and `proc_lib:hibernate/3` (pp. 243-247).

# Prerequisites

- **Special process** — `proc_lib` exists to start and manage special processes.

# Key Properties

1. Replaces raw `spawn`/`spawn_link` for special processes.
2. Stores process name, identity, parent, ancestors, and initial call.
3. Enables SASL crash reports on abnormal termination.
4. `start/3,4,5` and `start_link/3,4,5` start synchronously, waiting for `init_ack`.
5. `init_ack(Ret)` / `init_ack(Parent, Ret)` notifies the parent that startup succeeded; `Ret` becomes the start function's return value.
6. A `Time` argument bounds synchronous startup — without an `init_ack` in time, `{error, timeout}` is returned.
7. `spawn`/`spawn_link`/`spawn_opt` start asynchronously; `hibernate/3` hibernates while keeping logging/debugging working.

# Construction / Recognition

## To Construct/Create:
1. Start the process with `proc_lib:start_link(?MODULE, init, [self(), ...])`.
2. In `init`, set up state, then call `proc_lib:init_ack({ok, self()})`.
3. Enter the main loop.

## To Identify/Recognize:
1. Calls to `proc_lib:start_link/3,4,5` or `proc_lib:spawn*`.
2. A matching `proc_lib:init_ack/1,2` call inside `init`.

# Context & Application

- **Typical contexts**: Starting special processes and the foundation of all OTP behaviors.
- **Common applications**: Synchronous, deterministic process startup; hibernating special processes.
- **Historical/stylistic notes**: The book recommends synchronous starts so a startup error can be deterministically reproduced, avoiding race conditions (p. 246).

# Examples

**Example 1** (pp. 244-245): `mutex:start_link/2` calls `proc_lib:start_link(?MODULE, init, [self(), Name, DbgOpts])`; `init/3` calls `proc_lib:init_ack({ok,self()})`.

**Example 2** (p. 251): `proc_lib:hibernate(Mod, Fun, Args)` — hibernates a special process while keeping logging and debugging functional.

## Worked Example

The synchronous start/init-ack pair (pp. 244-245):

```erlang
start_link(Name, DbgOpts) ->
    proc_lib:start_link(?MODULE, init, [self(), Name, DbgOpts]).

init(Parent, Name, DbgOpts) ->
    register(Name, self()),
    process_flag(trap_exit, true),
    Debug = sys:debug_options(DbgOpts),
    proc_lib:init_ack({ok,self()}),   %% Value becomes start_link's return
    free(Name, Parent, Debug).
```

# Relationships

## Builds Upon
- *(none)*

## Enables
- **Custom behaviour** — User-defined behaviors are built on `sys` and `proc_lib`.

## Related
- **Special process system messages** — Together with `sys`, `proc_lib` underpins OTP-compliant process behavior.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Using `proc_lib:spawn` or `spawn_opt` without linking the child to the parent.
  **Correction**: Link the child — use `spawn_link`, `start_link`, or pass the `link` option in `SpawnOpts`.

- **Error**: Starting hundreds of special processes asynchronously and only then checking they started.
  **Correction**: Start synchronously where startup determinism matters, so race-condition startup errors are reproducible.

# Common Confusions

- **Confusion**: Thinking raw `spawn_link` is interchangeable with `proc_lib:start_link`.
  **Clarification**: Raw spawning stores no process metadata and generates no crash reports; `proc_lib` is required for OTP-compliant special processes.

# Source Reference

Chapter 9: Special Processes and Your Own Behaviors, "Starting Special Processes," pages 243-247; "Summing Up," Table 10-1, p. 261.

# Verification Notes

- Definition source: Direct adaptation from p. 243.
- Confidence rationale: HIGH — explicitly defined with the full API listing and worked example.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
