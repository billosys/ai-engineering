---
# === CORE IDENTIFICATION ===
concept: Property Descriptor
slug: property-descriptor

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
aliases:
  - "descriptor"
  - "PropDesc"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-attributes
extends: []
related:
  - data-property-descriptor
  - accessor-property-descriptor
  - object-get-own-property-descriptor
  - object-define-property
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a property descriptor?"
  - "How do I define a property with specific attributes using Object.defineProperty()?"
---

# Quick Definition

A property descriptor is a JavaScript object that encodes the attributes of a property. It is the interface used to read, create, and change property attributes via methods like `Object.getOwnPropertyDescriptor()` and `Object.defineProperty()`.

# Core Definition

As described in "Deep JavaScript" Ch 10, "A *property descriptor* encodes the attributes of a property as a JavaScript object." The TypeScript type is defined as:

```ts
type PropertyDescriptor = DataPropertyDescriptor | AccessorPropertyDescriptor;
```

All properties in a descriptor are optional. What happens when properties are omitted depends on whether the operation is creating or changing a property.

# Prerequisites

- **Property Attributes** — descriptors encode the attributes that make up properties

# Key Properties

1. A plain JavaScript object encoding property attributes
2. All fields are optional
3. Either a data property descriptor or an accessor property descriptor (not both)
4. Used as input to `Object.defineProperty()` and `Object.create()`
5. Returned by `Object.getOwnPropertyDescriptor()` and `Object.getOwnPropertyDescriptors()`
6. When creating: omitted boolean attributes default to `false`, value-type attributes to `undefined`
7. When changing: omitted attributes leave existing values unchanged

# Construction / Recognition

## To Construct/Create:
1. Create a plain object with attribute names as keys: `{ value: 42, writable: true, enumerable: true, configurable: true }`
2. Retrieve from an existing property: `Object.getOwnPropertyDescriptor(obj, key)`

## To Identify/Recognize:
1. An object with some combination of `value`, `writable`, `get`, `set`, `enumerable`, `configurable`
2. Returned by descriptor-retrieval methods

# Context & Application

Property descriptors are the JavaScript-facing representation of property attributes (the spec uses Records internally). They are essential for low-level property manipulation — creating properties with specific attributes, changing property kinds (data to accessor), and faithfully copying properties between objects.

# Examples

**Example 1** (Ch 10): TypeScript interfaces for descriptors:
```ts
interface DataPropertyDescriptor {
  value?: any;
  writable?: boolean;
  configurable?: boolean;
  enumerable?: boolean;
}
interface AccessorPropertyDescriptor {
  get?: (this: any) => any;
  set?: (this: any, v: any) => void;
  configurable?: boolean;
  enumerable?: boolean;
}
```

**Example 2** (Ch 10): Retrieving a descriptor:
```js
assert.deepEqual(
  Object.getOwnPropertyDescriptor({color: 'yellow'}, 'color'),
  {
    value: 'yellow',
    writable: true,
    enumerable: true,
    configurable: true,
  });
```

# Relationships

## Builds Upon
- **property-attributes** — descriptors are the JavaScript encoding of attributes

## Enables
- **object-define-property** — takes a descriptor as input
- **object-get-own-property-descriptor** — returns a descriptor
- **object-create** — accepts descriptors in its second argument
- **property-definition** — definition operates through descriptors

## Related
- **data-property-descriptor** — the descriptor subtype for data properties
- **accessor-property-descriptor** — the descriptor subtype for accessor properties

## Contrasts With
- None

# Common Errors

- **Error**: Mixing data and accessor attributes in one descriptor (e.g., `{ value: 1, get() {} }`).
  **Correction**: A descriptor must be either a data descriptor or an accessor descriptor. Including both `value`/`writable` and `get`/`set` throws a TypeError.

# Common Confusions

- **Confusion**: Thinking omitted descriptor properties always default to `false`/`undefined`.
  **Clarification**: Defaults apply only when creating a new property. When changing an existing property, omitted attributes leave the current values unchanged.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.2, lines 215-241. Section 10.7, lines 618-679.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with TypeScript interfaces and detailed omission behavior.
- Cross-reference status: verified
