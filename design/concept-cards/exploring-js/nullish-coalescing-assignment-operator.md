---
# === CORE IDENTIFICATION ===
concept: Nullish Coalescing Assignment Operator
slug: nullish-coalescing-assignment-operator

# === CLASSIFICATION ===
category: primitive-types
subcategory: non-values
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "The non-values undefined and null"
chapter_number: 16
pdf_page: null
section: "The nullish coalescing assignment operator (??=)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "??="

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nullish-coalescing-operator
extends:
  - nullish-coalescing-operator
  - assignment-operators
related:
  - logical-assignment-operators
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is `undefined` and how does it differ from `null`?"
---

# Quick Definition

The nullish coalescing assignment operator (`??=`) assigns a default value to a variable only if its current value is `undefined` or `null`. Introduced in ES2021.

# Core Definition

The expression `value ??= defaultValue` is roughly equivalent to `value ?? (value = defaultValue)`. It is short-circuiting: `defaultValue` is only evaluated and assigned if `value` is `undefined` or `null` (Ch. 16, Section 16.4.4).

# Prerequisites

- **nullish-coalescing-operator** -- `??=` builds on `??` semantics

# Key Properties

1. Short-circuiting: right-hand side only evaluated if left is nullish (ES2021)
2. Only assigns for `undefined` or `null`, not other falsy values
3. Equivalent to `a ?? (a = b)`, not `a = a ?? b`

# Construction / Recognition

```js
let value;
value = undefined;
value ??= 'DEFAULT'; // value is now 'DEFAULT'

value = 0;
value ??= 'DEFAULT'; // value remains 0
```

# Context & Application

Use `??=` to fill in missing properties or provide defaults for optional values.

# Examples

From the source text:

```js
const books = [
  { isbn: '123' },
  { title: 'ECMAScript Language Specification', isbn: '456' },
];
for (const book of books) {
  book.title ??= '(Untitled)';
}
// books[0].title is now '(Untitled)'
// books[1].title remains 'ECMAScript Language Specification'
```

# Relationships

## Builds Upon
- **nullish-coalescing-operator** — `??=` is the assignment version of `??`
- **assignment-operators** — one of the logical assignment operators

## Enables
- Concise initialization patterns for missing properties

## Related
- **logical-assignment-operators** — `??=` is part of the ES2021 logical assignment operator family

## Contrasts With
- None

# Common Errors

- **Error**: Expecting `value ??= 'DEFAULT'` to assign when `value` is `0` or `false`
  **Correction**: `??=` only assigns for `undefined` or `null`. Use `||=` if you want to cover all falsy values.

# Common Confusions

- **Confusion**: Thinking `a ??= b` is the same as `a = a ?? b`
  **Clarification**: `a ??= b` is `a ?? (a = b)` -- the assignment is only performed if `a` is nullish. The alternative always performs an assignment.

# Source Reference

Chapter 16: The non-values undefined and null, Section 16.4.4, lines 348-447.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with examples
- Cross-reference status: verified
