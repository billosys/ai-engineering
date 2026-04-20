---
concept: WeakMap Use Cases
slug: weakmap-use-cases
category: collections
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "WeakMaps (WeakMap) (advanced)"
chapter_number: 37
pdf_page: null
section: "37.4 Use case for WeakMaps: attaching values to objects"
extraction_confidence: high
aliases:
  - "WeakMap caching"
  - "WeakMap private data"
prerequisites:
  - weakmap-data-structure
  - weakly-held-keys
extends: []
related:
  - weakmap-black-box
contrasts_with: []
answers_questions:
  - "How do `WeakMap`/`WeakSet` relate to `Map`/`Set` regarding garbage collection?"
---

# Quick Definition

WeakMaps are primarily used for two patterns: caching computed results keyed by objects (cache cleans up automatically when objects are GC'd), and storing private instance data outside objects (using WeakMaps as external property stores).

# Core Definition

WeakMaps can externally attach values to objects: setting an "external property" via `wm.set(obj, value)` that is automatically cleaned up when `obj` is garbage-collected. Two key use cases: (1) caching computed results without memory leaks, and (2) keeping class instance data private by storing it in module-scoped WeakMaps.

# Prerequisites

- **weakmap-data-structure** -- understanding WeakMaps
- **weakly-held-keys** -- enables automatic cleanup

# Key Properties

1. Caching: store computed results keyed by object, auto-cleaned on GC
2. Private data: module-scoped WeakMaps store instance properties invisibly
3. External properties: like adding properties to objects you don't own
4. No memory leaks from forgotten cleanup

# Construction / Recognition

```js
// Caching pattern
const cache = new WeakMap();
function compute(obj) {
  if (cache.has(obj)) return cache.get(obj);
  const result = /* expensive computation */;
  cache.set(obj, result);
  return result;
}
```

# Context & Application

These patterns are used in frameworks, libraries, and any code that needs to associate metadata with objects without modifying them or causing memory leaks.

# Examples

```js
// Caching
const cache = new WeakMap();
function countOwnKeys(obj) {
  if (cache.has(obj)) return [cache.get(obj), 'cached'];
  const count = Object.keys(obj).length;
  cache.set(obj, count);
  return [count, 'computed'];
}

const obj = {foo: 1, bar: 2};
countOwnKeys(obj); // [2, 'computed']
countOwnKeys(obj); // [2, 'cached']

// Private data
const _counter = new WeakMap();
class Countdown {
  constructor(counter) { _counter.set(this, counter); }
  dec() {
    let c = _counter.get(this);
    _counter.set(this, --c);
  }
}
```

(Chapter 37, Section 37.4, lines 138-263)

# Relationships

## Builds Upon
- **weakmap-data-structure** -- the underlying collection
- **weakly-held-keys** -- enables automatic cleanup

## Enables
- Memory-safe caching
- Truly private instance data

## Related
- **weakmap-black-box** -- supports the private data pattern

## Contrasts With
- None

# Common Errors

- **Error**: Using a regular Map for caching objects, causing memory leaks.
  **Correction**: Use a WeakMap so entries are removed when keys are garbage-collected.

# Common Confusions

- **Confusion**: WeakMap private data pattern is obsolete since class `#private` fields.
  **Clarification**: Class private fields (ES2022) are now preferred, but WeakMaps are still useful for external metadata on objects you don't own.

# Source Reference

Chapter 37: WeakMaps (WeakMap) (advanced), Section 37.4, lines 138-263.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly demonstrated with two use cases
- Cross-reference status: verified
