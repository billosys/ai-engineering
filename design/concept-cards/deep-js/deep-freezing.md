---
# === CORE IDENTIFICATION ===
concept: Deep Freezing
slug: deep-freezing

# === CLASSIFICATION ===
category: object-protection
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Protecting objects from being changed"
chapter_number: 11
section: "11.4.3 Implementing deep freezing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "deep freeze"
  - "recursive freezing"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object-freeze
  - shallow-freezing
extends:
  - object-freeze
related: []
contrasts_with:
  - shallow-freezing

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do property attributes relate to Object.freeze()?"
---

# Quick Definition

Deep freezing is a pattern where `Object.freeze()` is applied recursively to an object and all objects reachable through its properties, making the entire object graph immutable.

# Core Definition

As described in "Deep JavaScript" Ch 11, "If we want deep freezing, we need to implement it ourselves." The book provides a reference implementation that recursively freezes arrays, objects, and leaves primitive values unchanged (since they are already immutable).

# Prerequisites

- **Object.freeze()** — deep freezing builds on the standard freeze
- **Shallow Freezing** — need to understand the limitation that deep freezing addresses

# Key Properties

1. Not built into JavaScript — must be implemented manually
2. Recursively visits all property values
3. Freezes arrays and objects encountered during traversal
4. Primitive values are skipped (already immutable)
5. Must handle both arrays and plain objects

# Construction / Recognition

## To Construct/Create:
1. Implement a recursive function that freezes objects and their property values

## To Identify/Recognize:
1. After deep freezing, no nested object can be mutated

# Context & Application

Deep freezing is used when full immutability of an object graph is required. It is commonly needed for configuration objects, constant data structures, and shared state in concurrent-style programming.

# Examples

**Example 1** (Ch 11): Implementation:
```js
function deepFreeze(value) {
  if (Array.isArray(value)) {
    for (const element of value) {
      deepFreeze(element);
    }
    Object.freeze(value);
  } else if (typeof value === 'object' && value !== null) {
    for (const v of Object.values(value)) {
      deepFreeze(v);
    }
    Object.freeze(value);
  } else {
    // Nothing to do: primitive values are already immutable
  }
  return value;
}
```

**Example 2** (Ch 11): Usage:
```js
const teacher = {
  name: 'Edna Krabappel',
  students: ['Bart'],
};
deepFreeze(teacher);
assert.throws(
  () => teacher.students.push('Lisa'),
  /^TypeError: Cannot add property 1, object is not extensible$/);
```

# Relationships

## Builds Upon
- **object-freeze** — uses `Object.freeze()` at each level
- **shallow-freezing** — addresses the limitation of shallow freezing

## Enables
- Full object-graph immutability

## Related
- None

## Contrasts With
- **shallow-freezing** — shallow only freezes the top-level object

# Common Errors

- **Error**: Not handling circular references in a deep-freeze implementation.
  **Correction**: The simple implementation shown can cause infinite recursion with circular references. Production implementations should track visited objects.

# Common Confusions

- **Confusion**: Thinking JavaScript has a built-in `Object.deepFreeze()`.
  **Clarification**: There is no built-in deep-freeze method. It must be implemented manually.

# Source Reference

Chapter 11: Protecting objects from being changed, Section 11.4.3, lines 300-338.

# Verification Notes

- Definition source: direct (implementation from source)
- Confidence rationale: Complete implementation provided in the source text.
- Cross-reference status: verified
