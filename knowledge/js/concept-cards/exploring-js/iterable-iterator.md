---
concept: Iterable Iterator
slug: iterable-iterator
category: iteration
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Synchronous iteration"
chapter_number: 32
pdf_page: null
section: "32.6 Iterable iterators"
extraction_confidence: high
aliases:
  - "self-iterable iterator"
prerequisites:
  - iterator-interface
  - iterable-interface
extends:
  - iterator-interface
related:
  - one-time-vs-many-times-iterable
contrasts_with: []
answers_questions:
  - "What is an iterable and what is the iteration protocol?"
---

# Quick Definition

An iterable iterator is an iterator that is also iterable -- it returns itself when `[Symbol.iterator]()` is called, allowing iterators to be used directly with for-of and other iteration constructs.

# Core Definition

All built-in iterators in JavaScript are iterable: they implement `[Symbol.iterator]()` by returning `this`. This means iterators can be passed to any construct that expects an iterable (for-of, spread, Array.from, etc.). This design makes generators more versatile, as they can serve as both iterators and iterables.

# Prerequisites

- **iterator-interface** -- the iterator concept
- **iterable-interface** -- the iterable concept

# Key Properties

1. All built-in iterators are iterable (ES6)
2. An iterable iterator returns itself from `[Symbol.iterator]()`
3. Generator objects are iterable iterators
4. Iterator helper method results (ES2025) are iterable iterators
5. This design creates two kinds of iterables: one-time and many-times

# Construction / Recognition

```js
const iterator = Iterator.from(['a', 'b']);
iterator[Symbol.iterator]() === iterator; // true
```

# Context & Application

Iterable iterators enable passing an iterator directly to for-of, Array.from, or spread. This is essential for generators and iterator helper methods to work seamlessly with the iteration ecosystem.

# Examples

```js
// Generator object is an iterable iterator
function* gen() { yield 'hello'; }
const genObj = gen();
genObj instanceof Iterator; // true
Symbol.iterator in genObj; // true

// Iterator helper result is iterable
const iter = Iterator.from([1, 2]).map(x => x * 2);
for (const x of iter) { console.log(x); }
// Output: 2, 4
```

(Chapter 32, Section 32.6, lines 552-710)

# Relationships

## Builds Upon
- **iterator-interface** -- extends it with iterability
- **iterable-interface** -- implements it by returning self

## Enables
- **one-time-vs-many-times-iterable** -- creates the distinction

## Related
- **generator-function** -- generators produce iterable iterators

## Contrasts With
- None

# Common Errors

- **Error**: Spreading an iterable iterator multiple times and expecting all values each time.
  **Correction**: Iterable iterators are one-time iterables. After exhaustion, they produce no more values.

# Common Confusions

- **Confusion**: All iterables behave the same when used multiple times.
  **Clarification**: Arrays (many-times iterables) restart each time; iterable iterators (one-time iterables) continue from where they left off.

# Source Reference

Chapter 32: Synchronous iteration, Section 32.6, lines 552-710.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly explained with examples
- Cross-reference status: verified
