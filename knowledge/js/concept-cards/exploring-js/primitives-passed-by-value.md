---
# === CORE IDENTIFICATION ===
concept: Primitives Passed by Value
slug: primitives-passed-by-value

# === CLASSIFICATION ===
category: types-values
subcategory: primitives
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Values"
chapter_number: 14
pdf_page: null
section: "14.5.2 Primitives are passed by value"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - pass by value

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primitive-values
extends:
  - primitive-values
related:
  - primitives-compared-by-value
contrasts_with:
  - objects-passed-by-identity

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

Primitives are passed by value: when assigned to a variable or passed to a function, their contents are copied, so changes to the copy don't affect the original.

# Core Definition

"Primitives are *passed by value*: variables (including parameters) store the contents of the primitives. When assigning a primitive value to a variable or passing it as an argument to a function, its content is copied." (Ch. 14, &sect;14.5.2). Due to immutability, the difference between passing by value and passing by identity is unobservable for primitives.

# Prerequisites

- **primitive-values** -- this describes how primitives are handled

# Key Properties

1. Variable stores the actual value (content)
2. Assignment copies the content
3. Function argument passing copies the content
4. Difference from "passing by identity" is unobservable for primitives (because they're immutable)

# Construction / Recognition

```js
const x = 123;
const y = x;
// y is the same as any other number 123
assert.equal(y, 123);
```

# Context & Application

Pass-by-value means primitives are independent copies. Modifying one variable doesn't affect another.

# Examples

From the source text (Ch. 14, &sect;14.5.2):
```js
const x = 123;
const y = x;
assert.equal(y, 123);
```

# Relationships

## Builds Upon
- **primitive-values** -- passing behavior of primitives

## Enables
- Understanding value independence

## Related
- **primitives-compared-by-value** -- comparison also works on content

## Contrasts With
- **objects-passed-by-identity** -- objects share identity, not content

# Common Errors

- **Error**: Expecting changes to a primitive variable to affect other variables holding the same value.
  **Correction**: Primitives are independent copies; changes don't propagate.

# Common Confusions

- **Confusion**: Thinking "pass by value" and "pass by identity" are different for primitives.
  **Clarification**: Because primitives are immutable, the distinction is unobservable in practice.

# Source Reference

Chapter 14: Values, Section 14.5.2, lines 169-198.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit definition with note on unobservability
- Cross-reference status: verified
