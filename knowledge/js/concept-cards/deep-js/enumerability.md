---
# === CORE IDENTIFICATION ===
concept: Enumerability
slug: enumerability

# === CLASSIFICATION ===
category: object-model
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Enumerability of properties"
chapter_number: 13
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "enumerable property"
  - "non-enumerable property"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - enumerable-attribute
  - property-attributes
extends: []
related:
  - for-in-loop
  - object-keys
  - object-assign-enumerability
  - reflect-own-keys
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is enumerability?"
  - "What must I understand before learning about enumerability?"
---

# Quick Definition

Enumerability is a property attribute that controls whether certain operations (like `Object.keys()`, `for-in`, `Object.assign()`, `JSON.stringify()`) include a property in their results. Most own properties are enumerable; most inherited prototype properties are non-enumerable.

# Core Definition

As described in "Deep JavaScript" Ch 13, "Enumerability is an *attribute* of object properties." It was introduced in ECMAScript 1 to hide prototype properties from `for-in` loops. The book concludes that "almost all applications for non-enumerability are work-arounds that now have other and better solutions" and that "for our own code, we can usually pretend that enumerability doesn't exist" because the defaults work correctly: "Creating properties via object literals and assignment always creates enumerable properties. Prototype properties created via classes are always non-enumerable."

# Prerequisites

- **Enumerable Attribute** — the attribute that controls enumerability
- **Property Attributes** — enumerability is one of the shared property attributes

# Key Properties

1. Introduced in ECMAScript 1 to hide prototype properties from `for-in`
2. Operations that respect enumerability: `Object.keys()`, `Object.values()`, `Object.entries()`, `Object.assign()`, spreading, `JSON.stringify()`, `for-in`
3. Operations that ignore enumerability: `Object.getOwnPropertyNames()`, `Object.getOwnPropertySymbols()`, `Reflect.ownKeys()`, `Object.getOwnPropertyDescriptors()`
4. Default behavior works well: own properties enumerable, prototype methods non-enumerable
5. `for-in` is the only operation where enumerability of INHERITED properties matters
6. Considered an inconsistent feature with limited modern use cases

# Construction / Recognition

## To Construct/Create:
1. Enumerable: `obj.prop = value` or `{ prop: value }`
2. Non-enumerable: `Object.defineProperty(obj, 'prop', { value: v })` (default)

## To Identify/Recognize:
1. Check `Object.getOwnPropertyDescriptor(obj, 'prop').enumerable`

# Context & Application

Enumerability is the gating mechanism for many property-listing operations. While it has historical significance, modern best practices make it largely invisible — own properties are enumerable by default, prototype methods are non-enumerable by default.

# Examples

**Example 1** (Ch 13): Only enumerable properties appear in `Object.keys()`:
```js
const obj = Object.create(Object.prototype, {
  enumProp: { value: 1, enumerable: true },
  nonEnumProp: { value: 2, enumerable: false },
});
assert.deepEqual(Object.keys(obj), ['enumProp']); // only enumerable
```

# Relationships

## Builds Upon
- **enumerable-attribute** — the underlying attribute
- **property-attributes** — part of the attribute system

## Enables
- Understanding which operations include which properties
- Understanding why prototype methods are hidden from `Object.keys()`

## Related
- **for-in-loop** — the original motivation for enumerability
- **object-keys** — respects enumerability
- **reflect-own-keys** — ignores enumerability

## Contrasts With
- None

# Common Errors

- **Error**: Making properties non-enumerable as a privacy mechanism.
  **Correction**: Non-enumerable properties are still accessible. Enumerability is not security. Use private class fields for true privacy.

# Common Confusions

- **Confusion**: Thinking enumerability affects property access (get/set).
  **Clarification**: Enumerability only affects listing/iteration operations. You can always get and set non-enumerable properties.

# Source Reference

Chapter 13: Enumerability of properties, full chapter, lines 1-720.

# Verification Notes

- Definition source: direct
- Confidence rationale: The entire chapter is dedicated to this topic.
- Cross-reference status: verified
