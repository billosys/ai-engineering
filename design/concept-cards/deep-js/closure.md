---
# === CORE IDENTIFICATION ===
concept: Closure
slug: closure

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
  - lexical closure

# === TYPED RELATIONSHIPS ===
prerequisites:
  - environment
  - outer-environment-reference
  - scope-internal-slot
extends: []
related:
  - scope-chain
  - currying
  - partial-application
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a closure?"
  - "How do lexical environments relate to closures?"
---

# Quick Definition

A closure is a function that retains access to variables from its birth scope even after execution has left that scope, enabled by the function's `[[Scope]]` keeping the birth environment alive on the heap.

# Core Definition

As described in "Deep JavaScript" (Ch 4, Section 4.4): A closure occurs when "the function created in line A does not lose the connection to its birth scope when it leaves that scope. The associated environment is kept alive by that connection and the function still has access to variable `x` in that environment (`x` is free inside the function)." The mechanism works through the `[[Scope]]` internal property, which points to the function's birth environment. When the function is called later, its new environment's `outer` links back to the birth environment, maintaining access to the enclosing variables.

# Prerequisites

- **Environment** — Closures work by keeping environments alive.
- **Outer environment reference** — The `outer` chain enables access to enclosing variables.
- **[[Scope]] internal slot** — The mechanism that connects a function to its birth environment.

# Key Properties

1. A function retains access to variables from the scope where it was **created**.
2. The birth environment persists on the **heap** even after its scope finishes executing.
3. The `[[Scope]]` property of the function keeps the birth environment **alive**.
4. Free variables (variables used but not defined in the function) are resolved via the scope chain.
5. Multiple closures over the same scope share the same environment.

# Construction / Recognition

## To Construct/Create:
1. Define a function inside another function.
2. The inner function references variables from the outer function.
3. Return or otherwise export the inner function so it outlives the outer scope.

## To Identify/Recognize:
1. A function accesses variables not defined in its own scope.
2. The function is used outside the scope where those variables were defined.

# Context & Application

Closures are fundamental to JavaScript patterns including: module patterns, event handlers, callbacks, partial application, currying, data privacy, and factory functions. They are the reason that functions in JavaScript are "first-class" in the fullest sense — they carry their environment with them.

# Examples

**Example 1** (Ch 4): Creating a closure:
```js
function add(x) {
  return (y) => {
    return x + y;
  };
}
assert.equal(add(3)(1), 4);
```
The arrow function is a closure over `x`. When `add(3)` returns, the arrow function retains access to `x` (which is 3) through its `[[Scope]]`.

**Example 2** (Ch 4): Partial application via closures:
```js
const plus2 = add(2);
assert.equal(plus2(5), 7);
```
`plus2` is the closure returned by `add(2)`. Its `[[Scope]]` points to `add(2)`'s environment where `x === 2`. When `plus2(5)` is called, the new environment's `outer` links to that environment, giving access to `x`.

# Relationships

## Builds Upon
- **Environment** — Closures keep environments alive on the heap.
- **Outer environment reference** — The `outer` chain connects the closure's environment to its birth environment.
- **[[Scope]] internal slot** — The mechanism that preserves the birth environment reference.

## Enables
- **Currying** — Converting multi-parameter functions into nested single-parameter closures.
- **Partial application** — Pre-filling some arguments of a function via closures.
- **Module pattern** — Using closures to create private state.
- **Data privacy** — Variables in the enclosing scope are private to the closure.

## Related
- **Scope chain** — Closures access variables through the scope chain.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Closures in loops with `var` capture the same variable.
  **Correction**: Use `let` (which creates a new binding per iteration) or create a new scope with an IIFE.

# Common Confusions

- **Confusion**: Closures capture the *value* of variables.
  **Clarification**: Closures capture the *environment* (i.e., the variable binding itself, not a snapshot of its value). Changes to the variable are visible to the closure, and changes by the closure are visible outside.

- **Confusion**: Every function is a closure.
  **Clarification**: Technically in JavaScript every function captures its lexical environment via `[[Scope]]`. However, the term "closure" is most meaningful when a function accesses free variables from an enclosing scope that has finished executing.

# Source Reference

Chapter 4: Environments: under the hood of variables, Section 4.4, lines 243-347.

# Verification Notes

- Definition source: direct (described in source with examples and diagrams)
- Confidence rationale: Central topic of the section with detailed walkthrough
- Cross-reference status: verified
