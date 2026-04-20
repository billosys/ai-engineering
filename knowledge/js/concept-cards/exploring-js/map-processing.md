---
concept: Processing Maps
slug: map-processing
category: collections
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Maps (Map)"
chapter_number: 36
pdf_page: null
section: "36.4 Processing Maps"
extraction_confidence: high
aliases:
  - "copying Maps"
  - "combining Maps"
  - "filtering Maps"
  - "mapping Maps"
prerequisites:
  - map-data-structure
  - map-iteration
extends: []
related:
  - iterator-helper-methods
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

Maps can be copied via `new Map(original)`, combined via `new Map([...map1, ...map2])`, and filtered/mapped using ES2025 iterator methods on `.entries()`.

# Core Definition

Maps are copied by passing them to the Map constructor (shallow copy). Multiple Maps are combined by spreading their entries into an Array and passing to `new Map()`. ES2025 iterator methods enable mapping and filtering: convert to an iterator via `.entries()`, apply `.map()` or `.filter()`, and create a new Map from the result.

# Prerequisites

- **map-data-structure** -- processing Maps
- **map-iteration** -- iteration is the basis for processing

# Key Properties

1. `new Map(original)` -- shallow copy
2. `new Map([...map1, ...map2])` -- combine (later entries win on key conflicts)
3. `.entries().map(...)` -- transform entries (ES2025)
4. `.entries().filter(...)` -- filter entries (ES2025)
5. Without iterator methods: use `Array.from(map)` then Array methods

# Construction / Recognition

```js
// Copy
const copy = new Map(original);

// Combine
const combined = new Map([...map1, ...map2]);

// Map entries (ES2025)
const mapped = new Map(
  original.entries().map(([k, v]) => [k * 2, '_' + v])
);
```

# Context & Application

These patterns are essential for immutable Map manipulation, especially in functional programming styles.

# Examples

```js
const map1 = new Map().set(1, '1a').set(2, '1b');
const map2 = new Map().set(2, '2b').set(3, '2c');
const combined = new Map([...map1, ...map2]);
// Map { 1 => '1a', 2 => '2b', 3 => '2c' }

const filtered = new Map(
  combined.entries().filter(([k, v]) => k < 3)
);
// Map { 1 => '1a', 2 => '2b' }
```

(Chapter 36, Section 36.4, lines 376-498)

# Relationships

## Builds Upon
- **map-data-structure** -- operating on Maps
- **map-iteration** -- iteration enables processing

## Enables
- Immutable Map operations

## Related
- **iterator-helper-methods** -- ES2025 methods used for map/filter

## Contrasts With
- None

# Common Errors

- **Error**: Expecting a built-in `.map()` method on Maps.
  **Correction**: Maps don't have `.map()`. Use `new Map(map.entries().map(...))`.

# Common Confusions

- **Confusion**: `new Map(original)` creates a deep copy.
  **Clarification**: It creates a shallow copy. Keys and values are shared, not cloned.

# Source Reference

Chapter 36: Maps (Map), Section 36.4, lines 376-498.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly demonstrated with ES2025 iterator methods
- Cross-reference status: verified
