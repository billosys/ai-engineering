---
# === CORE IDENTIFICATION ===
concept: Data Property Descriptor
slug: data-property-descriptor

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
section: "10.2 Property descriptors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-descriptor
  - data-property
extends:
  - property-descriptor
related: []
contrasts_with:
  - accessor-property-descriptor

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a data property descriptor from an accessor property descriptor?"
  - "What is a property descriptor?"
---

# Quick Definition

A data property descriptor is a property descriptor that encodes the attributes of a data property: `value`, `writable`, `configurable`, and `enumerable`. All fields are optional.

# Core Definition

As described in "Deep JavaScript" Ch 10, the TypeScript interface for a data property descriptor is:

```ts
interface DataPropertyDescriptor {
  value?: any;
  writable?: boolean;
  configurable?: boolean;
  enumerable?: boolean;
}
```

A data property descriptor contains `value` and/or `writable` but never `get` or `set`.

# Prerequisites

- **Property Descriptor** — this is a specific kind of property descriptor
- **Data Property** — this descriptor type corresponds to data properties

# Key Properties

1. Contains `value` (any type) and/or `writable` (boolean)
2. May also contain `configurable` and `enumerable`
3. Cannot contain `get` or `set`
4. All fields are optional

# Construction / Recognition

## To Construct/Create:
1. `{ value: 42, writable: true, enumerable: true, configurable: true }`
2. Minimal: `{ value: 42 }` (other attributes default to `false`)

## To Identify/Recognize:
1. Has `value` or `writable` property
2. Does not have `get` or `set` property

# Context & Application

Data property descriptors are used with `Object.defineProperty()` to create or modify data properties. They are returned by `Object.getOwnPropertyDescriptor()` for data properties.

# Examples

**Example 1** (Ch 10):
```js
Object.defineProperty(car, 'color', {
  value: 'blue',
  writable: true,
  enumerable: true,
  configurable: true,
});
```

# Relationships

## Builds Upon
- **property-descriptor** — data property descriptor is a subtype
- **data-property** — describes the attributes of data properties

## Enables
- **object-define-property** — accepts data property descriptors

## Related
- None

## Contrasts With
- **accessor-property-descriptor** — uses `get`/`set` instead of `value`/`writable`

# Common Errors

- **Error**: Including both `value` and `get` in a single descriptor.
  **Correction**: This creates an invalid descriptor that will throw a TypeError.

# Common Confusions

- **Confusion**: Thinking a descriptor with only `{ enumerable: true }` is a data property descriptor.
  **Clarification**: A descriptor with only shared attributes (no `value`/`writable`/`get`/`set`) is a "generic" descriptor, which is valid for both property kinds.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.2, lines 221-227.

# Verification Notes

- Definition source: direct (TypeScript interface from source)
- Confidence rationale: Explicitly defined with interface.
- Cross-reference status: verified
