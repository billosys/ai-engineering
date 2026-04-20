---
# === CORE IDENTIFICATION ===
concept: Accessor Property Descriptor
slug: accessor-property-descriptor

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
  - accessor-property
extends:
  - property-descriptor
related: []
contrasts_with:
  - data-property-descriptor

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a data property descriptor from an accessor property descriptor?"
  - "What is a property descriptor?"
---

# Quick Definition

An accessor property descriptor is a property descriptor that encodes the attributes of an accessor property: `get`, `set`, `configurable`, and `enumerable`. All fields are optional.

# Core Definition

As described in "Deep JavaScript" Ch 10, the TypeScript interface for an accessor property descriptor is:

```ts
interface AccessorPropertyDescriptor {
  get?: (this: any) => any;
  set?: (this: any, v: any) => void;
  configurable?: boolean;
  enumerable?: boolean;
}
```

An accessor property descriptor contains `get` and/or `set` but never `value` or `writable`.

# Prerequisites

- **Property Descriptor** — this is a specific kind of property descriptor
- **Accessor Property** — this descriptor type corresponds to accessor properties

# Key Properties

1. Contains `get` (function) and/or `set` (function)
2. May also contain `configurable` and `enumerable`
3. Cannot contain `value` or `writable`
4. All fields are optional

# Construction / Recognition

## To Construct/Create:
1. `{ get() { return 42; }, set(v) { ... }, enumerable: true, configurable: true }`
2. Minimal: `{ get() { return 42; } }`

## To Identify/Recognize:
1. Has `get` or `set` property
2. Does not have `value` or `writable` property

# Context & Application

Accessor property descriptors are needed to faithfully copy accessor properties between objects, because `Object.assign()` converts accessors to data properties. The combination of `Object.getOwnPropertyDescriptors()` with `Object.defineProperties()` preserves accessor descriptors.

# Examples

**Example 1** (Ch 10):
```js
const legoBrick = {
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
- **property-descriptor** — accessor property descriptor is a subtype
- **accessor-property** — describes the attributes of accessor properties

## Enables
- **object-define-property** — accepts accessor property descriptors

## Related
- None

## Contrasts With
- **data-property-descriptor** — uses `value`/`writable` instead of `get`/`set`

# Common Errors

- **Error**: Including both `set` and `writable` in a single descriptor.
  **Correction**: `writable` is exclusive to data property descriptors. Mixing types throws a TypeError.

# Common Confusions

- **Confusion**: Thinking `Object.assign()` copies accessor descriptors.
  **Clarification**: `Object.assign()` reads the getter's return value and creates a data property on the target. Use `Object.defineProperties(target, Object.getOwnPropertyDescriptors(source))` to preserve accessors.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.2, lines 228-234.

# Verification Notes

- Definition source: direct (TypeScript interface from source)
- Confidence rationale: Explicitly defined with interface.
- Cross-reference status: verified
