---
concept: Variable Names
slug: variable-name-format
category: core-idioms
subcategory: naming
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Naming"
chapter_number: null
pdf_page: null
section: "Variable Names"
extraction_confidence: high
aliases:
  - "variable naming"
  - "CamelCase variables"
prerequisites: []
extends: []
related:
  - function-name-format
  - lowercase-atoms
  - consistent-concept-naming
  - short-meaningful-variable-names
  - camelcase-variables-underscore-atoms
contrasts_with:
  - function-name-format
  - lowercase-atoms
answers_questions:
  - "How should variables be named in Erlang?"
  - "Should I separate words in variable names with underscores?"
---

# Quick Definition

Use CamelCase for variable names; do not separate words with underscores.

# Core Definition

"CamelCase must be used for variables. Don't separate words in variables with `_`" (Inaka, "Variable Names"). Variables are written `VariableName`, not `Variable_Name`.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Variables use CamelCase.
2. Underscores do not separate words within a variable name.
3. CamelCase makes variables visually distinct from (lowercase) atoms and matches the OTP standard.
4. It is a PR-rejection rule under Naming.

# Construction / Recognition

## To Apply

1. Write multi-word variables as `VariableName`.

## To Recognize a Violation

1. A variable name contains an underscore between words (`Another_Variable_Name`).

# Context & Application

A PR-blocking convention under Naming.

- **Typical contexts**: every binding in every function.
- **Common applications**: `Variable`, `VariableName`.

# Examples

**Example 1** — bad: `bad(Variablename, Another_Variable_Name)`.

**Example 2** — good: `good(Variable, VariableName)`.

# Relationships

## Related

- **Function Names** — the complementary format rule for functions.
- **Lowercase atoms** — the complementary format rule for atoms.
- **Be consistent when naming concepts** — naming consistency builds on this format.
- **Prefer shorter (but still meaningful) variable names** — refines variable naming further.
- **CamelCase over Under_Score** — the suggestion summarizing the casing split.

## Contrasts With

- **Function Names** — functions use lowercase snake_case; variables use CamelCase.
- **Lowercase atoms** — atoms use lowercase snake_case; variables use CamelCase.

# Common Errors

- **Error**: Writing `User_Id` for a variable.
  **Correction**: Write `UserId`.

# Common Confusions

- **Confusion**: Carrying snake_case habits from atoms over to variables.
  **Clarification**: The casing split is deliberate — it visually separates variables from atoms.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Naming", guideline "Variable Names".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
