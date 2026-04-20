---
# === CORE IDENTIFICATION ===
concept: Object.freeze()
slug: object-freeze

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
section: "11.4 Freezing objects"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "freeze"
  - "freezing"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-attributes
  - writable-attribute
  - configurable-attribute
  - object-seal
extends:
  - object-seal
related:
  - object-is-frozen
  - shallow-freezing
  - deep-freezing
contrasts_with:
  - object-seal
  - object-prevent-extensions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do property attributes relate to Object.freeze()?"
  - "What distinguishes Object.preventExtensions() from Object.seal() from Object.freeze()?"
---

# Quick Definition

`Object.freeze(obj)` makes all properties non-writable, seals the object, and returns it. The result is a fully immutable object (at the shallow level): not extensible, all properties read-only, and no way to change that.

# Core Definition

As described in "Deep JavaScript" Ch 11, `Object.freeze()` has the signature `<T>(obj: T): T`. "This method immediately returns `obj` if it isn't an object. Otherwise, it makes all properties non-writable, seals `obj`, and returns it. That is, `obj` is not extensible, all properties are read-only and there is no way to change that."

# Prerequisites

- **Property Attributes** — freezing manipulates writable and configurable
- **Writable Attribute** — freezing sets this to false
- **Configurable Attribute** — freezing sets this to false (via sealing)
- **Object.seal()** — freezing includes sealing

# Key Properties

1. Makes all data properties non-writable
2. Seals the object (non-extensible + all properties non-configurable)
3. The strongest built-in protection level
4. Shallow — does not freeze values of properties
5. Irreversible
6. Returns the frozen object
7. Non-objects are returned as-is

# Construction / Recognition

## To Construct/Create:
1. `Object.freeze(obj)`

## To Identify/Recognize:
1. `Object.isFrozen(obj)` returns `true`
2. `Object.isSealed(obj)` returns `true`
3. `Object.isExtensible(obj)` returns `false`
4. All data properties have `writable: false` and `configurable: false`

# Context & Application

Freezing provides the strongest built-in immutability guarantee for objects. It is commonly used for constant configuration objects, default values, and shared state that should never change. However, because it is shallow, nested objects need separate freezing (deep freezing).

# Examples

**Example 1** (Ch 11):
```js
const point = { x: 17, y: -5 };
Object.freeze(point);
assert.throws(
  () => point.x = 2,
  /^TypeError: Cannot assign to read only property 'x'/);
assert.throws(
  () => Object.defineProperty(point, 'x', {enumerable: false}),
  /^TypeError: Cannot redefine property: x$/);
assert.throws(
  () => point.z = 4,
  /^TypeError: Cannot add property z, object is not extensible$/);
```

# Relationships

## Builds Upon
- **object-seal** — freezing includes sealing
- **writable-attribute** — freezing sets this to `false`

## Enables
- **shallow-freezing** — understanding that freeze is shallow
- **deep-freezing** — the pattern for recursively freezing

## Related
- **object-is-frozen** — checks whether an object is frozen

## Contrasts With
- **object-seal** — seal does not make properties non-writable
- **object-prevent-extensions** — preventExtensions does not change any property attributes

# Common Errors

- **Error**: Expecting `Object.freeze()` to make nested objects immutable.
  **Correction**: Freezing is shallow. Nested objects must be frozen separately (deep freezing).

# Common Confusions

- **Confusion**: Thinking frozen objects are deeply immutable.
  **Clarification**: Only the own properties of the frozen object are read-only. Values that are objects can still be mutated.

# Source Reference

Chapter 11: Protecting objects from being changed, Section 11.4, lines 223-270.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with API signature and comprehensive examples.
- Cross-reference status: verified
