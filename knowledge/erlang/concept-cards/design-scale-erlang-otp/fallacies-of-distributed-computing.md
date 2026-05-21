---
# === CORE IDENTIFICATION ===
concept: Fallacies of Distributed Computing
slug: fallacies-of-distributed-computing

# === CLASSIFICATION ===
category: distribution
subcategory: distributed-systems-theory
tier: foundational

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Distributed Architectures"
chapter_number: 12
pdf_page: 378
section: "Networking — Fallacies of Distributed Computing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - distributed computing fallacies
  - Deutsch fallacies

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - network-partition
  - fault-tolerance
  - cap-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the fallacies of distributed computing?"
  - "What do I need to know before designing distributed architectures?"
---

# Quick Definition

The fallacies of distributed computing are a set of mistaken assumptions — such as "the network is reliable" — that engineers make when designing distributed systems, leading to disastrous consequences when those assumptions fail.

# Core Definition

The "fallacies of distributed computing" were "described by Peter Deutsch and his associates decades ago, but [are] just as relevant to the systems we design today" (Cesarini & Vinoski, p. 384). The central fallacy the chapter stresses is the belief that "your network is reliable and network partitions are rare" — in reality, "network issues occur when you least expect them, and if you are not handling all possible edge cases, the consequences and side effects can be disastrous" (p. 384). A consequence is that "it is impossible to differentiate between a node crash and a slow node" (p. 384).

# Prerequisites

This is a foundational concept with no prerequisites within this source. It frames the assumptions every distributed-system designer must guard against.

# Key Properties

1. The network is not reliable; partitions and congestion occur unpredictably.
2. A node crash and a slow node are indistinguishable from the outside.
3. Operations across nodes cost more CPU and I/O than local ones (serialization, virtualized interfaces, protocol handling).
4. Bandwidth is not unlimited; network latency affects end-to-end performance.
5. Nodes and machines come and go; topology changes during a system's lifetime.
6. The human factor counts: administrators make mistakes, ignore warnings, and may not even belong to the same organization.

# Construction / Recognition

## To Construct/Create:
This is not a constructed artifact. The procedure is to defend against the fallacies:
1. Map all errors that can occur in every workflow associated with a request.
2. Decide explicitly whether to return an error or retry on a different node.
3. Account for persistent side effects when retrying after a network error.
4. Handle topology changes and node churn programmatically.

## To Identify/Recognize:
1. Recognize a fallacy whenever a design silently assumes the network or another node is reliable, fast, or under your control.

# Context & Application

- **Typical contexts**: Designing the networking layer and failure handling of any distributed system.
- **Common applications**: Justifying retry strategies, monitoring, idempotence, and back-off algorithms.
- **Historical/stylistic notes**: The original fallacies paper notes that the network administrator might not even belong to the same organization (p. 384). Achieving resilience is even harder on cloud infrastructure where you do not control or know the network topology.

# Examples

**Example 1** (p. 384): If connectivity to a remote node goes down or gets congested, you cannot tell whether it is a network issue or the node has crashed or is slow — and if you retry on another node, you cannot be sure the first node did not already produce persistent side effects.

**Example 2** (p. 384): A network administrator tripping over network cables, messing up configurations, or holding different views on topology management — the human-factor fallacy.

# Relationships

## Builds Upon
- This is a foundational concept; it builds on nothing else within this source.

## Enables
- **Network partition** — Awareness of the fallacies motivates handling partitions
- **Fault tolerance** — The fallacies justify designing for predictable failure

## Related
- **Network partition** — A concrete manifestation of "the network is reliable" being false
- **Cap theorem** — Both express that delay and failure are inherent to distributed systems

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Assuming a non-responding node has crashed and retrying without idempotence
  **Correction**: Treat slow and dead nodes as indistinguishable; use unique identifiers and idempotent operations before retrying.

# Common Confusions

- **Confusion**: The fallacies are outdated since networks are now fast.
  **Clarification**: They remain just as relevant; cloud computing typically has slower instances and busier networks, making the problems harder, not easier (p. 385).

# Source Reference

Chapter 12: Distributed Architectures, "Networking — Fallacies of Distributed Computing," pages 384-385.

# Verification Notes

- Definition source: Direct quotes from pp. 384-385.
- Confidence rationale: HIGH — the source dedicates a named subsection to the fallacies.
- Uncertainties: The source references the fallacies by reputation rather than enumerating all eight; the card captures the ones the chapter emphasizes.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
