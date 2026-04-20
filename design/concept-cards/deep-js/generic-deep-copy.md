---
# === CORE IDENTIFICATION ===
concept: Generic Deep Copy Implementation
slug: generic-deep-copy

# === CLASSIFICATION ===
category: data-management
subcategory: copying
tier: foundational

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Copying objects and Arrays"
chapter_number: 7
section: "Implementing generic deep copying"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "recursive deep copy"
  - "deepCopy() function"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deep-copy
  - shallow-copy
extends:
  - deep-copy
related:
  - json-deep-copy
  - nested-spreading-deep-copy
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a deep copy of an object?"
  - "What distinguishes shallow copying from deep copying?"
---

# Quick Definition

A recursive function that traverses an object tree, creating new copies of Arrays and objects at every level while leaving primitive values unchanged.

# Core Definition

As described in "Deep JavaScript" Ch 7, Section 7.3.3, a generic deep copy function handles three cases: if the value is an Array, it creates a new Array and deep-copies each element; if it is an object, it creates a new object and deep-copies each entry; if it is a primitive, it returns the value directly (primitives are atomic). The author notes this "only fixes one issue of spreading: shallow copying. All others remain: prototypes are not copied, special objects are only partially copied, non-enumerable properties are ignored, most property attributes are ignored."

# Prerequisites

- **Deep copy** -- understanding the goal of full tree duplication
- **Shallow copy** -- understanding why shallow copy is insufficient for nested data
- **Recursion** -- the function calls itself for each nested level

# Key Properties

1. Recursively copies Arrays, objects, and primitives.
2. Handles three cases: Array, object, primitive.
3. Does NOT copy prototypes, special objects, non-enumerable properties, or property attributes.
4. "Implementing copying completely generically is generally impossible."
5. Can be written concisely using `.map()` and `Object.fromEntries()`.

# Construction / Recognition

## To Construct/Create:
1. Full version:
```js
function deepCopy(original) {
  if (Array.isArray(original)) {
    const copy = [];
    for (const [index, value] of original.entries()) {
      copy[index] = deepCopy(value);
    }
    return copy;
  } else if (typeof original === 'object' && original !== null) {
    const copy = {};
    for (const [key, value] of Object.entries(original)) {
      copy[key] = deepCopy(value);
    }
    return copy;
  } else {
    return original;
  }
}
```

2. Concise version:
```js
function deepCopy(original) {
  if (Array.isArray(original)) {
    return original.map(elem => deepCopy(elem));
  } else if (typeof original === 'object' && original !== null) {
    return Object.fromEntries(
      Object.entries(original).map(([k, v]) => [k, deepCopy(v)]));
  } else {
    return original;
  }
}
```

## To Identify/Recognize:
1. A recursive function that branches on `Array.isArray()` and `typeof === 'object'`.

# Context & Application

Use when you need deep copying of plain objects and arrays without external libraries. Understand that this is a basic implementation; production code may need to handle circular references, special objects, and prototype chains.

# Examples

**Example 1** (Ch 7): Verifying all levels are independent copies:
```js
const original = {a: 1, b: {c: 2, d: {e: 3}}};
const copy = deepCopy(original);

assert.deepEqual(copy, original);
assert.ok(copy     !== original);
assert.ok(copy.b   !== original.b);
assert.ok(copy.b.d !== original.b.d);
```

# Relationships

## Builds Upon
- **Deep copy** -- this is a concrete implementation of the deep copy concept

## Enables
- **Custom deep copy solutions** -- can be extended for specific object types

## Related
- **JSON deep copy** -- an alternative approach with different tradeoffs
- **Nested spreading deep copy** -- a manual approach for known structures

## Contrasts With
(none at this specificity)

# Common Errors

- **Error**: Not checking for `null` when testing `typeof === 'object'` (since `typeof null === 'object'`).
  **Correction**: Always include `&& original !== null` in the object check.

# Common Confusions

- **Confusion**: This generic deep copy handles all JavaScript values.
  **Clarification**: The author explicitly states it does not handle prototypes, special objects, non-enumerable properties, or property attributes. "Implementing copying completely generically is generally impossible."

# Source Reference

Chapter 7: "Copying objects and Arrays", Section 7.3.3, lines 3425-3505.

# Verification Notes

- Definition source: direct
- Confidence rationale: Complete implementation with test assertions and explicit limitations documented in source.
- Cross-reference status: verified against Ch 7 section 7.3.3
