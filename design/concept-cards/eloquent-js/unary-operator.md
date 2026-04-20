---
# === CORE IDENTIFICATION ===
concept: Unary Operator
slug: unary-operator

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
  - binary-operator
  - ternary-operator
  - logical-operators
contrasts_with:
  - binary-operator
  - ternary-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a value in JavaScript?"
  - "What must I know before understanding closures?"
---

# Quick Definition

A unary operator takes only one value as its operand, in contrast to binary operators which take two. Examples include `typeof`, the unary minus (`-`), and logical not (`!`).

# Core Definition

As described in "Eloquent JavaScript" (Ch 1, lines 376-380 of 01-values-types-and-operators.md): "The other operators shown so far in this chapter all operated on two values, but `typeof` takes only one. Operators that use two values are called *binary* operators, while those that take one are called *unary* operators. The minus operator (`-`) can be used both as a binary operator and as a unary operator."

# Prerequisites

- **Value** -- Operators act on values.

# Key Properties

1. Takes **one operand** (one value).
2. `typeof` is a unary operator that produces a string naming the type of a value (lines 360-361).
3. The minus operator `-` can be used as both unary (negation) and binary (subtraction) (line 380).
4. The `!` operator is unary -- it flips a Boolean value (lines 489-491).

# Construction / Recognition

## To Construct/Create:
1. Place the operator before its single operand: `typeof x`, `-8`, `!true`.

## To Identify/Recognize:
1. An operator that takes only one operand, typically written before the operand.

# Context & Application

Unary operators are used for type checking (`typeof`), numeric negation (`-`), and logical negation (`!`). Understanding the distinction between unary and binary operators clarifies how JavaScript parses expressions.

# Examples

**Example 1** (Ch 1, lines 363-368): The `typeof` operator:
```js
console.log(typeof 4.5)
// → number
console.log(typeof "x")
// → string
```

**Example 2** (Ch 1, lines 382-385): Unary minus for negation:
```js
console.log(- (10 - 2))
// → -8
```

# Relationships

## Builds Upon
- **Value** -- Operators act on values.

## Enables
- Understanding expression parsing and operator arity.

## Related
- **Logical Operators** -- `!` is a unary logical operator.

## Contrasts With
- **Binary Operator** -- Takes two operands instead of one.
- **Ternary Operator** -- Takes three operands.

# Common Errors

- **Error**: Confusing the unary minus with the binary minus.
  **Correction**: `- (10 - 2)` uses unary minus on the result of binary subtraction. Context determines which is which.

# Common Confusions

- **Confusion**: All operators work on two values.
  **Clarification**: Operators vary in arity: unary (one operand), binary (two), and ternary (three).

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Unary operators", lines 356-385 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with italicized term in dedicated section
- Cross-reference status: verified within chapter
