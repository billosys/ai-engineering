---
concept: Set-Like Objects
slug: set-like-objects
category: collections
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Sets (Set)"
chapter_number: 38
pdf_page: null
section: "38.4 Set-like objects (advanced)"
extraction_confidence: high
aliases:
  - "SetLike interface"
prerequisites:
  - set-data-structure
  - set-operations
extends: []
related:
  - map-data-structure
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

Set methods that accept "other" parameters require only a Set-like interface (`{size, has(key), keys()}`), not an actual Set -- Maps qualify as Set-like, and `.size` can be `Infinity` for infinite mathematical sets.

# Core Definition

A Set-like object implements: `.size` (number, can be `Infinity`), `.has(key)` (boolean), and `.keys()` (iterator). Maps fulfill this interface. The `.size` can be `Infinity` for conceptual infinite sets (e.g., even numbers), though `.union()` and `.symmetricDifference()` don't support infinite Sets. Method `.keys()` was chosen over `[Symbol.iterator]()` for Map compatibility.

# Prerequisites

- **set-data-structure** -- Set-like objects are parameters to Set methods
- **set-operations** -- the methods that accept Set-like objects

# Key Properties

1. Interface: `{size, has(key), keys()}`
2. Maps are Set-like (they have .size, .has, .keys)
3. `.size` can be `Infinity` for infinite sets
4. Custom objects can implement SetLike
5. `.union()` and `.symmetricDifference()` don't support infinite sets

# Construction / Recognition

```js
const setLike = {
  size: 1,
  has(x) { return x === 'b'; },
  * keys() { yield 'b'; },
};
new Set(['a', 'b', 'c']).difference(setLike); // Set {'a', 'c'}
```

# Context & Application

The SetLike interface allows Set methods to work with Maps and custom collections, providing flexibility beyond just Set-to-Set operations.

# Examples

```js
// Maps are Set-like
const mapLike = new Map([['b', true]]);
new Set(['a', 'b', 'c']).difference(mapLike); // Set {'a', 'c'}

// Infinite Set-like
const evenNumbers = {
  has(elem) { return (elem % 2) === 0; },
  size: Infinity,
  keys() { throw new TypeError(); }
};
new Set([0, 1, 2, 3]).difference(evenNumbers); // Set {1, 3}
```

(Chapter 38, Section 38.4, lines 323-446)

# Relationships

## Builds Upon
- **set-data-structure** -- extends Set method parameters
- **set-operations** -- the methods that accept Set-like objects

## Enables
- Set operations with Maps and custom collections
- Conceptual infinite sets

## Related
- **map-data-structure** -- Maps are Set-like

## Contrasts With
- None

# Common Errors

- **Error**: Passing a plain Array to a Set method expecting Set-like.
  **Correction**: Arrays are not Set-like. Convert to a Set first: `set.union(new Set(arr))`.

# Common Confusions

- **Confusion**: Set-like objects must be actual Sets.
  **Clarification**: Any object with `.size`, `.has()`, and `.keys()` qualifies.

# Source Reference

Chapter 38: Sets (Set), Section 38.4, lines 323-446.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with TypeScript interface
- Cross-reference status: verified
