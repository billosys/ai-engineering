---
# === CORE IDENTIFICATION ===
concept: String Type
slug: string-type

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
section: "Cheat sheet: strings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "string"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - string-literals
  - template-literal
  - utf-16-encoding
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

Strings are primitive, immutable values in JavaScript, representing sequences of UTF-16 code units. All string operations produce new strings rather than modifying existing ones.

# Core Definition

"Strings are primitive values in JavaScript and immutable. That is, string-related operations always produce new strings and never change existing strings" (Ch. 22, Section 22.1). JavaScript has no separate character type -- single characters are strings of length 1. String characters are UTF-16 code units, accessed via bracket notation and `.length`.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Primitive and immutable
2. Based on UTF-16 code units
3. No separate character type (characters are strings of length 1)
4. `.length` counts UTF-16 code units, not visible characters
5. Accessed via `str[index]` or `str.at(index)` (negative indices with `.at()`)
6. Three literal forms: single quotes, double quotes, backticks (template literals)

# Construction / Recognition

```js
const str1 = 'single quotes';
const str2 = "double quotes";
const str3 = `template literal ${123}`;
typeof str1 // 'string'
```

# Context & Application

Strings are one of the most commonly used types in JavaScript. Understanding their UTF-16 basis is important for correctly handling international text and emojis.

# Examples

From the source text:

```js
const str = 'abc';
assert.equal(str[2], 'c');
assert.equal(str.at(-1), 'c');
assert.equal(str.length, 3);

// Emojis: 2 code units per code point
> '🙂'.length
2
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **string-literals** — syntax for creating strings
- **string-concatenation** — combining strings
- **string-comparison** — comparing strings

## Related
- **template-literal** — template literals produce strings
- **utf-16-encoding** — strings are UTF-16 sequences

## Contrasts With
- None

# Common Errors

- **Error**: Trying to modify a string character: `str[0] = 'X'`
  **Correction**: Strings are immutable. Create a new string instead.

# Common Confusions

- **Confusion**: Thinking `.length` counts visible characters
  **Clarification**: `.length` counts UTF-16 code units. Emojis may have `.length` of 2 or more.

# Source Reference

Chapter 22: Strings, Section 22.1, lines 70-75.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition
- Cross-reference status: verified
