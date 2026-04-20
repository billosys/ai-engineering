---
# === CORE IDENTIFICATION ===
concept: Automatic Semicolon Insertion
slug: automatic-semicolon-insertion

# === CLASSIFICATION ===
category: syntax-fundamentals
subcategory: basic-syntax
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Syntax"
chapter_number: 9
pdf_page: null
section: "9.8 Automatic semicolon insertion (ASI)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - ASI

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semicolons
  - statements
extends: []
related:
  - javascript-quirks
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is automatic semicolon insertion and what are its pitfalls?"
---

# Quick Definition

Automatic semicolon insertion (ASI) is JavaScript's mechanism for inferring missing semicolons, triggered when parsing encounters a line terminator followed by an illegal token. It has known pitfalls that can cause unexpected behavior.

# Core Definition

"While I recommend to always write semicolons, most of them are optional in JavaScript. The mechanism that makes this possible is called *automatic semicolon insertion* (ASI). In a way, it corrects syntax errors." (Ch. 9, &sect;9.8). ASI triggers when parsing a statement encounters either a semicolon or "a line terminator followed by an illegal token." JavaScript also forbids line breaks after certain tokens (like `return`), inserting semicolons there.

# Prerequisites

- **semicolons** -- ASI fills in missing semicolons
- **statements** -- ASI applies at statement boundaries

# Key Properties

1. Inserts semicolons at line breaks when the next token is illegal
2. Forbids line breaks after `return` (and some other tokens), inserting semicolons
3. Can be triggered unexpectedly (e.g., after `return` before an object literal)
4. Can fail to trigger unexpectedly (e.g., `(` or `[` on next line)
5. Author recommends always writing semicolons to avoid ASI pitfalls

# Construction / Recognition

ASI pitfalls are recognized when code behaves unexpectedly across line breaks.

# Context & Application

Understanding ASI is critical for debugging unexpected behavior, especially when not using semicolons. Tools like Prettier handle ASI edge cases automatically.

# Examples

From the source text (Ch. 9, &sect;9.8.1-9.8.2):

ASI triggered unexpectedly:
```js
return
{
  first: 'jane'
};
// Parsed as: return;  (empty return!)
```

ASI not triggered (unintended function call):
```js
a = b + c
(d + e).print()
// Parsed as: a = b + c(d + e).print();
```

ASI not triggered (unintended property access):
```js
someFunction()
['ul', 'ol'].map(x => x + x)
// Parsed as: someFunction()['ol'].map(x => x + x);
```

# Relationships

## Builds Upon
- **semicolons** -- ASI is the mechanism for optional semicolons

## Enables
- Semicolon-free coding style (with caution)

## Related
- **javascript-quirks** -- ASI pitfalls are a notable quirk

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Putting a line break after `return` before the value.
  **Correction**: Keep the return value on the same line as `return`, or start it on the same line.

- **Error**: Starting a line with `(`, `[`, or `/` without a preceding semicolon.
  **Correction**: Use semicolons, or prefix defensive semicolon (`;[...].map()`).

# Common Confusions

- **Confusion**: Thinking ASI always inserts semicolons at line breaks.
  **Clarification**: ASI only inserts a semicolon if the next token is illegal without one. `(` and `[` are legal continuations.

# Source Reference

Chapter 9: Syntax, Section 9.8, lines 943-1057.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Detailed with multiple pitfall examples
- Cross-reference status: verified
