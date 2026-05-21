---
concept: Don't Write Very Long Lines
slug: dont-write-long-lines
category: core-idioms
subcategory: lexical-stylistic-conventions
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Specific Lexical and Stylistic Conventions"
chapter_number: 7
pdf_page: null
section: "7.4 Don't write very long lines"
extraction_confidence: high
aliases:
  - "long lines"
  - "80 characters per line"
  - "string constant concatenation"
prerequisites: []
extends: []
related:
  - dont-write-long-functions
  - consistent-formatting
contrasts_with: []
answers_questions:
  - "How long should a line of Erlang code be?"
---

# Quick Definition

Don't write very long lines — a line should not exceed 80 characters.

# Core Definition

"Don't write very long lines. A line should not have more than 80 characters" (Programming Rules, 7.4) — for example, so it fits on an A4 page. The source notes that in Erlang 4.3 and later, adjacent string constants are automatically concatenated, which lets a long format string be split across lines.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A line should not exceed 80 characters.
2. An 80-character line fits, for example, on an A4 page.
3. Adjacent string constants are auto-concatenated (Erlang 4.3+), so long strings can be split across lines.

# Construction / Recognition

## To Apply

1. Keep lines within 80 characters.
2. Split a long string literal across lines, relying on automatic constant concatenation.

## To Recognize a Violation

1. A source line exceeds 80 characters.

# Context & Application

A core lexical/stylistic convention (section 7).

- **Typical contexts**: every line; especially long format strings.
- **Common applications**: a two-line `io:format` format string split into adjacent literals.

# Examples

**Example** (from source): an `io:format` call whose format string is written as two adjacent string constants on separate lines, which Erlang concatenates automatically.

# Relationships

## Related

- **Don't write very long functions** — long lines must not be used to disguise a long function.
- **Format programs in a consistent manner** — line length is part of consistent formatting.

# Common Errors

- **Error**: Writing a line well beyond 80 characters.
  **Correction**: Break it; split long strings into adjacent literals.

# Common Confusions

- **Confusion**: Thinking a long string forces a long line.
  **Clarification**: Adjacent string constants concatenate automatically, so long strings can wrap.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 7.4 "Don't write very long lines".

# Verification Notes

- Definition source: Direct adaptation of section 7.4.
- Confidence rationale: HIGH — the rule is stated explicitly with a numeric limit and example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
