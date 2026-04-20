---
concept: RegExp Quantifiers
slug: regexp-quantifiers
category: standard-library
subcategory: regexp
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Regular expressions (RegExp)"
chapter_number: 46
pdf_page: null
section: "46.8 Syntax: quantifiers"
extraction_confidence: high
aliases:
  - regex quantifiers
  - greedy vs reluctant
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

Quantifiers specify how many times a pattern element should match: `?` (0-1), `*` (0+), `+` (1+), `{n}` (exactly n), `{n,}` (n+), `{n,m}` (n to m). By default greedy (match as much as possible); append `?` for reluctant (match as little as possible).

# Core Definition

"Exploring JavaScript" Ch. 46 lists all quantifiers and notes: "By default, all of the following quantifiers are greedy (they match as many characters as possible)." Adding `?` makes them reluctant: "so that they match as few characters as possible."

# Prerequisites

- **Regular expression creation** -- quantifiers are part of regex syntax

# Key Properties

1. `?` -- 0 or 1 times
2. `*` -- 0 or more times
3. `+` -- 1 or more times
4. `{n}` -- exactly n times
5. `{n,}` -- n or more times
6. `{n,m}` -- n to m times
7. Greedy by default; append `?` for reluctant

# Construction / Recognition

```js
> /X.*X/.exec('XabcXdefX')[0]   // greedy
'XabcXdefX'
> /X.*?X/.exec('XabcXdefX')[0]  // reluctant
'XabcX'
```

(Ch. 46, Section 46.8, lines 1049-1054)

# Context & Application

Quantifiers control repetition in patterns. The greedy vs reluctant distinction is critical for correct matching.

# Examples

See construction examples above. (Ch. 46, Section 46.8, lines 1049-1054)

# Relationships

## Builds Upon
- **Regular expression creation** -- quantifiers are pattern syntax

# Common Errors

- **Error**: Using `.*` to match "everything" when you want the shortest match
  **Correction**: Use `.*?` (reluctant) or a negated character class like `[^"]*`

# Common Confusions

- **Confusion**: Greedy quantifiers always consume the entire string
  **Clarification**: Greedy quantifiers try to match as much as possible while still allowing the overall pattern to match

# Source Reference

Chapter 46: Regular expressions (RegExp), Section 46.8, lines 1034-1055.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit list with greedy/reluctant distinction
- Cross-reference status: verified
