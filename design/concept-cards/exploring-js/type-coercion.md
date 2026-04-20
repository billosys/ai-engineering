---
# === CORE IDENTIFICATION ===
concept: Type Coercion
slug: type-coercion

# === CLASSIFICATION ===
category: types-values
subcategory: type-conversion
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Values"
chapter_number: 14
pdf_page: null
section: "14.9.2 Coercion (automatic conversion between types)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - coercion
  - implicit type conversion
  - automatic type conversion

# === TYPED RELATIONSHIPS ===
prerequisites:
  - specification-types
extends: []
related:
  - explicit-type-conversion
  - silent-failures
contrasts_with:
  - explicit-type-conversion

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the `typeof` operator and what does it return for each type?"
---

# Quick Definition

Coercion is JavaScript's automatic conversion of values when an operation receives operands of the wrong type, such as `'7' * '3'` producing `21`.

# Core Definition

"For many operations, JavaScript automatically converts the operands/parameters if their types don't fit. This kind of automatic conversion is called *coercion*." (Ch. 14, &sect;14.9.2). Examples: the multiplication operator coerces strings to numbers; `Number.parseInt()` coerces its parameter to a string. Coercion is related to JavaScript's silent failure pattern.

# Prerequisites

- **specification-types** -- coercion converts between spec types

# Key Properties

1. Automatic (implicit), not programmer-initiated
2. Operators coerce operands: `'7' * '3'` -> `21`
3. Built-in functions coerce: `Number.parseInt(123.45)` -> parses string `'123.45'`
4. Related to silent failures
5. Can produce surprising results
6. Explicit conversion is preferred over relying on coercion

# Construction / Recognition

```js
> '7' * '3'
21              // strings coerced to numbers

> Number.parseInt(123.45)
123             // number coerced to string, then parsed
```

# Context & Application

Coercion is a major source of bugs and confusion. Understanding it helps debug unexpected results. Best practice: use explicit conversions instead of relying on coercion.

# Examples

From the source text (Ch. 14, &sect;14.9.2):
```js
> '7' * '3'
21

> Number.parseInt(123.45)
123
```

The second example: `123.45` is coerced to string `'123.45'`, then parsed as integer `123`.

# Relationships

## Builds Upon
- **specification-types** -- coercion converts between types

## Enables
- Understanding of unexpected JavaScript behavior

## Related
- **silent-failures** -- coercion is a form of silent failure
- **explicit-type-conversion** -- the preferred alternative

## Contrasts With
- **explicit-type-conversion** -- intentional vs. automatic conversion

# Common Errors

- **Error**: Relying on coercion for type conversion (e.g., `+str` to convert to number).
  **Correction**: Use explicit conversion: `Number(str)` is clearer.

# Common Confusions

- **Confusion**: Thinking coercion follows simple rules.
  **Clarification**: Coercion rules are complex and vary by operator. The `+` operator concatenates strings but `*` converts to numbers.

# Source Reference

Chapter 14: Values, Section 14.9.2, lines 889-927.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit definition with surprising examples
- Cross-reference status: verified against Ch. 4 (&sect;4.2.1) and Ch. 7 (&sect;7.4)
