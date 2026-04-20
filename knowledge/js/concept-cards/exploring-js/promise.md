---
# === CORE IDENTIFICATION ===
concept: Promise
slug: promise

# === CLASSIFICATION ===
category: async-programming
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.1.1 Using a Promise-based function"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - JS Promise
  - Promise object

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-loop
  - callback-pattern
extends:
  - callback-pattern
related:
  - promise-states
  - promise-then
  - promise-catch
  - promise-chaining
contrasts_with:
  - callback-pattern
  - event-pattern

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Promise?"
  - "How do I create and consume a Promise?"
  - "How do callbacks, Promises, and async/await relate as async patterns?"
---

# Quick Definition

A Promise is a container object that is initially empty and eventually holds either a result value (fulfillment) or an error (rejection), providing a standardized pattern for asynchronous result delivery.

# Core Definition

"Exploring JavaScript" Ch. 43 defines Promises as "a technique for delivering results asynchronously. Instead of directly returning a result, a Promise-based function returns a Promise: a container object that is initially empty. If and when the function is eventually done, it puts either a result or an error into the Promise." Promises were introduced in ES6.

# Prerequisites

- **Event loop** -- Promises are settled asynchronously via the event loop
- **Callback pattern** -- Promises improve upon the callback approach

# Key Properties

1. Introduced in ES6
2. A Promise is a container that starts empty and eventually holds a value or error
3. `.then()` registers callbacks for fulfillment; `.catch()` registers callbacks for rejection
4. Once settled (fulfilled or rejected), a Promise's value is cached and immutable
5. Promises are both a standard pattern for callbacks and the foundation for async functions
6. Promise-based functions start synchronously but settle asynchronously

# Construction / Recognition

Consuming a Promise:
```js
addAsync(3, 4)
  .then((result) => {
    assert.equal(result, 7);
  })
  .catch((error) => {
    assert.fail(error);
  });
```

Creating a Promise:
```js
function addAsync(x, y) {
  return new Promise((resolve, reject) => {
    if (x === undefined || y === undefined) {
      reject(new Error('Must provide two parameters'));
    } else {
      resolve(x + y);
    }
  });
}
```

(Ch. 43, Section 43.1.1-43.1.3, lines 119-191)

# Context & Application

Promises are the standard for asynchronous programming in modern JavaScript. Browser APIs (Fetch, IndexedDB), Node.js APIs (`fs/promises`), and most libraries use Promises. They are the foundation upon which async/await is built.

# Examples

Reading a file with Promises:
```js
import {readFile} from 'node:fs/promises';
readFile('person.json')
  .then((text) => {
    const obj = JSON.parse(text);
  })
  .catch((err) => {
    assert.fail(err);
  });
```

(Ch. 43, Section 43.2.1.2, lines 984-1000)

# Relationships

## Builds Upon
- **Callback pattern** -- Promises standardize callback-based async patterns
- **Event loop** -- Promise settlement is delivered asynchronously

## Enables
- **Async function** -- async/await is built on Promises
- **Promise chaining** -- `.then()` and `.catch()` return Promises enabling chains
- **Promise combinator functions** -- `Promise.all()`, `Promise.race()`, etc.

## Contrasts With
- **Callback pattern** -- Promises have cleaner signatures, chaining, and unified error handling
- **Event pattern** -- Promises deliver exactly one result; events deliver zero or more

# Common Errors

- **Error**: Creating unnecessary new Promises around existing Promises (Promise constructor anti-pattern)
  **Correction**: Chain existing Promises with `.then()` instead of wrapping in `new Promise()`

# Common Confusions

- **Confusion**: A Promise "contains" the result immediately after creation
  **Clarification**: A Promise starts empty and is filled asynchronously when the operation completes

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.1.1-43.1.3, lines 115-202.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit definition with clear characterization
- Cross-reference status: verified across Ch. 41, 43, 44
