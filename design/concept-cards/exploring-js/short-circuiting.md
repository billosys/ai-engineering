---
# === CORE IDENTIFICATION ===
concept: Short-Circuiting
slug: short-circuiting

# === CLASSIFICATION ===
category: primitive-types
subcategory: booleans
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Booleans"
chapter_number: 17
pdf_page: null
section: "Short-circuiting"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "short-circuit evaluation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - falsy-and-truthy-values
extends: []
related:
  - logical-and-operator
  - logical-or-operator
  - nullish-coalescing-operator
  - value-preservation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
---

# Quick Definition

Short-circuiting means that if the first operand of a logical operator already determines the result, the second operand is not evaluated at all.

# Core Definition

"*Short-circuiting* means if the first operand already determines the result, then the second operand is not evaluated." This applies to `&&`, `||`, `??`, and the conditional operator (`? :`). It is significant because the second operand may have side effects that are skipped (Ch. 17, Section 17.5.2).

# Prerequisites

- **falsy-and-truthy-values** -- determines when short-circuiting occurs

# Key Properties

1. `&&` short-circuits if first operand is falsy
2. `||` short-circuits if first operand is truthy
3. `??` short-circuits if first operand is not nullish
4. The conditional operator also delays evaluation of its branches
5. Side effects in the skipped operand do not occur

# Construction / Recognition

```js
const x = false && console.log('hello');
// No output -- console.log is not evaluated

const y = true && console.log('hello');
// Output: hello
```

# Context & Application

Short-circuiting enables guard patterns (`condition && action()`), default value patterns (`value || default`), and is a fundamental performance and correctness property of logical operators.

# Examples

From the source text:

```js
const x = false && console.log('hello');
// No output

const x = true && console.log('hello');
// Output: hello
```

# Relationships

## Builds Upon
- **falsy-and-truthy-values** — determines short-circuit behavior

## Enables
- Guard expressions: `isReady && doWork()`
- Default value patterns: `value || fallback`

## Related
- **logical-and-operator** — uses short-circuiting
- **logical-or-operator** — uses short-circuiting
- **nullish-coalescing-operator** — uses short-circuiting

## Contrasts With
- None

# Common Errors

- **Error**: Relying on side effects in the second operand of `&&` when the first might be falsy
  **Correction**: If the side effect must always occur, do not put it in a short-circuited position.

# Common Confusions

- **Confusion**: Thinking both operands are always evaluated
  **Clarification**: The second operand is only evaluated if the first does not determine the result.

# Source Reference

Chapter 17: Booleans, Section 17.5.2, lines 512-540.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with examples
- Cross-reference status: verified
