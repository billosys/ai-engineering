---
# === CORE IDENTIFICATION ===
concept: String Comparison
slug: string-comparison

# === CLASSIFICATION ===
category: primitive-types
subcategory: strings
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Strings"
chapter_number: 22
pdf_page: null
section: "Comparing strings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string-type
  - ordering-operators
extends: []
related:
  - unicode-code-units
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

JavaScript compares strings using `<`, `<=`, `>`, `>=` based on UTF-16 code unit values, which differs from dictionary/alphabetical order and does not handle accents or case correctly for human-language sorting.

# Core Definition

"These operators compare based on the numeric values of JavaScript characters. That means that the order that JavaScript uses for strings is different from the one used in dictionaries and phone books." For locale-sensitive comparison, use the ECMAScript Internationalization API (`Intl.Collator`) (Ch. 22, Section 22.6).

# Prerequisites

- **string-type** -- strings are being compared
- **ordering-operators** -- the operators used for comparison

# Key Properties

1. Comparison is by UTF-16 code unit values
2. Case-sensitive: `'a' < 'B'` is `false` (lowercase > uppercase in Unicode)
3. Accent-insensitive: `'ä' < 'b'` is `false`
4. Not suitable for human-language sorting
5. Use `Intl.Collator` for locale-aware comparison

# Construction / Recognition

```js
> 'A' < 'B'   // ok
true
> 'a' < 'B'   // not ok for alphabetical
false
> 'ä' < 'b'   // not ok for German
false
```

# Context & Application

Use default comparison only for programmatic sorting (e.g., sorting identifiers). For user-facing text, use `Intl.Collator`.

# Examples

From the source text:

```js
> 'A' < 'B'
true
> 'a' < 'B'
false
> 'ä' < 'b'
false
```

# Relationships

## Builds Upon
- **string-type** — comparing string values
- **ordering-operators** — the comparison operators

## Enables
- Programmatic string sorting

## Related
- **unicode-code-units** — comparison is by code unit values

## Contrasts With
- None

# Common Errors

- **Error**: Using `<` and `>` for user-facing alphabetical sorting
  **Correction**: Use `Intl.Collator` for locale-aware comparison.

# Common Confusions

- **Confusion**: Thinking JavaScript string comparison is case-insensitive
  **Clarification**: It is strictly by code unit value. Lowercase letters have higher values than uppercase in Unicode.

# Source Reference

Chapter 22: Strings, Section 22.6, lines 1437-1464.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit warning with examples
- Cross-reference status: verified
