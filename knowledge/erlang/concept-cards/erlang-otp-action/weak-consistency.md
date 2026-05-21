---
# === CORE IDENTIFICATION ===
concept: Weak Consistency
slug: weak-consistency

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
section: "9.1.2 Synchronous versus asynchronous cache"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "weak consistency"
  - "eventual consistency (informal)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - asynchronous-communication
extends: []
related:
  - distributed-cache
  - synchronous-communication
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is weak consistency?"
  - "What consistency does an asynchronous cache give?"
---

# Quick Definition

Weak consistency is the property of an asynchronously updated distributed system in which replicas are not all guaranteed to reflect a change immediately, so the system may briefly be observed in an inconsistent state.

# Core Definition

Weak consistency is the consistency level the book attributes to an asynchronous (fire-and-forget) distributed cache. When an operation broadcasts an insert or delete message to all cache instances and returns immediately, the caches are not all guaranteed to have received and processed the message yet, even though the client has already been told the operation is done. The system as a whole can therefore temporarily be in an inconsistent state, and there is a small probability that someone might observe this once in a while — for example, a user who logs in and a second later is told they are not logged in, because the request was served by a cache instance that has not yet processed the insert (Ch. 9, Section 9.1.2).

# Prerequisites

- **asynchronous-communication** — Weak consistency results from updating replicas asynchronously.

# Key Properties

1. Replicas are not guaranteed to reflect a change immediately.
2. The operation returns before all replicas have processed it.
3. The system can temporarily be in an inconsistent state.
4. There is a small probability the inconsistency is observed.
5. Arises naturally from asynchronous (fire-and-forget) updates.

# Construction / Recognition

## How It Arises:
1. An operation broadcasts an update asynchronously to all replicas.
2. The operation returns immediately, before replicas confirm.
3. Until each replica processes the message, it holds stale data.

## To Recognize:
1. A distributed update that returns without confirmation from all replicas yields weak consistency.

# Context & Application

- **Typical contexts**: Asynchronous distributed caches and replicated stores.
- **Common applications**: Session caches where occasional brief staleness is tolerable.
- **Historical/stylistic notes**: For the Simple Cache, Erlware rejected weak consistency for login — even one "not logged in" message after a successful login was deemed unacceptable.

# Examples

**Example 1** (Section 9.1.2): With an asynchronous cache, a user logs in, requests another page a second later, and finds no record of being logged in — an observable weak-consistency window.

# Relationships

## Builds Upon
- **asynchronous-communication** — Weak consistency is the consequence of asynchronous updates.

## Enables
- None.

## Related
- **distributed-cache** — Weak consistency is one option for the cache's behaviour.
- **synchronous-communication** — Synchronous updates avoid weak consistency at the cost of latency.

## Contrasts With
- None.

# Common Errors

- **Error**: Choosing a weakly consistent design for an operation that requires a guaranteed state on return.
  **Correction**: Use synchronous communication when the application cannot tolerate any observable inconsistency.

# Common Confusions

- **Confusion**: Thinking weak consistency means the data is often wrong.
  **Clarification**: It only means there is a brief, low-probability window where replicas differ; they converge once messages are processed.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.1.2 "Synchronous versus asynchronous cache," subsection "Asynchronous cache," Figure 9.5.

# Verification Notes

- Definition source: Synthesized from Section 9.1.2's discussion of the asynchronous cache.
- Confidence rationale: MEDIUM — the term "weak consistency" is used by the book but not given a formal standalone definition.
- Uncertainties: None.
- Cross-reference status: Verified.
