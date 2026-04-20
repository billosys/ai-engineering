---
concept: Map Iteration
slug: map-iteration
category: collections
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Maps (Map)"
chapter_number: 36
pdf_page: null
section: "36.2 Iterating over Maps"
extraction_confidence: high
aliases:
  - "Map.prototype.entries"
  - "Map.prototype.keys"
  - "Map.prototype.values"
prerequisites:
  - map-data-structure
  - iteration-protocol
extends: []
related:
  - for-of-loop
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

Maps are iterable over key-value pairs (via `[Symbol.iterator]()` or `.entries()`), with `.keys()` and `.values()` providing iterators over keys or values alone, all in insertion order.

# Core Definition

Maps support iteration through `.entries()` (key-value pairs), `.keys()`, `.values()`, and `[Symbol.iterator]()` (same as `.entries()`). All iterate in insertion order. The default iteration yields `[key, value]` pairs, enabling destructuring in for-of: `for (const [key, value] of map)`. All returned iterators are also iterables, supporting both Array.from() and iterator methods.

# Prerequisites

- **map-data-structure** -- iterating over Maps
- **iteration-protocol** -- Maps implement it

# Key Properties

1. Default iteration yields [key, value] pairs
2. `.entries()` -- key-value pair iterator
3. `.keys()` -- key iterator
4. `.values()` -- value iterator
5. `[Symbol.iterator]()` -- same as `.entries()`
6. All iterate in insertion order
7. `.forEach(callback)` also available

# Construction / Recognition

```js
for (const [key, value] of map) {
  console.log(key, value);
}
for (const key of map.keys()) { }
for (const value of map.values()) { }
```

# Context & Application

Map iteration with destructuring is the idiomatic way to process all entries. The insertion-order guarantee makes Maps deterministic and testable.

# Examples

```js
const map = new Map().set(false, 'no').set(true, 'yes');
for (const [key, value] of map) {
  console.log(key + ' = ' + value);
}
// false = no
// true = yes

// Convert to arrays
map.keys().toArray(); // [false, true]
Array.from(map.entries()); // [[false,'no'], [true,'yes']]
```

(Chapter 36, Section 36.2, lines 183-283)

# Relationships

## Builds Upon
- **map-data-structure** -- what is being iterated
- **iteration-protocol** -- Maps implement it

## Enables
- Processing all Map entries
- Converting Maps to Arrays

## Related
- **for-of-loop** -- primary way to iterate

## Contrasts With
- None

# Common Errors

- **Error**: Expecting Map iteration to yield values directly (like Arrays).
  **Correction**: Maps yield `[key, value]` pairs. Destructure to get individual components.

# Common Confusions

- **Confusion**: Map insertion order is unreliable.
  **Clarification**: Maps guarantee insertion order for all iteration methods.

# Source Reference

Chapter 36: Maps (Map), Section 36.2, lines 183-283.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with examples
- Cross-reference status: verified
