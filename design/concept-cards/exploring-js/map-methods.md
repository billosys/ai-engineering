---
concept: Map Methods
slug: map-methods
category: collections
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Maps (Map)"
chapter_number: 36
pdf_page: null
section: "36.6 Quick reference: Map"
extraction_confidence: high
aliases:
  - "Map.prototype.get"
  - "Map.prototype.set"
  - "Map.prototype.has"
  - "Map.prototype.delete"
  - "Map.prototype.clear"
prerequisites:
  - map-data-structure
extends: []
related:
  - map-iteration
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

Map provides methods for single-entry operations (`.get()`, `.set()`, `.has()`, `.delete()`) and bulk operations (`.size`, `.clear()`), with `.set()` being chainable.

# Core Definition

Single entry methods: `.get(key)` returns value or undefined; `.set(key, value)` creates/updates and returns `this` (chainable); `.has(key)` returns boolean; `.delete(key)` returns boolean. Bulk methods: `.size` getter returns entry count; `.clear()` removes all entries.

# Prerequisites

- **map-data-structure** -- methods operate on Maps

# Key Properties

1. `.get(key)` -- returns value or undefined
2. `.set(key, value)` -- chainable, returns `this`
3. `.has(key)` -- boolean check
4. `.delete(key)` -- returns true if deleted, false otherwise
5. `.size` -- getter for entry count
6. `.clear()` -- removes all entries

# Construction / Recognition

```js
const map = new Map()
  .set('foo', true)
  .set('bar', false); // chainable
map.size; // 2
map.has('foo'); // true
map.get('foo'); // true
map.delete('foo'); // true
map.clear();
```

# Context & Application

These methods provide the complete CRUD interface for Map entries. The chainable `.set()` enables fluent initialization.

# Examples

```js
const map = new Map([['foo', 123]]);
assert.equal(map.has('foo'), true);
assert.equal(map.delete('foo'), true);
assert.equal(map.has('foo'), false);
```

(Chapter 36, Section 36.6, lines 546-697)

# Relationships

## Builds Upon
- **map-data-structure** -- the data structure these methods operate on

## Enables
- Complete CRUD for Map entries

## Related
- **map-iteration** -- iteration methods

## Contrasts With
- None

# Common Errors

- **Error**: Checking `map.get(key) === undefined` to determine if a key exists.
  **Correction**: A key can exist with value `undefined`. Use `map.has(key)` instead.

# Common Confusions

- **Confusion**: `.delete()` returns the deleted value.
  **Clarification**: `.delete()` returns a boolean indicating whether a deletion occurred.

# Source Reference

Chapter 36: Maps (Map), Section 36.6, lines 546-697.

# Verification Notes

- Definition source: direct
- Confidence rationale: Complete API reference in source
- Cross-reference status: verified
