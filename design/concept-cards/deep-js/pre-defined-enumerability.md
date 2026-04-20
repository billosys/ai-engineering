---
# === CORE IDENTIFICATION ===
concept: Pre-defined Property Enumerability
slug: pre-defined-enumerability

# === CLASSIFICATION ===
category: object-model
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Enumerability of properties"
chapter_number: 13
section: "13.2 The enumerability of pre-defined and created properties"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - enumerability
  - built-in-property-attributes
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is enumerability?"
---

# Quick Definition

Most user-created data properties are enumerable (via assignment, object literals, class fields, `Object.fromEntries()`). The most important non-enumerable properties are prototype properties of built-in and user-defined classes, and special properties like Array `.length`.

# Core Definition

As described in "Deep JavaScript" Ch 13, most data properties are created with `enumerable: true` (via assignment, object literals, public class fields, `Object.fromEntries()`). Non-enumerable properties include:
- Prototype properties of built-in classes (e.g., `Object.prototype.toString`)
- Prototype properties of user-defined classes
- Array `.length` (writable but non-enumerable and non-configurable)
- String `.length` (read-only, non-enumerable, non-configurable)

# Prerequisites

- **Enumerability** — this describes the default enumerability of various constructs
- **Built-in Property Attributes** — overlapping content from Ch 10

# Key Properties

1. Assignment, object literals, class fields: enumerable
2. Built-in prototype methods: non-enumerable
3. User-defined class methods: non-enumerable
4. Array/String `.length`: non-enumerable
5. Properties from `Object.defineProperty()` without explicit `enumerable`: non-enumerable

# Construction / Recognition

## To Construct/Create:
1. Not applicable — this describes default behavior

## To Identify/Recognize:
1. Check `Object.getOwnPropertyDescriptor(obj, key).enumerable`

# Context & Application

This knowledge explains why `Object.keys()` and `for-in` work as expected in most cases: own properties you create are enumerable, while inherited methods are non-enumerable, creating a natural and useful division.

# Examples

**Example 1** (Ch 13): Built-in prototype methods are non-enumerable:
```js
> Object.getOwnPropertyDescriptor(Object.prototype, 'toString').enumerable
false
```

**Example 2** (Ch 13): User-defined class methods are non-enumerable:
```js
> Object.getOwnPropertyDescriptor(class {foo() {}}.prototype, 'foo').enumerable
false
```

# Relationships

## Builds Upon
- **enumerability** — this describes default enumerability patterns
- **built-in-property-attributes** — overlapping content

## Enables
- Understanding why `Object.keys()` typically shows exactly what you want

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Assuming properties created via `Object.defineProperty()` are enumerable.
  **Correction**: Without explicit `enumerable: true`, defined properties default to non-enumerable.

# Common Confusions

- **Confusion**: Wondering why class methods don't appear in `Object.keys()`.
  **Clarification**: Class prototype methods are non-enumerable by design, hiding them from `Object.keys()` and `for-in`.

# Source Reference

Chapter 13: Enumerability of properties, Section 13.2, lines 303-362.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly listed with examples for each category.
- Cross-reference status: verified against Ch 10 (built-in property attributes)
