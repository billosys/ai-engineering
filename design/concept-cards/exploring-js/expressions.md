---
# === CORE IDENTIFICATION ===
concept: Expressions
slug: expressions

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
section: "9.5.2 Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - expression

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - expression-statements
  - statements
contrasts_with:
  - statements

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an expression in JavaScript?"
---

# Quick Definition

An expression is a piece of JavaScript code that can be evaluated to produce a value, such as `3 + 4`, `'abc'`, or `myBool ? 'Yes' : 'No'`.

# Core Definition

"An *expression* is a piece of code that can be *evaluated* to produce a value." (Ch. 9, &sect;9.5.2). Expressions include literals, operators, function calls, and the ternary operator. They can be used as function arguments and on the right side of assignments. Expressions can also be used as statements (expression statements).

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Evaluates to produce a value
2. Can be used as function/method arguments
3. Can be used as statements (expression statements)
4. Examples: string concatenation, `Number()` calls, boolean operations, ternary operator

# Construction / Recognition

```js
// Ternary operator (expression version of if)
let myStr = (myBool ? 'Yes' : 'No');

// String concatenation
'ab' + 'cd'  // evaluates to 'abcd'

// Function call as expression
Number('123')  // evaluates to 123
```

# Context & Application

Expressions are required in function arguments, assignments, return values, and template literal interpolations. The ternary operator `_?_:_` is the expression version of `if`.

# Examples

From the source text (Ch. 9, &sect;9.5.2):
```js
> 'ab' + 'cd'
'abcd'
> Number('123')
123
> true || false
true
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **expression-statements** -- expressions used in statement position

## Related
- No additional

## Contrasts With
- **statements** -- statements perform actions; expressions produce values

# Common Errors

- **Error**: Using a statement where an expression is needed (e.g., `if` inside a template literal).
  **Correction**: Use the expression equivalent: ternary operator, logical operators, etc.

# Common Confusions

- **Confusion**: Thinking all code is either a statement or an expression.
  **Clarification**: The book simplifies by pretending there are only these two categories, though the reality is slightly more nuanced.

# Source Reference

Chapter 9: Syntax, Section 9.5.2, lines 700-726.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit definition with examples
- Cross-reference status: verified
