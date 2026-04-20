---
# === CORE IDENTIFICATION ===
concept: Writable Attribute
slug: writable-attribute

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - data-property
extends: []
related:
  - value-attribute
  - configurable-attribute
contrasts_with:
  - configurable-attribute

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes the configurable attribute from the writable attribute?"
  - "How do property attributes relate to Object.freeze()?"
---

# Quick Definition

The `writable` attribute is a boolean that determines whether the `value` of a data property can be changed via assignment. Its default is `false`.

# Core Definition

As described in "Deep JavaScript" Ch 10, "`writable` determines if the value of a data property can be changed." It is a boolean attribute with a default value of `false`, specific to data properties. Notably, even when `configurable` is `false`, `writable` can be changed from `true` to `false` (but not back). The book explains this historical anomaly: "Property `.length` of Arrays has always been writable and non-configurable. Allowing its `writable` attribute to be changed enables us to freeze Arrays."

# Prerequisites

- **Data Property** — `writable` is an attribute specific to data properties

# Key Properties

1. Type: `boolean`
2. Default: `false`
3. Exclusive to data properties
4. When `false`, assignment to the property throws in strict mode
5. Can be changed from `true` to `false` even on non-configurable properties (special exception)
6. Cannot be changed from `false` to `true` on non-configurable properties
7. Inherited non-writable properties prevent creating own properties via assignment

# Construction / Recognition

## To Construct/Create:
1. Assignment creates properties with `writable: true`
2. `Object.defineProperty()` defaults to `writable: false` if omitted

## To Identify/Recognize:
1. Check `Object.getOwnPropertyDescriptor(obj, key).writable`

# Context & Application

The `writable` attribute is central to object immutability. `Object.freeze()` sets `writable` to `false` on all data properties. A critical pitfall is that an inherited non-writable property prevents creating own properties with the same key via assignment (but definition still works).

# Examples

**Example 1** (Ch 10):
```js
const proto = {
  prop: 1,
};
Object.defineProperty(
  proto, 'prop', {writable: false});
const obj = Object.create(proto);
assert.throws(
  () => obj.prop = 2,
  /^TypeError: Cannot assign to read only property 'prop'/);
```

# Relationships

## Builds Upon
- **data-property** — `writable` is an attribute of data properties

## Enables
- **object-freeze** — freezing sets `writable` to `false` on all properties
- **inherited-read-only-prevents-assignment** — non-writable inherited properties block assignment

## Related
- **value-attribute** — `writable` controls whether `value` can change

## Contrasts With
- **configurable-attribute** — `configurable` controls whether attributes themselves can be changed; `writable` only controls whether the value can be changed via assignment

# Common Errors

- **Error**: Expecting `Object.defineProperty(obj, 'prop', { value: 'x' })` to create a writable property.
  **Correction**: Omitting `writable` when creating a property defaults to `false`. You must explicitly set `writable: true`.

# Common Confusions

- **Confusion**: Thinking `writable: false` is the same as `configurable: false`.
  **Clarification**: `writable` only prevents changing the value via assignment. `configurable` prevents changing any attribute (except the special case of changing `writable` from `true` to `false`).

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.1.3, lines 157, 166, 173-179.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with detailed explanation of the historical exception.
- Cross-reference status: verified against Ch 10, 11, and 12
