---
# === CORE IDENTIFICATION ===
concept: Backpressure
slug: backpressure

# === CLASSIFICATION ===
category: performance
subcategory: load-control
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Scaling Out"
chapter_number: 14
pdf_page: 424
section: "Load Regulation and Backpressure"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - backpressure

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bottleneck
extends: []
related:
  - load-regulation
  - synchronous-load-regulation
  - cascading-failure
contrasts_with:
  - load-regulation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is backpressure?"
  - "What distinguishes backpressure from load regulation?"
---

# Quick Definition

Backpressure is the approach of telling the sender to stop sending because there is no room for new messages — rejecting requests rather than queuing them.

# Core Definition

"Backpressure is the approach of telling the sender to stop sending because there's no room for new messages" (Cesarini & Vinoski, p. 439). The book contrasts it with load regulation: "the difference is that load regulation allows you to keep and remember requests by imposing limits on the number of simultaneous connections and throttling requests using queues, while backpressure rejects them" (p. 439).

# Prerequisites

- **Bottleneck** — Backpressure manages load that would otherwise create bottlenecks; understand bottlenecks first.

# Key Properties

1. Tells the sender to stop sending because there is no room for new messages.
2. Rejects requests rather than queuing them.
3. Together with load regulation, keeps throughput and latency predictable under overload.
4. Prevents the system from failing as a result of overload.
5. Can be triggered in front-end nodes when downstream queues overflow.

# Construction / Recognition

## To Construct/Create:
1. Detect when there is no room for new messages (e.g., a queue has overflowed).
2. Signal the sender to stop sending.
3. Reject incoming requests until capacity is available again.

## To Identify/Recognize:
1. Recognize backpressure when a system refuses new requests instead of accepting and queuing them.

# Context & Application

- **Typical contexts**: Systems that must not fail under overload, e.g., a game back end at massive scale.
- **Common applications**: Rejecting requests in bulk in front-end nodes when downstream gateway queues overflow.
- **Historical/stylistic notes**: The classic example is the telephone network — calling an international trunk with no available lines returns a busy tone, so you keep trying until you get through (p. 438).

# Examples

**Example 1** (p. 438): On New Year's Eve, the phone network used backpressure — you always got a dial tone, but a call to a full international trunk was rejected with a busy tone.

**Example 2** (pp. 439-440, Figure 15-7): When a load-regulation queue overflows, the gateway rejects SMSs — individually in logic nodes or in bulk by triggering backpressure in the front-end nodes.

# Relationships

## Builds Upon
- **Bottleneck** — Backpressure manages load that would create bottlenecks

## Enables
- Backpressure enables a system to survive overload by rejecting excess requests.

## Related
- **Load regulation** — The complementary load-control technique
- **Synchronous calls for flow control** — Synchronous calls are a form of backpressure on producers
- **Cascading failure** — Backpressure guards against overload-driven cascades

## Contrasts With
- **Load regulation** — Backpressure rejects requests; load regulation queues and remembers them

# Common Errors

- **Error**: Relying solely on queuing under sustained overload
  **Correction**: If requests keep arriving faster than they can be handled, you must stop queuing and start applying backpressure (rejecting).

# Common Confusions

- **Confusion**: Backpressure and load regulation are the same.
  **Clarification**: Backpressure rejects requests; load regulation queues and remembers them — they are complementary, not identical.

# Source Reference

Chapter 14: Scaling Out, "Load Regulation and Backpressure," pages 438-441. See Figure 15-7.

# Verification Notes

- Definition source: Direct quote from p. 439.
- Confidence rationale: HIGH — the source explicitly defines backpressure and contrasts it with load regulation.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
