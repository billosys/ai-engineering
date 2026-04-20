---
concept: Promise Combinator Short-Circuiting
slug: promise-short-circuiting
category: async-programming
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.5.6 Short-circuiting"
extraction_confidence: high
aliases:
  - early settlement
prerequisites:
  - promise-combinator-functions
extends: []
related:
  - promise-all
  - promise-race
  - promise-any
  - promise-all-settled
contrasts_with: []
answers_questions:
  - "What distinguishes Promise.all() from Promise.race() from Promise.any()?"
---

# Quick Definition

Short-circuiting means a Promise combinator's output Promise settles before all input Promises are settled. `Promise.all()` short-circuits on first rejection, `Promise.race()` on first settlement, `Promise.any()` on first fulfillment. `Promise.allSettled()` never short-circuits.

# Core Definition

"Exploring JavaScript" Ch. 43: "For a Promise combinator, short-circuiting means that the output Promise is settled early -- before all input Promises are settled." The combinators that short-circuit: `Promise.all()` (rejected on first rejection), `Promise.race()` (settled on first settlement), `Promise.any()` (fulfilled on first fulfillment). "Once again, settling early does not mean that the operations behind the ignored Promises are stopped."

# Prerequisites

- **Promise combinator functions** -- short-circuiting is a combinator behavior

# Key Properties

1. `Promise.all()`: short-circuits on first rejection
2. `Promise.race()`: short-circuits on first settlement
3. `Promise.any()`: short-circuits on first fulfillment
4. `Promise.allSettled()`: does NOT short-circuit
5. Short-circuiting ignores remaining settlements; does NOT cancel operations

# Construction / Recognition

Identified by the combinator used and the combination of fulfilled/rejected inputs.

# Context & Application

Understanding short-circuiting is essential for predicting combinator behavior and knowing when operations complete early.

# Examples

From the source summary of short-circuiting behavior for all four combinators.

(Ch. 43, Section 43.5.6, lines 2024-2039)

# Relationships

## Builds Upon
- **Promise combinator functions** -- short-circuiting is their key behavioral difference

## Related
- All four combinator cards

# Common Errors

- **Error**: Expecting short-circuiting to cancel running operations
  **Correction**: Only the output Promise settles early; the underlying operations continue

# Common Confusions

- **Confusion**: `Promise.allSettled()` short-circuits like `Promise.all()`
  **Clarification**: `allSettled()` never short-circuits; it always waits for all inputs

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.5.6, lines 2024-2039.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit summary of all combinator short-circuiting behavior
- Cross-reference status: verified
