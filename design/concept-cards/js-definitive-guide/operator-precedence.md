---
# === CORE IDENTIFICATION ===
concept: Operator Precedence
slug: operator-precedence

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
pdf_page: 86
section: "4.7 Operator Overview"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "operator priority"
  - "operator associativity"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primary-expressions
extends: []
related:
  - addition-operator
  - short-circuit-evaluation
  - nullish-coalescing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

Operator precedence determines the order in which operators are evaluated in complex expressions, while associativity determines the order among operators of equal precedence.

# Core Definition

"Operator precedence controls the order in which operations are performed. Operators with higher precedence (nearer the top of the table) are performed before those with lower precedence (nearer to the bottom)." Associativity specifies order among same-precedence operators: left-to-right (L) or right-to-left (R). (Ch. 4, §4.7.4-4.7.5)

# Prerequisites

- **primary-expressions** — Precedence governs how primary expressions combine with operators.

# Key Properties

1. Property access and invocation have higher precedence than any listed operator.
2. Multiplication/division precede addition/subtraction; assignment has very low precedence.
3. Right-to-left associativity: exponentiation (`**`), unary operators, assignment (`=`), and ternary (`?:`).
4. Left-to-right associativity: most binary operators including arithmetic, comparison, and logical.
5. `??` has undefined precedence relative to `||` and `&&` — parentheses are required when mixing them.
6. Subexpressions are always evaluated left-to-right regardless of precedence.

# Construction / Recognition

```js
w = x + y * z;      // * before +, then =
w = (x + y) * z;    // Parentheses override precedence
typeof my.functions[x](y)  // Property access, index, invocation all before typeof
```

# Context & Application

Understanding precedence is essential for writing correct expressions without excessive parentheses and for reading others' code. When unsure, use parentheses to make evaluation order explicit.

# Examples

From the source text (§4.7.4-4.7.6, pp. 88-90):

```js
w = x + y*z;        // Multiplication before addition
w = (x + y)*z;      // Parentheses override

// Right-to-left associativity
y = a ** b ** c;     // Same as y = a ** (b ** c)
w = x = y = z;       // Same as w = (x = (y = z))
q = a?b:c?d:e?f:g;  // Same as q = a?b:(c?d:(e?f:g))

// Left-to-right associativity
w = x - y - z;       // Same as w = ((x - y) - z)
```

# Relationships

## Builds Upon
- **primary-expressions** — Precedence governs how simple expressions compose via operators

## Enables
- Understanding of all compound expressions in JavaScript

## Related
- **addition-operator** — Precedence determines when `+` is evaluated relative to other operators
- **short-circuit-evaluation** — Logical operators have specific precedence levels
- **nullish-coalescing** — Requires explicit parentheses when mixed with `||` or `&&`

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Mixing `??` with `||` or `&&` without parentheses.
  **Correction**: ES2020 requires explicit parentheses: `(a ?? b) || c` or `a ?? (b || c)`.

# Common Confusions

- **Confusion**: Believing precedence determines the order in which subexpressions are *evaluated*.
  **Clarification**: Subexpressions are always evaluated left-to-right. Precedence only determines how operators *group* their operands.

# Source Reference

Chapter 4: Expressions and Operators, Sections 4.7.1-4.7.6, pages 86-90.

# Verification Notes

- Definition source: Synthesized from §4.7.4 and §4.7.5
- Confidence rationale: High — detailed table and explanation in source
- Uncertainties: None
- Cross-reference status: Verified
