---
concept: Receive Timeout
slug: receive-timeout
category: processes-concurrency
subcategory: concurrency-primitives
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
  - "after clause"
  - "receive after"
  - "timeout"
prerequisites:
  - receive-expression
extends:
  - receive-expression
related:
  - selective-receive
contrasts_with: []
answers_questions:
  - "How do I make a receive give up after a period of time?"
  - "How do I avoid a process deadlocking while waiting for a message?"
---

# Receive Timeout

## Quick Definition

A receive timeout is the `after Delay -> Expression` clause of a `receive`. If no matching message arrives within `Delay` milliseconds, the `after` expression runs instead, preventing an indefinite wait.

## Core Definition

Without a timeout, a `receive` waiting for a message that never arrives leaves the process "waiting — forever, which is a *deadlock*." The chapter explains that "anything dealing with asynchronous operations... needs a way to give up after a certain period of time." Erlang's mechanism is part of the `receive` construct: `receive Match -> Expression1 after Delay -> Expression2 end`. The `after` part triggers "if the `Delay` (in milliseconds) has passed without receiving a message that matches the `Match` pattern." The delay may also be the atom `infinity`, meaning wait forever. A timeout of `0` is a special case used to scan the existing mailbox without blocking — the basis of `flush/0` and selective receives (Hébert, ch. 11, "Time Out").

## Prerequisites

- **Receive expression** — The timeout is the `after` clause of a `receive`

## Key Properties

1. Syntax: `receive Pattern -> Expr1 after Delay -> Expr2 end`
2. `Delay` is in milliseconds; if no matching message arrives in time, `Expr2` runs
3. The atom `infinity` is a valid delay, meaning wait forever (equivalent to no `after`)
4. A delay of `0` checks the current mailbox once without blocking
5. A `receive` with no patterns and only an `after` is a pure sleep — the basis of `timer:sleep/1`
6. Timeouts prevent deadlock when an expected message may never arrive

## Construction / Recognition

## To Use a Receive Timeout

1. Add an `after Delay -> Expression` clause before `end`
2. Choose `Delay` in milliseconds (e.g. `3000` for three seconds)
3. Return a sentinel like `timeout` from the `after` clause so callers can react
4. Use `after infinity` when the wait should be unbounded but parameterized
5. Use `after 0` to drain or scan the mailbox without blocking

## Examples

> **Three-second giving up** (ch. 11): `take2/2` does `receive {Pid, Msg} -> Msg after 3000 -> timeout end`, so a frozen call returns `timeout` instead of deadlocking.
>
> **Sleep** (ch. 11): `sleep(T) -> receive after T -> ok end.` — a `receive` with no pattern, only a timeout.
>
> **Flush with `after 0`** (ch. 11): `flush()` recursively matches `_` and stops at `after 0 -> ok` once the mailbox is empty.

## Relationships

## Builds Upon

- **Receive expression** — The timeout is its optional `after` clause

## Related

- **Selective receive** — Uses `after 0` to scan the mailbox by priority

## Common Errors

- **Error**: Omitting a timeout on a synchronous call whose target may be dead or wrong
  **Correction**: Add an `after` clause so the caller cannot deadlock
- **Error**: Treating a `timeout` result as success
  **Correction**: A timeout means no reply arrived; the operation's outcome is unknown and must be handled

## Common Confusions

- **Confusion**: Thinking `after 0` means "no waiting at all is allowed"
  **Clarification**: `after 0` still scans messages already in the mailbox; it only avoids *blocking* for new ones
- **Confusion**: Believing a timeout guarantees the message will never arrive
  **Clarification**: The message may still arrive later and "come back to haunt" the process; the timeout only stops the wait

## Source Reference

Chapter 11, "More on Multiprocessing," section "Time Out."

## Verification Notes

- Syntax, `infinity`, and `after 0` behavior: directly from ch. 11
- Confidence: HIGH — explicitly defined with examples
