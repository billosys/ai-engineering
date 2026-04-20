---
# === CORE IDENTIFICATION ===
concept: Shallow Freezing
slug: shallow-freezing

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
section: "11.4.2 Freezing is shallow"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "shallow freeze"
  - "freezing is shallow"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object-freeze
extends: []
related:
  - deep-freezing
contrasts_with:
  - deep-freezing

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do property attributes relate to Object.freeze()?"
---

# Quick Definition

`Object.freeze()` only freezes the object itself and its own properties' attributes. It does not freeze the values of those properties — nested objects remain mutable.

# Core Definition

As described in "Deep JavaScript" Ch 11, "`Object.freeze(obj)` only freezes `obj` and its properties. It does not freeze the values of those properties." This means that while you cannot reassign a property on a frozen object, you can still mutate the object that a property points to.

# Prerequisites

- **Object.freeze()** — need to understand what freeze does before understanding its limitation

# Key Properties

1. Only the top-level object's properties become read-only
2. Nested objects (values of properties) remain fully mutable
3. Arrays inside frozen objects can still be modified (push, pop, etc.)
4. This is a fundamental limitation of `Object.freeze()`

# Construction / Recognition

## To Construct/Create:
1. `Object.freeze(obj)` — always produces a shallow freeze

## To Identify/Recognize:
1. After freezing, attempt to mutate a nested object — if it succeeds, the freeze is shallow

# Context & Application

Shallow freezing is the default and only behavior of `Object.freeze()`. To achieve deep immutability, a custom deep-freeze function is needed.

# Examples

**Example 1** (Ch 11):
```js
const teacher = {
  name: 'Edna Krabappel',
  students: ['Bart'],
};
Object.freeze(teacher);
// Can't change own properties:
assert.throws(
  () => teacher.name = 'Elizabeth Hoover',
  /^TypeError: Cannot assign to read only property 'name'/);
// But CAN change values of own properties:
teacher.students.push('Lisa');
assert.deepEqual(
  teacher, {
    name: 'Edna Krabappel',
    students: ['Bart', 'Lisa'],
  });
```

# Relationships

## Builds Upon
- **object-freeze** — this is a property/limitation of freeze

## Enables
- Understanding the need for **deep-freezing**

## Related
- None

## Contrasts With
- **deep-freezing** — deep freezing recursively freezes nested objects

# Common Errors

- **Error**: Relying on `Object.freeze()` for deep immutability.
  **Correction**: `Object.freeze()` is shallow. Use a deep-freeze function for nested objects.

# Common Confusions

- **Confusion**: Thinking `Object.freeze()` makes the entire object graph immutable.
  **Clarification**: Only the frozen object's own property assignments are blocked. Nested objects are untouched.

# Source Reference

Chapter 11: Protecting objects from being changed, Section 11.4.2, lines 272-298.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly explained with a clear example demonstrating the limitation.
- Cross-reference status: verified
