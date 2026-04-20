---
concept: Regular Expression Creation
slug: regular-expression-creation
category: standard-library
subcategory: regexp
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Regular expressions (RegExp)"
chapter_number: 46
pdf_page: null
section: "46.1 Creating regular expressions"
extraction_confidence: high
aliases:
  - regex creation
  - RegExp creation
prerequisites: []
extends: []
related:
  - regexp-flags
  - regexp-syntax-characters
contrasts_with: []
answers_questions:
  - "How do I write and use regular expressions in JavaScript?"
---

# Quick Definition

Regular expressions can be created two ways in JavaScript: as literals (`/pattern/flags`) compiled at load time, or via the `RegExp` constructor (`new RegExp('pattern', 'flags')`) compiled at runtime.

# Core Definition

"Exploring JavaScript" Ch. 46 describes "the two main ways of creating regular expressions": "Literal: compiled statically (at load time). Constructor: compiled dynamically (at runtime)." Both have a body (the pattern) and flags (e.g., `i` for case-insensitive). The constructor also supports cloning: `new RegExp(regExp, flags)` (ES6). Using `String.raw` template tags avoids double-escaping with the constructor.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Literal syntax: `/abc/iv` -- compiled at load time
2. Constructor syntax: `new RegExp('abc', 'iv')` -- compiled at runtime
3. Constructor enables dynamic pattern creation from strings
4. `new RegExp(regExp, flags)` clones with optional new flags (ES6)
5. Use `String.raw` with constructor to avoid double-escaping

# Construction / Recognition

```js
/abc/iv                          // literal
new RegExp('abc', 'iv')          // constructor
new RegExp(String.raw`^\*$`, 'v') // constructor with raw string
new RegExp(/abc/i, 'g')          // clone with new flags
```

(Ch. 46, Section 46.1.1-46.1.3, lines 189-289)

# Context & Application

Use literals for static patterns known at code-writing time. Use the constructor when patterns are built dynamically from user input or variables.

# Examples

```js
> /^\*$/.test('*')
true
> new RegExp('^\\*$', 'v').test('*')
true
> new RegExp(String.raw`^\*$`, 'v').test('*')
true
```

(Ch. 46, Section 46.1.2, lines 241-247)

# Relationships

## Enables
- **RegExp flags** -- flags modify pattern behavior
- **RegExp syntax characters** -- patterns use special syntax

# Common Errors

- **Error**: Forgetting to double-escape backslashes in constructor strings
  **Correction**: Use `String.raw` template literals or double each backslash

# Common Confusions

- **Confusion**: Literals and constructor create different types of objects
  **Clarification**: Both create `RegExp` instances; the difference is compilation time

# Source Reference

Chapter 46: Regular expressions (RegExp), Section 46.1, lines 189-289.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with both forms
- Cross-reference status: verified
