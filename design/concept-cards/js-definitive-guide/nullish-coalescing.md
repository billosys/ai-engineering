---
# === CORE IDENTIFICATION ===
concept: Nullish Coalescing Operator (??)
slug: nullish-coalescing

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: operators
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Expressions and Operators"
chapter_number: 4
pdf_page: 109
section: "4.13.2 First-Defined (??)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "first-defined operator"
  - "?? operator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - short-circuit-evaluation
extends: []
related:
  - optional-chaining
  - operator-precedence
contrasts_with:
  - short-circuit-evaluation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

The nullish coalescing operator (`??`) returns its left operand if it is not `null` or `undefined`; otherwise it returns the right operand. Unlike `||`, it does not treat `0`, `""`, or `false` as triggering the fallback.

# Core Definition

"The first-defined operator ?? evaluates to its first defined operand: if its left operand is not null and not undefined, it returns that value. Otherwise, it returns the value of the right operand." (Ch. 4, §4.13.2) Formally called the "nullish coalescing" operator, introduced in ES2020.

# Prerequisites

- **short-circuit-evaluation** — `??` is similar to `||` but with narrower null-checking semantics.

# Key Properties

1. Only `null` and `undefined` trigger the fallback — `0`, `""`, `false` are returned as-is.
2. Short-circuiting: second operand is only evaluated if first is nullish.
3. Cannot be mixed with `&&` or `||` without explicit parentheses (SyntaxError).
4. Equivalent to: `(a !== null && a !== undefined) ? a : b`.

# Construction / Recognition

```js
a ?? b            // Returns a if defined, else b
(a ?? b) || c     // Parentheses required when mixing with ||
```

# Context & Application

`??` is the correct operator for providing default values when `0`, empty string, or `false` are valid values. It replaces the `||` idiom that incorrectly treats all falsy values as "missing."

# Examples

From the source text (§4.13.2, pp. 109-110):

```js
let options = { timeout: 0, title: "", verbose: false, n: null };
options.timeout ?? 1000    // => 0: as defined in the object
options.title ?? "Untitled" // => "": as defined in the object
options.verbose ?? true     // => false: as defined in the object
options.quiet ?? false      // => false: property is not defined
options.n ?? 10             // => 10: property is null

// Contrast with ||:
// options.timeout || 1000 would return 1000 (wrong!)

// Must use parentheses with && or ||
(a ?? b) || c   // OK
a ?? (b || c)   // OK
a ?? b || c     // SyntaxError
```

# Relationships

## Builds Upon
- **short-circuit-evaluation** — Same short-circuiting mechanism but with different triggering conditions

## Enables
- Correct default value patterns for configuration objects

## Related
- **optional-chaining** — Often used together: `obj?.prop ?? defaultValue`
- **operator-precedence** — Requires parentheses when mixed with `&&` or `||`

## Contrasts With
- **short-circuit-evaluation** — `||` treats all falsy values as triggers; `??` only treats `null`/`undefined`

# Common Errors

- **Error**: Mixing `??` with `||` or `&&` without parentheses.
  **Correction**: Always use explicit parentheses: `(a ?? b) || c`.

# Common Confusions

- **Confusion**: Believing `??` and `||` are interchangeable.
  **Clarification**: `0 ?? 1` returns `0`; `0 || 1` returns `1`. The difference matters when `0`, `""`, or `false` are valid values.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.13.2, pages 109-110.

# Verification Notes

- Definition source: Direct quote from §4.13.2
- Confidence rationale: High — detailed examples with contrast to ||
- Uncertainties: None
- Cross-reference status: Verified
