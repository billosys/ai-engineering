---
# === CORE IDENTIFICATION ===
concept: WeakMap
slug: weak-map

# === CLASSIFICATION ===
category: standard-library
subcategory: collections
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "The JavaScript Standard Library"
chapter_number: 11
pdf_page: 291
section: "11.1.3 WeakMap and WeakSet"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - map-class
extends: []
related:
  - weak-set
contrasts_with:
  - map-class

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

A variant of Map that holds "weak" references to its keys, allowing them to be garbage collected when no other references exist, preventing memory leaks in caching and metadata scenarios.

# Core Definition

"The WeakMap class is a variant of the Map class that does not prevent its key values from being garbage collected" (p. 291). WeakMap keys must be objects or arrays (not primitives). It only supports `get()`, `set()`, `has()`, and `delete()` — it is not iterable and has no `size` property, because its contents can change at any time due to garbage collection.

# Prerequisites

- **map-class** — WeakMap is a variant of Map with restricted functionality

# Key Properties

1. Keys must be objects or arrays — primitives cannot be garbage collected
2. Holds weak references — keys can be garbage collected
3. Not iterable — no `keys()`, `values()`, `forEach()`, or `size`
4. Only `get()`, `set()`, `has()`, `delete()` methods

# Construction / Recognition

```js
let cache = new WeakMap();
// Use objects as keys — they won't prevent garbage collection
cache.set(someObject, computedResult);
```

# Context & Application

Primary use case is associating metadata or cached values with objects without preventing those objects from being garbage collected. Common for private data in classes and memoization caches.

# Examples

From the source text (p. 291-292): Using WeakMap as a cache for expensive computations on objects. If you used a regular Map, the objects would remain in memory forever. With WeakMap, when the object is no longer referenced elsewhere, both the key and value can be reclaimed.

# Relationships

## Builds Upon
- **Map Class** — WeakMap is a restricted variant of Map

## Related
- **WeakSet** — The Set equivalent with weak references

## Contrasts With
- **Map Class** — Map holds strong references and is iterable; WeakMap holds weak references and is not iterable

# Common Errors

- **Error**: Trying to use a primitive (string, number) as a WeakMap key.
  **Correction**: WeakMap keys must be objects. Primitives are not subject to garbage collection and cannot be used.

# Common Confusions

- **Confusion**: Expecting to iterate over WeakMap entries or check its size.
  **Clarification**: WeakMap is deliberately not iterable and has no `size` property because its contents depend on garbage collection, which is unpredictable.

# Source Reference

Chapter 11: The JavaScript Standard Library, Section 11.1.3, pages 291-292.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: High — clearly explained
- Uncertainties: None
- Cross-reference status: Verified
