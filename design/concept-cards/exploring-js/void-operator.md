---
# === CORE IDENTIFICATION ===
concept: Void Operator
slug: void-operator

# === CLASSIFICATION ===
category: types-values
subcategory: operators
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Operators"
chapter_number: 15
pdf_page: null
section: "void operator"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - undefined-value
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is `undefined` and how does it differ from `null`?"
---

# Quick Definition

The `void` operator evaluates its operand and returns `undefined`, regardless of what the operand produces.

# Core Definition

The `void` operator evaluates its operand expression (including any side effects) and always returns `undefined` (Ch. 15, Section 15.7.2). It is rarely used in modern JavaScript.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Evaluates its operand (side effects occur)
2. Always returns `undefined`
3. Rarely used in modern JavaScript

# Construction / Recognition

```js
const result = void console.log('evaluated');
// Logs: 'evaluated'
// result is undefined
```

# Context & Application

The `void` operator is mostly a historical artifact. It was used in bookmarklets and `href` attributes (`javascript:void(0)`) to suppress navigation. Modern code rarely needs it.

# Examples

From the source text:

```js
const result = void console.log('evaluated');
assert.equal(result, undefined);
// Output: evaluated
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- Nothing significant in modern JavaScript

## Related
- **undefined-value** — `void` always produces `undefined`

## Contrasts With
- None

# Common Errors

- **Error**: Using `void` when `undefined` would suffice
  **Correction**: Simply use `undefined` directly in modern JavaScript.

# Common Confusions

- **Confusion**: Thinking `void` prevents side effects
  **Clarification**: `void` evaluates its operand fully (including side effects); it only discards the return value.

# Source Reference

Chapter 15: Operators, Section 15.7.2, lines 906-928.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with example
- Cross-reference status: verified
