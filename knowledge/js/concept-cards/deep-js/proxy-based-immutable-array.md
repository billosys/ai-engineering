---
# === CORE IDENTIFICATION ===
concept: Proxy-Based Immutable Array
slug: proxy-based-immutable-array

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
section: "16.3 An immutable wrapper for Arrays"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - immutable array wrapper
  - read-only array proxy

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
  - javascript-proxies
  - immutable-wrapper
extends:
  - immutable-wrapper
related:
  - immutable-map-wrapper
  - wrapper-pattern
contrasts_with:
  - immutable-map-wrapper

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I make a mutable collection immutable without copying it?"
---

# Quick Definition

A proxy-based immutable Array uses a JavaScript Proxy to intercept property access, method calls, and assignments on an Array, allowing only non-destructive operations and blocking all mutations.

# Core Definition

As explained in "Deep JavaScript" (Ch 16, Section 16.3): "For an Array `arr`, normal wrapping is not enough because we need to intercept not just method calls, but also property accesses such as `arr[1] = true`. JavaScript proxies enable us to do this." The Proxy handler intercepts `get` (allowing index access and whitelisted properties), `set` (always throws), and `deleteProperty` (always throws).

# Prerequisites

- **JavaScript classes** — Understanding of objects and methods.
- **JavaScript Proxies** — The `Proxy` constructor and handler traps (`get`, `set`, `deleteProperty`).
- **Immutable wrapper** — The general concept this implements.

# Key Properties

1. Uses a **Proxy** instead of a wrapper class — necessary because Arrays use property access (`arr[i]`).
2. The `get` trap **whitelists** allowed properties: numeric indices, `length`, `constructor`, `slice`, `concat`.
3. The `set` trap **always throws** — no property assignment allowed.
4. The `deleteProperty` trap **always throws** — no deletion allowed.
5. Destructive methods like `shift()`, `push()`, `splice()` are blocked by the `get` trap.

# Construction / Recognition

## To Construct/Create:
1. Define a Proxy handler with `get`, `set`, and `deleteProperty` traps.
2. In `get`: check if the property key is a numeric index or in the allowed list.
3. In `set` and `deleteProperty`: throw TypeError.
4. Return `new Proxy(arr, handler)`.

## To Identify/Recognize:
1. A Proxy wrapping an Array.
2. Property assignment throws TypeError.
3. Destructive method access throws TypeError.

# Context & Application

Arrays need Proxies rather than simple wrappers because their primary interface is property-based (`arr[i]`), not method-based. This approach intercepts all operations at the meta-object level, providing comprehensive protection against mutation.

# Examples

**Example 1** (Ch 16): Proxy-based immutable Array:
```js
const RE_INDEX_PROP_KEY = /^[0-9]+$/;
const ALLOWED_PROPERTIES = new Set([
  'length', 'constructor', 'slice', 'concat']);

function wrapArrayImmutably(arr) {
  const handler = {
    get(target, propKey, receiver) {
      if (RE_INDEX_PROP_KEY.test(propKey)
        || ALLOWED_PROPERTIES.has(propKey)) {
          return Reflect.get(target, propKey, receiver);
      }
      throw new TypeError(`Property "${propKey}" can't be accessed`);
    },
    set(target, propKey, value, receiver) {
      throw new TypeError('Setting is not allowed');
    },
    deleteProperty(target, propKey) {
      throw new TypeError('Deleting is not allowed');
    },
  };
  return new Proxy(arr, handler);
}

const arr = ['a', 'b', 'c'];
const wrapped = wrapArrayImmutably(arr);

assert.deepEqual(wrapped.slice(1), ['b', 'c']);
assert.equal(wrapped[1], 'b');

assert.throws(
  () => wrapped[1] = 'x',
  /^TypeError: Setting is not allowed$/);
assert.throws(
  () => wrapped.shift(),
  /^TypeError: Property "shift" can't be accessed$/);
```

# Relationships

## Builds Upon
- **JavaScript Proxies** — The meta-programming feature that intercepts property operations.
- **Reflect API** — Used for default property access (`Reflect.get`).
- **Immutable wrapper** — The general concept.

## Enables
- **Safe Array export** — Share internal Arrays without risk of mutation through any access pattern.

## Related
- **Immutable Map wrapper** — The Map equivalent using class-based wrapping.

## Contrasts With
- **Immutable Map wrapper** — Maps only need method forwarding; Arrays need Proxy interception for property access.
- **Object.freeze()** — Freezes the Array itself; the Proxy approach preserves internal mutability.

# Common Errors

- **Error**: Forgetting to handle Symbol property keys in the get trap.
  **Correction**: The source notes "We assume that propKey is a string (not a symbol)" — a production implementation should handle Symbols.

# Common Confusions

- **Confusion**: Thinking `Object.freeze()` is equivalent.
  **Clarification**: `Object.freeze()` makes the Array itself immutable. A Proxy wrapper leaves the original mutable (for the owner) while presenting an immutable view to consumers.

# Source Reference

Chapter 16: Immutable wrappers for collections, Section 16.3, lines 7743-7798.

# Verification Notes

- Definition source: direct (complete implementation from source)
- Confidence rationale: Full code example with comprehensive handler implementation
- Cross-reference status: verified against Chapter 20 (Proxies)
