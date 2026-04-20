---
# === CORE IDENTIFICATION ===
concept: Expression Statements
slug: expression-statements

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
pdf_page: 114
section: "5.1 Expression Statements"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "statement expressions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primary-expressions
extends: []
related:
  - compound-and-empty-statements
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

Expression statements are expressions that are evaluated for their side effects (such as assignments, function calls, and increments) and used as standalone statements terminated by semicolons.

# Core Definition

"The simplest kinds of statements in JavaScript are expressions that have side effects." Expressions are *evaluated* to produce a value, but statements are *executed* to make something happen. "Expressions with side effects, such as assignments and function invocations, can stand alone as statements, and when used this way are known as *expression statements*." (Ch. 5, §5.1)

# Prerequisites

- **primary-expressions** — Expression statements are built from expressions.

# Key Properties

1. Assignment statements are a major category: `greeting = "Hello " + name;`.
2. Increment/decrement: `counter++;`.
3. Function calls: `console.log(debugMessage);`.
4. The `delete` operator: `delete o.x;`.
5. If a function has no side effects, calling it as a standalone statement is pointless.
6. Each expression statement is terminated with a semicolon.

# Construction / Recognition

Any expression with side effects, followed by a semicolon, is an expression statement.

# Context & Application

Expression statements are the workhorses of JavaScript programs. Most lines of imperative code are expression statements: assignments, function calls, and updates.

# Examples

From the source text (§5.1, pp. 114-115):

```js
greeting = "Hello " + name;
i *= 3;
counter++;
delete o.x;
console.log(debugMessage);
displaySpinner();
cx = Math.cos(x);
```

# Relationships

## Builds Upon
- **primary-expressions** — Expression statements are expressions evaluated for side effects

## Enables
- All imperative programming patterns in JavaScript

## Related
- **compound-and-empty-statements** — Other basic statement forms

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Writing an expression with no side effects as a statement (e.g., `Math.cos(x);` without assigning).
  **Correction**: If a function has no side effects, calling it as a statement wastes computation. Assign the result or remove the call.

# Common Confusions

- **Confusion**: Confusing expressions and statements.
  **Clarification**: Expressions produce values; statements make things happen. Expression statements are the bridge — expressions used for their side effects.

# Source Reference

Chapter 5: Statements, Section 5.1, pages 114-115.

# Verification Notes

- Definition source: Direct quote from §5.1
- Confidence rationale: High — straightforward section
- Uncertainties: None
- Cross-reference status: Verified
