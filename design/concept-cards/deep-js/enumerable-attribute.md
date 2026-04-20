---
# === CORE IDENTIFICATION ===
concept: Enumerable Attribute
slug: enumerable-attribute

# === CLASSIFICATION ===
category: object-model
subcategory: property-structure
tier: foundational

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Property attributes: an introduction"
chapter_number: 10
section: "10.1.3 Property attributes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "enumerability"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-attributes
extends: []
related:
  - configurable-attribute
  - for-in-loop
  - object-keys
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is enumerability?"
  - "What must I understand before learning about enumerability?"
---

# Quick Definition

The `enumerable` attribute is a boolean shared by both data and accessor properties. It influences whether certain operations (such as `Object.keys()`, `for-in`, `Object.assign()`) see the property. Its default is `false`.

# Core Definition

As described in "Deep JavaScript" Ch 10, "`enumerable` influences some operations (such as `Object.keys()`). If it is `false`, then those operations ignore the property. Most properties are enumerable (e.g. those created via assignment or object literals), which is why you'll rarely notice this attribute in practice." Ch 13 expands: "Enumerability is an *attribute* of object properties" that was introduced in ECMAScript 1 to hide prototype properties from `for-in` loops.

# Prerequisites

- **Property Attributes** — `enumerable` is one of the shared property attributes

# Key Properties

1. Type: `boolean`
2. Default: `false`
3. Applies to both data and accessor properties
4. Properties created via assignment and object literals are enumerable (`true`)
5. Prototype properties of classes are non-enumerable (`false`)
6. Controls visibility to `Object.keys()`, `Object.assign()`, `for-in`, `JSON.stringify()`, and spreading

# Construction / Recognition

## To Construct/Create:
1. Assignment and object literals create enumerable properties
2. Class prototype methods are non-enumerable
3. `Object.defineProperty()` defaults to `enumerable: false` if omitted

## To Identify/Recognize:
1. Check `Object.getOwnPropertyDescriptor(obj, key).enumerable`

# Context & Application

Enumerability is the gating attribute for many property-listing operations. Its primary historical purpose was hiding inherited properties from `for-in`. In modern code, most own properties are enumerable, and prototype properties are non-enumerable, which matches best practices automatically.

# Examples

**Example 1** (Ch 10): Prototype properties of built-in classes are non-enumerable:
```js
assert.deepEqual(
  Object.getOwnPropertyDescriptor(Array.prototype, 'map'),
  {
    value: Array.prototype.map,
    writable: true,
    enumerable: false,
    configurable: true
  });
```

# Relationships

## Builds Upon
- **property-attributes** — `enumerable` is a shared attribute for all property kinds

## Enables
- **for-in-loop** — `for-in` only traverses enumerable properties
- **object-keys** — only returns enumerable own string keys
- **object-assign-enumerability** — only copies enumerable own properties
- **json-stringify-enumerability** — only serializes enumerable own string-keyed properties

## Related
- **configurable-attribute** — locked by `configurable: false`

## Contrasts With
- None

# Common Errors

- **Error**: Assuming `Object.defineProperty()` creates enumerable properties by default.
  **Correction**: Omitted `enumerable` defaults to `false` when creating a property, making it invisible to `Object.keys()`, `for-in`, etc.

# Common Confusions

- **Confusion**: Thinking enumerability is a reliable way to mark properties as private.
  **Clarification**: Non-enumerable properties are still accessible via get/set operations and visible to `Reflect.ownKeys()` and `Object.getOwnPropertyNames()`. Enumerability is not a security mechanism.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.1.3, lines 161, 180-185. Chapter 13: full chapter.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined in Ch 10 and extensively explored in Ch 13.
- Cross-reference status: verified across Ch 10 and Ch 13
