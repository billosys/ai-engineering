---
concept: RegExp Pattern Modifiers
slug: regexp-pattern-modifiers
category: standard-library
subcategory: regexp
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Regular expressions (RegExp)"
chapter_number: 46
pdf_page: null
section: "46.12 Pattern modifiers (inline flags)"
extraction_confidence: high
aliases:
  - inline flags
  - regex modifiers
prerequisites:
  - regular-expression-creation
  - regexp-flags
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How do I write and use regular expressions in JavaScript?"
---

# Quick Definition

Pattern modifiers (ES2025) allow applying flags `i`, `m`, or `s` to only part of a regular expression using the syntax `(?ims-ims:pattern)`, enabling fine-grained flag control within a single regex.

# Core Definition

"Exploring JavaScript" Ch. 46: "Pattern modifiers let us apply a flag to a part of a regular expression (vs. all of the regular expression)." Syntax: `(?ims-ims:pattern)` where flags after `?` are activated and flags after `-` are deactivated. Only `i`, `m`, and `s` flags are supported. Without any flags, it becomes a non-capturing group: `(?:pattern)`. Introduced in ES2025.

# Prerequisites

- **Regular expression creation** -- modifiers are part of regex syntax
- **RegExp flags** -- modifiers apply/remove flags locally

# Key Properties

1. Introduced in ES2025
2. Syntax: `(?ims-ims:pattern)` -- activate and/or deactivate flags
3. Only `i`, `m`, `s` flags are supported in modifiers
4. Use case: make only part of a regex case-insensitive
5. Without flags, equivalent to non-capturing group `(?:pattern)`

# Construction / Recognition

```js
> /^x(?i:HELLO)x$/.test('xHELLOx')  // true
> /^x(?i:HELLO)x$/.test('xhellox')  // true
> /^x(?i:HELLO)x$/.test('XhelloX')  // false (x is still case-sensitive)
```

(Ch. 46, Section 46.12, lines 1845-1851)

# Context & Application

Useful for matching patterns where only specific parts should be case-insensitive or have different flag behavior.

# Examples

See construction example above. (Ch. 46, Section 46.12, lines 1845-1851)

# Relationships

## Builds Upon
- **Regular expression creation** -- syntax element
- **RegExp flags** -- local flag control

# Common Errors

- **Error**: Trying to use flag `g` or `v` in a pattern modifier
  **Correction**: Only `i`, `m`, and `s` are supported in pattern modifiers

# Common Confusions

- **Confusion**: Pattern modifiers change the flag for the entire regex
  **Clarification**: Modifiers only apply to the pattern inside the group

# Source Reference

Chapter 46: Regular expressions (RegExp), Section 46.12, lines 1837-1989.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with syntax and examples
- Cross-reference status: verified
