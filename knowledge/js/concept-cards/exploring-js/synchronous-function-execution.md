---
# === CORE IDENTIFICATION ===
concept: Synchronous Function Execution
slug: synchronous-function-execution

# === CLASSIFICATION ===
category: async-programming
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "A roadmap for asynchronous programming"
chapter_number: 41
pdf_page: null
section: "41.2 Synchronous functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - synchronous call
  - sync execution

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - asynchronous-programming-overview
contrasts_with:
  - callback-pattern
  - promise
  - async-function

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes synchronous from asynchronous code execution?"
---

# Quick Definition

A synchronous function call blocks the caller until the callee finishes its computation and returns a result.

# Core Definition

In "Exploring JavaScript" Ch. 41, Rauschmayer defines synchronous functions as "normal" functions where "the caller waits until the callee is finished with its computation." The result is returned directly, and errors are thrown as exceptions.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. The caller is blocked while the callee executes
2. Results are returned directly via the `return` statement
3. Errors are communicated via thrown exceptions
4. Control flow is sequential and predictable

# Construction / Recognition

```js
function main() {
  try {
    const result = divideSync(12, 3);
    assert.equal(result, 4);
  } catch (err) {
    assert.fail(err);
  }
}
```

(Ch. 41, Section 41.2)

# Context & Application

Synchronous execution is the default in JavaScript. It is appropriate for CPU-bound computations that complete quickly. Long-running synchronous operations block the event loop and should be avoided.

# Examples

From the source:
```js
const result = divideSync(12, 3); // caller waits here
assert.equal(result, 4);
```

(Ch. 41, Section 41.2, line 85)

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **Asynchronous programming overview** -- understanding sync execution is prerequisite to understanding why async is needed

## Contrasts With
- **Callback pattern** -- callbacks deliver results asynchronously rather than blocking
- **Promise** -- Promises deliver results asynchronously via `.then()`
- **Async function** -- async functions look synchronous but execute asynchronously

# Common Errors

- **Error**: Using synchronous blocking operations (like busy-wait loops) for long-running tasks
  **Correction**: Use asynchronous patterns for operations that take significant time

# Common Confusions

- **Confusion**: All JavaScript code is synchronous or all is asynchronous
  **Clarification**: JavaScript code within a task runs synchronously; tasks themselves are scheduled asynchronously via the event loop

# Source Reference

Chapter 41: A roadmap for asynchronous programming, Section 41.2, lines 75-91.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit definition provided
- Cross-reference status: verified
