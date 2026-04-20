---
# === CORE IDENTIFICATION ===
concept: Explicit Type Conversion
slug: explicit-type-conversion

# === CLASSIFICATION ===
category: types-values
subcategory: type-conversion
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Values"
chapter_number: 14
pdf_page: null
section: "14.9.1 Explicit conversion between types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - type casting
  - manual type conversion

# === TYPED RELATIONSHIPS ===
prerequisites:
  - specification-types
  - constructor-functions
extends: []
related:
  - type-coercion
contrasts_with:
  - type-coercion

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the `typeof` operator and what does it return for each type?"
---

# Quick Definition

Explicit type conversion uses functions like `Boolean()`, `Number()`, `String()`, and `Object()` to intentionally convert values from one type to another.

# Core Definition

"The function associated with a primitive type explicitly converts values to that type." (Ch. 14, &sect;14.9.1). The constructor functions serve as conversion functions when called without `new`: `Boolean(0)` returns `false`, `Number('123')` returns `123`, `String(123)` returns `'123'`. `Object()` converts primitives to wrapper objects.

# Prerequisites

- **specification-types** -- conversions between the spec types
- **constructor-functions** -- constructor functions serve as converters

# Key Properties

1. `Boolean()`: converts to boolean
2. `Number()`: converts to number
3. `String()`: converts to string
4. `Object()`: converts to object (wrapping primitives)
5. Called WITHOUT `new` for conversion (with `new` creates wrapper objects)

# Construction / Recognition

```js
Boolean(0)      // false
Number('123')   // 123
String(123)     // '123'
Object(123)     // Number wrapper object
```

# Context & Application

Explicit conversion is the recommended way to convert between types, as opposed to relying on implicit coercion.

# Examples

From the source text (Ch. 14, &sect;14.9.1):
```js
> Boolean(0)
false
> Number('123')
123
> String(123)
'123'
> typeof Object(123)
'object'
```

# Relationships

## Builds Upon
- **specification-types** -- converting between spec types
- **constructor-functions** -- use constructor functions as converters

## Enables
- Intentional, readable type conversions

## Related
- No additional

## Contrasts With
- **type-coercion** -- automatic, implicit conversion

# Common Errors

- **Error**: Using `new Number('123')` instead of `Number('123')`.
  **Correction**: Without `new`, you get a primitive number. With `new`, you get a wrapper object.

# Common Confusions

- **Confusion**: Not knowing the difference between explicit conversion and coercion.
  **Clarification**: Explicit conversion is intentional (calling `Number()`); coercion is automatic (operators converting operands).

# Source Reference

Chapter 14: Values, Section 14.9.1, lines 747-887.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit with examples for each converter
- Cross-reference status: verified
