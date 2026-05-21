---
concept: Process Link
slug: process-link
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
  - "link"
  - "link/1"
  - "process linking"
prerequisites:
  - process
  - spawn
extends: []
related:
  - spawn-link
  - exit-signal
  - trapping-exits
contrasts_with:
  - process-monitor
answers_questions:
  - "What is a link?"
  - "How do links relate to monitors?"
  - "What distinguishes a link from a monitor?"
---

# Process Link

## Quick Definition

A link is a bidirectional relationship between two processes such that if one dies abnormally, the other dies too — binding their life cycles. Links are created with `link/1` and removed with `unlink/1`.

## Core Definition

A link is "a specific kind of relationship that can be created between two processes. When that relationship is set up and one of the processes dies from an unexpected throw, error, or exit, the other linked process also dies, binding their separate life cycles into a single, related one." Links are created with `link/1` (taking a pid) and removed with `unlink/1`. When a linked process crashes, a special *exit signal* propagates; no signal is sent if a process dies of natural causes (finishes running). Links are *bidirectional* — only one process need die for the others to follow. Links "cannot be stacked": calling `link/1` many times for the same pair still yields one link, and one `unlink/1` removes it (Hébert, ch. 12, "Links").

## Prerequisites

- **Process** — Links connect two processes
- **Spawn** — You need pids of running processes to link them

## Key Properties

1. A link is a bidirectional relationship between two processes
2. Created with `link/1`, removed with `unlink/1`
3. When one linked process dies abnormally, the others die too
4. No exit signal is sent when a process finishes normally
5. Links do not stack — multiple `link/1` calls yield one link; one `unlink/1` tears it down
6. Links are an organizational construct: fixed, known-in-advance dependencies between processes
7. Links let groups of interdependent processes "fail as soon as possible" together

## Construction / Recognition

## To Use a Link

1. Get the pid of the process to link to
2. Call `link(Pid)` from the current process
3. To break the link, call `unlink(Pid)`
4. To handle a linked process's death rather than dying, trap exits (see trapping exits)
5. Prefer `spawn_link` when spawning and linking together, for atomicity

## Examples

> **Shell dies with linked process** (ch. 12): `link(spawn(fun linkmon:myproc/0))` — when `myproc` calls `exit(reason)`, the shell crashes with `** exception error: reason`.
>
> **Chain of links** (ch. 12): `linkmon:chain(3)` links a chain of processes; when the last exits, the error propagates down the whole chain to the shell.

## Relationships

## Builds Upon

- **Process** — Links join processes
- **Spawn** — Provides the processes to link

## Related

- **Spawn-link** — The atomic spawn-and-link primitive
- **Exit signal** — What propagates along a link when a process dies
- **Trapping exits** — Converting incoming exit signals into messages instead of dying

## Contrasts With

- **Process monitor** — Links are bidirectional and do not stack; monitors are unidirectional and stackable

## Common Errors

- **Error**: Using `link(spawn(...))` and assuming atomicity
  **Correction**: `spawn` then `link` are two steps; the process may die in between — use `spawn_link`
- **Error**: A library calling `unlink/1` and tearing down a link it did not own
  **Correction**: Links do not stack, so `unlink` affects everyone; use monitors in library code instead

## Common Confusions

- **Confusion**: Thinking a link fires on normal termination
  **Clarification**: A normal exit sends no signal; only abnormal deaths propagate
- **Confusion**: Believing you can have multiple independent links between two processes
  **Clarification**: Links do not stack — there is at most one link per pair

## Source Reference

Chapter 12, "Errors and Processes," section "Links."

## Verification Notes

- Definition, bidirectionality, no-stacking: directly from ch. 12
- Confidence: HIGH — explicitly defined with examples
