---
concept: Async Function
slug: async-function
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Async functions"
chapter_number: 44
pdf_page: null
section: "44.1 Async functions: the basics"
extraction_confidence: high
aliases:
  - async/await
  - async function declaration
prerequisites:
  - promise
  - promise-chaining
extends:
  - promise
related:
  - await-operator
  - async-callable-entities
contrasts_with:
  - callback-pattern
answers_questions:
  - "What is an async function?"
  - "How do I use async/await to write asynchronous code?"
  - "How do callbacks, Promises, and async/await relate as async patterns?"
---

# Quick Definition

An async function is a function declared with the `async` keyword that always returns a Promise and can use `await` to pause execution until a Promise settles, providing synchronous-looking syntax for asynchronous code.

# Core Definition

"Exploring JavaScript" Ch. 44: "Async functions provide better syntax for code that uses Promises." Two keywords are important: "The keyword async before function means that this is an async function. The await operator is applied to Promises and either extracts fulfillment values or throws rejection values." Async functions were introduced in ES2017. "From the outside, it is virtually impossible to tell the difference between an async function and a function that returns a Promise."

# Prerequisites

- **Promise** -- async functions are built on Promises
- **Promise chaining** -- async/await replaces explicit chaining

# Key Properties

1. Introduced in ES2017
2. Declared with `async` keyword before `function`
3. Always returns a Promise (even for non-Promise return values)
4. Can use `await` to pause on Promises
5. `throw` inside an async function rejects the returned Promise
6. `return` inside an async function resolves the returned Promise
7. Start synchronously, settle asynchronously

# Construction / Recognition

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

Equivalent Promise-based code:
```js
function fetchJsonViaPromises(url) {
  return fetch(url)
    .then(request => request.text())
    .then(text => JSON.parse(text))
    .catch(error => assert.fail(error));
}
```

(Ch. 44, Section 44.1, lines 73-107)

# Context & Application

Async functions are the preferred way to write asynchronous code in modern JavaScript. They provide try/catch error handling and sequential-looking control flow for async operations.

# Examples

Both are called the same way:
```js
fetchJsonAsync('http://example.com/person.json')
  .then(obj => {
    assert.deepEqual(obj, { first: 'Jane', last: 'Doe' });
  });
```

(Ch. 44, Section 44.1, lines 114-121)

# Relationships

## Builds Upon
- **Promise** -- async functions are syntactic sugar for Promises
- **Promise chaining** -- async/await replaces explicit chains

## Enables
- **Await operator** -- `await` can only be used inside async functions
- **Async generator** -- combines async and generator features

## Contrasts With
- **Callback pattern** -- async functions provide much cleaner syntax

# Common Errors

- **Error**: Forgetting `await` when calling a Promise-returning function
  **Correction**: Without `await`, you get a Promise object, not the resolved value

# Common Confusions

- **Confusion**: "Asynchronous function" and "async function" are the same
  **Clarification**: An "asynchronous function" is any function that delivers results asynchronously; an "async function" is specifically defined with the `async` keyword

# Source Reference

Chapter 44: Async functions, Section 44.1, lines 64-134.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit definition as chapter focus
- Cross-reference status: verified against Ch. 43
