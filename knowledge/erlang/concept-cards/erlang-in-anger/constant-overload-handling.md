---
concept: Constant Overload Handling
slug: constant-overload-handling
category: production-ops
subcategory: overload
tier: advanced
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Planning for Overload"
chapter_number: 3
pdf_page: null
section: "Dealing With Constant Overload"
extraction_confidence: high
aliases:
  - "Dealing with constant overload"
prerequisites:
  - load-shedding
  - queue-buffer
extends: []
related:
  - random-drop
  - stack-buffer
contrasts_with:
  - queue-buffer
answers_questions:
  - "How do I handle a system that is under constant overload?"
---

# Quick Definition

Constant overload handling addresses systems where input never drops back down: instead of buffers (which assume a catch-up period), it spreads load across many processes or uses ETS tables as locks and counters.

# Core Definition

From Chapter 3, section "Dealing With Constant Overload": "Being under constant overload may require a new solution. Whereas both queues and buffers will be great for cases where overload happens from time to time... they both work more reliably when you expect the input rate to eventually drop, letting you catch up."

Two approaches are recommended: "Have many processes that act as buffers and load-balance through them (scale horizontally)" and "use ETS tables as locks and counters (reduce the input)."

# Prerequisites

- `load-shedding` — constant overload handling is an overload-management context.
- `queue-buffer` — understanding why buffers fail here (they assume a catch-up period) motivates these approaches.

# Key Properties

1. Buffers (queue/stack) are unreliable under constant overload because they assume the input rate eventually drops.
2. Approach 1 — horizontal scaling: N processes share the load; pick one (randomly, with even distribution) and send to it. No state communication needed, insensitive to failure.
3. Approach 2 — ETS locks/counters: before sending, atomically update an ETS counter against a known shared limit; each request must clear the limit first.
4. ETS tables handle far more requests per second than a process, but support only basic operations (a single read, atomic counter add/remove).
5. Both approaches require ETS tables.
6. To avoid dynamically-generated atoms, register workers in an ETS table with `read_concurrency` set to `true` rather than via named processes.

# Construction / Recognition

For horizontal scaling: spawn N worker/buffer processes, register them (preferably in an ETS table with `read_concurrency`), and randomly pick one per message. For locks/counters: before sending, call `ets:update_counter/3` against a shared limit; proceed only if the limit is not exceeded.

# Context & Application

Used when overload is permanent, not bursty. The `lhttpc` library uses the horizontal-scaling approach (per-domain load balancers). The `dispcount` library uses the counters/locks approach to avoid message queues and guarantee low-latency responses even for denied requests.

# Examples

From Chapter 3, section "Dealing With Constant Overload": "An approach similar to this one is used in the `lhttpc` library... to split load balancers on a per-domain basis." And: the counters approach "has been used in `dispcount` to avoid message queues, and to guarantee low-latency responses to any message that won't be handled."

# Relationships

## Builds Upon
- `load-shedding` — the broader strategy family.

## Enables
Survivable operation under permanent overload.

## Related
- `random-drop`, `stack-buffer` — load-shedding tools for bursty overload.

## Contrasts With
- `queue-buffer` — queue and stack buffers handle *intermittent* overload by buffering until input drops; constant overload handling assumes input never drops and instead scales out or gates with ETS counters.

# Common Errors

- Relying on queue or stack buffers under constant overload — they assume a catch-up period that never comes.
- Generating atoms dynamically to name workers — use an ETS registry with `read_concurrency` instead.

# Common Confusions

- ETS counters reduce input by *gating* it (each request clears a limit), not by buffering it — denied requests are rejected immediately, allowing low-latency failure.

# Source Reference

Chapter 3: Planning for Overload, Section "Dealing With Constant Overload". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 3, section "Dealing With Constant Overload."
- Confidence rationale: high — both approaches and their library examples are explicit.
- Uncertainties: none.
- Cross-reference status: Verified
