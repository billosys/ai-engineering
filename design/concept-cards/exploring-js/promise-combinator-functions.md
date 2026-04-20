---
concept: Promise Combinator Functions
slug: promise-combinator-functions
category: async-programming
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.5.1 What is a Promise combinator function?"
extraction_confidence: high
aliases:
  - Promise combinators
prerequisites:
  - promise
extends: []
related:
  - promise-all
  - promise-race
  - promise-any
  - promise-all-settled
  - promise-resolve-reject
contrasts_with: []
answers_questions:
  - "What distinguishes Promise.all() from Promise.race() from Promise.any()?"
---

# Quick Definition

Promise combinator functions take an iterable of Promises as input and return a single output Promise, combining multiple async operations into one. JavaScript provides four: `Promise.all()`, `Promise.race()`, `Promise.any()`, and `Promise.allSettled()`.

# Core Definition

"Exploring JavaScript" Ch. 43 defines combinators using the combinator pattern from functional programming: "Primitive functions (short: primitives) create atomic pieces. Combinator functions (short: combinators) combine atomic and/or compound pieces to create compound pieces." For Promises, primitives are `Promise.resolve()` and `Promise.reject()`; combinators are `Promise.all()`, `Promise.race()`, `Promise.any()`, and `Promise.allSettled()`. "In each of these cases: Input is an iterable over zero or more Promises. Output is a single Promise."

# Prerequisites

- **Promise** -- combinators operate on Promises

# Key Properties

1. Four combinators: `all()`, `race()`, `any()`, `allSettled()`
2. Each takes an iterable of Promises, returns a single Promise
3. Some short-circuit (settle before all inputs are settled)
4. Based on the combinator pattern from functional programming

# Construction / Recognition

All combinators follow the pattern `Promise.xxx(iterableOfPromises)`.

# Context & Application

Used to coordinate multiple concurrent async operations: waiting for all, racing for first, finding first success, or collecting all results regardless of outcome.

# Examples

See individual combinator cards for specific examples.

(Ch. 43, Section 43.5.1, lines 1276-1301)

# Relationships

## Builds Upon
- **Promise** -- combinators operate on Promises

## Enables
- **Concurrent async operations** -- coordinating multiple Promises

## Related
- **Promise.all()**, **Promise.race()**, **Promise.any()**, **Promise.allSettled()** -- the four combinators

# Common Errors

- **Error**: Assuming short-circuiting stops the underlying async operations
  **Correction**: Short-circuiting only ignores settlements; the operations continue running

# Common Confusions

- **Confusion**: Combinators create parallelism
  **Clarification**: Combinators coordinate already-started async operations; the concurrency comes from starting the operations before combining

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.5.1, lines 1276-1301.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit definition with pattern reference
- Cross-reference status: verified
