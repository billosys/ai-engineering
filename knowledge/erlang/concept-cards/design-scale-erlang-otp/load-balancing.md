---
# === CORE IDENTIFICATION ===
concept: Load Balancing
slug: load-balancing

# === CLASSIFICATION ===
category: distribution
subcategory: scaling-techniques
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Systems That Never Stop"
chapter_number: 13
pdf_page: 402
section: "Reliability"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - load balancer
  - load balancing

# === TYPED RELATIONSHIPS ===
prerequisites:
  - front-end-node
extends: []
related:
  - redundancy
  - single-point-of-failure
  - load-regulation
  - share-nothing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is load balancing?"
  - "How are requests distributed across front-end nodes?"
---

# Quick Definition

Load balancing distributes incoming requests across multiple front-end nodes using a strategy such as random, round robin, hashing, or least-load selection.

# Core Definition

"Your request hits one of the load balancers, which forwards it to one of the front-end nodes. The node used is chosen by the load balancer using a variety of strategies — random, round robin, hashing, or sending the request to the front-end node with the least CPU load or the one with the smallest number of open TCP connections" (Cesarini & Vinoski, p. 407). The authors "prefer hashing algorithms, as they are fast and give you predictability and consistency with low overheads."

# Prerequisites

- **Front-end node** — Load balancers distribute requests across front-end nodes; understand them first.

# Key Properties

1. Distributes incoming requests across multiple front-end nodes.
2. Strategies include random, round robin, hashing, least CPU load, and fewest open TCP connections.
3. Hashing algorithms are preferred — fast, predictable, consistent, low overhead.
4. A deterministic route across nodes makes debugging easier.
5. Load balancers can also throttle simultaneously connected users and control inbound request rate.
6. Load balancers themselves can become bottlenecks and may need stress testing.

# Construction / Recognition

## To Construct/Create:
1. Place one or more load balancers in front of the front-end nodes.
2. Choose a balancing strategy (hashing is preferred for predictability).
3. Optionally configure the balancer to throttle connections and inbound request rate.

## To Identify/Recognize:
1. Recognize load balancing as a layer that selects a target front-end node per request by a defined strategy.

# Context & Application

- **Typical contexts**: Distributing client load across redundant front-end nodes.
- **Common applications**: Avoiding single points of failure, routing requests to logic nodes holding session data, controlling load (chapter 14).
- **Historical/stylistic notes**: Deterministic routing helps when troubleshooting across hundreds of nodes with decentralized logs.

# Examples

**Example 1** (p. 407): A load balancer chooses a front-end node by random, round robin, hashing, least CPU load, or fewest open TCP connections — the authors prefer hashing for predictability.

**Example 2** (p. 411, Figure 14-5): In a share-nothing architecture, load balancers forward client login requests to front-end nodes, which forward them to their primary logic nodes; future requests must be routed to the logic node holding the session.

# Relationships

## Builds Upon
- **Front-end node** — Load balancers distribute requests across front-end nodes

## Enables
- Load balancing enables request distribution across redundant nodes and routing to session-holding nodes.

## Related
- **Redundancy** — Load balancing distributes load across redundant front-end nodes
- **Single point of failure** — Load balancers route around failed front-end nodes
- **Load regulation** — Load balancers can also throttle and regulate inbound load
- **Share nothing** — Share-nothing routing depends on consistent load-balancer choices

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Routing a returning client's request to a different logic node than the one holding its session
  **Correction**: With share-nothing, route each request to the logic node that stores its matching session data.

# Common Confusions

- **Confusion**: A load balancer cannot fail.
  **Clarification**: Load balancers themselves can become bottlenecks and crash under heavy load; they may need stress testing too.

# Source Reference

Chapter 13: Systems That Never Stop, "Reliability," page 407, and "Sharing Data" examples, pages 411-412. Load-balancer throttling is revisited in Chapter 14, pages 439-440.

# Verification Notes

- Definition source: Direct quote from p. 407.
- Confidence rationale: HIGH — the source explicitly describes load-balancing strategies.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
