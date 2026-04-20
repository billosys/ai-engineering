---
# === CORE IDENTIFICATION ===
concept: String.raw
slug: string-raw

# === CLASSIFICATION ===
category: primitive-types
subcategory: strings
tier: advanced

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Using template literals and tagged templates"
chapter_number: 23
pdf_page: null
section: "Raw string literals via the template tag String.raw"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "raw string literal"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tagged-template
extends: []
related:
  - cooked-vs-raw-template-strings
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

`String.raw` is a built-in tag function that produces "raw" string literals where backslashes have no special meaning, useful for Windows paths and regex patterns.

# Core Definition

"Raw string literals are implemented via the tag function `String.raw`. They are string literals where backslashes don't do anything special (such as escaping characters, etc.)" (Ch. 23, Section 23.5). `String.raw` uses the raw interpretation of the template strings.

# Prerequisites

- **tagged-template** -- `String.raw` is a tag function

# Key Properties

1. Backslashes are literal: `String.raw`\back`` produces `'\\back'`
2. Useful for regex patterns and Windows file paths
3. Built-in tag function (no import needed)

# Construction / Recognition

```js
assert.equal(String.raw`\back`, '\\back');

// Regex without double escaping
const regex = new RegExp(String.raw`^\.`);

// Windows paths
const WIN_PATH = String.raw`C:\Users\Robin\Documents`;
```

# Context & Application

Use `String.raw` when writing regex patterns for `new RegExp()` or Windows file paths to avoid double-backslash escaping.

# Examples

From the source text:

```js
assert.equal(String.raw`\back`, '\\back');

const regex1 = /^\./;
const regex2 = new RegExp('^\\.');
const regex3 = new RegExp(String.raw`^\.`);
// All three are equivalent

const WIN_PATH = String.raw`C:\Users\Robin\Documents`;
assert.equal(WIN_PATH, 'C:\\Users\\Robin\\Documents');
```

# Relationships

## Builds Upon
- **tagged-template** — `String.raw` is a tag function

## Enables
- Clean regex patterns with `new RegExp()`
- Windows file path literals

## Related
- **cooked-vs-raw-template-strings** — `String.raw` uses the raw interpretation

## Contrasts With
- None

# Common Errors

- **Error**: Using `String.raw` and still double-escaping backslashes
  **Correction**: In `String.raw`, backslashes are literal. `String.raw`\n`` is two characters (backslash + n), not a newline.

# Common Confusions

- **Confusion**: Thinking `String.raw` prevents all processing of the template
  **Clarification**: Interpolation (`${}`) still works normally. Only backslash escape sequences are kept literal.

# Source Reference

Chapter 23: Using template literals and tagged templates, Section 23.5, lines 358-397.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with practical examples
- Cross-reference status: verified
