---
# === CORE IDENTIFICATION ===
concept: Synchronous Communication
slug: synchronous-communication

# === CLASSIFICATION ===
category: distribution
subcategory: communication-strategy
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Adding distribution to the cache with Mnesia"
chapter_number: 9
pdf_page: null
section: "9.1.1 Choosing a communication strategy"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "blocking communication"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - message-passing
extends: []
related:
  - asynchronous-communication
  - distributed-cache
  - gen-server-call
contrasts_with:
  - asynchronous-communication

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is synchronous communication?"
  - "Why does synchronous communication need timeouts?"
  - "What are the trade-offs of synchronous communication?"
---

# Quick Definition

Synchronous (blocking) communication means the sender is suspended until it receives a reply or acknowledgment; it provides strong synchronization at the cost of latency.

# Core Definition

Synchronous communication is a strategy in which every message requires a reply, or at least an acknowledgment that the message was received. The sender becomes suspended — *blocked* — until the reply arrives and can do nothing else meanwhile. Its drawback is that the sender cannot do further work until it gets a response, which in a distributed environment takes at least twice the network traversal time; its benefit is that systems can be easily synchronized around an activity, ending in a known state. For synchronous communication to be practical it needs to support timeouts, so the sender does not wait indefinitely — at some point it must give up and either consider the operation a failure or assume it worked. Erlang implements synchronous communication as a pair of asynchronous request/reply messages, as `gen_server:call/3` does (Ch. 9, Section 9.1.1).

# Prerequisites

- **message-passing** — Synchronous communication is built from a request/reply pair of messages.

# Key Properties

1. Every message requires a reply or acknowledgment.
2. The sender is suspended (blocked) until the reply arrives.
3. Costs at least a full network round-trip of latency.
4. Leaves the system in a known, synchronized state on return.
5. Requires timeouts to be practical.
6. Built atop asynchronous request/reply messages (e.g., `gen_server:call/3`).

# Construction / Recognition

## To Use Synchronous Communication:
1. Send a request and block waiting for the reply.
2. Apply a maximum waiting time (timeout).
3. On timeout, treat the operation as failed or assume it succeeded.

## To Recognize:
1. A `gen_server:call` or any send-then-block-for-reply pattern is synchronous.

# Context & Application

- **Typical contexts**: Operations needing a guaranteed consistent state on return.
- **Common applications**: A cache insert that must confirm all instances are updated before reporting success.
- **Historical/stylistic notes**: The book illustrates it with a businessman waiting at a government office for a receipt before he can leave.

# Examples

**Example 1** (Section 9.1.1, Figure 9.4): A synchronous call with a 10-second timeout completes in 8 seconds — 2 to get there, 4 to handle the request, 2 to return.

**Example 2** (Section 9.1.2): A synchronous cache insert blocks until all cache instances confirm the data is inserted, only then telling the user they are logged in.

# Relationships

## Builds Upon
- **message-passing** — Synchronous communication is a request/reply message pair.

## Enables
- None.

## Related
- **distributed-cache** — Synchronous vs. asynchronous is a key cache design choice.
- **gen-server-call** — `gen_server:call/3` is the canonical synchronous primitive.

## Contrasts With
- **asynchronous-communication** — Asynchronous communication does not block; synchronous suspends the sender until a reply arrives.

# Common Errors

- **Error**: Using synchronous communication without a timeout.
  **Correction**: Always bound the wait; without a timeout the sender may block indefinitely.

- **Error**: Calling N remote nodes one at a time synchronously.
  **Correction**: This costs at least N round-trips; gather replies concurrently if latency matters.

# Common Confusions

- **Confusion**: Believing Erlang has a built-in synchronous primitive separate from message passing.
  **Clarification**: Synchronous communication is implemented as a request/reply pair of asynchronous messages.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.1.1 "Choosing a communication strategy," subsection "Synchronous communication," Figures 9.3–9.4.

# Verification Notes

- Definition source: Directly adapted from Section 9.1.1.
- Confidence rationale: HIGH — the book explicitly defines and illustrates the concept.
- Uncertainties: None.
- Cross-reference status: Verified; `gen-server-call` exists as a card in this directory.
