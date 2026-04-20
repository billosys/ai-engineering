---
concept: RegExp Unicode Property Escapes
slug: regexp-unicode-property-escapes
category: standard-library
subcategory: regexp
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Regular expressions (RegExp)"
chapter_number: 46
pdf_page: null
section: "46.5.2 Unicode property escapes"
extraction_confidence: high
aliases:
  - "\\p{} escape"
  - Unicode property matching
prerequisites:
  - regular-expression-creation
  - regexp-flags
extends: []
related:
  - regexp-character-class-escapes
contrasts_with: []
answers_questions:
  - "How do I write and use regular expressions in JavaScript?"
---

# Quick Definition

Unicode property escapes (`\p{PropertyName}` and `\P{PropertyName}`) match characters based on Unicode properties like `White_Space`, `Letter`, or `Script=Greek`, requiring flag `/u` or `/v`. Introduced in ES2018.

# Core Definition

"Exploring JavaScript" Ch. 46: "Positive escape: \p{UP} matches Unicode characters or Unicode strings that have the Unicode property UP. Negative escape: \P{UP} matches Unicode characters that do not have the Unicode property UP." Two kinds: Unicode character properties (sets of code points, `/u` or `/v`) and Unicode string properties (sets of code point sequences, `/v` only, ES2024).

# Prerequisites

- **Regular expression creation** -- these are regex pattern elements
- **RegExp flags** -- require `/u` or `/v` flag

# Key Properties

1. Introduced in ES2018 (character properties), ES2024 (string properties)
2. Require flag `/u` or `/v`
3. `\p{prop=value}` for named properties, `\p{bin_prop}` for binary properties
4. `\P{}` is the negation (not supported for string properties)
5. Unicode string properties (e.g., `RGI_Emoji`) only with flag `/v`

# Construction / Recognition

```js
> /^\p{White_Space}+$/v.test('\t \n\r')
true
> /^\p{Script=Greek}+$/v.test('meta')
true
> '1pi2ue3e4'.replace(/\p{Letter}/gv, '')
'1234'
```

(Ch. 46, Section 46.5.3, lines 669-699)

# Context & Application

Essential for internationalized text processing. Allows matching based on character properties rather than hardcoded ranges.

# Examples

```js
> /^\p{RGI_Emoji}$/v.test('face_with_spiral_eyes') // 3 code points
true // with /v flag
```

(Ch. 46, Section 46.5.4, lines 759-767)

# Relationships

## Builds Upon
- **Regular expression creation** -- part of regex syntax
- **RegExp flags** -- requires Unicode flags

## Related
- **RegExp character class escapes** -- `\p{}` extends the escape mechanism

# Common Errors

- **Error**: Using `\p{}` without a Unicode flag
  **Correction**: Must use `/u` or `/v` flag for Unicode property escapes

# Common Confusions

- **Confusion**: `\p{Emoji}` matches all emoji including multi-code-point sequences
  **Clarification**: `\p{Emoji}` (character property) only matches single code points; use `\p{RGI_Emoji}` (string property) with `/v` for sequences

# Source Reference

Chapter 46: Regular expressions (RegExp), Section 46.5.2-46.5.4, lines 594-799.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit definitions with character vs string property distinction
- Cross-reference status: verified
