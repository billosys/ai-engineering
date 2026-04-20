---
# === CORE IDENTIFICATION ===
concept: String Escaping
slug: string-escaping

# === CLASSIFICATION ===
category: primitive-types
subcategory: strings
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Strings"
chapter_number: 22
pdf_page: null
section: "Escaping"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "escape sequences"
  - "backslash escaping"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string-literals
extends: []
related:
  - string-raw
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

In JavaScript string literals, the backslash (`\`) creates special characters: `\n` (newline), `\r` (carriage return), `\t` (tab), `\\` (literal backslash), and escaped delimiters (`\'` or `\"`).

# Core Definition

"The backslash lets us create special characters" in string literals: `\n` for Unix newline, `\r\n` for Windows newline, `\t` for tab, `\\` for a literal backslash. It also enables using the delimiter character within its own string: `\'` inside single-quoted strings, `\"` inside double-quoted strings. Unicode escapes are also supported: `\uXXXX` (code unit) and `\u{XXXXX}` (code point) (Ch. 22, Section 22.2.1).

# Prerequisites

- **string-literals** -- escape sequences are used in string literals

# Key Properties

1. `\n` -- Unix newline
2. `\r\n` -- Windows newline
3. `\t` -- tab
4. `\\` -- literal backslash
5. `\'` and `\"` -- escaped delimiters
6. `\uXXXX` -- Unicode code unit escape
7. `\u{XXXXX}` -- Unicode code point escape (ES6)
8. `\xXX` -- ASCII/Latin-1 escape

# Construction / Recognition

```js
'She said: "Let\'s go!"'
"She said: \"Let's go!\""

'\n'  // newline
'\t'  // tab
'\\'  // backslash
```

# Context & Application

Escape sequences are essential for representing special characters and embedding quotes in strings. Template literals reduce the need for escaping.

# Examples

From the source text:

```js
assert.equal(
  'She said: "Let\'s go!"',
  "She said: \"Let's go!\""
);
```

# Relationships

## Builds Upon
- **string-literals** — escape sequences are part of literal syntax

## Enables
- Representing special characters in strings

## Related
- **string-raw** — `String.raw` treats backslashes as literal

## Contrasts With
- None

# Common Errors

- **Error**: Forgetting to escape backslashes in Windows paths: `'C:\new\folder'`
  **Correction**: `\n` is interpreted as newline. Use `'C:\\new\\folder'` or `String.raw`C:\new\folder``.

# Common Confusions

- **Confusion**: Thinking escape sequences work the same in all string types
  **Clarification**: They work in single/double-quoted strings and template literals, but `String.raw` template literals treat backslashes as literal.

# Source Reference

Chapter 22: Strings, Section 22.2.1, lines 280-298.

# Verification Notes

- Definition source: direct
- Confidence rationale: Complete list of escape sequences
- Cross-reference status: verified
