---
concept: Selective Receive
slug: selective-receive
category: processes-concurrency
subcategory: concurrency-primitives
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "More on Multiprocessing"
chapter_number: 11
pdf_page: null
section: "Selective Receives"
extraction_confidence: high
aliases:
  - "selective receive"
  - "message prioritization"
prerequisites:
  - receive-expression
  - process-mailbox
extends:
  - receive-expression
related:
  - receive-timeout
  - mailbox-performance
contrasts_with: []
answers_questions:
  - "What is selective receive?"
  - "How does selective receive relate to the process mailbox?"
---

# Selective Receive

## Quick Definition

A selective receive uses `receive` to pull only specific messages out of the mailbox, ignoring the rest for later. Nesting `receive` clauses with `after 0` lets a process prioritize certain messages.

## Core Definition

The chapter explains that "Erlang's 'flushing' concept makes it possible to implement a selective receive, which can give a priority to the messages you receive by nesting calls." The `important/0` example first grabs all messages with priority above 10, then falls through (`after 0`) to `normal/0`, which grabs the rest. The mechanics: when a `receive` runs, the mailbox is scanned from the oldest message; the first message is tried against every pattern; if none match, it is moved to a *save queue* and the next message is tried; when a later message matches, the saved messages are put back on top of the mailbox to be retried later. "Ignoring some messages to handle them later in the manner described is the essence of selective receives" (Hébert, ch. 11, "Selective Receives").

## Prerequisites

- **Receive expression** — Selective receive is built from `receive`
- **Process mailbox** — Selective receive controls which mailbox messages are handled when

## Key Properties

1. A `receive` matches only specified patterns, leaving non-matching messages in the mailbox
2. The mailbox is scanned oldest-first; unmatched messages go to a save queue
3. When a match is found, saved (skipped) messages are returned to the top of the mailbox
4. Nesting `receive` blocks with `after 0` implements message priority
5. It lets a process care only about useful messages right now
6. It can cause performance problems when many unwanted messages must be scanned each time

## Construction / Recognition

## To Implement a Selective Receive

1. Write a high-priority `receive` with patterns (and guards) for the urgent messages
2. End it with `after 0 -> ...` falling through to a lower-priority receive
3. The lower-priority `receive` handles the remaining messages, also ending in `after 0`
4. Each receive accumulates its matched messages, e.g. into a list

## Examples

> **Priority receive** (ch. 11): `important/0` matches `{Priority, Message} when Priority > 10`, then `after 0` calls `normal/0` for the rest; the result for messages `{15,high},{7,low},{1,low},{17,high}` is `[high,high,low,low]`.
>
> **Save queue** (ch. 11): "When there is no way to match a given message, it is put in a *save queue*, and the next message is tried."

## Relationships

## Builds Upon

- **Receive expression** — Selective receive is `receive` used to skip messages

## Related

- **Receive timeout** — `after 0` is what makes nested selective receives non-blocking
- **Mailbox performance** — Selective receive is a frequent cause of mailbox slowdowns

## Common Errors

- **Error**: Relying on deep selective receives when many junk messages fill the mailbox
  **Correction**: Each scan must skip all junk first; instead fix why unwanted messages arrive, or use a `gb_trees` min-heap
- **Error**: Coercing code to trigger the compiler's selective-receive optimization
  **Correction**: Write idiomatic code; the optimization (reference-tagged messages) applies automatically when appropriate

## Common Confusions

- **Confusion**: Thinking a `receive` consumes the whole mailbox
  **Clarification**: It consumes only the first matching message; the rest stay queued
- **Confusion**: Believing skipped messages are lost
  **Clarification**: Skipped messages go to a save queue and are returned to the mailbox for later matching

## Source Reference

Chapter 11, "More on Multiprocessing," section "Selective Receives" (including subsection "The Pitfalls of Selective Receives").

## Verification Notes

- Definition, save-queue mechanics, priority example: directly from ch. 11
- Confidence: HIGH — explicitly defined with a worked example
