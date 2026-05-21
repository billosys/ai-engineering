---
concept: Honor DRY
slug: honor-dry
category: core-idioms
subcategory: source-code-layout
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Source Code Layout"
chapter_number: null
pdf_page: null
section: "Honor DRY"
extraction_confidence: high
aliases:
  - "DRY"
  - "don't repeat yourself"
prerequisites: []
extends: []
related:
  - maintain-existing-style
  - keep-functions-small
contrasts_with: []
answers_questions:
  - "What does the DRY principle mean for Erlang code?"
  - "Why is DRY a PR-rejection rule rather than a suggestion?"
---

# Quick Definition

Don't write the same code in many places — factor repetition into functions and variables.

# Core Definition

"Don't write the same code in many places, use functions and variables for that" (Inaka, "Honor DRY"). DRY ("Don't Repeat Yourself") is deliberately placed among the PR-blocking rules — not the suggestions — so reviewers can reject PRs that duplicate code or re-implement something already done elsewhere.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Repeated expressions are bound to a variable and reused.
2. Repeated logic is extracted into a shared function.
3. DRY has a wide scope; the source's example is deliberately trivial.
4. It is a PR-rejection rule, chosen as a rule (not a suggestion) so reviewers may enforce it.

# Construction / Recognition

## To Apply

1. When the same expression appears twice, bind it once (often via a pattern match) and reuse the binding.
2. When the same logic appears in several places, extract a function.

## To Recognize a Violation

1. An identical sub-expression is computed more than once in the same scope.
2. A PR re-implements functionality the reviewer knows already exists.

# Context & Application

A PR-blocking convention under Source Code Layout.

- **Typical contexts**: branches of a `case` that recompute the same value.
- **Common applications**: binding `{show, _} = ThingToShow` in a `case` pattern instead of calling `something:from(other, place)` again.

# Examples

**Example 1** — bad: a `case` whose scrutinee `something:from(other, place)` is recomputed inside the matching branch.

**Example 2** — good: the matched value is captured as `ThingToShow` in the pattern and reused.

# Relationships

## Related

- **Maintain existing style** — both are PR-blocking Source Code Layout conventions.
- **Keep functions small** — extracting shared helpers serves both DRY and small functions.

# Common Errors

- **Error**: Calling the same function twice to obtain a value already available from a pattern match.
  **Correction**: Capture it once with `Var = Pattern` (or `Pattern = Expr`) and reuse `Var`.

# Common Confusions

- **Confusion**: Treating DRY as a soft suggestion.
  **Clarification**: The source explicitly classifies it as a rule so it can block PRs.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Source Code Layout", guideline "Honor DRY".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
