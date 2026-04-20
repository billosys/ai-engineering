---
# === CORE IDENTIFICATION ===
concept: Array.isArray()
slug: array-isarray

# === CLASSIFICATION ===
category: arrays
subcategory: array methods
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Arrays"
chapter_number: 7
pdf_page: 194
section: "7.8.8 Static Array Functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
extends: []
related:
  - array-like-objects
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I test whether a value is an array?"
---

# Quick Definition

`Array.isArray()` is a static method that returns `true` if its argument is an array, `false` otherwise -- the definitive way to test for arrays in JavaScript.

# Core Definition

"The one other static array function is Array.isArray(), which is useful for determining whether an unknown value is an array or not." (Flanagan, p. 194)

# Prerequisites

- **array-fundamentals** — Must understand arrays

# Key Properties

1. Static method on Array (not an instance method)
2. Returns true only for true arrays
3. Returns false for array-like objects
4. More reliable than typeof (which returns "object" for arrays)

# Construction / Recognition

```javascript
Array.isArray(value)
```

# Context & Application

Use when you need to distinguish true arrays from array-like objects or other object types.

# Examples

```javascript
Array.isArray([])   // => true
Array.isArray({})   // => false
```
(Flanagan, p. 194)

# Relationships

## Builds Upon
- **array-fundamentals** — Tests for array type

## Enables
- Type checking and validation

## Related
- **array-like-objects** — Returns false for array-like objects

## Contrasts With
- None specific

# Common Errors

- **Error**: Using `typeof` to check for arrays.
  **Correction**: `typeof []` returns "object". Use Array.isArray() instead.

# Common Confusions

- **Confusion**: Array.isArray() returns true for array-like objects.
  **Clarification**: It returns true only for actual arrays, not array-like objects.

# Source Reference

Chapter 7: Arrays, Section 7.8.8, page 194.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Simple, clearly stated
- Uncertainties: None
- Cross-reference status: Verified
