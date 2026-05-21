---
# === CORE IDENTIFICATION ===
concept: Synchronous Calls for Flow Control
slug: synchronous-load-regulation

# === CLASSIFICATION ===
category: performance
subcategory: capacity
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Scaling Out"
chapter_number: 14
pdf_page: 424
section: "Capacity Planning — Synchronous versus asynchronous calls"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "synchronous versus asynchronous calls"
  - synchronous flow control

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bottleneck
extends: []
related:
  - backpressure
  - load-regulation
  - balancing-erlang-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do synchronous calls regulate load?"
  - "How do I prevent a consumer's mailbox from being flooded?"
---

# Quick Definition

Using synchronous calls — even when no reply is needed — blocks a producer until the consumer has handled the previous request, preventing the consumer's mailbox from being flooded.

# Core Definition

"A trick to regulate the load and control the flow, so as to get rid of these bottlenecks, is to use synchronous calls even if you do not require a response back from the server. When you use a synchronous call, a producer initiating a request will not send a new log request until the previous one has been received and acknowledged. Synchronous calls block the producer until the consumer has handled previous requests, preventing its mailbox from being flooded" (Cesarini & Vinoski, p. 437).

# Prerequisites

- **Bottleneck** — This technique removes message-queue bottlenecks; understand bottlenecks first.

# Key Properties

1. Synchronous calls are used even when no response is required.
2. A producer does not send a new request until the previous one is received and acknowledged.
3. The producer is blocked until the consumer has handled previous requests.
4. Prevents the consumer's mailbox from being flooded with messages.
5. Trades throughput for a stable and predictable system.
6. Timeout values must be tuned — never take the default 5-second value for granted, and never set it to infinity.

# Construction / Recognition

## To Construct/Create:
1. Replace `gen_server:cast` (asynchronous) with a synchronous call for high-rate producers.
2. Have each producer wait for acknowledgment before sending the next request.
3. Fine-tune the call timeout — not the default 5 seconds, never infinity.

## To Identify/Recognize:
1. Recognize the technique when producers block on acknowledgments rather than firing messages asynchronously.

# Context & Application

- **Typical contexts**: Removing message-queue bottlenecks under sustained heavy load.
- **Common applications**: Throttling log producers; any producer/consumer where the consumer cannot keep up.
- **Historical/stylistic notes**: Has the same effect as removing bottlenecks (Figure 15-6) — a stable, predictable system at the expense of throughput. The penalty the VM adds to senders of large mailboxes is not sufficient on its own to prevent overgrown queues.

# Examples

**Example 1** (pp. 436-437): A log server fed asynchronous `gen_server:cast` requests faster than it can handle builds a huge mailbox; switching to synchronous calls makes each producer wait for acknowledgment, controlling the flow.

**Example 2** (p. 437): Another bottleneck-reduction strategy is moving work from consumer to client — for log entries, batch them and let the requesting process format them, since formatting can be concurrent while disk writes must be sequential.

# Relationships

## Builds Upon
- **Bottleneck** — This technique removes message-queue bottlenecks

## Enables
- Synchronous flow control enables a stable, predictable system free of overgrown mailboxes.

## Related
- **Backpressure** — Synchronous calls are a form of backpressure on the producer
- **Load regulation** — Both control the rate of requests
- **Balancing an Erlang system** — Synchronous flow control helps balance a system

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Setting the synchronous call timeout to infinity or leaving it at the default 5 seconds
  **Correction**: Fine-tune timeout values; never take the default for granted and never set it to infinity.

# Common Confusions

- **Confusion**: The VM's reduction penalty on senders is enough to control mailbox growth.
  **Clarification**: Penalizing senders with added reductions is "not adequate to prevent overgrown message queues for overloaded processes" (p. 437); synchronous calls are the explicit fix.

# Source Reference

Chapter 14: Scaling Out, "Capacity Planning — Synchronous versus asynchronous calls," pages 436-437.

# Verification Notes

- Definition source: Direct quote from p. 437.
- Confidence rationale: HIGH — the source explicitly describes the technique in a named subsection.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
