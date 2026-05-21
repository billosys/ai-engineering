---
concept: Back-Pressure
slug: back-pressure
category: production-ops
subcategory: overload
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Planning for Overload"
chapter_number: 3
pdf_page: null
section: "Restricting Input"
extraction_confidence: high
aliases:
  - "Restricting input"
prerequisites:
  - message-queue-overload
  - true-bottleneck
extends: []
related:
  - load-shedding
  - synchronous-call-back-pressure
  - timeout-selection
  - ask-for-permission
contrasts_with:
  - load-shedding
answers_questions:
  - "What is back-pressure?"
  - "What are the two main classes of strategies to handle overload?"
  - "How does back-pressure relate to load-shedding?"
---

# Quick Definition

Back-pressure is an overload-management strategy that restricts input by slowing the producer down, propagating "please slow down" from the bottleneck out to the system's edge.

# Core Definition

From Chapter 3, section "Restricting Input": "Restricting input is the simplest way to manage message queue growth in Erlang systems. It's the simplest approach because it basically means you're slowing the user down (applying *back-pressure*), which instantly fixes the problem without any further optimization required. On the other hand, it can lead to a really crappy experience for the user."

Back-pressure is one of the two broad strategies for handling overload (the other being load-shedding).

# Prerequisites

- `message-queue-overload` — back-pressure is a response to queue growth.
- `true-bottleneck` — back-pressure must originate at the bottleneck and propagate outward.

# Key Properties

1. One of the two broad overload-management strategies (with load-shedding).
2. Works by slowing the producer rather than dropping data — no data is lost.
3. Instantly fixes the problem with no further optimization, but degrades the user experience.
4. Commonly implemented by making calls to the at-risk process synchronous, forcing a response before the next request.
5. Because the bottleneck is deep in the system, back-pressure must be handled level by level until it reaches the edge, where the user can be told to slow down.
6. Can be made explicit (asking for permission) or implicit (synchronous calls); implicit back-pressure is hard to diagnose.

# Construction / Recognition

Introduce synchronous behaviour at the bottleneck so callers must wait for a response. Propagate that synchronicity outward, level by level, to the system edge. Alternatively, gate the bottleneck resource behind an "ask for permission" interface, or impose per-user API limits at entry points.

# Context & Application

Back-pressure is the right choice when you can afford to slow producers down and must not lose data. It guarantees a basic quality of service and lets you allocate resources fairly (or unfairly) — e.g. per-user API limits.

# Examples

From Chapter 3, section "Restricting Input": "when you introduce synchronous behaviour deep in the system, you'll possibly need to handle back-pressure, level by level, until you end up at the system's edges and can tell the user, 'please slow down.'" Developers often "put API limits per user on the system entry points."

# Relationships

## Builds Upon
- `message-queue-overload`, `true-bottleneck` — the problem and its locus.

## Enables
- `synchronous-call-back-pressure`, `ask-for-permission` — concrete mechanisms.

## Related
- `timeout-selection` — synchronous back-pressure forces timeout decisions.

## Contrasts With
- `load-shedding` — back-pressure slows the producer and keeps all data; load-shedding drops data instead. The chapter's exercises explicitly ask how to convert one into the other.

# Common Errors

- Introducing synchronous calls only at the edge, not at the bottleneck — the queue deep inside still grows.
- Relying on implicit back-pressure and then being unable to tell overload apart from bad hardware, slow networks, or a slow client.

# Common Confusions

- Back-pressure does not discard data; that is load-shedding. Back-pressure preserves data by making the producer wait.
- Slower system responsiveness is a *symptom* of implicit back-pressure, not proof of it — it can also indicate unrelated problems.

# Source Reference

Chapter 3: Planning for Overload, Section "Restricting Input". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 3, section "Restricting Input."
- Confidence rationale: high — explicitly named and defined as one of the two strategies.
- Uncertainties: none.
- Cross-reference status: Verified
