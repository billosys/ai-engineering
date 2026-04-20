---
# === CORE IDENTIFICATION ===
concept: Type Coercion
slug: type-coercion

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
section: "2.1 What is type coercion?"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - implicit type conversion
  - coercion

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - explicit-type-conversion
  - to-primitive
  - to-number
  - to-string
  - to-boolean
contrasts_with:
  - explicit-type-conversion
  - type-casting

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion in JavaScript?"
---

# Quick Definition

Type coercion is implicit type conversion where an operation automatically converts its arguments to the types it needs.

# Core Definition

As defined in "Deep JavaScript" (Ch 2, Section 2.1): "Each operation (function, operator, etc.) expects its parameters to have certain types." When a value does not have the right type, the function can convert its arguments to useful values. "In (3), the operation performs an implicit type conversion. That is called *type coercion*." JavaScript uses coercion extensively because "JavaScript initially didn't have exceptions, which is why it uses coercion and error values for most of its operations."

# Prerequisites

- **JavaScript types** — Understanding of primitive types (string, number, boolean, etc.) is needed to understand conversions between them.

# Key Properties

1. Coercion is **implicit** — the operation triggers the conversion, not the programmer explicitly.
2. Coercion can be **checked** (throwing exceptions) or **unchecked** (returning error values like `NaN`).
3. JavaScript uses coercion heavily due to its history of lacking exceptions.
4. Modern JavaScript features tend to throw `TypeError` instead of coercing (e.g., symbols, bigint mixing).

# Construction / Recognition

## To Construct/Create:
1. Pass a value of one type where another type is expected by an operator or function.
2. The operator/function automatically converts the value.

## To Identify/Recognize:
1. An operation accepts a value of a type it does not expect.
2. Instead of throwing an error, it converts the value and proceeds.

# Context & Application

Type coercion is pervasive in JavaScript and affects how operators like `+`, `*`, `==`, and built-in functions behave when given unexpected types. Understanding coercion is essential for avoiding subtle bugs, especially with the `==` operator and the `+` operator.

# Examples

**Example 1** (Ch 2): Coercion in multiplication:
```js
// Coercion
assert.equal(3 * true, 3);

// Error values
assert.equal(1 / 0, Infinity);
assert.equal(Number('xyz'), NaN);
```

**Example 2** (Ch 2): Explicit conversion vs. implicit coercion:
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
- **JavaScript types** — Coercion moves values between types.

## Enables
- **ToPrimitive** — The primary intermediate step for object-to-primitive coercion.
- **Abstract Equality Comparison** — The `==` operator relies heavily on coercion.
- **Addition Operator coercion** — The `+` operator uses coercion to decide between concatenation and addition.

## Related
- **Explicit type conversion** — The programmer-initiated counterpart to coercion.
- **ToString** — Spec algorithm for coercing to strings.
- **ToNumber** — Spec algorithm for coercing to numbers.

## Contrasts With
- **Explicit type conversion** — Programmer triggers conversion intentionally vs. operation triggers it implicitly.
- **Type casting** — Language-dependent; in Java, it means explicit checked type conversion.

# Common Errors

- **Error**: Assuming `==` only compares values without conversion.
  **Correction**: `==` performs extensive type coercion; use `===` for strict comparison without coercion.

- **Error**: Assuming `+` always adds numbers.
  **Correction**: If either operand coerces to a string, `+` performs string concatenation.

# Common Confusions

- **Confusion**: Type coercion and explicit type conversion are the same thing.
  **Clarification**: Coercion is *implicit* (triggered by an operation), while explicit conversion is triggered deliberately by the programmer using functions like `Number()` or `String()`.

# Source Reference

Chapter 2: Type coercion in JavaScript, Sections 2.1 and 2.6, lines 496-1063.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition provided in Section 2.1 and glossary in Section 2.6
- Cross-reference status: verified against ECMAScript specification references in source
