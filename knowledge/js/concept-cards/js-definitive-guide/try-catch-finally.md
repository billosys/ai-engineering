---
# === CORE IDENTIFICATION ===
concept: try/catch/finally Statement
slug: try-catch-finally

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
pdf_page: 135
section: "5.5.7 try/catch/finally"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "exception handling"
  - "error handling"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - throw-statement
  - compound-and-empty-statements
extends: []
related:
  - return-statement
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

The `try/catch/finally` statement is JavaScript's exception handling mechanism: `try` defines code to monitor, `catch` handles exceptions, and `finally` runs cleanup code regardless of what happens.

# Core Definition

"The try/catch/finally statement is JavaScript's exception handling mechanism. The try clause of this statement simply defines the block of code whose exceptions are to be handled. The try block is followed by a catch clause, which is a block of statements that are invoked when an exception occurs anywhere within the try block. The catch clause is followed by a finally block containing cleanup code that is guaranteed to be executed, regardless of what happens in the try block." (Ch. 5, §5.5.7)

# Prerequisites

- **throw-statement** — `try/catch` handles exceptions thrown by `throw`.
- **compound-and-empty-statements** — All three clauses use block statements (curly braces required).

# Key Properties

1. `catch` and `finally` are both optional, but at least one must be present.
2. Curly braces are required for all clauses, even with single statements.
3. The `catch` parameter has block scope — only defined within the catch block.
4. `finally` executes regardless of: normal completion, `break`/`continue`/`return`, caught exception, or uncaught exception.
5. If `finally` contains a `return`, `break`, `throw`, or `continue`, it overrides any pending jump.
6. ES2019 allows bare `catch` (without parentheses/parameter).

# Construction / Recognition

```js
try { ... }
catch(e) { ... }
finally { ... }
```

# Context & Application

`try/catch/finally` is essential for robust error handling. The `finally` clause is used for cleanup tasks like closing resources, restoring state, or ensuring logging occurs regardless of errors.

# Examples

From the source text (§5.5.7, pp. 135-138):

```js
try {
    let n = Number(prompt("Please enter a positive integer", ""));
    let f = factorial(n);
    alert(n + "! = " + f);
}
catch(ex) {
    alert(ex);
}

// Bare catch (ES2019)
function parseJSON(s) {
    try {
        return JSON.parse(s);
    } catch {
        return undefined;
    }
}

// finally overrides pending jumps
// If finally throws, it replaces any exception in progress
// If finally returns, the method returns normally even if an exception was thrown
```

# Relationships

## Builds Upon
- **throw-statement** — `try/catch` is the receiving end of `throw`
- **compound-and-empty-statements** — Requires block syntax

## Enables
- Robust error handling and cleanup patterns

## Related
- **return-statement** — `finally` executes even when `return` is used in `try`

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Relying on `finally` to not interfere with control flow.
  **Correction**: A `return` or `throw` in `finally` overrides any pending return or exception from `try`/`catch`.

# Common Confusions

- **Confusion**: Believing `finally` only runs when there is an exception.
  **Clarification**: `finally` always runs — after normal completion, after `return`, after exceptions (caught or not), and after `break`/`continue`.

# Source Reference

Chapter 5: Statements, Section 5.5.7, pages 135-138.

# Verification Notes

- Definition source: Direct quote from §5.5.7
- Confidence rationale: High — extensive coverage of all edge cases
- Uncertainties: None
- Cross-reference status: Verified
