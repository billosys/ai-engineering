---
# === CORE IDENTIFICATION ===
concept: Load Regulation
slug: load-regulation

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
  - load regulation
  - throttling

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bottleneck
extends: []
related:
  - backpressure
  - littles-law
  - cascading-failure
contrasts_with:
  - backpressure

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is load regulation?"
  - "What distinguishes load regulation from backpressure?"
---

# Quick Definition

Load regulation diverts incoming requests into a queue so none are lost, then feeds them from the queue as fast as the system can handle, by imposing connection limits and throttling.

# Core Definition

"The mobile operators were applying a technique called load regulation, where the flow of requests was diverted to a queue to ensure that no requests were lost. Messages were retrieved from the queue and sent to the SMS center (SMSC) as fast as it could handle them" (Cesarini & Vinoski, p. 438). "Load regulation allows you to keep and remember requests by imposing limits on the number of simultaneous connections and throttling requests using queues" (p. 439).

# Prerequisites

- **Bottleneck** — Load regulation manages load that would otherwise create bottlenecks; understand bottlenecks first.

# Key Properties

1. Diverts the flow of requests into a queue so none are lost.
2. Feeds requests from the queue as fast as the system can handle.
3. Imposes limits on the number of simultaneous connections.
4. Throttles requests using queues.
5. Keeps and remembers requests, unlike backpressure which rejects them.
6. If requests keep arriving faster than they can be handled, the queue eventually overflows and rejection must begin.

# Construction / Recognition

## To Construct/Create:
1. Place a queue in the request path (a load-regulation framework, e.g., Jobs or Safetyvalve).
2. Limit the number of simultaneous connections.
3. Feed requests from the queue at the rate downstream can handle (the service-level agreement).
4. When the queue overflows, begin rejecting requests.

## To Identify/Recognize:
1. Recognize load regulation when excess requests are queued and remembered rather than rejected.

# Context & Application

- **Typical contexts**: Systems facing peaks, e.g., a game back end scaling to millions of users.
- **Common applications**: Smoothing peaks toward third-party APIs and service nodes; throttling toward an SMSC.
- **Historical/stylistic notes**: Originated in telecom — mobile operators used it for the New Year's Eve SMS surge. Two widely used Erlang load-regulation applications are Jobs and Safetyvalve.

# Examples

**Example 1** (pp. 439-440, Figure 15-7): If an SMS gateway receives more texts than the SMSC can handle, it queues them in the load-regulation application and feeds them on a FIFO basis at the SMSC's rate; if the queue overflows, the gateway starts rejecting SMSs.

**Example 2** (p. 441): Jobs, written by Ulf Wiger, is a scheduler for load regulation providing configurable queues; Safetyvalve, inspired by Jobs, focuses on queuing with a token bucket algorithm for bursts.

# Relationships

## Builds Upon
- **Bottleneck** — Load regulation manages load that would create bottlenecks

## Enables
- Load regulation enables predictable latency/throughput under peak loads without losing requests.

## Related
- **Backpressure** — The complementary load-control technique
- **Littles law** — Load regulation controls queue length, an input to Little's Law
- **Cascading failure** — Load regulation guards against overload-driven cascades

## Contrasts With
- **Backpressure** — Load regulation queues and remembers requests; backpressure rejects them

# Common Errors

- **Error**: Applying load regulation everywhere by default
  **Correction**: Load regulation comes at a cost — queues and a dispatcher add overhead and can become a bottleneck; start controlling load only if you have to.

# Common Confusions

- **Confusion**: Load regulation never loses requests.
  **Clarification**: It queues requests, but if they keep arriving faster than they can be handled, the queue overflows and you must start rejecting.

# Source Reference

Chapter 14: Scaling Out, "Load Regulation and Backpressure," pages 438-441. See Figure 15-7.

# Verification Notes

- Definition source: Direct quotes from pp. 438-439.
- Confidence rationale: HIGH — the source dedicates a named section with an explicit definition.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
