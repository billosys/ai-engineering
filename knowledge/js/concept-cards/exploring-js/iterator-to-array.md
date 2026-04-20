---
concept: "Iterator .toArray()"
slug: iterator-to-array
category: iteration
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Synchronous iteration"
chapter_number: 32
pdf_page: null
section: "32.10.6 Iterator.prototype.*: methods that return other kinds of values"
extraction_confidence: high
aliases:
  - "Iterator.prototype.toArray"
  - ".toArray()"
prerequisites:
  - iterator-class
extends: []
related:
  - array-from
contrasts_with: []
answers_questions:
  - "What is an iterable and what is the iteration protocol?"
---

# Quick Definition

`.toArray()` (ES2025) materializes all remaining iterator values into a new Array, providing the final step in a lazy iterator method chain.

# Core Definition

`Iterator.prototype.toArray()` collects all remaining elements of an iterator into an Array and returns it. It is the terminal operation in lazy iterator chains, converting the lazy computation to an eager result.

# Prerequisites

- **iterator-class** -- method on Iterator.prototype

# Key Properties

1. Introduced in ES2025
2. Collects all remaining values into an Array
3. Consumes the iterator
4. Terminal operation in iterator chains
5. Alternative to `Array.from(iterator)` or `[...iterator]`

# Construction / Recognition

```js
['a', 'b', 'c'].values().map(x => x + x).toArray();
// ['aa', 'bb', 'cc']
```

# Context & Application

`.toArray()` is the standard way to materialize iterator results after a chain of lazy operations.

# Examples

```js
Iterator.from(['a', 'b', 'c', 'd']).toArray();
// ['a', 'b', 'c', 'd']

new Set([1, 2, 3]).values().filter(x => x > 1).toArray();
// [2, 3]
```

(Chapter 32, Section 32.10.6, lines 1709-1725)

# Relationships

## Builds Upon
- **iterator-class** -- method on Iterator.prototype

## Enables
- Materializing lazy iterator chains

## Related
- **array-from** -- alternative: `Array.from(iter)`

## Contrasts With
- None

# Common Errors

- **Error**: Calling `.toArray()` on an Array directly.
  **Correction**: `.toArray()` is an iterator method. Use `arr.values().toArray()` or just `[...arr]`.

# Common Confusions

- **Confusion**: `.toArray()` and spreading (`[...iter]`) always produce different results.
  **Clarification**: They produce the same result; `.toArray()` is more explicit.

# Source Reference

Chapter 32: Synchronous iteration, Section 32.10.6, lines 1709-1725.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with ES2025 marker
- Cross-reference status: verified
