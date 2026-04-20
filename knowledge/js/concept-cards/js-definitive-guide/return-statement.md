---
# === CORE IDENTIFICATION ===
concept: return Statement
slug: return-statement

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
pdf_page: 133
section: "5.5.4 return"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-definition-expressions
  - invocation-expressions
extends: []
related:
  - yield-statement
  - throw-statement
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

The `return` statement exits a function and optionally specifies the value of the function invocation expression. Without `return`, a function returns `undefined`.

# Core Definition

"A return statement within a function specifies the value of invocations of that function... When the return statement is executed, the function that contains it returns the value of *expression* to its caller." (Ch. 5, §5.5.4)

# Prerequisites

- **function-definition-expressions** — `return` is only valid inside a function body.
- **invocation-expressions** — `return` specifies the value of the invocation expression.

# Key Properties

1. May only appear within a function body (SyntaxError otherwise).
2. `return expression;` returns the expression's value.
3. `return;` (no expression) returns `undefined`.
4. If no `return` is reached, the function returns `undefined`.
5. No line break allowed between `return` and the expression (ASI will insert a semicolon).

# Construction / Recognition

```js
return expression;
return;
```

# Context & Application

The `return` statement is fundamental to functions that compute and produce values. Understanding `return` behavior (including its absence) is essential for working with functions and closures.

# Examples

From the source text (§5.5.4, pp. 133-134):

```js
function square(x) { return x*x; }
square(2) // => 4

function displayObject(o) {
    if (!o) return;   // Return early with undefined
    // Rest of function goes here...
}
```

# Relationships

## Builds Upon
- **function-definition-expressions** — `return` is meaningful only within functions
- **invocation-expressions** — The returned value becomes the invocation expression's value

## Enables
- Functions that compute and produce values

## Related
- **yield-statement** — Similar to `return` but for generator functions
- **throw-statement** — Another way to exit a function (with an exception)

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Putting a line break after `return` and before the expression.
  **Correction**: ASI inserts a semicolon after `return`, making the function return `undefined`. Keep the expression on the same line.

# Common Confusions

- **Confusion**: Believing a function without `return` returns `null`.
  **Clarification**: Functions without a `return` statement (or with bare `return`) return `undefined`, not `null`.

# Source Reference

Chapter 5: Statements, Section 5.5.4, pages 133-134.

# Verification Notes

- Definition source: Direct quote from §5.5.4
- Confidence rationale: High — clearly defined
- Uncertainties: None
- Cross-reference status: Verified
