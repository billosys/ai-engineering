---
concept: Promise Chaining
slug: promise-chaining
category: async-programming
subcategory: promises
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Asynchronous JavaScript"
chapter_number: 13
pdf_page: 368
section: "13.2.2 Chaining Promises"
extraction_confidence: high
aliases:
  - "Promise chain"
  - "then chain"
prerequisites:
  - promise-object
  - promise-then
extends: []
related:
  - promise-catch
  - promise-finally
contrasts_with: []
answers_questions:
  - "How do I handle errors in a Promise chain?"
---

# Quick Definition

A pattern where multiple `.then()` calls are linked sequentially, with each `then()` returning a new Promise whose value is determined by the callback's return value, enabling a linear sequence of asynchronous operations.

# Core Definition

"Each invocation of the then() method returns a new Promise object. That new Promise object is not fulfilled until the function passed to then() is complete" (p. 369). If a callback returns a non-Promise value, the chain continues with that value. If it returns a Promise, the chain waits for that Promise to settle. This is the "resolved" state — the chain Promise is locked onto the returned Promise.

# Prerequisites

- **promise-object** — Understanding Promise states
- **promise-then** — Chaining is built on successive then() calls

# Key Properties

1. Each `.then()` returns a new Promise (not the original)
2. Callback return value determines the next Promise's value
3. If callback returns a Promise, the chain waits for it (resolution)
4. Errors propagate down the chain until caught
5. The chain is a sequence of Promises, not multiple handlers on one Promise

# Construction / Recognition

```js
fetch("/api/user/profile")
    .then(response => response.json())
    .then(profile => displayUserProfile(profile))
    .catch(error => handleError(error));
```

# Context & Application

The primary pattern for expressing sequential asynchronous operations. Replaces deeply nested callbacks with a flat, readable chain.

# Examples

From the source text (p. 368-372): `fetch(theURL).then(callback1).then(callback2)` — task 1 returns promise 1, task 2 runs when promise 1 fulfills, task 3 runs when promise 2 fulfills. The detailed walkthrough shows promises 1-4 including the response.json() Promise.

# Relationships

## Builds Upon
- **Promise.then()** — Chaining relies on then() returning new Promises

## Related
- **Promise.catch()** — Error handling at the end of a chain
- **Promise.finally()** — Cleanup at the end of a chain

# Common Errors

- **Error**: Forgetting to return from a `.then()` callback, breaking the chain.
  **Correction**: `.catch(e => { wait(500).then(queryDatabase) })` is wrong — needs `return`: `.catch(e => { return wait(500).then(queryDatabase) })` or use arrow shorthand without braces.

# Common Confusions

- **Confusion**: Thinking `.then()` calls on the same Promise create a chain.
  **Clarification**: `p.then(f1); p.then(f2)` registers two parallel handlers on p. `p.then(f1).then(f2)` creates a sequential chain.

# Source Reference

Chapter 13: Asynchronous JavaScript, Section 13.2.2, pages 368-372.

# Verification Notes

- Definition source: Synthesized from source text
- Confidence rationale: High — detailed step-by-step explanation in source
- Uncertainties: None
- Cross-reference status: Verified
