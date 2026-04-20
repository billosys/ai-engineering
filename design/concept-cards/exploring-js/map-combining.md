---
concept: Combining Maps
slug: map-combining
category: collections
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Maps (Map)"
chapter_number: 36
pdf_page: null
section: "36.4.2 Combining multiple Maps into a single Map"
extraction_confidence: high
aliases: []
prerequisites:
  - map-data-structure
  - array-spreading
extends: []
related:
  - map-processing
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

Multiple Maps are combined into one via `new Map([...map1, ...map2])`, where entries from later Maps override earlier ones for duplicate keys.

# Core Definition

There are no built-in methods for combining Maps. The workaround is to spread entries from both Maps into an Array and pass it to the Map constructor: `new Map([...map1, ...map2])`. When keys overlap, later entries win. This leverages the fact that Maps are iterable over key-value pairs.

# Prerequisites

- **map-data-structure** -- the collection being combined
- **array-spreading** -- used to collect entries

# Key Properties

1. No built-in merge method
2. Pattern: `new Map([...map1, ...map2])`
3. Later entries override earlier for duplicate keys
4. Preserves insertion order (first occurrence of each key)

# Construction / Recognition

```js
const map1 = new Map().set(1, '1a').set(2, '1b');
const map2 = new Map().set(2, '2b').set(3, '2c');
const combined = new Map([...map1, ...map2]);
// Map { 1 => '1a', 2 => '2b', 3 => '2c' }
```

# Context & Application

Used for merging configuration maps, combining partial results, and providing defaults with overrides.

# Examples

```js
const defaults = new Map([['color', 'blue'], ['size', 'medium']]);
const custom = new Map([['color', 'red']]);
const merged = new Map([...defaults, ...custom]);
// Map { 'color' => 'red', 'size' => 'medium' }
```

(Chapter 36, Section 36.4.2, lines 395-432)

# Relationships

## Builds Upon
- **map-data-structure** -- combining Maps
- **array-spreading** -- spreading entries

## Enables
- Map merging and defaults patterns

## Related
- **map-processing** -- broader Map manipulation

## Contrasts With
- None

# Common Errors

- **Error**: Expecting a `.merge()` method on Maps.
  **Correction**: Use `new Map([...map1, ...map2])` instead.

# Common Confusions

- **Confusion**: The first Map's entries always win for duplicate keys.
  **Clarification**: The last entry wins. `new Map([...map1, ...map2])` preserves map2's values for shared keys.

# Source Reference

Chapter 36: Maps (Map), Section 36.4.2, lines 395-432.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly demonstrated
- Cross-reference status: verified
