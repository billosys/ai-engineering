---
concept: Iterable vs Iterator
slug: iterable-vs-iterator
category: iterators-generators
subcategory: iterator-protocol
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Iterators and Generators"
chapter_number: 12
pdf_page: 345
section: "12.1 How Iterators Work"
extraction_confidence: high
aliases: []
prerequisites:
  - iterator-protocol
extends: []
related:
  - symbol-iterator
contrasts_with: []
answers_questions:
  - "What is an iterator in JavaScript?"
  - "How does `for/of` relate to the iterator protocol?"
---

# Quick Definition

An iterable is an object with a `[Symbol.iterator]()` method that returns an iterator; an iterator is an object with a `next()` method — they are distinct roles, though an object can serve as both by returning `this` from its `[Symbol.iterator]()` method.

# Core Definition

"An *iterable* object is any object with a special iterator method that returns an iterator object. An *iterator* is any object with a next() method that returns an iteration result object" (p. 345). Built-in iterators are themselves iterable: they have a `[Symbol.iterator]()` method that returns `this`, enabling partially-consumed iterators to be used with `for/of`.

# Prerequisites

- **iterator-protocol** — Understanding the three-part protocol (iterable, iterator, result)

# Key Properties

1. Iterable: has `[Symbol.iterator]()` method → can be used with `for/of`
2. Iterator: has `next()` method → produces values sequentially
3. An object can be both by implementing both methods
4. Built-in iterators return `this` from `[Symbol.iterator]()` for convenience
5. Iterables can create multiple independent iterators
6. Iterators are typically single-use (stateful)

# Construction / Recognition

An iterable-and-iterator object pattern:
```js
return {
    [Symbol.iterator]() { return this; },
    next() { return (next <= last) ? { value: next++ } : { done: true }; }
};
```

# Context & Application

Understanding the distinction is crucial for implementing custom iterables. A class (iterable) should return a new iterator each time `[Symbol.iterator]()` is called, so multiple `for/of` loops can iterate independently.

# Examples

From the source text (p. 345-346): `let iter = list[Symbol.iterator](); let head = iter.next().value; let tail = [...iter];` — the iterator is partially consumed, then the spread operator consumes the rest because the iterator is itself iterable.

# Relationships

## Builds Upon
- **Iterator Protocol** — The distinction is part of the protocol

## Related
- **Symbol.iterator** — The symbol that makes an object iterable

# Common Errors

- **Error**: Implementing `[Symbol.iterator]()` to return `this` on a class that maintains shared state, causing concurrent iterations to interfere.
  **Correction**: Return a new iterator object from `[Symbol.iterator]()` each time, with independent state.

# Common Confusions

- **Confusion**: Thinking every iterator is automatically iterable.
  **Clarification**: An iterator is only iterable if it also implements `[Symbol.iterator]()`. Built-in iterators do, but custom iterators must explicitly add this method.

# Source Reference

Chapter 12: Iterators and Generators, Section 12.1, pages 345-346.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
