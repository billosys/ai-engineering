---
concept: IteratorResult Interface
slug: iterator-result
category: iteration
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Synchronous iteration"
chapter_number: 32
pdf_page: null
section: "32.2 Core iteration roles: iterables and iterators"
extraction_confidence: high
aliases:
  - "IteratorResult"
  - "iteration result object"
prerequisites:
  - iterator-interface
extends: []
related:
  - iteration-protocol
contrasts_with: []
answers_questions:
  - "What is an iterable and what is the iteration protocol?"
---

# Quick Definition

An IteratorResult is a plain object with `.value` (the current iterated value) and `.done` (a boolean indicating whether the end of iteration has been reached), returned by an iterator's `.next()` method.

# Core Definition

The IteratorResult interface is defined as `interface IteratorResult<T> { value: T; done: boolean; }`. The `.done` property is `true` after the last iterated value and `false` beforehand. The values are not returned directly but always wrapped in these objects.

# Prerequisites

- **iterator-interface** -- IteratorResult is what `.next()` returns

# Key Properties

1. Introduced in ES2015 (ES6)
2. Two properties: `.value` and `.done`
3. When `.done` is `false`, `.value` holds the current element
4. When `.done` is `true`, `.value` is typically `undefined`
5. The wrapping enables signaling end-of-iteration alongside values

# Construction / Recognition

```js
// Returned by iterator.next()
{ value: 'a', done: false }  // has more values
{ value: undefined, done: true }  // iteration complete
```

# Context & Application

IteratorResult objects are the communication mechanism between iterators and their consumers. They are typically consumed implicitly by for-of and similar constructs, but seen directly when using manual iteration.

# Examples

```js
const iter = ['a', 'b'][Symbol.iterator]();
iter.next(); // { value: 'a', done: false }
iter.next(); // { value: 'b', done: false }
iter.next(); // { value: undefined, done: true }
```

(Chapter 32, Section 32.3.1, lines 217-233)

# Relationships

## Builds Upon
- **iterator-interface** -- returned by `.next()`

## Enables
- Manual iteration patterns using while loops

## Related
- **iteration-protocol** -- one of the three core interfaces

## Contrasts With
- None

# Common Errors

- **Error**: Checking only `.value` without checking `.done`.
  **Correction**: Always check `.done` first; `.value` can be `undefined` for valid iteration values.

# Common Confusions

- **Confusion**: The last meaningful value has `done: true`.
  **Clarification**: The last meaningful value still has `done: false`. The `done: true` result comes after all values have been delivered.

# Source Reference

Chapter 32: Synchronous iteration, Section 32.2, lines 178-210.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with TypeScript interface
- Cross-reference status: verified
