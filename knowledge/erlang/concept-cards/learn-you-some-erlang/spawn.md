---
concept: Spawn
slug: spawn
category: processes-concurrency
subcategory: concurrency-primitives
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "The Hitchhiker's Guide to Concurrency"
chapter_number: 10
pdf_page: null
section: "Spawning Processes"
extraction_confidence: high
aliases:
  - "spawn/1"
  - "spawn/3"
  - "process creation"
prerequisites:
  - process
extends: []
related:
  - message-passing
  - receive-expression
  - spawn-link
contrasts_with:
  - spawn-link
answers_questions:
  - "How do I spawn a process and send it messages?"
  - "What distinguishes spawn from spawn_link?"
---

# Spawn

## Quick Definition

`spawn` is the primitive that creates a new process to run a function, returning the new process's pid. It comes in `spawn/1` (taking a fun) and `spawn/3` (taking module, function, and arguments).

## Core Definition

`spawn` is the first of the three concurrency primitives. `spawn/1` "takes a single function and runs it," returning a pid — "an arbitrary value representing any process that exists (or might have existed)." Since processes return nothing, only the pid is visible. `spawn/3` is an alternative form: "rather than taking a single function, `spawn/3` takes the module, function, and its arguments as its own arguments." The processes created run concurrently, so the ordering of their effects is not guaranteed (Hébert, ch. 10, "Spawning Processes").

## Prerequisites

- **Process** — `spawn` exists to create processes; you must understand what a process is

## Key Properties

1. `spawn/1` takes a zero-argument fun and runs it in a new process
2. `spawn/3` takes a module name, function name, and argument list
3. Returns the new process's pid immediately
4. The spawning process and the new process run concurrently
5. The new process is fully isolated — no shared memory, no link by default
6. The function's return value is discarded; communicate via messages instead

## Construction / Recognition

## To Spawn a Process

1. With a fun: `Pid = spawn(fun() -> my_loop() end)`
2. With module/function/args: `Pid = spawn(my_module, my_func, [Arg1, Arg2])`
3. Capture the returned pid to address messages to the new process
4. If you need the new process to stay alive, have its function loop with `receive`

## Examples

> **spawn/1** (ch. 10): `F = fun() -> 2 + 2 end.` then `spawn(F).` → `<0.44.0>`.
>
> **spawn/3** (ch. 10): `Dolphin = spawn(dolphins, dolphin1, []).` starts the dolphin process by module, function, and arguments.
>
> **Spawning in a list comprehension** (ch. 10): `[spawn(fun() -> G(X) end) || X <- lists:seq(1,10)]` starts ten processes at once.

## Relationships

## Builds Upon

- **Process** — `spawn` is the means of creating one

## Related

- **Message passing** — After spawning, you communicate with the process via messages
- **Receive expression** — The spawned function typically loops on `receive`
- **Spawn-link** — The atomic spawn-and-link variant

## Contrasts With

- **Spawn-link** — `spawn` creates an unlinked, isolated process; `spawn_link` atomically links it to the caller so crashes propagate

## Common Errors

- **Error**: Using `link(spawn(...))` and assuming it is atomic
  **Correction**: `spawn` then `link` happen in two steps; the process can die in between — use `spawn_link` for atomicity
- **Error**: Expecting `spawn` to return the function result
  **Correction**: `spawn` returns only a pid; processes return nothing

## Common Confusions

- **Confusion**: Thinking `spawn/1` and `spawn/3` differ in behavior
  **Clarification**: They only differ in how the function is specified — fun vs. module/function/args; the resulting process is the same

## Source Reference

Chapter 10, "The Hitchhiker's Guide to Concurrency," section "So Long and Thanks for All the Fish!", subsection "Spawning Processes."

## Verification Notes

- Definitions of spawn/1 and spawn/3: directly from ch. 10
- spawn_link contrast: cross-referenced from ch. 12
- Confidence: HIGH — explicitly defined with examples
