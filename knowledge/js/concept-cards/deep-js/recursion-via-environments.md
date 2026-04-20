---
# === CORE IDENTIFICATION ===
concept: Recursion via Environments
slug: recursion-via-environments

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
section: "4.2 Recursion via environments"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - environment
  - execution-context
extends: []
related:
  - scope-chain
  - closure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a lexical environment?"
---

# Quick Definition

Recursion in JavaScript is supported by creating a fresh environment for each function call, with execution contexts managed via a stack that grows with each call and shrinks with each return.

# Core Definition

As described in "Deep JavaScript" (Ch 4, Section 4.2): "For each function call, you need fresh storage space for the variables (parameters and local variables) of the called function. This is managed via a stack of so-called *execution contexts*, which are references to environments." Each recursive call pushes a new execution context onto the stack, pointing to a new environment with its own parameter and local variable bindings. When a function returns, its execution context is popped.

# Prerequisites

- **Environment** — Each call creates a fresh environment.
- **Execution context** — The stack manages which environment is active.

# Key Properties

1. Each function call creates a **new environment** for its parameters and locals.
2. Execution contexts form a **stack** that tracks active function calls.
3. The stack grows on each call and shrinks on each return.
4. Environments are on the heap; execution contexts reference them from the stack.
5. Recursive calls simply add more entries to both stack and heap.

# Construction / Recognition

## To Construct/Create:
1. Call a function — a new execution context and environment are created.
2. Recursive calls repeat this process.

## To Identify/Recognize:
1. Multiple execution contexts for the same function in the stack indicate recursion.

# Context & Application

Understanding recursion through environments explains why each recursive call has its own independent copies of parameters and local variables, and why stack overflow occurs with too-deep recursion (too many execution contexts on the stack).

# Examples

**Example 1** (Ch 4): Step-by-step execution:
```js
function f(x) {
  // Pause 3: stack = [top-level, g's env, f's env]
  return x * 2;
}
function g(y) {
  const tmp = y + 1;
  // Pause 2: stack = [top-level, g's env]
  return f(tmp);
}
// Pause 1: stack = [top-level]
assert.equal(g(3), 8);
```
At Pause 3: three execution contexts on the stack, each referencing its own environment. `g`'s environment has `y: 3, tmp: 4`. `f`'s environment has `x: 4`.

# Relationships

## Builds Upon
- **Environment** — Fresh environment per call.
- **Execution context** — Stack-managed references to environments.

## Enables
- **Understanding stack overflows** — Too-deep recursion exhausts the execution context stack.

## Related
- **Scope chain** — Each environment also has `outer` references for scope.
- **Closure** — Environments that persist beyond their function's return.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Assuming recursive calls share the same variable storage.
  **Correction**: Each call has its own environment. Variables in different recursive calls are independent.

# Common Confusions

- **Confusion**: The call stack and environments are the same thing.
  **Clarification**: The call stack contains execution contexts (references). Environments are the actual variable storage on the heap. They are separate data structures with different lifetimes.

# Source Reference

Chapter 4: Environments: under the hood of variables, Section 4.2, lines 47-131.

# Verification Notes

- Definition source: direct (quoted and illustrated from source)
- Confidence rationale: Detailed explanation with diagrams
- Cross-reference status: verified
