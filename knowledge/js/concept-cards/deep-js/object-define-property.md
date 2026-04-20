---
# === CORE IDENTIFICATION ===
concept: Object.defineProperty()
slug: object-define-property

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
section: "10.4.1 Object.defineProperty()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-descriptor
extends: []
related:
  - object-define-properties
  - property-definition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a property with specific attributes using Object.defineProperty()?"
  - "How does property assignment differ from property definition?"
---

# Quick Definition

`Object.defineProperty(obj, key, propDesc)` creates or changes a property on `obj` whose key is `key` and whose attributes are specified by the property descriptor `propDesc`. It returns the modified object.

# Core Definition

As described in "Deep JavaScript" Ch 10, `Object.defineProperty()` has the signature `(obj: object, key: string|symbol, propDesc: PropertyDescriptor): object`. It "creates or changes a property on `obj` whose key is `key` and whose attributes are specified via `propDesc`. Returns the modified object." When the property does not exist, it is created with omitted attributes defaulting to `false`/`undefined`. When the property exists, only the specified attributes are changed.

# Prerequisites

- **Property Descriptor** — takes a property descriptor as input

# Key Properties

1. Creates a new property or changes an existing one
2. Returns the modified object
3. When creating: omitted attributes default to `false`/`undefined`
4. When changing: omitted attributes are left unchanged
5. Ignores inherited setters (unlike assignment)
6. Can change a property from data to accessor or vice versa
7. Throws TypeError if change violates `configurable: false` constraints
8. Introduced in ES5

# Construction / Recognition

## To Construct/Create:
1. `Object.defineProperty(obj, 'prop', { value: 42, writable: true, enumerable: true, configurable: true })`
2. Changing kind: `Object.defineProperty(obj, 'prop', { get() { return 42; } })`

## To Identify/Recognize:
1. A method call that takes three arguments: object, key, descriptor

# Context & Application

This is the primary method for property definition (as opposed to assignment). It is used when you need to create properties with specific attributes, convert between data and accessor properties, or bypass inherited setters.

# Examples

**Example 1** (Ch 10): Creating a property:
```js
const car = {};
Object.defineProperty(car, 'color', {
  value: 'blue',
  writable: true,
  enumerable: true,
  configurable: true,
});
assert.deepEqual(car, { color: 'blue' });
```

**Example 2** (Ch 10): Converting data property to getter:
```js
const car = { color: 'blue' };
let readCount = 0;
Object.defineProperty(car, 'color', {
  get() {
    readCount++;
    return 'red';
  },
});
assert.equal(car.color, 'red');
assert.equal(readCount, 1);
```

# Relationships

## Builds Upon
- **property-descriptor** — takes a descriptor as the third argument

## Enables
- **property-definition** — this method performs property definition
- **object-seal** — uses definition internally to set `configurable: false`
- **object-freeze** — uses definition internally

## Related
- **object-define-properties** — the batch version

## Contrasts With
- None

# Common Errors

- **Error**: Forgetting that omitted attributes default to `false` when creating a new property.
  **Correction**: Always specify all desired attributes explicitly, especially `writable`, `enumerable`, and `configurable`, when creating properties via definition.

# Common Confusions

- **Confusion**: Thinking `Object.defineProperty()` and assignment (`=`) are interchangeable.
  **Clarification**: They have different semantics: assignment invokes setters and creates properties with all-`true` boolean attributes; definition ignores setters and defaults to all-`false`.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.4.1, lines 346-412. Section 10.9, lines 829-850.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with API signature and multiple examples.
- Cross-reference status: verified against Ch 12 (definition semantics)
