---
# === CORE IDENTIFICATION ===
concept: Set Attribute
slug: set-attribute

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
  - "setter"
  - "setter function"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - accessor-property
extends: []
related:
  - get-attribute
contrasts_with:
  - writable-attribute

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a data property vs. an accessor property?"
  - "How does property assignment differ from property definition?"
---

# Quick Definition

The `set` attribute of an accessor property stores a setter function with the signature `(this: any, v: any) => void`. It is invoked when the property is assigned to. Its default value is `undefined`.

# Core Definition

As described in "Deep JavaScript" Ch 10, an accessor property's setter is "stored in the attribute `set`." The `set` attribute has the type signature `(this: any, v: any) => void` and defaults to `undefined`. When a property with a `set` attribute is assigned to, the setter function is called. Critically, assignment invokes setters but definition does not (Ch 12).

# Prerequisites

- **Accessor Property** — `set` is an attribute specific to accessor properties

# Key Properties

1. Type: `(this: any, v: any) => void`
2. Default: `undefined`
3. Exclusive to accessor properties
4. Called by assignment, but NOT by definition
5. An accessor without a setter is considered read-only

# Construction / Recognition

## To Construct/Create:
1. Object literal: `{ set prop(v) { ... } }`
2. Definition: `Object.defineProperty(obj, 'prop', { set(v) { ... } })`

## To Identify/Recognize:
1. Check `Object.getOwnPropertyDescriptor(obj, key).set`

# Context & Application

Setters are central to the distinction between assignment and definition (Ch 12). Assignment invokes inherited setters; definition ignores them. This distinction matters when you want to create an own property that shadows an inherited accessor.

# Examples

**Example 1** (Ch 10):
```js
const source = {
  set data(value) {
    this._data = value;
  }
};
assert.equal('data' in source, true);
assert.equal(source.data, undefined); // no getter, so undefined
```

# Relationships

## Builds Upon
- **accessor-property** — `set` is an attribute of accessor properties

## Enables
- **assignment-calls-setters** — assignment triggers setters; definition does not

## Related
- **get-attribute** — the companion getter attribute

## Contrasts With
- **writable-attribute** — `writable` controls data property mutability; `set` intercepts writes to accessor properties

# Common Errors

- **Error**: Expecting definition via `Object.defineProperty()` to invoke an inherited setter.
  **Correction**: Definition always creates or changes an own property directly, ignoring inherited setters.

# Common Confusions

- **Confusion**: Thinking an accessor without a setter silently ignores writes.
  **Clarification**: In strict mode, assigning to an accessor property that has no setter throws a TypeError.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.1.3, lines 148-149, 159.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly listed in the property attributes table with type signature.
- Cross-reference status: verified against Ch 12 (assignment vs. definition)
