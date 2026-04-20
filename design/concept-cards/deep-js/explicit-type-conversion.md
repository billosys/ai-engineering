---
# === CORE IDENTIFICATION ===
concept: Explicit Type Conversion
slug: explicit-type-conversion

# === CLASSIFICATION ===
category: type-system
subcategory: type-conversion
tier: foundational

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Type coercion in JavaScript"
chapter_number: 2
section: "2.6 Glossary: terms related to type conversion"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - explicit conversion
  - manual type conversion

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-coercion
extends: []
related:
  - string-function
  - to-number
  - to-boolean
  - type-casting
contrasts_with:
  - type-coercion
  - type-casting

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion in JavaScript?"
---

# Quick Definition

Explicit type conversion is when a programmer deliberately uses an operation (function, operator, etc.) to convert a value from one type to another.

# Core Definition

As defined in "Deep JavaScript" (Ch 2, Section 2.6): "*Explicit type conversion* means that the programmer uses an operation (a function, an operator, etc.) to trigger a type conversion. Explicit conversions can be: *Checked*: If a value can't be converted, an exception is thrown. *Unchecked*: If a value can't be converted, an error value is returned."

# Prerequisites

- **Type coercion** — Understanding explicit conversion requires contrasting it with implicit coercion.

# Key Properties

1. Triggered deliberately by the programmer.
2. Can be **checked** (throws exception on failure) or **unchecked** (returns error value).
3. Uses functions like `Number()`, `String()`, `Boolean()`.
4. Preferred over implicit coercion for code clarity.

# Construction / Recognition

## To Construct/Create:
1. Call `Number(value)`, `String(value)`, or `Boolean(value)`.
2. Use unary `+` for number conversion.
3. Use `!!` for boolean conversion.

## To Identify/Recognize:
1. The programmer explicitly calls a conversion function or uses a conversion operator.

# Context & Application

The author recommends explicit conversion over relying on coercion: "I usually prefer the former, because it clarifies my intention: I expect `x` and `y` not to be numbers, but want to multiply two numbers." Explicit conversion makes intent clear and avoids surprising coercion behaviors.

# Examples

**Example 1** (Ch 2): Explicit vs. implicit:
```js
let x = '3';
let y = '2';

// Explicit conversion (preferred)
assert.equal(Number(x) * Number(y), 6);

// Implicit coercion
assert.equal(x * y, 6);
```

# Relationships

## Builds Upon
- **Type coercion** — Explicit conversion is the deliberate counterpart.

## Enables
- **Predictable code** — Makes type expectations clear.

## Related
- **String() function** — Primary explicit string conversion.
- **ToNumber** — Underlying algorithm for `Number()`.
- **ToBoolean** — Underlying algorithm for `Boolean()`.

## Contrasts With
- **Type coercion** — Coercion is implicit; explicit conversion is intentional.
- **Type casting** — Language-dependent term; in Java means explicit checked conversion.

# Common Errors

- **Error**: Assuming explicit conversion and coercion always produce the same result.
  **Correction**: They usually do, but `String()` handles symbols while implicit coercion (via `ToString`) throws.

# Common Confusions

- **Confusion**: "Type casting" and "explicit type conversion" are synonymous.
  **Clarification**: The meaning of "type casting" depends on the language. In JavaScript, the term "explicit type conversion" is more precise.

# Source Reference

Chapter 2: Type coercion in JavaScript, Sections 2.1.1 and 2.6, lines 163-188 and 1035-1063.

# Verification Notes

- Definition source: direct (quoted from glossary)
- Confidence rationale: Explicit definition provided in glossary
- Cross-reference status: verified
