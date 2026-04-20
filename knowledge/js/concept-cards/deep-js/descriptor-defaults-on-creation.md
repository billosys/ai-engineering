---
# === CORE IDENTIFICATION ===
concept: Descriptor Defaults on Creation
slug: descriptor-defaults-on-creation

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
section: "10.7 Omitting descriptor properties"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "omitting descriptor properties"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-descriptor
  - object-define-property
extends: []
related:
  - property-attributes
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a property with specific attributes using Object.defineProperty()?"
  - "What is a property descriptor?"
---

# Quick Definition

When creating a new property via `Object.defineProperty()`, omitted descriptor attributes use their default values (`false` for booleans, `undefined` for value/get/set). When changing an existing property, omitted attributes leave the current values unchanged.

# Core Definition

As described in "Deep JavaScript" Ch 10, "All properties of descriptors are optional. What happens when you omit a property depends on the operation." When creating: "omitting attributes means that their default values are used." When changing: "omitting descriptor properties means that the corresponding attributes are not touched."

# Prerequisites

- **Property Descriptor** — understanding descriptor structure
- **Object.defineProperty()** — the method where these defaults apply

# Key Properties

1. Creating new property: omitted booleans default to `false`; omitted `value`/`get`/`set` default to `undefined`
2. Changing existing property: omitted attributes are left at their current values
3. This is a critical difference from assignment, which always sets boolean attributes to `true`

# Construction / Recognition

## To Construct/Create:
1. Create with minimal descriptor: `Object.defineProperty(obj, 'prop', { value: 'red' })`
2. Result: `{ value: 'red', writable: false, enumerable: false, configurable: false }`

## To Identify/Recognize:
1. A property created via `Object.defineProperty()` with incomplete descriptor

# Context & Application

This behavior is a common source of bugs. Developers who are used to assignment (where properties are writable, enumerable, and configurable) may be surprised that `Object.defineProperty()` with `{ value: 42 }` creates a non-writable, non-enumerable, non-configurable property.

# Examples

**Example 1** (Ch 10): Creating — defaults to `false`:
```js
const car = {};
Object.defineProperty(car, 'color', { value: 'red' });
assert.deepEqual(
  Object.getOwnPropertyDescriptor(car, 'color'),
  {
    value: 'red',
    writable: false,
    enumerable: false,
    configurable: false,
  });
```

**Example 2** (Ch 10): Changing — preserves existing attributes:
```js
const car = { color: 'yellow' };
Object.defineProperty(car, 'color', { value: 'pink' });
assert.deepEqual(
  Object.getOwnPropertyDescriptor(car, 'color'),
  {
    value: 'pink',
    writable: true,    // preserved from original
    enumerable: true,  // preserved from original
    configurable: true, // preserved from original
  });
```

# Relationships

## Builds Upon
- **property-descriptor** — this describes behavior when descriptor fields are omitted
- **object-define-property** — this is where the behavior manifests

## Enables
- Understanding why defined properties often behave differently from assigned properties

## Related
- **property-attributes** — the defaults are attribute defaults from the spec

## Contrasts With
- None

# Common Errors

- **Error**: Creating a property with `Object.defineProperty(obj, 'x', { value: 1 })` and expecting it to be writable and enumerable.
  **Correction**: Explicitly set `writable: true, enumerable: true, configurable: true` when creating properties that should behave like assigned properties.

# Common Confusions

- **Confusion**: Thinking defaults always apply.
  **Clarification**: Defaults only apply when creating a NEW property. When changing an existing property, omitted attributes keep their current values.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.7, lines 618-679.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly explained with contrasting examples for creation vs. change.
- Cross-reference status: verified
