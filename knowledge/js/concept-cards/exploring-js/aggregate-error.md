---
concept: AggregateError
slug: aggregate-error
category: async-programming
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Promises for asynchronous programming"
chapter_number: 43
pdf_page: null
section: "43.5.4.1 AggregateError"
extraction_confidence: high
aliases: []
prerequisites:
  - promise-any
extends: []
related:
  - promise-combinator-functions
contrasts_with: []
answers_questions:
  - "What distinguishes Promise.all() from Promise.race() from Promise.any()?"
---

# Quick Definition

`AggregateError` (ES2021) is an Error subclass that holds multiple errors in its `.errors` property, used by `Promise.any()` when all input Promises are rejected.

# Core Definition

"Exploring JavaScript" Ch. 43 provides the type: `class AggregateError extends Error { errors: Array<any>; constructor(errors: Iterable<any>, message: string = '', options?: ErrorOptions); }`. It is the rejection value of `Promise.any()` when all Promises reject. Introduced in ES2021.

# Prerequisites

- **Promise.any()** -- `AggregateError` is the rejection type for `Promise.any()`

# Key Properties

1. Introduced in ES2021
2. Subclass of `Error`
3. `.errors` property contains an Array of all rejection values
4. Accepts `ErrorOptions` with `cause` property (ES2022)

# Construction / Recognition

```js
Promise.any([
  Promise.reject('ERROR A'),
  Promise.reject('ERROR B'),
  Promise.reject('ERROR C'),
])
.catch(aggregateError =>
  assert.deepEqual(aggregateError.errors, ['ERROR A', 'ERROR B', 'ERROR C'])
);
```

(Ch. 43, Section 43.5.4.2, lines 1734-1744)

# Context & Application

Encountered when using `Promise.any()` with all-rejecting inputs. Provides access to all individual error reasons.

# Examples

See construction example above. (Ch. 43, Section 43.5.4.1, lines 1691-1711)

# Relationships

## Builds Upon
- **Promise.any()** -- AggregateError is its rejection type

# Common Errors

- **Error**: Accessing `.message` expecting all error details
  **Correction**: Access `.errors` array for individual rejection reasons

# Common Confusions

- **Confusion**: AggregateError is thrown by `Promise.all()`
  **Clarification**: `Promise.all()` rejects with the first rejection value directly; only `Promise.any()` uses AggregateError

# Source Reference

Chapter 43: Promises for asynchronous programming, Section 43.5.4.1, lines 1691-1711.

# Verification Notes

- Definition source: direct from source text with type signature
- Confidence rationale: explicit type definition
- Cross-reference status: verified
