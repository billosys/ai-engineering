---
concept: Converting Between Maps and Objects
slug: map-converting-to-from-objects
category: collections
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Maps (Map)"
chapter_number: 36
pdf_page: null
section: "36.3.2 Converting between Maps and Objects"
extraction_confidence: high
aliases: []
prerequisites:
  - map-data-structure
extends: []
related:
  - map-vs-object
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

Convert a Map to an object with `Object.fromEntries(map)` (string/symbol keys only), and an object to a Map with `new Map(Object.entries(obj))`.

# Core Definition

As long as a Map only uses strings and symbols as keys, it can be converted to an object via `Object.fromEntries(map)`. An object can be converted to a Map via `new Map(Object.entries(obj))`. These conversions leverage the fact that both `.entries()` and the Map constructor work with iterables of key-value pairs.

# Prerequisites

- **map-data-structure** -- understanding Maps

# Key Properties

1. `Object.fromEntries(map)` -- Map to object (string/symbol keys)
2. `new Map(Object.entries(obj))` -- object to Map
3. Non-string/symbol keys are lost in Map-to-object conversion
4. Both rely on key-value pair iterables

# Construction / Recognition

```js
// Map -> Object
const obj = Object.fromEntries(new Map([['a', 1], ['b', 2]]));
// { a: 1, b: 2 }

// Object -> Map
const map = new Map(Object.entries({ a: 1, b: 2 }));
```

# Context & Application

These conversions are common when interfacing Maps with JSON (which requires objects) or when upgrading object-based dictionaries to Maps for better API.

# Examples

```js
const map = new Map([['a', 1], ['b', 2]]);
const obj = Object.fromEntries(map);
assert.deepEqual(obj, {a: 1, b: 2});

const map2 = new Map(Object.entries(obj));
assert.deepEqual(map2, new Map([['a', 1], ['b', 2]]));
```

(Chapter 36, Section 36.3.2, lines 343-374)

# Relationships

## Builds Upon
- **map-data-structure** -- conversion of Maps

## Enables
- JSON serialization of Maps
- Migration between objects and Maps

## Related
- **map-vs-object** -- understanding when to convert

## Contrasts With
- None

# Common Errors

- **Error**: Converting a Map with object keys to a plain object.
  **Correction**: Object keys are stringified, so `{} => "[object Object]"`. Only use this with string/symbol keys.

# Common Confusions

- **Confusion**: `JSON.stringify(map)` serializes a Map.
  **Clarification**: Maps serialize to `{}` with JSON.stringify. Convert to object first: `JSON.stringify(Object.fromEntries(map))`.

# Source Reference

Chapter 36: Maps (Map), Section 36.3.2, lines 343-374.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly demonstrated
- Cross-reference status: verified
