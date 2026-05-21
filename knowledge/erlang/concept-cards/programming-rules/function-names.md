---
concept: Function Names
slug: function-names
category: core-idioms
subcategory: lexical-stylistic-conventions
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Specific Lexical and Stylistic Conventions"
chapter_number: 7
pdf_page: null
section: "7.6 Function names"
extraction_confidence: high
aliases:
  - "function names"
  - "function naming conventions"
  - "is_ check_ prefixes"
prerequisites: []
extends: []
related:
  - variable-names
  - principle-of-least-astonishment
  - use-tagged-return-values
contrasts_with: []
answers_questions:
  - "How should functions be named in Erlang?"
  - "What naming conventions signal what a function returns?"
---

# Quick Definition

A function's name must agree exactly with what it does and not surprise the reader; use conventional names for conventional functions and naming-prefix conventions to signal return types.

# Core Definition

"The function name must agree exactly with what the function does" (Programming Rules, 7.6). It should return the kind of arguments implied by its name and not surprise the reader. Use conventional names for conventional functions (`start`, `stop`, `init`, `main_loop`). Functions in different modules that solve the same problem should share a name (e.g. `Module:module_info()`). Naming conventions help: an `is_` prefix can signify a function returning `true`/`false`; a `check_` prefix, one returning `{ok, ...}` or `{error, ...}`.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A function name agrees exactly with what the function does.
2. Conventional functions use conventional names (`start`, `stop`, `init`, `main_loop`).
3. Functions solving the same problem in different modules share a name.
4. Prefix conventions signal return type: `is_...() -> true | false`; `check_...() -> {ok, ...} | {error, ...}`.

# Construction / Recognition

## To Apply

1. Name a function for exactly what it does and returns.
2. Use `is_`/`check_` prefixes to signal boolean vs. tagged-result returns.

## To Recognize a Violation

1. A function name does not reflect what the function does (a top common mistake).

# Context & Application

A core lexical/stylistic convention (section 7).

- **Typical contexts**: every function definition.
- **Common applications**: `is_valid/1` returning `true`/`false`; `check_args/1` returning `{ok,...}`/`{error,...}`.

# Examples

**Example** (from source): the prefix conventions `is_...() -> true | false` and `check_...() -> {ok, ...} | {error, ...}`.

# Relationships

## Related

- **Variable names** — companion naming rule.
- **Use the principle of "least astonishment"** — a surprising function is often misnamed.
- **Use tagged return values** — the `check_`-prefix convention pairs with tagged returns.

# Common Errors

- **Error**: Giving a function a name that does not reflect what it does.
  **Correction**: Rename it to agree exactly with its behavior — the source calls bad names one of the most common mistakes.

# Common Confusions

- **Confusion**: Thinking naming is a minor cosmetic concern.
  **Clarification**: The source calls good naming "very difficult" and bad naming one of the most common programming errors.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 7.6 "Function names".

# Verification Notes

- Definition source: Direct adaptation of section 7.6.
- Confidence rationale: HIGH — the rule is stated explicitly with conventions and examples.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
