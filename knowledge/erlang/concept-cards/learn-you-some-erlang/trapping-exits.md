---
concept: Trapping Exits
slug: trapping-exits
category: fault-tolerance
subcategory: error-propagation
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Errors and Processes"
chapter_number: 12
pdf_page: null
section: "It's a Trap!"
extraction_confidence: high
aliases:
  - "trap_exit"
  - "system process"
  - "process_flag(trap_exit, true)"
prerequisites:
  - process-link
  - exit-signal
extends: []
related:
  - keeping-processes-alive
  - named-process
contrasts_with:
  - process-monitor
answers_questions:
  - "How do I make a process survive a linked process's death?"
  - "How do supervisors relate to the let-it-crash philosophy?"
---

# Trapping Exits

## Quick Definition

Trapping exits turns a process into a system process that converts incoming exit signals into ordinary `{'EXIT', Pid, Reason}` messages instead of dying. It is enabled with `process_flag(trap_exit, true)`.

## Core Definition

Links alone can kill processes together; what is missing is *restarting*. To restart a dead process you must first know it died. This is done by adding a layer on top of links called *system processes*. "System processes are basically normal processes, except they can convert exit signals to regular messages. This is done by calling `process_flag(trap_exit, true)` in a running process." Once trapping exits, instead of dying when a linked process crashes, the process receives `{'EXIT', Pid, Reason}` in its mailbox and can act on it. This mechanism "allows for a quick restart of processes" — it is what lets you write a process whose only job is to watch for deaths and restart what failed. The `kill` reason remains untrappable as a deliberate exception (Hébert, ch. 12, "It's a Trap!").

## Prerequisites

- **Process link** — Trapping exits handles signals that arrive via links
- **Exit signal** — The signals being converted into messages

## Key Properties

1. Enabled by `process_flag(trap_exit, true)` in the running process
2. A process trapping exits is called a *system process*
3. Exit signals from linked processes become `{'EXIT', FromPid, Reason}` messages in the mailbox
4. The trapping process survives instead of dying, and can react to the death
5. This is the basis of restarting failed processes (a basic supervisor)
6. The `kill` reason is untrappable — a hard kill always succeeds
7. A normal exit, when trapped, arrives as `{'EXIT', Pid, normal}`

## Construction / Recognition

## To Trap Exits

1. Call `process_flag(trap_exit, true)` early in the process's function
2. Link to (or spawn_link) the processes whose deaths you want to observe
3. Add `receive` clauses matching `{'EXIT', Pid, Reason}`
4. Decide per reason whether to restart, ignore, or stop
5. Treat `normal` and `shutdown` as non-crashes; restart on other reasons

## Examples

> **Chain example trapping** (ch. 12): after `process_flag(trap_exit, true)`, `spawn_link(fun() -> linkmon:chain(3) end)` lets the shell receive `{'EXIT',<0.49.0>,"chain dies here"}` instead of crashing.
>
> **Restarter** (ch. 12): `restarter/0` calls `process_flag(trap_exit, true)`, spawn_links the critic, and on `{'EXIT', Pid, _}` (an abnormal reason) loops to recreate it; `normal` and `shutdown` are treated as non-crashes.

## Relationships

## Builds Upon

- **Process link** — Trapping handles linked-process death signals
- **Exit signal** — The signals converted into messages

## Related

- **Keeping processes alive** — Trapping exits is the foundation of restart loops
- **Named process** — Restarters typically register the restarted process under a stable name

## Contrasts With

- **Process monitor** — Monitors observe deaths without linking or trapping; trapping requires a link and changes process behavior globally

## Common Errors

- **Error**: Treating every trapped `{'EXIT', Pid, Reason}` as a crash to restart
  **Correction**: `normal` and `shutdown` are not crashes; match them separately and do not restart
- **Error**: Expecting to trap a `kill` signal
  **Correction**: `kill` is untrappable by design — a guaranteed hard kill

## Common Confusions

- **Confusion**: Thinking trapping exits affects only a specific link
  **Clarification**: `trap_exit` is a process-wide flag; it converts signals from *all* linked processes
- **Confusion**: Believing a trapping process can never be killed
  **Clarification**: An `exit(Pid, kill)` signal still kills a trapping process

## Source Reference

Chapter 12, "Errors and Processes," section "Links," subsection "It's a Trap!".

## Verification Notes

- Definition, system processes, restart basis: directly from ch. 12
- Confidence: HIGH — explicitly defined with examples
