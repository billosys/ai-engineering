---
concept: Await Expressions
slug: await-expressions
category: async-programming
subcategory: async-await
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Asynchronous JavaScript"
chapter_number: 13
pdf_page: 385
section: "13.3.1 await Expressions"
extraction_confidence: high
aliases:
  - "await keyword"
  - "await operator"
prerequisites:
  - async-functions
  - promise-object
extends: []
related:
  - sequential-vs-parallel-await
contrasts_with: []
answers_questions:
  - "How does `async/await` relate to Promises?"
  - "How do I use `async/await` with error handling?"
---

# Quick Definition

The `await` keyword that pauses execution of an `async` function until a Promise settles, resolving to the fulfillment value or throwing the rejection reason, making asynchronous code read like synchronous code.

# Core Definition

"The await keyword takes a Promise and turns it back into a return value or a thrown exception. Given a Promise object p, the expression await p waits until p settles. If p fulfills, then the value of await p is the fulfillment value of p. On the other hand, if p is rejected, then the await p expression throws the rejection value of p" (p. 385).

# Prerequisites

- **async-functions** — await can only be used inside async functions
- **promise-object** — await operates on Promises

# Key Properties

1. Can only be used inside `async` functions (or top-level module code)
2. Pauses the async function (not the entire program)
3. Fulfillment value becomes the expression's value
4. Rejection throws — can be caught with try/catch
5. Does not block — other code continues to run

# Construction / Recognition

```js
let response = await fetch("/api/user/profile");
let profile = await response.json();
```

# Context & Application

Used wherever a Promise value is needed. Combined with try/catch, it provides synchronous-looking error handling for async operations.

# Examples

From the source text (p. 385): `let response = await fetch("/api/user/profile"); let profile = await response.json();` — two sequential awaits that read like synchronous code.

# Relationships

## Builds Upon
- **Async Functions** — await only works inside async functions
- **Promise Object** — await unwraps Promises

## Enables
- **Sequential vs Parallel Await** — Understanding when sequential await is appropriate

# Common Errors

- **Error**: Using `await` in a regular (non-async) function.
  **Correction**: The function containing `await` must be declared `async`.

- **Error**: Sequentially awaiting independent Promises instead of using `Promise.all()`.
  **Correction**: `let [v1, v2] = await Promise.all([getJSON(url1), getJSON(url2)])` runs in parallel.

# Common Confusions

- **Confusion**: Thinking `await` makes the program block.
  **Clarification**: `await` only pauses the current async function. The event loop continues processing other events and callbacks.

# Source Reference

Chapter 13: Asynchronous JavaScript, Section 13.3.1, pages 385-386.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
