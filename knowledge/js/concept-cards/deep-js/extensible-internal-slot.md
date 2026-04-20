---
# === CORE IDENTIFICATION ===
concept: "[[Extensible]] Internal Slot"
slug: extensible-internal-slot

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
  - "[[Extensible]]"
  - "extensible slot"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - internal-slots
extends: []
related:
  - prototype-internal-slot
  - object-prevent-extensions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Object.preventExtensions() from Object.seal() from Object.freeze()?"
---

# Quick Definition

The `[[Extensible]]` internal slot is a boolean that indicates whether it is possible to add new properties to an object. It can be set to `false` via `Object.preventExtensions()`.

# Core Definition

As described in "Deep JavaScript" Ch 10, `[[Extensible]]` is a data slot of ordinary objects with type `boolean`. It "indicates if it is possible to add properties to an object" and "can be set to `false` via `Object.preventExtensions()`." Once set to `false`, it cannot be changed back to `true`.

# Prerequisites

- **Internal Slots** — `[[Extensible]]` is a specific internal slot

# Key Properties

1. Boolean type
2. Defaults to `true` for newly created objects
3. Can be set to `false` via `Object.preventExtensions()`
4. Once `false`, cannot be changed back to `true`
5. Checked by `Object.isExtensible()`

# Construction / Recognition

## To Construct/Create:
1. Automatically set to `true` when an object is created
2. Set to `false` by `Object.preventExtensions()`, `Object.seal()`, or `Object.freeze()`

## To Identify/Recognize:
1. Use `Object.isExtensible(obj)` to check the current value

# Context & Application

The `[[Extensible]]` slot is the foundation for all three levels of object protection. Preventing extensions is the weakest protection level; sealing and freezing both set `[[Extensible]]` to `false` as part of their stronger protections.

# Examples

**Example 1** (Ch 11):
```js
const obj = { first: 'Jane' };
Object.preventExtensions(obj);
assert.throws(
  () => obj.last = 'Doe',
  /^TypeError: Cannot add property last, object is not extensible$/);
```

# Relationships

## Builds Upon
- **internal-slots** — `[[Extensible]]` is a specific data slot

## Enables
- **object-prevent-extensions** — directly manipulates this slot
- **object-seal** — sets `[[Extensible]]` to `false` as part of sealing
- **object-freeze** — sets `[[Extensible]]` to `false` as part of freezing

## Related
- **prototype-internal-slot** — another data slot of ordinary objects

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `Object.preventExtensions()` to be reversible.
  **Correction**: Once `[[Extensible]]` is set to `false`, it cannot be changed back to `true`.

# Common Confusions

- **Confusion**: Thinking non-extensible means properties cannot be changed or deleted.
  **Clarification**: Non-extensible only prevents adding new properties. Existing properties can still be changed or deleted (unless further restricted by sealing or freezing).

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.1.1, lines 122-124.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly described in the source text with type and access method.
- Cross-reference status: verified against Ch 11 (object protection)
