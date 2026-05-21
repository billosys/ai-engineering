---
concept: Exit Signal
slug: exit-signal
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
  - "exit signal"
  - "signal"
  - "exit/2"
prerequisites:
  - process-link
extends: []
related:
  - trapping-exits
  - process-link
contrasts_with: []
answers_questions:
  - "What is an exit signal?"
  - "What distinguishes errors, exits, and throws across processes?"
---

# Exit Signal

## Quick Definition

An exit signal is a special "secret" message that propagates along links when a process dies, automatically killing linked processes. It can be sent explicitly with `exit/2`, and the reason `kill` is untrappable.

## Core Definition

"Error propagation across processes is done through a process similar to message passing, but with a special type of message called *signals*. Exit signals are 'secret' messages that automatically act on processes, killing them." A process can send one explicitly with `exit(Pid, Reason)` — "the Erlang process equivalent of a gun. It allows a process to kill another one from a distance." The chapter catalogues the special cases: `exit(Pid, normal)` cannot kill another process; `exit(Pid, kill)` is an untrappable signal that always kills, but is changed to `killed` when it propagates to other linked processes so that a death cascade is avoided. `exit(self(), kill)` cannot be trapped even locally (Hébert, ch. 12, "It's a Trap!", "exit/2 Changes Everything," "Killing Me (Not So) Softly").

## Prerequisites

- **Process link** — Exit signals propagate along links

## Key Properties

1. An exit signal is a special message that automatically acts on (kills) a process
2. Signals propagate along links when a process dies abnormally
3. `exit(Pid, Reason)` sends a signal to another process from a distance
4. `exit(Pid, normal)` does not kill another process — `normal` is a non-killing reason
5. `exit(Pid, kill)` always kills and cannot be trapped by the target
6. A `kill` signal is changed to `killed` when received by other linked processes, preventing a death cascade
7. `exit(self(), kill)` is untrappable even locally
8. Most exit reasons *can* be trapped; only `kill` is special

## Construction / Recognition

## To Work With Exit Signals

1. Let a linked process's abnormal death send a signal automatically
2. To kill a process explicitly: `exit(Pid, Reason)`
3. Use `exit(Pid, kill)` as a last resort to kill a process that traps exits or is stuck
4. To survive a signal instead of dying, trap exits (`process_flag(trap_exit, true)`)
5. Expect a trapped signal as the message `{'EXIT', Pid, Reason}`

## Examples

> **Untrappable kill** (ch. 12): `exit(self(), kill)` gives `** exception exit: killed` whether or not exits are trapped.
>
> **Kill changes to killed** (ch. 12): `exit(spawn_link(fun() -> timer:sleep(50000) end), kill)`, when trapped, arrives as `{'EXIT', Pid, killed}` — not `kill`.
>
> **Killing the critic** (ch. 12): `exit(Critic, solar_storm)` kills the critic process from a distance.

## Relationships

## Builds Upon

- **Process link** — Signals propagate along links

## Related

- **Trapping exits** — Converts most exit signals into ordinary messages
- **Process link** — The conduit along which signals travel

## Common Errors

- **Error**: Expecting `exit(Pid, normal)` to kill another process
  **Correction**: `normal` cannot remotely kill a process; use a different reason
- **Error**: Expecting to trap a `kill` signal sent to the local process
  **Correction**: `exit(self(), kill)` is untrappable; `kill` is a last-resort hard kill

## Common Confusions

- **Confusion**: Thinking exit signals are ordinary messages
  **Clarification**: Signals act automatically on processes; only trapping converts them into ordinary `{'EXIT',...}` messages
- **Confusion**: Wondering why a trapped `kill` shows as `kill` locally but `killed` to neighbors
  **Clarification**: The signal is rewritten on propagation specifically to stop a death cascade

## Source Reference

Chapter 12, "Errors and Processes," section "Links," subsections "It's a Trap!", "exit/2 Changes Everything," "Killing Me (Not So) Softly."

## Verification Notes

- Definition, exit/2 cases, kill/killed rewriting: directly from ch. 12
- Confidence: HIGH — explicitly defined with a detailed case catalogue
