---
# === CORE IDENTIFICATION ===
concept: Process Tracing
slug: process-tracing

# === CLASSIFICATION ===
category: production-ops
subcategory: tracing
tier: advanced

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Profiling, Debugging, and Tracing"
chapter_number: 21
pdf_page: null
section: "Tracing Messages and Process Execution"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "trace BIFs"
  - "erlang:trace/3"
  - "erlang:trace_pattern/3"
  - "trace pattern"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - message-passing
extends: []
related:
  - dbg-trace-library
  - io-format-debugging
contrasts_with:
  - erlang-debugger

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is process tracing in Erlang?"
  - "How do the Erlang trace BIFs work?"
  - "How do I observe message passing and function calls in a running process?"
---

# Quick Definition

Process tracing observes the behavior of a running process — its function calls, return values, and message passing — without modifying or recompiling the code. At the low level it is set up with the BIFs `erlang:trace/3` and `erlang:trace_pattern/3`.

# Core Definition

"You can always trace a process without having to compile your code in a special way. Tracing a process (or processes) provides a powerful way of understanding how your system behaves and can be used to test complex systems without modifying the code" ("Tracing Messages and Process Execution"). This is especially useful in embedded systems or where the code cannot be modified. Two BIFs are central:

- `erlang:trace(PidSpec, How, FlagList)` — starts (or stops) tracing. `PidSpec` says what to trace, `How` is a boolean turning tracing on/off, and `FlagList` governs what is traced (function calls, messages sent, garbage collections, etc.). After calling it, the calling process is sent trace messages when trace events occur.
- `erlang:trace_pattern(MFA, MatchSpec, FlagList)` — sets up a trace pattern; if the pattern matches, the requested actions are performed. `MFA` is a `{Module, Function, Args}` tuple, `MatchSpec` is tested each time the function is entered, and `FlagList` says what to do when the conditions are satisfied.

Writing match specifications by hand is complicated, so higher-level libraries exist.

# Prerequisites

- **Process** — Tracing observes processes and their scheduling.
- **Message passing** — A key thing tracing reveals is the messages flowing between processes.

# Key Properties

1. Works on any process without special compilation of the code.
2. `erlang:trace/3` says "monitor this process; send me messages when something interesting happens".
3. `erlang:trace_pattern/3` defines what counts as "interesting".
4. Trace messages are delivered to the process that called `erlang:trace/3`.
5. Trace flags can select function calls, messages sent/received, garbage collections, process events, etc.
6. Match specifications are hard to write by hand; libraries simplify them.
7. Tracing reveals the dynamic behavior of a system, complementing the static view from reading code.

# Construction / Recognition

## To Set Up Low-Level Tracing:
1. Decide what to trace and call `erlang:trace_pattern({Mod,'_','_'}, MatchSpec, FlagList)` to define the pattern.
2. Spawn (or identify) the process that will run the code.
3. Call `erlang:trace(Pid, true, FlagList)` (e.g. `[call, procs]`) to start tracing it.
4. Receive the resulting `{trace, ...}` messages in a loop and display them.

## To Recognize:
1. Look for `erlang:trace/3` and `erlang:trace_pattern/3` calls and a loop receiving `{trace, ...}` messages.

# Context & Application

Process tracing is the way to understand a running system's dynamic behavior.

- **Typical contexts**: Diagnosing complex or embedded systems where you cannot change the code.
- **Common applications**: Tracing all function calls and return values in a module; observing message flow.
- **Historical/stylistic notes**: For fine-grained control, write custom tracing on the BIFs; for quick experiments, use the trace libraries.

# Examples

**Example 1** ("Tracing Messages and Process Execution"): The `trace_module1/2` helper sets a trace pattern for all functions of `Mod` and starts tracing.

```erlang
erlang:trace_pattern({Mod, '_','_'},
                     [{'_',[],[{return_trace}]}],
                     [local]),
...
erlang:trace(Pid, true, [call,procs]),
```

**Example 2** ("Tracing Messages and Process Execution"): The trace loop receives `{trace,_,call,X}` and `{trace,_,return_from,Call,Ret}` messages and prints the calls and return values — producing fine-grained output such as `Call: {tracer_test,fib,[4]}` and `Return From: {tracer_test,fib,1} => 5`.

# Relationships

## Builds Upon
- **Process** — Tracing is fundamentally process observation.

## Enables
- **dbg trace library** — `dbg` is a higher-level interface built on these trace BIFs.

## Related
- **Message passing** — Tracing can observe inter-process messages.
- **io:format debugging** — Tracing observes behavior without code changes; io:format requires editing the code.

## Contrasts With
- **The Erlang debugger** — The debugger is interactive (breakpoints, stepping); tracing passively records events of a running, unmodified system.

# Common Errors

- **Error**: Writing match specifications by hand for non-trivial traces.
  **Correction**: Match specs are complicated; use the trace libraries (e.g. `dbg`, `ms_transform`) that generate them.

- **Error**: Forgetting that trace messages go to the process that called `erlang:trace/3`.
  **Correction**: Ensure that process has a receive loop to consume `{trace, ...}` messages.

# Common Confusions

- **Confusion**: Thinking tracing requires special compilation like the debugger.
  **Clarification**: A process can always be traced without compiling the code in any special way.

# Source Reference

Chapter 21: "Profiling, Debugging, and Tracing", section "Tracing Messages and Process Execution". See footnote 31 for the `ms_transform` documentation.

# Verification Notes

- Definition source: Direct quotes from "Tracing Messages and Process Execution".
- Confidence rationale: HIGH — the two trace BIFs and their roles are explicitly defined, with a full worked tracer.
- Uncertainties: Match-specification syntax is deliberately not detailed in the book.
- Cross-reference status: Verified against planned cards; `process` and `message-passing` are canonical shared slugs.
- Re-extraction notes: Fresh extraction — no pre-existing card.
