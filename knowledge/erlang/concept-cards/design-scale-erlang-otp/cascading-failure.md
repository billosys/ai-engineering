---
# === CORE IDENTIFICATION ===
concept: Cascading Failure
slug: cascading-failure

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: failure-modes
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Systems That Never Stop"
chapter_number: 13
pdf_page: 402
section: "Resilience — Back-Off Algorithms in Clients"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - cascading failures
  - retry storm

# === TYPED RELATIONSHIPS ===
prerequisites:
  - resilience
extends: []
related:
  - back-off-algorithm
  - load-regulation
  - backpressure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a cascading failure?"
  - "How do I prevent retry surges after an outage?"
---

# Quick Definition

A cascading failure is a chain reaction in which an overload causes some nodes to fail, increasing the load on the survivors until they fail too, taking out the system batch by batch.

# Core Definition

When an outage causes all clients to reconnect and retry at once, "this surge increases for every second of downtime, hitting the system with force as soon as it becomes operational again. If not handled properly, this will cause more front-end nodes to terminate, creating an even larger surge on the remaining ones and taking out the next batch until there are none left. This is what we call a cascading failure, something you need to guard against in both your client and server" (Cesarini & Vinoski, p. 405).

# Prerequisites

- **Resilience** — Cascading failure is the failure mode resilience and back-off must guard against; understand resilience first.

# Key Properties

1. A chain reaction triggered by overload.
2. Failure of some nodes shifts their load onto the survivors.
3. The increased load causes the next batch of nodes to fail.
4. The process repeats until no nodes remain.
5. Commonly triggered by a post-outage retry surge from many clients.
6. Must be guarded against in both client and server.

# Construction / Recognition

## To Construct/Create:
This is a failure mode to prevent, not to build. To guard against it:
1. Use back-off algorithms in clients to smooth the post-outage retry surge.
2. Apply load regulation and backpressure in servers.
3. Ensure capacity planning leaves headroom so losing a node does not overload survivors.

## To Identify/Recognize:
1. Recognize a cascading failure when node failures progressively overload and take out the remaining nodes.

# Context & Application

- **Typical contexts**: Systems with many connected devices recovering from an outage.
- **Common applications**: Justifying back-off algorithms, load regulation, and capacity headroom.
- **Historical/stylistic notes**: The surge that triggers a cascading failure grows for every second of downtime, so longer outages produce worse cascades.

# Examples

**Example 1** (p. 405): A system with millions of connected devices and a 1-minute outage — all devices reconnect at once; the surge terminates front-end nodes, the survivors get an even larger surge, and the failure cascades until none are left.

**Example 2** (p. 405): The book prescribes back-off algorithms in clients (and load handling in servers) precisely to guard against this cascading failure.

# Relationships

## Builds Upon
- **Resilience** — Cascading failure is what resilient design must prevent

## Enables
- Understanding cascading failure motivates back-off, load regulation, and backpressure.

## Related
- **Back-off algorithm** — Guards against cascading failure on the client side
- **Load regulation** — Guards against cascading failure on the server side
- **Backpressure** — Rejects excess load to prevent cascades

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Guarding against retry surges only on the client
  **Correction**: Cascading failure must be guarded against in both client and server.

# Common Confusions

- **Confusion**: A cascading failure is just a single node crash.
  **Clarification**: It is a chain reaction — each failure shifts load onto survivors, causing the next batch to fail until the system is gone.

# Source Reference

Chapter 13: Systems That Never Stop, "Resilience — Back-Off Algorithms in Clients," page 405.

# Verification Notes

- Definition source: Direct quote from p. 405.
- Confidence rationale: HIGH — the source explicitly names and defines cascading failure.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
