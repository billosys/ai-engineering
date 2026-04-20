---
# === CORE IDENTIFICATION ===
concept: Operator Precedence
slug: operator-precedence

# === CLASSIFICATION ===
category: fundamentals
subcategory: operators
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Values, Types, and Operators"
chapter_number: 1
pdf_page: null
section: "Arithmetic"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - order of operations

# === TYPED RELATIONSHIPS ===
prerequisites:
  - arithmetic-operator
  - binary-operator
extends: []
related:
  - logical-operators
  - comparison-operators
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a value in JavaScript?"
  - "What must I know before understanding closures?"
---

# Quick Definition

Operator precedence determines the order in which operators are applied when they appear together without parentheses, with multiplication/division before addition/subtraction, and arithmetic before comparison before logical operators.

# Core Definition

As described in "Eloquent JavaScript" (Ch 1, lines 204-210 of 01-values-types-and-operators.md): "When operators appear together without parentheses, the order in which they are applied is determined by the *precedence* of the operators. The example shows that multiplication comes before addition. The `/` operator has the same precedence as `*`. Likewise, `+` and `-` have the same precedence. When multiple operators with the same precedence appear next to each other, as in `1 - 2 + 1`, they are applied left to right: `(1 - 2) + 1`."

# Prerequisites

- **Arithmetic Operator** -- Precedence governs how arithmetic operators interact.
- **Binary Operator** -- Precedence applies to expressions with multiple binary operators.

# Key Properties

1. `*`, `/`, `%` have **higher precedence** than `+` and `-` (lines 206-208).
2. Operators with equal precedence are evaluated **left to right** (line 210).
3. **Parentheses override** precedence (lines 192-197).
4. For logical operators: `||` has lowest precedence, then `&&`, then comparison operators, then arithmetic (lines 497-499).
5. "When in doubt, just add parentheses" (line 214).

# Construction / Recognition

## To Identify/Recognize:
1. An expression with multiple operators and no parentheses.
2. The result depends on which operators are applied first.

# Context & Application

Understanding operator precedence prevents surprises in expression evaluation. While parentheses can always make order explicit, knowing the default precedence helps read and write idiomatic JavaScript.

# Examples

**Example 1** (Ch 1, lines 178-179): Multiplication before addition:
```js
100 + 4 * 11  // evaluates as 100 + (4 * 11) = 144
```

**Example 2** (Ch 1, lines 195-197): Parentheses overriding precedence:
```js
(100 + 4) * 11  // evaluates as 1144
```

**Example 3** (Ch 1, lines 503-505): Full precedence chain:
```js
1 + 1 == 2 && 10 * 10 > 50
```
Evaluates as: `((1 + 1) == 2) && ((10 * 10) > 50)`.

# Relationships

## Builds Upon
- **Arithmetic Operator** -- Arithmetic precedence rules are the primary examples.
- **Binary Operator** -- Precedence applies to binary operator chains.

## Enables
- Correct interpretation of complex expressions.

## Related
- **Logical Operators** -- Have their own precedence ranking.
- **Comparison Operators** -- Fall between arithmetic and logical in precedence.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Assuming `+` and `*` have the same precedence.
  **Correction**: `*` and `/` bind tighter than `+` and `-`. Use parentheses when unsure.

# Common Confusions

- **Confusion**: Precedence and associativity are the same thing.
  **Clarification**: Precedence determines which operators apply first; associativity (left-to-right for most operators) determines order among operators of equal precedence.

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Arithmetic", lines 204-214 of 01-values-types-and-operators.md; also lines 497-501 (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with italicized term and multiple examples
- Cross-reference status: verified across arithmetic and logical operator sections
