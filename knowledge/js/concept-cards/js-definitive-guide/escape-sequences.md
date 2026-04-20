---
# === CORE IDENTIFICATION ===
concept: Escape Sequences in Strings
slug: escape-sequences

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: literals
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 51
section: "3.3.2 Escape Sequences in String Literals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - backslash escapes
  - string escapes

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string-literals
extends: []
related:
  - unicode-escape-sequences
  - string-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Escape sequences are backslash-prefixed character combinations in strings that represent special characters not otherwise representable, such as `\n` for newline, `\t` for tab, and `\\` for a literal backslash.

# Core Definition

"The backslash character (\) has a special purpose in JavaScript strings. Combined with the character that follows it, it represents a character that is not otherwise representable within the string. For example, \n is an escape sequence that represents a newline character." Three escape sequences are generic and use hexadecimal Unicode codes: `\xNN`, `\uNNNN`, and `\u{N}` (ES6). (pp. 51-52)

# Prerequisites

- **string-literals** — Escape sequences appear within string literals

# Key Properties

1. `\0` — NUL character
2. `\b` — Backspace
3. `\t` — Horizontal tab
4. `\n` — Newline
5. `\v` — Vertical tab
6. `\f` — Form feed
7. `\r` — Carriage return
8. `\"` — Double quote
9. `\'` — Single quote / apostrophe
10. `\\` — Backslash
11. `\xNN` — Unicode character by two hex digits
12. `\uNNNN` — Unicode character by four hex digits
13. `\u{N}` — Unicode character by 1-6 hex digits (ES6)
14. Unrecognized escape sequences: backslash is ignored (e.g., `\#` is just `#`)

# Construction / Recognition

```javascript
'You\'re right, it can\'t be a quote'
"Line1\nLine2"
"\xA9"                    // copyright symbol ©
"\u03c0"                  // π
"\u{1f600}"               // grinning face emoji (ES6)
```

# Context & Application

Escape sequences are essential for including special characters in strings, especially newlines, tabs, quotes within strings, and Unicode characters that cannot be typed directly.

# Examples

From the source text (pp. 51-52):
```javascript
'You\'re right, it can\'t be a quote'
```

Table 3-1 escape sequences include: `\0`, `\b`, `\t`, `\n`, `\v`, `\f`, `\r`, `\"`, `\'`, `\\`, `\xnn`, `\unnnn`, `\u{n}`.

# Relationships

## Builds Upon
- **string-literals** — Escape sequences are used within string literals

## Enables
- Representing special characters in strings

## Related
- **unicode-escape-sequences** — `\u` escapes are a subset of string escape sequences

## Contrasts With
- None within this source

# Common Errors

- **Error**: Forgetting to escape backslashes in file paths: `"C:\new\folder"`.
  **Correction**: The `\n` and `\f` are escape sequences. Use `"C:\\new\\folder"` or a template literal.

# Common Confusions

- **Confusion**: All backslash sequences are escape sequences.
  **Clarification**: If the character after `\` is not a recognized escape character, the backslash is simply ignored (p. 52).

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.3.2, pages 51-52.

# Verification Notes

- Definition source: Direct quotes from pp. 51-52
- Confidence rationale: High — clearly defined with table
- Uncertainties: None
- Cross-reference status: Verified
