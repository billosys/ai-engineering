---
# === CORE IDENTIFICATION ===
concept: Statements
slug: statements

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
section: "9.5.1 Statements"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - statement

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - expression-statements
  - semicolons
contrasts_with:
  - expressions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a statement in JavaScript?"
---

# Quick Definition

A statement is a piece of JavaScript code that can be executed and performs some kind of action, such as `if` conditionals, `for` loops, and function declarations.

# Core Definition

"A *statement* is a piece of code that can be executed and performs some kind of action." (Ch. 9, &sect;9.5.1). Statements include control flow constructs (`if`, `while`, `for`), declarations (`function`, `class`), and other action-performing code. The body of a function must be a sequence of statements.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Performs an action when executed
2. Cannot be used where an expression is expected
3. Function bodies are sequences of statements
4. Terminated by semicolons (except when ending with a block `{}`)
5. Expressions can be used as statements (expression statements), but not vice versa

# Construction / Recognition

```js
// if statement
if (myBool) {
  myStr = 'Yes';
} else {
  myStr = 'No';
}

// function declaration (a statement)
function twice(x) {
  return x + x;
}
```

# Context & Application

Statements form the backbone of JavaScript programs. Understanding the statement/expression distinction is essential for avoiding syntax errors.

# Examples

From the source text (Ch. 9, &sect;9.5.1):
```js
let myStr;
if (myBool) {
  myStr = 'Yes';
} else {
  myStr = 'No';
}

function twice(x) {
  return x + x;
}
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **expression-statements** -- expressions used as statements
- **semicolons** -- statement termination rules

## Related
- No additional

## Contrasts With
- **expressions** -- expressions produce values; statements perform actions

# Common Errors

- **Error**: Using a statement where an expression is required (e.g., in a function argument).
  **Correction**: Use the expression equivalent (e.g., ternary instead of if/else).

# Common Confusions

- **Confusion**: Not recognizing that expressions can be statements but statements cannot be expressions.
  **Clarification**: `bar()` can be both an expression (producing a value) and a statement (discarding the value).

# Source Reference

Chapter 9: Syntax, Section 9.5.1, lines 674-698.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit definition with examples
- Cross-reference status: verified
