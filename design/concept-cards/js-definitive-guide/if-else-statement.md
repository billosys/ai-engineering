---
# === CORE IDENTIFICATION ===
concept: if/else Statement
slug: if-else-statement

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: statements
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Statements"
chapter_number: 5
pdf_page: 117
section: "5.3.1 if"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "conditional statement"
  - "if statement"
  - "else if"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - expression-statements
  - compound-and-empty-statements
extends: []
related:
  - switch-case-statement
  - ternary-operator
contrasts_with:
  - switch-case-statement
  - ternary-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

The `if/else` statement is the fundamental control structure for conditional execution: it evaluates an expression and executes one of two statements depending on whether the result is truthy or falsy.

# Core Definition

"The if statement is the fundamental control statement that allows JavaScript to make decisions, or, more precisely, to execute statements conditionally." Two forms exist: `if (expression) statement` and `if (expression) statement1 else statement2`. The `else if` idiom chains multiple conditions. (Ch. 5, §5.3.1)

# Prerequisites

- **expression-statements** — The condition is an expression; the bodies are statements.
- **compound-and-empty-statements** — Block statements are commonly used for if/else bodies.

# Key Properties

1. The expression in parentheses is required syntax.
2. The expression is evaluated as truthy/falsy, not strictly boolean.
3. `else` clause is optional.
4. `else if` is an idiom (not a distinct keyword) — it's an `else` followed by another `if`.
5. Dangling else: an `else` belongs to the nearest `if` statement.
6. Best practice: always use curly braces for if/else bodies.

# Construction / Recognition

```js
if (expression) statement
if (expression) statement1 else statement2
if (n === 1) { ... } else if (n === 2) { ... } else { ... }
```

# Context & Application

The `if/else` statement is the most basic decision-making construct. It is used for branching logic, input validation, feature detection, and all forms of conditional execution.

# Examples

From the source text (§5.3.1-5.3.2, pp. 117-120):

```js
if (username == null)
    username = "John Doe";

if (n === 1)
    console.log("You have 1 new message.");
else
    console.log(`You have ${n} new messages.`);

// else if idiom
if (n === 1) {
    // Execute code block #1
} else if (n === 2) {
    // Execute code block #2
} else {
    // If all else fails, execute block #4
}
```

# Relationships

## Builds Upon
- **expression-statements** — Conditions are expressions
- **compound-and-empty-statements** — Bodies are typically block statements

## Enables
- All branching logic in JavaScript programs

## Related
- **switch-case-statement** — Alternative for multiway branching on a single expression
- **ternary-operator** — Expression-level conditional

## Contrasts With
- **switch-case-statement** — `switch` is better when branching on one expression's value
- **ternary-operator** — `?:` is an expression; `if/else` is a statement

# Common Errors

- **Error**: The dangling else problem — an `else` binds to the nearest `if`, not the outer one.
  **Correction**: Always use curly braces to make the intended structure explicit.

# Common Confusions

- **Confusion**: Believing `else if` is a single keyword.
  **Clarification**: `else if` is syntactic sugar — it's just an `else` clause containing another `if` statement.

# Source Reference

Chapter 5: Statements, Sections 5.3.1-5.3.2, pages 117-120.

# Verification Notes

- Definition source: Direct quote from §5.3.1
- Confidence rationale: High — extensively covered
- Uncertainties: None
- Cross-reference status: Verified
