---
# === CORE IDENTIFICATION ===
concept: Consistency-Availability Tradeoff
slug: consistency-availability-tradeoff

# === CLASSIFICATION ===
category: distribution
subcategory: distributed-systems-theory
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Systems That Never Stop"
chapter_number: 13
pdf_page: 402
section: "Tradeoffs Between Consistency and Availability"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - consistency vs availability
  - distributed-system tradeoffs

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cap-theorem
  - message-delivery-semantics
extends: []
related:
  - sharing-data
  - eventual-consistency
  - scalability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the tradeoff between consistency and availability?"
  - "How do retry and data-sharing strategies affect consistency and availability?"
---

# Quick Definition

The consistency-availability tradeoff is the recognition that a distributed system must give up some consistency to gain availability, or vice versa — choices made through its recovery and data-sharing strategies.

# Core Definition

"The choices you make in your recovery strategy are all about tradeoffs between consistency and availability, while your data-sharing strategy is about tradeoffs between latency and consistency" (Cesarini & Vinoski, p. 420). On one side is the exactly-once approach — strong consistency, least available; on the other is weak consistency with high availability. The at-least-once approach is the compromise. "Nirvana would be reaching the top right of both graphs: a system that is consistent, reliable, and available ... Alas, having it all is not possible" (p. 421).

# Prerequisites

- **CAP theorem** — The tradeoff is the practical face of CAP; understand CAP first.
- **Message delivery semantics** — The retry strategy is one axis of the tradeoff.

# Key Properties

1. Recovery-strategy choices trade off consistency against availability.
2. Data-sharing-strategy choices trade off latency against consistency.
3. Exactly-once is the most consistent but least available approach.
4. Weak consistency with high availability lets you keep servicing requests under partitions.
5. At-least-once is the compromise — guarantees execution on at least one node, leaving propagation/merging to the system.
6. A consistent, reliable, and available system ("nirvana") is not achievable in practice.

# Construction / Recognition

## To Construct/Create:
1. For each request, choose a retry strategy on the consistency-versus-availability axis.
2. For each table/state, choose a sharing strategy on the latency-versus-consistency axis.
3. Accept that you cannot have full consistency, reliability, and availability at once.
4. Base the tradeoff on system requirements, customer guarantees, and operational cost.

## To Identify/Recognize:
1. Recognize the tradeoff whenever increasing one of consistency or availability forces the other down.

# Context & Application

- **Typical contexts**: Choosing recovery and data-sharing strategies for a distributed system.
- **Common applications**: Deciding exactly-once vs at-least-once per request; deciding share-everything vs share-something per table.
- **Historical/stylistic notes**: The same choices also trade off scalability — covered further in chapter 14 ("Scalability tradeoffs," p. 429).

# Examples

**Example 1** (pp. 419-420, Figure 14-9 part 1): Exactly-once strong-consistency requirements mean choosing consistency over availability — under some circumstances the system becomes unavailable to ensure consistency.

**Example 2** (p. 420, Figure 14-9 part 2): Using share-everything makes a system more reliable, since any node with a copy of the data can correctly take over a request — a tradeoff between availability and reliability.

# Relationships

## Builds Upon
- **Cap theorem** — The tradeoff is CAP applied to design choices
- **Message delivery semantics** — The retry strategy is one axis

## Enables
- Understanding the tradeoff enables deliberate, requirement-driven design choices.

## Related
- **Sharing data** — The data-sharing strategy is the latency-vs-consistency axis
- **Eventual consistency** — The weak-consistency, high-availability option
- **Scalability** — The same choices also affect scalability

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Trying to design a system that is fully consistent, reliable, and available
  **Correction**: Having it all is not possible; choose tradeoffs wisely based on requirements and cost.

# Common Confusions

- **Confusion**: Availability and reliability are the same axis in the tradeoff.
  **Clarification**: Recovery strategy trades consistency against availability; data-sharing trades latency against consistency, and also availability against reliability — they are distinct axes (Figure 14-9).

# Source Reference

Chapter 13: Systems That Never Stop, "Tradeoffs Between Consistency and Availability," pages 419-421. See Figure 14-9.

# Verification Notes

- Definition source: Direct quote from p. 420.
- Confidence rationale: HIGH — the source dedicates a named section to the tradeoff with a two-part figure.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
