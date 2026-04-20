---
# === CORE IDENTIFICATION ===
concept: Conditional Invocation
slug: conditional-invocation

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: expressions
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Expressions and Operators"
chapter_number: 4
pdf_page: 84
section: "4.5.1 Conditional Invocation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "?.() operator"
  - "optional call"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - invocation-expressions
  - optional-chaining
extends:
  - invocation-expressions
related:
  - optional-chaining
contrasts_with:
  - invocation-expressions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

Conditional invocation (`?.()`) calls a function only if the expression to the left of `?.` is not `null` or `undefined`; otherwise the entire expression evaluates to `undefined` without throwing.

# Core Definition

"In ES2020, you can also invoke a function using ?.() instead of (). Normally when you invoke a function, if the expression to the left of the parentheses is null or undefined or any other non-function, a TypeError is thrown. With the new ?.() invocation syntax, if the expression to the left of the ?. evaluates to null or undefined, then the entire invocation expression evaluates to undefined and no exception is thrown." (Ch. 4, §4.5.1)

# Prerequisites

- **invocation-expressions** — Conditional invocation modifies normal invocation behavior.
- **optional-chaining** — Uses the same `?.` short-circuiting mechanism.

# Key Properties

1. `?.()` only checks for `null` or `undefined` — it does not verify the value is a function.
2. Short-circuiting: argument expressions are not evaluated if the function is nullish.
3. Three distinct patterns: `o.m()` (regular), `o?.m()` (conditional access, regular call), `o.m?.()` (regular access, conditional call).

# Construction / Recognition

```js
log?.(x)           // Call log if it's not null/undefined
o.method?.()       // Call o.method if it exists
```

# Context & Application

Used for optional callbacks, optional method calls, and safely invoking functions that may not be defined, such as optional event handlers or configuration callbacks.

# Examples

From the source text (§4.5.1, pp. 84-85):

```js
function square(x, log) {
    log?.(x);           // Call the function if there is one
    return x * x;
}

// Short-circuiting prevents argument evaluation
let f = null, x = 0;
f?.(x++)   // => undefined: f is null, no exception
x          // => 0: increment is skipped

// Three forms compared:
o.m()      // Regular property access, regular invocation
o?.m()     // Conditional property access, regular invocation
o.m?.()    // Regular property access, conditional invocation
```

# Relationships

## Builds Upon
- **invocation-expressions** — Extends standard invocation with null-safety
- **optional-chaining** — Applies the same `?.` mechanism to function calls

## Enables
- No specific concepts enabled

## Related
- **optional-chaining** — Same family of ES2020 null-safe operators

## Contrasts With
- **invocation-expressions** — Regular `()` throws TypeError on non-functions; `?.()` returns undefined on null/undefined

# Common Errors

- **Error**: Assuming `?.()` validates that the value is actually a function.
  **Correction**: `?.()` only checks for null/undefined. If the value is a non-function (e.g., a number), a TypeError is still thrown.

# Common Confusions

- **Confusion**: Confusing `o?.m()` with `o.m?.()`.
  **Clarification**: `o?.m()` guards against `o` being null. `o.m?.()` guards against `o.m` being null. These are different checks.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.5.1, pages 84-85.

# Verification Notes

- Definition source: Direct quote from §4.5.1
- Confidence rationale: High — detailed examples with clear edge-case discussion
- Uncertainties: None
- Cross-reference status: Verified
