---
# === CORE IDENTIFICATION ===
concept: Message Delivery Semantics
slug: message-delivery-semantics

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: retry-strategies
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Systems That Never Stop"
chapter_number: 13
pdf_page: 402
section: "Reliability — At most once, exactly once, and at least once"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - delivery guarantees
  - "at most once"
  - "at least once"
  - "exactly once"
  - retry strategy

# === TYPED RELATIONSHIPS ===
prerequisites:
  - fault-tolerance
extends: []
related:
  - idempotence
  - consistency-availability-tradeoff
  - sharing-data
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are at-most-once, at-least-once, and exactly-once semantics?"
  - "How do I pick a retry strategy for a request?"
---

# Quick Definition

Message delivery semantics are the three guarantees — at most once, at least once, and exactly once — that you can choose for each request, mapping how requests are retried across nodes in a distributed system.

# Core Definition

"There are three approaches you can take for every request, because how you handle requests maps to message delivery semantics across nodes in distributed systems" (Cesarini & Vinoski, p. 408). At most once means you "send your request and forget about it" — acceptable when occasional loss is fine. At least once gives the only guarantee that "your request has been executed at least once," at the cost of storing request state, monitoring it, and forwarding on timeout. Exactly once requires "providing guarantees when executing what is in effect a transaction. The request can succeed or fail, but nothing in between" (p. 409) — but "these guarantees are impossible with distributed systems, since failure can also mean a request being successfully executed but its acknowledgment and reply being lost" (p. 410).

# Prerequisites

- **Fault tolerance** — Delivery semantics are the per-request retry strategies that implement fault tolerance.

# Key Properties

1. Three approaches: at most once, at least once, exactly once.
2. At most once — send and forget; cheapest, least memory/CPU; loss is possible without affecting other requests.
3. At least once — guarantees execution on at least one node; requires storing/monitoring request state and forwarding on error.
4. Exactly once — request succeeds or fails entirely; the hardest, most expensive strategy.
5. Exactly-once guarantees cannot truly be provided across distributed systems.
6. The strategy is chosen per interface function based on all failure scenarios in the call chain.

# Construction / Recognition

## To Construct/Create:
1. For each interface function, examine all failure scenarios — software, hardware, network.
2. Choose at most once for loss-tolerant requests (SMS, instant messages).
3. Choose at least once where a request must execute somewhere, accepting possible duplication.
4. Choose exactly once for money/transactional requests, using unique sequence numbers and idempotence.

## To Identify/Recognize:
1. Recognize the strategy by whether a request may be lost (at most once), duplicated (at least once), or guaranteed once (exactly once).

# Context & Application

- **Typical contexts**: Picking a retry strategy for every external call (step 5 of the architecture design).
- **Common applications**: At most once for SMS/IM; at least once for resilient logins; exactly once for billing and money transfers.
- **Historical/stylistic notes**: A system often ends up with a mixture of all three strategies depending on the importance of each state change (p. 417).

# Examples

**Example 1** (p. 408): With the no-single-point-of-failure example, if the first logic node is slow and the front-end node succeeds with another, the worst case under at-least-once is logging on twice with two sessions, one of which expires.

**Example 2** (pp. 409-410): A billing system for premium-rate SMS uses exactly-once semantics — reserving funds before sending, charging only on the first delivery report, with subsequent delivery reports not causing additional charges.

# Relationships

## Builds Upon
- **Fault tolerance** — Delivery semantics are the per-request retry strategies of fault tolerance

## Enables
- Choosing delivery semantics enables correct, cost-appropriate failure handling per request.

## Related
- **Idempotence** — Exactly-once with at-most-once calls relies on idempotence
- **Consistency-availability tradeoff** — Exactly-once favors consistency, at-least-once is the compromise
- **Sharing data** — Retry strategy and data-sharing strategy must be chosen together

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Using exactly-once for every request
  **Correction**: Exactly-once is the most expensive; use it only for the subset of requests (e.g., money) that require it, and at-most-once where loss is acceptable.

# Common Confusions

- **Confusion**: Exactly-once delivery can be guaranteed in a distributed system.
  **Clarification**: It cannot — failure can mean a request executed successfully but its acknowledgment and reply were lost.

# Source Reference

Chapter 13: Systems That Never Stop, "Reliability — At most once, exactly once, and at least once," pages 408-411. See Figure 14-4.

# Verification Notes

- Definition source: Direct quotes from pp. 408-410.
- Confidence rationale: HIGH — the source dedicates a named subsection to the three semantics.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
