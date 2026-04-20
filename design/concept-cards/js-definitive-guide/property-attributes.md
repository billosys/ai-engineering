---
# === CORE IDENTIFICATION ===
concept: Property Attributes
slug: property-attributes

# === CLASSIFICATION ===
category: objects
subcategory: property-system
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Objects"
chapter_number: 6
pdf_page: 147
section: "6.1 Introduction to Objects"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "property descriptors"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - objects-as-property-collections
extends: []
related:
  - deleting-properties
  - enumerating-properties
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do property descriptors relate to Object.freeze()?"
---

# Quick Definition

Each JavaScript property has three attributes beyond its name and value: *writable* (can the value be changed), *enumerable* (is it returned by for/in), and *configurable* (can it be deleted or have its attributes altered).

# Core Definition

"In addition to its name and value, each property has three *property attributes*: The *writable* attribute specifies whether the value of the property can be set. The *enumerable* attribute specifies whether the property name is returned by a for/in loop. The *configurable* attribute specifies whether the property can be deleted and whether its attributes can be altered." (Ch. 6, §6.1)

# Prerequisites

- **objects-as-property-collections** — Properties exist on objects; attributes describe their behavior.

# Key Properties

1. **writable**: whether the value can be set. Read-only if false.
2. **enumerable**: whether the property appears in for/in and Object.keys().
3. **configurable**: whether the property can be deleted and whether attributes can be changed.
4. Built-in properties are typically read-only, non-enumerable, or non-configurable.
5. User-created properties are writable, enumerable, and configurable by default.
6. Techniques for setting non-default attributes are in §14.1.

# Construction / Recognition

Property attributes are not visible in normal code but are manipulated via `Object.defineProperty()` and inspected via `Object.getOwnPropertyDescriptor()` (covered in §14.1).

# Context & Application

Property attributes control the mutability and visibility of properties. They are the mechanism behind `Object.freeze()`, `Object.seal()`, and non-enumerable built-in methods. Understanding them is essential for advanced object manipulation.

# Examples

From the source text (§6.1, p. 147):

```js
// Built-in properties are non-enumerable
let o = {x: 1, y: 2, z: 3};
o.propertyIsEnumerable("toString") // => false: inherited, not enumerable

// User-defined properties are enumerable by default
o.propertyIsEnumerable("x")       // => true
```

# Relationships

## Builds Upon
- **objects-as-property-collections** — Attributes are metadata about properties

## Enables
- **deleting-properties** — `configurable` controls whether `delete` works
- **enumerating-properties** — `enumerable` controls whether properties appear in for/in

## Related
- `Object.freeze()` and `Object.seal()` work by modifying property attributes

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Attempting to delete a non-configurable property (silently fails in non-strict mode).
  **Correction**: In strict mode, this throws TypeError. Check configurability before attempting deletion.

# Common Confusions

- **Confusion**: Believing all properties behave the same way.
  **Clarification**: Built-in properties are often non-writable, non-enumerable, or non-configurable, which is why they don't appear in for/in loops or can't be deleted.

# Source Reference

Chapter 6: Objects, Section 6.1, page 147; details in §14.1.

# Verification Notes

- Definition source: Direct quote from §6.1
- Confidence rationale: High — clearly enumerated attributes
- Uncertainties: Full API for setting attributes is in §14.1 (outside scope)
- Cross-reference status: Verified against §6.4, §6.6
