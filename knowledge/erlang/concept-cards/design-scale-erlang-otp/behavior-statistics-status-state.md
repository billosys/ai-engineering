---
# === CORE IDENTIFICATION ===
concept: Behavior Statistics, Status, and State Inspection
slug: behavior-statistics-status-state

# === CLASSIFICATION ===
category: production-ops
subcategory: behavior-inspection
tier: intermediate

# === PROVENANCE ===
source: Designing for Scalability with Erlang/OTP
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Controlling OTP Behaviors"
chapter_number: 4
pdf_page: 123
section: "Statistics, Status, and State"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "sys:statistics"
  - "sys:get_status"
  - "sys:get_state"
  - "sys:replace_state"
  - state inspection
  - "format_status/2"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - the-sys-module
extends: []
related:
  - sys-tracing-and-logging
  - gen-server
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I trace and inspect an OTP process with the sys module?"
  - "How does the sys module relate to OTP behaviors?"
---

# Quick Definition

The `sys` module can collect runtime statistics on a behavior and report or replace its internal state and loop data — using `sys:statistics/2`, `sys:get_status/1`, `sys:get_state/1`, and `sys:replace_state/2` — without requiring any new code.

# Core Definition

The `sys` module "lets you collect general statistics on behaviors as well as retrieve information about their internal state, including loop data, without having to reinvent the wheel" (Cesarini & Vinoski, p. 123). `sys:statistics(Name, Flag)` turns statistics gathering on/off and (with `get`) returns tagged values such as `start_time`, `current_time`, `reductions`, `messages_in`, and `messages_out`. `sys:get_status(Name)` returns `{status, Pid, {module, Mod}, [ProcessDictionary, SysState, Parent, Dbg, Misc]}` (p. 124). `sys:get_state(Name)` returns just the loop data stored by the callback module, and `sys:replace_state(Name, ReplaceFun)` replaces the loop data of a running behavior — both intended only for debugging (pp. 125-126). A behavior can customize the `Misc`/`State` portion of the status by exporting the optional `format_status/2` callback.

# Prerequisites

- **The sys module** — These are `sys` functions; they inherit its synchronous-call semantics and optional timeout.

# Key Properties

1. `sys:statistics(Name, true|false)` toggles gathering; `sys:statistics(Name, get)` returns `start_time`, `current_time`, `reductions`, `messages_in`, `messages_out`.
2. `sys:get_status(Name)` returns `{status, Pid, {module, Mod}, [ProcDict, SysState, Parent, Dbg, Misc]}`.
3. `SysState` is `running` or `suspended`; `sys:suspend/1` and `sys:resume/1` toggle it (only system messages are handled while suspended).
4. `Misc` holds behavior-specific data; for generic servers the most important item is the loop data.
5. `sys:get_state/1` returns the loop data directly, avoiding the need to dig it out of `get_status/1`.
6. `sys:replace_state(Name, ReplaceFun)` passes the current loop data to a fun and stores the returned value.
7. The optional `format_status(Opt, [ProcDict, State])` callback customizes the displayed `{data, [{"State", ...}]}` field; `Opt` is `normal` for a `get_status` call or `terminate` for an error report.

# Construction / Recognition

## To Gather Statistics:
1. Call `sys:statistics(Name, true)`.
2. Exercise the behavior.
3. Call `sys:statistics(Name, get)` to read the tagged values.
4. Call `sys:statistics(Name, false)` to stop.

## To Inspect or Replace State:
1. Call `sys:get_state(Name)` to read the loop data, or `sys:get_status(Name)` for the full status tuple.
2. To modify, call `sys:replace_state(Name, fun(Old) -> New end)`.

# Context & Application

- **Typical contexts**: Live debugging and troubleshooting, especially mid-test with large state.
- **Common applications**: Reading reductions/message counts; examining loop data; surgically patching state without a restart.
- **Historical/stylistic notes**: The book calls `get_state/1`, `replace_state/2`, and `get_status/1` "incredibly helpful when debugging and troubleshooting live systems" (p. 127).

# Examples

**Example 1** (p. 123-124): `sys:statistics(frequency, get)` returns `{ok,[{start_time,...},{current_time,...},{reductions,33},{messages_in,1},{messages_out,0}]}`.

**Example 2** (pp. 125-126): `{Free, Alloc} = sys:get_state(frequency)` reads the loop data, then `sys:replace_state(frequency, fun(_) -> {[16,17], Alloc} end)` injects two new available frequencies so a subsequent `frequency:allocate()` returns `{ok,16}`.

# Relationships

## Builds Upon
- **The sys module** — Statistics, status, and state inspection are part of the `sys` facility set.

## Enables
- *(No downstream concepts in this scope.)*

## Related
- **Behavior tracing and logging** — Another `sys` facility; statistics flags can be enabled together with trace/log in the `Opts` field.
- **Generic server** — The loop data inspected is the `gen_server`'s loop data.

## Contrasts With
- *(None.)*

# Common Errors

- **Error**: Calling `sys:replace_state/2` with a fun that returns a wholly new value, discarding parts of a complex loop data structure.
  **Correction**: The replace fun receives the current loop data; use it to modify only the necessary portions and keep the rest.

# Common Confusions

- **Confusion**: Thinking `sys:get_state/1` and `sys:get_status/1` return the same thing.
  **Clarification**: `get_state/1` returns only the callback module's loop data; `get_status/1` returns the full status tuple (process dictionary, sys state, parent, debug flags, and misc).

# Source Reference

Chapter 4: Controlling OTP Behaviors, Section "Statistics, Status, and State," pages 123-126; recap on pages 125-127.

# Verification Notes

- Definition source: Direct quotes and shell examples from pp. 123-126.
- Confidence rationale: HIGH — explicit function signatures, return-value formats, and worked shell sessions in the source.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
