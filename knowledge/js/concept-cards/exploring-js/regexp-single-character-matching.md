---
concept: RegExp Single Character Matching
slug: regexp-single-character-matching
category: standard-library
subcategory: regexp
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Regular expressions (RegExp)"
chapter_number: 46
pdf_page: null
section: "46.4 Syntax: matching single characters"
extraction_confidence: high
aliases:
  - dot operator
  - character escapes
prerequisites:
  - regular-expression-creation
extends: []
related:
  - regexp-character-class-escapes
  - regexp-flags
contrasts_with: []
answers_questions:
  - "How do I write and use regular expressions in JavaScript?"
---

# Quick Definition

Single characters are matched by pattern characters (literals), the dot (`.`) which matches any character (except line terminators without `/s`), and character escapes like `\n`, `\t`, `\x20`, `\u{1F642}`.

# Core Definition

"Exploring JavaScript" Ch. 46 describes three ways to match single characters: "Pattern characters are all characters except syntax characters. Pattern characters match themselves." The dot "matches any character. We can use flag /s (dotAll) to control if the dot matches line terminators or not." Character escapes include control escapes (`\n`, `\t`), hex escapes (`\x20`), Unicode code unit escapes (`\u00E4`), and code point escapes (`\u{1F642}`, requires `/u` or `/v`).

# Prerequisites

- **Regular expression creation** -- these are pattern elements

# Key Properties

1. Pattern characters match themselves: `A`, `b`, `%`, `-`
2. `.` matches any character (flag `/s` controls line terminator matching)
3. `\n` (line feed), `\r` (carriage return), `\t` (tab), `\f` (form feed)
4. `\x20` (hex escape for space)
5. `\u{1F642}` (code point escape, requires `/u` or `/v`)
6. Without Unicode flags, "character" means UTF-16 code unit; with flags, code point

# Construction / Recognition

```js
> '🙂'.match(/./g)   // without Unicode flag: 2 code units
[ '\uD83D', '\uDE42' ]
> '🙂'.match(/./gv)  // with /v flag: 1 code point
[ '🙂' ]
```

(Ch. 46, Section 46.3, lines 430-436)

# Context & Application

Understanding what "character" means in regex context (code unit vs code point) is critical for correct Unicode handling.

# Examples

See construction example above. (Ch. 46, Section 46.3, lines 430-436)

# Relationships

## Builds Upon
- **Regular expression creation** -- fundamental pattern elements

## Related
- **RegExp flags** -- `/s` flag changes dot behavior; `/u`/`/v` change character meaning

# Common Errors

- **Error**: Using `.` to match emoji or other multi-code-unit characters without `/v`
  **Correction**: Always use flag `/v` (or `/u`) for correct Unicode matching

# Common Confusions

- **Confusion**: `.` matches literally everything including newlines
  **Clarification**: Without `/s` flag, `.` does not match line terminators

# Source Reference

Chapter 46: Regular expressions (RegExp), Sections 46.3-46.4, lines 419-473.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with Unicode behavior
- Cross-reference status: verified
