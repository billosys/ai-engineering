---
concept: Exceptions Across Processes
slug: exceptions-across-processes
category: fault-tolerance
subcategory: error-propagation
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Errors and Processes"
chapter_number: 12
pdf_page: null
section: "Old Exceptions, New Concepts"
extraction_confidence: high
aliases:
  - "exceptions and processes"
  - "uncaught exceptions in processes"
prerequisites:
  - process-link
  - exit-signal
  - trapping-exits
extends: []
related:
  - trapping-exits
contrasts_with: []
answers_questions:
  - "What distinguishes errors, exits, and throws across processes?"
  - "What happens to an uncaught exception in a linked process?"
---

# Exceptions Across Processes

## Quick Definition

When a process raises an uncaught throw, error, or exit, it dies and propagates an exit signal to linked processes. A process trapping exits receives this as an `{'EXIT', Pid, Reason}` message instead of dying.

## Core Definition

The chapter examines how the exception functions from Chapter 7 behave around processes. An uncaught exception always bubbles up into an exit: an uncaught `throw` "bubbles up into an error, which in turn bubbles up into an `EXIT`"; an `erlang:error/1` or a runtime error like `1/0` bubbles into an `'EXIT'` carrying a stack trace; an explicit `exit(reason)` exits directly. For each, the chapter contrasts the *untrapped result* (the linked process crashes or, for `normal`, nothing happens) with the *trapped result* (the linked process receives a `{'EXIT', Pid, Reason}` message). A normal exit, when trapped, arrives as `{'EXIT', Pid, normal}` — "this looks a bit like the result of `catch exit(normal)`, except a pid is added to the tuple to identify which process failed" (Hébert, ch. 12, "Old Exceptions, New Concepts").

## Prerequisites

- **Process link** — Exceptions propagate to linked processes
- **Exit signal** — An uncaught exception becomes an exit signal
- **Trapping exits** — Determines whether a linked process dies or receives a message

## Key Properties

1. An uncaught throw, error, or exit kills the process and propagates an exit signal
2. An uncaught `throw` bubbles into `{nocatch, Value}`, then into an `EXIT`
3. An uncaught error (e.g. `1/0`, `erlang:error/1`) bubbles into an `EXIT` with a stack trace
4. `exit(reason)` exits with `reason` directly — no stack trace
5. Untrapped: a linked process crashes (except for `normal`, which propagates nothing)
6. Trapped: the linked process receives `{'EXIT', Pid, Reason}` instead of dying
7. A trapped normal exit arrives as `{'EXIT', Pid, normal}` and is not a crash

## Construction / Recognition

## To Reason About Cross-Process Exceptions

1. Identify whether the source raises a throw, error, or exit
2. Note that any uncaught exception ends up as an exit signal
3. If the observer does not trap exits, expect it to crash on an abnormal reason
4. If the observer traps exits, expect an `{'EXIT', Pid, Reason}` message
5. Treat a `normal` reason as a non-crash in both cases

## Examples

> **Uncaught error** (ch. 12): `spawn_link(fun() -> 1/0 end)` — untrapped gives an exit value `{badarith, [...]}`; trapped gives `{'EXIT', Pid, {badarith, [...]}}`.
>
> **Uncaught throw** (ch. 12): `spawn_link(fun() -> throw(rocks) end)` — the throw "bubbles up into an error, which in turn bubbles up into an `EXIT`."
>
> **Normal exit trapped** (ch. 12): `spawn_link(fun() -> ok end)` trapped yields `{'EXIT', Pid, normal}`.

## Relationships

## Builds Upon

- **Process link** — The conduit for cross-process exception propagation
- **Exit signal** — What an uncaught exception becomes
- **Trapping exits** — Decides crash vs. message

## Common Errors

- **Error**: Expecting `try ... catch` to catch a linked process's failure
  **Correction**: A linked process's death cannot be caught with `try ... catch`; trap exits to receive it as a message

## Common Confusions

- **Confusion**: Thinking throws and errors behave differently across processes
  **Clarification**: Any uncaught exception — throw, error, or exit — ends up as an exit signal to linked processes

## Source Reference

Chapter 12, "Errors and Processes," section "Links," subsection "Old Exceptions, New Concepts" ("Exceptions and Traps").

## Verification Notes

- Untrapped/trapped result catalogue: directly from the ch. 12 table
- Confidence: HIGH — explicitly tabulated in the source
