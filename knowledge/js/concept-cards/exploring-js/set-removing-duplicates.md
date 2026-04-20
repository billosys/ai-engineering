---
concept: Removing Duplicates with Sets
slug: set-removing-duplicates
category: collections
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Sets (Set)"
chapter_number: 38
pdf_page: null
section: "38.6.1 Removing duplicates from an Array"
extraction_confidence: high
aliases: []
prerequisites:
  - set-data-structure
extends: []
related:
  - array-from
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

Converting an Array to a Set and back removes duplicates: `Array.from(new Set(arr))` or `[...new Set(arr)]`.

# Core Definition

Converting an Array to a Set and back removes duplicates from the Array, since Sets only store unique values. The pattern `Array.from(new Set(arr))` is a concise and efficient deduplication idiom.

# Prerequisites

- **set-data-structure** -- Sets enforce uniqueness

# Key Properties

1. Simple one-liner for deduplication
2. Preserves first occurrence of each value (insertion order)
3. Uses SameValueZero for equality comparison
4. Works with primitives; objects are compared by identity

# Construction / Recognition

```js
const noDuplicates = Array.from(new Set([1, 2, 1, 2, 3]));
// [1, 2, 3]
```

# Context & Application

This is one of the most common Set use cases, frequently seen in data processing and array utilities.

# Examples

```js
const arr = [1, 2, 1, 2, 3, 3, 3];
const noDuplicates = Array.from(new Set(arr));
assert.deepEqual(noDuplicates, [1, 2, 3]);

// Also works with strings
assert.deepEqual(
  new Set('abc'),
  new Set(['a', 'b', 'c'])
);
```

(Chapter 38, Section 38.6, lines 597-624)

# Relationships

## Builds Upon
- **set-data-structure** -- uniqueness property

## Enables
- Concise array deduplication

## Related
- **array-from** -- conversion back to array

## Contrasts With
- None

# Common Errors

- **Error**: Expecting object deduplication by value.
  **Correction**: Objects are compared by identity. `[{a:1}, {a:1}]` still has two elements after Set deduplication.

# Common Confusions

- **Confusion**: The order of deduplicated elements is random.
  **Clarification**: Sets preserve insertion order, so the first occurrence of each value is kept.

# Source Reference

Chapter 38: Sets (Set), Section 38.6.1, lines 597-611.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly demonstrated
- Cross-reference status: verified
