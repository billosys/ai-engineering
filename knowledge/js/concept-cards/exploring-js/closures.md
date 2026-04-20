---
# === CORE IDENTIFICATION ===
concept: Closures
slug: closures

# === CLASSIFICATION ===
category: variables-scope
subcategory: closures
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Variables and assignment"
chapter_number: 13
pdf_page: null
section: "13.9.2 What is a closure?"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - closure
  - lexical closure

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variable-scope
  - bound-vs-free-variables
  - static-vs-dynamic
extends: []
related:
  - arrow-function-expressions
  - function-declarations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

A closure is a function plus a connection to the variables that exist at its "birth place," allowing it to access free variables from its enclosing scope even after that scope has finished executing.

# Core Definition

"A *closure* is a function plus a connection to the variables that exist at its 'birth place'." (Ch. 13, &sect;13.9.2). The connection provides values for the function's free variables. "Static scoping is supported via closures in JavaScript. Therefore, every function is a closure." (Ch. 13, &sect;13.9.2, tip box). Closures enable three main use cases: providing context data for callbacks, storing state across function calls, and providing private data for objects.

# Prerequisites

- **variable-scope** -- closures capture scope
- **bound-vs-free-variables** -- closures provide values for free variables
- **static-vs-dynamic** -- closures implement static (lexical) scoping

# Key Properties

1. Every JavaScript function is a closure
2. Closures capture the variables (bindings) at their birth scope
3. Free variables are resolved via the closure's scope connection
4. Closures can both read and write to captured variables
5. State persists across function calls via closure variables
6. Influenced by Scheme (Ch. 4, &sect;4.1)

# Construction / Recognition

```js
function funcFactory(value) {
  return () => {
    return value; // `value` is a free variable, provided by closure
  };
}
const func = funcFactory('abc');
assert.equal(func(), 'abc'); // closure retains access to `value`
```

# Context & Application

Closures are used for callbacks with context, factory functions, module patterns, and encapsulation of private state.

# Examples

From the source text (Ch. 13, &sect;13.9.2-13.9.3):

Basic closure:
```js
function funcFactory(value) {
  return () => {
    return value;
  };
}
const func = funcFactory('abc');
assert.equal(func(), 'abc');
```

Incrementor factory (state via closure):
```js
function createInc(startValue) {
  return (step) => {
    startValue += step;
    return startValue;
  };
}
const inc = createInc(5);
assert.equal(inc(2), 7);
```

# Relationships

## Builds Upon
- **variable-scope** -- closures capture scope chain
- **bound-vs-free-variables** -- closures provide free variable values
- **static-vs-dynamic** -- closures implement static scoping

## Enables
- Factory functions
- Callback context
- Private state encapsulation
- Module pattern

## Related
- **arrow-function-expressions** -- commonly used to create closures
- **function-declarations** -- also create closures

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Expecting closures to capture values, not bindings.
  **Correction**: Closures capture bindings (variables), so if the variable changes, the closure sees the new value.

# Common Confusions

- **Confusion**: Thinking closures only work with arrow functions.
  **Clarification**: All JavaScript functions are closures, including function declarations and function expressions.

# Source Reference

Chapter 13: Variables and assignment, Section 13.9.2, lines 1095-1129.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit definition with "all functions are closures" tip
- Cross-reference status: verified against Ch. 4 (Scheme influence)
