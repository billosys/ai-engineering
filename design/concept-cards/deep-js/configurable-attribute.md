---
# === CORE IDENTIFICATION ===
concept: Configurable Attribute
slug: configurable-attribute

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-attributes
extends: []
related:
  - writable-attribute
  - enumerable-attribute
contrasts_with:
  - writable-attribute

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes the configurable attribute from the writable attribute?"
  - "How do property attributes relate to Object.freeze()?"
---

# Quick Definition

The `configurable` attribute is a boolean shared by both data and accessor properties. When `false`, the property cannot be deleted, cannot be converted between data and accessor types, and its attributes (other than `value`) cannot be changed.

# Core Definition

As described in "Deep JavaScript" Ch 10, "`configurable` determines if the attributes of a property can be changed. If it is `false`, then: We cannot delete the property. We cannot change a property from a data property to an accessor property or vice versa. We cannot change any attribute other than `value`. However, one more attribute change is allowed: We can change `writable` from `true` to `false`."

# Prerequisites

- **Property Attributes** — `configurable` is one of the shared property attributes

# Key Properties

1. Type: `boolean`
2. Default: `false`
3. Applies to both data and accessor properties
4. When `false`: property cannot be deleted
5. When `false`: cannot change property kind (data <-> accessor)
6. When `false`: cannot change any attribute other than `value`
7. Exception: `writable` can still be changed from `true` to `false` (historical reason)

# Construction / Recognition

## To Construct/Create:
1. Assignment creates properties with `configurable: true`
2. `Object.defineProperty()` defaults to `configurable: false` if omitted

## To Identify/Recognize:
1. Check `Object.getOwnPropertyDescriptor(obj, key).configurable`

# Context & Application

The `configurable` attribute is set to `false` by `Object.seal()` and `Object.freeze()`. It locks down a property's metadata. The special exception allowing `writable` to change from `true` to `false` exists because Array `.length` has always been writable and non-configurable, and this exception enables freezing arrays.

# Examples

**Example 1** (Ch 11): After sealing, `configurable` becomes `false`:
```js
const obj = { first: 'Jane' };
Object.seal(obj);
assert.throws(
  () => Object.defineProperty(obj, 'first', { enumerable: false }),
  /^TypeError: Cannot redefine property: first$/);
```

# Relationships

## Builds Upon
- **property-attributes** — `configurable` is a shared attribute for all property kinds

## Enables
- **object-seal** — sealing sets `configurable` to `false` on all properties
- **object-freeze** — freezing also sets `configurable` to `false`
- **property-definition** — the definition algorithm checks `configurable` to validate changes

## Related
- **enumerable-attribute** — another shared attribute, locked by `configurable: false`

## Contrasts With
- **writable-attribute** — `writable` controls value changes via assignment; `configurable` controls attribute changes and property deletion

# Common Errors

- **Error**: Expecting to change `enumerable` on a non-configurable property.
  **Correction**: Non-configurable properties cannot have any attribute changed except `value` (and `writable` can go from `true` to `false`).

# Common Confusions

- **Confusion**: Thinking `configurable: false` means the value cannot change.
  **Clarification**: A non-configurable but writable property can still have its `value` changed via assignment or `Object.defineProperty()`.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.1.3, lines 160, 167-179.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with detailed rules and historical rationale.
- Cross-reference status: verified against Ch 11 (seal/freeze behavior)
