---
# === CORE IDENTIFICATION ===
concept: Iteration Protocol
slug: iteration-protocol

# === CLASSIFICATION ===
category: iteration
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Synchronous iteration"
chapter_number: 32
pdf_page: null
section: "32.1 What is synchronous iteration about?"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "synchronous iteration protocol"
  - "iteration API"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - iterable-interface
  - iterator-interface
  - iterator-result
  - for-of-loop
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an iterable and what is the iteration protocol?"
  - "How do I use `for-of` loops with iterables?"
---

# Quick Definition

The iteration protocol is a set of interfaces (Iterable, Iterator, IteratorResult) that connects data sources (Arrays, Sets, Maps) with data consumers (for-of, spread, destructuring) through a standardized sequential access mechanism.

# Core Definition

Synchronous iteration is a protocol (interfaces plus rules for using them) that connects two groups of entities in JavaScript: data sources that deliver their contents sequentially through the Iterable interface, and data consumers that access input one value at a time. As Rauschmayer states: "data comes in all shapes and sizes... we have a whole class of constructs and algorithms that only need to access their input sequentially."

# Prerequisites

Foundational concept with no prerequisites beyond basic JavaScript objects and methods.

# Key Properties

1. Introduced in ES2015 (ES6) as a core language feature
2. Connects data producers (Array, Set, Map, strings) with data consumers (for-of, spread, destructuring)
3. Comprises three interfaces: Iterable, Iterator, and IteratorResult
4. Any object implementing Iterable can be used with all iteration-based constructs
5. Developing a new data structure only requires implementing Iterable to gain access to all iteration tools

# Construction / Recognition

The protocol is defined by three TypeScript-style interfaces:

```js
interface Iterable<T> {
  [Symbol.iterator]() : Iterator<T>;
}

abstract class Iterator<T> {
  abstract next() : IteratorResult<T>;
}

interface IteratorResult<T> {
  value: T;
  done: boolean;
}
```

# Context & Application

Used whenever sequential access to a collection's elements is needed. The protocol abstracts away the internal structure of data, allowing uniform processing of Arrays, Sets, Maps, strings, generators, and custom data structures.

# Examples

```js
const iterable = ['a', 'b'];
const iterator = iterable[Symbol.iterator]();

iterator.next(); // { value: 'a', done: false }
iterator.next(); // { value: 'b', done: false }
iterator.next(); // { value: undefined, done: true }
```

(Chapter 32, Section 32.3.1, lines 217-233)

# Relationships

## Builds Upon
- No prerequisites -- foundational protocol

## Enables
- **for-of-loop** -- uses the protocol to iterate
- **spread-syntax** -- iterates to expand values
- **array-destructuring** -- iterates to extract values
- **generator-function** -- produces iterators via yield

## Related
- **iterable-interface** -- one of the three protocol interfaces
- **iterator-interface** -- the pointer used for traversal
- **iterator-result** -- wraps each yielded value

## Contrasts With
- None at this level

# Common Errors

- **Error**: Trying to iterate over a non-iterable value (e.g., a plain object).
  **Correction**: Plain objects are not iterable. Use `Object.keys()`, `Object.values()`, or `Object.entries()` to get an iterable.

# Common Confusions

- **Confusion**: The iteration protocol is the same as `for-of`.
  **Clarification**: `for-of` is one of many consumers of the protocol. Spreading, destructuring, `Array.from()`, `new Map()`, `new Set()`, and `yield*` also consume iterables.

# Source Reference

Chapter 32: Synchronous iteration, Section 32.1-32.2, lines 98-210.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with interfaces and detailed explanation
- Cross-reference status: verified across multiple sections
