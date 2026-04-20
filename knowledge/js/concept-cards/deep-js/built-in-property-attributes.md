---
# === CORE IDENTIFICATION ===
concept: Built-in Property Attributes
slug: built-in-property-attributes

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
section: "10.8 What property attributes do built-in constructs use?"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-attributes
  - data-property
  - accessor-property
extends: []
related:
  - enumerable-attribute
  - configurable-attribute
  - writable-attribute
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is enumerability?"
  - "What must I understand before learning about enumerability?"
---

# Quick Definition

JavaScript built-in constructs use consistent patterns for property attributes: own properties from assignment/literals are writable, enumerable, and configurable; prototype properties of classes are writable, non-enumerable, and configurable.

# Core Definition

As described in "Deep JavaScript" Ch 10, the general rule for property attributes is: "Properties of objects at the beginning of a prototype chain are usually writable, enumerable, and configurable." And "most inherited properties are non-enumerable, to hide them from legacy constructs such as `for-in` loops. Inherited properties are usually writable and configurable."

Specific patterns:
- **Assignment/object literals**: `writable: true, enumerable: true, configurable: true`
- **Array `.length`**: `writable: true, enumerable: false, configurable: false`
- **Built-in prototype methods** (e.g., `Array.prototype.map`): `writable: true, enumerable: false, configurable: true`
- **User-defined class prototype methods**: `writable: true, enumerable: false, configurable: true`
- **User-defined class instance properties**: `writable: true, enumerable: true, configurable: true`

# Prerequisites

- **Property Attributes** — need to understand what attributes are
- **Data Property** / **Accessor Property** — need to understand property kinds

# Key Properties

1. Own properties from assignment/literals: all-`true` boolean attributes
2. Prototype methods (built-in and user-defined): non-enumerable but writable and configurable
3. Array `.length`: writable but non-enumerable and non-configurable
4. Instance properties from class constructors: all-`true` boolean attributes

# Construction / Recognition

## To Construct/Create:
1. Not directly constructed — these are the patterns used by the language itself

## To Identify/Recognize:
1. Use `Object.getOwnPropertyDescriptor()` to inspect any built-in property

# Context & Application

Understanding these default patterns explains why `for-in` and `Object.keys()` typically work as expected: own data properties are enumerable and thus visible, while prototype methods are non-enumerable and thus hidden. This is the foundation for understanding Ch 13 (enumerability).

# Examples

**Example 1** (Ch 10): Prototype methods are non-enumerable:
```js
assert.deepEqual(
  Object.getOwnPropertyDescriptor(Array.prototype, 'map'),
  {
    value: Array.prototype.map,
    writable: true,
    enumerable: false,
    configurable: true
  });
```

**Example 2** (Ch 10): Instance properties are enumerable:
```js
const dc = new DataContainer('abc');
assert.deepEqual(
  Object.getOwnPropertyDescriptor(dc, 'data'),
  {
    value: 'abc',
    writable: true,
    enumerable: true,
    configurable: true,
  });
```

# Relationships

## Builds Upon
- **property-attributes** — this describes the attribute patterns used by built-in constructs

## Enables
- **enumerable-attribute** — understanding why most properties you encounter are enumerable
- **for-in-loop** — understanding why `for-in` works as expected with classes

## Related
- **writable-attribute** — part of the pattern
- **configurable-attribute** — part of the pattern

## Contrasts With
- None

# Common Errors

- **Error**: Assuming all properties follow the same attribute pattern.
  **Correction**: Own properties and prototype properties follow different patterns. Array `.length` is a special case.

# Common Confusions

- **Confusion**: Wondering why `Object.keys()` doesn't show methods inherited from a class.
  **Clarification**: Class prototype methods are non-enumerable by default, so they are hidden from `Object.keys()` and `for-in`.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.8, lines 681-821.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly documented with examples for each built-in construct.
- Cross-reference status: verified against Ch 13
