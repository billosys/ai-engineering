---
# === CORE IDENTIFICATION ===
concept: Promise Constructor
slug: promise-constructor

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
section: "43.1.3 Implementing a Promise-based function"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - new Promise()
  - revealing constructor pattern

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - promise-states
extends: []
related:
  - resolving-vs-fulfilling
  - promise-with-resolvers
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create and consume a Promise?"
---

# Quick Definition

The `Promise` constructor creates a new Promise by accepting an executor callback that receives `resolve` and `reject` functions, which are the only way to settle the Promise from inside the constructor.

# Core Definition

"Exploring JavaScript" Ch. 43 explains that `new Promise((resolve, reject) => { ... })` uses the "revealing constructor pattern": "the Promise constructor is revealing its internal capabilities, but only to the code that constructs the promise in question. The ability to resolve or reject the promise is only revealed to the constructing code, and is crucially not revealed to anyone using the promise."

# Prerequisites

- **Promise** -- the constructor creates Promises
- **Promise states** -- resolve/reject change the state

# Key Properties

1. The executor callback runs synchronously
2. `resolve(value)` resolves the Promise (may fulfill or adopt another Promise's state)
3. `reject(reason)` rejects the Promise with the given reason
4. After first invocation of resolve or reject, subsequent calls have no effect
5. Exceptions thrown inside the executor are converted to rejections

# Construction / Recognition

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

(Ch. 43, Section 43.1.3, lines 180-191)

# Context & Application

Used to wrap callback-based APIs into Promise-based ones (promisification) and to create Promises from scratch. Modern code often prefers `Promise.withResolvers()` (ES2024) when resolve/reject are needed outside the constructor.

# Examples

Promisifying XMLHttpRequest:
```js
function httpGet(url) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.onload = () => {
      if (xhr.status === 200) {
        resolve(xhr.responseText);
      } else {
        reject(new Error(xhr.statusText));
      }
    };
    xhr.onerror = () => reject(new Error('Network error'));
    xhr.open('GET', url);
    xhr.send();
  });
}
```

(Ch. 43, Section 43.2.2, lines 1021-1038)

# Relationships

## Builds Upon
- **Promise** -- the constructor creates Promise instances
- **Promise states** -- resolve and reject change the state

## Enables
- **Promisification** -- wrapping callback APIs in Promises

## Related
- **Promise.withResolvers()** -- alternative that exposes resolve/reject outside the constructor

# Common Errors

- **Error**: Wrapping an existing Promise in a new Promise (constructor anti-pattern)
  **Correction**: Chain the existing Promise with `.then()` instead

# Common Confusions

- **Confusion**: The executor callback is called asynchronously
  **Clarification**: The executor runs synchronously when the Promise is created

# Source Reference

Chapter 43: Promises for asynchronous programming, Sections 43.1.3, 43.1.3.1, lines 174-239.

# Verification Notes

- Definition source: direct from source text with Domenic Denicola quotation
- Confidence rationale: explicit definition with named pattern
- Cross-reference status: verified
