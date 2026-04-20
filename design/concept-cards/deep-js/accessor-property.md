---
# === CORE IDENTIFICATION ===
concept: Accessor Property
slug: accessor-property

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
  - "getter/setter property"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-attributes
extends: []
related:
  - get-attribute
  - set-attribute
  - accessor-property-descriptor
contrasts_with:
  - data-property

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a data property vs. an accessor property?"
  - "What distinguishes a data property descriptor from an accessor property descriptor?"
---

# Quick Definition

An accessor property consists of a getter function and/or a setter function. The getter is stored in the `get` attribute; the setter in the `set` attribute.

# Core Definition

As described in "Deep JavaScript" Ch 10, "An *accessor property* consists of a getter function and/or a setter function. The former is stored in the attribute `get`, the latter in the attribute `set`." Accessor properties also have the shared `configurable` and `enumerable` attributes, but do not have `value` or `writable`.

# Prerequisites

- **Property Attributes** — accessor properties are defined by their specific set of attributes

# Key Properties

1. Has `get` attribute (type: `(this: any) => any`, default: `undefined`)
2. Has `set` attribute (type: `(this: any, v: any) => void`, default: `undefined`)
3. Has shared `configurable` and `enumerable` attributes
4. Cannot have `value` or `writable` attributes (mutually exclusive with data property)
5. An accessor with only `get` and no `set` is considered read-only

# Construction / Recognition

## To Construct/Create:
1. Object literal syntax: `{ get prop() { ... }, set prop(v) { ... } }`
2. `Object.defineProperty(obj, 'prop', { get() { ... }, set(v) { ... } })`

## To Identify/Recognize:
1. Inspect with `Object.getOwnPropertyDescriptor()` — if result has `get` or `set`, it is an accessor
2. Cannot be created via simple assignment

# Context & Application

Accessor properties intercept read and write operations. They are important for understanding assignment vs. definition: assignment invokes inherited setters, while definition ignores them. `Object.assign()` reads via getters but writes via assignment, which can convert accessor properties to data properties.

# Examples

**Example 1** (Ch 10):
```js
const legoBrick = {
  kind: 'Plate 1x3',
  color: 'yellow',
  get description() {
    return `${this.kind} (${this.color})`;
  },
};
assert.deepEqual(
  Object.getOwnPropertyDescriptor(legoBrick, 'description'),
  {
    get: Object.getOwnPropertyDescriptor(legoBrick, 'description').get,
    set: undefined,
    enumerable: true,
    configurable: true
  });
```

# Relationships

## Builds Upon
- **property-attributes** — accessor properties are characterized by `get` and `set` attributes

## Enables
- **accessor-property-descriptor** — the descriptor type for accessor properties
- **assignment-calls-setters** — assignment invokes inherited setters

## Related
- **get-attribute** — the getter function attribute
- **set-attribute** — the setter function attribute

## Contrasts With
- **data-property** — stores a value directly instead of using get/set functions

# Common Errors

- **Error**: Using `Object.assign()` to copy accessor properties faithfully.
  **Correction**: `Object.assign()` reads the getter's return value and creates a data property on the target. Use `Object.defineProperties()` with `Object.getOwnPropertyDescriptors()` to copy accessors faithfully.

# Common Confusions

- **Confusion**: Thinking an accessor property without a setter simply ignores writes.
  **Clarification**: An accessor property without a setter is considered read-only; attempting to assign to it in strict mode throws a TypeError.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.1.3, lines 147-149, 158-159.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined in the property attributes table and demonstrated with examples.
- Cross-reference status: verified against Ch 10 and Ch 12
