---
# === CORE IDENTIFICATION ===
concept: The Erlang Debugger
slug: erlang-debugger

# === CLASSIFICATION ===
category: production-ops
subcategory: debugging
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Profiling, Debugging, and Tracing"
chapter_number: 21
pdf_page: null
section: "The Erlang Debugger"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - debugger
  - "debugger/interpreter interface"
  - "module i"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
extends: []
related:
  - io-format-debugging
  - process-tracing
contrasts_with:
  - io-format-debugging

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Erlang debugger?"
  - "How do I start the Erlang debugger?"
  - "How do I set breakpoints in Erlang code?"
---

# Quick Definition

The Erlang debugger is a graphical tool in the standard distribution that lets you set breakpoints, single-step code, and inspect variables. It can spawn a separate debug window for each process being debugged.

# Core Definition

"The standard Erlang distribution contains a debugger" ("The Erlang Debugger"). Once started it is easy to use — "You can inspect variables, single-step the code, set breakpoints, and so on." Because you often debug several processes, the debugger can spawn copies of itself, giving one debug window per process. The only tricky part is starting it: code must be compiled with `debug_info`, and a short sequence of commands from the module `i` (the debugger/interpreter interface) sets it up:

- `im()` — start a new graphical monitor (the debugger's main window) showing the state of all monitored processes.
- `ii(Mod)` — interpret the code in module `Mod`.
- `iaa([init])` — attach the debugger to any process executing interpreted code when that process starts.

The commands without a module prefix (`ii/1`, `iaa/1`, etc.) are exported from module `i` and are accessible directly from the shell.

# Prerequisites

- **Process** — The debugger monitors processes and can open a separate window per debugged process.

# Key Properties

1. Ships with the standard Erlang distribution; graphical.
2. Supports breakpoints, single-stepping, and variable inspection.
3. Can spawn one debug window per debugged process.
4. Requires modules to be compiled with `debug_info` (e.g. `c(lib_misc, [debug_info])`).
5. Driven by the module `i`; its shell shortcuts (`im`, `ii`, `iaa`, ...) need no module prefix.
6. `im()` opens the main monitor window; `ii(Mod)` interprets a module; `iaa([init])` auto-attaches to interpreted processes.

# Construction / Recognition

## To Start the Debugger:
1. Recompile the target module with debug info: `c(lib_misc, [debug_info])`.
2. Call `im()` to open the graphical monitor.
3. Call `ii(Mod)` to interpret the module(s) of interest.
4. Call `iaa([init])` to auto-attach to interpreted processes.
5. Run the code; set breakpoints and inspect/step in the debug window.

## To Recognize:
1. Shell use of `im()`, `ii/1`, `iaa/1`, or modules compiled with `debug_info` for debugging.

# Context & Application

The debugger is the option when print statements are not enough.

- **Typical contexts**: Inspecting variable values, stepping through logic, debugging multiple processes at once.
- **Common applications**: Setting a breakpoint and single-stepping interpreted code.
- **Historical/stylistic notes**: The debugger reference manual and the `i` module man page are recommended for serious users.

# Examples

**Example 1** ("The Erlang Debugger"): Starting the debugger for `lib_misc`.

```erlang
1> c(lib_misc, [debug_info]).
{ok, lib_misc}
2> im().            %% A window pops up
<0.42.0>
3> ii(lib_misc).
{module,lib_misc}
4> iaa([init]).
true.
```

# Relationships

## Builds Upon
- **Process** — Debugging is organized per process.

## Enables
- (No card depends on this concept.)

## Related
- **io:format debugging** — A simpler alternative debugging technique.
- **Process tracing** — Another way to observe a running system.

## Contrasts With
- **io:format debugging** — The debugger sets breakpoints and steps without editing code; io:format debugging requires inserting print statements into the source.

# Common Errors

- **Error**: Trying to interpret a module that was not compiled with `debug_info`.
  **Correction**: Recompile with `debug_info` (e.g. `c(Mod, [debug_info])`) before calling `ii/1`.

- **Error**: Prefixing the interface functions with a module name (e.g. `i:im()`).
  **Correction**: `im/0`, `ii/1`, `iaa/1` are exported from module `i` and are usable directly in the shell without the prefix.

# Common Confusions

- **Confusion**: Thinking the debugger is the primary way to debug Erlang.
  **Clarification**: Print statements are by far the most common technique; the debugger is one option among several.

# Source Reference

Chapter 21: "Profiling, Debugging, and Tracing", section "The Erlang Debugger". See Figure 1 (Debugger initial window).

# Verification Notes

- Definition source: Direct quotes from "The Erlang Debugger".
- Confidence rationale: HIGH — the startup sequence and the `i`-module commands are explicitly described with a worked shell session.
- Uncertainties: The book intentionally keeps the debugger treatment brief, pointing to the reference manual.
- Cross-reference status: Verified against planned cards; `process` is a canonical shared slug.
- Re-extraction notes: Fresh extraction — no pre-existing card.
