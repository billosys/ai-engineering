---
concept: Promise.prototype.finally()
slug: promise-finally
category: async-programming
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.1.10 Promise.prototype.finally()"
extraction_confidence: high
aliases:
  - ".finally()"
  - Promise finally
prerequisites:
  - promise
  - promise-then
  - promise-catch
extends: []
related:
  - promise-chaining
contrasts_with: []
answers_questions:
  - "How do I create and consume a Promise?"
---

# Quick Definition

`.finally()` registers a callback that always executes when a Promise is settled, regardless of whether it was fulfilled or rejected, and passes through the original settlement unless the callback itself throws or returns a rejected Promise.

# Core Definition

"Exploring JavaScript" Ch. 43 states: "The .finally() callback is always executed -- independently of somePromise and the values returned by .then() and/or .catch()." Introduced in ES2018. If the callback returns a non-Promise value or a fulfilled Promise, `.finally()` "ignores that result and simply passes on the settlement that existed before it was called."

# Prerequisites

- **Promise** -- `.finally()` is a Promise instance method
- **Promise.then()** -- understanding the chain context
- **Promise.catch()** -- understanding rejection handling

# Key Properties

1. Introduced in ES2018
2. Callback runs regardless of fulfillment or rejection
3. Passes through the original settlement value (transparent)
4. Only affects the chain if the callback throws or returns a rejected Promise
5. Ideal for cleanup operations (closing connections, releasing resources)

# Construction / Recognition

```js
somePromise
  .then(result => { /* ... */ })
  .catch(error => { /* ... */ })
  .finally(() => {
    connection.close(); // cleanup always runs
  });
```

(Ch. 43, Section 43.1.10, lines 603-699)

# Context & Application

Used for cleanup operations that must run regardless of success or failure: closing database connections, hiding loading spinners, releasing locks.

# Examples

```js
Promise.resolve(123)
  .finally(() => {})
  .then(result => assert.equal(result, 123)); // passes through

Promise.reject('error')
  .finally(() => {})
  .catch(error => assert.equal(error, 'error')); // passes through
```

(Ch. 43, Section 43.1.10, lines 636-649)

# Relationships

## Builds Upon
- **Promise** -- instance method on Promise

## Related
- **Promise chaining** -- `.finally()` participates in chains

# Common Errors

- **Error**: Expecting `.finally()` to receive the settlement value as a parameter
  **Correction**: `.finally()` callback receives no arguments; use `.then()`/`.catch()` for values

# Common Confusions

- **Confusion**: `.finally()` can change the settlement value by returning a value
  **Clarification**: Non-rejected returns are ignored; only throwing or returning a rejected Promise changes the outcome

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.1.10, lines 603-699.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit detailed section
- Cross-reference status: verified
