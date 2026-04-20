---
# === CORE IDENTIFICATION ===
concept: Environment
slug: environment

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
section: "4.1 Environment: data structure for managing variables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - lexical environment
  - environment record

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - execution-context
  - scope-chain
  - closure
  - outer-environment-reference
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a lexical environment?"
---

# Quick Definition

An environment is the data structure the ECMAScript specification uses to manage variables — a dictionary mapping variable names to their values, with each scope having its own associated environment.

# Core Definition

As described in "Deep JavaScript" (Ch 4, Section 4.1): "An environment is the data structure that the ECMAScript specification uses to manage variables. It is a dictionary whose keys are variable names and whose values are the values of those variables. Each scope has its associated environment." Environments must support three phenomena: recursion, nested scopes, and closures.

# Prerequisites

- None (foundational concept).

# Key Properties

1. A **dictionary** mapping variable names to variable values.
2. Each **scope** has its associated environment.
3. Stored on the **heap** (not the stack), because they may outlive their scope via closures.
4. Must support: **recursion**, **nested scopes**, and **closures**.
5. Contains an `outer` reference linking to the enclosing environment.

# Construction / Recognition

## To Construct/Create:
1. A new environment is created for each function call.
2. A new environment is created for each block scope (with `let`/`const`/`class`).

## To Identify/Recognize:
1. Any scope in JavaScript has a corresponding environment managing its variables.

# Context & Application

Environments are the internal mechanism that makes scoping, closures, and recursion work in JavaScript. Understanding environments explains why closures can access variables from their enclosing scopes even after those scopes have finished executing.

# Examples

**Example 1** (Ch 4): Basic concept:
```js
function f(x) {
  return x * 2;
}
function g(y) {
  const tmp = y + 1;
  return f(tmp);
}
assert.equal(g(3), 8);
```
At pause during `g()` execution: the environment for `g()` contains entries for `y` (value: 3) and `tmp` (value: 4).

**Example 2** (Ch 4): Environments are stored on the heap: "That is necessary because they occasionally live on after execution has left their scopes (we'll see that when exploring *closures*). Therefore, they themselves can't be managed via a stack."

# Relationships

## Builds Upon
- None (foundational concept).

## Enables
- **Execution context** — Execution contexts reference environments.
- **Scope chain** — Environments linked via `outer` form the scope chain.
- **Closure** — Closures keep environments alive beyond their scope's lifetime.

## Related
- **Outer environment reference** — Links environments to form scope chains.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Assuming environments are stack-allocated.
  **Correction**: Environments are heap-allocated because closures may keep them alive after the function returns.

# Common Confusions

- **Confusion**: An environment is the same as a scope.
  **Clarification**: A scope is the region of code where a variable is accessible. An environment is the *data structure* that stores the variables for that scope.

# Source Reference

Chapter 4: Environments: under the hood of variables, Section 4.1, lines 29-45.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition provided
- Cross-reference status: verified against ECMAScript specification references
