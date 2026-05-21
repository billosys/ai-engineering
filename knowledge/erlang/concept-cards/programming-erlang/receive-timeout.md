---
# === CORE IDENTIFICATION ===
concept: Receive with a Timeout
slug: receive-timeout

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: communication
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Concurrent Programming"
chapter_number: 12
pdf_page: null
section: "Receive with a Timeout"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "after clause"
  - "receive ... after"
  - "timeout"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - receive
extends:
  - receive
related:
  - selective-receive
  - mailbox
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I add a timeout to a receive?"
  - "What does an after clause do?"
  - "What happens with a receive timeout of 0 or infinity?"
---

# Quick Definition

A receive with a timeout adds an `after Time -> Expressions` clause to a `receive`, so the process stops waiting after `Time` milliseconds if no matching message arrives.

# Core Definition

"Sometimes a receive statement might wait forever for a message that never comes ... To avoid this problem, we can add a timeout to the receive statement" (Armstrong, "Concurrent Programming," "Receive with a Timeout"). The syntax adds `after Time -> Expressions` before `end`. "If no matching message has arrived within `Time` milliseconds of entering the receive expression, then the process will stop waiting for a message and evaluate `Expressions`." Special cases: a `receive` with *only* an `after` clause sleeps for `Time` ms (used to implement `sleep/1`); a timeout value of `0` runs the `after` body immediately but *after* trying to match any messages already in the mailbox (used by `flush_buffer` and priority receive); and the atom `infinity` means the timeout will never trigger.

# Prerequisites

- **receive** — A timeout is an optional `after` clause on the `receive` primitive.

# Key Properties

1. Syntax: `receive ... after Time -> Expressions end`, where `Time` is in milliseconds.
2. The timer starts when the `receive` is entered.
3. If no matching message arrives within `Time` ms, the `after` expressions run.
4. A `receive` with only an `after` clause suspends the process for `Time` ms.
5. `after 0` runs the body immediately, but only after matching any messages already in the mailbox.
6. `after infinity` means the timeout never fires.
7. On a normal match, the timer is cleared; saved messages are restored to the mailbox.

# Construction / Recognition

## To Construct/Create:
1. Add `after Time -> Expressions` before the `end` of a `receive`.
2. For a pure delay, use a body-less `receive` with only `after T -> true`.
3. For mailbox flushing, use `after 0` so existing messages are matched then the body runs.

## To Identify/Recognize:
1. An `after` keyword inside a `receive` marks a timeout.
2. `after 0` indicates a non-blocking / priority-receive idiom; `after infinity` indicates an intentional wait-forever.

# Context & Application

- **Typical contexts**: Communication protocols where waiting forever is unacceptable; timers; sleeping; flushing mailboxes.
- **Common applications**: `sleep(T)`, `flush_buffer()`, `priority_receive()`, and cancellable timers (`stimer`).
- **Historical/stylistic notes**: "Timeouts and timers are central to the implementation of many communication protocols."

# Examples

**Example 1** ("Receive with Just a Timeout"): `sleep(T) -> receive after T -> true end.` suspends the current process for `T` milliseconds.

**Example 2** ("Receive with Timeout Value of Zero"): `flush_buffer() -> receive _Any -> flush_buffer() after 0 -> true end.` empties all messages from the mailbox.

**Example 3** ("Implementing a Timer"): `stimer` — `timer(Time, Fun) -> receive cancel -> void after Time -> Fun() end.` runs `Fun` after `Time` ms unless a `cancel` message arrives first.

# Relationships

## Builds Upon
- **receive** — A timeout is an `after` clause extending `receive`.

## Enables
- (No downstream concept strictly depends on it.)

## Related
- **Selective receive** — The timeout interacts with the selective-receive algorithm (timer starts on entry, cleared on match).
- **Mailbox** — `after 0` matches existing mailbox messages before firing.

## Contrasts With
- None.

# Common Errors

- **Error**: Omitting a timeout in a `receive` that could wait for a message that never arrives.
  **Correction**: Add an `after Time -> ...` clause to bound the wait.

- **Error**: Using `flush_buffer` without the `after 0` clause.
  **Correction**: Without `after 0` it suspends forever once the mailbox is empty; the zero timeout lets it return.

# Common Confusions

- **Confusion**: Thinking `after 0` ignores messages already in the mailbox.
  **Clarification**: `after 0` first tries to match all existing messages; the body runs only if none match.

- **Confusion**: Believing `after infinity` is the same as omitting the `after` clause.
  **Clarification**: Behaviorally similar (wait forever), but `infinity` is useful when the timeout value is computed dynamically.

# Source Reference

Chapter 12: "Concurrent Programming," section "Receive with a Timeout" (subsections "Receive with Just a Timeout," "Receive with Timeout Value of Zero," "receive with Timeout Value of Infinity," "Implementing a Timer"). EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the `after` syntax and the `sleep`/`flush_buffer`/`stimer` examples.
- Confidence rationale: HIGH — the timeout mechanism and all special cases are described explicitly.
- Uncertainties: None.
- Cross-reference status: Cross-refs verified against KB slugs.
- Re-extraction notes: Fresh extraction; new card (no prior file).
