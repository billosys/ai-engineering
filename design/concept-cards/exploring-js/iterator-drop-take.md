---
concept: "Iterator .drop() and .take()"
slug: iterator-drop-take
category: iteration
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Synchronous iteration"
chapter_number: 32
pdf_page: null
section: "32.7.1 Iterator.prototype.* methods"
extraction_confidence: high
aliases:
  - "Iterator.prototype.drop"
  - "Iterator.prototype.take"
prerequisites:
  - iterator-class
  - iterator-helper-methods
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What is an iterable and what is the iteration protocol?"
---

# Quick Definition

`.drop(limit)` returns an iterator that skips the first `limit` values; `.take(limit)` returns an iterator with only the first `limit` values -- both are unique to iterators (no Array equivalent) and enable lazy subsequence extraction.

# Core Definition

`iterator.drop(limit)` returns an iterator with all values of the original except the first `limit` ones. `iterator.take(limit)` returns an iterator with only the first `limit` values. Both are ES2025 iterator helper methods unique to iterators (not available on Arrays). They enable lazy pagination and windowing without materializing intermediate arrays.

# Prerequisites

- **iterator-class** -- methods on Iterator.prototype
- **iterator-helper-methods** -- part of the helper method set

# Key Properties

1. Introduced in ES2025
2. `.drop(n)` -- skip first n elements
3. `.take(n)` -- keep only first n elements
4. Both return iterators (lazy)
5. No Array equivalents (use `.slice()` for arrays)
6. Chainable with other iterator methods

# Construction / Recognition

```js
Iterator.from(['a', 'b', 'c', 'd']).drop(1).toArray();
// ['b', 'c', 'd']

Iterator.from(['a', 'b', 'c', 'd']).take(2).toArray();
// ['a', 'b']
```

# Context & Application

Use `.drop()` and `.take()` for lazy pagination, skipping headers, or limiting output from infinite generators.

# Examples

```js
function* naturals() { let n = 0; while (true) yield n++; }

// First 5 natural numbers
naturals().take(5).toArray(); // [0, 1, 2, 3, 4]

// Skip first 3, take next 2
naturals().drop(3).take(2).toArray(); // [3, 4]
```

(Chapter 32, Section 32.7.1, lines 744-773; Section 32.10.4, lines 1491-1601)

# Relationships

## Builds Upon
- **iterator-class** -- provides the methods
- **iterator-helper-methods** -- part of the set

## Enables
- Lazy pagination and windowing

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Calling `.drop()` or `.take()` on an Array.
  **Correction**: These are iterator methods. Use `arr.values().drop(n)` or `arr.slice()`.

# Common Confusions

- **Confusion**: `.take()` creates a copy of the first N elements.
  **Clarification**: `.take()` returns a lazy iterator; elements are produced on demand.

# Source Reference

Chapter 32: Synchronous iteration, Section 32.7.1, lines 744-773.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with ES2025 markers
- Cross-reference status: verified
