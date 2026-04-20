---
concept: RegExp Capture Groups
slug: regexp-capture-groups
category: standard-library
subcategory: regexp
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Regular expressions (RegExp)"
chapter_number: 46
pdf_page: null
section: "46.7 Syntax: capture groups"
extraction_confidence: high
aliases:
  - regex groups
  - named capture groups
prerequisites:
  - regular-expression-creation
extends: []
related:
  - regexp-quantifiers
  - regexp-methods
contrasts_with: []
answers_questions:
  - "How do I write and use regular expressions in JavaScript?"
---

# Quick Definition

Capture groups extract sub-matches from a regex match: numbered groups `(pattern)` are referenced by index or `\1`, named groups `(?<name>pattern)` (ES2018) by name or `\k<name>`, and non-capturing groups `(?:pattern)` group without capturing.

# Core Definition

"Exploring JavaScript" Ch. 46 lists three types: "Numbered capture group: (a+), Backreference: \1, \2, etc. Named capture group (ES2018): (?<as>a+), Backreference: \k<as>. Noncapturing group: (?:a+)."

# Prerequisites

- **Regular expression creation** -- groups are pattern elements

# Key Properties

1. Numbered groups: `(pattern)` -- referenced by position `\1`, `\2`
2. Named groups: `(?<name>pattern)` -- referenced by `\k<name>` (ES2018)
3. Non-capturing groups: `(?:pattern)` -- grouping without capturing
4. Groups appear in match objects as indexed entries and `.groups` property
5. Named groups recommended for readability

# Construction / Recognition

```js
// Numbered group
/(\w+) (\w+)/

// Named group (ES2018)
/(?<first>\w+) (?<last>\w+)/

// Non-capturing group
/(?:https?|ftp):\/\//
```

(Ch. 46, Section 46.7, lines 1026-1032)

# Context & Application

Capture groups extract structured data from text: parsing dates, URLs, log entries, etc.

# Examples

From the source:
- `(a+)` captures one or more 'a' characters
- `(?<as>a+)` captures with name "as"
- `\1` backreferences the first capture

(Ch. 46, Section 46.7, lines 1026-1032)

# Relationships

## Builds Upon
- **Regular expression creation** -- groups are part of regex syntax

## Related
- **RegExp methods** -- match objects contain group captures

# Common Errors

- **Error**: Using a capturing group when only grouping is needed
  **Correction**: Use `(?:...)` for grouping without capturing to avoid unwanted captures

# Common Confusions

- **Confusion**: Backreferences match the same pattern again
  **Clarification**: Backreferences match the exact same text that was captured, not the pattern

# Source Reference

Chapter 46: Regular expressions (RegExp), Section 46.7, lines 1026-1032.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit enumeration of three types
- Cross-reference status: verified
