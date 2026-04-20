---
# === CORE IDENTIFICATION ===
concept: JavaScript Comments
slug: javascript-comments

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
section: "9.1.1.1 Comments"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - single-line comment
  - multi-line comment

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - statements
  - expressions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you write comments in JavaScript?"
---

# Quick Definition

JavaScript supports two comment styles: single-line comments starting with `//` and multi-line comments enclosed in `/* */`.

# Core Definition

JavaScript has two comment syntaxes (Ch. 9, &sect;9.1.1.1): single-line comments beginning with `//` that continue to the end of the line, and multi-line (block) comments enclosed between `/*` and `*/`.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Single-line: `// comment text`
2. Multi-line: `/* comment text */`
3. C-family syntax, inherited from Java

# Construction / Recognition

```js
// single-line comment

/*
Comment with
multiple lines
*/
```

# Context & Application

Comments document code intent, disable code temporarily, and explain complex logic. JSDoc uses multi-line comments with special formatting.

# Examples

From the source text (Ch. 9, &sect;9.1.1.1):
```js
// single-line comment

/*
Comment with
multiple lines
*/
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- Code documentation and JSDoc

## Related
- **statements** -- comments appear between statements

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Nesting multi-line comments (`/* /* */ */`).
  **Correction**: Multi-line comments cannot be nested; the first `*/` ends the comment.

# Common Confusions

- **Confusion**: Using comments instead of proper documentation tools.
  **Clarification**: For API documentation, use JSDoc format within multi-line comments.

# Source Reference

Chapter 9: Syntax, Section 9.1.1.1, lines 79-89.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicitly shown with code examples
- Cross-reference status: verified
