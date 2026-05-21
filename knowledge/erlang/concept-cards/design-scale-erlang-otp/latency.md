---
# === CORE IDENTIFICATION ===
concept: Latency
slug: latency

# === CLASSIFICATION ===
category: performance
subcategory: capacity
tier: foundational

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Scaling Out"
chapter_number: 14
pdf_page: 424
section: "Capacity Planning"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - response time

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - throughput
  - capacity-planning
  - littles-law
contrasts_with:
  - throughput

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is latency?"
  - "How does load affect latency?"
---

# Quick Definition

Latency is the time it takes to serve a particular request. It often rises with the number of simultaneous requests going through the system.

# Core Definition

"Latency is the time it takes to serve a particular request. Latency might vary depending on the load of your system, and is often correlated to the number of simultaneous requests going through it at any point in time. More simultaneous requests often means higher latency" (Cesarini & Vinoski, p. 429).

# Prerequisites

This is a foundational concept with no prerequisites within this source. It is one of the two core measures (with throughput) used throughout capacity planning.

# Key Properties

1. The time it takes to serve a particular request.
2. Varies with system load.
3. Correlated to the number of simultaneous requests in the system.
4. More simultaneous requests often means higher latency.
5. In a balanced Erlang system at maximum capacity, latency varies while throughput stays constant.

# Construction / Recognition

## To Construct/Create:
This is a measure, not an artifact. To measure it:
1. Time how long an individual request takes from arrival to completion.
2. Track it across load levels, correlating with the number of simultaneous requests.

## To Identify/Recognize:
1. Recognize latency as the per-request service time, distinct from the rate of work completed.

# Context & Application

- **Typical contexts**: Capacity planning, balancing, load regulation.
- **Common applications**: Verifying request times stay within service-level agreements; deciding when to apply load regulation.
- **Historical/stylistic notes**: In Little's Law, latency is the response time W in L = lambda*W.

# Examples

**Example 1** (p. 433): In a balanced Erlang system with constant 20,000 requests/second throughput, if 20,000 requests are in the system the peak latency is 1 second; if 40,000 are in the system simultaneously, latency doubles to 2 seconds.

**Example 2** (p. 460): After solving an EXIT-signal bug, the team monitored request latency and noticed it spiked every hour, exactly on the hour, from a few hundred milliseconds to a few seconds, traced to synchronous calls during log rotation.

# Relationships

## Builds Upon
- This is a foundational concept; it builds on nothing else within this source.

## Enables
- Latency is a core input to capacity planning, load regulation, and Little's Law.

## Related
- **Throughput** — The complementary capacity measure
- **Capacity planning** — Uses latency as a core measure
- **Littles law** — Latency is the response time W in L = lambda*W

## Contrasts With
- **Throughput** — Latency is per-request service time; throughput is the rate of work completed

# Common Errors

- **Error**: Expecting latency to stay constant as load grows
  **Correction**: More simultaneous requests usually mean higher latency, even when throughput stays constant.

# Common Confusions

- **Confusion**: Latency and throughput are the same measure.
  **Clarification**: Latency is the time for one request; throughput is the rate of requests completed — in a balanced Erlang system, throughput holds constant while latency rises.

# Source Reference

Chapter 14: Scaling Out, "Capacity Planning," page 429, and "Balancing Your System," page 433.

# Verification Notes

- Definition source: Direct quote from p. 429.
- Confidence rationale: HIGH — the source explicitly defines latency.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
