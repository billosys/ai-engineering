---
# === CORE IDENTIFICATION ===
concept: Strict Equality
slug: strict-equality

# === CLASSIFICATION ===
category: fundamentals
subcategory: operators
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Values, Types, and Operators"
chapter_number: 1
pdf_page: null
section: "Automatic type conversion"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - strict comparison
  - precise equality
  - triple equals

# === TYPED RELATIONSHIPS ===
prerequisites:
  - comparison-operators
  - type-coercion
extends:
  - comparison-operators
related:
  - type-coercion
contrasts_with:
  - loose-equality

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes == and ===?"
  - "What is type coercion?"
---

# Quick Definition

The strict equality operator (`===`) tests whether a value is precisely equal to another without performing any type conversion, and `!==` tests for precise inequality.

# Core Definition

As described in "Eloquent JavaScript" (Ch 1, lines 612-615 of 01-values-types-and-operators.md): "When you do *not* want any type conversions to happen, there are two additional operators: `===` and `!==`. The first tests whether a value is *precisely* equal to the other, and the second tests whether it is not precisely equal. Thus `\"\" === false` is false, as expected."

# Prerequisites

- **Comparison Operators** -- `===` and `!==` are comparison operators.
- **Type Coercion** -- Understanding why strict equality exists requires understanding coercion.

# Key Properties

1. `===` tests for **precise equality** -- no type conversion (line 613).
2. `!==` tests for **precise inequality** -- no type conversion (line 614).
3. `"" === false` is `false` (different types), while `"" == false` is `true` (coercion) (lines 611, 615).
4. The source recommends using `===` "defensively to prevent unexpected type conversions from tripping you up" (lines 618-619).
5. When types on both sides are known to be the same, `==` is acceptable (lines 620-621).

# Construction / Recognition

## To Construct/Create:
1. Use `===` for equality: `value === "hello"`.
2. Use `!==` for inequality: `value !== 0`.

## To Identify/Recognize:
1. Three-character comparison operators: `===` or `!==`.

# Context & Application

Strict equality is the recommended default comparison in JavaScript because it avoids the confusing implicit type conversions that `==` performs. Most style guides and linters recommend `===` over `==`.

# Examples

**Example 1** (Ch 1, lines 611-615): Strict vs. loose equality:
```js
// With ==, type coercion makes this true:
0 == false     // true
"" == false    // true

// With ===, no coercion:
"" === false   // false
```

**Example 2** (Ch 1, lines 618-621): The source's recommendation: "I recommend using the three-character comparison operators defensively to prevent unexpected type conversions from tripping you up."

# Relationships

## Builds Upon
- **Comparison Operators** -- `===` and `!==` are specialized comparison operators.
- **Type Coercion** -- Strict equality exists specifically to avoid coercion.

## Enables
- Safer, more predictable conditional logic.

## Related
- **Type Coercion** -- The problem that strict equality solves.

## Contrasts With
- **Loose Equality** (`==`, `!=`) -- Performs type coercion before comparing.

# Common Errors

- **Error**: Using `==` and getting unexpected `true` results from type coercion.
  **Correction**: Use `===` to avoid implicit conversions. For example, `0 == ""` is `true` but `0 === ""` is `false`.

# Common Confusions

- **Confusion**: `===` is always needed.
  **Clarification**: "When you're certain the types on both sides will be the same, there is no problem with using the shorter operators" (lines 620-621). However, `===` is safer as a default.

# Source Reference

Chapter 1: Values, Types, and Operators, Section "Automatic type conversion", lines 608-621 of 01-values-types-and-operators.md (book.md line 595).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with recommendation
- Cross-reference status: verified within chapter
