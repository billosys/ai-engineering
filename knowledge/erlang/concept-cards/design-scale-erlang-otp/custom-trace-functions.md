---
# === CORE IDENTIFICATION ===
concept: Custom Trace Functions
slug: custom-trace-functions

# === CLASSIFICATION ===
category: production-ops
subcategory: behavior-inspection
tier: advanced

# === PROVENANCE ===
source: Designing for Scalability with Erlang/OTP
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Controlling OTP Behaviors"
chapter_number: 4
pdf_page: 122
section: "Your Own Trace Functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - own trace functions
  - "sys:install"
  - trace triggers
  - debug functions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - system-message
  - sys-tracing-and-logging
extends:
  - sys-tracing-and-logging
related:
  - the-sys-module
contrasts_with:
  - sys-tracing-and-logging

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I trace and inspect an OTP process with the sys module?"
  - "How does the sys module relate to OTP behaviors?"
---

# Quick Definition

A custom trace function is a user-supplied fun, installed with `sys:install/2`, that is triggered on each behavior system event so you can pattern match events and run arbitrary diagnostic code — without modifying the behavior's source.

# Core Definition

Custom trace functions let you "implement your own fun that gets triggered in conjunction with a system event" (Cesarini & Vinoski, p. 122). You install the fun with `sys:install(Name, {Func, FuncState})` and remove it with `sys:remove(Name, Func)`. The fun takes three arguments: `FuncState` (the trace function's own state, passed between calls), the system message (which you can pattern match on), and `ProcData` (behavior-specific data — for a `gen_server` the registered name or pid, for a `gen_fsm` a tuple of name/pid plus the current state name). On each invocation the fun returns the new `FuncState`; returning the atom `done` is equivalent to calling `sys:remove/2` (pp. 122-124). Trace functions can generate custom printouts, turn on `dbg` or trace BIFs, enable selective logging, or run any code at all.

# Prerequisites

- **System message** — The trace fun pattern matches on system messages, so you must know their forms.
- **Behavior tracing and logging** — Custom trace functions extend the built-in tracing facility.

# Key Properties

1. Installed via `sys:install(Name, {Func, FuncState} [,Timeout])`; removed via `sys:remove(Name, Func [,Timeout])`.
2. The fun has arity 3: `fun(FuncState, SystemMessage, ProcData) -> NewFuncState`.
3. `FuncState` acts as a state variable carried between invocations (e.g., a counter).
4. `ProcData` is behavior-specific: name/pid for `gen_server`; `{name-or-pid, StateName}` for `gen_fsm`.
5. Returning the atom `done` from the fun disables it, equivalent to `sys:remove/2`.
6. Requires no change to the traced behavior's original code.

# Construction / Recognition

## To Install a Custom Trace Function:
1. Define a fun of arity 3 that pattern matches the system messages of interest.
2. Make non-matching events fall through a catch-all clause that returns `FuncState` unchanged.
3. Call `sys:install(Name, {Fun, InitialFuncState})`.
4. Exercise the behavior; observe your custom output.
5. Call `sys:remove(Name, Fun)` (or return `done`) to detach it.

# Context & Application

- **Typical contexts**: Diagnosing live systems that cannot be restarted or recompiled.
- **Common applications**: Counting specific events, raising custom warnings, enabling low-level traces conditionally, running diagnostics.
- **Historical/stylistic notes**: `io:format/2` inside the fun attaches to the traced behavior's group leader; on a remote shell the warnings won't be visible (p. 123, footnote 1).

# Examples

**Example 1** (pp. 122-124): A fun `F` counts every time a client is refused a frequency and prints a warning, installed with `sys:install(frequency, {F, 1})`:

```erlang
F = fun(Count, {out, {error, no_frequency}, Pid, _LoopData}, _ProcData) ->
        io:format("*DBG* Warning, Client ~p refused frequency! Count:~w~n",
                  [Pid, Count]),
        Count + 1;
       (Count, _, _) ->
        Count
    end.
```

## Worked Example

From the source (pp. 122-124):

1. Create fun `F` taking `Count`, the system message, and `ProcData`.
2. Install it with initial state 1: `sys:install(frequency, {F, 1})`.
3. Call `frequency:allocate/0` until frequencies run out.
4. Each refusal matches clause 1, prints a warning, and increments `Count`.
5. `sys:remove(frequency, F)` detaches the trace fun; later allocations no longer print.

# Relationships

## Builds Upon
- **Behavior tracing and logging** — Custom trace functions extend built-in `sys` tracing with arbitrary user logic.

## Enables
- *(No downstream concepts in this scope.)*

## Related
- **The sys module** — Installed and removed through `sys:install/2` and `sys:remove/2`.
- **System message** — The second argument of the trace fun.

## Contrasts With
- **Behavior tracing and logging** — Built-in tracing prints fixed `*DBG*` lines; a custom trace function lets you match events and execute any code you choose.

# Common Errors

- **Error**: Omitting the catch-all clause, so the fun crashes on system messages it didn't expect.
  **Correction**: Always include a final `(State, _, _) -> State` clause to ignore unmatched events.

# Common Confusions

- **Confusion**: Thinking the trace fun must modify the behavior's loop data.
  **Clarification**: The fun's `FuncState` is entirely separate from the behavior's loop data; it is the trace function's own private state.

# Source Reference

Chapter 4: Controlling OTP Behaviors, Section "Your Own Trace Functions," pages 122-124; recap on pages 125-127.

# Verification Notes

- Definition source: Direct quotes and worked example from pp. 122-124.
- Confidence rationale: HIGH — the source provides a full worked example with shell session and explains each fun argument.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
