---
# === CORE IDENTIFICATION ===
concept: Generic Server Deadlocks
slug: gen-server-deadlocks

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: gen-server
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Generic Servers"
chapter_number: 3
pdf_page: 96
section: "Deadlocks"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - deadlock
  - circular synchronous call
  - deadlock avoidance

# === TYPED RELATIONSHIPS ===
prerequisites:
  - synchronous-message-passing
extends: []
related:
  - call-timeouts
  - asynchronous-message-passing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do deadlocks happen between gen_servers?"
  - "How are gen_server deadlocks resolved and avoided?"
---

# Quick Definition

A `gen_server` deadlock occurs when two servers each make a synchronous call to the other and both block waiting for a reply. OTP resolves it via call timeouts and avoids it by ordering synchronous calls.

# Core Definition

"Picture two generic servers in a badly designed system. server1 does a synchronous call to server2. server2 receives the request, and through a series of calls in other modules ends up (possibly unknowingly) executing a synchronous callback to server1" (Cesarini & Vinoski, p. 94). "This problem is resolved not through complex deadlock prevention algorithms, but through timeouts. If server1 has not received a response within 5,000 milliseconds, it terminates, causing server2 to terminate as well." For avoidance: "A standard practice when dealing with static processes ... is to allow synchronous calls to be made only to processes that were started before the process making the call. Calls from older processes to younger ones may only be asynchronous" (p. 95).

# Prerequisites

- **Synchronous message passing** — Deadlocks arise from mutually blocking synchronous `call`s.

# Key Properties

1. A deadlock arises when two (or more) servers synchronously call each other in a cycle.
2. Both block in their `receive`, each waiting for the other's reply.
3. OTP resolves deadlocks via the 5-second `call` timeout, which terminates the waiting server.
4. The termination propagates (via monitor signal or further timeout) to the other servers in the cycle.
5. A supervisor then restarts the servers; the deadlock is logged for diagnosis.
6. Deadlocks are rare in Erlang due to the lack of shared memory and critical sections.
7. Avoidance rule: synchronous calls only to older processes; older-to-younger calls must be asynchronous.

# Construction / Recognition

## To Avoid:
1. Allow synchronous calls only to processes started *before* the calling process.
2. Make older-to-younger calls asynchronous; have the younger process reply via an asynchronous callback.
3. Use supervision-tree start order to determine process age.

## To Recognize:
1. Two servers each issuing a synchronous `call` that, directly or transitively, reaches the other.

# Context & Application

- **Typical contexts**: Poorly designed systems with circular synchronous dependencies.
- **Common applications**: Designing process dependencies so calls flow in one direction.
- **Historical/stylistic notes**: One author reports encountering only a single deadlock in 17 years of Erlang — fixed in 5 minutes by making one call asynchronous.

# Examples

**Example 1** (p. 94, Figure 4-8): server1 synchronously calls server2, which transitively makes a synchronous callback to server1; neither can reply. The 5-second timeout terminates server1, then server2.

**Example 2** (p. 95): The author's real deadlock — a chain A→B→(RPC)→C→D→(RPC)→A; the fix was for A to call B asynchronously and B to respond with an asynchronous callback.

# Relationships

## Builds Upon
- **Synchronous message passing** — Deadlocks are a failure mode of synchronous calls.

## Enables
- *(none specific in scope)*

## Related
- **Call timeouts** — The mechanism that breaks deadlocks.
- **Asynchronous message passing** — The tool for restructuring calls to avoid deadlocks.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Letting an older process make a synchronous call to a younger one.
  **Correction**: Calls from older to younger processes must be asynchronous, with replies via asynchronous callbacks.

# Common Confusions

- **Confusion**: Thinking OTP prevents deadlocks with a prevention algorithm.
  **Clarification**: There is no prevention algorithm — deadlocks are *resolved* by call timeouts and *avoided* by call-ordering discipline.

# Source Reference

Chapter 3: Generic Servers, Section "Deadlocks" / "Strategies for Avoiding Deadlocks," pages 94-95. See Figure 4-8 (generic server deadlocks).

# Verification Notes

- Definition source: Direct quotes from pp. 94-95.
- Confidence rationale: HIGH — explicit treatment of cause, resolution, and avoidance.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
