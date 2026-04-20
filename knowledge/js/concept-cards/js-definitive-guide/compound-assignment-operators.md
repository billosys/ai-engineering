---
# === CORE IDENTIFICATION ===
concept: Compound Assignment Operators
slug: compound-assignment-operators

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
pdf_page: 104
section: "4.11.1 Assignment with Operation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "assignment with operation"
  - "augmented assignment"
  - "op-assign operators"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primary-expressions
  - operator-precedence
extends: []
related:
  - addition-operator
  - bitwise-operators
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

Compound assignment operators (like `+=`, `-=`, `*=`) combine an arithmetic or bitwise operation with assignment, providing a shorthand for `a = a op b`.

# Core Definition

"Besides the normal = assignment operator, JavaScript supports a number of other assignment operators that provide shortcuts by combining assignment with some other operation. For example, the += operator performs addition and assignment." In the form `a op= b`, the expression `a` is evaluated only once (unlike `a = a op b` where `a` is evaluated twice). (Ch. 4, §4.11.1)

# Prerequisites

- **primary-expressions** — The left operand must be an lvalue.
- **operator-precedence** — Assignment operators have very low precedence and right-to-left associativity.

# Key Properties

1. Available: `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `<<=`, `>>=`, `>>>=`, `&=`, `|=`, `^=`.
2. `a op= b` is mostly equivalent to `a = a op b`, but `a` is evaluated only once.
3. The single-evaluation difference matters when `a` has side effects: `data[i++] *= 2` differs from `data[i++] = data[i++] * 2`.
4. `+=` works for both addition and string concatenation.

# Construction / Recognition

```js
total += salesTax;    // Same as total = total + salesTax
count -= 1;           // Same as count = count - 1
```

# Context & Application

Compound assignment is a common shorthand in loops, accumulators, and any situation where a variable is updated relative to its current value.

# Examples

From the source text (§4.11.1, pp. 104-105):

```js
total += salesTax;    // Equivalent to: total = total + salesTax

// Side-effect difference:
data[i++] *= 2;               // i incremented once
data[i++] = data[i++] * 2;   // i incremented twice (different behavior!)
```

# Relationships

## Builds Upon
- **addition-operator** — `+=` inherits the dual behavior of `+`

## Enables
- Concise loop body expressions, accumulator patterns

## Related
- **bitwise-operators** — Bitwise compound assignments: `&=`, `|=`, `^=`, `<<=`, `>>=`, `>>>=`

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Assuming `a op= b` is always identical to `a = a op b`.
  **Correction**: When `a` involves side effects (like `i++`), the single-evaluation form differs.

# Common Confusions

- **Confusion**: Confusing `=` (assignment) with `==` or `===` (equality).
  **Clarification**: `=` assigns a value; `==` and `===` compare values. This is a perennial source of bugs.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.11.1, pages 104-105.

# Verification Notes

- Definition source: Direct quote from §4.11.1
- Confidence rationale: High — complete operator table and clear explanation
- Uncertainties: None
- Cross-reference status: Verified
