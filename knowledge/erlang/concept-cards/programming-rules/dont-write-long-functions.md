---
concept: Don't Write Very Long Functions
slug: dont-write-long-functions
category: core-idioms
subcategory: lexical-stylistic-conventions
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Specific Lexical and Stylistic Conventions"
chapter_number: 7
pdf_page: null
section: "7.3 Don't write very long functions"
extraction_confidence: high
aliases:
  - "long functions"
  - "15 to 20 lines per function"
prerequisites: []
extends: []
related:
  - dont-write-large-modules
  - dont-write-deeply-nested-code
  - dont-write-long-lines
contrasts_with: []
answers_questions:
  - "How long should an Erlang function be?"
---

# Quick Definition

Don't write functions longer than about 15 to 20 lines — split a large function into several smaller ones.

# Core Definition

"Don't write functions with more than 15 to 20 lines of code. Split large function into several smaller ones. Don't solve the problem by writing long lines" (Programming Rules, 7.3).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A function should not exceed roughly 15-20 lines of code.
2. A large function is split into several smaller functions.
3. Cramming code onto long lines to "shorten" a function does not count.

# Construction / Recognition

## To Apply

1. When a function passes ~15-20 lines, extract parts into smaller functions.

## To Recognize a Violation

1. A function exceeds about 15-20 lines, or hides its length in long lines.

# Context & Application

A core lexical/stylistic convention (section 7).

- **Typical contexts**: functions that accumulated several steps of logic.
- **Common applications**: extracting helper functions from an overgrown function.

# Examples

The source states the numeric guideline directly; no code listing is given.

# Relationships

## Related

- **Don't write very large modules** — the module-level analogue of this size limit.
- **Don't write deeply nested code** — both are cured by extracting smaller functions.
- **Don't write very long lines** — long lines must not be used to disguise a long function.

# Common Errors

- **Error**: Letting a function grow well past 20 lines.
  **Correction**: Split it into several smaller functions.

# Common Confusions

- **Confusion**: Thinking a function can be "shortened" by packing logic onto fewer, longer lines.
  **Clarification**: The source explicitly forbids this — fewer long lines is not a smaller function.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 7.3 "Don't write very long functions".

# Verification Notes

- Definition source: Direct adaptation of section 7.3.
- Confidence rationale: HIGH — the rule is stated explicitly with a numeric guideline.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
