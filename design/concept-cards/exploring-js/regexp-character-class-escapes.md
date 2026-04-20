---
concept: RegExp Character Class Escapes
slug: regexp-character-class-escapes
category: standard-library
subcategory: regexp
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Regular expressions (RegExp)"
chapter_number: 46
pdf_page: null
section: "46.5 Syntax: character class escapes"
extraction_confidence: high
aliases:
  - "\\d \\w \\s escapes"
  - shorthand character classes
prerequisites:
  - regular-expression-creation
extends: []
related:
  - regexp-character-classes
  - regexp-unicode-property-escapes
contrasts_with: []
answers_questions:
  - "How do I write and use regular expressions in JavaScript?"
---

# Quick Definition

Character class escapes are shorthand notations for common character sets: `\d` (digits, `[0-9]`), `\w` ("word" characters, `[a-zA-Z0-9_]`), `\s` (whitespace), and their complements `\D`, `\W`, `\S`.

# Core Definition

"Exploring JavaScript" Ch. 46 lists the basic character class escapes: `\d`/`\D` for digits, `\w`/`\W` for "word" characters (related to programming identifiers), `\s`/`\S` for whitespace. These are available since ES3 and match sets of code units. With Unicode flags, Unicode property escapes (`\p{}` and `\P{}`) are also available.

# Prerequisites

- **Regular expression creation** -- these are pattern elements

# Key Properties

1. `\d` = `[0-9]`, `\D` = complement
2. `\w` = `[a-zA-Z0-9_]`, `\W` = complement
3. `\s` = whitespace (space, tab, line terminators), `\S` = complement
4. Without Unicode flags, these match code units
5. Unicode property escapes (`\p{...}`, `\P{...}`) available with `/u` or `/v` flags (ES2018)

# Construction / Recognition

```js
> 'a7x4'.match(/\d/g)
[ '7', '4' ]
> 'high - low'.match(/\w+/g)
[ 'high', 'low' ]
> 'hello\t\n everyone'.replaceAll(/\s/g, '-')
'hello---everyone'
```

(Ch. 46, Section 46.5.1, lines 582-592)

# Context & Application

Fundamental building blocks for most regex patterns. Used in validation, extraction, and text processing.

# Examples

See construction examples above. (Ch. 46, Section 46.5.1, lines 582-592)

# Relationships

## Builds Upon
- **Regular expression creation** -- part of regex syntax

## Related
- **RegExp character classes** -- escapes can be used inside `[...]`
- **RegExp Unicode property escapes** -- `\p{}` extends escapes to Unicode properties

# Common Errors

- **Error**: Assuming `\w` matches Unicode letters like accented characters
  **Correction**: `\w` only matches `[a-zA-Z0-9_]`; use `\p{Letter}` with Unicode flag for broader matching

# Common Confusions

- **Confusion**: `\b` inside a character class means word boundary
  **Clarification**: `\b` inside `[...]` means backspace; outside, it means word boundary

# Source Reference

Chapter 46: Regular expressions (RegExp), Section 46.5, lines 475-592.

# Verification Notes

- Definition source: direct from source text with equivalence table
- Confidence rationale: explicit table of escapes and equivalents
- Cross-reference status: verified
