---
# === CORE IDENTIFICATION ===
concept: Closure
slug: closure

# === CLASSIFICATION ===
category: functions
subcategory: advanced-functions
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Functions"
chapter_number: 3
pdf_page: null
section: "Closure"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - closures
  - lexical closure

# === TYPED RELATIONSHIPS ===
prerequisites:
  - scope
  - local-scope
  - nested-scope
  - lexical-scoping
  - function-definition
extends:
  - lexical-scoping
related:
  - higher-order-function
  - arrow-function
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a closure?"
  - "What must I know before understanding closures?"
  - "How does lexical scoping relate to closures?"
---

# Quick Definition

A closure is a function that references bindings from local scopes around it, retaining access to those bindings even after the enclosing function has returned.

# Core Definition

As defined in "Eloquent JavaScript" (Ch 3, lines 526-531 of 03-functions.md): "This feature -- being able to reference a specific instance of a local binding in an enclosing scope -- is called *closure*. A function that references bindings from local scopes around it is called *a* closure. This behavior not only frees you from having to worry about the lifetimes of bindings but also makes it possible to use function values in some creative ways."

Further (lines 554-559): "A good mental model is to think of function values as containing both the code in their body and the environment in which they are created. When called, the function body sees the environment in which it was created, not the environment in which it is called."

# Prerequisites

- **scope**: Understanding what scope is.
- **local-scope**: Closures capture local bindings.
- **nested-scope**: Closures arise from nested functions accessing outer scope bindings.
- **lexical-scoping**: Closures work because JavaScript uses lexical scoping.
- **function-definition**: Closures are functions.

# Key Properties

1. A closure retains access to bindings from its enclosing scope even after that scope's function has returned.
2. Local bindings are created **anew** for every function call -- different calls produce independent closures.
3. Function values contain both their code AND the environment in which they were created.
4. Closures enable functions that "remember" values from their creation context.

# Construction / Recognition

## To Construct/Create:
1. Define a function inside another function.
2. Have the inner function reference a binding from the outer function.
3. Return the inner function (or pass it elsewhere).

## To Identify/Recognize:
- A function that accesses bindings not defined in its own body or parameters, but in an enclosing scope.

# Context & Application

Closures are fundamental to many JavaScript patterns: factory functions, private state, callbacks, and higher-order functions. They enable data encapsulation without classes and are used extensively in functional programming patterns.

# Examples

**Example 1** (Ch 3, lines 504-516 of 03-functions.md) -- wrapValue:
```javascript
function wrapValue(n) {
  let local = n;
  return () => local;
}

let wrap1 = wrapValue(1);
let wrap2 = wrapValue(2);
console.log(wrap1());
// → 1
console.log(wrap2());
// → 2
```

**Example 2** (Ch 3, lines 538-546 of 03-functions.md) -- multiplier:
```javascript
function multiplier(factor) {
  return number => number * factor;
}

let twice = multiplier(2);
console.log(twice(5));
// → 10
```
"`multiplier` is called and creates an environment in which its `factor` parameter is bound to 2. The function value it returns, which is stored in `twice`, remembers this environment."

# Relationships

## Builds Upon
- **lexical-scoping** -- Closures work because of lexical scoping.
- **nested-scope** -- Closures arise from nested functions.
- **local-scope** -- Closures capture local bindings.

## Enables
- **higher-order-function** -- Many higher-order functions create closures.
- Factory functions, private state patterns, and callback patterns.

## Related
- **arrow-function** -- Arrow functions are commonly used as closures.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Expecting all closures from the same function to share the same binding values.
  **Correction**: Each call to the enclosing function creates new binding instances, so closures from different calls are independent.

# Common Confusions

- **Confusion**: Closures copy the values of bindings at the time they are created.
  **Clarification**: Closures reference the bindings themselves, not copies. If the binding's value changes, the closure sees the new value.

# Source Reference

Chapter 3: Functions, Section "Closure", lines 489-567 of 03-functions.md (book.md line 2297).

# Verification Notes

- Definition source: direct (quoted from lines 526-531)
- Confidence rationale: Explicit definition with italicized term "closure"
- Cross-reference status: verified against nested-scope and lexical-scoping sections
