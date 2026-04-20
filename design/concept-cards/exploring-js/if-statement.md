---
# === CORE IDENTIFICATION ===
concept: If Statement
slug: if-statement

# === CLASSIFICATION ===
category: control-flow
subcategory: conditionals
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Control flow statements"
chapter_number: 25
pdf_page: null
section: "25.3 `if` statements"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "if-else"
  - "conditional statement"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - truthy-and-falsy-values
extends: []
related:
  - switch-statement
contrasts_with:
  - switch-statement

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I conditionally execute code in JavaScript?"
---

# Quick Definition

The `if` statement executes a block of code only when its condition is truthy, with optional `else` and `else if` branches for alternative paths.

# Core Definition

As described in "Exploring JavaScript" Ch. 25, the `if` statement has the general syntax `if (cond) then_statement else else_statement`. The condition need only be truthy (not strictly `true`) for the then-branch to execute. The `else if` construct is not its own syntax -- it is simply an `if` statement used as the else-branch of another `if`.

# Prerequisites

- Truthy and falsy values
- Block statements

# Key Properties

1. Introduced in ES1.
2. Condition is evaluated for truthiness, not strict boolean equality.
3. `else if` is syntactic sugar -- an `if` used as the else-statement.
4. The then-branch and else-branch can be any statement, not just blocks.

# Construction / Recognition

```js
if (cond) {
  // then branch
} else if (cond2) {
  // else-if branch
} else {
  // else branch
}
```

# Context & Application

Used universally for conditional branching. Prefer `if` over `switch` when testing non-equality conditions or when there are few branches.

# Examples

From the source text (Ch. 25, section 25.3):

```js
if (cond) {
  // then branch
} else {
  // else branch
}
```

Single-statement form:
```js
if (true) console.log('Yes'); else console.log('No');
```

# Relationships

## Builds Upon
- **Truthy and Falsy Values** -- the condition uses truthiness, not strict boolean

## Enables
- **Control Flow Patterns** -- foundational branching mechanism

## Related
- **Switch Statement** -- alternative multi-branch conditional

## Contrasts With
- **Switch Statement** -- `switch` uses strict equality on a single expression; `if` supports arbitrary conditions

# Common Errors

- **Error**: Forgetting that the condition uses truthiness, leading to unexpected branch selection with values like `0`, `''`, or `null`.
  **Correction**: Understand the full list of falsy values: `undefined`, `null`, `false`, `0`, `NaN`, `0n`, `''`.

# Common Confusions

- **Confusion**: Thinking `else if` is a special keyword.
  **Clarification**: `else if` is just an `if` statement used as the else-clause. There is no `elseif` keyword.

# Source Reference

Chapter 25: Control flow statements, Section 25.3, lines 214-276.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit syntax and semantics in source text
- Cross-reference status: verified with section 17.2 (falsy/truthy values)
