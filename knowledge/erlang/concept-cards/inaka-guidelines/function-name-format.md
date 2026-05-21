---
concept: Function Names
slug: function-name-format
category: core-idioms
subcategory: naming
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Naming"
chapter_number: null
pdf_page: null
section: "Function Names"
extraction_confidence: high
aliases:
  - "function naming"
  - "snake_case functions"
prerequisites: []
extends:
  - lowercase-atoms
related:
  - consistent-module-naming
  - variable-name-format
  - camelcase-variables-underscore-atoms
contrasts_with:
  - variable-name-format
answers_questions:
  - "How should functions be named in Erlang?"
---

# Quick Definition

Function names use only lowercase characters or digits, with words separated by underscores.

# Core Definition

"Function names must use only lowercase characters or digits. Words in function names must be separated with `_`" (Inaka, "Function Names"). Because function names are atoms, they follow the same rules atoms do.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Function names contain only lowercase letters and digits.
2. Words are separated by underscores (`snake_case`).
3. Function names are atoms, so the atom-naming rule applies to them.
4. It is a PR-rejection rule under Naming.

# Construction / Recognition

## To Apply

1. Name functions in lowercase `snake_case` (`good_function`, `base64_encode`).

## To Recognize a Violation

1. A function name uses camelCase (`badFunction`) or is a quoted uppercase atom (`'BAD_FUNCTION'`).

# Context & Application

A PR-blocking convention under Naming.

- **Typical contexts**: every function definition and export.
- **Common applications**: `good_function/0`, `base64_encode/0`.

# Examples

**Example 1** — bad: `badFunction/0` (camelCase) and `'BAD_FUNCTION'/0` (uppercase).

**Example 2** — good: `good_function/0` and `base64_encode/0`.

# Relationships

## Builds Upon

- **Lowercase atoms** — function names are atoms; this rule is the atom rule applied to them.

## Related

- **Stick to one convention for naming modules** — companion naming-format rule.
- **Variable Names** — the complementary rule for variables.
- **CamelCase over Under_Score** — the suggestion summarizing the casing split.

## Contrasts With

- **Variable Names** — variables use CamelCase; functions use lowercase snake_case.

# Common Errors

- **Error**: Naming a function `getUserById`.
  **Correction**: Use `get_user_by_id`.

# Common Confusions

- **Confusion**: Treating function-name casing as separate from atom rules.
  **Clarification**: Function names *are* atoms; the same constraints apply.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Naming", guideline "Function Names".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
