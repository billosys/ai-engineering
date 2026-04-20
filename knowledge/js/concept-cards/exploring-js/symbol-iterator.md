---
concept: Symbol.iterator
slug: symbol-iterator
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
  - "[Symbol.iterator]()"
prerequisites: []
extends: []
related:
  - iterable-interface
  - iteration-protocol
contrasts_with: []
answers_questions:
  - "What is an iterable and what is the iteration protocol?"
---

# Quick Definition

`Symbol.iterator` is a well-known Symbol used as a method key on objects to mark them as iterable; calling `obj[Symbol.iterator]()` returns an iterator for that object.

# Core Definition

`Symbol.iterator` is the method key that the iteration protocol uses to request an iterator from an iterable. An object is iterable if it has a method keyed by `Symbol.iterator` that returns an iterator. This is how data consumers (for-of, spread, destructuring) obtain iterators from data sources.

# Prerequisites

Foundational concept (symbols and method keys).

# Key Properties

1. Well-known Symbol defined in the spec
2. Method key for the iterable protocol
3. `obj[Symbol.iterator]()` returns an iterator
4. All built-in iterables (Array, Set, Map, String) implement it

# Construction / Recognition

```js
const arr = ['a', 'b'];
const iter = arr[Symbol.iterator]();
iter.next(); // { value: 'a', done: false }
```

# Context & Application

`Symbol.iterator` is the bridge between iterables and the language constructs that consume them. Implementing `[Symbol.iterator]()` on a custom object makes it work with for-of, spread, and destructuring.

# Examples

```js
class Range {
  constructor(start, end) {
    this.start = start;
    this.end = end;
  }
  * [Symbol.iterator]() {
    for (let i = this.start; i < this.end; i++) yield i;
  }
}
[...new Range(1, 4)]; // [1, 2, 3]
```

(Chapter 32, Section 32.2, lines 178-200)

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **iterable-interface** -- defines how to implement it

## Related
- **iteration-protocol** -- the protocol that uses this symbol

## Contrasts With
- None

# Common Errors

- **Error**: Using a regular string method name instead of `Symbol.iterator`.
  **Correction**: The method must use the Symbol key: `[Symbol.iterator]()`, not `iterator()`.

# Common Confusions

- **Confusion**: `Symbol.iterator` is the iterator itself.
  **Clarification**: `Symbol.iterator` is a method key. The method it keys returns an iterator.

# Source Reference

Chapter 32: Synchronous iteration, Section 32.2, lines 178-200.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined in protocol interfaces
- Cross-reference status: verified
