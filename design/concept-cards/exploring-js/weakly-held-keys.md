---
concept: Weakly Held Keys
slug: weakly-held-keys
category: collections
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "WeakMaps (WeakMap) (advanced)"
chapter_number: 37
pdf_page: null
section: "37.3 The keys of a WeakMap are weakly held"
extraction_confidence: high
aliases:
  - "weak references"
  - "CanBeHeldWeakly"
prerequisites:
  - weakmap-data-structure
extends: []
related:
  - weakset-data-structure
contrasts_with: []
answers_questions:
  - "How do `WeakMap`/`WeakSet` relate to `Map`/`Set` regarding garbage collection?"
---

# Quick Definition

WeakMap keys are weakly held, meaning if no other references to a key exist, the key and its entry can be garbage-collected even though the WeakMap itself still exists.

# Core Definition

The keys of a WeakMap are weakly held: normally if one object refers to another, the latter can't be garbage-collected. With WeakMaps, if a key object has no other references, it can be garbage-collected, and the entry is removed. Valid keys must have identity semantics: objects (ES6) and non-registered symbols (ES2023). Registered symbols (from `Symbol.for()`) cannot be keys because they lack identity semantics.

# Prerequisites

- **weakmap-data-structure** -- weak keys are a WeakMap property

# Key Properties

1. Keys must pass `CanBeHeldWeakly()`: objects or non-registered symbols
2. Registered symbols (`Symbol.for()`) cannot be keys
3. Strings cannot be keys (compared by value, not identity)
4. Garbage collection of keys removes entries automatically
5. No way to observe entry removal (no iteration)

# Construction / Recognition

```js
const wm = new WeakMap();
{
  const obj = {};
  wm.set(obj, 'data');
} // obj is now eligible for GC, entry removed
```

# Context & Application

Weak references prevent memory leaks in caches and metadata stores. When the key object is no longer needed elsewhere, the WeakMap automatically cleans up.

# Examples

```js
// Objects as keys (ES6)
const wm = new WeakMap();
wm.set({}, 'value'); // entry may be GC'd immediately

// Non-registered symbols as keys (ES2023)
const sym = Symbol('myKey');
wm.set(sym, 'value');

// Registered symbols CANNOT be keys
// wm.set(Symbol.for('key'), 'val'); // TypeError
```

(Chapter 37, Section 37.3, lines 70-127)

# Relationships

## Builds Upon
- **weakmap-data-structure** -- defines how keys work in WeakMaps

## Enables
- Automatic memory cleanup
- Cache patterns without memory leaks

## Related
- **weakset-data-structure** -- uses the same weak-holding semantics

## Contrasts With
- None

# Common Errors

- **Error**: Using a string as a WeakMap key.
  **Correction**: Strings are compared by value and are not garbage-collected individually. Only objects and non-registered symbols can be keys.

# Common Confusions

- **Confusion**: All symbols can be WeakMap keys.
  **Clarification**: Only non-registered symbols can be keys. Symbols created with `Symbol.for()` are registered and cannot be used.

# Source Reference

Chapter 37: WeakMaps (WeakMap) (advanced), Section 37.3, lines 70-127.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with specification reference (CanBeHeldWeakly)
- Cross-reference status: verified
