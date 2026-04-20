---
concept: Error Handling in Async Functions
slug: async-function-error-handling
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Async functions"
chapter_number: 44
pdf_page: null
section: "44.2.2 Awaiting rejected Promises"
extraction_confidence: high
aliases:
  - try/catch with await
  - async error handling
prerequisites:
  - async-function
  - await-operator
extends: []
related:
  - promise-error-handling
  - return-await
contrasts_with: []
answers_questions:
  - "How do I use async/await to write asynchronous code?"
---

# Quick Definition

Error handling in async functions uses standard `try/catch` syntax: `await` throws the rejection value of a rejected Promise, which can be caught with `catch`, replacing the `.catch()` method chains of Promise-based code.

# Core Definition

"Exploring JavaScript" Ch. 44: "If its operand is a rejected Promise, then await throws the rejection value." This means standard `try/catch` blocks work for handling async errors, unifying sync and async error handling in a single mechanism. Throwing in an async function rejects its result Promise.

# Prerequisites

- **Async function** -- error handling context
- **Await operator** -- converts rejections to thrown exceptions

# Key Properties

1. `await rejectedPromise` throws the rejection value
2. Standard `try/catch` catches both sync exceptions and async rejections
3. `throw` in an async function rejects the returned Promise
4. Unifies sync and async error handling syntax
5. Use `return await` in try/catch to properly catch returned rejected Promises

# Construction / Recognition

```js
async function f() {
  try {
    await Promise.reject(new Error('Problem!'));
    assert.fail(); // never reached
  } catch (err) {
    assert.deepEqual(err, new Error('Problem!'));
  }
}
```

(Ch. 44, Section 44.2.2, lines 313-328)

# Context & Application

Try/catch with await is the standard error handling pattern in modern JavaScript async code, replacing `.catch()` chains.

# Examples

```js
async function fetchJsonAsync(url) {
  try {
    const request = await fetch(url);
    const text = await request.text();
    return JSON.parse(text);
  } catch (error) {
    assert.fail(error);
  }
}
```

(Ch. 44, Section 44.1, lines 75-84)

# Relationships

## Builds Upon
- **Async function** -- error handling context
- **Await operator** -- converts rejections to exceptions

## Related
- **Promise error handling** -- the Promise-chain equivalent
- **return await** -- important for try/catch correctness

# Common Errors

- **Error**: Not wrapping `await` calls in try/catch, causing unhandled rejections
  **Correction**: Always handle potential rejections with try/catch or a `.catch()` on the returned Promise

# Common Confusions

- **Confusion**: Try/catch in async functions only catches synchronous errors
  **Clarification**: `await` converts async rejections into thrown exceptions, making them catchable by try/catch

# Source Reference

Chapter 44: Async functions, Section 44.2.2, lines 313-328.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit example with rejected Promise
- Cross-reference status: verified
