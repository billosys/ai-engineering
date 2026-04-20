---
concept: Iterator Protocol
slug: iterator-protocol
category: iterators-generators
subcategory: iterator-protocol
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Iterators and Generators"
chapter_number: 12
pdf_page: 344
section: "12.1 How Iterators Work"
extraction_confidence: high
aliases:
  - "iteration protocol"
prerequisites: []
extends: []
related:
  - iterable-vs-iterator
  - symbol-iterator
  - generator-functions
contrasts_with: []
answers_questions:
  - "What is an iterator in JavaScript?"
  - "How does `for/of` relate to the iterator protocol?"
  - "What must I understand before learning about generators?"
---

# Quick Definition

The protocol by which JavaScript objects provide sequential access to their values through a `next()` method that returns `{value, done}` result objects, enabling `for/of` loops and spread syntax.

# Core Definition

"There are three separate types that you need to understand to understand iteration in JavaScript. First, there are the *iterable* objects... Second, there is the *iterator* object itself, which performs the iteration. And third, there is the *iteration result* object that holds the result of each step of the iteration" (p. 345). An iterator has a `next()` method returning objects with `value` and `done` properties.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. An **iterable** has a `[Symbol.iterator]()` method that returns an iterator
2. An **iterator** has a `next()` method
3. `next()` returns an **iteration result**: `{value: ..., done: false}` or `{done: true}`
4. When `done` is `true`, iteration is complete
5. Built-in iterables: Array, String, Set, Map, TypedArray
6. Iterators are consumed — once exhausted, they cannot be restarted

# Construction / Recognition

```js
let iterable = [99];
let iterator = iterable[Symbol.iterator]();
for(let result = iterator.next(); !result.done; result = iterator.next()) {
    console.log(result.value)  // 99
}
```

# Context & Application

The iterator protocol underpins `for/of` loops, spread operator, destructuring assignment, `Array.from()`, `new Set()`, `new Map()`, `Promise.all()`, and more.

# Examples

From the source text (p. 345): Manual iteration: `let iter = list[Symbol.iterator](); let head = iter.next().value; let tail = [...iter];` — partially consuming an iterator and spreading the rest. Built-in iterators are themselves iterable (they return `this` from `[Symbol.iterator]()`).

# Relationships

## Enables
- **for/of Loop** — The loop mechanism that consumes iterators
- **Spread Operator** — Expands iterables into arrays/arguments
- **Generator Functions** — A simplified way to create iterators
- **Async Iteration** — The asynchronous version of this protocol

## Related
- **Symbol.iterator** — The well-known symbol used to implement iterables
- **Iterable vs Iterator** — The distinction between the two concepts

# Common Errors

- **Error**: Trying to iterate an iterator a second time after it's been exhausted.
  **Correction**: Iterators are single-use. To iterate again, get a new iterator from the iterable.

# Common Confusions

- **Confusion**: Conflating "iterable" and "iterator."
  **Clarification**: An iterable is an object with a `[Symbol.iterator]()` method. An iterator is the object returned by that method, with a `next()` method. They are distinct roles (though an object can be both).

# Source Reference

Chapter 12: Iterators and Generators, Section 12.1, pages 344-346.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High — core definition with detailed explanation
- Uncertainties: None
- Cross-reference status: Verified
