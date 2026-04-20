---
concept: RegExp Disjunction
slug: regexp-disjunction
category: standard-library
subcategory: regexp
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Regular expressions (RegExp)"
chapter_number: 46
pdf_page: null
section: "46.10 Syntax: disjunction (|)"
extraction_confidence: high
aliases:
  - regex alternation
  - regex OR
  - pipe operator
prerequisites:
  - regular-expression-creation
extends: []
related:
  - regexp-capture-groups
contrasts_with: []
answers_questions:
  - "How do I write and use regular expressions in JavaScript?"
---

# Quick Definition

The disjunction operator `|` matches either the pattern on its left or right. It has low precedence -- lower than `^` and `$` -- so grouping with parentheses is often needed.

# Core Definition

"Exploring JavaScript" Ch. 46 warns: "Caveat: this operator has low precedence (binds very weakly). Use groups if necessary." Examples: `^aa|zz$` matches strings starting with `aa` AND/OR ending with `zz`; `^(aa|zz)$` matches exactly `'aa'` or `'zz'`.

# Prerequisites

- **Regular expression creation** -- disjunction is part of regex syntax

# Key Properties

1. `|` matches left or right alternative
2. Very low precedence -- lower than `^` and `$`
3. Use parentheses for precise grouping
4. Works with capture groups `()` or non-capturing groups `(?:)`

# Construction / Recognition

```js
// Matches strings starting with 'aa' and/or ending with 'zz'
/^aa|zz$/
// Matches exactly 'aa' or 'zz'
/^(aa|zz)$/
// Matches 'aaz' or 'azz'
/^a(a|z)z$/
```

(Ch. 46, Section 46.10, lines 1213-1222)

# Context & Application

Used for matching alternative patterns. Grouping is essential for correct behavior.

# Examples

See construction examples above. (Ch. 46, Section 46.10, lines 1218-1222)

# Relationships

## Builds Upon
- **Regular expression creation** -- part of regex syntax

## Related
- **RegExp capture groups** -- often used with disjunction for grouping

# Common Errors

- **Error**: Writing `^aa|bb$` expecting to match exactly 'aa' or 'bb'
  **Correction**: Use `^(aa|bb)$` -- without parentheses, `^` only applies to 'aa' and `$` only to 'bb'

# Common Confusions

- **Confusion**: `|` has the same precedence as other regex operators
  **Clarification**: `|` has the lowest precedence in regex; always use groups for clarity

# Source Reference

Chapter 46: Regular expressions (RegExp), Section 46.10, lines 1213-1222.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit caveat about precedence
- Cross-reference status: verified
