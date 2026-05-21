---
concept: Queue Buffer
slug: queue-buffer
category: production-ops
subcategory: overload
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Planning for Overload"
chapter_number: 3
pdf_page: null
section: "Queue Buffers"
extraction_confidence: high
aliases: []
prerequisites:
  - load-shedding
extends:
  - load-shedding
related:
  - random-drop
  - stack-buffer
  - time-sensitive-buffer
contrasts_with:
  - stack-buffer
answers_questions:
  - "When would you pick a queue buffer before a stack buffer?"
  - "How do I shed load with more control than random dropping?"
---

# Quick Definition

A queue buffer is a load-shedding mechanism using a dedicated buffer process that holds incoming messages in a FIFO queue, dropping the oldest when it grows too large — well suited to bursty overload.

# Core Definition

From Chapter 3, section "Queue Buffers": "Queue buffers are a good alternative when you want more control over the messages you get rid of than with random drops, particularly when you expect overload to be coming in bursts rather than a constant stream in need of thinning."

It needs two processes: the regular working process (likely a `gen_server`), and a separate buffer process that does nothing but accumulate messages.

# Prerequisites

- `load-shedding` — a queue buffer is a load-shedding implementation.

# Key Properties

1. Requires two processes: the worker and a dedicated buffer process; external messages go to the buffer.
2. The buffer process drains its mailbox immediately into a `queue` data structure it manages.
3. When the worker is ready, it asks the buffer for N messages; the buffer forwards them and resumes accumulating.
4. When the queue exceeds a size limit and a new message arrives, the oldest is popped and dropped, the new one pushed — functionally similar to a ring buffer.
5. Best when overload arrives in bursts and the input rate is expected to drop again so you can catch up.
6. The *PO Box* library implements such a queue buffer.

# Construction / Recognition

Spawn a buffer process that pulls all messages from its mailbox into an Erlang `queue`. Have the worker request batches from it. When the queue passes its size limit, drop the oldest element per new arrival. Track length with an incrementing/decrementing counter rather than iterating the queue.

# Context & Application

Use a queue buffer when you need control over which messages are dropped and overload is bursty. Preserves FIFO order, so it suits workloads where event sequence matters.

# Examples

From Chapter 3, section "Queue Buffers": "Whenever the queue grows beyond a certain size and you receive a new message, you can then pop the oldest one and push the new one in there, dropping the oldest elements as you go." A footnote notes you can alternatively keep older data and drop the newest if previous data matters more.

# Relationships

## Builds Upon
- `load-shedding` — a concrete implementation.

## Enables
Controlled, order-preserving overload resistance.

## Related
- `random-drop`, `time-sensitive-buffer` — other load-shedding implementations.

## Contrasts With
- `stack-buffer` — a stack buffer (LIFO) favors low latency but loses message order; a queue buffer (FIFO) preserves order but old messages accumulate wait time.

# Common Errors

- Computing queue length by iterating the queue each time instead of maintaining a counter, causing uneven load and sudden build-ups in the buffer's mailbox.
- Using a queue buffer for constant overload — buffers work reliably only when input is expected to eventually drop.

# Common Confusions

- A process's regular mailbox is already a queue, but you should drain it fully into your own `queue` structure — leaving messages in the mailbox does not give you the control a queue buffer provides.

# Source Reference

Chapter 3: Planning for Overload, Section "Queue Buffers". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 3, section "Queue Buffers."
- Confidence rationale: high — mechanism and use case stated explicitly.
- Uncertainties: none.
- Cross-reference status: Verified
