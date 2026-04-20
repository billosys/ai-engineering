---
# === CORE IDENTIFICATION ===
concept: Execution Context
slug: execution-context

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
aliases:
  - call stack entry

# === TYPED RELATIONSHIPS ===
prerequisites:
  - environment
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

An execution context is a stack-managed reference to an environment, created for each function call and used to track which environment is currently active.

# Core Definition

As described in "Deep JavaScript" (Ch 4, Section 4.2): "For each function call, you need fresh storage space for the variables (parameters and local variables) of the called function. This is managed via a stack of so-called *execution contexts*, which are references to environments." Execution contexts form a stack — pushed on function call, popped on return. The environments they reference are stored on the heap because they may outlive the execution context (via closures).

# Prerequisites

- **Environment** — Execution contexts reference environments.

# Key Properties

1. Managed via a **stack** (the call stack).
2. Each entry is a **reference** to an environment (not the environment itself).
3. Pushed when a function is called; popped when a function returns.
4. The top of the stack indicates the currently executing scope.
5. The referenced environment is on the heap (may outlive the execution context).

# Construction / Recognition

## To Construct/Create:
1. Call a function — a new execution context is pushed onto the stack.

## To Identify/Recognize:
1. Each entry in the call stack is an execution context.

# Context & Application

The execution context stack (call stack) is what enables recursion — each recursive call gets its own execution context pointing to a fresh environment. Stack overflow errors occur when too many execution contexts are pushed without being popped.

# Examples

**Example 1** (Ch 4): Call stack with three pauses:
```js
function f(x) {
  // Pause 3 — stack has 3 entries
  return x * 2;
}
function g(y) {
  const tmp = y + 1;
  // Pause 2 — stack has 2 entries
  return f(tmp);
}
// Pause 1 — stack has 1 entry (top-level)
assert.equal(g(3), 8);
```
At Pause 1: stack = [top-level env]. At Pause 2: stack = [top-level env, g's env]. At Pause 3: stack = [top-level env, g's env, f's env].

# Relationships

## Builds Upon
- **Environment** — Each execution context references an environment.

## Enables
- **Recursion** — The stack of execution contexts supports recursive calls.
- **Call stack debugging** — Stack traces reflect the execution context stack.

## Related
- **Scope chain** — The current execution context determines the starting environment for scope chain lookups.
- **Closure** — Execution contexts are popped on return, but environments may persist via closures.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Assuming the environment is destroyed when the execution context is popped.
  **Correction**: The execution context is stack-managed, but the environment is on the heap and may persist if referenced by a closure.

# Common Confusions

- **Confusion**: Execution context and environment are the same thing.
  **Clarification**: An execution context is a stack entry that *references* an environment. The environment is the actual variable storage. One is stack-managed; the other is heap-managed.

# Source Reference

Chapter 4: Environments: under the hood of variables, Section 4.2, lines 47-131.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with diagrams
- Cross-reference status: verified
