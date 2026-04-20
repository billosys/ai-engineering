---
# === CORE IDENTIFICATION ===
concept: Optional Chaining
slug: optional-chaining

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
pdf_page: 82
section: "4.4.1 Conditional Property Access"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "conditional property access"
  - "?. operator"
  - "optional chaining operator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-access-expressions
extends:
  - property-access-expressions
related:
  - nullish-coalescing
  - conditional-invocation
  - short-circuit-evaluation
contrasts_with:
  - property-access-expressions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

Optional chaining (`?.` and `?.[]`) provides safe property access that returns `undefined` instead of throwing a TypeError when the value to the left is `null` or `undefined`.

# Core Definition

"In JavaScript, the values null and undefined are the only two values that do not have properties. In a regular property access expression using . or [], you get a TypeError if the expression on the left evaluates to null or undefined. You can use ?. and ?.[] syntax to guard against errors of this type." (Ch. 4, §4.4.1)

# Prerequisites

- **property-access-expressions** — Optional chaining modifies standard property access behavior.

# Key Properties

1. `a?.b` evaluates to `undefined` if `a` is `null` or `undefined`, otherwise evaluates as `a.b`.
2. Short-circuiting: `a.b?.c.d` evaluates to `undefined` without throwing if `a.b` is null/undefined — the entire remaining chain is skipped.
3. Bracket form: `a?.[b][c]` short-circuits the entire chain if `a` is nullish.
4. Parenthesized expressions break the short-circuit: `(a.b?.c).d` will throw if `a.b?.c` is `undefined`.
5. Introduced in ES2020.

# Construction / Recognition

```js
expression?.identifier
expression?.[expression]
```

# Context & Application

Optional chaining is used to safely navigate deeply nested object structures where intermediate properties may be `null` or `undefined`. It replaces verbose guard patterns like `a && a.b && a.b.c`.

# Examples

From the source text (§4.4.1, pp. 82-83):

```js
let a = { b: null };
a.b?.c.d   // => undefined (short-circuits at a.b)

let a = { b: {} };
a.b?.c?.d  // => undefined

// Side effects are skipped during short-circuit
let a;         // undefined
let index = 0;
a?.[index++]   // => undefined: a is undefined
index          // => 0: not incremented because ?.[] short-circuits
```

# Relationships

## Builds Upon
- **property-access-expressions** — Extends standard property access with null-safety

## Enables
- **conditional-invocation** — The `?.()` syntax applies the same concept to function calls

## Related
- **nullish-coalescing** — Often used together: `obj?.prop ?? defaultValue`
- **short-circuit-evaluation** — Optional chaining uses the same short-circuit principle

## Contrasts With
- **property-access-expressions** — Standard `.` throws TypeError on null/undefined; `?.` returns undefined

# Common Errors

- **Error**: Assuming `(a.b?.c).d` is safe when `a.b` is null.
  **Correction**: Parentheses break the short-circuit chain. Use `a.b?.c?.d` instead.

# Common Confusions

- **Confusion**: Believing `?.` checks whether the property exists on the object.
  **Clarification**: `?.` only checks whether the left-hand value is `null` or `undefined`. If the object exists but has no such property, the result is `undefined` (same as regular access), not an error.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.4.1, pages 82-83.

# Verification Notes

- Definition source: Direct quote from §4.4.1
- Confidence rationale: High — detailed section with clear examples and edge cases
- Uncertainties: None
- Cross-reference status: Verified against §6.3.3
