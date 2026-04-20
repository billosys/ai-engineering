---
# === CORE IDENTIFICATION ===
concept: Asynchronous Tests
slug: async-tests

# === CLASSIFICATION ===
category: tooling
subcategory: testing
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Getting started with exercises"
chapter_number: 12
pdf_page: null
section: "12.2.2 Asynchronous tests in Mocha"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - async test
  - Promise-based tests

# === TYPED RELATIONSHIPS ===
prerequisites:
  - unit-testing
extends:
  - unit-testing
related:
  - assertions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are unit tests structured in JavaScript?"
---

# Quick Definition

Asynchronous tests in Mocha use callbacks, Promises, or async functions to signal completion, allowing testing of code that produces results later.

# Core Definition

"Writing tests for asynchronous code requires extra work: The test receives its results later and has to signal to Mocha that it isn't finished yet when it returns." (Ch. 12, &sect;12.2.2). Three approaches: callback-based (test receives `done` parameter), Promise-based (test returns a Promise), and async functions (preferred, using `async/await`).

# Prerequisites

- **unit-testing** -- async tests extend the basic test pattern

# Key Properties

1. Callback-based: test callback receives `done` parameter, call `done()` when finished
2. Promise-based: return a Promise from the test
3. Async function: preferred approach, uses `async/await`
4. Test fails if Promise is rejected or settlement exceeds timeout

# Construction / Recognition

```js
// Async function approach (preferred)
test('dividePromise', async () => {
  const result = await dividePromise(8, 4);
  assert.strictEqual(result, 2);
});
```

# Context & Application

Async tests are needed for testing any code involving Promises, fetch, file I/O, timers, or other asynchronous operations.

# Examples

From the source text (Ch. 12, &sect;12.2.2):

Promise-based:
```js
test('dividePromise 1', () => {
  return dividePromise(8, 4)
  .then(result => {
    assert.strictEqual(result, 2);
  });
});
```

Async function:
```js
test('dividePromise 2', async () => {
  const result = await dividePromise(8, 4);
  assert.strictEqual(result, 2);
});
```

# Relationships

## Builds Upon
- **unit-testing** -- extends basic testing with async support

## Enables
- Testing asynchronous code

## Related
- **assertions** -- used within async tests

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Forgetting to return the Promise or use `async`.
  **Correction**: Without returning a Promise or using async, Mocha thinks the test is synchronous and may pass before assertions run.

# Common Confusions

- **Confusion**: Thinking you need a special test runner for async tests.
  **Clarification**: Mocha handles async tests natively via Promises and async functions.

# Source Reference

Chapter 12: Getting started with exercises, Section 12.2.2, lines 155-257.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: All three approaches documented with examples
- Cross-reference status: verified
