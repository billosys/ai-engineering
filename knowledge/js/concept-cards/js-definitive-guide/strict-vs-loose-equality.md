---
# === CORE IDENTIFICATION ===
concept: Strict vs Loose Equality
slug: strict-vs-loose-equality

# === CLASSIFICATION ===
category: type-system
subcategory: equality-semantics
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 63
section: "3.9.1 Conversions and Equality"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "=== vs =="
  - strict equality vs abstract equality
  - triple equals vs double equals

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-coercion
  - primitive-vs-object-types
extends: []
related:
  - null-vs-undefined
  - boolean-truthy-falsy
  - bigint-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes `==` from `===`?"
  - "What is type coercion in JavaScript?"
  - "What distinguishes `null` from `undefined`?"
---

# Quick Definition

The strict equality operator (`===`) compares values without type conversion and requires both type and value to match, while the loose equality operator (`==`) performs type coercion before comparing, leading to surprising results like `"0" == false` being true.

# Core Definition

"The 'strict equality operator,' ===, does not consider its operands to be equal if they are not of the same type, and this is almost always the right operator to use when coding." "Because JavaScript is so flexible with type conversions, it also defines the == operator with a flexible definition of equality." The `==` operator "is deprecated in favor of the strict equality operator ===, which does no type conversions." (pp. 62-63)

# Prerequisites

- **type-coercion** — Must understand how JavaScript converts between types
- **primitive-vs-object-types** — Equality behavior differs for primitives vs objects

# Key Properties

1. `===` (strict): no type conversion; different types are always unequal
2. `==` (loose): performs type coercion before comparison
3. `===` is "almost always the right operator to use" (p. 63)
4. `null == undefined` is `true`; `null === undefined` is `false`
5. `"0" == 0` is `true`; `"0" === 0` is `false`
6. `0 == false` is `true`; `0 === false` is `false`
7. `"0" == false` is `true` (both convert to 0)
8. `0 == 0n` is `true` (BigInt); `0 === 0n` is `false` (different types)
9. Objects compared by reference with both `==` and `===`

# Construction / Recognition

```javascript
// Strict equality (===) — no coercion
"0" === 0          // false: different types
null === undefined // false: different types
0 === false        // false: different types

// Loose equality (==) — with coercion
"0" == 0           // true: string converts to number
null == undefined  // true: treated as equal by spec
0 == false         // true: boolean converts to number
"0" == false       // true: both convert to 0
```

# Context & Application

This is one of the most important distinctions in JavaScript. Best practice is to always use `===` and `!==` to avoid unexpected coercion. The only common exception is `x == null` as a shorthand for `x === null || x === undefined`.

# Examples

From the source text (p. 63):
```javascript
null == undefined  // => true: These two values are treated as equal.
"0" == 0           // => true: String converts to a number before comparing.
0 == false         // => true: Boolean converts to number before comparing.
"0" == false       // => true: Both operands convert to 0 before comparing!
```

From BigInt section (p. 49):
```javascript
0 == 0n            // => true
0 === 0n           // => false: the === checks for type equality as well
```

# Relationships

## Builds Upon
- **type-coercion** — Loose equality uses type coercion
- **primitive-vs-object-types** — Objects are compared by reference in both cases

## Enables
- Defensive coding practices (always use `===`)

## Related
- **null-vs-undefined** — Key example: `null == undefined` but `null !== undefined`
- **boolean-truthy-falsy** — Understanding why `0 == false` is true
- **bigint-type** — `0 == 0n` demonstrates cross-type loose equality

## Contrasts With
- `===` contrasts with `==` — this is the card's core content

# Common Errors

- **Error**: Using `==` to compare values and getting unexpected `true` results.
  **Correction**: Always use `===` unless you specifically want type coercion.

- **Error**: Assuming `undefined == false` is true because undefined is falsy.
  **Clarification**: "The == operator never attempts to convert its operands to booleans" (p. 63). `undefined == false` is actually `false`.

# Common Confusions

- **Confusion**: `==` converts both operands to the same type.
  **Clarification**: The rules are specific to operand combinations. `==` does not simply convert to boolean. `null == undefined` is a special case — null only loosely equals undefined and nothing else.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.9.1, pages 63. Also §4.9.1.

# Verification Notes

- Definition source: Direct quotes from pp. 62-63
- Confidence rationale: High — clearly defined with examples
- Uncertainties: Detailed `==` algorithm deferred to §4.9.1
- Cross-reference status: Verified
