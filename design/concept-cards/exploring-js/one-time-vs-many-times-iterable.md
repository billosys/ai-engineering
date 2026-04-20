---
concept: One-Time vs. Many-Times Iterable
slug: one-time-vs-many-times-iterable
category: iteration
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Synchronous iteration"
chapter_number: 32
pdf_page: null
section: "32.6.3 Iteration quirk: two kinds of iterables"
extraction_confidence: high
aliases:
  - "one-time iterable"
  - "many-times iterable"
prerequisites:
  - iterable-iterator
extends: []
related:
  - iterable-interface
  - iterator-interface
contrasts_with: []
answers_questions:
  - "What is an iterable and what is the iteration protocol?"
---

# Quick Definition

A one-time iterable (an iterable iterator) always returns the same exhaustible iterator, continuing from where it left off. A many-times iterable (like an Array or Set) always returns a fresh iterator, restarting iteration.

# Core Definition

Iterable iterators create a quirk: there are two kinds of iterables. A one-time iterable returns the same iterator (itself) each time `[Symbol.iterator]()` is called, so iteration continues and eventually exhausts. A many-times iterable (Array, Set, etc.) returns a fresh iterator each time, so iteration always restarts from the beginning.

# Prerequisites

- **iterable-iterator** -- the mechanism that creates one-time iterables

# Key Properties

1. One-time iterables: iterator results, generator objects
2. Many-times iterables: Arrays, Sets, Maps, strings
3. Spreading a one-time iterable multiple times yields fewer values each time
4. Spreading a many-times iterable always yields all values

# Construction / Recognition

```js
// One-time iterable
const oneTime = ['a', 'b', 'c'].values();
[...oneTime, ...oneTime, ...oneTime]; // ['a', 'b', 'c']

// Many-times iterable
const manyTimes = ['a', 'b', 'c'];
[...manyTimes, ...manyTimes]; // ['a','b','c', 'a','b','c']
```

# Context & Application

Understanding this distinction is critical to avoid bugs when passing iterators (rather than iterables) to multiple consumers. When reuse is needed, convert to an Array first.

# Examples

```js
const oneTime = ['a', 'b', 'c'].values();
for (const x of oneTime) { break; } // consumed 'a'
Array.from(oneTime); // ['b', 'c'] -- continues
Array.from(oneTime); // [] -- exhausted
```

(Chapter 32, Section 32.6.3, lines 640-710)

# Relationships

## Builds Upon
- **iterable-iterator** -- the cause of one-time iterables

## Enables
- Awareness of iterator state management

## Related
- **iterable-interface** -- many-times iterables
- **iterator-interface** -- one-time iterables (when also iterable)

## Contrasts With
- None

# Common Errors

- **Error**: Using an iterator (one-time iterable) in two separate for-of loops expecting full data both times.
  **Correction**: Convert to an Array first with `Array.from()` or `[...iter]` if you need to iterate multiple times.

# Common Confusions

- **Confusion**: Generators produce many-times iterables.
  **Clarification**: Calling a generator function produces a one-time iterable iterator. To iterate multiple times, call the generator function again.

# Source Reference

Chapter 32: Synchronous iteration, Section 32.6.3, lines 640-710.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly explained with contrasting examples
- Cross-reference status: verified
