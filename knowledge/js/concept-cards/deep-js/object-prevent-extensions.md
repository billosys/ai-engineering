---
# === CORE IDENTIFICATION ===
concept: Object.preventExtensions()
slug: object-prevent-extensions

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
section: "11.2 Preventing extensions of objects"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "preventExtensions"
  - "preventing extensions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - extensible-internal-slot
  - property-attributes
extends: []
related:
  - object-is-extensible
contrasts_with:
  - object-seal
  - object-freeze

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Object.preventExtensions() from Object.seal() from Object.freeze()?"
---

# Quick Definition

`Object.preventExtensions(obj)` makes it impossible to add new properties to `obj`, but existing properties can still be changed and deleted. It is the weakest level of object protection.

# Core Definition

As described in "Deep JavaScript" Ch 11, `Object.preventExtensions()` has the signature `<T>(obj: T): T`. "If `obj` is not an object, it returns it. Otherwise, it changes `obj` so that we can't add properties anymore and returns it." This sets the `[[Extensible]]` internal slot to `false`.

# Prerequisites

- **[[Extensible]] Internal Slot** — this method sets it to `false`
- **Property Attributes** — understanding what can still be changed

# Key Properties

1. Prevents adding new properties
2. Existing properties can still be changed (values, attributes)
3. Existing properties can still be deleted
4. Returns the object passed to it
5. Irreversible
6. Non-objects are returned as-is (no error)

# Construction / Recognition

## To Construct/Create:
1. `Object.preventExtensions(obj)`

## To Identify/Recognize:
1. `Object.isExtensible(obj)` returns `false`

# Context & Application

Preventing extensions is the weakest protection level. It is used when you want to prevent new properties from being added but still allow modification of existing properties.

# Examples

**Example 1** (Ch 11):
```js
const obj = { first: 'Jane' };
Object.preventExtensions(obj);
assert.throws(
  () => obj.last = 'Doe',
  /^TypeError: Cannot add property last, object is not extensible$/);
// Can still delete:
delete obj.first;
assert.deepEqual(Object.keys(obj), []);
```

# Relationships

## Builds Upon
- **extensible-internal-slot** — sets `[[Extensible]]` to `false`

## Enables
- **object-seal** — sealing includes preventing extensions
- **object-freeze** — freezing includes preventing extensions

## Related
- **object-is-extensible** — checks whether an object is extensible

## Contrasts With
- **object-seal** — seal also makes all properties unconfigurable
- **object-freeze** — freeze also makes all properties non-writable and unconfigurable

# Common Errors

- **Error**: Expecting `preventExtensions` to prevent property deletion.
  **Correction**: It only prevents adding new properties. Existing properties can still be deleted.

# Common Confusions

- **Confusion**: Thinking non-extensible means immutable.
  **Clarification**: Non-extensible only prevents adding new properties. Existing property values can still be changed, and properties can be deleted.

# Source Reference

Chapter 11: Protecting objects from being changed, Section 11.2, lines 64-97.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with API signature and examples.
- Cross-reference status: verified
