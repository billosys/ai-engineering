---
concept: CamelCase Over Under_Score
slug: camelcase-variables-underscore-atoms
category: core-idioms
subcategory: suggestions
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Suggestions & Great Ideas"
chapter_number: null
pdf_page: null
section: "CamelCase over Under_Score"
extraction_confidence: high
aliases:
  - "CamelCase over Under_Score"
  - "casing convention summary"
prerequisites: []
extends: []
related:
  - variable-name-format
  - function-name-format
  - lowercase-atoms
  - consistent-module-naming
  - short-meaningful-variable-names
contrasts_with: []
answers_questions:
  - "What is the overall casing convention for Erlang symbols?"
  - "How does CamelCase-over-underscore relate to the variable/atom naming rules?"
---

# Quick Definition

Use CamelCase for variables; use underscores (snake_case) for atoms, function names, and module names.

# Core Definition

"Symbol naming: Use variables in CamelCase and atoms, function and module names with underscores" (Inaka, "CamelCase over Under_Score"). This suggestion summarizes the casing split: variables are `CamelCase`; atoms, functions, and modules are lowercase `snake_case`.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Variables use CamelCase.
2. Atoms, function names, and module names use lowercase with underscores.
3. The split visually distinguishes variables from atoms.
4. This is a "Suggestion & Great Idea" that restates the PR-blocking Naming rules in one line.

# Construction / Recognition

## To Apply

1. Write variables as `VariableName`.
2. Write atoms, functions, and modules as `snake_case`.

## To Recognize a Candidate

1. A variable uses `Under_Score`, or an atom/function/module uses camelCase.

# Context & Application

A "Suggestion & Great Idea" — advisory in form, though it summarizes rules ("Variable Names", "Function Names", "Lowercase atoms") that *are* PR-blocking.

- **Typical contexts**: every identifier in every module.
- **Common applications**: `VariableName = module_name:function_name(atom_constant)`.

# Examples

**Example 1** — bad: `Variable_Name = moduleName:functionName(atomConstant)`.

**Example 2** — good: `VariableName = module_name:function_name(atom_constant)`.

# Relationships

## Related

- **Variable Names** — the PR-blocking rule for the CamelCase half.
- **Function Names** — the PR-blocking rule for the function half.
- **Lowercase atoms** — the PR-blocking rule for the atom half.
- **Stick to one convention for naming modules** — the module-naming companion.
- **Prefer shorter (but still meaningful) variable names** — the source notes this suggestion "helps a lot with the next issue."

# Common Errors

- **Error**: Mixing `Under_Score` variables with `camelCase` atoms.
  **Correction**: CamelCase variables, snake_case everything else.

# Common Confusions

- **Confusion**: Treating this as a separate, weaker rule.
  **Clarification**: It is a one-line summary of three PR-blocking Naming rules; the underlying conventions are enforced.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Suggestions & Great Ideas", guideline "CamelCase over Under_Score".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit suggestion with a bad/good example.
- Uncertainties: None — overlap with the Naming-section rules is intentional and cross-referenced.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
