---
# === CORE IDENTIFICATION ===
concept: The + Operator (Addition and Concatenation)
slug: addition-operator

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: operators
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Expressions and Operators"
chapter_number: 4
pdf_page: 91
section: "4.8.1 The + Operator"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "addition operator"
  - "string concatenation operator"
  - "plus operator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primary-expressions
  - operator-precedence
extends: []
related:
  - comparison-operators
  - compound-assignment-operators
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes == from ===? (operator side)"
---

# Quick Definition

The binary `+` operator adds numeric operands or concatenates string operands. When operand types are mixed, it gives priority to string concatenation.

# Core Definition

"The binary + operator adds numeric operands or concatenates string operands... The conversion rules for + give priority to string concatenation: if either of the operands is a string or an object that converts to a string, the other operand is converted to a string and concatenation is performed. Addition is performed only if neither operand is string-like." (Ch. 4, §4.8.1)

# Prerequisites

- **primary-expressions** — The operands of `+` are expressions.
- **operator-precedence** — `+` has specific precedence below `*`, `/`, `%`.

# Key Properties

1. If either operand is a string, the other is converted to string and concatenation is performed.
2. Objects are converted to primitives: Date via `toString()`, others via `valueOf()` first.
3. If neither operand is string-like, both are converted to numbers and added.
4. `+` is not associative with mixed types: `1 + 2 + " blind mice"` differs from `1 + (2 + " blind mice")`.
5. `true + true` evaluates to `2` (boolean-to-number conversion).
6. `2 + null` evaluates to `2` (null converts to 0); `2 + undefined` evaluates to `NaN`.

# Construction / Recognition

```js
number + number    // Numeric addition
string + anything  // String concatenation
```

# Context & Application

The `+` operator is one of the most frequently used operators in JavaScript. Its dual behavior (addition vs. concatenation) based on operand types is a common source of bugs, especially when mixing types.

# Examples

From the source text (§4.8.1, pp. 91-92):

```js
1 + 2           // => 3: addition
"1" + "2"       // => "12": concatenation
"1" + 2         // => "12": concatenation after number-to-string
1 + {}          // => "1[object Object]": concatenation after object-to-string
true + true     // => 2: addition after boolean-to-number
2 + null        // => 2: addition after null converts to 0
2 + undefined   // => NaN: addition after undefined converts to NaN

1 + 2 + " blind mice"    // => "3 blind mice"
1 + (2 + " blind mice")  // => "12 blind mice"
```

# Relationships

## Builds Upon
- **operator-precedence** — `+` has lower precedence than `*`, `/`, `%`

## Enables
- **compound-assignment-operators** — `+=` combines addition/concatenation with assignment

## Related
- **comparison-operators** — Comparison operators favor numbers; `+` favors strings

## Contrasts With
- No specific contrast, but behavior differs markedly from comparison operators on type conversion

# Common Errors

- **Error**: Expecting `"1" + 2` to produce `3`.
  **Correction**: If either operand is a string, concatenation occurs. Result is `"12"`. Use `Number("1") + 2` for addition.

- **Error**: Relying on left-to-right associativity with mixed types.
  **Correction**: `1 + 2 + "3"` produces `"33"`, not `"123"`, because `1 + 2` is evaluated first as `3`.

# Common Confusions

- **Confusion**: Believing `+` always performs addition if one operand is a number.
  **Clarification**: String concatenation takes priority. If either operand is a string (or converts to a string), the other is converted to a string and concatenated.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.8.1, pages 91-92.

# Verification Notes

- Definition source: Direct quote from §4.8.1
- Confidence rationale: High — detailed algorithm with multiple examples
- Uncertainties: None
- Cross-reference status: Verified against §3.9.3 type conversion rules
