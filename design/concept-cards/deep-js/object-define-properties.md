---
# === CORE IDENTIFICATION ===
concept: Object.defineProperties()
slug: object-define-properties

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
section: "10.4.2 Object.defineProperties()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-descriptor
  - object-define-property
extends:
  - object-define-property
related:
  - object-get-own-property-descriptors
  - object-create
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a property with specific attributes using Object.defineProperty()?"
---

# Quick Definition

`Object.defineProperties(obj, properties)` is the batch version of `Object.defineProperty()`. It defines multiple properties on `obj` at once, where each key in `properties` maps to a property descriptor.

# Core Definition

As described in "Deep JavaScript" Ch 10, `Object.defineProperties()` has the signature `(obj: object, properties: {[k: string|symbol]: PropertyDescriptor}): object`. "Each property `p` of the object `properties` specifies one property that is to be added to `obj`: The key of `p` specifies the key of the property, the value of `p` is a descriptor that specifies the attributes of the property."

# Prerequisites

- **Property Descriptor** — each entry in the properties object is a descriptor
- **Object.defineProperty()** — this is the batch version

# Key Properties

1. Defines multiple properties at once
2. Returns the modified object
3. Accepts the output of `Object.getOwnPropertyDescriptors()` directly
4. Same creation/change semantics as `Object.defineProperty()`
5. Introduced in ES5

# Construction / Recognition

## To Construct/Create:
1. `Object.defineProperties(obj, { prop1: { value: 1 }, prop2: { value: 2 } })`
2. Faithful copy: `Object.defineProperties(target, Object.getOwnPropertyDescriptors(source))`

## To Identify/Recognize:
1. Takes two arguments: an object and an object of descriptors

# Context & Application

Combined with `Object.getOwnPropertyDescriptors()`, this method enables faithful property copying that preserves accessor properties (unlike `Object.assign()`).

# Examples

**Example 1** (Ch 10):
```js
const address = Object.defineProperties({}, {
  street: { value: 'Evergreen Terrace', enumerable: true },
  number: { value: 742, enumerable: true },
});
```

# Relationships

## Builds Upon
- **object-define-property** — batch version of this method

## Enables
- Faithful property copying when combined with `Object.getOwnPropertyDescriptors()`

## Related
- **object-get-own-property-descriptors** — output feeds directly into this method
- **object-create** — similar batch definition via second argument

## Contrasts With
- None

# Common Errors

- **Error**: Forgetting that omitted attributes default to `false` for new properties.
  **Correction**: Same as `Object.defineProperty()` — explicitly specify desired attributes.

# Common Confusions

- **Confusion**: Thinking `Object.defineProperties()` works like `Object.assign()`.
  **Clarification**: `Object.assign()` uses get/set (invokes getters, uses assignment). `Object.defineProperties()` uses definition semantics (ignores setters, preserves descriptors).

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.4.2, lines 414-456. Section 10.9, lines 852-865.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with API signature.
- Cross-reference status: verified
