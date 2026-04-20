---
concept: "Map.groupBy()"
slug: map-groupby
category: collections
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Maps (Map)"
chapter_number: 36
pdf_page: null
section: "36.6.2 Map.*"
extraction_confidence: high
aliases:
  - "Map.groupBy"
prerequisites:
  - map-data-structure
  - iterable-interface
extends: []
related:
  - grouping-iterables
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

`Map.groupBy(items, computeGroupKey)` (ES2024) groups iterable items into a Map where each key is a group key computed by the callback, and each value is an Array of items sharing that group key.

# Core Definition

`Map.groupBy()` is a static method that takes an iterable and a callback that computes a group key for each item. It returns a Map where each entry's key is a group key and its value is an Array of all items that produced that group key. This enables grouping by arbitrary key types (unlike `Object.groupBy()` which is limited to string keys).

# Prerequisites

- **map-data-structure** -- returns a Map
- **iterable-interface** -- accepts any iterable

# Key Properties

1. Introduced in ES2024
2. Static method: `Map.groupBy(items, callback)`
3. Callback receives (item, index)
4. Returns Map<K, Array<T>>
5. Supports any key type (unlike Object.groupBy)

# Construction / Recognition

```js
Map.groupBy(
  ['orange', 'apricot', 'banana', 'apple'],
  str => str[0]
);
// Map { 'o' => ['orange'], 'a' => ['apricot','apple'], 'b' => ['banana'] }
```

# Context & Application

Use for grouping data by computed keys, especially when keys are not strings (e.g., numbers, objects). Prefer `Object.groupBy()` when you need to destructure the result.

# Examples

```js
assert.deepEqual(
  Map.groupBy(
    ['orange', 'apricot', 'banana', 'apple', 'blueberry'],
    (str) => str[0]
  ),
  new Map()
    .set('o', ['orange'])
    .set('a', ['apricot', 'apple'])
    .set('b', ['banana', 'blueberry'])
);
```

(Chapter 36, Section 36.6.2, lines 576-607)

# Relationships

## Builds Upon
- **map-data-structure** -- produces a Map
- **iterable-interface** -- accepts any iterable

## Enables
- Data categorization by computed keys

## Related
- **grouping-iterables** -- the broader concept

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `Map.groupBy()` to return an object.
  **Correction**: It returns a Map. Use `Object.groupBy()` for a plain object result.

# Common Confusions

- **Confusion**: `Map.groupBy()` is an instance method.
  **Clarification**: It is a static method: `Map.groupBy(items, fn)`, not `map.groupBy(fn)`.

# Source Reference

Chapter 36: Maps (Map), Section 36.6.2, lines 576-607.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with ES2024 marker
- Cross-reference status: verified
