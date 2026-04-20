---
concept: WeakMap Black Box Property
slug: weakmap-black-box
category: collections
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "WeakMaps (WeakMap) (advanced)"
chapter_number: 37
pdf_page: null
section: "37.2 WeakMaps are black boxes"
extraction_confidence: high
aliases:
  - "black box pattern"
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

WeakMaps are black boxes: their contents cannot be inspected, iterated, or enumerated -- accessing a value requires both the WeakMap and its key, providing a security property for private data.

# Core Definition

It is impossible to inspect what's inside a WeakMap: no iteration, no looping over keys/values/entries, no `.size`, no `.clear()`. As Mark Miller stated: "The mapping from weakmap/key pair value can only be observed or affected by someone who has both the weakmap and the key."

# Prerequisites

- **weakmap-data-structure** -- black box is a WeakMap property

# Key Properties

1. No iteration methods (.entries, .keys, .values)
2. No .size property
3. No .clear() method
4. Value access requires both WeakMap and key
5. Provides security: holding only the WeakMap is insufficient

# Construction / Recognition

```js
const wm = new WeakMap();
const key = {};
wm.set(key, 'secret');
// Cannot enumerate, iterate, or inspect wm without key
```

# Context & Application

The black box property makes WeakMaps suitable for storing private data -- if the WeakMap is not exposed, and the key is controlled, the data is effectively private.

# Examples

```js
const _counter = new WeakMap();
const _action = new WeakMap();
class Countdown {
  constructor(counter, action) {
    _counter.set(this, counter);
    _action.set(this, action);
  }
  dec() {
    let counter = _counter.get(this);
    counter--;
    _counter.set(this, counter);
    if (counter === 0) _action.get(this)();
  }
}
Object.keys(new Countdown()); // [] -- truly private
```

(Chapter 37, Section 37.2 and 37.4.2, lines 53-263)

# Relationships

## Builds Upon
- **weakmap-data-structure** -- a fundamental property of WeakMaps

## Enables
- Private data patterns for objects

## Related
- **weakset-data-structure** -- also a black box

## Contrasts With
- None

# Common Errors

- **Error**: Expecting to `.clear()` a WeakMap.
  **Correction**: Create a new WeakMap instance instead.

# Common Confusions

- **Confusion**: WeakMap's restrictions are a limitation.
  **Clarification**: The restrictions are intentional security features that prevent unauthorized access to stored data.

# Source Reference

Chapter 37: WeakMaps (WeakMap) (advanced), Section 37.2, lines 53-68.

# Verification Notes

- Definition source: direct (includes Mark Miller quote)
- Confidence rationale: Explicitly defined with security rationale
- Cross-reference status: verified
