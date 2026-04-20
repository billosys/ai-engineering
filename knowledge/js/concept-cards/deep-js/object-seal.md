---
# === CORE IDENTIFICATION ===
concept: Object.seal()
slug: object-seal

# === CLASSIFICATION ===
category: object-protection
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Protecting objects from being changed"
chapter_number: 11
section: "11.3 Sealing objects"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "seal"
  - "sealing"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-attributes
  - configurable-attribute
  - object-prevent-extensions
extends:
  - object-prevent-extensions
related:
  - object-is-sealed
contrasts_with:
  - object-prevent-extensions
  - object-freeze

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Object.preventExtensions() from Object.seal() from Object.freeze()?"
  - "How do property attributes relate to Object.freeze()?"
---

# Quick Definition

`Object.seal(obj)` prevents extensions and makes all existing properties unconfigurable. Property values can still be changed (if writable), but properties cannot be deleted or have their attributes changed.

# Core Definition

As described in "Deep JavaScript" Ch 11, `Object.seal()` has the signature `<T>(obj: T): T`. "If `obj` isn't an object, it returns it. Otherwise, it prevents extensions of `obj`, makes all of its properties *unconfigurable*, and returns it. The properties being unconfigurable means that they can't be changed, anymore (except for their values): Read-only properties stay read-only, enumerable properties stay enumerable, etc."

# Prerequisites

- **Property Attributes** — sealing manipulates the configurable attribute
- **Configurable Attribute** — sealing sets this to false for all properties
- **Object.preventExtensions()** — sealing includes preventing extensions

# Key Properties

1. Prevents adding new properties (like preventExtensions)
2. Makes all properties unconfigurable (configurable: false)
3. Property values can still be changed if writable is true
4. Properties cannot be deleted
5. Property attributes (other than value) cannot be changed
6. Returns the sealed object
7. Irreversible

# Construction / Recognition

## To Construct/Create:
1. `Object.seal(obj)`

## To Identify/Recognize:
1. `Object.isSealed(obj)` returns `true`
2. `Object.isExtensible(obj)` returns `false`
3. All properties have `configurable: false`

# Context & Application

Sealing is the middle level of protection. It locks down the structure of an object (no adding/removing properties, no changing property types) while still allowing value changes for writable properties.

# Examples

**Example 1** (Ch 11):
```js
const obj = { first: 'Jane', last: 'Doe' };
Object.seal(obj);
assert.equal(Object.isExtensible(obj), false);
// Values can still be changed:
obj.first = 'John';
assert.deepEqual(obj, {first: 'John', last: 'Doe'});
// But attributes cannot:
assert.throws(
  () => Object.defineProperty(obj, 'first', { enumerable: false }),
  /^TypeError: Cannot redefine property: first$/);
```

# Relationships

## Builds Upon
- **object-prevent-extensions** — sealing includes preventing extensions
- **configurable-attribute** — sealing sets this to `false`

## Enables
- **object-freeze** — freezing is sealing plus making properties non-writable

## Related
- **object-is-sealed** — checks whether an object is sealed

## Contrasts With
- **object-prevent-extensions** — preventExtensions does not change configurable
- **object-freeze** — freeze also makes properties non-writable

# Common Errors

- **Error**: Expecting to delete properties from a sealed object.
  **Correction**: Sealed properties are unconfigurable and therefore cannot be deleted.

# Common Confusions

- **Confusion**: Thinking sealing makes properties read-only.
  **Clarification**: Sealing only makes properties unconfigurable. Writable properties remain writable — their values can still be changed.

# Source Reference

Chapter 11: Protecting objects from being changed, Section 11.3, lines 120-220.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with API signature and detailed examples.
- Cross-reference status: verified
