---
# === CORE IDENTIFICATION ===
concept: Little's Law
slug: littles-law

# === CLASSIFICATION ===
category: performance
subcategory: load-control
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Scaling Out"
chapter_number: 14
pdf_page: 424
section: "Load Regulation and Backpressure — Little's Law"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - Little's law
  - "L = lambda W"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - load-regulation
extends: []
related:
  - backpressure
  - throughput
  - latency
  - amdahls-law
contrasts_with:
  - amdahls-law

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Little's Law?"
  - "How are queue length, arrival rate, and response time related?"
---

# Quick Definition

Little's Law states that queue length equals arrival rate multiplied by response time (L = λW); rearranged, response time equals queue length divided by arrival rate.

# Core Definition

"Little's Law is an equation L = λW stating that the queue length, L, is equal to the arrival rate, λ, multiplied by the response time, W. In most Internet-connected programs, the queue length is the number of client requests waiting to be (and currently being) serviced, the arrival rate is the number of client requests per time unit being accepted into and serviced by the system, and the response time is how long it takes to service one client request. Reorganizing the parameters in the equation, we get response time = queue length / arrival rate" (Cesarini & Vinoski, p. 439).

# Prerequisites

- **Load regulation** — Little's Law explains why controlling queue length controls response time, the basis of load regulation.

# Key Properties

1. The equation is L = λW: queue length = arrival rate × response time.
2. Queue length L is the number of client requests waiting and being serviced.
3. Arrival rate λ is the number of client requests per time unit accepted and serviced.
4. Response time W is how long it takes to service one client request.
5. Rearranged: response time = queue length / arrival rate.
6. You cannot control arrival rate, but you can control queue length (backpressure) and throughput (removing bottlenecks).

# Construction / Recognition

## To Construct/Create:
This is a law to apply, not an artifact. To apply it:
1. Identify queue length, arrival rate, and response time for the system.
2. Use response time = queue length / arrival rate to reason about latency.
3. Control queue length via backpressure and throughput via bottleneck removal to control response time.

## To Identify/Recognize:
1. Recognize Little's Law's effect when a longer queue or lower throughput raises response time.

# Context & Application

- **Typical contexts**: Reasoning about load regulation and backpressure.
- **Common applications**: Deciding when to apply backpressure to keep response time bounded.
- **Historical/stylistic notes**: "The key to getting the values right and applying backpressure at the right time is to have full visibility of what is going on in your system and to measure it" (p. 439).

# Examples

**Example 1** (p. 439): If the queue length gets longer or the arrival rate (or throughput) decreases, the response time will go up — directly from response time = queue length / arrival rate.

**Example 2** (p. 439): In a live system you cannot control the arrival rate, but you can control queue length by applying backpressure and throughput by removing bottlenecks, thereby controlling response time.

# Relationships

## Builds Upon
- **Load regulation** — Little's Law justifies controlling queue length to control response time

## Enables
- Little's Law enables principled decisions about when to apply backpressure.

## Related
- **Backpressure** — Backpressure controls the queue-length term L
- **Throughput** — Throughput corresponds to the arrival-rate term in a balanced system
- **Latency** — Response time W is latency

## Contrasts With
- **Amdahls law** — Both are quantitative laws in the chapter; Little's Law relates queue length, arrival rate, and response time, while Amdahl's Law concerns parallel speedup

# Common Errors

- **Error**: Trying to control response time by controlling the arrival rate
  **Correction**: You cannot control the arrival rate; control queue length (backpressure) and throughput (bottleneck removal) instead.

# Common Confusions

- **Confusion**: Little's Law applies only to physical queues.
  **Clarification**: In Internet-connected programs, L is the number of client requests waiting and being serviced — the law applies to the request-processing path generally.

# Source Reference

Chapter 14: Scaling Out, "Load Regulation and Backpressure — Little's Law," page 439.

# Verification Notes

- Definition source: Direct quote from p. 439.
- Confidence rationale: HIGH — the source states the law, the equation, and the rearrangement explicitly.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
