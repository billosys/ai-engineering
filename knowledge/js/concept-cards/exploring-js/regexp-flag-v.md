---
concept: RegExp Flag /v (Unicode Sets)
slug: regexp-flag-v
category: standard-library
subcategory: regexp
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Regular expressions (RegExp)"
chapter_number: 46
pdf_page: null
section: "46.11.4 Flag /v: limited support for multi-code-point grapheme clusters"
extraction_confidence: high
aliases:
  - unicodeSets flag
  - "/v flag"
prerequisites:
  - regular-expression-creation
  - regexp-flags
extends: []
related:
  - regexp-unicode-property-escapes
  - regexp-character-classes
contrasts_with: []
answers_questions:
  - "How do I write and use regular expressions in JavaScript?"
---

# Quick Definition

Flag `/v` (ES2024) is the recommended Unicode flag for regular expressions. It improves on `/u` by supporting Unicode string property escapes (`\p{RGI_Emoji}`), character class set operations (`--`, `&&`), code point sequence literals (`\q{}`), and improved case-insensitive matching.

# Core Definition

"Exploring JavaScript" Ch. 46: "This flag improves many aspects of JavaScript's regular expressions and should be used by default." Flag `/v` "builds on the improvements brought by flag /u and fixes several of its shortcomings." It is mutually exclusive with `/u`. "I recommend to use flag /v with all regular expressions."

# Prerequisites

- **Regular expression creation** -- `/v` is a regex flag
- **RegExp flags** -- `/v` is one of the available flags

# Key Properties

1. Introduced in ES2024
2. Recommended for all regular expressions
3. Supports Unicode string properties (`\p{RGI_Emoji}`) for multi-code-point matches
4. Supports `\q{}` for code point sequence literals in character classes
5. Supports set operations: subtraction (`--`) and intersection (`&&`)
6. Fixes case-insensitive matching quirks of `/u`
7. Mutually exclusive with `/u`

# Construction / Recognition

```js
> /^\p{RGI_Emoji}$/v.test('emoji_with_3_code_points')
true // matches multi-code-point emoji

> /^[\w--[a-g]]$/v.test('h')
true // set subtraction

> /[\p{ASCII}&&\p{Letter}]/v.test('D')
true // set intersection
```

(Ch. 46, Section 46.11.4, lines 1688-1835)

# Context & Application

Use `/v` on all new regular expressions for the best Unicode support and most features.

# Examples

See construction examples above. (Ch. 46, Section 46.11.4, lines 1763-1787)

# Relationships

## Builds Upon
- **Regular expression creation** -- a flag applied to regex
- **RegExp flags** -- one of the available flags

## Related
- **RegExp Unicode property escapes** -- enabled by `/v`
- **RegExp character classes** -- set operations enabled by `/v`

# Common Errors

- **Error**: Using both `/u` and `/v` flags
  **Correction**: They are mutually exclusive; use `/v` which supersedes `/u`

# Common Confusions

- **Confusion**: `/v` is just an alias for `/u`
  **Clarification**: `/v` adds significant new features beyond `/u`: string properties, set operations, `\q{}`

# Source Reference

Chapter 46: Regular expressions (RegExp), Section 46.11.4, lines 1688-1835.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit recommendation with detailed feature list
- Cross-reference status: verified
