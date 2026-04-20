---
# === CORE IDENTIFICATION ===
concept: Infectiousness of Asynchronous Code
slug: async-code-infectiousness

# === CLASSIFICATION ===
category: async-programming
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Foundations of asynchronous programming in JavaScript"
chapter_number: 42
pdf_page: null
section: "42.4 Asynchronous code: the downsides"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - async infectiousness
  - colored functions problem

# === TYPED RELATIONSHIPS ===
prerequisites:
  - asynchronous-programming-overview
extends: []
related:
  - async-function
  - promise
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes synchronous from asynchronous code execution?"
---

# Quick Definition

Asynchronous code is "infectious" because callers of asynchronous functions must themselves become asynchronous, since they cannot wait synchronously for an asynchronous result.

# Core Definition

"Exploring JavaScript" Ch. 42 identifies two downsides of async code: "Asynchronous code is more verbose than synchronous code" and "If we call asynchronous code, our code must become asynchronous too. That's because we can't wait synchronously for an asynchronous result. Asynchronous code has an infectious quality." Promises reduce verbosity, and async functions mostly eliminate it, but the infectious nature persists.

# Prerequisites

- **Asynchronous programming overview** -- understanding async patterns

# Key Properties

1. Calling an async function forces the caller to handle async results
2. This propagates up the call chain
3. Promises reduce the verbosity cost
4. Async functions make switching between sync and async easier but don't eliminate infectiousness

# Construction / Recognition

Any function that calls an async function must return a Promise or use callbacks:
```js
// This function must be async because it calls an async function
async function processData() {
  const data = await fetchData(); // async call forces this function to be async
  return transform(data);
}
```

# Context & Application

This property shapes API design and architecture decisions. Libraries that provide both sync and async versions of functions do so because of this infectious quality.

# Examples

From the source: "If we call asynchronous code, our code must become asynchronous too."

(Ch. 42, Section 42.4, lines 448-451)

# Relationships

## Builds Upon
- **Asynchronous programming overview** -- infectiousness is a fundamental property of async patterns

## Related
- **Async function** -- async functions mitigate but don't eliminate infectiousness
- **Promise** -- Promises are the mechanism through which infectiousness propagates

# Common Errors

- **Error**: Trying to use `await` in a non-async function to "block" on an async result
  **Correction**: Either make the calling function async or use `.then()` to handle the result

# Common Confusions

- **Confusion**: Async functions can return synchronous results to synchronous callers
  **Clarification**: Async functions always return Promises; the caller must handle a Promise

# Source Reference

Chapter 42: Foundations of asynchronous programming in JavaScript, Section 42.4, lines 442-461.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicitly described as a downside
- Cross-reference status: verified
