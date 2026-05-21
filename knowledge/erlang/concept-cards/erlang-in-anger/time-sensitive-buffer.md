---
concept: Time-Sensitive Buffer
slug: time-sensitive-buffer
category: production-ops
subcategory: overload
tier: advanced
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Planning for Overload"
chapter_number: 3
pdf_page: null
section: "Time-Sensitive Buffers"
extraction_confidence: medium
aliases:
  - "Bucket buffer"
prerequisites:
  - load-shedding
  - stack-buffer
extends:
  - stack-buffer
related:
  - queue-buffer
  - random-drop
contrasts_with:
  - stack-buffer
answers_questions:
  - "How do I shed load while reacting to old events before they expire?"
---

# Quick Definition

A time-sensitive buffer is a load-shedding mechanism using multiple stacks ("buckets"), each holding a time slice, so an entire bucket of too-old requests can be dropped without discarding the whole buffer.

# Core Definition

From Chapter 3, section "Time-Sensitive Buffers": "If you need to react to old events *before* they are too old, then things become more complex... An interesting approach could be done with buckets, where multiple stacks are used, with each of them containing a given time slice. When requests get too old for the QoS constraints, drop an entire bucket, but not the entire buffer."

# Prerequisites

- `load-shedding` — a time-sensitive buffer is a load-shedding implementation.
- `stack-buffer` — it is built from multiple stacks and extends the stack-buffer idea.

# Key Properties

1. Uses multiple stacks (buckets), each holding a given time slice of requests.
2. When requests get too old for QoS constraints, an entire bucket is dropped — not the whole buffer.
3. Solves the inefficiency of constantly inspecting deep in a single stack to find and drop old elements.
4. Trade-off: great medians but poor 99th-percentile latencies — some requests are made much worse to benefit the majority.
5. Acceptable specifically because it occurs in a state where messages would be dropped anyway, and is preferable when low latency is genuinely required.

# Construction / Recognition

Maintain several stacks, each tagged with a time slice. Route incoming requests into the current bucket. When a bucket's time slice has aged past the QoS limit, drop that whole bucket and continue with the remaining buckets.

# Context & Application

Use a time-sensitive buffer when you must react to events before they age out *and* low latency matters — going beyond a plain stack buffer, which cannot efficiently identify aging elements.

# Examples

From Chapter 3, section "Time-Sensitive Buffers": "It may sound counter-intuitive to make some requests a lot worse to benefit the majority — you'll have great medians but poor 99 percentiles — but this happens in a state where you would drop messages anyway, and is preferable in cases where you do need low latency."

# Relationships

## Builds Upon
- `load-shedding` — a concrete implementation.
- `stack-buffer` — composed of multiple stacks.

## Enables
Age-aware load-shedding without scanning a single deep buffer.

## Related
- `queue-buffer`, `random-drop` — other load-shedding implementations.

## Contrasts With
- `stack-buffer` — a single stack cannot efficiently react to aging elements; the time-sensitive buffer partitions into time-sliced buckets to drop whole age groups.

# Common Errors

- Trying to react to old events by repeatedly scanning the bottom of a single stack — inefficient; partition into time-sliced buckets instead.

# Common Confusions

- Dropping a bucket harms the 99th percentile on purpose; this is an accepted trade because the alternative (in this overloaded state) is dropping messages anyway.

# Source Reference

Chapter 3: Planning for Overload, Section "Time-Sensitive Buffers". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 3, section "Time-Sensitive Buffers."
- Confidence rationale: medium — the source describes the bucket approach as "an interesting approach could be done," i.e. a sketch rather than a fully specified, named technique with a reference implementation.
- Uncertainties: no library implementation is cited for this variant, unlike queue and stack buffers (PO Box).
- Cross-reference status: Verified
