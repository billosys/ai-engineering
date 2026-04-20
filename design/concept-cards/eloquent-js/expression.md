---
# === CORE IDENTIFICATION ===
concept: Expression
slug: expression

# === CLASSIFICATION ===
category: fundamentals
subcategory: program-structure
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Program Structure"
chapter_number: 2
pdf_page: null
section: "Expressions and statements"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - value
extends: []
related:
  - statement
  - binary-operator
  - unary-operator
contrasts_with:
  - statement

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an expression vs. a statement?"
  - "What must I know before understanding closures?"
  - "What must I know before learning about prototypes and classes?"
---

# Quick Definition

An expression is a fragment of code that produces a value, including literals, operators applied to expressions, and function calls.

# Core Definition

As defined in "Eloquent JavaScript" (Ch 2, lines 48-52 of 02-program-structure.md): "A fragment of code that produces a value is called an *expression*. Every value that is written literally (such as `22` or `\"psychoanalysis\"`) is an expression. An expression between parentheses is also an expression, as is a binary operator applied to two expressions or a unary operator applied to one."

# Prerequisites

- **Value** -- Expressions produce values.

# Key Properties

1. A fragment of code that **produces a value** (line 49).
2. **Literal values** are expressions: `22`, `"psychoanalysis"` (line 50).
3. Expressions can **contain other expressions** -- they nest like subsentences in human language (lines 56-59).
4. Parenthesized expressions, binary operations, and unary operations are all expressions (lines 51-52).
5. **Function calls** are expressions when they produce values (Ch 2, lines 324-325).
6. Expressions can describe **arbitrarily complex computations** through nesting (line 59).

# Construction / Recognition

## To Construct/Create:
1. Write a literal: `42`, `"hello"`, `true`.
2. Apply operators: `3 + 4`, `!false`.
3. Call a function that returns a value: `Math.max(2, 4)`.
4. Nest expressions: `(3 + 4) * 2`.

## To Identify/Recognize:
1. Any code fragment that produces a value.
2. Can appear on the right side of `=`, as arguments to functions, or inside other expressions.

# Context & Application

Expressions are one of the two fundamental building blocks of programs (alongside statements). Understanding the distinction between expressions and statements is essential for understanding how JavaScript programs are structured and evaluated.

# Examples

**Example 1** (Ch 2, lines 48-52): Definition with examples:
"Every value that is written literally (such as `22` or `\"psychoanalysis\"`) is an expression."

**Example 2** (Ch 2, lines 329-332): Function call as expression:
```js
console.log(Math.min(2, 4) + 100);
// → 102
```
`Math.min(2, 4)` is an expression used within a larger plus expression.

# Relationships

## Builds Upon
- **Value** -- Every expression produces a value.

## Enables
- **Statement** -- Statements contain expressions.
- All compound program structures.

## Related
- **Binary Operator** -- Binary operations are expressions.
- **Unary Operator** -- Unary operations are expressions.

## Contrasts With
- **Statement** -- "If an expression corresponds to a sentence fragment, a JavaScript statement corresponds to a full sentence" (lines 62-63).

# Common Errors

- **Error**: Treating statements and expressions as interchangeable.
  **Correction**: An expression produces a value; a statement performs an action. `1 + 2` is an expression; `let x = 1 + 2;` is a statement that contains an expression.

# Common Confusions

- **Confusion**: Only complex code fragments are expressions.
  **Clarification**: Even a single literal value like `22` is an expression. Any code that produces a value qualifies.

# Source Reference

Chapter 2: Program Structure, Section "Expressions and statements", lines 38-95 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with italicized term in dedicated section
- Cross-reference status: verified within chapter
