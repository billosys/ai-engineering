---
# === CORE IDENTIFICATION ===
concept: Truthy and Falsy Values
slug: boolean-truthy-falsy

# === CLASSIFICATION ===
category: type-system
subcategory: type-coercion
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 56
section: "3.4 Boolean Values"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - falsy values
  - truthy values
  - truthiness

# === TYPED RELATIONSHIPS ===
prerequisites:
  - boolean-type
  - type-system-overview
extends:
  - boolean-type
related:
  - type-coercion
  - null-vs-undefined
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion in JavaScript?"
  - "What must I understand before learning about closures?"
---

# Quick Definition

In JavaScript, every value is either "truthy" (converts to `true` in boolean context) or "falsy" (converts to `false`), with exactly six falsy values: `undefined`, `null`, `0`, `-0`, `NaN`, and `""` (empty string).

# Core Definition

"Any JavaScript value can be converted to a boolean value." The falsy values are: `undefined`, `null`, `0`, `-0`, `NaN`, and `""` (the empty string). "All other values, including all objects (and arrays) convert to, and work like, true. false, and the six values that convert to it, are sometimes called falsy values, and all other values are called truthy." "Any time JavaScript expects a boolean value, a falsy value works like false and a truthy value works like true." (pp. 56-57)

# Prerequisites

- **boolean-type** — Must understand the Boolean type
- **type-system-overview** — Must understand JavaScript's type flexibility

# Key Properties

1. Exactly six falsy values: `undefined`, `null`, `0`, `-0`, `NaN`, `""`
2. `false` itself is also falsy (making seven total including false)
3. ALL objects are truthy — including empty arrays `[]` and empty objects `{}`
4. Even `new Boolean(false)` is truthy (it's an object)
5. Truthy/falsy conversion happens automatically in boolean contexts (if, while, &&, ||, !)
6. Testing with `if (o)` is less strict than `if (o !== null)` — the former catches all falsy values

# Construction / Recognition

```javascript
// All falsy values:
undefined
null
0
-0
NaN
""          // the empty string

// Truthy (some surprising ones):
[]          // empty array — truthy!
{}          // empty object — truthy!
"0"         // non-empty string — truthy!
"false"     // non-empty string — truthy!
```

# Context & Application

Truthy/falsy conversion is one of JavaScript's most frequently used features and one of its most common sources of bugs. It is used in conditional statements, logical operators, and ternary expressions.

# Examples

From the source text (pp. 56-57):
```javascript
// Explicit null check:
if (o !== null) ...

// Truthy/falsy check (less strict):
if (o) ...
// The second case will NOT execute for null, undefined, 0, "", NaN, or false

// Boolean operators use truthy/falsy:
if ((x === 0 && y === 0) || !(z === 0)) {
    // x and y are both zero or z is non-zero
}
```

# Relationships

## Builds Upon
- **boolean-type** — Truthy/falsy extends boolean to all value types

## Enables
- **type-coercion** — Boolean coercion is a key part of type coercion
- **strict-vs-loose-equality** — Understanding why `==` coercion matters

## Related
- **null-vs-undefined** — Both are falsy values
- **type-coercion** — Truthy/falsy is a form of implicit type conversion

## Contrasts With
- None within this source

# Common Errors

- **Error**: Checking `if (value)` when `value` could legitimately be `0` or `""`.
  **Correction**: If `0` or `""` are valid values, use explicit checks: `if (value !== null && value !== undefined)`.

# Common Confusions

- **Confusion**: Empty arrays `[]` are falsy because they have no elements.
  **Clarification**: ALL objects (including empty arrays and empty objects) are truthy. Only the six primitive falsy values convert to false.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.4, pages 56-57.

# Verification Notes

- Definition source: Direct quotes from pp. 56-57
- Confidence rationale: High — complete enumeration of falsy values provided
- Uncertainties: None
- Cross-reference status: Verified
