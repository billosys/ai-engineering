---
# === CORE IDENTIFICATION ===
concept: Object.getOwnPropertyDescriptors()
slug: object-get-own-property-descriptors

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
section: "10.3.2 Object.getOwnPropertyDescriptors()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-descriptor
  - object-get-own-property-descriptor
extends: []
related:
  - object-define-properties
  - object-create
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a property descriptor?"
---

# Quick Definition

`Object.getOwnPropertyDescriptors(obj)` returns an object mapping each own property key of `obj` to its property descriptor. The result can be used as input for `Object.defineProperties()` and `Object.create()`.

# Core Definition

As described in "Deep JavaScript" Ch 10, `Object.getOwnPropertyDescriptors()` has the signature `(obj: object): {[k: string|symbol]: PropertyDescriptor}`. It "returns an object where each property key `'k'` of `obj` is mapped to the property descriptor for `obj.k`." Introduced in ES2017.

# Prerequisites

- **Property Descriptor** — returns property descriptors
- **Object.getOwnPropertyDescriptor()** — this is the batch version

# Key Properties

1. Returns descriptors for ALL own properties (both enumerable and non-enumerable)
2. Includes both string-keyed and symbol-keyed properties
3. Result can be passed directly to `Object.defineProperties()` or `Object.create()`
4. Introduced in ES2017

# Construction / Recognition

## To Construct/Create:
1. Call: `Object.getOwnPropertyDescriptors(obj)`

## To Identify/Recognize:
1. Returns an object of descriptors, not a single descriptor

# Context & Application

This method is crucial for faithfully copying properties (including accessors) between objects. `Object.assign()` cannot faithfully copy accessor properties because it reads via getters and writes via assignment. The combination of `Object.getOwnPropertyDescriptors()` with `Object.defineProperties()` or `Object.create()` preserves the full property descriptor.

# Examples

**Example 1** (Ch 10): Faithful property copying:
```js
const source = {
  set data(value) {
    this._data = value;
  }
};
const target = {};
Object.defineProperties(
  target, Object.getOwnPropertyDescriptors(source));
// target.data is still an accessor property (not converted to data property)
```

**Example 2** (Ch 10): Cloning objects:
```js
const clone = Object.create(
  Object.getPrototypeOf(original),
  Object.getOwnPropertyDescriptors(original));
```

# Relationships

## Builds Upon
- **property-descriptor** — returns a map of property descriptors
- **object-get-own-property-descriptor** — batch version of this single-property method

## Enables
- Faithful property copying (preserving accessors)
- Object cloning with correct prototypes and descriptors

## Related
- **object-define-properties** — accepts the output of this method
- **object-create** — accepts the output as second argument

## Contrasts With
- None

# Common Errors

- **Error**: Using `Object.assign()` instead when accessor properties need to be preserved.
  **Correction**: Use `Object.defineProperties(target, Object.getOwnPropertyDescriptors(source))` for faithful copies.

# Common Confusions

- **Confusion**: Thinking this method includes inherited properties.
  **Clarification**: It only includes own properties, not inherited ones.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.3.2, lines 293-332. Section 10.6, lines 497-615. Section 10.9, lines 905-939.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with API signature, examples, and use cases.
- Cross-reference status: verified
