---
concept: Supervisor Shutdown
slug: supervisor-shutdown
category: fault-tolerance
subcategory: supervision
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Who Supervises the Supervisors?"
chapter_number: 17
pdf_page: null
section: "Shutdown"
extraction_confidence: high
aliases:
  - shutdown value
  - "brutal_kill"
  - orderly shutdown
prerequisites:
  - supervisor
  - child-specification
extends: []
related:
  - child-specification
  - supervision-tree
contrasts_with: []
answers_questions:
  - "What is a supervisor?"
  - "How do I write a supervisor?"
---

# Supervisor Shutdown

## Quick Definition

The `Shutdown` value of a child specification is the deadline a supervisor gives a child to terminate cleanly before brutally killing it. Supervision trees enable well-ordered VM shutdown.

## Core Definition

"When the top-level supervisor is asked to terminate, it calls `exit(ChildPid, shutdown)` on each of the pids. ... The `Shutdown` value of a child specification is thus used to give a deadline for the termination" (Ch. 17, "Shutdown"). The deadline is a time in milliseconds, `infinity`, or `brutal_kill`.

## Prerequisites

- **Supervisor** — Shutdown is the supervisor's termination procedure.
- **Child specification** — The `Shutdown` value is one of its six fields.

## Key Properties

1. To terminate a child, the supervisor calls `exit(ChildPid, shutdown)`.
2. A worker trapping exits runs its `terminate` function; otherwise it just dies.
3. A child supervisor receiving `shutdown` forwards it to its own children.
4. `Shutdown` is a millisecond deadline, `infinity`, or `brutal_kill`.
5. If the deadline passes, the process is killed with `exit(Pid, kill)` (untrappable).
6. `brutal_kill` kills immediately with `exit(Pid, kill)` — no deadline, untrappable, instantaneous.
7. Mismatched deadlines in a supervisor chain can cause children to be brutally killed because an ancestor's cutoff is shorter.

## Construction / Recognition

## To Choose a Shutdown Value

1. If the child must close files/sockets/notify a service → set a millisecond deadline long enough for that.
2. If the child is patient and you trust it to finish → `infinity`.
3. If the child can die instantly with no consequences → `brutal_kill`.

## Context & Application

Supervisors are also valued because they give "a well-ordered VM shutdown" — a top supervisor terminating propagates `shutdown` down the whole tree. The book's `band_supervisor` musicians use a 1000 ms shutdown; the `ppool_supersup` gives each pool supervisor 10500 ms "large enough that all the children will have time to stop." The book warns: choosing a good value "is sometimes complex" and "entirely application-dependent."

## Examples

**Example 1** (Ch. 17): `{singer, {musicians, start_link, [singer, good]}, permanent, 1000, worker, [musicians]}` — a 1000 ms shutdown deadline.

**Example 2** (Ch. 18): `start_pool` uses a child spec with `10500` ms shutdown for each pool supervisor, "large enough that all the children will have time to stop."

## Relationships

## Builds Upon

- **Child specification** — `Shutdown` is one of its fields.

## Related

- **supervision-tree** — Shutdown propagates down the tree for an orderly VM stop.

## Common Errors

- **Error**: Giving a worker that closes resources a too-short or `brutal_kill` shutdown.
  **Correction**: Set a deadline long enough for `terminate` to finish its cleanup.
- **Error**: Inconsistent deadlines down a supervisor chain (e.g. 5 → 2 → 5 → 5).
  **Correction**: Ensure ancestors' deadlines are not shorter than descendants', or descendants get brutally killed.

## Common Confusions

- **Confusion**: Thinking `brutal_kill` is just a fast shutdown.
  **Clarification**: `brutal_kill` uses `exit(Pid, kill)`, which is *untrappable* — the child's `terminate` never runs.

## Source Reference

Chapter 17: "Who Supervises the Supervisors?", section "Child Specifications," subsection "Shutdown"; orderly-shutdown discussion in "Supervisor Concepts."

## Verification Notes

- Definition: Direct quotes from the "Shutdown" subsection.
- Key Properties: Adapted from the subsection and the orderly-shutdown discussion.
- Confidence: HIGH — explicitly described.
