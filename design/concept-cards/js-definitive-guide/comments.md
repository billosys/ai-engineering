---
# === CORE IDENTIFICATION ===
concept: Comments
slug: comments

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: lexical-structure
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Lexical Structure"
chapter_number: 2
pdf_page: 33
section: "2.2 Comments"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - single-line comment
  - multi-line comment
  - block comment

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-language-overview
extends: []
related:
  - case-sensitivity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

JavaScript supports two styles of comments: single-line comments beginning with `//` and multi-line comments enclosed between `/*` and `*/`.

# Core Definition

"JavaScript supports two styles of comments. Any text between a // and the end of a line is treated as a comment and is ignored by JavaScript. Any text between the characters /* and */ is also treated as a comment; these comments may span multiple lines but may not be nested." (p. 33)

# Prerequisites

- **javascript-language-overview** — Comments are a basic language feature

# Key Properties

1. Single-line comments: `//` to end of line
2. Multi-line comments: `/*` to `*/`
3. Multi-line comments cannot be nested
4. Comments are ignored by the JavaScript interpreter
5. Unicode escapes in comments are treated as ASCII, not interpreted as Unicode

# Construction / Recognition

```javascript
// This is a single-line comment.
/* This is also a comment */  // and here is another comment.
/*
 * This is a multi-line comment. The extra * characters at the start of
 * each line are not a required part of the syntax; they just look cool!
 */
```

# Context & Application

Comments are used to document code, explain complex logic, and temporarily disable code. They are a fundamental part of readable programming.

# Examples

From the source text (p. 33):
```javascript
// This is a single-line comment.
/* This is also a comment */  // and here is another comment.
/*
 * This is a multi-line comment. The extra * characters at the start of
 * each line are not a required part of the syntax; they just look cool!
 */
```

# Relationships

## Builds Upon
- **javascript-language-overview** — Comments are basic syntax

## Enables
- Code documentation practices

## Related
- **case-sensitivity** — Both are part of lexical structure

## Contrasts With
- None within this source

# Common Errors

- **Error**: Attempting to nest multi-line comments (`/* /* inner */ outer */`).
  **Correction**: Multi-line comments cannot be nested; the first `*/` ends the comment.

# Common Confusions

- **Confusion**: Unicode escapes in comments are interpreted.
  **Clarification**: "Since comments are ignored, they are simply treated as ASCII characters in that context and not interpreted as Unicode" (p. 35).

# Source Reference

Chapter 2: Lexical Structure, Section 2.2, page 33.

# Verification Notes

- Definition source: Direct quote from p. 33
- Confidence rationale: High — clearly defined
- Uncertainties: None
- Cross-reference status: Verified
