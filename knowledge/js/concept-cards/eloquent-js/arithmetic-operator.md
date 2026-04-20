---
# === CORE IDENTIFICATION ===
concept: Arithmetic Operator
slug: arithmetic-operator

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - value
  - number
extends: []
related:
  - operator-precedence
  - binary-operator
  - unary-operator
  - remainder-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a value in JavaScript?"
  - "What must I know before understanding closures?"
---

# Quick Definition

Arithmetic operators (`+`, `-`, `*`, `/`, `%`) take two number values and produce a new number from them.

# Core Definition

As described in "Eloquent JavaScript" (Ch 1, lines 173-176 of 01-values-types-and-operators.md): "The main thing to do with numbers is arithmetic. Arithmetic operations such as addition or multiplication take two number values and produce a new number from them." The operators are `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), and `%` (remainder/modulo).

# Prerequisites

- **Value** -- Operators act on values.
- **Number** -- Arithmetic operators work primarily with numbers.

# Key Properties

1. `+` and `*` are called **operators**; "putting an operator between two values will apply it to those values and produce a new value" (lines 183-186).
2. **Precedence** determines evaluation order: `*` and `/` before `+` and `-` (lines 204-210).
3. Parentheses override precedence: `(100 + 4) * 11` (lines 195-197).
4. Operators with the same precedence are applied **left to right**: `(1 - 2) + 1` (line 210).
5. The `%` (remainder) operator has the same precedence as `*` and `/` (line 221).
6. The `+` operator also performs **string concatenation** when applied to strings.

# Construction / Recognition

## To Construct/Create:
1. Place an operator between two numeric values: `100 + 4 * 11`.
2. Use parentheses to control grouping: `(100 + 4) * 11`.

## To Identify/Recognize:
1. Binary operators `+`, `-`, `*`, `/`, `%` used between numeric values.

# Context & Application

Arithmetic operators are the fundamental tools for numeric computation in JavaScript. They are used in everything from simple calculations to loop counters and complex algorithms.

# Examples

**Example 1** (Ch 1, lines 178-179): Basic arithmetic:
```js
100 + 4 * 11
```

**Example 2** (Ch 1, lines 195-197): Parentheses overriding precedence:
```js
(100 + 4) * 11
```

**Example 3** (Ch 1, lines 219-221): Remainder operator:
"`X % Y` is the remainder of dividing `X` by `Y`. For example, `314 % 100` produces `14`, and `144 % 12` gives `0`."

# Relationships

## Builds Upon
- **Value** -- Operators act on values.
- **Number** -- Arithmetic operators work with numbers.

## Enables
- **Expression** -- Arithmetic expressions are the simplest compound expressions.
- **Operator Precedence** -- Understanding arithmetic requires understanding precedence.

## Related
- **Binary Operator** -- Arithmetic operators are binary (take two operands).
- **Remainder Operator** -- The `%` operator is often discussed separately.

## Contrasts With
- None directly within this source.

# Common Errors

- **Error**: Assuming `+` always adds numbers.
  **Correction**: When either operand is a string, `+` performs string concatenation (lines 324-327).

# Common Confusions

- **Confusion**: The `%` operator computes percentages.
  **Clarification**: `%` is the remainder (modulo) operator, not a percentage operator. `314 % 100` gives `14`.

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Arithmetic", lines 170-223 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Dedicated subsection with clear examples
- Cross-reference status: verified within chapter
