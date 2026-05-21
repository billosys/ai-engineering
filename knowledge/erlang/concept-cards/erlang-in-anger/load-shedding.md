---
concept: Load-Shedding
slug: load-shedding
category: production-ops
subcategory: overload
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Planning for Overload"
chapter_number: 3
pdf_page: null
section: "Discarding Data"
extraction_confidence: high
aliases:
  - "Discarding data"
  - "Dropping data"
prerequisites:
  - message-queue-overload
extends: []
related:
  - back-pressure
  - random-drop
  - queue-buffer
  - stack-buffer
contrasts_with:
  - back-pressure
answers_questions:
  - "What is load-shedding?"
  - "What are the two main classes of strategies to handle overload?"
  - "How does back-pressure relate to load-shedding?"
---

# Quick Definition

Load-shedding is an overload-management strategy that deliberately drops messages to avoid crashing when input cannot be slowed and the system cannot be scaled up.

# Core Definition

From Chapter 3, section "Discarding Data": "When nothing can slow down outside of your Erlang system and things can't be scaled up, you must either drop data or crash (which drops data that was in flight, for most cases, but with more violence)." And: "If you don't have the option of limiting how much data you receive, you then have to drop messages to avoid crashing."

Load-shedding is one of the two broad strategies for handling overload (the other being back-pressure).

# Prerequisites

- `message-queue-overload` — load-shedding is a response to queue growth.

# Key Properties

1. One of the two broad overload-management strategies (with back-pressure).
2. Used when input cannot be slowed externally and the system cannot scale up.
3. Deliberately drops messages — the alternative is crashing, which drops in-flight data anyway, but more violently.
4. Implementations include random drop, queue buffers, stack buffers, and time-sensitive buffers.
5. Dropping is best done at the producer level, not the receiver level — see `random-drop`.
6. Lampson's design hint, quoted in a footnote: "Shed load to control demand, rather than allowing the system to become overloaded."

# Construction / Recognition

Choose load-shedding when producers cannot be slowed and capacity cannot be added. Pick an implementation: random drop (simplest, most robust), queue buffer (more control, bursty overload), stack buffer (low-latency requirement), or time-sensitive buffer (must react to old events). Prefer dropping at the producer.

# Context & Application

Load-shedding is the strategy of last resort when back-pressure is impossible. The chapter notes it is psychologically hard — engineers are trained to keep useful data — but sometimes unavoidable. Telling users "N messages were dropped for reason X" makes it more acceptable (as in Heroku's logplex L10 errors).

# Examples

From Chapter 3, section "Discarding Data": "there's a point that can be reached where the data that comes in does so at a rate faster than it goes out, even if the Erlang system on its own is able to do everything fast enough. In some cases, It's the component *after* it that blocks." The chapter's drop implementations — random drop, queue/stack/time-sensitive buffers — are all forms of load-shedding.

# Relationships

## Builds Upon
- `message-queue-overload` — the problem it addresses.

## Enables
- `random-drop`, `queue-buffer`, `stack-buffer`, `time-sensitive-buffer` — its concrete implementations.

## Related
Nothing further.

## Contrasts With
- `back-pressure` — back-pressure slows the producer and keeps all data; load-shedding drops data. The chapter's exercises explicitly ask how to convert one into the other.

# Common Errors

- Refusing to shed load and instead letting the node crash — crashing drops in-flight data anyway, "but with more violence."
- Dropping at the receiver instead of the producer (see `random-drop`).

# Common Confusions

- Load-shedding is not the same as failure — it is a controlled choice to drop some data so the rest of the system survives.
- Load-shedding does not require slowing producers; that is back-pressure.

# Source Reference

Chapter 3: Planning for Overload, Section "Discarding Data". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 3, section "Discarding Data."
- Confidence rationale: high — explicitly named and defined as one of the two strategies.
- Uncertainties: none.
- Cross-reference status: Verified
