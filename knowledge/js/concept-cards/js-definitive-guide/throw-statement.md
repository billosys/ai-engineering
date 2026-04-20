---
# === CORE IDENTIFICATION ===
concept: throw Statement
slug: throw-statement

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
pdf_page: 134
section: "5.5.6 throw"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "throwing exceptions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - expression-statements
extends: []
related:
  - try-catch-finally
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

The `throw` statement signals an error or exceptional condition by throwing an exception value, which propagates up the call stack until caught by a `try/catch` handler.

# Core Definition

"To *throw* an exception is to signal such an error or exceptional condition. To *catch* an exception is to handle it. In JavaScript, exceptions are thrown whenever a runtime error occurs and whenever the program explicitly throws one using the throw statement." (Ch. 5, §5.5.6)

# Prerequisites

- **expression-statements** — The thrown value is any expression.

# Key Properties

1. `throw expression;` — the expression can be any type, but Error objects are conventional.
2. Error objects have `name` and `message` properties.
3. When thrown, the interpreter immediately stops normal execution and jumps to the nearest exception handler.
4. Exceptions propagate up through the call stack until caught.
5. Uncaught exceptions are reported as errors to the user.

# Construction / Recognition

```js
throw new Error("message");
throw expression;
```

# Context & Application

`throw` is used for signaling errors in functions, enforcing preconditions, and implementing error-handling protocols.

# Examples

From the source text (§5.5.6, pp. 134-135):

```js
function factorial(x) {
    if (x < 0) throw new Error("x must not be negative");
    let f;
    for(f = 1; x > 1; f *= x, x--) /* empty */ ;
    return f;
}
factorial(4) // => 24
```

# Relationships

## Builds Upon
- **expression-statements** — The thrown value is an expression

## Enables
- **try-catch-finally** — `throw` is designed to work with `try/catch`

## Related
- **return-statement** — Both cause function exit, but `throw` propagates an exception

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Throwing strings instead of Error objects.
  **Correction**: While any value can be thrown, Error objects provide stack traces and conventional `name`/`message` properties.

# Common Confusions

- **Confusion**: Believing `throw` only works inside `try` blocks.
  **Clarification**: `throw` can be used anywhere. The exception propagates up until caught by any enclosing `try/catch`, even in a calling function.

# Source Reference

Chapter 5: Statements, Section 5.5.6, pages 134-135.

# Verification Notes

- Definition source: Direct quote from §5.5.6
- Confidence rationale: High — clearly defined with example
- Uncertainties: None
- Cross-reference status: Verified
