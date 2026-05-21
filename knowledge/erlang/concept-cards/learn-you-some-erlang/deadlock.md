---
concept: Deadlock
slug: deadlock
category: processes-concurrency
subcategory: concurrency-hazards
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "More on Multiprocessing"
chapter_number: 11
pdf_page: null
section: "Time Out"
extraction_confidence: high
aliases:
  - "deadlock"
prerequisites:
  - receive-expression
  - message-passing
extends: []
related:
  - receive-timeout
contrasts_with:
  - race-condition
answers_questions:
  - "What is a deadlock in Erlang?"
  - "How do I prevent a process from waiting forever?"
---

# Deadlock

## Quick Definition

A deadlock in Erlang is a process stuck in a `receive` waiting forever for a message that will never arrive — for example because it sent a request to a wrong or dead process.

## Core Definition

The chapter demonstrates a deadlock by feeding `kitchen:take/2` a fake pid: "the shell is frozen." Nothing illegal happened — "the program is just waiting — forever, which is a *deadlock*." It arises because the caller switches to `receive` mode expecting a reply, but the target "either doesn't exist or doesn't expect such a message and does nothing with it," so the caller "is stuck in receive mode." The chapter's general principle: "anything dealing with asynchronous operations... needs a way to give up after a certain period of time if it gets no sign of receiving data." The remedy is a receive timeout (`after`). Note also (ch. 12) that Erlang's message passing makes deadlocks *less* common but does not eliminate them — "you should never assume your code is entirely free of race conditions" or deadlocks (Hébert, ch. 11, "Time Out").

## Prerequisites

- **Receive expression** — A deadlock is a `receive` that never matches
- **Message passing** — The missing message is what would unblock the process

## Key Properties

1. A deadlocked process is blocked in `receive` waiting for a message that never comes
2. Common cause: a request sent to a non-existent or wrong process
3. No error is raised — the process simply waits indefinitely
4. The remedy is a receive timeout (`after Delay -> ...`)
5. Erlang's mailbox model makes deadlocks rarer but does not guarantee freedom from them

## Construction / Recognition

## To Avoid Deadlock

1. Add an `after Delay` clause to any `receive` whose message might never arrive
2. Verify the target pid or registered name is correct before sending
3. Return a sentinel like `timeout` so callers can react instead of hanging
4. In the shell, escape a frozen process with Ctrl-G

## Examples

> **Frozen shell** (ch. 11): `kitchen:take(pid(0,250,0), dog)` sends to a fake pid; the shell freezes because the caller waits forever in `receive`.
>
> **The fix** (ch. 11): `take2/2` adds `after 3000 -> timeout`, so the call returns `timeout` instead of deadlocking.

## Relationships

## Related

- **Receive timeout** — The mechanism that prevents deadlock

## Contrasts With

- **Race condition** — A deadlock is a process stuck forever; a race condition is a timing-dependent inconsistency

## Common Errors

- **Error**: Omitting a timeout on a synchronous receive whose reply may never arrive
  **Correction**: Add an `after` clause so the wait is bounded

## Common Confusions

- **Confusion**: Thinking Erlang cannot deadlock
  **Clarification**: Message passing reduces deadlocks but a process can still wait forever on a message that never comes

## Source Reference

Chapter 11, "More on Multiprocessing," section "Time Out."

## Verification Notes

- Definition and frozen-shell example: directly from ch. 11
- Non-immunity note: cross-referenced from ch. 12
- Confidence: HIGH — explicitly defined
