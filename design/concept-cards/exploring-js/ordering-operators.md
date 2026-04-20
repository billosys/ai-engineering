---
# === CORE IDENTIFICATION ===
concept: Ordering Operators
slug: ordering-operators

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
section: "Ordering operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "comparison operators"
  - "relational operators"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - operator-coercion
extends: []
related:
  - strict-equality-operator
  - string-comparison
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert between JavaScript types (string, number, boolean)?"
---

# Quick Definition

JavaScript's ordering operators (`<`, `<=`, `>`, `>=`) compare both numbers and strings, with `<=` and `>=` based on strict equality semantics.

# Core Definition

The ordering operators compare values for relative ordering. They work for both numbers and strings. The `<=` and `>=` operators are based on strict equality. Importantly, these operators do not work well for comparing text in human languages -- capitalization and accents produce unexpected results (Ch. 15, Section 15.6).

# Prerequisites

- **operator-coercion** -- ordering operators coerce operands

# Key Properties

1. Four operators: `<`, `<=`, `>`, `>=` (ES1)
2. Work for both numbers and strings
3. `<=` and `>=` based on strict equality
4. Not suitable for locale-sensitive text comparison

# Construction / Recognition

```js
5 >= 2       // true
'bar' < 'foo' // true (lexicographic comparison by code unit values)
```

# Context & Application

Use ordering operators for numeric comparisons and simple ASCII string comparisons. For human-language text comparison, use the ECMAScript Internationalization API (`Intl`).

# Examples

From the source text:

```js
> 5 >= 2
true
> 'bar' < 'foo'
true
```

# Relationships

## Builds Upon
- **operator-coercion** — operands are coerced as needed

## Enables
- Sorting algorithms and conditional logic

## Related
- **strict-equality-operator** — `<=` and `>=` are based on strict equality
- **string-comparison** — string ordering uses code unit values

## Contrasts With
- None

# Common Errors

- **Error**: Using `<` or `>` to sort strings with accents or mixed case
  **Correction**: Use `Intl.Collator` for locale-sensitive string comparison.

# Common Confusions

- **Confusion**: Thinking string comparison is alphabetical
  **Clarification**: Comparison is by UTF-16 code unit values, so `'a' < 'B'` is `false` (lowercase letters have higher code unit values than uppercase).

# Source Reference

Chapter 15: Operators, Section 15.6, lines 762-866.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with table of operators
- Cross-reference status: verified against Ch. 22 string comparison section
