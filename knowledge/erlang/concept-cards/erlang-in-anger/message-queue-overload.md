---
concept: Message Queue Overload
slug: message-queue-overload
category: production-ops
subcategory: overload
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Planning for Overload"
chapter_number: 3
pdf_page: null
section: "Planning for Overload"
extraction_confidence: high
aliases:
  - "Mailbox overflow"
  - "Queue blowup"
prerequisites:
  - let-it-crash
extends: []
related:
  - true-bottleneck
  - back-pressure
  - load-shedding
  - error-logger-overload
  - blocking-operation-in-hub-process
contrasts_with: []
answers_questions:
  - "What is the most common cause of Erlang node failure?"
  - "Name the common sources of overload in Erlang systems."
---

# Quick Definition

Message queue overload is the unbounded growth of a process's mailbox, which exhausts node memory and is the most common cause of Erlang node failure in production.

# Core Definition

From Chapter 3, section "Planning for Overload": "By far, the most common cause of failure I've encountered in real-world scenarios is due to the node running out of memory. Furthermore, it is usually related to message queues going out of bounds."

Because Erlang mailboxes are unbounded, a process that receives messages faster than it can process them accumulates them until the node runs Out Of Memory.

# Prerequisites

- `let-it-crash` — overload is the dominant *non*-handled failure mode that even the supervision model cannot absorb cleanly.

# Key Properties

1. The single most common cause of node failure observed by the author.
2. Caused by a process receiving messages faster than it processes them; Erlang mailboxes have no bound.
3. Determining *which* queue blew up is not hard — it can be found in a crash dump.
4. Determining *why* it blew up is trickier — causes include fast flooding and processes blocked so they cannot drain fast enough.
5. The hardest part is deciding *how to fix it*; fixes fall into two broad strategies: back-pressure and load-shedding.

# Construction / Recognition

Recognize it from a node OOM crash plus a crash dump showing a large message queue. Diagnose the cause from the process's role and runtime inspection (fast flooding vs. blocked process). Fix it by choosing back-pressure (slow the producer) or load-shedding (drop messages).

# Context & Application

This is the central problem of Chapter 3. The book's "bathroom sink" metaphor frames it: input flows from the faucet, the Erlang system is the sink and pipes, and the destination is the sewer; overload is the sink clogging.

# Examples

From Chapter 3: the bathroom-sink metaphor — "Did someone put too much water in the sink? Are the sewer systems backing up? Did you just design too small a pipe?" The chapter lists common concrete sources: `error_logger` exploding, locks and blocking operations, and unexpected messages.

# Relationships

## Builds Upon
- `let-it-crash` — the supervision model handles process crashes, but a node OOM from queue overload takes everything down.

## Enables
The need for `back-pressure` and `load-shedding`.

## Related
- `true-bottleneck`, `error-logger-overload`, `blocking-operation-in-hub-process` — causes and related concepts.

## Contrasts With
Nothing directly.

# Common Errors

- Optimizing the wrong layer: enlarging the process that crashed, then its drain, then the pipes — only to push the overload further down without finding the true bottleneck.

# Common Confusions

- Finding *which* queue overflowed (easy, from the crash dump) is not the same as understanding *why* (hard) or deciding *how to fix it* (hardest).
- Queue overload is a memory problem, not merely a CPU problem — the mailbox itself consumes the memory.

# Source Reference

Chapter 3: Planning for Overload, Section "Planning for Overload" (chapter introduction). (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 3 introduction.
- Confidence rationale: high — explicitly identified as the most common failure cause.
- Uncertainties: none.
- Cross-reference status: Verified
