---
concept: Mailbox Performance
slug: mailbox-performance
category: processes-concurrency
subcategory: process-design
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "More on Multiprocessing"
chapter_number: 11
pdf_page: null
section: "More Mailbox Pitfalls"
extraction_confidence: high
aliases:
  - "mailbox pitfalls"
  - "message queue performance"
prerequisites:
  - process-mailbox
  - selective-receive
extends: []
related:
  - gb-trees
contrasts_with: []
answers_questions:
  - "Why can a process slow down when it has many messages?"
  - "How do I keep a process mailbox from causing performance problems?"
---

# Mailbox Performance

## Quick Definition

Mailbox performance is the concern that a process with many unwanted messages slows down: each `receive` must scan past junk to find useful messages, and the mailbox itself grows. Defensive catch-all clauses and priority data structures mitigate this.

## Core Definition

The chapter warns that selective receives are "a frequent cause of performance problems in Erlang." When a process accumulates messages it never reads, "reading useful messages will actually take longer and longer (and the processes will grow in size, too)." The illustrative case: to reach the 367th message, a process must try-and-skip the first 366 junk messages, queue them, take the wanted one, then put the 366 back. Two defenses are offered. First, a *catch-all clause* (`Unexpected -> io:format(...)`) ensures every message matches and is drained from the mailbox. Second, when genuine priority is needed, implement a *min-heap* or use `gb_trees`, dumping each message in keyed by priority, then pulling the smallest/largest — usually more efficient than selective receives. The recurring advice: "profile and measure before optimizing" (Hébert, ch. 11, "The Pitfalls of Selective Receives," "More Mailbox Pitfalls").

## Prerequisites

- **Process mailbox** — The structure whose growth causes the problem
- **Selective receive** — The pattern that scans the mailbox and exposes the cost

## Key Properties

1. Unread messages accumulate in the mailbox, growing the process
2. Each `receive` scans the mailbox oldest-first; junk messages must be skipped every time
3. The more junk precedes a useful message, the slower it is found
4. A catch-all `receive` clause drains unexpected messages so they cannot accumulate
5. For real priority handling, a min-heap or `gb_trees` keyed by priority is usually faster than nested selective receives
6. The `gb_trees` approach can be slower if most messages already have the highest priority
7. Always profile and measure before optimizing

## Construction / Recognition

## To Protect Mailbox Performance

1. Add a final catch-all clause: `Unexpected -> io:format("unexpected message ~p~n", [Unexpected])`
2. Optionally log unexpected messages to a logging facility for later diagnosis
3. If slow with many messages, ask: are messages sent to the right process? are patterns correct? is the format right? should there be more processes?
4. For priority needs, store messages in a `gb_trees` keyed with the priority first, then pull smallest/largest
5. Profile and measure before and after any change

## Examples

> **Defensive catch-all** (ch. 11): a final `Unexpected -> io:format("unexpected message ~p~n", [Unexpected])` clause guarantees every message matches and leaves the mailbox.
>
> **Burrowed message** (ch. 11): "imagine we want the 367th message, but the first 366 messages are junk... The next useful message could be burrowed much deeper and take even longer to be found."
>
> **gb_trees priority store** (ch. 11): dump messages into `gb_trees` with the priority first in the key, then search for the `smallest` or `largest`.

## Relationships

## Related

- **GB trees** — Recommended structure for handling message priority efficiently

## Common Errors

- **Error**: Omitting a catch-all clause so stray messages pile up forever
  **Correction**: Always add a catch-all `receive` clause to drain and log unexpected messages
- **Error**: Optimizing the mailbox before measuring
  **Correction**: Profile first; the real fix may be sending messages to the right process

## Common Confusions

- **Confusion**: Thinking a large mailbox only costs memory
  **Clarification**: It also costs time — every `receive` rescans skipped messages
- **Confusion**: Believing a `gb_trees` priority queue is always faster
  **Clarification**: It can be slower when most messages share the highest priority

## Source Reference

Chapter 11, "More on Multiprocessing," section "Selective Receives," subsections "The Pitfalls of Selective Receives" and "More Mailbox Pitfalls."

## Verification Notes

- Pitfalls, catch-all defense, gb_trees suggestion: directly from ch. 11
- Confidence: HIGH — explicitly discussed
