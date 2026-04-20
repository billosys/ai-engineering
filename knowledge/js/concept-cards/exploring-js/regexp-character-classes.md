---
concept: RegExp Character Classes
slug: regexp-character-classes
category: standard-library
subcategory: regexp
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Regular expressions (RegExp)"
chapter_number: 46
pdf_page: null
section: "46.6 Syntax: character classes"
extraction_confidence: high
aliases:
  - "[...] character class"
  - regex character sets
prerequisites:
  - regular-expression-creation
extends: []
related:
  - regexp-character-class-escapes
  - regexp-character-class-set-operations
contrasts_with: []
answers_questions:
  - "How do I write and use regular expressions in JavaScript?"
---

# Quick Definition

A character class `[...]` defines a set of characters to match; `[^...]` matches any character NOT in the set. Character classes support ranges (`[a-z]`), escapes (`\d`), and with flag `/v`, nesting and set operations.

# Core Definition

"Exploring JavaScript" Ch. 46: "A character class wraps class ranges in square brackets. The class ranges specify a set of characters: [class ranges] matches any character in the set. [^class ranges] matches any character not in the set." With flag `/v` (ES2024), character classes support nesting, set subtraction (`--`), and intersection (`&&`).

# Prerequisites

- **Regular expression creation** -- character classes are pattern elements

# Key Properties

1. `[abc]` matches a, b, or c
2. `[^abc]` matches anything except a, b, or c
3. `[a-z]` specifies ranges
4. Escapes work inside: `\d`, `\w`, `\p{...}`, etc.
5. `\b` inside a class means backspace (not word boundary)
6. With flag `/v`: nesting, `--` subtraction, `&&` intersection (ES2024)
7. With flag `/v`: `\q{...}` for code point sequences (ES2024)

# Construction / Recognition

```js
> /^[\d\w]$/v.test('7')     // true
> /^[\d\w]$/v.test('?')     // false
> /^[\w--[a-g]]$/v.test('h') // true (subtraction)
> /[\p{ASCII}&&\p{Letter}]/v.test('D') // true (intersection)
```

(Ch. 46, Section 46.6, lines 827-1025)

# Context & Application

Character classes are fundamental for defining what characters to match in regex patterns.

# Examples

Set operations with flag `/v`:
```js
> /^[\p{Number}--[0-9]]$/v.test('three_arabic')
true  // matches non-ASCII digits
> /^[\p{Number}--[0-9]]$/v.test('3')
false // excludes ASCII digits
```

(Ch. 46, Section 46.6.2, lines 975-978)

# Relationships

## Builds Upon
- **Regular expression creation** -- part of regex syntax

## Related
- **RegExp character class escapes** -- used inside character classes
- **RegExp character class set operations** -- enabled by flag `/v`

# Common Errors

- **Error**: Putting an unescaped `-` in the middle of a character class
  **Correction**: Escape it (`\-`), or place it first or last: `[-abc]` or `[abc-]`

# Common Confusions

- **Confusion**: `^` inside a character class means "start of string"
  **Clarification**: `^` as the first character inside `[...]` means negation; elsewhere it's literal

# Source Reference

Chapter 46: Regular expressions (RegExp), Section 46.6, lines 827-1025.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with set operations
- Cross-reference status: verified
