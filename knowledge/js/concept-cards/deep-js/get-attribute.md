---
# === CORE IDENTIFICATION ===
concept: Get Attribute
slug: get-attribute

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
  - "getter"
  - "getter function"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - accessor-property
extends: []
related:
  - set-attribute
contrasts_with:
  - value-attribute

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a data property vs. an accessor property?"
  - "What distinguishes a data property descriptor from an accessor property descriptor?"
---

# Quick Definition

The `get` attribute of an accessor property stores a getter function with the signature `(this: any) => any`. It is invoked when the property is read. Its default value is `undefined`.

# Core Definition

As described in "Deep JavaScript" Ch 10, an accessor property's getter is "stored in the attribute `get`." The `get` attribute has the type signature `(this: any) => any` and defaults to `undefined`. When a property with a `get` attribute is read, the getter function is called with `this` bound to the object.

# Prerequisites

- **Accessor Property** — `get` is an attribute specific to accessor properties

# Key Properties

1. Type: `(this: any) => any`
2. Default: `undefined`
3. Exclusive to accessor properties
4. Called automatically when the property is read
5. Cannot coexist with `value` or `writable` in a descriptor

# Construction / Recognition

## To Construct/Create:
1. Object literal: `{ get prop() { return ...; } }`
2. Definition: `Object.defineProperty(obj, 'prop', { get() { return ...; } })`

## To Identify/Recognize:
1. Check `Object.getOwnPropertyDescriptor(obj, key).get`

# Context & Application

Getters allow computed properties and intercept read access. They are relevant to understanding `Object.assign()`, which reads via getters but writes via assignment — converting accessor properties to data properties on the target.

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
assert.equal(legoBrick.description, 'Plate 1x3 (yellow)');
```

# Relationships

## Builds Upon
- **accessor-property** — `get` is an attribute of accessor properties

## Enables
- **assignment-calls-setters** — understanding getters helps understand the getter/setter contract

## Related
- **set-attribute** — the companion setter attribute

## Contrasts With
- **value-attribute** — data properties store a static value; getters compute a value

# Common Errors

- **Error**: Defining both `get` and `value` in the same property descriptor.
  **Correction**: A descriptor must be either a data descriptor (with `value`/`writable`) or an accessor descriptor (with `get`/`set`). Mixing them throws a TypeError.

# Common Confusions

- **Confusion**: Thinking `Object.assign()` copies getters.
  **Clarification**: `Object.assign()` invokes the getter to read the value, then writes it as a data property on the target. The getter function itself is not copied.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.1.3, lines 148, 158.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly listed in the property attributes table with type signature.
- Cross-reference status: verified
