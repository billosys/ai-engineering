---
# === CORE IDENTIFICATION ===
concept: Asynchronous Communication
slug: asynchronous-communication

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
  - "fire and forget"
  - "nonblocking communication"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - message-passing
extends: []
related:
  - synchronous-communication
  - distributed-cache
  - weak-consistency
contrasts_with:
  - synchronous-communication

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is asynchronous communication?"
  - "When should I use asynchronous communication?"
  - "What are the trade-offs of asynchronous communication?"
---

# Quick Definition

Asynchronous communication ("fire and forget") means the sender proceeds immediately after posting a message, without waiting for any confirmation or reply.

# Core Definition

Asynchronous communication is a strategy in which the sender immediately proceeds without waiting for any kind of confirmation or answer; if a reply is expected, the sender checks for it later. The book calls it "fire and forget" or "send and pray." Erlang's basic form of message passing is asynchronous, because it is the most straightforward and flexible form and a good match for distributed programming. Asynchronous communication implies very little overhead — nothing to check, scan, verify, or time — so it is fast and lends itself to simple, intuitive systems; the book recommends striving to use it except when you obviously cannot. Its drawback is weaker guarantees: the system as a whole can temporarily be in an inconsistent state (Ch. 9, Section 9.1.1).

# Prerequisites

- **message-passing** — Asynchronous communication is the natural mode of Erlang message passing.

# Key Properties

1. The sender proceeds immediately after posting the message.
2. No confirmation or reply is awaited; replies, if any, are checked later.
3. Very low overhead — fast and simple.
4. Erlang's basic message passing is asynchronous.
5. Provides weaker consistency guarantees than synchronous communication.
6. The recommended default unless requirements force otherwise.

# Construction / Recognition

## To Use Asynchronous Communication:
1. Post the message and continue working immediately.
2. If a result is needed, retrieve any reply at a later point.

## To Recognize:
1. A send with no blocking wait for a reply (e.g., `gen_server:cast`) is asynchronous.

# Context & Application

- **Typical contexts**: Distributed systems where low latency matters and strict consistency is not required.
- **Common applications**: Broadcasting cache inserts to all nodes and returning immediately.
- **Historical/stylistic notes**: The book illustrates it with the postal service — drop a letter and go about your day.

# Examples

**Example 1** (Section 9.1.1): The postal-service analogy — you write a letter, post it, and are done the second it leaves your hand; the message may or may not arrive, but either way it does not impede your day.

**Example 2** (Section 9.1.2): An asynchronous cache insert sends messages to all cache instances and returns immediately, before the remote caches have processed them.

# Relationships

## Builds Upon
- **message-passing** — Asynchronous send is the basic message-passing mode.

## Enables
- **weak-consistency** — Asynchronous updates give weak consistency among replicas.

## Related
- **distributed-cache** — The cache's communication strategy is asynchronous vs. synchronous.

## Contrasts With
- **synchronous-communication** — Synchronous communication blocks the sender until a reply arrives; asynchronous does not.

# Common Errors

- **Error**: Using asynchronous communication where the application needs a guaranteed-consistent state on return.
  **Correction**: Use synchronous communication when an ironclad guarantee is required.

# Common Confusions

- **Confusion**: Thinking asynchronous means messages are slow or frequently lost.
  **Clarification**: It only means no guarantee is provided on return; messages are typically fast and reliable.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.1.1 "Choosing a communication strategy," subsection "Asynchronous communication," Figure 9.2.

# Verification Notes

- Definition source: Directly adapted from Section 9.1.1.
- Confidence rationale: HIGH — the book explicitly defines and illustrates the concept.
- Uncertainties: None.
- Cross-reference status: Verified.
