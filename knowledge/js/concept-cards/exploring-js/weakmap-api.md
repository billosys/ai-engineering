---
concept: WeakMap API
slug: weakmap-api
category: collections
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "WeakMaps (WeakMap) (advanced)"
chapter_number: 37
pdf_page: null
section: "37.5 Quick reference: WeakMap"
extraction_confidence: high
aliases:
  - "WeakMap methods"
prerequisites:
  - weakmap-data-structure
extends: []
related:
  - map-methods
contrasts_with:
  - map-methods
answers_questions:
  - "How do `WeakMap`/`WeakSet` relate to `Map`/`Set` regarding garbage collection?"
---

# Quick Definition

WeakMap provides only four methods (`.get()`, `.set()`, `.has()`, `.delete()`) and a constructor -- no `.size`, `.clear()`, `.keys()`, `.values()`, `.entries()`, or `.forEach()` -- matching its black-box design.

# Core Definition

The WeakMap API consists of: constructor `new WeakMap(entries?)`, `.get(key)`, `.set(key, value)` (returns `this`), `.has(key)`, and `.delete(key)`. No iteration, no size, no clearing. The methods work identically to their Map equivalents but are the only operations possible.

# Prerequisites

- **weakmap-data-structure** -- the collection these methods operate on

# Key Properties

1. `new WeakMap(entries?)` -- accepts iterable of [key, value] pairs
2. `.get(key)` -- returns value or undefined
3. `.set(key, value)` -- returns `this` (chainable)
4. `.has(key)` -- boolean
5. `.delete(key)` -- boolean
6. No other methods (no iteration, no size, no clear)

# Construction / Recognition

```js
const wm = new WeakMap();
const key = {};
wm.set(key, 42);
wm.get(key); // 42
wm.has(key); // true
wm.delete(key); // true
```

# Context & Application

The limited API reflects the black-box design. To "clear" a WeakMap, create a new instance. To "iterate", maintain a separate list of keys.

# Examples

```js
const wm = new WeakMap([[{}, 'a'], [{}, 'b']]);
// Cannot inspect contents -- entries may be GC'd at any time
```

(Chapter 37, Section 37.5, lines 266-276)

# Relationships

## Builds Upon
- **weakmap-data-structure** -- API for WeakMaps

## Enables
- CRUD on WeakMap entries

## Related
- **map-methods** -- WeakMap methods are a subset

## Contrasts With
- **map-methods** -- Map has additional iteration and size methods

# Common Errors

- **Error**: Looking for `.clear()` on a WeakMap.
  **Correction**: WeakMaps don't support `.clear()`. Assign a new WeakMap to the variable instead.

# Common Confusions

- **Confusion**: WeakMap and Map have the same API.
  **Clarification**: WeakMap has only 4 methods; Map has many more including iteration and size.

# Source Reference

Chapter 37: WeakMaps (WeakMap) (advanced), Section 37.5, lines 266-276.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly listed
- Cross-reference status: verified
