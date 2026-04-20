---
concept: RegExp Character Class Set Operations
slug: regexp-character-class-set-operations
category: standard-library
subcategory: regexp
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Regular expressions (RegExp)"
chapter_number: 46
pdf_page: null
section: "46.6.2 Set operations for character classes"
extraction_confidence: high
aliases:
  - regex set operations
  - character class subtraction
  - character class intersection
prerequisites:
  - regexp-character-classes
  - regexp-flag-v
extends: []
related:
  - regexp-unicode-property-escapes
contrasts_with: []
answers_questions:
  - "How do I write and use regular expressions in JavaScript?"
---

# Quick Definition

With flag `/v` (ES2024), character classes support set operations: subtraction (`--`) removes characters from a set, intersection (`&&`) keeps only characters in both sets, and union is achieved by placing sets side by side.

# Core Definition

"Exploring JavaScript" Ch. 46: "Flag /v enables set operations for character classes." Subtraction: `[\w--[a-g]]` matches word characters except a-g. Intersection: `[\p{ASCII}&&\p{Letter}]` matches ASCII letters only. Union: `[\p{Emoji_Keycap_Sequence}[a-z]]`. Character classes can also be nested.

# Prerequisites

- **RegExp character classes** -- set operations extend character classes
- **RegExp flag /v** -- required for set operations

# Key Properties

1. Introduced in ES2024 (requires flag `/v`)
2. Subtraction: `[A--B]` -- characters in A but not B
3. Intersection: `[A&&B]` -- characters in both A and B
4. Union: `[AB]` -- characters in A or B (juxtaposition)
5. Nesting: character classes can contain other character classes

# Construction / Recognition

```js
> /^[\w--[a-g]]$/v.test('h')  // true (word chars minus a-g)
> /^[\w--[a-g]]$/v.test('a')  // false
> /[\p{ASCII}&&\p{Letter}]/v.test('D')  // true (ASCII + Letter)
> /[\p{ASCII}&&\p{Letter}]/v.test('Delta')  // false (Greek, not ASCII)
```

(Ch. 46, Section 46.6.2, lines 963-1012)

# Context & Application

Set operations enable precise character set definitions that would be difficult or impossible to express otherwise, especially for Unicode-aware matching.

# Examples

See construction examples above. (Ch. 46, Section 46.6.2, lines 963-1012)

# Relationships

## Builds Upon
- **RegExp character classes** -- extends their capabilities
- **RegExp flag /v** -- required to enable set operations

## Related
- **RegExp Unicode property escapes** -- commonly used with set operations

# Common Errors

- **Error**: Using set operations without flag `/v`
  **Correction**: Set operations require flag `/v`; they are not available with `/u` or no flag

# Common Confusions

- **Confusion**: `&&` in character classes is the same as JavaScript's `&&` operator
  **Clarification**: In character classes, `&&` means set intersection, not logical AND

# Source Reference

Chapter 46: Regular expressions (RegExp), Section 46.6.2, lines 930-1025.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with examples for each operation
- Cross-reference status: verified
