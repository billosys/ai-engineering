---
concept: Variable Names
slug: variable-names
category: core-idioms
subcategory: lexical-stylistic-conventions
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Specific Lexical and Stylistic Conventions"
chapter_number: 7
pdf_page: null
section: "7.5 Variable names"
extraction_confidence: high
aliases:
  - "variable names"
  - "meaningful variable names"
  - "underscore variables"
prerequisites: []
extends: []
related:
  - function-names
  - module-names
contrasts_with: []
answers_questions:
  - "How should variables be named in Erlang?"
  - "Should I use _ as a don't-care variable?"
---

# Quick Definition

Choose meaningful variable names; separate words with `_` or capitalization; and prefer `_`-prefixed variables over a bare `_` for don't-care values.

# Core Definition

"Choose meaningful variable names — this is very difficult" (Programming Rules, 7.5). If a variable name consists of several words, use `_` or a capitalized letter to separate them (`My_variable` or `MyVariable`). Avoid using `_` as a don't-care variable; use a `_`-prefixed variable instead (`_Name`) — if you later need the value, you just remove the leading underscore, with no trouble finding which underscore to replace.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Variable names are meaningful.
2. Multi-word names separate words with `_` or capitalization.
3. A `_`-prefixed variable (`_Name`) is preferred over a bare `_` for don't-care values.
4. A `_`-prefixed name can later become a used variable by removing the underscore.

# Construction / Recognition

## To Apply

1. Pick a name that conveys the variable's meaning.
2. For an unused binding, write `_Name` rather than `_`.

## To Recognize a Violation

1. A meaningless variable name, or a bare `_` used where a `_Name` would document intent.

# Context & Application

A core lexical/stylistic convention (section 7).

- **Typical contexts**: every variable binding.
- **Common applications**: `_Name` for a deliberately unused argument.

# Examples

**Example** (from source): multi-word names `My_variable` or `MyVariable`; the don't-care form `_Name` rather than a bare `_`.

# Relationships

## Related

- **Function names** — companion naming rule.
- **Module names** — companion naming rule.

# Common Errors

- **Error**: Using a bare `_` for an argument you may later need.
  **Correction**: Use `_Name`; drop the underscore later if you need the value.

# Common Confusions

- **Confusion**: Thinking the variable-naming case style is fixed.
  **Clarification**: The source permits both `My_variable` and `MyVariable` for word separation; the firm rule is meaningfulness and the `_Name` don't-care form.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 7.5 "Variable names".

# Verification Notes

- Definition source: Direct adaptation of section 7.5.
- Confidence rationale: HIGH — the rule is stated explicitly with examples.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
