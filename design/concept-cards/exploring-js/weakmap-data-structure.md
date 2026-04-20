---
concept: WeakMap Data Structure
slug: weakmap-data-structure
category: collections
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "WeakMaps (WeakMap) (advanced)"
chapter_number: 37
pdf_page: null
section: "37.1 How are WeakMaps different from Maps?"
extraction_confidence: high
aliases:
  - "WeakMap"
prerequisites:
  - map-data-structure
extends: []
related:
  - weakmap-use-cases
  - weakmap-black-box
  - weakly-held-keys
contrasts_with:
  - map-data-structure
answers_questions:
  - "How do `WeakMap`/`WeakSet` relate to `Map`/`Set` regarding garbage collection?"
---

# Quick Definition

A WeakMap holds key-value pairs where keys are weakly held (allowing garbage collection when no other references exist) and the collection is a "black box" that cannot be iterated, cleared, or sized.

# Core Definition

WeakMaps are similar to Maps with key differences: they are black boxes where a value can only be accessed with both the WeakMap and the key; keys are weakly held, meaning if a key has no other references, it can be garbage-collected along with its entry. This enables attaching data to objects without preventing their garbage collection, and keeping data private by not exposing the WeakMap.

# Prerequisites

- **map-data-structure** -- WeakMaps are a variant of Maps

# Key Properties

1. Introduced in ES2015 (ES6)
2. Keys must have identity semantics: objects or non-registered symbols (ES2023)
3. Keys are weakly held -- garbage-collectable
4. No iteration, no `.size`, no `.clear()`
5. Only `.get()`, `.set()`, `.has()`, `.delete()`
6. Black box security property

# Construction / Recognition

```js
const wm = new WeakMap();
const key = {};
wm.set(key, 'value');
wm.get(key); // 'value'
// After key is garbage-collected, entry is automatically removed
```

# Context & Application

Primary use cases: caching computed results for objects (cache is cleaned up when object is GC'd), and keeping private data associated with objects outside of the objects themselves.

# Examples

```js
const externalId = new WeakMap();
{
  const obj = {};
  externalId.set(obj, 'x3cdw5am');
  externalId.get(obj); // 'x3cdw5am'
}
// obj can be garbage-collected despite being a WeakMap key
```

(Chapter 37, Section 37.1-37.3, lines 35-127)

# Relationships

## Builds Upon
- **map-data-structure** -- WeakMap is a constrained Map variant

## Enables
- **weakmap-use-cases** -- caching and private data patterns
- Memory-safe external metadata

## Related
- **weakmap-black-box** -- security property
- **weakly-held-keys** -- GC semantics

## Contrasts With
- **map-data-structure** -- Maps have strong keys and support iteration

# Common Errors

- **Error**: Trying to iterate over a WeakMap.
  **Correction**: WeakMaps are not iterable. Store the keys separately if you need to enumerate them.

# Common Confusions

- **Confusion**: WeakMap values are weakly held.
  **Clarification**: Only keys are weakly held. Values are strongly held as long as their key exists.

# Source Reference

Chapter 37: WeakMaps (WeakMap) (advanced), Section 37.1-37.3, lines 35-127.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined as chapter introduction
- Cross-reference status: verified
