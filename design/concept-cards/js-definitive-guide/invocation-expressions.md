---
# === CORE IDENTIFICATION ===
concept: Invocation Expressions
slug: invocation-expressions

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: expressions
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Expressions and Operators"
chapter_number: 4
pdf_page: 83
section: "4.5 Invocation Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "function call"
  - "method invocation"
  - "function invocation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primary-expressions
  - function-definition-expressions
  - property-access-expressions
extends: []
related:
  - conditional-invocation
  - new-operator
contrasts_with:
  - new-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

An invocation expression calls (executes) a function or method, consisting of a function expression followed by parenthesized arguments. It evaluates to the function's return value or `undefined`.

# Core Definition

"An *invocation expression* is JavaScript's syntax for calling (or executing) a function or method. It starts with a function expression that identifies the function to be called. The function expression is followed by an open parenthesis, a comma-separated list of zero or more argument expressions, and a close parenthesis." (Ch. 4, §4.5)

# Prerequisites

- **primary-expressions** — The function being invoked is referenced via an expression.
- **function-definition-expressions** — Understanding what functions are.
- **property-access-expressions** — Method invocations use property access syntax.

# Key Properties

1. The function expression is evaluated first, then argument expressions left to right.
2. If the function expression value is not a function, a TypeError is thrown.
3. If the function uses `return`, its value becomes the invocation expression's value; otherwise `undefined`.
4. When the function expression is a property access, the invocation is a *method invocation* and the object becomes the value of `this`.
5. Invocation expressions have higher precedence than any operator.

# Construction / Recognition

```js
f(0)              // Function invocation
Math.max(x,y,z)  // Method invocation
a.sort()          // Method invocation with no arguments
```

# Context & Application

Invocation expressions are used constantly in JavaScript to execute functions. The distinction between function invocation and method invocation is critical for understanding `this` binding.

# Examples

From the source text (§4.5, pp. 83-84):

```js
f(0)              // f is the function expression; 0 is the argument expression.
Math.max(x,y,z)  // Math.max is the function; x, y, and z are the arguments.
a.sort()          // a.sort is the function; there are no arguments.
```

# Relationships

## Builds Upon
- **property-access-expressions** — Method invocations combine property access with invocation

## Enables
- **conditional-invocation** — `?.()` adds null-safety to invocation

## Related
- **new-operator** — Object creation expressions are invocations prefixed with `new`

## Contrasts With
- **new-operator** — Regular invocation calls a function; `new` invocation creates an object and calls a constructor

# Common Errors

- **Error**: Invoking a value that is not a function.
  **Correction**: Ensure the expression before `()` evaluates to a function; use `typeof` to check or `?.()` to guard.

# Common Confusions

- **Confusion**: Not distinguishing function invocation from method invocation.
  **Clarification**: In method invocations (where the function is accessed via property access), the object becomes `this`. In plain function invocations, `this` is `undefined` in strict mode or the global object otherwise.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.5, pages 83-85.

# Verification Notes

- Definition source: Direct quote from §4.5
- Confidence rationale: High — clearly defined with examples
- Uncertainties: Full `this` binding details deferred to Ch. 8 and Ch. 9
- Cross-reference status: Verified
