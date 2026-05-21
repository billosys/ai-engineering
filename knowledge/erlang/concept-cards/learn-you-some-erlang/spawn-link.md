---
concept: Spawn-Link
slug: spawn-link
category: fault-tolerance
subcategory: error-propagation
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Errors and Processes"
chapter_number: 12
pdf_page: null
section: "Links"
extraction_confidence: high
aliases:
  - "spawn_link"
  - "spawn_link/1"
  - "spawn_link/3"
prerequisites:
  - spawn
  - process-link
extends:
  - spawn
  - process-link
related:
  - process-monitor
contrasts_with:
  - spawn
answers_questions:
  - "What distinguishes spawn from spawn_link?"
  - "How do I atomically spawn and link a process?"
---

# Spawn-Link

## Quick Definition

`spawn_link` atomically creates a new process and links it to the caller in a single indivisible operation, avoiding the race where a process dies between a separate `spawn` and `link`.

## Core Definition

The chapter notes that `link(spawn(Function))` "happens in more than one step. In some cases, it is possible for a process to die before the link has been set up and then provoke unexpected behavior." For this reason `spawn_link/1-3` was added: it "takes the same arguments as `spawn/1-3`, creates a process, and links it as if `link/1` had been there, except it's all done as an atomic operation (the operations are combined as a single one, which can either fail or succeed, but nothing else)." It is "generally considered safer," and saves a set of parentheses (Hébert, ch. 12, "Links").

## Prerequisites

- **Spawn** — `spawn_link` is the spawn primitive plus linking
- **Process link** — It establishes a link as part of spawning

## Key Properties

1. Atomically spawns a process and links it to the caller
2. Takes the same arguments as `spawn/1-3` (fun, or module/function/args)
3. The combined operation either fully succeeds or fully fails — no in-between state
4. Eliminates the race window of separate `spawn` then `link`
5. Considered the safer default for creating dependent processes

## Construction / Recognition

## To Use Spawn-Link

1. Replace `link(spawn(fun() -> ... end))` with `spawn_link(fun() -> ... end)`
2. Or use `spawn_link(Module, Function, Args)` for the module/function form
3. Use it inside supervisor-like processes that must be linked to their children
4. Pair it with `process_flag(trap_exit, true)` if the caller must survive the child's death

## Examples

> **Atomic spawn-and-link** (ch. 12): `spawn_link(fun() -> linkmon:chain(3) end)` from a trapping process — the chain's death arrives as `{'EXIT', Pid, "chain dies here"}`.
>
> **Restarter** (ch. 12): `restarter/0` uses `Pid = spawn_link(?MODULE, critic, [])` so the supervisor is linked to the critic it must restart.

## Relationships

## Builds Upon

- **Spawn** — Provides the process creation
- **Process link** — Provides the linking

## Related

- **Process monitor** — `spawn_monitor` is the analogous atomic spawn-and-monitor primitive

## Contrasts With

- **Spawn** — `spawn` creates an isolated unlinked process; `spawn_link` links it atomically

## Common Errors

- **Error**: Continuing to use `link(spawn(...))` for dependent processes
  **Correction**: Use `spawn_link` so a process cannot die before the link is established

## Common Confusions

- **Confusion**: Thinking `spawn_link` only saves typing
  **Clarification**: Its real value is atomicity — closing the race window between spawn and link

## Source Reference

Chapter 12, "Errors and Processes," section "Links."

## Verification Notes

- Definition and atomicity: directly from ch. 12
- Restarter usage: from ch. 12 "Naming Processes"
- Confidence: HIGH — explicitly defined
