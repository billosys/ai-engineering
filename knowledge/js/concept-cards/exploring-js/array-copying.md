---
concept: Array Copying
slug: array-copying
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.7 Copying Arrays"
extraction_confidence: high
aliases:
  - "shallow copy"
  - "deep copy"
prerequisites:
  - array-creation
extends: []
related:
  - array-spreading
  - array-from
contrasts_with: []
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

Arrays can be shallow-copied via `.slice()`, `Array.from()`, spreading, or `.values().toArray()`, and deep-copied via `structuredClone()`; shallow copies share element references while deep copies clone them.

# Core Definition

Five ways to copy an Array: `arr.slice()`, `Array.from(arr)`, `[...arr]`, `arr.values().toArray()` (all shallow), and `structuredClone(arr)` (deep). A shallow copy shares the original elements; a deep copy recursively clones them.

# Prerequisites

- **array-creation** -- must have an array to copy

# Key Properties

1. Four shallow copy methods available
2. Only `structuredClone()` produces deep copies
3. Shallow copies share element references
4. Deep copies have limitations (no functions, no Symbols)

# Construction / Recognition

```js
const arr = ['a', 'b'];
const shallow1 = arr.slice();
const shallow2 = Array.from(arr);
const shallow3 = [...arr];
const shallow4 = arr.values().toArray();
const deep = structuredClone(arr);
```

# Context & Application

Choose shallow copying for most cases. Use `structuredClone()` when elements contain nested objects that must be independent copies.

# Examples

```js
const arr = ['a', 'b'];
const copy = [...arr];
assert.deepEqual(copy, arr);
assert.ok(copy !== arr); // different object
```

(Chapter 34, Section 34.7, lines 968-996)

# Relationships

## Builds Upon
- **array-creation** -- creates new arrays from existing

## Enables
- Non-destructive array operations

## Related
- **array-spreading** -- one of the copy methods
- **array-from** -- another copy method

## Contrasts With
- None

# Common Errors

- **Error**: Expecting spreading to deep copy nested objects.
  **Correction**: Spreading creates a shallow copy. Use `structuredClone()` for deep copies.

# Common Confusions

- **Confusion**: `.slice()` and `structuredClone()` produce the same result.
  **Clarification**: `.slice()` is shallow (shares nested objects); `structuredClone()` is deep (clones them).

# Source Reference

Chapter 34: Arrays (Array), Section 34.7, lines 968-996.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly enumerated with all five methods
- Cross-reference status: verified
