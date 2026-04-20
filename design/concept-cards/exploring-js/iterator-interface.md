---
concept: Iterator Interface
slug: iterator-interface
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
  - "Iterator"
  - "synchronous iterator"
prerequisites:
  - iterable-interface
extends: []
related:
  - iteration-protocol
  - iterator-result
  - iterator-class
contrasts_with:
  - iterable-interface
answers_questions:
  - "What is an iterable and what is the iteration protocol?"
---

# Quick Definition

An iterator is the pointer used for traversal of an iterable, providing values one at a time via its `.next()` method which returns IteratorResult objects.

# Core Definition

An iterator extends the abstract class `Iterator` and returns iterated values via its method `.next()`. Each call to `.next()` returns an IteratorResult with `.value` (the current value) and `.done` (whether iteration is complete). Before ES2025, `Iterator` was simply an interface; no globally accessible class existed.

# Prerequisites

- **iterable-interface** -- iterators are obtained from iterables

# Key Properties

1. Introduced in ES2015 (ES6); `Iterator` class added in ES2025
2. Defines a `.next()` method returning `{ value, done }`
3. All built-in iterators inherit from `Iterator.prototype`
4. All built-in iterators are also iterable (they return themselves from `[Symbol.iterator]()`)
5. Iterators are stateful -- they track their position in the sequence

# Construction / Recognition

```js
const iterable = ['a', 'b'];
const iterator = iterable[Symbol.iterator]();

iterator.next(); // { value: 'a', done: false }
iterator.next(); // { value: 'b', done: false }
iterator.next(); // { value: undefined, done: true }
```

# Context & Application

Iterators are typically used indirectly through for-of loops and other iteration constructs. Direct use is needed when implementing custom iteration logic or when using iterator helper methods (ES2025).

# Examples

```js
// Manual iteration with while loop
function logAll(iterable) {
  const iterator = iterable[Symbol.iterator]();
  while (true) {
    const {value, done} = iterator.next();
    if (done) break;
    console.log(value);
  }
}
```

(Chapter 32, Section 32.3.2, lines 236-258)

# Relationships

## Builds Upon
- **iterable-interface** -- iterators are produced by iterables

## Enables
- **iterator-helper-methods** -- ES2025 methods on Iterator.prototype
- **generator-function** -- generators return iterators

## Related
- **iterator-result** -- the return type of .next()
- **iterator-class** -- the ES2025 class all built-in iterators extend

## Contrasts With
- **iterable-interface** -- an iterable is a factory; an iterator is the traversal pointer

# Common Errors

- **Error**: Calling `.next()` after iteration is done and expecting new values.
  **Correction**: Once `.done` is `true`, subsequent calls continue to return `{ value: undefined, done: true }`.

# Common Confusions

- **Confusion**: Iterators can be reused after exhaustion.
  **Clarification**: Iterators are one-time use. To iterate again, get a new iterator from the iterable.

# Source Reference

Chapter 32: Synchronous iteration, Section 32.2-32.3, lines 156-258.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with interface and examples
- Cross-reference status: verified
