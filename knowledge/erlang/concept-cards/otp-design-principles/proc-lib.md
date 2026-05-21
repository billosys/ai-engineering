---
# === CORE IDENTIFICATION ===
concept: proc_lib
slug: proc-lib

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: otp-compliance
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "sys and proc_lib"
chapter_number: null
pdf_page: null
section: "Starting the Process"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "proc_lib module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervision-tree
extends: []
related:
  - special-process
  - sys-module
  - system-messages
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement a special process using proc_lib?"
  - "What must I know before writing a special process?"
---

# Quick Definition

`proc_lib` is an STDLIB module that provides functions for starting processes in a way that stores supervision-tree metadata (ancestors, initial call) and generates crash reports on abnormal termination.

# Core Definition

A function in the `proc_lib` module is to be used to start a special process. Several functions are available: `proc_lib:spawn_link/3,4` for asynchronous start and `proc_lib:start_link/3,4,5` for synchronous start. When a process is started through one of these functions, information necessary for a process within a supervision tree -- such as details on ancestors and the initial call -- is stored. If the process terminates with a reason other than `normal` or `shutdown`, a crash report is generated. For synchronous start, `proc_lib:start_link/3` does not return until `proc_lib:init_ack/1,2` or `proc_lib:init_fail/2,3` has been called, or the process has exited. (Source: spec_proc.md, "Starting the Process")

# Prerequisites

- **[Supervision Tree](/concept-cards/otp-design-principles/supervision-tree.md)** -- `proc_lib` stores supervision tree metadata required for OTP compliance.

# Key Properties

1. **Supervision metadata**: Stores ancestor information (`$ancestors`) and initial call (`$initial_call`) in the process dictionary.
2. **Crash reports**: Generates crash reports on abnormal termination (exit reason other than `normal` or `shutdown`).
3. **Synchronous start**: `proc_lib:start_link/3,4,5` blocks until `init_ack` or `init_fail` is called.
4. **Asynchronous start**: `proc_lib:spawn_link/3,4` returns immediately.
5. **Acknowledgement**: `proc_lib:init_ack(Parent, {ok, self()})` signals successful initialization to the parent.
6. **Part of STDLIB**: Belongs to the STDLIB application.

# Construction / Recognition

## To Construct/Create:
1. For synchronous start:

```erlang
start_link() ->
    proc_lib:start_link(Module, init, [self()]).
```

2. In the init function, acknowledge startup:

```erlang
init(Parent) ->
    register(Name, self()),
    ...
    proc_lib:init_ack(Parent, {ok, self()}),
    loop(...).
```

## To Identify/Recognize:
1. Look for calls to `proc_lib:start_link/3,4,5` or `proc_lib:spawn_link/3,4`.
2. Look for `proc_lib:init_ack/1,2` in init functions.

# Context & Application

`proc_lib` is the foundation for making any Erlang process compatible with OTP supervision trees. All standard behaviours (gen_server, gen_statem, gen_event, supervisor) use `proc_lib` internally. When implementing special processes or user-defined behaviours, `proc_lib` must be used explicitly to ensure proper supervision tree integration, crash reporting, and release handling support.

# Examples

**Example 1** (spec_proc.md, "Starting the Process"): Synchronous start with init_ack:

```erlang
start_link() ->
    proc_lib:start_link(ch4, init, [self()]).

init(Parent) ->
    register(ch4, self()),
    Chs = channels(),
    Deb = sys:debug_options([]),
    proc_lib:init_ack(Parent, {ok, self()}),
    loop(Chs, Parent, Deb).
```

**Example 2** (spec_proc.md, "Starting the Process"): The source notes that `proc_lib:start_link/3` takes a module name, function name, and argument list. It spawns a new process, establishes a link, and the new process executes the given function. The parent's pid is passed as an argument (obtained by `self()` in the call).

# Relationships

## Builds Upon
- **[Supervision Tree](/concept-cards/otp-design-principles/supervision-tree.md)** -- Stores metadata needed for supervision tree participation.

## Enables
- **[Special Process](/concept-cards/otp-design-principles/special-process.md)** -- proc_lib is required for implementing special processes.
- **[User-Defined Behaviour](/concept-cards/otp-design-principles/user-defined-behaviour.md)** -- User-defined behaviours also use proc_lib for process start.

## Related
- **[sys Module](/concept-cards/otp-design-principles/sys-module.md)** -- Together, sys and proc_lib enable OTP-compliant special processes.

## Contrasts With
- None directly; `proc_lib` is complementary to `sys`.

# Common Errors

- **Error**: Forgetting to call `proc_lib:init_ack/2` when using synchronous start.
  **Correction**: `proc_lib:start_link/3` blocks until `init_ack`, `init_fail`, or process exit. Without it, the caller hangs indefinitely.

- **Error**: Using plain `spawn_link` instead of `proc_lib:spawn_link`.
  **Correction**: Plain `spawn_link` does not store supervision tree metadata or generate crash reports. Use `proc_lib` functions for OTP compliance.

# Common Confusions

- **Confusion**: `proc_lib:start_link` and `proc_lib:spawn_link` are interchangeable.
  **Clarification**: `start_link` is synchronous (blocks until init_ack) while `spawn_link` is asynchronous (returns immediately). Use `start_link` when the parent needs to know the child is fully initialized.

# Source Reference

spec_proc.md, "Starting the Process" section. See also `m:proc_lib` in STDLIB.

# Verification Notes

- Definition source: Directly from spec_proc.md, "Starting the Process" section.
- Confidence rationale: High -- explicitly described with code examples.
- Uncertainties: None.
- Cross-reference status: References supervision-tree, special-process, sys-module, user-defined-behaviour.
