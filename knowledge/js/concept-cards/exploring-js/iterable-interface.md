---
concept: Iterable Interface
slug: iterable-interface
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
  - "Iterable"
  - "synchronous iterable"
prerequisites: []
extends: []
related:
  - iteration-protocol
  - iterator-interface
  - symbol-iterator
contrasts_with:
  - iterator-interface
answers_questions:
  - "What is an iterable and what is the iteration protocol?"
---

# Quick Definition

An iterable is an object whose contents can be traversed sequentially by implementing a `[Symbol.iterator]()` method that returns an iterator.

# Core Definition

The Iterable interface requires a single method keyed by `Symbol.iterator` that returns an Iterator. As defined in the specification: `interface Iterable<T> { [Symbol.iterator]() : Iterator<T>; }`. Data sources such as Arrays, Sets, Maps, and strings implement this interface.

# Prerequisites

Foundational concept -- requires understanding of Symbol.iterator.

# Key Properties

1. Introduced in ES2015 (ES6)
2. Defined by having a `[Symbol.iterator]()` method
3. Built-in iterables: Array, String, Set, Map, TypedArray
4. Enables use with for-of, spread, destructuring, Array.from(), new Map(), new Set()
5. Custom objects can be made iterable by implementing `[Symbol.iterator]()`

# Construction / Recognition

```js
// Any object with [Symbol.iterator]() is iterable
const myIterable = {
  * [Symbol.iterator]() {
    yield 'good';
    yield 'morning';
  }
};
Array.from(myIterable); // ['good', 'morning']
```

# Context & Application

Iterables are the uniform interface through which all iteration-based language constructs access data. Any new data structure that implements Iterable gains automatic compatibility with for-of, spread, destructuring, and more.

# Examples

```js
// Arrays are iterable
for (const x of ['a', 'b']) { console.log(x); }

// Sets are iterable
const set = new Set(['hello', 'world']);
const arr = [...set]; // ['hello', 'world']

// Strings are iterable
const [first] = 'abc'; // first === 'a'
```

(Chapter 32, Section 32.3.4, lines 285-355)

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **for-of-loop** -- iterates over the iterable
- **spread-syntax** -- expands iterable values
- **array-destructuring** -- extracts from iterables

## Related
- **iteration-protocol** -- the overarching protocol
- **iterator-interface** -- returned by the iterable's method

## Contrasts With
- **iterator-interface** -- an iterable produces iterators; an iterator does the actual traversal

# Common Errors

- **Error**: Assuming plain objects are iterable.
  **Correction**: Plain objects do not implement `[Symbol.iterator]()`. Use `Object.entries(obj)` to get an iterable of key-value pairs.

# Common Confusions

- **Confusion**: An iterable and an iterator are the same thing.
  **Clarification**: An iterable is a factory for iterators. It produces a new iterator each time `[Symbol.iterator]()` is called (for many-times iterables like Arrays).

# Source Reference

Chapter 32: Synchronous iteration, Section 32.2, lines 156-210.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with TypeScript interface notation
- Cross-reference status: verified
