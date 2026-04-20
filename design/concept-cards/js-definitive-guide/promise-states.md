---
concept: Promise States (Pending, Fulfilled, Rejected, Resolved)
slug: promise-states
category: async-programming
subcategory: promises
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Asynchronous JavaScript"
chapter_number: 13
pdf_page: 367
section: "13.2.1 Using Promises"
extraction_confidence: high
aliases:
  - "Promise lifecycle"
  - "settled"
  - "resolved"
prerequisites:
  - promise-object
extends: []
related:
  - promise-chaining
contrasts_with: []
answers_questions:
  - "What is a Promise?"
---

# Quick Definition

The four states a Promise can be in: **pending** (not yet settled), **fulfilled** (completed with a value), **rejected** (failed with a reason), and **resolved** (locked onto another Promise's outcome) — once settled (fulfilled or rejected), a Promise never changes state.

# Core Definition

"We say that the promise has been *fulfilled* if and when the first callback is called. And we say that the Promise has been *rejected* if and when the second callback is called. If a Promise is neither fulfilled nor rejected, then it is *pending*. And once a promise is fulfilled or rejected, we say that it is *settled*" (p. 367). A Promise is *resolved* when it is "associated with, or 'locked onto,' another Promise" — it may be settled, or its fate may depend on the other Promise.

# Prerequisites

- **promise-object** — States are a fundamental property of Promises

# Key Properties

1. **Pending** — initial state, not yet settled
2. **Fulfilled** — completed successfully, has a value
3. **Rejected** — failed, has a reason (usually an Error)
4. **Settled** — either fulfilled or rejected (never changes after)
5. **Resolved** — fate determined (either settled, or locked onto another Promise)
6. A Promise can be resolved but not yet fulfilled (waiting for another Promise)

# Construction / Recognition

States are not directly observable as properties, but are manifested through `.then()` and `.catch()` callbacks.

# Context & Application

Understanding the distinction between resolved and fulfilled is "one of the keys to a deep understanding of Promises" (p. 368). It explains how Promise chains work when callbacks return Promises.

# Examples

From the source text (p. 367-372): When callback c1 returns Promise p4, Promise p2 becomes *resolved* (locked onto p4) but not yet *fulfilled*. Only when p4 fulfills does p2 also fulfill, triggering the next `.then()` in the chain.

# Relationships

## Builds Upon
- **Promise Object** — States describe the Promise lifecycle

## Enables
- **Promise Chaining** — Understanding resolved state is key to understanding chains

# Common Errors

- **Error**: Treating "resolved" and "fulfilled" as synonyms.
  **Correction**: A resolved Promise may not be fulfilled yet — it may be locked onto another pending Promise.

# Common Confusions

- **Confusion**: Thinking a Promise can change from fulfilled to rejected or vice versa.
  **Clarification**: Once settled, a Promise's state and value/reason are immutable.

# Source Reference

Chapter 13: Asynchronous JavaScript, Section 13.2.1, pages 367-368.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High — carefully defined with explicit terminology
- Uncertainties: None
- Cross-reference status: Verified
