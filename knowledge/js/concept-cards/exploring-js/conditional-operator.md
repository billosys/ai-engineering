---
# === CORE IDENTIFICATION ===
concept: Conditional Operator
slug: conditional-operator

# === CLASSIFICATION ===
category: primitive-types
subcategory: booleans
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Booleans"
chapter_number: 17
pdf_page: null
section: "Conditional operator (? :)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "ternary operator"
  - "? :"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - falsy-and-truthy-values
extends: []
related:
  - short-circuiting
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
---

# Quick Definition

The conditional operator (`condition ? thenExpression : elseExpression`) is the expression version of `if`/`else`, evaluating and returning one of two expressions based on a truthy/falsy condition.

# Core Definition

"The conditional operator is the expression version of the `if` statement." It has the syntax `condition ? thenExpression : elseExpression`. If `condition` is truthy, it evaluates and returns `thenExpression`; otherwise, it evaluates and returns `elseExpression`. It is also called the *ternary operator* because it has three operands. Only the chosen branch is evaluated (Ch. 17, Section 17.4).

# Prerequisites

- **falsy-and-truthy-values** -- the condition is evaluated for truthiness

# Key Properties

1. Expression-level if/else (returns a value)
2. Only the selected branch is evaluated
3. Three operands (ternary)
4. Condition uses truthiness, not strict boolean

# Construction / Recognition

```js
> true ? 'yes' : 'no'
'yes'
> false ? 'yes' : 'no'
'no'
> '' ? 'yes' : 'no'
'no'
```

# Context & Application

Use the conditional operator for inline value selection. It is especially useful in JSX, template literals, and anywhere an expression is needed rather than a statement.

# Examples

From the source text:

```js
> true ? 'yes' : 'no'
'yes'
> false ? 'yes' : 'no'
'no'
> '' ? 'yes' : 'no'
'no'

// Only the chosen branch is evaluated
const x = (true ? console.log('then') : console.log('else'));
// Output: then
```

# Relationships

## Builds Upon
- **falsy-and-truthy-values** — condition uses truthiness

## Enables
- Inline conditional expressions

## Related
- **short-circuiting** — the conditional operator also delays evaluation of branches

## Contrasts With
- None

# Common Errors

- **Error**: Nesting too many ternary operators, making code unreadable
  **Correction**: Use `if`/`else` statements for complex conditions.

# Common Confusions

- **Confusion**: Thinking both branches are always evaluated
  **Clarification**: Only the selected branch is evaluated; the other is skipped entirely.

# Source Reference

Chapter 17: Booleans, Section 17.4, lines 442-487.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with examples
- Cross-reference status: verified
