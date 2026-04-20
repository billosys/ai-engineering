---
# === CORE IDENTIFICATION ===
concept: Strict Equality Operator
slug: strict-equality

# === CLASSIFICATION ===
category: syntax-fundamentals
subcategory: operators
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Syntax"
chapter_number: 9
pdf_page: null
section: "9.1.1.5 Operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "==="
  - "!=="
  - triple equals

# === TYPED RELATIONSHIPS ===
prerequisites:
  - expressions
extends: []
related:
  - primitives-compared-by-value
  - objects-compared-by-identity
  - assert-equal
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the `typeof` operator and what does it return for each type?"
---

# Quick Definition

The strict equality operator (`===`) compares values without type coercion: primitives by value, objects by identity. The book recommends always using `===` instead of `==`.

# Core Definition

`===` evaluates to `true` if two values are equal: for primitives, this means same content; for objects, same identity (Ch. 14, &sect;14.5.3, 14.6.3). "JavaScript also has a `==` comparison operator. I recommend to avoid it" (Ch. 9, &sect;9.1.1.5). The recommendation is "Always use `===` to determine if two values are equal, never `==`." (Ch. 4, &sect;4.3).

# Prerequisites

- **expressions** -- equality operators are expressions

# Key Properties

1. `===`: strict equality (no coercion)
2. `!==`: strict inequality
3. Primitives: compares by value (content)
4. Objects: compares by identity (reference)
5. Always prefer `===` over `==`
6. `==` performs type coercion, leading to surprising results

# Construction / Recognition

```js
assert.equal('abc' === 'abc', true);
assert.equal('abc' !== 'def', true);
assert.equal(3 < 4, true);
```

# Context & Application

`===` is the standard equality check in JavaScript. The `assert.equal()` method uses `===` internally.

# Examples

From the source text (Ch. 9, &sect;9.1.1.5):
```js
assert.equal('abc' === 'abc', true);
assert.equal('abc' !== 'def', true);
```

# Relationships

## Builds Upon
- **expressions** -- equality checks are expressions

## Enables
- **assert-equal** -- uses `===` internally

## Related
- **primitives-compared-by-value** -- `===` compares primitive content
- **objects-compared-by-identity** -- `===` compares object identity

## Contrasts With
- No direct contrast (but `==` is the loose alternative to avoid)

# Common Errors

- **Error**: Using `==` which coerces types: `'' == 0` is `true`.
  **Correction**: Always use `===`: `'' === 0` is `false`.

# Common Confusions

- **Confusion**: Thinking `===` does deep comparison for objects.
  **Clarification**: `===` compares object identity, not content. `{} === {}` is `false`.

# Source Reference

Chapter 9: Syntax, Section 9.1.1.5, lines 193-201. Chapter 4: Section 4.3, lines 117.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit recommendation to use === over ==
- Cross-reference status: verified across Ch. 4, 9, 14
