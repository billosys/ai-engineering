---
# === CORE IDENTIFICATION ===
concept: Binary Operator
slug: binary-operator

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
section: "Unary operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - value
extends: []
related:
  - unary-operator
  - ternary-operator
  - arithmetic-operator
  - comparison-operators
  - logical-operators
contrasts_with:
  - unary-operator
  - ternary-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a value in JavaScript?"
  - "What must I know before understanding closures?"
---

# Quick Definition

A binary operator takes two values (operands) and produces a new value. Most operators in JavaScript are binary, including arithmetic (`+`, `-`, `*`, `/`), comparison (`>`, `<`, `==`), and logical (`&&`, `||`) operators.

# Core Definition

As described in "Eloquent JavaScript" (Ch 1, lines 377-378 of 01-values-types-and-operators.md): "Operators that use two values are called *binary* operators." The source introduces this term in the section on unary operators, establishing the classification by arity. Binary operators include arithmetic operators (lines 183-186), comparison operators (lines 409-412), and logical `&&` and `||` (lines 466-479).

# Prerequisites

- **Value** -- Binary operators act on two values.

# Key Properties

1. Takes **two operands** -- one on each side of the operator symbol.
2. Includes all **arithmetic operators**: `+`, `-`, `*`, `/`, `%`.
3. Includes all **comparison operators**: `>`, `<`, `>=`, `<=`, `==`, `!=`, `===`, `!==`.
4. Includes logical `&&` and `||`.
5. "Putting an operator between two values will apply it to those values and produce a new value" (lines 185-186).

# Construction / Recognition

## To Construct/Create:
1. Place the operator between two values: `3 + 4`, `"a" < "b"`, `true && false`.

## To Identify/Recognize:
1. An operator positioned between two operands in an expression.

# Context & Application

Binary operators form the backbone of JavaScript expressions. Nearly every computation involves combining two values with a binary operator to produce a result.

# Examples

**Example 1** (Ch 1, lines 178-179): Arithmetic binary operators:
```js
100 + 4 * 11
```

**Example 2** (Ch 1, lines 401-406): Comparison binary operators:
```js
console.log(3 > 2)
// → true
console.log(3 < 2)
// → false
```

# Relationships

## Builds Upon
- **Value** -- Binary operators act on two values.

## Enables
- **Expression** -- Binary operations are the primary way expressions are composed.

## Related
- **Arithmetic Operator** -- All arithmetic operators are binary.
- **Comparison Operators** -- All comparison operators are binary.
- **Logical Operators** -- `&&` and `||` are binary.

## Contrasts With
- **Unary Operator** -- Takes one operand.
- **Ternary Operator** -- Takes three operands.

# Common Errors

- **Error**: Assuming `-` is always a binary operator.
  **Correction**: The minus operator can be unary (negation: `- (10 - 2)`) or binary (subtraction: `10 - 2`).

# Common Confusions

- **Confusion**: "Binary" refers to the binary number system.
  **Clarification**: In the context of operators, "binary" means "takes two operands," not "related to binary numbers."

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Unary operators", lines 376-380 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with italicized term
- Cross-reference status: verified within chapter
