---
# === CORE IDENTIFICATION ===
concept: Short-Circuit Evaluation (&& and ||)
slug: short-circuit-evaluation

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: operators
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Expressions and Operators"
chapter_number: 4
pdf_page: 101
section: "4.10.1 Logical AND (&&), 4.10.2 Logical OR (||)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "logical AND"
  - "logical OR"
  - "&& operator"
  - "|| operator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primary-expressions
  - operator-precedence
extends: []
related:
  - nullish-coalescing
  - optional-chaining
  - ternary-operator
contrasts_with:
  - nullish-coalescing

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

The `&&` and `||` operators use short-circuit evaluation: `&&` returns its first falsy operand (or the last operand if all are truthy), while `||` returns its first truthy operand (or the last operand if all are falsy). Neither necessarily returns a boolean.

# Core Definition

"The && operator starts by evaluating its first operand. If the value on the left is falsy, the value of the entire expression must also be falsy, so && simply returns the value on the left and does not even evaluate the expression on the right." For `||`: "It starts by evaluating its first operand. If the value of this first operand is truthy, it short-circuits and returns that truthy value without ever evaluating the expression on the right." (Ch. 4, §4.10.1-4.10.2)

# Prerequisites

- **primary-expressions** — Operands are expressions.
- **operator-precedence** — `&&` has higher precedence than `||`.

# Key Properties

1. `&&` returns the first falsy value, or the last value if all are truthy.
2. `||` returns the first truthy value, or the last value if all are falsy.
3. Neither operator necessarily returns `true` or `false` — they return the actual operand value.
4. Right-side operand is not evaluated if the result is determined by the left side.
5. Side effects in the right operand may or may not occur depending on the left.
6. Falsy values: `false`, `null`, `undefined`, `0`, `-0`, `NaN`, `""`.
7. Idiomatic usage: `||` for default values, `&&` for conditional execution.

# Construction / Recognition

```js
a && b     // Returns a if falsy, else b
a || b     // Returns a if truthy, else b
```

# Context & Application

Short-circuit evaluation enables idiomatic patterns like providing default values (`x || defaultValue`), guarding property access (`obj && obj.prop`), and conditional execution (`condition && doSomething()`). Understanding short-circuiting is essential for reading idiomatic JavaScript.

# Examples

From the source text (§4.10.1-4.10.2, pp. 101-103):

```js
let o = {x: 1};
let p = null;
o && o.x     // => 1: o is truthy, so return value of o.x
p && p.x     // => null: p is falsy, so return it (don't evaluate p.x)

// Conditional execution
if (a === b) stop();      // Standard form
(a === b) && stop();      // Equivalent using &&

// Default value idiom
let max = maxWidth || preferences.maxWidth || 500;

// Default parameter (pre-ES6)
p = p || {};
```

# Relationships

## Builds Upon
- **operator-precedence** — `&&` binds tighter than `||`

## Enables
- Guard patterns for safe property access (before optional chaining)
- Default value patterns (before nullish coalescing)

## Related
- **nullish-coalescing** — `??` is a refined alternative to `||` for defaults
- **optional-chaining** — `?.` is a refined alternative to `&&` for property guards
- **ternary-operator** — Another conditional expression form

## Contrasts With
- **nullish-coalescing** — `||` treats `0`, `""`, `false` as falsy; `??` only treats `null`/`undefined` as nullish

# Common Errors

- **Error**: Using `||` for defaults when `0`, `""`, or `false` are valid values.
  **Correction**: Use `??` (nullish coalescing) instead when falsy values should be preserved.

# Common Confusions

- **Confusion**: Believing `&&` and `||` always return boolean `true` or `false`.
  **Clarification**: They return the actual operand value that determined the result. `"hello" || "world"` returns `"hello"`, not `true`.

# Source Reference

Chapter 4: Expressions and Operators, Sections 4.10.1-4.10.2, pages 101-103.

# Verification Notes

- Definition source: Direct quotes from §4.10.1 and §4.10.2
- Confidence rationale: High — detailed three-level explanation of behavior
- Uncertainties: None
- Cross-reference status: Verified
