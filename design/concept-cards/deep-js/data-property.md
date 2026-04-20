---
# === CORE IDENTIFICATION ===
concept: Data Property
slug: data-property

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
  - property-attributes
extends: []
related:
  - value-attribute
  - writable-attribute
  - data-property-descriptor
contrasts_with:
  - accessor-property

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a data property vs. an accessor property?"
  - "What distinguishes a data property descriptor from an accessor property descriptor?"
---

# Quick Definition

A data property stores data directly. Its attributes are `value` (holds any JavaScript value), `writable` (whether the value can be changed), plus the shared `configurable` and `enumerable` attributes.

# Core Definition

As described in "Deep JavaScript" Ch 10, "A *data property* stores data. Its attribute `value` holds any JavaScript value." Data properties also have a `writable` attribute that "determines if the value of a data property can be changed." Data properties are the most common kind of property in JavaScript — all properties created via assignment or object literals are data properties.

# Prerequisites

- **Property Attributes** — data properties are defined by their specific set of attributes

# Key Properties

1. Has `value` attribute (type: `any`, default: `undefined`)
2. Has `writable` attribute (type: `boolean`, default: `false`)
3. Has shared `configurable` and `enumerable` attributes
4. Cannot have `get` or `set` attributes (mutually exclusive with accessor property)
5. Most common kind of property in JavaScript

# Construction / Recognition

## To Construct/Create:
1. Assignment: `obj.prop = value` (creates with writable/enumerable/configurable all `true`)
2. Object literal: `{ prop: value }` (same attributes as assignment)
3. `Object.defineProperty(obj, 'prop', { value: v })` (omitted boolean attributes default to `false`)

## To Identify/Recognize:
1. Inspect with `Object.getOwnPropertyDescriptor()` — if result has `value` property, it is a data property
2. A descriptor with `get` or `set` indicates an accessor property instead

# Context & Application

Data properties are the standard way to store values on objects. When a property is created via the `=` operator or within an object literal, it is always a data property with `writable: true`, `enumerable: true`, `configurable: true`.

# Examples

**Example 1** (Ch 10):
```js
const legoBrick = {
  kind: 'Plate 1x3',
  color: 'yellow',
};
assert.deepEqual(
  Object.getOwnPropertyDescriptor(legoBrick, 'color'),
  {
    value: 'yellow',
    writable: true,
    enumerable: true,
    configurable: true,
  });
```

# Relationships

## Builds Upon
- **property-attributes** — data properties are characterized by the `value` and `writable` attributes

## Enables
- **data-property-descriptor** — the descriptor type for data properties
- **property-assignment** — assignment creates or changes data properties

## Related
- **value-attribute** — the attribute that stores the data
- **writable-attribute** — controls mutability of the value

## Contrasts With
- **accessor-property** — uses `get`/`set` functions instead of storing a value directly

# Common Errors

- **Error**: Trying to add both `value` and `get`/`set` in a single descriptor.
  **Correction**: A property is either a data property (with `value`/`writable`) or an accessor property (with `get`/`set`). These are mutually exclusive.

# Common Confusions

- **Confusion**: Thinking `Object.defineProperty()` with only `{ value: 'x' }` creates a normal writable property.
  **Clarification**: Omitted boolean attributes default to `false` when creating, so the property will be non-writable, non-enumerable, and non-configurable.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.1.3, lines 145-146, 154-157.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined in the property attributes table.
- Cross-reference status: verified
