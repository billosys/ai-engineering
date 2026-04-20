---
# === CORE IDENTIFICATION ===
concept: "[[Prototype]] Internal Slot"
slug: prototype-internal-slot

# === CLASSIFICATION ===
category: object-model
subcategory: object-structure
tier: foundational

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Property attributes: an introduction"
chapter_number: 10
section: "10.1.1 Internal slots"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "[[Prototype]]"
  - "prototype slot"
  - "object prototype"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - internal-slots
extends: []
related:
  - extensible-internal-slot
  - property-assignment
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about property assignment vs. definition?"
---

# Quick Definition

The `[[Prototype]]` internal slot stores the prototype of an object. Its type is `null | object`, and it can be accessed indirectly via `Object.getPrototypeOf()` and `Object.setPrototypeOf()`.

# Core Definition

As described in "Deep JavaScript" Ch 10, `[[Prototype]]` is a data slot of ordinary objects with the type `null | object`. It stores the prototype of an object and "can be accessed indirectly via `Object.getPrototypeOf()` and `Object.setPrototypeOf()`." The prototype chain formed by `[[Prototype]]` links is central to inheritance, property lookup, and assignment behavior.

# Prerequisites

- **Internal Slots** — `[[Prototype]]` is a specific internal slot; understanding the general concept is needed first

# Key Properties

1. Type is `null` or an object reference
2. Not directly accessible from JavaScript
3. Accessible via `Object.getPrototypeOf()` and `Object.setPrototypeOf()`
4. Forms the prototype chain used for property lookup
5. Inherited non-writable properties in the chain can block assignment

# Construction / Recognition

## To Construct/Create:
1. Set at object creation time (e.g., via `Object.create(proto)`)
2. Object literals get `Object.prototype` as their `[[Prototype]]`
3. Can be changed via `Object.setPrototypeOf()`

## To Identify/Recognize:
1. Use `Object.getPrototypeOf(obj)` to read the value
2. Appears in specification text as `[[Prototype]]`

# Context & Application

The `[[Prototype]]` slot is foundational to JavaScript's prototypal inheritance. It determines which properties an object inherits, affects property assignment behavior (inherited setters, inherited non-writable properties), and is central to the prototype chain traversal described in the assignment algorithm.

# Examples

**Example 1** (Ch 10):
```js
const proto = { prop: 1 };
const obj = Object.create(proto);
// obj.[[Prototype]] is proto
```

# Relationships

## Builds Upon
- **internal-slots** — `[[Prototype]]` is a specific data slot

## Enables
- **property-assignment** — assignment traverses the prototype chain via `[[Prototype]]`
- **inherited-read-only-prevents-assignment** — the prototype chain determines whether inherited non-writable properties block assignment

## Related
- **extensible-internal-slot** — another data slot of ordinary objects
- **object-create** — creates objects with a specified `[[Prototype]]`

## Contrasts With
- None

# Common Errors

- **Error**: Confusing `[[Prototype]]` with the `.prototype` property of functions/classes.
  **Correction**: `[[Prototype]]` is an internal slot on every object; `.prototype` is a regular property on constructor functions used to set `[[Prototype]]` of instances.

# Common Confusions

- **Confusion**: Thinking `__proto__` and `[[Prototype]]` are the same thing.
  **Clarification**: `__proto__` is a legacy accessor property that reads/writes `[[Prototype]]`; the proper APIs are `Object.getPrototypeOf()` and `Object.setPrototypeOf()`.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.1.1, lines 118-121.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly described in the source text with type and access methods.
- Cross-reference status: verified against Ch 10 and Ch 12 (prototype chain and assignment)
