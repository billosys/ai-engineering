---
# === CORE IDENTIFICATION ===
concept: Ternary Operator
slug: ternary-operator

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
section: "Logical operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - conditional operator

# === TYPED RELATIONSHIPS ===
prerequisites:
  - boolean
  - expression
extends: []
related:
  - conditional-execution
  - short-circuit-evaluation
contrasts_with:
  - unary-operator
  - binary-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an expression vs. a statement?"
  - "What must I know before understanding closures?"
---

# Quick Definition

The ternary operator (`? :`) operates on three values: it uses a Boolean condition to choose between two result values, written as `a ? b : c`.

# Core Definition

As described in "Eloquent JavaScript" (Ch 1, lines 520-525 of 01-values-types-and-operators.md): "This one is called the *conditional* operator (or sometimes just *the ternary operator* since it is the only such operator in the language). The operator uses the value to the left of the question mark to decide which of the two other values to 'pick'. If you write `a ? b : c`, the result will be `b` when `a` is true and `c` otherwise."

# Prerequisites

- **Boolean** -- The condition value is evaluated as Boolean.
- **Expression** -- The ternary operator is an expression that produces a value.

# Key Properties

1. The **only ternary operator** in JavaScript (operates on three values) (line 521).
2. Written as `condition ? valueIfTrue : valueIfFalse` (line 524).
3. Also called the **conditional operator** (line 520).
4. Only the **selected branch** is evaluated (similar to short-circuit evaluation) (lines 688-690).
5. It is an **expression** -- it produces a value and can be used inside other expressions.

# Construction / Recognition

## To Construct/Create:
1. Write: `condition ? resultIfTrue : resultIfFalse`.

## To Identify/Recognize:
1. The `?` and `:` pair in an expression context.

# Context & Application

The ternary operator provides a concise way to choose between two values based on a condition within an expression, without needing a full `if`/`else` statement. It is commonly used for inline conditional assignments and returns.

# Examples

**Example 1** (Ch 1, lines 512-517): Basic ternary usage:
```js
console.log(true ? 1 : 2);
// → 1
console.log(false ? 1 : 2);
// → 2
```

# Relationships

## Builds Upon
- **Boolean** -- The condition is evaluated as Boolean.
- **Expression** -- The ternary operator produces a value.

## Enables
- Inline conditional value selection.

## Related
- **Conditional Execution** -- `if`/`else` is the statement-level equivalent.
- **Short-Circuit Evaluation** -- Similar lazy evaluation of only the selected branch.

## Contrasts With
- **Unary Operator** -- Takes one operand.
- **Binary Operator** -- Takes two operands.

# Common Errors

- **Error**: Using the ternary operator for side effects rather than value selection.
  **Correction**: The ternary operator is best used to choose between two values. For side-effect-based branching, use `if`/`else`.

# Common Confusions

- **Confusion**: The ternary operator and `if`/`else` are interchangeable.
  **Clarification**: The ternary operator is an **expression** (produces a value), while `if`/`else` is a **statement** (performs actions). They serve related but distinct purposes.

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Logical operators", lines 507-525 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with italicized term
- Cross-reference status: verified within chapter
