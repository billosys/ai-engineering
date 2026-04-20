---
# === CORE IDENTIFICATION ===
concept: Type Coercion (Implicit Conversion)
slug: type-coercion

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
pdf_page: 62
section: "3.9 Type Conversions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - implicit type conversion
  - automatic type conversion
  - type conversion

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primitive-vs-object-types
  - boolean-truthy-falsy
  - number-type
  - string-type
extends: []
related:
  - strict-vs-loose-equality
  - explicit-type-conversion
  - object-to-primitive-conversion
contrasts_with:
  - explicit-type-conversion

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion in JavaScript?"
  - "What distinguishes `==` from `===`?"
  - "What must I understand before learning about closures?"
---

# Quick Definition

Type coercion is JavaScript's automatic conversion of values from one type to another when a different type is expected, such as converting a number to a string for concatenation or any value to boolean for a conditional test.

# Core Definition

"JavaScript is very flexible about the types of values it requires." "When JavaScript expects a boolean value, you may supply a value of any type, and JavaScript will convert it as needed." "If JavaScript wants a string, it will convert whatever value you give it to a string. If JavaScript wants a number, it will try to convert the value you give it to a number (or to NaN if it cannot perform a meaningful conversion)." Table 3-2 provides the complete conversion rules. (pp. 62-63)

# Prerequisites

- **primitive-vs-object-types** — Must understand what types exist
- **boolean-truthy-falsy** — Boolean coercion is a key part of type coercion
- **number-type** — Understanding numeric conversion targets
- **string-type** — Understanding string conversion targets

# Key Properties

Key conversion rules from Table 3-2:

**To Boolean:**
- `undefined`, `null`, `0`, `-0`, `NaN`, `""` → `false`
- All other values → `true` (including all objects)

**To Number:**
- `undefined` → `NaN`
- `null` → `0`
- `true` → `1`, `false` → `0`
- `""` → `0`
- Numeric strings → their numeric value
- Non-numeric strings → `NaN`
- `[]` → `0`, `[9]` → `9`, other arrays → `NaN`

**To String:**
- `undefined` → `"undefined"`
- `null` → `"null"`
- `true` → `"true"`, `false` → `"false"`
- Numbers → their string representation (`-0` → `"0"`)
- `[]` → `""`, `[9]` → `"9"`

# Construction / Recognition

```javascript
10 + " objects"       // => "10 objects": Number 10 converts to string
"7" * "4"             // => 28: both strings convert to numbers
let n = 1 - "x";     // n == NaN: string "x" can't convert to a number
n + " objects"        // => "NaN objects": NaN converts to string "NaN"
```

# Context & Application

Type coercion is one of JavaScript's most distinctive and controversial features. It enables concise code but can cause subtle bugs. Understanding coercion rules is essential for predicting the behavior of operators and built-in functions, and for understanding why `===` is preferred over `==`.

# Examples

From the source text (pp. 62-63):
```javascript
10 + " objects"       // => "10 objects": Number 10 converts to a string
"7" * "4"             // => 28: both strings convert to numbers
let n = 1 - "x";     // n == NaN; string "x" can't convert to a number
n + " objects"        // => "NaN objects": NaN converts to string "NaN"
```

Surprising conversions from Table 3-2:
- `-0` to string → `"0"` (not `"-0"`)
- `null` to number → `0` (not NaN)
- `[]` (empty array) to number → `0`
- `[9]` (single-element array) to number → `9`

# Relationships

## Builds Upon
- **primitive-vs-object-types** — Coercion converts between types
- **boolean-truthy-falsy** — Boolean coercion follows truthy/falsy rules

## Enables
- **strict-vs-loose-equality** — `==` uses type coercion; `===` does not
- **object-to-primitive-conversion** — How objects participate in coercion

## Related
- **explicit-type-conversion** — Deliberate use of conversion functions

## Contrasts With
- **explicit-type-conversion** — Implicit vs deliberate conversion

# Common Errors

- **Error**: Assuming `+` always performs addition.
  **Correction**: If either operand is a string, `+` concatenates. `1 + "2"` produces `"12"`, not `3`.

- **Error**: Assuming `null` converts to `NaN` like `undefined`.
  **Correction**: `null` converts to `0`; `undefined` converts to `NaN`.

# Common Confusions

- **Confusion**: Type coercion only happens with `==`.
  **Clarification**: Coercion happens with many operators (+, -, *, /) and in boolean contexts (if, while), not just `==`.

- **Confusion**: "Convertibility of one value to another implies equality."
  **Clarification**: "undefined converts to false in boolean context, but undefined == false is false. The == operator never attempts to convert its operands to booleans" (p. 63).

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.9, pages 62-63. Table 3-2.

# Verification Notes

- Definition source: Direct quotes from pp. 62-63
- Confidence rationale: High — thorough treatment with complete conversion table
- Uncertainties: None
- Cross-reference status: Verified
