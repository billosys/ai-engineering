---
# === CORE IDENTIFICATION ===
concept: Idempotence
slug: idempotence

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
section: "Reliability — At most once, exactly once, and at least once"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - idempotent
  - idempotent operation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - message-delivery-semantics
extends: []
related:
  - fault-tolerance
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is idempotence?"
  - "How do I achieve exactly-once semantics with at-most-once calls?"
---

# Quick Definition

Idempotence is the property of an operation that can be applied multiple times with the same effect as applying it once, so retried requests cause no additional observable effect.

# Core Definition

"The term describes an operation that the user can apply multiple times with the same effect as applying it once. For example, if a request changes a customer's shipping address, whether the system performs the request successfully once or multiple times has the same result, assuming the shipping address is the same in each request. Such a request can actually be executed multiple times because the side effects of any second or subsequent executions essentially have no observable effect" (Cesarini & Vinoski, p. 409).

# Prerequisites

- **Message delivery semantics** — Idempotence is the property that makes exactly-once-with-at-most-once-calls possible; understand the semantics first.

# Key Properties

1. An idempotent operation applied multiple times has the same effect as applying it once.
2. Second and subsequent executions have no observable effect.
3. It underpins the pattern of achieving exactly-once semantics using unique sequence numbers in client requests.
4. It is a property of the operation itself, not of the messaging infrastructure.

# Construction / Recognition

## To Construct/Create:
1. Design the operation so repeating it produces the same final state.
2. Combine with unique sequence numbers so duplicate requests are recognized and the original reply returned.

## To Identify/Recognize:
1. Recognize idempotence by asking: does executing this operation twice differ in observable effect from executing it once? If not, it is idempotent.

# Context & Application

- **Typical contexts**: Retry-safe request handling in distributed systems.
- **Common applications**: Achieving exactly-once semantics with at-most-once calls; safely retrying after transient errors.
- **Historical/stylistic notes**: With a request-identification scheme, the second and subsequent executions never actually occur — the duplicate is recognized and the original reply returned (p. 409).

# Examples

**Example 1** (p. 409): Changing a customer's shipping address — whether performed once or many times, the result is the same shipping address.

**Example 2** (p. 409, Figure 14-4): A client resends a request with the same identifier after a timeout; the logic node identifies it as a duplicate and returns the original reply, possibly tagged as a duplicate — this works in the presence of transient errors because the operation is idempotent.

# Relationships

## Builds Upon
- **Message delivery semantics** — Idempotence enables exactly-once-with-at-most-once-calls

## Enables
- Idempotence enables safe retries and the unique-sequence-number pattern for exactly-once semantics.

## Related
- **Fault tolerance** — Idempotence is a key technique for handling failure uncertainty

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Retrying a non-idempotent operation after a timeout
  **Correction**: Only retry freely if the operation is idempotent, or use unique sequence numbers so duplicates are recognized.

# Common Confusions

- **Confusion**: Idempotence means an operation has no effect.
  **Clarification**: It has an effect — the first time; subsequent identical executions simply produce no further observable change.

# Source Reference

Chapter 13: Systems That Never Stop, "Reliability — At most once, exactly once, and at least once," pages 409-410. See Figure 14-4.

# Verification Notes

- Definition source: Direct quote from p. 409.
- Confidence rationale: HIGH — the source explicitly defines idempotence with an example.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
