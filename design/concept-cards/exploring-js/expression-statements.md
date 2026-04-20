---
# === CORE IDENTIFICATION ===
concept: Expression Statements
slug: expression-statements

# === CLASSIFICATION ===
category: syntax-fundamentals
subcategory: syntax-categories
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Syntax"
chapter_number: 9
pdf_page: null
section: "9.5.3 What is allowed where?"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - statements
  - expressions
extends: []
related:
  - ambiguous-syntax
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can expressions be used as statements in JavaScript?"
---

# Quick Definition

An expression statement is an expression used in statement position, such as a standalone function call. Expressions can be used as statements, but statements cannot be used as expressions.

# Core Definition

"Expressions can be used as statements. Then they are called *expression statements*. The opposite is not true: when the context requires an expression, you can't use a statement." (Ch. 9, &sect;9.5.3). A function call like `bar()` can serve as either an expression (when its return value is used) or an expression statement (when its return value is discarded).

# Prerequisites

- **statements** -- expression statements are a type of statement
- **expressions** -- expression statements are expressions in statement context

# Key Properties

1. Expressions can appear in statement position
2. The reverse is not true (statements cannot appear where expressions are needed)
3. A function call can be expression or statement depending on context
4. Expression statements end with semicolons

# Construction / Recognition

```js
function f() {
  console.log(bar()); // bar() is expression
  bar(); // bar(); is (expression) statement
}
```

# Context & Application

Expression statements are common in JavaScript: function calls, assignments, and increment operations are all typically used as statements.

# Examples

From the source text (Ch. 9, &sect;9.5.3):
```js
function f() {
  console.log(bar()); // bar() is expression
  bar(); // bar(); is (expression) statement
}
```

# Relationships

## Builds Upon
- **statements** -- expression statements are statements
- **expressions** -- expression statements are expressions used as statements

## Enables
- **ambiguous-syntax** -- expression statements create syntactic ambiguity

## Related
- No additional

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Starting an expression statement with `{` or `function`, causing ambiguity.
  **Correction**: Wrap in parentheses to force expression interpretation.

# Common Confusions

- **Confusion**: Thinking a function call is always a statement.
  **Clarification**: `bar()` is an expression that produces a value; using it alone on a line makes it an expression statement.

# Source Reference

Chapter 9: Syntax, Section 9.5.3, lines 728-766.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit definition with example
- Cross-reference status: verified
