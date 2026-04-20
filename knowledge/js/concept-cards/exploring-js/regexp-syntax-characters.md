---
concept: RegExp Syntax Characters and Escaping
slug: regexp-syntax-characters
category: standard-library
subcategory: regexp
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Regular expressions (RegExp)"
chapter_number: 46
pdf_page: null
section: "46.2 Syntax characters and escaping"
extraction_confidence: high
aliases:
  - regex escaping
  - special characters in regex
prerequisites:
  - regular-expression-creation
extends: []
related:
  - regexp-character-classes
contrasts_with: []
answers_questions:
  - "How do I write and use regular expressions in JavaScript?"
---

# Quick Definition

Syntax characters (`^ $ \ . * + ? ( ) [ ] { } |`) have special meaning in regular expressions and must be escaped with a backslash to match literally. With Unicode flags (`/u` or `/v`), escaping non-syntax characters is a SyntaxError.

# Core Definition

"Exploring JavaScript" Ch. 46 lists the syntax characters: `^ $ \ . * + ? ( ) [ ] { } |`. "They are escaped by prefixing a backslash." With flag `/u` or `/v`, "escaping a non-syntax character at the top level is a syntax error." Escaping rules differ inside character classes, especially with flag `/v`.

# Prerequisites

- **Regular expression creation** -- escaping is part of pattern construction

# Key Properties

1. 13 syntax characters require escaping to match literally
2. Slashes must be escaped in literals: `\/`
3. With Unicode flags, only syntax characters can be escaped (stricter)
4. Without Unicode flags, non-syntax characters can be identity-escaped
5. Different escaping rules apply inside character classes

# Construction / Recognition

```js
> /\*/v.test('*')
true
> /\//v.test('/')
true
```

(Ch. 46, Section 46.2.1, lines 300-321)

# Context & Application

Essential knowledge for constructing correct regex patterns, especially when matching characters that have special regex meaning.

# Examples

From the source: `^ $ \ . * + ? ( ) [ ] { } |` are all syntax characters.

(Ch. 46, Section 46.2.1, lines 300-305)

# Relationships

## Builds Upon
- **Regular expression creation** -- escaping is part of writing patterns

## Related
- **RegExp character classes** -- different escaping rules inside `[...]`

# Common Errors

- **Error**: Not escaping `.` when you want to match a literal period
  **Correction**: Use `\.` to match a literal dot

# Common Confusions

- **Confusion**: All special characters need escaping everywhere
  **Clarification**: Escaping rules vary between top-level and inside character classes, and depend on whether Unicode flags are used

# Source Reference

Chapter 46: Regular expressions (RegExp), Section 46.2, lines 296-418.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit list of syntax characters
- Cross-reference status: verified
