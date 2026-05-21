---
concept: Process
slug: process
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
  - "Erlang process"
  - "lightweight process"
  - "actor"
prerequisites: []
extends: []
related:
  - spawn
  - message-passing
  - process-mailbox
contrasts_with: []
answers_questions:
  - "What is a process?"
  - "What must I know before writing concurrent programs?"
---

# Process

## Quick Definition

An Erlang process is a lightweight, isolated, VM-managed actor that runs a function and then disappears. Processes share no memory and communicate only by asynchronous message passing.

## Core Definition

The chapter explains that a process "is actually nothing but a function. A process runs a function, and once it's finished, it disappears." Technically it also has hidden state such as a mailbox. Processes are *lightweight*: each takes about 300 words of memory and can be created in microseconds — "not something currently doable on major operating systems." The Erlang VM, not the OS, handles processes, which let the implementers keep control of optimization and reliability. Processes share no memory; they communicate by copying data in messages. Each process is identified by a *process identifier* (pid), an arbitrary value used as an address. Processes do not return values — only their pid is visible to the spawner (Hébert, ch. 10, "Concurrency Implementation," "Spawning Processes").

## Prerequisites

This is a foundational concept with no prerequisites within this source.

## Key Properties

1. A process is a function plus hidden state (notably a mailbox)
2. Lightweight: ~300 words of memory, created in microseconds
3. Managed by the Erlang VM, not the operating system
4. Shares no memory with other processes (shared-nothing)
5. Communicates only by asynchronous message passing, with data copied
6. Identified by a pid, used as an address for messages
7. Returns no value; once its function finishes, the process disappears
8. The VM runs one scheduler thread per core, each with a run queue, doing automatic load balancing

## Construction / Recognition

## To Create and Use a Process

1. Define the function the process should run
2. Spawn it with `spawn/1` or `spawn/3`, receiving a pid
3. Send it messages addressed by its pid
4. Use `self/0` to get the current process's own pid
5. Keep the process alive by having its function loop (tail-recursive `receive`)

## Examples

> **A process is a function** (ch. 10): `F = fun() -> 2 + 2 end.`, then `spawn(F).` returns a pid like `<0.44.0>`.
>
> **The shell is a process** (ch. 10): `self()` returns the shell's pid; `exit(self())` kills and restarts it, and `self()` then returns a new pid.
>
> **Many processes** (ch. 10): `[spawn(fun() -> G(X) end) || X <- lists:seq(1,10)]` starts 10 processes whose output order is nondeterministic.

## Relationships

## Related

- **Spawn** — The primitive that creates a process
- **Message passing** — How processes communicate
- **Process mailbox** — The per-process queue where incoming messages wait

## Common Errors

- **Error**: Expecting `spawn` to return the function's result
  **Correction**: Processes return nothing; `spawn` returns only a pid — communicate results via messages
- **Error**: Letting a process finish its function when you need it to keep serving
  **Correction**: Loop with a tail-recursive `receive` so the process stays alive

## Common Confusions

- **Confusion**: Equating Erlang processes with OS processes or threads
  **Clarification**: Erlang processes are VM-managed, far lighter (~300 words), and share no memory
- **Confusion**: Assuming spawned processes run in a predictable order
  **Clarification**: The VM schedules them; ordering of independent processes is not guaranteed

## Source Reference

Chapter 10, "The Hitchhiker's Guide to Concurrency," sections "Concurrency Implementation" and "Spawning Processes."

## Verification Notes

- Definition, memory size, VM scheduling: directly from ch. 10
- Confidence: HIGH — explicitly defined with examples
