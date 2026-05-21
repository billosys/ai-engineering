---
concept: No Macros
slug: avoid-macros
category: core-idioms
subcategory: macros
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Macros"
chapter_number: null
pdf_page: null
section: "No Macros"
extraction_confidence: high
aliases:
  - "no macros"
  - "avoid macros"
  - "macro avoidance"
prerequisites: []
extends: []
related:
  - no-module-or-function-name-macros
  - uppercase-macro-names
  - header-file-contents
contrasts_with: []
answers_questions:
  - "Should I use macros in Erlang?"
  - "What distinguishes an acceptable macro use from one that should be avoided?"
---

# Quick Definition

Don't use macros, except for a few specific cases: the predefined `?MODULE`, `?MODULE_STRING`, `?LINE`, and literal constants like `?DEFAULT_TIMEOUT`.

# Core Definition

"Don't use macros, except for very specific cases" (Inaka, "No Macros"). The permitted exceptions are the predefined macros (`?MODULE`, `?MODULE_STRING`, `?LINE`) and literal constants (`?DEFAULT_TIMEOUT`, `?HTTP_CREATED`). Macros that wrap blocks of code should be replaced by functions.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Macros are avoided by default.
2. Predefined macros `?MODULE`, `?MODULE_STRING`, `?LINE` are allowed.
3. Literal-constant macros (e.g., `?HTTP_CREATED`, `?DEFAULT_TIMEOUT`) are allowed.
4. Code-block macros should be functions instead; macros make code harder to debug.

# Construction / Recognition

## To Apply

1. Use a macro only for a predefined name or a literal constant.
2. Replace any macro that expands to a code block with a function.

## To Recognize a Violation

1. A `-define` expands to multi-expression code (e.g., `?LOG_ERROR(...)`).

# Context & Application

A PR-blocking convention under Macros.

- **Typical contexts**: logging helpers, repeated expressions.
- **Common applications**: replacing a `?LOG_ERROR` macro with a `log_error/2` function; keeping `?HTTP_CREATED` as a literal constant.

# Examples

**Example 1** — bad: `?OTHER_MODULE` (a module-name macro) and `?LOG_ERROR(Error)` (a code-block macro).

**Example 2** — good: a literal constant `?HTTP_CREATED` plus a real `log_error/2` function.

# Relationships

## Related

- **No module or function name macros** — a specific case of macro avoidance.
- **Uppercase macros** — the naming rule for the macros you do keep.
- **Header files** — headers may define macros but, per this rule, macros should be avoided anyway.

# Common Errors

- **Error**: Defining a macro to avoid repeating a block of code.
  **Correction**: Extract a function — functions are debuggable; macro expansions are not.

# Common Confusions

- **Confusion**: Reading the rule as a total ban.
  **Clarification**: Predefined macros and literal constants are explicitly permitted.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Macros", guideline "No Macros". Links a blog post by @erszcz on when not to use macros.

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
