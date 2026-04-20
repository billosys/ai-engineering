---
# === CORE IDENTIFICATION ===
concept: Value Attribute
slug: value-attribute

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
  - writable-attribute
  - property-descriptor
contrasts_with:
  - get-attribute
  - set-attribute

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a property descriptor?"
  - "What is a data property vs. an accessor property?"
---

# Quick Definition

The `value` attribute of a data property holds any JavaScript value. Its default is `undefined`. It is the attribute that actually stores the data in a data property.

# Core Definition

As described in "Deep JavaScript" Ch 10, a data property's `value` attribute has type `any` and a default value of `undefined`. The book emphasizes that "even the value of a data property is stored in an attribute" — the value is not the property itself but one of its attributes.

# Prerequisites

- **Data Property** — `value` is an attribute specific to data properties

# Key Properties

1. Type: `any` (can hold any JavaScript value)
2. Default: `undefined`
3. Exclusive to data properties (not present on accessor properties)
4. Can be changed via assignment (if `writable` is `true`) or via `Object.defineProperty()`

# Construction / Recognition

## To Construct/Create:
1. Assignment: `obj.prop = 'hello'` sets `value` to `'hello'`
2. Definition: `Object.defineProperty(obj, 'prop', { value: 'hello' })`

## To Identify/Recognize:
1. Present in the descriptor returned by `Object.getOwnPropertyDescriptor()` for data properties

# Context & Application

The `value` attribute is the most commonly interacted-with attribute, as reading and writing properties in normal code accesses this attribute. Even when a property is non-configurable and non-writable is `false`, the value can still be changed via `Object.defineProperty()` if `writable` is `true`.

# Examples

**Example 1** (Ch 10):
```js
const obj = {};
obj.prop = 3;
assert.deepEqual(
  Object.getOwnPropertyDescriptors(obj),
  {
    prop: {
      value: 3,
      writable: true,
      enumerable: true,
      configurable: true,
    }
  });
```

# Relationships

## Builds Upon
- **data-property** — `value` is an attribute of data properties

## Enables
- **property-assignment** — assignment changes the `value` attribute

## Related
- **writable-attribute** — controls whether `value` can be changed via assignment

## Contrasts With
- **get-attribute** — accessor properties use a getter function instead of a stored value
- **set-attribute** — accessor properties use a setter function instead of direct value storage

# Common Errors

- **Error**: Assuming `value` defaults to `null`.
  **Correction**: The default value for the `value` attribute is `undefined`.

# Common Confusions

- **Confusion**: Thinking the `value` attribute and the property are the same thing.
  **Clarification**: The value is just one of several attributes that make up a property. A property also has `writable`, `enumerable`, and `configurable` attributes.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.1.3, lines 145-146, 156.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly listed in the property attributes table.
- Cross-reference status: verified
