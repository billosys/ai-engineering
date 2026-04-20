---
# === CORE IDENTIFICATION ===
concept: Boolean Type
slug: boolean-type

# === CLASSIFICATION ===
category: type-system
subcategory: primitive-types
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 55
section: "3.4 Boolean Values"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Boolean
  - bool

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primitive-vs-object-types
extends: []
related:
  - boolean-truthy-falsy
  - type-coercion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion in JavaScript?"
---

# Quick Definition

The Boolean type has exactly two values — `true` and `false` — representing truth and falsehood, and is the result type of comparison operators and the expected type for control structure conditions.

# Core Definition

"A boolean value represents truth or falsehood, on or off, yes or no. There are only two possible values of this type. The reserved words true and false evaluate to these two values." "Boolean values are generally the result of comparisons you make in your JavaScript programs." Three important boolean operators: `&&` (AND), `||` (OR), `!` (NOT). (pp. 55-57)

# Prerequisites

- **primitive-vs-object-types** — Boolean is a primitive type

# Key Properties

1. Only two values: `true` and `false`
2. Result of comparison operators (`===`, `!==`, `<`, `>`, `<=`, `>=`)
3. Used in control structures (if/else, while, for)
4. Boolean operators: `&&` (AND), `||` (OR), `!` (NOT)
5. Any JavaScript value can be converted to boolean (truthy/falsy)
6. `toString()` converts to "true" or "false"

# Construction / Recognition

```javascript
let b = true;
let result = (a === 4);    // boolean from comparison
```

# Context & Application

Booleans are the foundation of conditional logic in JavaScript. They control program flow through if/else, while, and for statements. Understanding truthy/falsy values is essential because JavaScript automatically converts other types to boolean in conditional contexts.

# Examples

From the source text (pp. 55-57):
```javascript
a === 4                     // Tests if a equals 4; result is true or false

if (a === 4) {
    b = b + 1;
} else {
    a = a + 1;
}

// Boolean operators
(x === 0 && y === 0) || !(z === 0)
// x and y are both zero or z is non-zero
```

# Relationships

## Builds Upon
- **primitive-vs-object-types** — Boolean is a primitive type

## Enables
- **boolean-truthy-falsy** — Any value can behave as boolean
- Control structures (if/else, while)

## Related
- **type-coercion** — Other types convert to boolean in conditional contexts

## Contrasts With
- None within this source

# Common Errors

- **Error**: Using `=` instead of `===` in conditions.
  **Correction**: `=` is assignment, not comparison. Use `===` for equality testing.

# Common Confusions

- **Confusion**: Only boolean values can be used in if statements.
  **Clarification**: Any JavaScript value can be used where a boolean is expected — truthy values work like true, falsy values like false.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.4, pages 55-57.

# Verification Notes

- Definition source: Direct quotes from pp. 55-57
- Confidence rationale: High — clearly defined
- Uncertainties: None
- Cross-reference status: Verified
