---
# === CORE IDENTIFICATION ===
concept: Outer Environment Reference
slug: outer-environment-reference

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
  - outer reference
  - outer field

# === TYPED RELATIONSHIPS ===
prerequisites:
  - environment
extends: []
related:
  - scope-chain
  - scope-internal-slot
  - closure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a lexical environment?"
  - "How do lexical environments relate to closures?"
---

# Quick Definition

The outer environment reference is a field in every environment that points to the environment of the surrounding (enclosing) scope, forming a chain that enables nested scope variable lookup.

# Core Definition

As described in "Deep JavaScript" (Ch 4, Section 4.3): "The environment of each scope points to the environment of the surrounding scope via a field called `outer`." When looking up a variable, the engine searches the current environment first, then follows the `outer` chain: "When we are looking up the value of a variable, we first search for its name in the current environment, then in the outer environment, then in the outer environment's outer environment, etc." This chain contains all currently accessible variables (minus shadowed ones).

# Prerequisites

- **Environment** — The outer reference is a field within environments.

# Key Properties

1. A field named `outer` in each environment.
2. Points to the environment of the **enclosing** (surrounding) scope.
3. Forms a **chain** of environments representing nested scopes.
4. Variable lookup traverses this chain.
5. Set up using the function's `[[Scope]]` internal property during function calls.
6. The global environment's `outer` is `null`.

# Construction / Recognition

## To Construct/Create:
1. When a function is called, a new environment is created.
2. Its `outer` is set to the function's `[[Scope]]` (its birth environment).

## To Identify/Recognize:
1. The chain of environments reachable via `outer` references from any given environment.

# Context & Application

The outer reference mechanism is what makes nested scoping and closures possible. It establishes the connection between a function's local environment and the environment where the function was defined, enabling access to variables from enclosing scopes.

# Examples

**Example 1** (Ch 4): Three nested scopes:
```js
function f(x) {
  function square() {
    const result = x * x; // accesses x via outer chain
    return result;
  }
  return square();
}
```
The environment for `square()` has `outer` pointing to the environment for `f()`, which has `outer` pointing to the top-level environment. This chain allows `square()` to access `x`.

# Relationships

## Builds Upon
- **Environment** — Outer reference is a field within environments.

## Enables
- **Scope chain** — The chain of outer references forms the scope chain.
- **Closure** — Outer references keep enclosing environments accessible.
- **Variable shadowing** — Inner environments can shadow variables from outer ones.

## Related
- **[[Scope]] internal slot** — Used to set the `outer` field when creating new environments.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Assuming `outer` is set based on the call site (dynamic scoping).
  **Correction**: `outer` is set based on where the function was **defined** (lexical/static scoping), via the function's `[[Scope]]` property.

# Common Confusions

- **Confusion**: The outer reference changes when a function is called from different locations.
  **Clarification**: The outer reference is determined by the function's `[[Scope]]`, which is fixed at function creation time. JavaScript uses lexical (static) scoping, not dynamic scoping.

# Source Reference

Chapter 4: Environments: under the hood of variables, Section 4.3, lines 134-240.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit description with diagrams
- Cross-reference status: verified
