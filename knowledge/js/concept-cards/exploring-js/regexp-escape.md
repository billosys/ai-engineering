---
concept: RegExp.escape()
slug: regexp-escape
category: standard-library
subcategory: regexp
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Regular expressions (RegExp)"
chapter_number: 46
pdf_page: null
section: "46.17 RegExp.escape()"
extraction_confidence: high
aliases:
  - escaping text for regex
prerequisites:
  - regular-expression-creation
  - regexp-syntax-characters
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How do I write and use regular expressions in JavaScript?"
---

# Quick Definition

`RegExp.escape()` (ES2025) escapes a string so that all regex-special characters are treated as literal characters when used inside a regular expression pattern, enabling safe inclusion of user input in regex patterns.

# Core Definition

"Exploring JavaScript" Ch. 46 describes `RegExp.escape()` as a method for escaping text so it can be safely used inside regular expressions. Introduced in ES2025. Use cases include replacing all occurrences of a text and building regex patterns from dynamic strings.

# Prerequisites

- **Regular expression creation** -- creates patterns from escaped strings
- **RegExp syntax characters** -- the characters being escaped

# Key Properties

1. Introduced in ES2025
2. Escapes all regex-special characters in a string
3. Essential for safely including user input in regex patterns
4. Use cases: replacing all occurrences, building dynamic patterns

# Construction / Recognition

```js
// Replacing all occurrences of a text
const searchText = 'foo.bar';
const escaped = RegExp.escape(searchText); // 'foo\\.bar'
const regex = new RegExp(escaped, 'g');
```

(Ch. 46, Section 46.17, lines 1837 and following)

# Context & Application

Essential for any code that builds regex patterns from user input or dynamic strings.

# Examples

From the source, two use cases: replacing all occurrences of a text, and building a regex where part must match a given text exactly.

(Ch. 46, Section 46.17, lines 1837 and following)

# Relationships

## Builds Upon
- **Regular expression creation** -- escaped strings are used in regex construction
- **RegExp syntax characters** -- these are the characters being escaped

# Common Errors

- **Error**: Building regex from user input without escaping
  **Correction**: Always use `RegExp.escape()` for user-provided strings in regex patterns

# Common Confusions

- **Confusion**: `RegExp.escape()` has been available for a long time
  **Clarification**: It was only standardized in ES2025; before that, custom helper functions were needed

# Source Reference

Chapter 46: Regular expressions (RegExp), Section 46.17.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with use cases
- Cross-reference status: verified
