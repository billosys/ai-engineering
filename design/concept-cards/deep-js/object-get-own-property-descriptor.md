---
# === CORE IDENTIFICATION ===
concept: Object.getOwnPropertyDescriptor()
slug: object-get-own-property-descriptor

# === CLASSIFICATION ===
category: object-model
subcategory: property-descriptors
tier: foundational

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Property attributes: an introduction"
chapter_number: 10
section: "10.3.1 Object.getOwnPropertyDescriptor()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-descriptor
extends: []
related:
  - object-get-own-property-descriptors
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a property descriptor?"
  - "How do I define a property with specific attributes using Object.defineProperty()?"
---

# Quick Definition

`Object.getOwnPropertyDescriptor(obj, key)` returns the property descriptor for a single own (non-inherited) property of `obj`, or `undefined` if no such property exists.

# Core Definition

As described in "Deep JavaScript" Ch 10, `Object.getOwnPropertyDescriptor()` has the signature `(obj: object, key: string|symbol): undefined|PropertyDescriptor`. It "returns the descriptor of the own (non-inherited) property of `obj` whose key is `key`. If there is no such property, `undefined` is returned."

# Prerequisites

- **Property Descriptor** — this method returns property descriptors

# Key Properties

1. Only returns descriptors for own properties (not inherited)
2. Returns `undefined` if the property does not exist
3. Works with both string and symbol keys
4. Returns a data property descriptor or accessor property descriptor
5. Introduced in ES5

# Construction / Recognition

## To Construct/Create:
1. Call: `Object.getOwnPropertyDescriptor(obj, 'propName')`
2. Common shorthand: `const desc = Object.getOwnPropertyDescriptor.bind(Object);`

## To Identify/Recognize:
1. Used to inspect property attributes at runtime

# Context & Application

This method is essential for introspecting property attributes. It is commonly used to check whether a property is writable, configurable, or enumerable, and to determine whether a property is a data property or accessor property.

# Examples

**Example 1** (Ch 10):
```js
assert.deepEqual(
  Object.getOwnPropertyDescriptor(Object.prototype, 'toString'),
  {
    value: {}.toString,
    writable: true,
    enumerable: false,
    configurable: true,
  });
assert.equal(
  Object.getOwnPropertyDescriptor({}, 'toString'),
  undefined);
```

# Relationships

## Builds Upon
- **property-descriptor** — returns a property descriptor object

## Enables
- Inspection of property attributes at runtime

## Related
- **object-get-own-property-descriptors** — the batch version for all own properties

## Contrasts With
- None

# Common Errors

- **Error**: Expecting this method to return descriptors for inherited properties.
  **Correction**: It only returns descriptors for own properties. For inherited `toString`, calling on `{}` returns `undefined`; calling on `Object.prototype` returns the descriptor.

# Common Confusions

- **Confusion**: Thinking the returned descriptor is "live" (connected to the property).
  **Clarification**: The returned descriptor is a plain object snapshot. Modifying it does not affect the property.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.3.1, lines 246-291. Section 10.9, lines 884-903.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with API signature and examples.
- Cross-reference status: verified
