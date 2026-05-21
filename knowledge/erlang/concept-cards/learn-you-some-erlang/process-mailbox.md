---
concept: Process Mailbox
slug: process-mailbox
category: processes-concurrency
subcategory: concurrency-primitives
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "The Hitchhiker's Guide to Concurrency"
chapter_number: 10
pdf_page: null
section: "Sending Messages"
extraction_confidence: high
aliases:
  - "mailbox"
  - "message queue"
prerequisites:
  - process
  - message-passing
extends: []
related:
  - receive-expression
  - selective-receive
  - mailbox-performance
contrasts_with: []
answers_questions:
  - "What is a process mailbox?"
  - "How does selective receive relate to the process mailbox?"
---

# Process Mailbox

## Quick Definition

The process mailbox is a per-process queue holding messages that have been sent to a process but not yet read. Messages are kept in arrival order and removed when matched by a `receive`.

## Core Definition

Each process has a *mailbox* — described in the chapter as hidden process state. When a message is sent with `!`, it "has been put in the process's mailbox, but it hasn't been read yet." Messages "are kept in the order they are received. Every time a message is read, it is taken out of the mailbox." Messages remain in the mailbox until a `receive` matches a pattern against them, "even if the process that originally sent them has died since then." The shell's `flush()` command outputs and clears the current mailbox (Hébert, ch. 10, "Sending Messages"; ch. 11, "The Pitfalls of Selective Receives").

## Prerequisites

- **Process** — The mailbox is part of a process's hidden state
- **Message passing** — The mailbox is filled by `!` sends

## Key Properties

1. Every process has its own mailbox
2. Messages are stored in arrival order
3. A message stays in the mailbox until a `receive` matches it
4. Reading a message removes it from the mailbox
5. Messages persist even if the sending process has since died
6. Messages a process never reads accumulate, growing the mailbox
7. `flush()` in the shell prints and clears the mailbox

## Construction / Recognition

## To Work With the Mailbox

1. Send messages to a pid with `!` — they queue in arrival order
2. Consume them with a `receive` expression, which removes the matched one
3. In the shell, inspect and clear the mailbox with `flush()`
4. Add a catch-all `receive` clause so unexpected messages do not accumulate

## Examples

> **Message queued, not read** (ch. 10): after `self() ! hello.` the message sits in the mailbox; `flush()` later prints `Shell got hello`.
>
> **Arrival order** (ch. 10): "the messages are kept in the order they are received. Every time a message is read, it is taken out of the mailbox."

## Relationships

## Builds Upon

- **Process** — The mailbox is per-process hidden state
- **Message passing** — `!` deposits messages into the mailbox

## Related

- **Receive expression** — Consumes messages from the mailbox
- **Selective receive** — Scans the mailbox for messages matching a pattern
- **Mailbox performance** — How an accumulating mailbox can slow a process

## Common Errors

- **Error**: Never consuming certain messages, letting the mailbox grow unbounded
  **Correction**: Add a catch-all `receive` clause to drain unexpected messages
- **Error**: Assuming a `receive` only sees recent messages
  **Correction**: The mailbox holds all unread messages from the start; `receive` scans from the oldest

## Common Confusions

- **Confusion**: Thinking messages disappear when the sender dies
  **Clarification**: Messages persist in the receiver's mailbox regardless of the sender's fate

## Source Reference

Chapter 10, "The Hitchhiker's Guide to Concurrency," subsection "Sending Messages"; Chapter 11, subsection "The Pitfalls of Selective Receives."

## Verification Notes

- Definition and ordering: directly from ch. 10
- Persistence-after-sender-death detail: from ch. 11
- Confidence: HIGH — explicitly described
