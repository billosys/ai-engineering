---
# === CORE IDENTIFICATION ===
concept: Internal Slots
slug: internal-slots

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
  - "internal state"
  - "[[Slot]]"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - prototype-internal-slot
  - extensible-internal-slot
contrasts_with:
  - property-attributes

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a property descriptor?"
  - "What must I understand before learning about property assignment vs. definition?"
---

# Quick Definition

Internal slots are storage locations within JavaScript objects that are not accessible from JavaScript code, only from operations in the ECMAScript specification. They are identified by names enclosed in double square brackets, e.g., `[[Prototype]]`.

# Core Definition

As described in "Deep JavaScript" Ch 10, the ECMAScript specification defines internal slots as internal state associated with objects used by specification algorithms. Internal slots "are not object properties and they are not inherited." They are allocated when an object is created and "may not be dynamically added to an object." The ECMAScript language "provides no direct way to associate internal slots with an object."

There are two kinds of internal slots:
- **Method slots** for manipulating objects (getting properties, setting properties, etc.)
- **Data slots** that store values

# Prerequisites

No prerequisites — this is a foundational concept for the object model.

# Key Properties

1. Not accessible from JavaScript, only from specification operations
2. Not object properties and not inherited
3. Allocated during object creation; cannot be dynamically added
4. Initial value is `undefined` unless specified otherwise
5. Identified by names in double square brackets `[[ ]]`
6. Come in two kinds: method slots and data slots

# Construction / Recognition

## To Construct/Create:
1. Internal slots are created automatically by the JavaScript engine during object creation
2. They cannot be created by user code

## To Identify/Recognize:
1. Look for double-bracket notation `[[ ]]` in specification text
2. They represent engine-internal state, not user-facing properties

# Context & Application

Internal slots are essential for understanding how JavaScript objects work at the specification level. Ordinary objects have data slots like `[[Prototype]]`, `[[Extensible]]`, and `[[PrivateFieldValues]]`. Understanding internal slots is a prerequisite for understanding property attributes, property descriptors, and object protection mechanisms.

# Examples

**Example 1** (Ch 10): Ordinary objects have these data slots:
- `.[[Prototype]]: null | object` — the prototype, accessible via `Object.getPrototypeOf()`
- `.[[Extensible]]: boolean` — whether properties can be added, settable via `Object.preventExtensions()`
- `.[[PrivateFieldValues]]: EntryList` — manages private class fields

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **property-attributes** — understanding internal slots provides context for how property attributes work at the spec level
- **prototype-internal-slot** — `[[Prototype]]` is a specific internal slot
- **extensible-internal-slot** — `[[Extensible]]` is a specific internal slot

## Related
- **property-key** — properties are the user-facing counterpart to internal slots

## Contrasts With
- **property-attributes** — properties are accessible from JavaScript; internal slots are not

# Common Errors

- **Error**: Attempting to access internal slots directly from JavaScript code.
  **Correction**: Use the corresponding API methods (e.g., `Object.getPrototypeOf()` for `[[Prototype]]`).

# Common Confusions

- **Confusion**: Internal slots are the same as properties.
  **Clarification**: Internal slots are not object properties, are not inherited, and cannot be accessed from JavaScript. They exist only in the specification's model of objects.

# Source Reference

Chapter 10: Property attributes: an introduction, Section 10.1.1, lines 84-128.

# Verification Notes

- Definition source: direct (quoted from specification via the book)
- Confidence rationale: The book directly quotes and explains the ECMAScript specification's description of internal slots.
- Cross-reference status: verified against Ch 10 text
