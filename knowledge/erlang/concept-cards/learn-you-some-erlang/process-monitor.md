---
concept: Process Monitor
slug: process-monitor
category: fault-tolerance
subcategory: error-propagation
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Errors and Processes"
chapter_number: 12
pdf_page: null
section: "Monitors"
extraction_confidence: high
aliases:
  - "monitor"
  - "erlang:monitor/2"
  - "spawn_monitor"
prerequisites:
  - process
extends: []
related:
  - process-link
  - exit-signal
contrasts_with:
  - process-link
answers_questions:
  - "What is a monitor?"
  - "How do links relate to monitors?"
  - "What distinguishes a link from a monitor?"
---

# Process Monitor

## Quick Definition

A monitor is a unidirectional, stackable observation of one process by another. When the watched process dies, the watcher receives a `{'DOWN', Ref, process, Pid, Reason}` message — without dying itself.

## Core Definition

Monitors are "a special type of link, with two differences": they are *unidirectional*, and "you can have many of them between two processes (they *stack* and they have an *identity*)." Set up with `erlang:monitor(process, Pid)`, where the first argument is always the atom `process`. Every time a monitored process goes down, the watcher receives `{'DOWN', MonitorReference, process, Pid, Reason}`. The reference uniquely identifies each monitor, enabling `demonitor/1,2` to remove a specific one. Unlike links, monitors do not kill the watcher. They are ideal for libraries, because a library can set up and tear down its own monitors without disturbing unrelated links. There is an atomic `spawn_monitor/1-3` (Hébert, ch. 12, "Monitors").

## Prerequisites

- **Process** — A monitor observes one process from another

## Key Properties

1. A monitor is unidirectional — only the watcher is notified
2. Monitors stack — many can exist between the same two processes, each with a unique reference
3. Created with `erlang:monitor(process, Pid)`, returning a reference
4. The watcher receives `{'DOWN', Ref, process, Pid, Reason}` when the watched process dies
5. The watcher does not die — monitoring never kills
6. Removed individually with `demonitor/1` or `demonitor/2`; `demonitor/2` options are `info` and `flush`
7. `spawn_monitor/1-3` atomically spawns and monitors a process
8. Best suited to library code that must observe processes without organizational coupling

## Construction / Recognition

## To Use a Monitor

1. Set up: `Ref = erlang:monitor(process, Pid)`
2. Add a `receive` clause for `{'DOWN', Ref, process, Pid, Reason}`
3. Remove it when no longer needed: `erlang:demonitor(Ref)`
4. Use `demonitor(Ref, [flush])` to also purge any pending `DOWN` message
5. To spawn and monitor atomically, use `spawn_monitor/1-3`

## Examples

> **Basic monitor** (ch. 12): `erlang:monitor(process, spawn(fun() -> timer:sleep(500) end))`; later `flush()` shows `{'DOWN',#Ref<...>,process,<0.63.0>,normal}`.
>
> **spawn_monitor and demonitor** (ch. 12): `{Pid, Ref} = spawn_monitor(fun() -> receive _ -> exit(boom) end end)`, then `erlang:demonitor(Ref)` removes it before the crash, leaving no trace.
>
> **Monitoring in an interface function** (ch. 13): `event:cancel/1` monitors the event process so it returns `ok` even if the process is already dead.

## Relationships

## Related

- **Process link** — The bidirectional counterpart; monitors are "a special type of link"
- **Exit signal** — Links propagate exit signals; monitors instead deliver `DOWN` messages

## Contrasts With

- **Process link** — Links are bidirectional and non-stacking and kill the partner; monitors are unidirectional, stackable, identified by a reference, and never kill the watcher

## Common Errors

- **Error**: Using a link in library code to check liveness, then unlinking
  **Correction**: Use a monitor — `unlink` would tear down unrelated links since links do not stack
- **Error**: Leaving a `DOWN` message in the mailbox after demonitoring
  **Correction**: Use `demonitor(Ref, [flush])` to purge a possibly already-sent `DOWN` message

## Common Confusions

- **Confusion**: Thinking a monitor can kill the watching process
  **Clarification**: Monitors only deliver a `DOWN` message; they never kill the watcher
- **Confusion**: Believing one monitor exists per process pair
  **Clarification**: Monitors stack — each `erlang:monitor/2` call creates a separately-referenced monitor

## Source Reference

Chapter 12, "Errors and Processes," section "Monitors."

## Verification Notes

- Definition, unidirectionality, stacking, DOWN message: directly from ch. 12
- `event:cancel/1` use: cross-referenced from ch. 13
- Confidence: HIGH — explicitly defined with examples
