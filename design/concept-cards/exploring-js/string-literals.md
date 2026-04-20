---
# === CORE IDENTIFICATION ===
concept: String Literals
slug: string-literals

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
section: "Plain string literals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "plain string literals"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string-type
extends: []
related:
  - template-literal
  - string-escaping
contrasts_with:
  - template-literal

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Plain string literals are delimited by single quotes (`'...'`) or double quotes (`"..."`), with backslash escape sequences for special characters like newlines (`\n`), tabs (`\t`), and the delimiter itself.

# Core Definition

Plain string literals use single or double quotes as delimiters. Single quotes are more commonly used because they make it easier to include HTML (which prefers double quotes). Backslashes enable escape sequences: `\n` (newline), `\r` (carriage return), `\t` (tab), `\\` (backslash), and escaped delimiters (`\'` or `\"`) (Ch. 22, Section 22.2).

# Prerequisites

- **string-type** -- literals create string values

# Key Properties

1. Single quotes or double quotes (no semantic difference)
2. Single quotes preferred in practice (easier to embed HTML)
3. Escape sequences: `\n`, `\r`, `\t`, `\\`
4. Delimiter escaping: `\'` in single-quoted, `\"` in double-quoted
5. Cannot span multiple lines (use template literals for that)

# Construction / Recognition

```js
const str1 = 'abc';
const str2 = "abc";
assert.equal(str1, str2);

assert.equal(
  'She said: "Let\'s go!"',
  "She said: \"Let's go!\""
);
```

# Context & Application

Plain string literals are the most common way to write strings. For multiline strings or string interpolation, use template literals instead.

# Examples

From the source text:

```js
const str1 = 'abc';
const str2 = "abc";
assert.equal(str1, str2);

// Escape sequences
'\n' // newline
'\t' // tab
'\\' // backslash
```

# Relationships

## Builds Upon
- **string-type** — literals produce string values

## Enables
- Writing string constants in code

## Related
- **template-literal** — alternative string syntax with interpolation
- **string-escaping** — escape sequence details

## Contrasts With
- **template-literal** — template literals use backticks and support interpolation

# Common Errors

- **Error**: Using `\n` in a template literal expecting a literal backslash-n
  **Correction**: Use `String.raw` or double-backslash `\\n` for a literal backslash.

# Common Confusions

- **Confusion**: Thinking single and double quotes have different semantics
  **Clarification**: They are functionally identical. The only difference is which delimiter needs escaping inside the string.

# Source Reference

Chapter 22: Strings, Section 22.2, lines 258-298.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit description with examples
- Cross-reference status: verified
