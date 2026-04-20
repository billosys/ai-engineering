---
# === CORE IDENTIFICATION ===
concept: Promise.prototype.then()
slug: promise-then

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
section: "43.1.6 Returning and throwing in .then() callbacks"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - ".then()"
  - then method

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise
  - promise-states
extends: []
related:
  - promise-catch
  - promise-chaining
  - promise-finally
contrasts_with:
  - promise-catch

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create and consume a Promise?"
---

# Quick Definition

`.then()` registers a callback for the fulfillment value of a Promise and returns a new Promise, enabling method chaining. The returned Promise's state depends on what the callback returns or throws.

# Core Definition

"Exploring JavaScript" Ch. 43: ".then() registers callbacks for Promise fulfillments. It also returns a new Promise. Doing so enables method chaining." The returned Promise is resolved based on the callback's behavior: returning a non-Promise value fulfills it; returning a Promise resolves it; throwing an exception rejects it.

# Prerequisites

- **Promise** -- `.then()` is a method on Promise instances
- **Promise states** -- `.then()` callback runs on fulfillment

# Key Properties

1. Registers a callback called when the Promise is fulfilled
2. Returns a new Promise (enabling chaining)
3. Callback returning a non-Promise value -> returned Promise fulfilled with that value
4. Callback returning a Promise -> returned Promise resolves with that Promise
5. Callback throwing an exception -> returned Promise rejected with that exception
6. `.then()` is "the asynchronous version of the synchronous semicolon"

# Construction / Recognition

```js
Promise.resolve('abc')
  .then(str => str + str)        // returns non-Promise
  .then(str2 => assert.equal(str2, 'abcabc'));

Promise.resolve('abc')
  .then(str => Promise.resolve(123))  // returns Promise
  .then(num => assert.equal(num, 123));

Promise.resolve('abc')
  .then(str => { throw myError; })    // throws
  .catch(err => assert.equal(err, myError));
```

(Ch. 43, Section 43.1.6, lines 349-436)

# Context & Application

`.then()` is the primary mechanism for consuming Promise fulfillment values and chaining sequential async operations.

# Examples

From the source:
```js
Promise.resolve('abc')
  .then((str) => {
    return str + str; // returns non-Promise value
  })
  .then((str2) => {
    assert.equal(str2, 'abcabc');
  });
```

(Ch. 43, Section 43.1.6.1, lines 366-374)

# Relationships

## Builds Upon
- **Promise** -- `.then()` is a Promise instance method

## Enables
- **Promise chaining** -- `.then()` returns a Promise enabling chains

## Related
- **Promise.catch()** -- handles rejections; `.then()` handles fulfillments
- **Promise.finally()** -- runs regardless of fulfillment or rejection

## Contrasts With
- **Promise.catch()** -- `.catch()` is triggered by rejections, not fulfillments

# Common Errors

- **Error**: Forgetting to return a value from the `.then()` callback
  **Correction**: Always return values explicitly; otherwise the next `.then()` receives `undefined`

# Common Confusions

- **Confusion**: `.then()` can only receive non-Promise values
  **Clarification**: If the callback returns a Promise, the returned Promise from `.then()` resolves with it (flattening)

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.1.6, lines 349-436.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit detailed explanation with three cases
- Cross-reference status: verified
