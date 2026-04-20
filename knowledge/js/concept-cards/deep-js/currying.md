---
# === CORE IDENTIFICATION ===
concept: Currying
slug: currying

# === CLASSIFICATION ===
category: language-mechanics
subcategory: environments
tier: foundational

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Environments: under the hood of variables"
chapter_number: 4
section: "4.4 Closures and environments"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - curried function

# === TYPED RELATIONSHIPS ===
prerequisites:
  - closure
extends: []
related:
  - partial-application
contrasts_with:
  - partial-application

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a closure?"
---

# Quick Definition

Currying is the technique of converting a function with two (or more) parameters into nested functions with one parameter each, enabled by closures.

# Core Definition

As described in "Deep JavaScript" (Ch 4, Section 4.4): "Converting a function with two parameters into two nested functions with one parameter each, is called *currying*. `add()` is a curried function." The `add()` example demonstrates how currying leverages closures to capture the first parameter, returning a function that awaits the second parameter.

# Prerequisites

- **Closure** — Curried functions use closures to retain access to earlier parameters.

# Key Properties

1. Transforms a multi-parameter function into a chain of single-parameter functions.
2. Each function in the chain returns the next function.
3. The final function in the chain performs the computation.
4. Enabled by closures — each returned function captures its parameter.
5. Allows partial application by calling only some functions in the chain.

# Construction / Recognition

## To Construct/Create:
1. Nest functions, each taking one parameter.
2. The outermost function returns the next function, and so on.
3. The innermost function has access to all parameters via closures.

## To Identify/Recognize:
1. A function that returns another function, where both take single parameters.
2. Chained calls: `func(a)(b)(c)`.

# Context & Application

Currying is common in functional programming and is used for creating reusable, partially applied functions. In JavaScript, it is enabled by closures and first-class functions.

# Examples

**Example 1** (Ch 4):
```js
function add(x) {
  return (y) => {
    return x + y;
  };
}
assert.equal(add(3)(1), 4);

// Partial application via currying:
const plus2 = add(2);
assert.equal(plus2(5), 7);
```

# Relationships

## Builds Upon
- **Closure** — Each nested function closes over its parameter.

## Enables
- **Partial application** — Curried functions enable easy partial application.

## Related
- **Partial application** — Related but distinct concept.

## Contrasts With
- **Partial application** — Currying transforms a function's structure; partial application fills in some arguments of any function. Currying is one way to achieve partial application.

# Common Errors

- **Error**: Calling a curried function with multiple arguments at once: `add(2, 5)`.
  **Correction**: Curried functions take one argument at a time: `add(2)(5)`.

# Common Confusions

- **Confusion**: Currying and partial application are the same thing.
  **Clarification**: Currying restructures a function into nested single-parameter functions. Partial application fixes some arguments of a function (which can be done via currying, `.bind()`, or other means).

# Source Reference

Chapter 4: Environments: under the hood of variables, Section 4.4, lines 279-281.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition provided
- Cross-reference status: verified
