---
concept: Set Iteration
slug: set-iteration
category: collections
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Sets (Set)"
chapter_number: 38
pdf_page: null
section: "38.5 Iterating over Sets"
extraction_confidence: high
aliases:
  - "Set.prototype.values"
  - "Set.prototype.keys"
prerequisites:
  - set-data-structure
  - iteration-protocol
extends: []
related:
  - iterator-helper-methods
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

Sets are iterable in insertion order, with `.values()` (or `[Symbol.iterator]()`) iterating over elements; `.keys()` and `.entries()` exist for Map symmetry, and iterator methods enable mapping/filtering without conversion.

# Core Definition

Sets preserve insertion order during iteration. Default iteration via `[Symbol.iterator]()` is the same as `.values()`. `.keys()` is an alias for `.values()` (for Map symmetry). `.entries()` yields `[value, value]` pairs (for Map symmetry). ES2025 iterator methods enable `.map()` and `.filter()` via `.values().map(...)` and `.values().filter(...)`.

# Prerequisites

- **set-data-structure** -- iterating over Sets
- **iteration-protocol** -- Sets implement it

# Key Properties

1. Iteration follows insertion order
2. `[Symbol.iterator]()` same as `.values()`
3. `.keys()` same as `.values()` (Map symmetry)
4. `.entries()` yields `[value, value]` pairs
5. Iterator methods enable lazy map/filter (ES2025)
6. `.forEach()` also available

# Construction / Recognition

```js
for (const x of set) { console.log(x); }
Array.from(set); // convert to Array
set.values().map(x => x * 2); // lazy transform
```

# Context & Application

Set iteration combined with ES2025 iterator methods provides map/filter capabilities without converting to arrays first.

# Examples

```js
const set = new Set([1, 2, 3]);
const mappedSet = new Set(set.values().map(x => x * 2));
// Set {2, 4, 6}

const filteredSet = new Set(set.values().filter(x => x % 2 === 0));
// Set {2}

// Remove duplicates from array
const noDups = Array.from(new Set([1, 2, 1, 2, 3]));
// [1, 2, 3]
```

(Chapter 38, Section 38.5, lines 448-571)

# Relationships

## Builds Upon
- **set-data-structure** -- iterating over Sets
- **iteration-protocol** -- Sets are iterable

## Enables
- Map/filter on Sets via iterator methods

## Related
- **iterator-helper-methods** -- enables Set transformations

## Contrasts With
- None

# Common Errors

- **Error**: Calling `.map()` directly on a Set.
  **Correction**: Sets don't have `.map()`. Use `new Set(set.values().map(...))`.

# Common Confusions

- **Confusion**: `.keys()` and `.values()` return different things for Sets.
  **Clarification**: They return the same thing. `.keys()` exists only for symmetry with the Map API.

# Source Reference

Chapter 38: Sets (Set), Section 38.5, lines 448-571.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with iterator method patterns
- Cross-reference status: verified
