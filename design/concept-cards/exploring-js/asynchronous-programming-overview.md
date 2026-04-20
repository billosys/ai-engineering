---
# === CORE IDENTIFICATION ===
concept: Asynchronous Programming Overview
slug: asynchronous-programming-overview

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
section: "41.1 The next chapters"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - async programming roadmap

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - event-loop
  - callback-pattern
  - promise
  - async-function
contrasts_with:
  - synchronous-function-execution

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do callbacks, Promises, and async/await relate as async patterns?"
  - "What distinguishes synchronous from asynchronous code execution?"
---

# Quick Definition

Asynchronous programming in JavaScript is a set of patterns and mechanisms (callbacks, Promises, async/await) that allow code to initiate long-running operations and be notified of their results later, without blocking the single-threaded JavaScript process.

# Core Definition

As described in "Exploring JavaScript" Ch. 41, JavaScript provides a progression of asynchronous programming approaches: callbacks deliver results via functions passed as arguments; Promises standardize callback-based patterns into chainable objects; and async functions provide synchronous-looking syntax built on top of Promises. Each successive pattern reduces verbosity and complexity.

# Prerequisites

Foundational concept. Requires understanding of functions and basic JavaScript execution.

# Key Properties

1. JavaScript runs in a single process using an event loop
2. Asynchronous code allows the process to continue while waiting for results
3. Three main patterns exist in order of evolution: callbacks, Promises (ES6), async/await (ES2017)
4. Asynchronous code is "infectious" -- calling async code requires the caller to also be async

# Construction / Recognition

Asynchronous code is identified by:
- Callback functions passed to handle results later
- `.then()` and `.catch()` method chains on Promises
- `async`/`await` keywords

# Context & Application

Used whenever operations may take time: network requests, file I/O, timers, user interaction handling. Essential in both browser and Node.js environments.

# Examples

Synchronous call:
```js
const result = divideSync(12, 3);
assert.equal(result, 4);
```

Callback-based:
```js
divideCallback(12, 3, (err, result) => {
  if (err) { assert.fail(err); }
  else { assert.equal(result, 4); }
});
```

Promise-based:
```js
dividePromise(12, 3)
  .then(result => assert.equal(result, 4))
  .catch(err => assert.fail(err));
```

Async/await:
```js
async function main() {
  const result = await dividePromise(12, 3);
  assert.equal(result, 4);
}
```

(Ch. 41, Section 41.2-41.6)

# Relationships

## Builds Upon
- **Synchronous function execution** -- async programming extends the synchronous model to handle delayed results

## Enables
- **Promise** -- Promises formalize async result delivery
- **Async function** -- async/await provides cleaner syntax for Promise-based code

## Related
- **Event loop** -- the mechanism that enables asynchronous execution

## Contrasts With
- **Synchronous function execution** -- synchronous code blocks until complete; async code returns immediately

# Common Errors

- **Error**: Writing async code as if it were synchronous (expecting immediate results)
  **Correction**: Always handle async results through callbacks, `.then()`, or `await`

# Common Confusions

- **Confusion**: Async code runs in parallel threads
  **Clarification**: JavaScript uses a single thread with an event loop; async operations use cooperative multitasking, not true parallelism

# Source Reference

Chapter 41: A roadmap for asynchronous programming, Sections 41.1-41.6, lines 35-208.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit overview chapter with clear definitions
- Cross-reference status: verified against Ch. 42-45
