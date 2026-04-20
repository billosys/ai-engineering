---
concept: Iteration Data Consumers
slug: iteration-data-consumers
category: iteration
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Synchronous iteration"
chapter_number: 32
pdf_page: null
section: "32.9.2 Synchronous iteration: data consumers"
extraction_confidence: high
aliases:
  - "iteration consumers"
prerequisites:
  - iteration-protocol
extends: []
related:
  - for-of-loop
  - spread-syntax
  - array-destructuring
contrasts_with: []
answers_questions:
  - "How does `for-of` relate to the iteration protocol?"
---

# Quick Definition

Iteration data consumers are language constructs and APIs that accept iterables as input, including for-of, spread, destructuring, Array.from(), new Map(), new Set(), yield*, and Promise combinators.

# Core Definition

The iteration protocol defines a standard set of consumers that use iterables. Language constructs that iterate include: for-of loop, spreading into Array literals and function calls, Array destructuring patterns, and yield*. APIs that convert iterables to data structures include: Object.fromEntries(), Array.from(), new Map(), new Set(), new WeakMap(), new WeakSet(). Promise combinators (Promise.all, .race, .any, .allSettled) also consume iterables.

# Prerequisites

- **iteration-protocol** -- consumers rely on the protocol

# Key Properties

1. Language constructs: for-of, spread (`...`), Array destructuring, yield*
2. Data structure constructors: Array.from(), new Map(), new Set()
3. Object construction: Object.fromEntries()
4. Promise combinators: Promise.all(), Promise.race(), Promise.any(), Promise.allSettled()
5. Grouping: Map.groupBy(), Object.groupBy()
6. All use the iteration protocol internally

# Construction / Recognition

```js
for (const x of iterable) { }           // for-of
const arr = [...iterable];               // spread
const [a, b] = iterable;                // destructuring
const map = new Map(iterableOfPairs);    // constructor
yield* iterable;                         // generator delegation
```

# Context & Application

Understanding the full set of iteration consumers helps developers recognize how broadly the iteration protocol applies and why implementing Iterable on a custom data structure is so powerful.

# Examples

```js
// All of these consume iterables:
const arr = Array.from(new Set(['a', 'b']));
const map = new Map([['key', 'val']]);
const [x, y] = 'hi';
const spread = [...'abc']; // ['a', 'b', 'c']
```

(Chapter 32, Section 32.9.2, lines 1315-1413)

# Relationships

## Builds Upon
- **iteration-protocol** -- the protocol these consumers use

## Enables
- Universal data access patterns

## Related
- **for-of-loop** -- the primary consumer
- **spread-syntax** -- expansion consumer
- **array-destructuring** -- extraction consumer

## Contrasts With
- None

# Common Errors

- **Error**: Assuming only for-of uses the iteration protocol.
  **Correction**: Spread, destructuring, Array.from, Map/Set constructors, yield*, and Promise combinators all use it.

# Common Confusions

- **Confusion**: `new Map(array)` requires an Array argument.
  **Clarification**: `new Map()` accepts any iterable of key-value pairs, not just Arrays.

# Source Reference

Chapter 32: Synchronous iteration, Section 32.9.2, lines 1315-1413.

# Verification Notes

- Definition source: direct (quick reference section)
- Confidence rationale: Comprehensive enumeration in the source
- Cross-reference status: verified
