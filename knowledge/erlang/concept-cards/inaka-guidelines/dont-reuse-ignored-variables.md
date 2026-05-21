---
concept: Don't Use _Ignored Variables
slug: dont-reuse-ignored-variables
category: core-idioms
subcategory: naming
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Naming"
chapter_number: null
pdf_page: null
section: "Don't use _Ignored variables"
extraction_confidence: high
aliases:
  - "underscore variables"
  - "ignored variables"
  - "_-prefixed variables"
prerequisites: []
extends: []
related:
  - variable-name-format
contrasts_with: []
answers_questions:
  - "Can I use a variable whose name begins with an underscore?"
  - "What does a leading underscore on a variable name mean?"
---

# Quick Definition

A variable whose name begins with `_` signals "deliberately unused" — if you actually use it, don't give it the underscore.

# Core Definition

"Variables beginning with _ are still variables, and are matched and bound, the _ just keeps the compiler from warning when you don't use them. If you add the _ to a variable's name, don't use it" (Inaka, "Don't use _Ignored variables"). The leading underscore is a promise to the reader and compiler that the binding is ignored.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A `_`-prefixed variable is still a real, bound variable.
2. The `_` only suppresses the compiler's unused-variable warning.
3. If a value is needed, the variable must not carry the `_` prefix.
4. It is a PR-rejection rule under Naming.

# Construction / Recognition

## To Apply

1. Prefix a binding with `_` only when you will not reference it.
2. If you do reference it, rename it without the `_`.

## To Recognize a Violation

1. A `_`-prefixed variable (e.g., `_Number`) is used in the function body.

# Context & Application

A PR-blocking convention under Naming.

- **Typical contexts**: function clause heads with arguments some clauses ignore.
- **Common applications**: renaming `_Number` to `Number` once it is actually multiplied.

# Examples

**Example 1** — bad: `bad(_Number) -> 2 * _Number.` — the "ignored" variable is used.

**Example 2** — good: `good(Number) -> 2 * Number.`

# Relationships

## Related

- **Variable Names** — both govern how variables are named.

# Common Errors

- **Error**: Keeping the `_` prefix on a parameter you go on to use, just to silence a warning.
  **Correction**: Drop the `_`; the warning was telling the truth that the variable *is* used.

# Common Confusions

- **Confusion**: Believing `_Var` is a special "weak" or read-only variable.
  **Clarification**: It is an ordinary variable; only the unused-warning suppression differs.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Naming", guideline "Don't use _Ignored variables".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: `variable-name-format` is a planned card in this extraction.
