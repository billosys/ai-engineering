---
concept: Async Map Pattern
slug: async-map-pattern
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Async functions"
chapter_number: 44
pdf_page: null
section: "44.3.3 Example: .map() with an async function as a callback"
extraction_confidence: high
aliases:
  - async Array.map()
  - Promise.all with map
prerequisites:
  - async-function
  - await-operator
  - promise-all
  - awaiting-is-shallow
extends: []
related:
  - await-concurrency
contrasts_with: []
answers_questions:
  - "How do I use async/await to write asynchronous code?"
---

# Quick Definition

When using `.map()` with an async callback, the result is an Array of Promises (not resolved values). Wrap with `await Promise.all(arr.map(async (x) => ...))` to get the actual resolved values.

# Core Definition

"Exploring JavaScript" Ch. 44: "What happens if we use an async function as a callback for .map()? Then the result is an Array of Promises." The solution: "We can use Promise.all() to convert that Array of Promises to a Promise for an Array and await that Promise."

# Prerequisites

- **Async function** -- the callback is async
- **Await operator** -- await the combined result
- **Promise.all()** -- combines the Promise array
- **Awaiting is shallow** -- explains why `.map()` returns Promises

# Key Properties

1. `.map(async (x) => ...)` returns `Array<Promise>`, not `Array<value>`
2. Wrap with `Promise.all()` to get resolved values
3. All operations run concurrently (started immediately by `.map()`)
4. Use `for...of` with `await` for sequential processing instead

# Construction / Recognition

```js
const uppercaseTexts = await Promise.all(
  urls.map(async (url) => {
    const response = await fetch(url);
    const text = await response.text();
    return text.toUpperCase();
  })
);
```

(Ch. 44, Section 44.3.3, lines 477-488)

# Context & Application

Essential pattern for processing arrays of async operations concurrently with async/await.

# Examples

See construction example above. (Ch. 44, Section 44.3.3, lines 477-488)

# Relationships

## Builds Upon
- **Awaiting is shallow** -- the reason `.map()` returns Promises
- **Promise.all()** -- combines the results

## Related
- **Await concurrency** -- concurrent processing pattern

# Common Errors

- **Error**: Using `arr.forEach(async ...)` expecting sequential execution
  **Correction**: Use `for...of` with `await` for sequential; use `Promise.all` with `.map` for concurrent

# Common Confusions

- **Confusion**: `.map()` with async callback returns resolved values
  **Clarification**: It returns an Array of Promises that must be awaited

# Source Reference

Chapter 44: Async functions, Section 44.3.3, lines 443-498.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit example section
- Cross-reference status: verified
