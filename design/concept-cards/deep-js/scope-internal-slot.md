---
# === CORE IDENTIFICATION ===
concept: "[[Scope]] Internal Slot"
slug: scope-internal-slot

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
section: "4.3 Nested scopes via environments"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "[[Scope]]"
  - birth environment reference
  - internal scope property

# === TYPED RELATIONSHIPS ===
prerequisites:
  - environment
  - outer-environment-reference
extends: []
related:
  - scope-chain
  - closure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a lexical environment?"
  - "How do lexical environments relate to closures?"
---

# Quick Definition

`[[Scope]]` is an internal property of every function that points to the environment where the function was created (its "birth environment"), used to set up the `outer` reference when the function is called.

# Core Definition

As described in "Deep JavaScript" (Ch 4, Section 4.3): "To help set up the field `outer` of environments created via function calls, each function has an internal property named `[[Scope]]` that points to its 'birth environment'." When a function is called and a new environment is created, the new environment's `outer` field is set to the value of the called function's `[[Scope]]`. This is the mechanism that makes lexical (static) scoping work.

# Prerequisites

- **Environment** — [[Scope]] points to an environment.
- **Outer environment reference** — [[Scope]] is used to initialize the `outer` field.

# Key Properties

1. An **internal** property of every function (not accessible from user code).
2. Set at **function creation time** — points to the current environment when the function is created.
3. Used to initialize the `outer` field of new environments during function calls.
4. Never changes after function creation.
5. Key mechanism for **lexical scoping** and **closures**.

# Construction / Recognition

## To Construct/Create:
1. When a function is created, its `[[Scope]]` is automatically set to the current environment.

## To Identify/Recognize:
1. Internal mechanism — observable through closure behavior and lexical scoping.

# Context & Application

`[[Scope]]` is the bridge between function creation and function execution. It captures the environment at creation time and carries it forward, so when the function is later called (possibly in a different context), the new environment correctly links back to the defining scope. This is the fundamental mechanism behind closures.

# Examples

**Example 1** (Ch 4): Function creation captures [[Scope]]:
```js
function f(x) {
  function square() {
    const result = x * x;
    return result;
  }
  return square();
}
```
When `square` is created inside `f(6)`, `square.[[Scope]]` points to `f`'s environment (containing `x: 6`). When `square()` is called, the new environment's `outer` is set to `square.[[Scope]]` — giving `square` access to `x`.

**Example 2** (Ch 4): Closure via [[Scope]]:
```js
function add(x) {
  return (y) => { return x + y; };
}
const plus2 = add(2);
```
The arrow function's `[[Scope]]` points to `add(2)`'s environment (containing `x: 2`). When `plus2(5)` is called, the new environment's `outer` links back to `add(2)`'s environment via `[[Scope]]`.

# Relationships

## Builds Upon
- **Environment** — [[Scope]] references an environment.
- **Outer environment reference** — [[Scope]] provides the value for `outer`.

## Enables
- **Lexical scoping** — [[Scope]] ensures functions access their defining scope, not their calling scope.
- **Closure** — [[Scope]] keeps the birth environment alive and accessible.

## Related
- **Scope chain** — [[Scope]] determines where a function's scope chain begins.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Trying to access `[[Scope]]` directly in JavaScript.
  **Correction**: `[[Scope]]` is an internal slot, not accessible via user code. Its effects are observable through closure behavior.

# Common Confusions

- **Confusion**: [[Scope]] changes when a function is assigned to a new variable or passed as an argument.
  **Clarification**: [[Scope]] is set once at function creation and never changes, regardless of how the function is later used or where it is called.

# Source Reference

Chapter 4: Environments: under the hood of variables, Section 4.3, lines 169-173.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with diagrams showing the mechanism
- Cross-reference status: verified
