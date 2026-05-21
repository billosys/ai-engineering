---
# === CORE IDENTIFICATION ===
concept: Back-Off Algorithm
slug: back-off-algorithm

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
section: "Resilience — Back-Off Algorithms in Clients"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - backoff algorithm
  - exponential back-off
  - random back-off

# === TYPED RELATIONSHIPS ===
prerequisites:
  - resilience
extends: []
related:
  - cascading-failure
  - load-regulation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a back-off algorithm?"
  - "How do I prevent retry surges after an outage?"
---

# Quick Definition

A back-off algorithm regulates the frequency of a client's retries after a failure, increasing the interval between attempts to avoid overwhelming a recovering system.

# Core Definition

"If you have a client that automatically tries to reconnect and send a request after a failure, make sure it uses a back-off algorithm to regulate the frequency of its retries" (Cesarini & Vinoski, p. 405). Without it, an outage causes all devices to retry simultaneously, "creating a surge in traffic" that can take out front-end nodes one batch after another — a cascading failure. The algorithm "will control the surge in failed retry attempts coming at the same time, allowing the system to recover and continue functioning even after a failure" (p. 406).

# Prerequisites

- **Resilience** — Back-off algorithms support recovery after failure; understand resilience first.

# Key Properties

1. Regulates the frequency of a client's retries after failure.
2. Increases the interval between successive retries.
3. The Fibonacci variant increases intervals as 1, 2, 3, 5, 8, 13... seconds, capped at a large value (89, 144, or more).
4. An exponential back-off algorithm increases the retry interval exponentially.
5. A random back-off algorithm uses random delays so multiple nodes retry at different times.
6. It guards against cascading failure by smoothing the post-outage retry surge.

# Construction / Recognition

## To Construct/Create:
1. On each failed retry, increase the wait before the next attempt.
2. Choose a growth pattern: Fibonacci, exponential, or random.
3. Cap the interval at a large maximum value.
4. Optionally randomize delays so nodes do not retry in lockstep.

## To Identify/Recognize:
1. Recognize a back-off algorithm when successive retry intervals grow rather than staying constant.

# Context & Application

- **Typical contexts**: Clients (and servers) of systems with millions of connected devices.
- **Common applications**: Reconnecting after an outage without causing a traffic surge.
- **Historical/stylistic notes**: The algorithm that best suits a system depends on its characteristics; random delays help when many nodes would otherwise retry simultaneously.

# Examples

**Example 1** (p. 405): A system with millions of connected devices and a 1-minute outage — without back-off, all devices retry at once, the surge grows for every second of downtime, and front-end nodes terminate in a cascading failure.

**Example 2** (p. 405): The Fibonacci-based back-off increases the retry interval from 1 second to 2, 3, 5, 8, and 13 seconds, capped at a large number such as 89 or 144 seconds.

# Relationships

## Builds Upon
- **Resilience** — Back-off algorithms support post-failure recovery

## Enables
- Back-off algorithms enable safe client reconnection without overwhelming a recovering system.

## Related
- **Cascading failure** — Back-off algorithms guard against cascading failure
- **Load regulation** — Both control the rate of requests to protect a system

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Having clients retry at a fixed, immediate interval after failure
  **Correction**: Use a back-off algorithm so retries spread out and do not surge the recovering system.

# Common Confusions

- **Confusion**: Back-off only needs to be implemented in the client.
  **Clarification**: Cascading failure must be guarded against "in both your client and server" (p. 405).

# Source Reference

Chapter 13: Systems That Never Stop, "Resilience — Back-Off Algorithms in Clients," pages 405-406.

# Verification Notes

- Definition source: Direct quote from p. 405.
- Confidence rationale: HIGH — the source explicitly defines back-off algorithms and names three variants.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
