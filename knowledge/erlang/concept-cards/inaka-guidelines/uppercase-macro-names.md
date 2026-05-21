---
concept: Uppercase Macros
slug: uppercase-macro-names
category: core-idioms
subcategory: macros
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Macros"
chapter_number: null
pdf_page: null
section: "Uppercase macros"
extraction_confidence: high
aliases:
  - "macro naming"
  - "ALL_UPPER_CASE macros"
prerequisites: []
extends: []
related:
  - avoid-macros
  - no-module-or-function-name-macros
contrasts_with: []
answers_questions:
  - "How should macros be named in Erlang?"
---

# Quick Definition

Name macros in `ALL_UPPER_CASE`.

# Core Definition

"Macros should be named in ALL_UPPER_CASE" (Inaka, "Uppercase macros"). Whatever macros remain (predefined names and literal constants) carry fully uppercase names with underscores between words.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Macro names use only uppercase letters (and underscores between words).
2. Mixed-case, lowercase, or symbol-laden macro names are disallowed.
3. Uppercase names make macros easy to spot and to find with `grep`.
4. It is a PR-rejection rule under Macros.

# Construction / Recognition

## To Apply

1. Write `-define(GOOD, ...)` and `-define(GOOD_MACRO_NAME, ...)`.

## To Recognize a Violation

1. A macro name is lowercase (`?bad`), mixed-case (`?Bad_Macro_Name`), or contains symbols (`?Bad_L33t_M@Cr0`).

# Context & Application

A PR-blocking convention under Macros.

- **Typical contexts**: literal-constant definitions.
- **Common applications**: `?GOOD_MACRO_NAME`.

# Examples

**Example 1** — bad: `?bad`, `?BADMACRONAME`, `?Bad_Macro_Name`, `?Bad_L33t_M@Cr0`.

**Example 2** — good: `?GOOD`, `?GOOD_MACRO_NAME`.

# Relationships

## Related

- **No Macros** — this rule names the few macros that remain after macro avoidance.
- **No module or function name macros** — companion macro rule.

# Common Errors

- **Error**: Defining `?Timeout` in mixed case.
  **Correction**: Use `?TIMEOUT`.

# Common Confusions

- **Confusion**: Thinking `?BADMACRONAME` is fine because it is uppercase.
  **Clarification**: It is uppercase but lacks word separation; multi-word names need underscores (`?GOOD_MACRO_NAME`).

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Macros", guideline "Uppercase macros".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
