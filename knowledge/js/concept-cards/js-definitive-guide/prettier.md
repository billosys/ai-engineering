---
concept: Prettier
slug: prettier
category: tooling
subcategory: formatting
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript Tools and Extensions"
chapter_number: 17
pdf_page: 654
section: "17.2 JavaScript Formatting with Prettier"
extraction_confidence: high
aliases:
  - code formatter
  - auto-formatter
prerequisites: []
extends: []
related:
  - eslint
contrasts_with: []
answers_questions:
  - "How do I write and run unit tests with Jest?"
---

# Quick Definition

Prettier is an opinionated code formatter that automatically parses and reformats JavaScript code to a consistent style, handling indentation, semicolons, spacing, and line breaks with minimal configuration.

# Core Definition

Prettier parses JavaScript code and reprints it with consistent formatting, fixing indentation, adding missing semicolons, adding spaces around operators, and inserting line breaks. It has few configuration options (line length, indentation amount, semicolons, quote style) and is designed to eliminate formatting debates. The `--write` option reformats files in place. It can be integrated into editors (format on save) and git commit hooks (Flanagan, Ch. 17, pp. 654-655).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Opinionated: few configuration options by design.
2. `--write` flag reformats files in place.
3. Can integrate with code editors for format-on-save.
4. Can run as a git commit hook.
5. Default options are reasonable for most projects.

# Construction / Recognition

```bash
$ prettier factorial.js        # Print reformatted version
$ prettier --write factorial.js # Reformat in place
```

# Context & Application

Adopted at the project level so the entire team uses consistent formatting without manual effort or debate.

# Examples

From the source (p. 654): Unconventionally formatted code with missing semicolons and inconsistent spacing is automatically reformatted to clean, conventional JavaScript.

# Relationships

## Builds Upon
- (None - foundational tooling concept)

## Enables
- Consistent formatting across teams

## Related
- **eslint** — ESLint catches bugs; Prettier handles formatting

## Contrasts With
- (None)

# Common Errors

- **Error**: Fighting Prettier's formatting choices by adding manual overrides everywhere.
  **Correction**: Accept Prettier's opinionated defaults; the value is in consistency, not personal preference.

# Common Confusions

- **Confusion**: Prettier replaces ESLint.
  **Clarification**: Prettier handles formatting only. ESLint handles code quality rules. Use both together.

# Source Reference

Chapter 17: JavaScript Tools and Extensions, Section 17.2, pages 654-655.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clear before/after example
- Uncertainties: None
- Cross-reference status: Verified
