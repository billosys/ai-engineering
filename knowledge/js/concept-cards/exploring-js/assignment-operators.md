---
# === CORE IDENTIFICATION ===
concept: Assignment Operators
slug: assignment-operators

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
section: "Assignment operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "compound assignment"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - logical-assignment-operators
  - nullish-coalescing-assignment-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
---

# Quick Definition

Assignment operators store values in variables, properties, or array elements. Compound assignment operators combine an operation with assignment, such as `+=` for add-and-assign.

# Core Definition

The plain assignment operator (`=`) stores a value in a storage location. Compound assignment operators combine an operation with assignment. For most operators, `myvar op= value` is equivalent to `myvar = myvar op value`. Logical assignment operators (`||=`, `&&=`, `??=`) are different: they short-circuit, only assigning if a condition is met (Ch. 15, Section 15.4).

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Plain assignment: `x = value`, `obj.propKey = value`, `arr[index] = value` (ES1)
2. Arithmetic compound: `+= -= *= /= %=` (ES1), `**=` (ES2016)
3. Bitwise compound: `&= ^= |=` (ES1)
4. Shift compound: `<<= >>= >>>=` (ES1)
5. Logical compound: `||= &&= ??=` (ES2021) -- these short-circuit

# Construction / Recognition

```js
let str = '';
str += '<b>';
str += 'Hello!';
str += '</b>';
// str is '<b>Hello!</b>'
```

# Context & Application

Compound assignment operators provide concise syntax for common update patterns. The logical assignment operators introduced in ES2021 are especially useful for providing defaults and conditional assignments.

# Examples

From the source text:

```js
let str = '';
str += '<b>';
str += 'Hello!';
str += '</b>';
assert.equal(str, '<b>Hello!</b>');
```

Logical assignment operators (ES2021):
- `a ||= b` is equivalent to `a || (a = b)` -- assigns if `a` is falsy
- `a &&= b` is equivalent to `a && (a = b)` -- assigns if `a` is truthy
- `a ??= b` is equivalent to `a ?? (a = b)` -- assigns if `a` is nullish

# Relationships

## Builds Upon
- No strict prerequisites

## Enables
- **logical-assignment-operators** — specialized subset of assignment operators
- **nullish-coalescing-assignment-operator** — `??=` combines nullish coalescing with assignment

## Related
- **plus-operator** — `+=` uses the plus operator's dual behavior

## Contrasts With
- None

# Common Errors

- **Error**: Thinking `a ||= b` is equivalent to `a = a || b`
  **Correction**: It is `a || (a = b)` -- the assignment only happens if `a` is falsy. The latter always performs an assignment.

# Common Confusions

- **Confusion**: Treating all compound operators as having the same semantics
  **Clarification**: Logical assignment operators (`||=`, `&&=`, `??=`) short-circuit and may not perform the assignment at all, unlike arithmetic compound operators.

# Source Reference

Chapter 15: Operators, Section 15.4, lines 252-410.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definitions and equivalence tables in source
- Cross-reference status: verified
