---
# === CORE IDENTIFICATION ===
concept: Object.create()
slug: object-create

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
section: "10.5 Object.create()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-descriptor
  - prototype-internal-slot
extends: []
related:
  - object-define-properties
  - object-get-own-property-descriptors
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a property with specific attributes using Object.defineProperty()?"
---

# Quick Definition

`Object.create(proto, properties?)` creates a new object whose `[[Prototype]]` is `proto`. The optional second argument specifies property descriptors for the new object's own properties, using the same semantics as `Object.defineProperties()`.

# Core Definition

As described in "Deep JavaScript" Ch 10, `Object.create()` has the signature `(proto: null|object, properties?: {[k: string|symbol]: PropertyDescriptor}): object`. It "first, creates an object whose prototype is `proto`. Then, if the optional parameter `properties` has been provided, adds properties to it -- in the same manner as `Object.defineProperties()`. Finally, returns the result."

# Prerequisites

- **Property Descriptor** — the optional second argument uses descriptors
- **[[Prototype]] Internal Slot** — the first argument sets `[[Prototype]]`

# Key Properties

1. First argument sets the prototype of the new object
2. Optional second argument defines properties via descriptors
3. Same definition semantics as `Object.defineProperties()` for the second argument
4. Can create objects with `null` prototype (no inherited properties)
5. Introduced in ES5

# Construction / Recognition

## To Construct/Create:
1. `Object.create(Object.prototype)` — creates a plain object
2. `Object.create(proto, descriptors)` — creates with prototype and properties
3. `Object.create(null)` — creates an object with no prototype

## To Identify/Recognize:
1. Creates new objects with explicit prototype control

# Context & Application

`Object.create()` is used for cloning objects with correct prototypes, creating objects with null prototype for use as dictionaries, and creating objects with specific property attributes. Combined with `Object.getOwnPropertyDescriptors()`, it enables faithful object cloning.

# Examples

**Example 1** (Ch 10): Cloning with correct prototype:
```js
const clone = Object.create(
  Object.getPrototypeOf(original),
  Object.getOwnPropertyDescriptors(original));
```

**Example 2** (Ch 10): Creating with descriptors:
```js
const address = Object.create(Object.prototype, {
  street: { value: 'Evergreen Terrace', enumerable: true },
  number: { value: 742, enumerable: true },
});
```

# Relationships

## Builds Upon
- **property-descriptor** — second argument uses descriptors
- **prototype-internal-slot** — first argument sets `[[Prototype]]`

## Enables
- Object cloning with correct prototype chains
- Creation of null-prototype objects

## Related
- **object-define-properties** — second argument uses same semantics
- **object-get-own-property-descriptors** — output used as second argument for cloning

## Contrasts With
- None

# Common Errors

- **Error**: Forgetting that properties defined via the second argument default to non-enumerable.
  **Correction**: Like `Object.defineProperty()`, omitted attributes default to `false`. Always specify `enumerable: true` if the property should be visible to `Object.keys()`.

# Common Confusions

- **Confusion**: Thinking `Object.create({})` and `{}` produce the same result.
  **Clarification**: `Object.create({})` creates an object whose prototype is an empty object, which itself inherits from `Object.prototype`. So the result has one extra level in its prototype chain.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.5, lines 459-495. Section 10.9, lines 867-882.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with API signature and examples.
- Cross-reference status: verified
