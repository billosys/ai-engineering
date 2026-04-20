---
# === CORE IDENTIFICATION ===
concept: Protection Levels
slug: protection-levels

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
section: "11.1 Levels of protection"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "object protection levels"
  - "immutability levels"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-attributes
  - configurable-attribute
  - writable-attribute
  - extensible-internal-slot
extends: []
related:
  - object-prevent-extensions
  - object-seal
  - object-freeze
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Object.preventExtensions() from Object.seal() from Object.freeze()?"
  - "How do property attributes relate to Object.freeze()?"
---

# Quick Definition

JavaScript provides three increasingly strict levels of object protection: preventing extensions (no new properties), sealing (no new properties + all properties unconfigurable), and freezing (no new properties + all properties unconfigurable and non-writable).

# Core Definition

As described in "Deep JavaScript" Ch 11, "JavaScript has three levels of protecting objects:
- *Preventing extensions* makes it impossible to add new properties to an object. We can still delete and change properties, though.
- *Sealing* prevents extensions and makes all properties *unconfigurable* (roughly: we can't change how a property works anymore).
- *Freezing* seals an object after making all of its properties non-writable. That is, the object is not extensible, all properties are read-only and there is no way to change that."

# Prerequisites

- **Property Attributes** — protection levels manipulate property attributes
- **Configurable Attribute** — sealing sets configurable to false
- **Writable Attribute** — freezing sets writable to false
- **[[Extensible]] Internal Slot** — all levels set extensible to false

# Key Properties

1. Three levels: preventExtensions < seal < freeze (each includes the previous)
2. All three are irreversible
3. Preventing extensions: only blocks adding new properties
4. Sealing: adds non-configurable to all properties
5. Freezing: adds non-writable to all data properties (on top of sealing)
6. All operate only on own properties (shallow)

# Construction / Recognition

## To Construct/Create:
1. `Object.preventExtensions(obj)` — weakest protection
2. `Object.seal(obj)` — medium protection
3. `Object.freeze(obj)` — strongest protection

## To Identify/Recognize:
1. `Object.isExtensible(obj)` — false for all three levels
2. `Object.isSealed(obj)` — true for sealed and frozen
3. `Object.isFrozen(obj)` — true only for frozen

# Context & Application

These protection levels are used to create varying degrees of immutability. Freezing is the strongest built-in mechanism for making objects immutable, but it is shallow — nested objects are not affected.

# Examples

**Example 1** (Ch 11): Frozen objects are fully protected:
```js
const point = { x: 17, y: -5 };
Object.freeze(point);
assert.throws(
  () => point.x = 2,
  /^TypeError: Cannot assign to read only property 'x'/);
assert.throws(
  () => point.z = 4,
  /^TypeError: Cannot add property z, object is not extensible$/);
```

# Relationships

## Builds Upon
- **property-attributes** — each level manipulates specific attributes
- **extensible-internal-slot** — all levels set `[[Extensible]]` to `false`

## Enables
- Understanding of object immutability patterns in JavaScript

## Related
- **object-prevent-extensions** — the weakest level
- **object-seal** — the medium level
- **object-freeze** — the strongest level

## Contrasts With
- None

# Common Errors

- **Error**: Expecting to "unfreeze" or "unseal" an object.
  **Correction**: All three protection levels are irreversible.

# Common Confusions

- **Confusion**: Thinking freeze makes an object deeply immutable.
  **Clarification**: Freezing is shallow — it only affects the object's own properties, not the values those properties reference.

# Source Reference

Chapter 11: Protecting objects from being changed, Section 11.1, lines 47-62.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with three-level hierarchy.
- Cross-reference status: verified
