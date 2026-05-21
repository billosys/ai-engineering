---
# === CORE IDENTIFICATION ===
concept: Fault Tolerance
slug: fault-tolerance

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: availability-properties
tier: foundational

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Systems That Never Stop"
chapter_number: 13
pdf_page: 402
section: "Availability — Fault Tolerance"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - fault tolerant
  - fault-tolerant system

# === TYPED RELATIONSHIPS ===
prerequisites:
  - availability
extends: []
related:
  - resilience
  - reliability
  - network-partition
contrasts_with:
  - resilience
  - reliability

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is fault tolerance?"
  - "How does a fault-tolerant system behave under failure?"
---

# Quick Definition

Fault tolerance is the ability of a system to act predictably under failure — fulfilling requests via alternative nodes or returning valid errors to callers.

# Core Definition

"Fault tolerance refers to the ability of a system to act predictably under failure. Such failure could be due to a software fault, where a process crashes because of a bug or corrupt state. Or it could be due to a network or hardware fault, or the result of a node crashing. Acting predictably can mean looking for alternative nodes and ensuring that requests are fulfilled, or just returning errors back to the callers" (Cesarini & Vinoski, p. 403).

# Prerequisites

- **Availability** — Fault tolerance is one of the concepts availability encompasses; understand availability first.

# Key Properties

1. The ability to act predictably under failure.
2. Failure may be a software fault, network/hardware fault, or node crash.
3. Predictable behavior can mean fulfilling requests via alternative nodes, or returning errors.
4. A valid (even unsuccessful) response to a client counts as fault-tolerant behavior.
5. Erlang provides dedicated, asynchronous error channels (monitors, links, exit signals) that work across nodes.
6. The hard part is that a slow node and a dead node are indistinguishable.

# Construction / Recognition

## To Construct/Create:
1. Use Erlang's monitors, links, and exit signals to detect failure locally and across nodes.
2. On detecting an error, either retry on an alternative node or return a valid error to the caller.
3. Propagate errors through the call chain, taking corrective actions at each level.
4. Handle false positives — an action may succeed asynchronously after a timeout was reported.

## To Identify/Recognize:
1. A system is fault-tolerant if, under any failure, it gives the client a valid (if not desired) response.

# Context & Application

- **Typical contexts**: Any distributed system that must behave predictably during failure.
- **Common applications**: Returning errors to clients, retrying on alternative nodes, escalating failures.
- **Historical/stylistic notes**: Erlang's same error-handling techniques work within a node and across distributed nodes; the only difference is latency for remote exit signals (p. 404).

# Examples

**Example 1** (pp. 403-404, Figure 14-1): A client request is forwarded to a logic node which crashes; the front-end node detects the crash (or an internal timeout fires) and sends an error back to the client — predictable, fault-tolerant behavior.

**Example 2** (p. 404): A purchase request that times out and is blindly retried by the client could result in buying 50 copies of the same book — illustrating why fault tolerance needs unique identifiers, idempotence, and bounded retries.

# Relationships

## Builds Upon
- **Availability** — Fault tolerance is a component of availability

## Enables
- Fault tolerance enables predictable client behavior under failure.

## Related
- **Resilience** — A sibling component of availability
- **Reliability** — A sibling component of availability
- **Network partition** — A failure mode fault tolerance must handle

## Contrasts With
- **Resilience** — Fault tolerance is about acting predictably during failure; resilience is about recovering quickly from it
- **Reliability** — Fault tolerance is predictability under failure; reliability is continued correct function under predefined conditions

# Common Errors

- **Error**: Letting a client retry a timed-out request indefinitely
  **Correction**: Use unique identifiers, idempotence, and bounded retry attempts; an action may succeed asynchronously after a timeout.

# Common Confusions

- **Confusion**: A fault-tolerant system always succeeds.
  **Clarification**: A fault-tolerant system always responds predictably — the response may be a valid error, not the desired result.

# Source Reference

Chapter 13: Systems That Never Stop, "Availability — Fault Tolerance," pages 403-404. See Figure 14-1.

# Verification Notes

- Definition source: Direct quote from p. 403.
- Confidence rationale: HIGH — the source explicitly defines fault tolerance.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
