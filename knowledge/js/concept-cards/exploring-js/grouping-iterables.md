---
concept: Grouping Iterables
slug: grouping-iterables
category: iteration
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Synchronous iteration"
chapter_number: 32
pdf_page: null
section: "32.8 Grouping iterables"
extraction_confidence: high
aliases:
  - "Map.groupBy()"
  - "Object.groupBy()"
prerequisites:
  - iterable-interface
  - map-data-structure
extends: []
related:
  - map-data-structure
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

`Map.groupBy()` and `Object.groupBy()` (ES2024) group the elements of any iterable into a Map or object, respectively, using a callback that computes a group key for each element.

# Core Definition

`Map.groupBy(items, computeGroupKey)` returns a Map where each key is a group key computed by the callback, and each value is an Array of items with that group key. `Object.groupBy()` works the same but returns a null-prototype object. Both accept any iterable as their first argument.

# Prerequisites

- **iterable-interface** -- the items parameter is an iterable
- **map-data-structure** -- Map.groupBy returns a Map

# Key Properties

1. Introduced in ES2024
2. `Map.groupBy()` returns a Map (supports any key type)
3. `Object.groupBy()` returns a null-prototype object (keys are strings/symbols)
4. Works with any iterable, not just Arrays
5. The callback receives (item, index) parameters

# Construction / Recognition

```js
Map.groupBy([0, -5, 3, -4, 8, 9], x => Math.sign(x));
// Map { 0 => [0], -1 => [-5,-4], 1 => [3,8,9] }

Object.groupBy([0, -5, 3], x => Math.sign(x));
// { '0': [0], '-1': [-5], '1': [3], __proto__: null }
```

# Context & Application

Use `Map.groupBy()` when group keys are not strings/symbols or when you need a Map. Use `Object.groupBy()` when you want to destructure the result. Both are useful for categorizing data.

# Examples

```js
const settled = [
  { status: 'rejected', reason: 'Jhon' },
  { status: 'fulfilled', value: 'Jane' },
];
const {fulfilled, rejected} = Object.groupBy(settled, x => x.status);
```

(Chapter 32, Section 32.8, lines 1117-1267)

# Relationships

## Builds Upon
- **iterable-interface** -- groups any iterable
- **map-data-structure** -- Map.groupBy returns a Map

## Enables
- Categorization and case handling patterns

## Related
- **map-data-structure** -- result type for Map.groupBy

## Contrasts With
- None

# Common Errors

- **Error**: Using `Map.groupBy()` then trying to destructure the result.
  **Correction**: Use `Object.groupBy()` if you need destructuring; Maps don't support it directly.

# Common Confusions

- **Confusion**: `Map.groupBy()` and `Object.groupBy()` produce the same results.
  **Clarification**: `Map.groupBy()` returns a Map (arbitrary keys); `Object.groupBy()` returns a null-prototype object (string keys only).

# Source Reference

Chapter 32: Synchronous iteration, Section 32.8, lines 1117-1267.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with ES2024 marker
- Cross-reference status: verified
