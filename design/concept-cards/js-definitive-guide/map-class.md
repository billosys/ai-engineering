---
# === CORE IDENTIFICATION ===
concept: Map Class
slug: map-class

# === CLASSIFICATION ===
category: standard-library
subcategory: collections
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "The JavaScript Standard Library"
chapter_number: 11
pdf_page: 289
section: "11.1.2 The Map Class"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - set-class
  - weak-map
contrasts_with:
  - set-class

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

An ES6 collection class that maps arbitrary keys to arbitrary values, providing fast key-based lookup regardless of map size, unlike plain objects which only support string and symbol keys.

# Core Definition

"A Map object represents a set of values known as keys, where each key has another value associated with (or 'mapped to') it" (p. 289). Unlike plain objects, Maps allow any value as a key (including objects, arrays, `null`, `NaN`), compare keys by identity, maintain insertion order, and provide a `size` property.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Any JavaScript value can be a key (not limited to strings/symbols like objects)
2. Keys compared by identity (like `===`) — two empty objects `{}` are different keys
3. `get()`, `set()`, `has()`, `delete()`, `clear()` methods
4. `size` property gives the number of key-value pairs
5. Iterable — yields `[key, value]` pairs in insertion order
6. `set()` returns the map itself, enabling chaining

# Construction / Recognition

```js
let m = new Map();
let n = new Map([["one", 1], ["two", 2]]);
let p = new Map(Object.entries(obj));  // From object
```

# Context & Application

Use Map instead of plain objects when keys may not be strings, when you need to preserve insertion order, when you need the `size` property, or when you want to avoid prototype pollution issues.

# Examples

From the source text (p. 289-291): `new Map().set("one", 1).set("two", 2).set("three", 3)` demonstrates chaining. Iteration with destructuring: `for(let [key, value] of m) { ... }`. Separate iteration: `[...m.keys()]` returns `["x", "y"]`, `[...m.values()]` returns `[1, 2]`. Note: `m.set({}, 1); m.set({}, 2); m.size` is `2` because each `{}` is a different key.

# Relationships

## Enables
- **Iteration with for/of** — Maps are iterable, yielding [key, value] pairs

## Related
- **Set Class** — Another ES6 collection; Sets store values only, Maps store key-value pairs
- **WeakMap** — A variant that allows garbage collection of its keys

## Contrasts With
- **Plain Objects** — Objects only support string/symbol keys and have prototype chain issues; Maps support any key type and have clean semantics

# Common Errors

- **Error**: Using `map[key] = value` syntax instead of `map.set(key, value)`.
  **Correction**: Maps use `get()` and `set()` methods. Square bracket notation sets regular object properties, not Map entries.

# Common Confusions

- **Confusion**: Expecting `forEach()` callback to receive `(key, value)` like `for/of`.
  **Clarification**: Map's `forEach()` passes `(value, key)` — value first, key second, matching Array's `forEach(element, index)` convention.

# Source Reference

Chapter 11: The JavaScript Standard Library, Section 11.1.2, pages 289-291.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High — thoroughly described
- Uncertainties: None
- Cross-reference status: Verified
