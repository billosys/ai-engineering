---
# === CORE IDENTIFICATION ===
concept: Mailbox
slug: mailbox

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: communication
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Concurrent Programming"
chapter_number: 12
pdf_page: null
section: "The Concurrency Primitives"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "process mailbox"
  - "message queue"
  - "save queue"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
extends: []
related:
  - message-passing
  - receive
  - selective-receive
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a process mailbox?"
  - "Where do sent messages go before they are received?"
  - "What is the save queue in a receive?"
---

# Quick Definition

A mailbox is the per-process queue that holds messages sent to a process. It is created with the process and is examined only when the process evaluates a `receive`.

# Core Definition

"Each process has an associated mailbox that is also created when the process is created. When you send a message to a process, the message is put into the mailbox of the process. The only time the mailbox is examined is when your program evaluates a receive statement" (Armstrong, "Concurrent Programming," "The Concurrency Primitives"). During selective receive, messages that match no clause are moved into a temporary "save queue"; once a message is matched, "all messages that have been put into the save queue are reentered into the mailbox in the order in which they arrived" (Armstrong, "Concurrent Programming," "Selective Receive").

# Prerequisites

- **Process** — Every process has exactly one mailbox; you must know what a process is.

# Key Properties

1. One mailbox per process, created together with the process.
2. A message sent with `!` is placed in the recipient's mailbox.
3. The mailbox is examined only when a `receive` is evaluated.
4. During a `receive`, unmatched messages are moved to a temporary save queue.
5. After a match, saved messages are returned to the mailbox in their original arrival order.
6. Messages that never match any `receive` clause accumulate in the mailbox indefinitely.
7. Large mailboxes make priority-receive techniques inefficient.

# Construction / Recognition

## To Construct/Create:
A mailbox is not constructed explicitly — it is created automatically when a process is spawned.

## To Identify/Recognize:
1. Messages "ending up in the mailbox and never being received" indicate unmatched messages accumulating.
2. A `flush_buffer` style function (a `receive _Any -> ...` with `after 0`) is used to empty a mailbox.

# Context & Application

- **Typical contexts**: Every message-receiving process; buffering between asynchronous senders and a receiver.
- **Common applications**: Decoupling senders from receivers; holding requests until the server's `receive` runs.
- **Historical/stylistic notes**: Armstrong warns to keep mailboxes small when using priority receive, since scanning a large mailbox is inefficient.

# Examples

**Example 1** ("The Concurrency Primitives"): `Pid ! {rectangle, 6, 10}` puts the tuple into the area-server process's mailbox; it is read when `loop/0` evaluates its `receive`.

**Example 2** ("Receive with Timeout Value of Zero"): `flush_buffer()` uses `receive _Any -> flush_buffer() after 0 -> true end` to empty all messages from the mailbox.

**Example 3** ("Selective Receive"): Messages not matching any `receive` clause are placed in a "save queue" and reentered into the mailbox, in arrival order, once a match occurs.

# Relationships

## Builds Upon
- **Process** — A mailbox belongs to a process.

## Enables
- **receive** — `receive` is the operation that reads the mailbox.
- **Selective receive** — The save-queue mechanism operates on the mailbox.

## Related
- **Message passing** — Sent messages land in the mailbox.

## Contrasts With
- None.

# Common Errors

- **Error**: Letting unmatched messages pile up unboundedly in the mailbox.
  **Correction**: Add a catch-all `receive` clause so every message is consumed.

- **Error**: Using priority receive over a very large mailbox.
  **Correction**: Keep mailboxes small; scanning a large mailbox for priority messages is inefficient.

# Common Confusions

- **Confusion**: Thinking the mailbox is continuously processed.
  **Clarification**: It is examined only when the process evaluates a `receive`.

- **Confusion**: Believing the save queue reorders messages.
  **Clarification**: Saved messages are returned to the mailbox in their original arrival order.

# Source Reference

Chapter 12: "Concurrent Programming," sections "The Concurrency Primitives," "Receive with Timeout Value of Zero," and "Selective Receive." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct quotes of the mailbox description from "The Concurrency Primitives" and "Selective Receive."
- Confidence rationale: HIGH — the mailbox and save queue are described explicitly.
- Uncertainties: None.
- Cross-reference status: Canonical slug `mailbox`; cross-refs verified.
- Re-extraction notes: Fresh extraction; new card (no prior file).
