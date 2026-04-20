---
concept: Map Data Structure
slug: map-data-structure
category: collections
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Maps (Map)"
chapter_number: 36
pdf_page: null
section: "36.1 Using Maps"
extraction_confidence: high
aliases:
  - "Map"
  - "ES6 Map"
prerequisites:
  - iterable-interface
extends: []
related:
  - map-methods
  - map-iteration
  - map-vs-object
contrasts_with:
  - weakmap-data-structure
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

A Map is an ES6 collection that maps arbitrary keys to arbitrary values, preserving insertion order and providing O(1) access via `.get()`, `.set()`, `.has()`, and `.delete()`.

# Core Definition

Before ES6, JavaScript used objects as dictionaries from strings to arbitrary values. ES6 introduced Maps, which are dictionaries from arbitrary values to arbitrary values. An instance of Map maps keys to values; a single key-value mapping is called an entry. Maps preserve insertion order and use SameValueZero for key comparison (like `===` but treats `NaN` as equal to itself).

# Prerequisites

- **iterable-interface** -- Maps accept iterables in constructor and are themselves iterable

# Key Properties

1. Introduced in ES2015 (ES6)
2. Keys can be any value (objects, primitives, symbols)
3. Preserves insertion order
4. `.size` property (not `.length`)
5. Key comparison via SameValueZero (NaN === NaN)
6. Different objects are always different keys (identity-based)

# Construction / Recognition

```js
const map = new Map([
  [1, 'one'],
  [2, 'two'],
]);

const map2 = new Map()
  .set(1, 'one')
  .set(2, 'two');
```

# Context & Application

Use Maps when keys are not strings/symbols, when the key set changes at runtime, when insertion order matters, or when you need a clean dictionary without prototype pollution.

# Examples

```js
const map = new Map();
map.set('foo', 123);
assert.equal(map.get('foo'), 123);
assert.equal(map.get('bar'), undefined);
assert.equal(map.has('foo'), true);
map.delete('foo');
assert.equal(map.size, 0);
```

(Chapter 36, Section 36.1, lines 68-181)

# Relationships

## Builds Upon
- **iterable-interface** -- constructor accepts iterable of pairs

## Enables
- **map-methods** -- operations on entries
- **map-iteration** -- iterating entries

## Related
- **map-vs-object** -- when to choose which

## Contrasts With
- **weakmap-data-structure** -- WeakMap has weak keys and no iteration

# Common Errors

- **Error**: Using objects as Map keys and expecting equality by value.
  **Correction**: Maps compare objects by identity. Two different `{}` are different keys.

# Common Confusions

- **Confusion**: Maps and plain objects serve the same purpose.
  **Clarification**: Maps support any key type, have `.size`, preserve order deterministically, and have no prototype interference.

# Source Reference

Chapter 36: Maps (Map), Section 36.1, lines 68-181.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined as the chapter introduction
- Cross-reference status: verified
