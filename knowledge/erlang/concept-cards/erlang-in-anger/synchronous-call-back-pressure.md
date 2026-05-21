---
concept: Synchronous Call Back-Pressure
slug: synchronous-call-back-pressure
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
  - "Synchronous calls for back-pressure"
prerequisites:
  - back-pressure
extends:
  - back-pressure
related:
  - timeout-selection
  - ask-for-permission
contrasts_with: []
answers_questions:
  - "What is back-pressure?"
  - "How do synchronous calls apply back-pressure?"
---

# Quick Definition

Synchronous call back-pressure is the most common way to apply back-pressure: making calls to an at-risk process synchronous so the caller must wait for a response before issuing the next request.

# Core Definition

From Chapter 3, section "Restricting Input": "The most common way to restrict data input is to make calls to a process whose queue would grow in uncontrollable ways synchronously. By requiring a response before moving on to the next request, you will generally ensure that the direct source of the problem will be slowed down."

# Prerequisites

- `back-pressure` — this is the canonical concrete mechanism for it.

# Key Properties

1. Calls to the at-risk process are made synchronous — the caller blocks until a response.
2. This slows the direct source of the problem automatically.
3. The bottleneck is usually deep inside the system, so the synchronicity must propagate level by level out to the edge.
4. It forces a hard question: choosing the timeout for each synchronous call.
5. Diagnosing it is hard — implicit back-pressure only manifests as a slower, less usable system, which mimics unrelated problems.

# Construction / Recognition

Convert asynchronous casts/sends to synchronous calls (`gen_server:call`) at the bottleneck. Then propagate the change outward through each layer until the edge can tell the user to slow down. Decide a timeout for every synchronous call (see `timeout-selection`).

# Context & Application

This is the default, simplest implementation of back-pressure. It requires no further optimization and instantly relieves queue growth, at the cost of user-visible slowness and the difficulty of choosing timeouts at every layer.

# Examples

From Chapter 3, section "Restricting Input": "when you introduce synchronous behaviour deep in the system, you'll possibly need to handle back-pressure, level by level, until you end up at the system's edges and can tell the user, 'please slow down.'"

# Relationships

## Builds Upon
- `back-pressure` — this is one realization of the strategy.

## Enables
Nothing further.

## Related
- `timeout-selection` — synchronous calls force timeout decisions.
- `ask-for-permission` — an alternative back-pressure mechanism that avoids making every layer synchronous.

## Contrasts With
Nothing directly.

# Common Errors

- Making only the edge synchronous; the deep queue still grows. Synchronicity must reach the bottleneck.
- Setting edge timeouts shorter than internal ones, causing operations to be reported as timed out at the edge even though they succeeded internally.

# Common Confusions

- Synchronous calls give back-pressure *implicitly* — you cannot easily tell from the outside that it is happening, only that the system is slow.

# Source Reference

Chapter 3: Planning for Overload, Section "Restricting Input". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 3, section "Restricting Input."
- Confidence rationale: high — explicitly described as the most common back-pressure mechanism.
- Uncertainties: none.
- Cross-reference status: Verified
