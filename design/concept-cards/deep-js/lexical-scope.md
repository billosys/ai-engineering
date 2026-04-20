---
# === CORE IDENTIFICATION ===
concept: Lexical Scope
slug: lexical-scope

# === CLASSIFICATION ===
category: language-mechanics
subcategory: scoping
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "A detailed look at global variables"
chapter_number: 5
section: "5.1 Scopes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - scope
  - static scope

# === TYPED RELATIONSHIPS ===
prerequisites:
  - environment
extends: []
related:
  - lexical-environment
  - scope-chain
  - outer-environment-reference
  - closure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a lexical environment?"
  - "How does the global scope differ from module scope?"
---

# Quick Definition

A lexical scope is the static region of a program where a variable can be accessed, determined by the textual (lexical) structure of the code rather than runtime behavior.

# Core Definition

As described in "Deep JavaScript" (Ch 5, Section 5.1): "The *lexical scope* (short: *scope*) of a variable is the region of a program where it can be accessed. JavaScript's scopes are *static* (they don't change at runtime) and they can be nested." The innermost surrounding scope of a scope S is called the *outer scope* of S.

# Prerequisites

- **Environment** — Scopes are implemented via environments in the spec.

# Key Properties

1. **Static** — determined by code structure, not runtime behavior.
2. **Nestable** — scopes can be nested within other scopes.
3. Each scope has an **outer scope** (the innermost surrounding scope).
4. Implemented via **lexical environments** in the ECMAScript specification.
5. Block scopes (`if`, `for`, etc.) are scopes for `let`, `const`, and `class`.

# Construction / Recognition

## To Construct/Create:
1. Functions create scopes.
2. Blocks (`{}`) create scopes for `let`/`const`/`class`.
3. The global level is a scope.
4. Each module is a scope.

## To Identify/Recognize:
1. Any region enclosed by function boundaries or blocks (for `let`/`const`/`class`).

# Context & Application

Scopes are the fundamental organizing principle for variable visibility in JavaScript. Understanding scope nesting explains variable shadowing, closures, and the difference between global and local variables.

# Examples

**Example 1** (Ch 5): Nested scopes:
```js
function func() { // (A)
  const aVariable = 1;
  if (true) { // (B)
    const anotherVariable = 2;
  }
}
```
The scope introduced by `if` (line B) is nested inside the scope of `func()` (line A). `func` is the outer scope of `if`.

# Relationships

## Builds Upon
- **Environment** — Scopes are implemented as environments.

## Enables
- **Lexical environment** — The spec's implementation of scopes.
- **Scope chain** — Nested scopes form a chain for variable lookup.
- **Closure** — Functions close over their lexical scope.

## Related
- **Outer environment reference** — Connects nested scope implementations.

## Contrasts With
- None directly (JavaScript does not have dynamic scoping).

# Common Errors

- **Error**: Expecting `var` to be block-scoped.
  **Correction**: `var` is function-scoped, not block-scoped. Only `let`, `const`, and `class` respect block scope boundaries.

# Common Confusions

- **Confusion**: Scopes change at runtime based on how functions are called.
  **Clarification**: JavaScript scopes are static/lexical — determined by where code is written, not how it is executed. This is why JavaScript closures work correctly regardless of where a function is called.

# Source Reference

Chapter 5: A detailed look at global variables, Section 5.1, lines 40-61.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition provided
- Cross-reference status: verified
