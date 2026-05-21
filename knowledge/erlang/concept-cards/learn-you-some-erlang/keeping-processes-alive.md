---
concept: Keeping Processes Alive
slug: keeping-processes-alive
category: fault-tolerance
subcategory: restart-strategies
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Errors and Processes"
chapter_number: 12
pdf_page: null
section: "Naming Processes"
extraction_confidence: high
aliases:
  - "restarter"
  - "basic supervisor"
  - "process restart"
prerequisites:
  - trapping-exits
  - spawn-link
  - named-process
extends:
  - trapping-exits
related:
  - concurrent-application-design
contrasts_with: []
answers_questions:
  - "How do I keep a process alive when it crashes?"
  - "How do supervisors relate to the let-it-crash philosophy?"
---

# Keeping Processes Alive

## Quick Definition

Keeping processes alive means writing a "restarter" — a dedicated process that traps exits, spawn-links the worker it watches, and recreates it whenever it dies abnormally. It is the most basic form of a supervisor.

## Core Definition

After links, trapping exits, and naming are introduced, the chapter combines them to "write a basic 'supervisor' process whose only role is to restart the critic when it goes down." The restarter is its own process: it calls `process_flag(trap_exit, true)`, uses `spawn_link` to start the worker, registers the worker under a stable name, and then `receive`s exit messages. A `normal` or `shutdown` reason is treated as intentional and not restarted; any other reason triggers a recursive call that creates a fresh worker. This pattern — trap, link, watch, restart — is the conceptual seed of OTP supervisors (Hébert, ch. 12, "Naming Processes"; expanded into the `sup` module in ch. 13).

## Prerequisites

- **Trapping exits** — The restarter must trap exits to survive the worker's death
- **Spawn-link** — The restarter spawn-links the worker so it learns of crashes
- **Named process** — The worker is registered so callers always reach the current instance

## Key Properties

1. The restarter is a separate process dedicated to keeping a worker alive
2. It calls `process_flag(trap_exit, true)` so it receives exit messages instead of dying
3. It uses `spawn_link` to start the worker, establishing the link atomically
4. It registers the worker under a stable name so callers are insulated from pid changes
5. `normal` and `shutdown` exit reasons are intentional and not restarted
6. Any other exit reason causes the restarter to loop and recreate the worker
7. This is the most basic supervisor; OTP supervisors generalize it (deferred to ch. 17/18)

## Construction / Recognition

## To Write a Restarter

1. Define a `restarter/0` (or `init/1`) function as its own process
2. Call `process_flag(trap_exit, true)`
3. `Pid = spawn_link(?MODULE, worker, [])`
4. Register the worker: `register(worker_name, Pid)`
5. `receive` exit messages: ignore `{'EXIT', Pid, normal}` and `{'EXIT', Pid, shutdown}`; on `{'EXIT', Pid, _}` recurse to restart

## Examples

> **Critic restarter** (ch. 12): `restarter/0` traps exits, `spawn_link`s the critic, registers it as `critic`, and loops on abnormal exits to recreate it.
>
> **Generic sup module** (ch. 13): the `sup` module takes any module with a `start_link` function, traps exits, and "will restart the process it watches indefinitely, unless the supervisor itself is terminated with a shutdown exit signal."

## Relationships

## Builds Upon

- **Trapping exits** — Lets the restarter survive and observe the worker's death

## Related

- **Concurrent application design** — The reminder app uses a `sup` restarter as its supervisor

## Common Errors

- **Error**: Restarting on a `normal` or `shutdown` exit
  **Correction**: Match those reasons separately; they are intentional, not crashes
- **Error**: Not registering the restarted worker under a name
  **Correction**: Register it so callers reach the new instance after a restart

## Common Confusions

- **Confusion**: Thinking this hand-written restarter is production-grade supervision
  **Clarification**: It is the most basic form; real OTP supervisors are far more advanced (ch. 17/18)

## Source Reference

Chapter 12, "Errors and Processes," section "Naming Processes"; Chapter 13, "Designing a Concurrent Application," section "Adding Supervision."

## Verification Notes

- Definition and restarter code: directly from ch. 12 and ch. 13
- Confidence: HIGH — explicitly demonstrated in both chapters
