---
concept: Promise.resolve() and Promise.reject()
slug: promise-resolve-reject
category: async-programming
subcategory: promises
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Asynchronous JavaScript"
chapter_number: 13
pdf_page: 379
section: "13.2.6 Making Promises"
extraction_confidence: high
aliases:
  - "Promise.resolve()"
  - "Promise.reject()"
prerequisites:
  - promise-object
extends: []
related:
  - promise-constructor
contrasts_with: []
answers_questions:
  - "What is a Promise?"
---

# Quick Definition

Static factory methods that create Promises with predetermined outcomes: `Promise.resolve(value)` creates a Promise that fulfills with the given value, and `Promise.reject(reason)` creates a Promise that rejects with the given reason.

# Core Definition

"Promise.resolve() takes a value as its single argument and returns a Promise that will immediately (but asynchronously) be fulfilled to that value" (p. 379). If passed a Promise, it returns a new Promise that resolves to that Promise. "Promise.reject() takes a single argument and returns a Promise that will be rejected with that value as the reason."

# Prerequisites

- **promise-object** — These are static methods on the Promise class

# Key Properties

1. `Promise.resolve(value)` — creates a fulfilled Promise (asynchronously)
2. `Promise.reject(reason)` — creates a rejected Promise (asynchronously)
3. `Promise.resolve(promise)` — wraps and resolves to the given Promise
4. Settlement is always asynchronous, even though the value is known
5. Useful for starting Promise chains and handling synchronous special cases

# Construction / Recognition

```js
let p = Promise.resolve(42);  // Fulfilled with 42
let q = Promise.reject(new Error("bad"));  // Rejected

// Starting a chain:
Promise.resolve([]).then(handleNextInput);

// Error reporting from an async API:
if (badArgs) return Promise.reject(new Error("Invalid arguments"));
```

# Context & Application

Used to convert synchronous values into Promises for API consistency, to start Promise chains, and to report errors from functions that must return Promises.

# Examples

From the source text (p. 379-380): `Promise.resolve()` used to start a sequential Promise chain: `Promise.resolve([]).then(handleNextInput)`. Reporting errors: return `Promise.reject()` for bad arguments in a Promise-returning function instead of throwing synchronously.

# Relationships

## Builds Upon
- **Promise Object** — Static methods on the Promise class

## Related
- **Promise Constructor** — The more general way to create Promises from scratch

# Common Errors

- **Error**: Calling Promise.resolve() and expecting it to fulfill synchronously.
  **Correction**: The Promise fulfills asynchronously — `.then()` callbacks always run after the current synchronous code finishes.

# Common Confusions

- **Confusion**: Thinking `Promise.resolve()` is named "fulfill" and always creates a fulfilled Promise.
  **Clarification**: Passing a Promise to `Promise.resolve(p)` creates a new Promise that resolves *to* p — it may still reject if p rejects.

# Source Reference

Chapter 13: Asynchronous JavaScript, Section 13.2.6, pages 379-380.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
