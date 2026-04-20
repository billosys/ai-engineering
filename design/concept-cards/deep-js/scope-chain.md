---
# === CORE IDENTIFICATION ===
concept: Scope Chain
slug: scope-chain

# === CLASSIFICATION ===
category: language-mechanics
subcategory: scoping
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
  - environment chain
  - outer chain

# === TYPED RELATIONSHIPS ===
prerequisites:
  - environment
  - outer-environment-reference
extends: []
related:
  - closure
  - scope-internal-slot
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a lexical environment?"
  - "How do lexical environments relate to closures?"
---

# Quick Definition

The scope chain is the linked list of environments connected via `outer` references, representing all variables accessible from a given point in the code.

# Core Definition

As described in "Deep JavaScript" (Ch 4, Section 4.3): "The whole chain of outer environments contains all variables that can currently be accessed (minus shadowed variables)." The scope chain is formed by following `outer` references from the current environment through all enclosing environments to the global environment. Variable lookup traverses this chain: "we first search for its name in the current environment, then in the outer environment, then in the outer environment's outer environment, etc."

# Prerequisites

- **Environment** — The scope chain is composed of environments.
- **Outer environment reference** — The `outer` field links environments into a chain.

# Key Properties

1. Formed by following `outer` references from current to global environment.
2. Contains all variables accessible from the current scope.
3. Variable lookup goes from innermost to outermost.
4. Shadowing occurs when an inner environment has the same variable name as an outer one.
5. Terminates at the global environment (whose `outer` is `null`).
6. Reflects **static** (lexical) nesting, not dynamic call order.

# Construction / Recognition

## To Construct/Create:
1. Start from the current environment.
2. Follow `outer` references to build the chain.

## To Identify/Recognize:
1. The set of variables accessible at any point in code corresponds to the scope chain.

# Context & Application

The scope chain explains variable resolution in JavaScript. When a variable is referenced, the engine walks the scope chain to find the first binding. This is why inner functions can access outer variables, and why variable shadowing works. The chain also explains why closures retain access to enclosing variables.

# Examples

**Example 1** (Ch 4): Scope chain during `square()` execution:
```js
function f(x) {
  function square() {
    const result = x * x;
    return result;
  }
  return square();
}
assert.equal(f(6), 36);
```
During `square()`: the chain is [square's env → f's env → top-level env]. From square's env, we can access `result`, `square`, `x`, and `f` by traversing the chain.

# Relationships

## Builds Upon
- **Environment** — The chain is made of environments.
- **Outer environment reference** — The link between environments.

## Enables
- **Variable resolution** — Variables are found by traversing the scope chain.
- **Closure** — Closures work because the scope chain persists via environment references.

## Related
- **[[Scope]] internal slot** — Determines the starting point for the outer chain when new environments are created.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Assuming the scope chain reflects the call stack.
  **Correction**: The scope chain reflects lexical nesting (where functions are defined), not the dynamic call stack (where functions are called from).

# Common Confusions

- **Confusion**: Variables are inherited from the calling function.
  **Clarification**: JavaScript uses lexical scoping. A function's scope chain is based on where it was defined, not where it is called. This is why closures work correctly.

# Source Reference

Chapter 4: Environments: under the hood of variables, Section 4.3, lines 134-240.

# Verification Notes

- Definition source: synthesized (described through examples and diagrams)
- Confidence rationale: High because the concept is thoroughly illustrated with diagrams
- Cross-reference status: verified
