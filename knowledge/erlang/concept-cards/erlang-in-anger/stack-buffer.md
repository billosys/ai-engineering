---
concept: Stack Buffer
slug: stack-buffer
category: production-ops
subcategory: overload
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Planning for Overload"
chapter_number: 3
pdf_page: null
section: "Stack Buffers"
extraction_confidence: high
aliases: []
prerequisites:
  - load-shedding
  - queue-buffer
extends:
  - load-shedding
related:
  - random-drop
  - time-sensitive-buffer
contrasts_with:
  - queue-buffer
answers_questions:
  - "When would you pick a stack buffer over a queue buffer?"
  - "What happens to new and old requests in a stack buffer under overload?"
---

# Quick Definition

A stack buffer is a load-shedding mechanism that buffers messages in a LIFO stack (an Erlang list), so newer messages reach the worker quickly while only a few old ones wait — ideal for low-latency requirements.

# Core Definition

From Chapter 3, section "Stack Buffers": "Stack buffers are ideal when you want the amount of control offered by queue buffers, but you have an important requirement for low latency. To use a stack as a buffer, you'll need two processes, just like you would with queue buffers, but a list will be used instead of a queue data structure."

# Prerequisites

- `load-shedding` — a stack buffer is a load-shedding implementation.
- `queue-buffer` — a stack buffer shares the two-process design and is best understood by contrast with the queue buffer.

# Key Properties

1. Two processes, like the queue buffer, but uses a list (a stack) instead of a `queue` structure — Erlang lists give O(1) push and pop.
2. Good for low latency because it avoids bufferbloat: only a restricted number of old elements wait while newer ones keep reaching the worker promptly.
3. When the stack grows beyond a size limit, or an element is too old for QoS, the rest of the stack is dropped.
4. Major downside: messages are not processed in submission order — good for independent tasks, bad when event sequence matters.
5. *PO Box* also offers a stack-buffer implementation.

# Construction / Recognition

Spawn a buffer process that accumulates messages onto a list (stack). The worker pops the newest elements first. When the stack exceeds its size limit or its bottom element is too old, drop the remaining stack and continue.

# Context & Application

Use a stack buffer when low latency matters more than ordering. Under overload, new requests are served quickly; old requests that backed up get dropped en masse — a deliberate trade favoring recency.

# Examples

From Chapter 3, section "Stack Buffers": "If you get behind on a few messages being buffered in a queue, all the messages in the queue get to be slowed down and acquire milliseconds of wait time... a stack will make it so only a restricted number of elements are kept waiting while the newer ones keep making it to the server to be processed in a timely manner."

# Relationships

## Builds Upon
- `load-shedding` — a concrete implementation.
- `queue-buffer` — same two-process design, different data structure.

## Enables
Low-latency overload handling.

## Related
- `random-drop`, `time-sensitive-buffer` — other load-shedding implementations.

## Contrasts With
- `queue-buffer` — FIFO, preserves order, but every queued message accrues wait time; the stack buffer is LIFO, low-latency, but breaks ordering.

# Common Errors

- Using a stack buffer where event order must be preserved — submission order is not respected.

# Common Confusions

- The stack buffer does not eliminate old messages individually as they age; it drops "the rest of the stack" wholesale when a size or age limit is hit. Reacting to old events *before* they age out requires a time-sensitive buffer.

# Source Reference

Chapter 3: Planning for Overload, Section "Stack Buffers". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 3, section "Stack Buffers."
- Confidence rationale: high — mechanism, trade-off, and use case stated explicitly.
- Uncertainties: none.
- Cross-reference status: Verified
