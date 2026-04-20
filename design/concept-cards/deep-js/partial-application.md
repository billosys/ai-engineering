---
# === CORE IDENTIFICATION ===
concept: Partial Application
slug: partial-application

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
  - partially applied function

# === TYPED RELATIONSHIPS ===
prerequisites:
  - closure
extends: []
related:
  - currying
contrasts_with:
  - currying

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a closure?"
---

# Quick Definition

Partial application is the technique of fixing some parameters of a function, producing a new function that takes the remaining parameters.

# Core Definition

As described in "Deep JavaScript" (Ch 4, Section 4.4): "Only filling in some of the parameters of a function is called *partial application* (the function has not been fully applied yet). Method `.bind()` of functions performs partial application." The source notes that "partial application is simple if a function is curried," as shown by the `add()` example where `add(2)` produces `plus2`, a partially applied function.

# Prerequisites

- **Closure** — Partial application typically uses closures to capture the fixed arguments.

# Key Properties

1. Fixes some arguments of a function, producing a new function.
2. The new function takes the remaining arguments.
3. Can be achieved via currying, `.bind()`, or manual wrapper functions.
4. "The function has not been fully applied yet."

# Construction / Recognition

## To Construct/Create:
1. Via currying: call only the first function in a curried chain.
2. Via `.bind()`: `const partialFn = fn.bind(null, arg1, arg2)`.
3. Via closures: `const partialFn = (...rest) => fn(fixedArg, ...rest)`.

## To Identify/Recognize:
1. A function that was derived from another by pre-filling some arguments.

# Context & Application

Partial application is used to create specialized versions of general functions, such as creating an `add5` function from a general `add` function. It is a common technique in functional programming and in JavaScript patterns like event handlers and middleware.

# Examples

**Example 1** (Ch 4):
```js
function add(x) {
  return (y) => { return x + y; };
}
const plus2 = add(2);  // partial application
assert.equal(plus2(5), 7);
```

# Relationships

## Builds Upon
- **Closure** — The partially applied function retains access to fixed arguments via closures.

## Enables
- **Specialized functions** — Creates purpose-specific functions from general ones.

## Related
- **Currying** — One way to enable partial application.
- **Function.prototype.bind** — Built-in method for partial application.

## Contrasts With
- **Currying** — Currying is a structural transformation; partial application is the act of fixing arguments. Currying enables partial application, but they are different concepts.

# Common Errors

- **Error**: Confusing partial application with calling a function with fewer arguments than expected.
  **Correction**: Partial application produces a **new function**. Simply calling a function with too few arguments just gives `undefined` for the missing parameters.

# Common Confusions

- **Confusion**: Partial application requires currying.
  **Clarification**: Currying makes partial application easy, but `.bind()` and manual closures also achieve partial application without currying.

# Source Reference

Chapter 4: Environments: under the hood of variables, Section 4.4, lines 284-289.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition provided
- Cross-reference status: verified
