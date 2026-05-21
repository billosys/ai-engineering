---
concept: Lowercase Atoms
slug: lowercase-atoms
category: core-idioms
subcategory: naming
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Naming"
chapter_number: null
pdf_page: null
section: "Lowercase atoms"
extraction_confidence: high
aliases:
  - "atom naming"
  - "snake_case atoms"
prerequisites: []
extends: []
related:
  - function-name-format
  - lowercase-record-names
  - camelcase-variables-underscore-atoms
contrasts_with:
  - variable-name-format
answers_questions:
  - "How should atoms be named in Erlang?"
  - "Should atoms use uppercase or special characters?"
---

# Quick Definition

Atoms should use only lowercase characters, with words separated by underscores; quoted special-case atoms must be justified.

# Core Definition

"Atoms should use only lowercase characters. Words in atom names should be separated with `_`. Special cases are allowed (like `'GET'`, `'POST'`, etc.) but should be properly justified" (Inaka, "Lowercase atoms"). The default atom form is unquoted `snake_case`.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Atoms use lowercase letters only.
2. Words within an atom are separated by underscores.
3. Quoted atoms with caps/special characters (`'GET'`, `'POST'`) are allowed only with justification.
4. It is a PR-rejection rule under Naming.

# Construction / Recognition

## To Apply

1. Write atoms as unquoted lowercase `snake_case` (`also_good`).
2. Use a quoted special-case atom only when there is a clear reason.

## To Recognize a Violation

1. An atom contains uppercase letters or camelCase (`'BAD'`, `alsoBad`, `bad_AS_well`) without justification.

# Context & Application

A PR-blocking convention under Naming.

- **Typical contexts**: tag atoms, status atoms, message tags.
- **Common applications**: `good`, `also_good`; justified special case `'good@its.mail'`.

# Examples

**Example 1** — bad: `['BAD', alsoBad, bad_AS_well]`.

**Example 2** — good: `[good, also_good, 'good@its.mail']`.

# Relationships

## Related

- **Function Names** — function names are atoms and follow the same rule.
- **Record names** — record/field names are atoms and follow the same rule.
- **CamelCase over Under_Score** — the suggestion summarizing atom vs. variable casing.

## Contrasts With

- **Variable Names** — variables use CamelCase; atoms use lowercase `snake_case`. The contrast is what visually distinguishes them.

# Common Errors

- **Error**: Writing camelCase atoms like `alsoBad`.
  **Correction**: Use `also_good`-style lowercase snake_case.

# Common Confusions

- **Confusion**: Thinking quoted atoms are freely allowed.
  **Clarification**: They are permitted for genuine special cases but must be justified.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Naming", guideline "Lowercase atoms".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
