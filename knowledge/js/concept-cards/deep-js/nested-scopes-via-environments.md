---
# === CORE IDENTIFICATION ===
concept: Nested Scopes via Environments
slug: nested-scopes-via-environments

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
  - scope nesting

# === TYPED RELATIONSHIPS ===
prerequisites:
  - environment
  - outer-environment-reference
  - scope-internal-slot
extends: []
related:
  - scope-chain
  - closure
  - recursion-via-environments
contrasts_with:
  - recursion-via-environments

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a lexical environment?"
  - "How do lexical environments relate to closures?"
---

# Quick Definition

Nested scopes are implemented via environments linked by `outer` references, where each inner scope's environment points to the enclosing scope's environment, with the connection established through functions' `[[Scope]]` internal property.

# Core Definition

As described in "Deep JavaScript" (Ch 4, Section 4.3): "The scopes are connected. An inner scope 'inherits' all the variables of an outer scope (minus the ones it shadows)." The key insight is that "Nesting scopes as a mechanism is independent of recursion. The latter is best managed by a stack of independent environments. The former is a relationship that each environment has with the environment 'in which' it is created." When a function is called, its new environment's `outer` is set to the value of the function's `[[Scope]]`.

# Prerequisites

- **Environment** — Nested scopes are represented by linked environments.
- **Outer environment reference** — The `outer` field links environments.
- **[[Scope]] internal slot** — Determines the `outer` value for new environments.

# Key Properties

1. Inner scopes "inherit" variables from outer scopes (minus shadowed ones).
2. Implemented via the `outer` field on environments.
3. Independent from recursion — a different mechanism.
4. `outer` is set using the called function's `[[Scope]]` (birth environment).
5. Reflects **static** code structure, not dynamic call patterns.
6. The chain of `outer` references forms the scope chain.

# Construction / Recognition

## To Construct/Create:
1. Define a function inside another function or block.
2. The inner function's environment will have `outer` pointing to the enclosing environment.

## To Identify/Recognize:
1. When a function accesses variables from an enclosing scope, nested scoping via environments is at work.

# Context & Application

The source distinguishes two "aspects of variables" reflected by environments: "First, the chain of outer environments reflects the nested static scopes. Second, the stack of execution contexts reflects what function calls were made, dynamically." This distinction is crucial for understanding closures and lexical scoping.

# Examples

**Example 1** (Ch 4): Three nested scopes:
```js
function f(x) {
  function square() {
    const result = x * x;
    // Pause 3
    return result;
  }
  // Pause 2
  return square();
}
// Pause 1
assert.equal(f(6), 36);
```
At Pause 3: `square`'s env has `outer` → `f`'s env → top-level env. The chain of `outer` references gives access to `result`, `square`, `x`, and `f`.

# Relationships

## Builds Upon
- **Environment** — Nested scopes are implemented via environments.
- **Outer environment reference** — Links form the nesting chain.
- **[[Scope]] internal slot** — Determines the `outer` link.

## Enables
- **Scope chain** — The chain of outer references.
- **Closure** — Functions carry their scope nesting via [[Scope]].
- **Variable shadowing** — Inner environments can redefine names from outer scopes.

## Related
- **Recursion via environments** — Another phenomenon that environments support, but via the execution context stack rather than `outer` references.

## Contrasts With
- **Recursion via environments** — Recursion uses the stack of execution contexts; nesting uses the chain of `outer` references. They are independent mechanisms.

# Common Errors

- **Error**: Assuming nested scope access depends on the call stack.
  **Correction**: Scope nesting is based on the `outer` chain (static/lexical), not the execution context stack (dynamic).

# Common Confusions

- **Confusion**: Nested scopes and recursion are the same mechanism.
  **Clarification**: They are independent. Recursion is handled by the execution context stack (each call creates a new context). Nested scopes are handled by the `outer` chain (each environment links to its enclosing environment). Both use environments but in different ways.

# Source Reference

Chapter 4: Environments: under the hood of variables, Section 4.3, lines 134-240.

# Verification Notes

- Definition source: direct (quoted and illustrated from source)
- Confidence rationale: Central concept of the section with detailed diagrams
- Cross-reference status: verified
