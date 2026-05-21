---
# === CORE IDENTIFICATION ===
concept: Behavior Tracing and Logging
slug: sys-tracing-and-logging

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
pdf_page: 120
section: "Tracing and Logging"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "sys:trace"
  - "sys:log"
  - "sys:log_to_file"
  - behavior tracing
  - built-in tracing

# === TYPED RELATIONSHIPS ===
prerequisites:
  - the-sys-module
extends: []
related:
  - system-message
  - custom-trace-functions
contrasts_with:
  - custom-trace-functions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I trace and inspect an OTP process with the sys module?"
  - "How does the sys module relate to OTP behaviors?"
---

# Quick Definition

Built-in tracing and logging let you generate printouts of a behavior's system events — messages and state changes — either streamed to the shell, stored in the process loop, or piped to a file, all via the `sys` module without touching the behavior's code.

# Core Definition

Tracing and logging are the `sys` module facilities for capturing system events from a running behavior. `sys:trace/2` turns trace flags on or off; when on, the behavior generates "printouts of system events, including messages and state changes" piped to the shell (Cesarini & Vinoski, p. 120-121). `sys:log/2` instead stores the events inside the server loop, where they can be displayed with the `print` flag or retrieved as an Erlang data structure with the `get` flag (p. 121). By default the last 10 events are stored; passing `{true, Int}` overrides this count. For large volumes or long-running debugging, `sys:log_to_file/2` pipes events in textual form to a named file (p. 121).

# Prerequisites

- **The sys module** — Tracing and logging are functions of the `sys` module and inherit its synchronous-call semantics and optional timeout.

# Key Properties

1. `sys:trace(Name, TraceFlag [,Timeout])` streams events to the shell when `TraceFlag` is `true`.
2. `sys:log(Name, LogFlag [,Timeout])` stores events in the server loop; flags include `true`, `false`, `print`, `get`, and `{true, Int}`.
3. Default log buffer holds 10 events; `{true, Int}` sets a new non-negative integer count.
4. `sys:log_to_file(Name, FileFlag [,Timeout])` writes events in textual format; `FileFlag` is a filename string or `false` to turn it off.
5. `*DBG*` is the prefix of trace printouts in the shell.
6. Tracing, logging, and statistics can be enabled at start time via `[{debug, DbgList}]` in the behavior's `Opts` field.

# Construction / Recognition

## To Trace a Behavior:
1. Start the behavior (e.g., `frequency:start()`).
2. Call `sys:trace(frequency, true)`.
3. Exercise the behavior; observe `*DBG*` lines in the shell.
4. Call `sys:trace(frequency, false)` to stop.

## To Log and Retrieve Events:
1. Call `sys:log(frequency, true)` to begin storing events.
2. Exercise the behavior.
3. Call `sys:log(frequency, print)` to display, or `sys:log(frequency, get)` to retrieve as a term.
4. Call `sys:log(frequency, false)` to stop.

# Context & Application

- **Typical contexts**: Interactive shell debugging and live production troubleshooting.
- **Common applications**: Watching messages and state transitions; capturing a bounded event history; archiving long debug runs to disk.
- **Historical/stylistic notes**: The authors recommend starting with built-in tracing and logging before reaching for lower-level tools (p. 127).

# Examples

**Example 1** (p. 120-121): With `sys:trace(frequency, true)` on, `frequency:allocate()` prints `*DBG* frequency got call {allocate,<0.33.0>} from <0.33.0>` and a `*DBG* ... new state ...` line.

**Example 2** (p. 121): `sys:log(frequency, get)` returns a list of `{in, ...}` and `{out, ...}` and `{noreply, ...}` system events wrapped with module and fun references.

# Relationships

## Builds Upon
- **The sys module** — Tracing and logging are part of the `sys` module's facility set.

## Enables
- **system-message** — The events captured by tracing and logging take the form of system messages.

## Related
- **custom-trace-functions** — Custom trace funs are installed alongside built-in tracing.

## Contrasts With
- **custom-trace-functions** — Built-in tracing produces fixed `*DBG*` printouts; custom trace functions let you pattern match events and run arbitrary code.

# Common Errors

- **Error**: Leaving `sys:log/2` on for a long debugging session and losing early events because only 10 are kept.
  **Correction**: Pass `{true, Int}` to enlarge the buffer, or use `sys:log_to_file/2` for large volumes or long runs.

# Common Confusions

- **Confusion**: Thinking `sys:trace` and `sys:log` do the same thing.
  **Clarification**: `trace` streams events to the shell immediately; `log` stores them in the server loop for later retrieval via `print` or `get`.

# Source Reference

Chapter 4: Controlling OTP Behaviors, Section "Tracing and Logging," pages 120-121; recap on pages 125-127.

# Verification Notes

- Definition source: Direct quotes and paraphrase from pp. 120-121.
- Confidence rationale: HIGH — explicit shell examples and function signatures are given in the source.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
