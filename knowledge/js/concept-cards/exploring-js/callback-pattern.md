---
# === CORE IDENTIFICATION ===
concept: Callback Pattern
slug: callback-pattern

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
section: "42.3.2 Delivering asynchronous results via callbacks"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Node.js-style callbacks
  - error-first callbacks

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-loop
  - task-queue
extends: []
related:
  - event-pattern
  - asynchronous-programming-overview
contrasts_with:
  - promise
  - async-function

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do callbacks, Promises, and async/await relate as async patterns?"
  - "What concepts are prerequisite to understanding Promises?"
---

# Quick Definition

The callback pattern delivers a one-off asynchronous result by passing a function (callback) to the async operation, which invokes it with an error or a result when the operation completes.

# Core Definition

"Exploring JavaScript" Ch. 42 describes callbacks as "another pattern for handling asynchronous results. They are only used for one-off results and have the advantage of being less verbose than events." In the Node.js convention, "there is a single callback that handles both success and failure. If the first parameter is not null then an error happened. Otherwise, the result can be found in the second parameter."

# Prerequisites

- **Event loop** -- callback execution depends on the event loop
- **Task queue** -- callbacks are enqueued as tasks

# Key Properties

1. Used for one-off (single) asynchronous results
2. Node.js convention: `(error, result)` -- error-first callback
3. Less verbose than events for single results
4. Callback is invoked when the async operation completes
5. Pre-dates Promises as the standard async pattern

# Construction / Recognition

```js
readFile('some-file.txt', {encoding: 'utf-8'},
  (error, data) => {
    if (error) {
      assert.fail(error);
      return;
    }
    assert.equal(data, 'The content of some-file.txt');
  });
```

(Ch. 42, Section 42.3.2, lines 409-416)

# Context & Application

Callback-based APIs are common in Node.js core (the older `fs` module) and older browser APIs. Modern code generally prefers Promises and async/await, but understanding callbacks is essential for working with legacy code and understanding the evolution of async patterns.

# Examples

From Ch. 41, callback-based divide function:
```js
divideCallback(12, 3,
  (err, result) => {
    if (err) {
      assert.fail(err);
    } else {
      assert.equal(result, 4);
    }
  });
```

(Ch. 41, Section 41.4, lines 127-135)

# Relationships

## Builds Upon
- **Event loop** -- callbacks are delivered via the event loop
- **Task queue** -- callback invocations are enqueued as tasks

## Enables
- **Promise** -- Promises standardize and improve upon callback patterns

## Related
- **Event pattern** -- both are async result delivery mechanisms

## Contrasts With
- **Promise** -- Promises support chaining, unified error handling, and caching
- **Async function** -- async/await provides synchronous-looking syntax vs. nested callbacks

# Common Errors

- **Error**: Forgetting to check the error parameter in a Node.js callback
  **Correction**: Always check `if (error)` before using the result

- **Error**: Callback hell -- deeply nested callbacks
  **Correction**: Use Promises or async/await to flatten the structure

# Common Confusions

- **Confusion**: Callbacks are always asynchronous
  **Clarification**: A callback can be called synchronously or asynchronously depending on the API; Node.js async callbacks are called asynchronously

# Source Reference

Chapter 42: Foundations of asynchronous programming in JavaScript, Section 42.3.2, lines 395-440.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit definition with Node.js convention
- Cross-reference status: verified against Ch. 41
