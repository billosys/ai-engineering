---
# === CORE IDENTIFICATION ===
concept: Property Attributes
slug: property-attributes

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
  - "attributes"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-key
extends: []
related:
  - property-descriptor
  - data-property
  - accessor-property
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a property descriptor?"
  - "How do property attributes relate to Object.freeze()?"
  - "What must I understand before learning about property assignment vs. definition?"
  - "What must I understand before learning about enumerability?"
---

# Quick Definition

Property attributes are the fields that make up a property in the ECMAScript specification. Properties are not atomic — they are composed of multiple attributes including `value`, `writable`, `get`, `set`, `configurable`, and `enumerable`.

# Core Definition

As described in "Deep JavaScript" Ch 10, "properties are not atomic in the spec, but composed of multiple *attributes* (think fields in a record). Even the value of a data property is stored in an attribute!" There are two kinds of properties, each with different attributes:

| Kind | Attribute | Default |
|------|-----------|---------|
| Data property | `value: any` | `undefined` |
| Data property | `writable: boolean` | `false` |
| Accessor property | `get: (this: any) => any` | `undefined` |
| Accessor property | `set: (this: any, v: any) => void` | `undefined` |
| All properties | `configurable: boolean` | `false` |
| All properties | `enumerable: boolean` | `false` |

# Prerequisites

- **Property Key** — attributes are associated with a property identified by its key

# Key Properties

1. Data properties have `value` and `writable` attributes
2. Accessor properties have `get` and `set` attributes
3. All properties share `configurable` and `enumerable` attributes
4. Default values are `undefined` for value/get/set and `false` for boolean attributes
5. Attributes are manipulated via property descriptors

# Construction / Recognition

## To Construct/Create:
1. Properties created via assignment or object literals get `writable: true`, `enumerable: true`, `configurable: true`
2. Properties created via `Object.defineProperty()` get defaults of `false`/`undefined` for omitted attributes

## To Identify/Recognize:
1. Use `Object.getOwnPropertyDescriptor(obj, key)` to inspect attributes of a specific property
2. Use `Object.getOwnPropertyDescriptors(obj)` to inspect all own properties

# Context & Application

Property attributes are the foundation for the entire property system in JavaScript. They underpin object protection (freeze, seal, preventExtensions), property definition vs. assignment semantics, and enumerability behavior. Ch 10 serves as the prerequisite for Ch 11, 12, and 13.

# Examples

**Example 1** (Ch 10): Properties created via object literals have all-`true` boolean attributes:
```js
const obj = { prop: 'yes' };
assert.deepEqual(
  Object.getOwnPropertyDescriptors(obj),
  {
    prop: {
      value: 'yes',
      writable: true,
      enumerable: true,
      configurable: true
    }
  });
```

# Relationships

## Builds Upon
- **property-key** — each property is identified by its key and characterized by its attributes

## Enables
- **property-descriptor** — descriptors encode attributes as JavaScript objects
- **data-property** — a property kind defined by its attributes
- **accessor-property** — a property kind defined by its attributes
- **configurable-attribute** — one of the shared attributes
- **enumerable-attribute** — one of the shared attributes
- **writable-attribute** — a data property attribute
- **value-attribute** — a data property attribute

## Related
- **object-freeze** — manipulates property attributes to achieve immutability

## Contrasts With
- None

# Common Errors

- **Error**: Assuming that omitted attributes in `Object.defineProperty()` default to `true`.
  **Correction**: When creating a new property, omitted attributes default to `false`/`undefined`, not `true`. This differs from assignment, which sets boolean attributes to `true`.

# Common Confusions

- **Confusion**: Thinking properties are just key-value pairs.
  **Clarification**: Properties are composed of multiple attributes. Even the "value" is just one attribute among several that control the property's behavior.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.1.3, lines 139-186.

# Verification Notes

- Definition source: direct
- Confidence rationale: Central topic of the chapter, explicitly defined with attribute table.
- Cross-reference status: verified — Ch 11, 12, 13 all reference Ch 10 as prerequisite
