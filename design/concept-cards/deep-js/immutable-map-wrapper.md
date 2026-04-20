---
# === CORE IDENTIFICATION ===
concept: Immutable Map Wrapper
slug: immutable-map-wrapper

# === CLASSIFICATION ===
category: class-patterns
subcategory: wrapping
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Immutable wrappers for collections"
chapter_number: 16
section: "16.2 An immutable wrapper for Maps"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - ImmutableMapWrapper
  - ReadOnlyMap

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
  - javascript-maps
  - immutable-wrapper
  - wrapper-pattern
extends:
  - immutable-wrapper
related:
  - proxy-based-immutable-array
  - delegation-via-forwarding
contrasts_with:
  - proxy-based-immutable-array

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I make a mutable collection immutable without copying it?"
---

# Quick Definition

The `ImmutableMapWrapper` class wraps a `Map` and only forwards non-destructive methods (`get`, `has`, `keys`, `size`), making the wrapped Map read-only through the wrapper interface.

# Core Definition

As implemented in "Deep JavaScript" (Ch 16, Section 16.2): The `ImmutableMapWrapper` class stores the original Map in a private field `#wrappedMap`. Non-destructive methods are set up on the prototype via a static `_setUpPrototype()` method that iterates over allowed method names and creates forwarding functions. "The setup of the prototype has to be performed by a static method, because we only have access to the private field `.#wrappedMap` from inside the class."

# Prerequisites

- **JavaScript classes** — Static methods and private fields.
- **JavaScript Maps** — The `Map` API (get, has, set, keys, etc.).
- **Immutable wrapper** — The general concept.
- **Wrapper pattern** — The underlying technique.

# Key Properties

1. Only forwards: `get`, `has`, `keys`, `size`.
2. Blocks: `set`, `delete`, `clear` (they simply don't exist on the wrapper).
3. Prototype setup uses a **static method** for private field access.
4. Calling a blocked method throws **TypeError** (not a function).
5. Works **shallowly** — values returned by `get` are not themselves wrapped.

# Construction / Recognition

## To Construct/Create:
1. Define a class with a `#wrappedMap` private field.
2. Use a static `_setUpPrototype()` method to create forwarding methods for allowed operations.
3. Call `_setUpPrototype()` after the class definition.

## To Identify/Recognize:
1. A class wrapping a Map with selective method forwarding.
2. Destructive operations throw TypeError when called.

# Context & Application

This is the Map-specific implementation of the immutable wrapper pattern. It is useful when an object owns a Map internally and wants to expose a read-only view without copying the data.

# Examples

**Example 1** (Ch 16): ImmutableMapWrapper implementation and usage:
```js
class ImmutableMapWrapper {
  static _setUpPrototype() {
    for (const methodName of ['get', 'has', 'keys', 'size']) {
      ImmutableMapWrapper.prototype[methodName] = function (...args) {
        return this.#wrappedMap[methodName](...args);
      }
    }
  }
  #wrappedMap;
  constructor(wrappedMap) {
    this.#wrappedMap = wrappedMap;
  }
}
ImmutableMapWrapper._setUpPrototype();

const map = new Map([[false, 'no'], [true, 'yes']]);
const wrapped = new ImmutableMapWrapper(map);

assert.equal(wrapped.get(true), 'yes');
assert.equal(wrapped.has(false), true);
assert.deepEqual([...wrapped.keys()], [false, true]);

// Destructive operations are not available:
assert.throws(
  () => wrapped.set(false, 'never!'),
  /^TypeError: wrapped.set is not a function$/);
```

# Relationships

## Builds Upon
- **Immutable wrapper** — This is a concrete implementation for Maps.
- **Private fields** — `#wrappedMap` prevents external access to the mutable Map.

## Enables
- **Safe Map sharing** — Share internal Maps without risk of mutation.

## Related
- **Proxy-based immutable Array** — The Array equivalent using a different approach.

## Contrasts With
- **Proxy-based immutable Array** — Arrays need Proxies for property access interception; Maps only need method forwarding.

# Common Errors

- **Error**: Trying to use `wrapped.size` when `size` is a getter on Map, not a method.
  **Correction**: The implementation forwards `size` as a method call, which may not work correctly since `Map.prototype.size` is a getter. This is one of the limitations the author notes ("More work is needed").

# Common Confusions

- **Confusion**: Thinking the wrapper makes the original Map immutable.
  **Clarification**: The original Map `map` remains fully mutable. Only access through `wrapped` is restricted.

# Source Reference

Chapter 16: Immutable wrappers for collections, Section 16.2, lines 7692-7741.

# Verification Notes

- Definition source: direct (complete implementation from source)
- Confidence rationale: Full code example with usage demonstration
- Cross-reference status: verified against immutable wrapper concept
