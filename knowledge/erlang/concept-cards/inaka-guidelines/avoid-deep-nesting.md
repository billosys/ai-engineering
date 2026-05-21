---
concept: Avoid Deep Nesting
slug: avoid-deep-nesting
category: core-idioms
subcategory: syntax
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Syntax"
chapter_number: null
pdf_page: null
section: "Avoid deep nesting"
extraction_confidence: high
aliases:
  - "deep nesting"
  - "3 levels deep"
  - "nesting limit"
prerequisites: []
extends: []
related:
  - functions-over-case-expressions
  - keep-functions-small
  - avoid-spaghetti-code
  - spaces-over-tabs
contrasts_with: []
answers_questions:
  - "How deeply may Erlang code be nested?"
  - "How does \"avoid deep nesting\" relate to smaller functions?"
---

# Quick Definition

Try not to nest control structures more than three levels deep.

# Core Definition

"Try not to nest more than 3 levels deep" (Inaka, "Avoid deep nesting"). Nested levels of `case`, `try`, `receive`, etc. signal too many decisions packed into one function; the fix is to refactor inner blocks into separate functions.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The soft limit is three levels of nested control structures.
2. Deep nesting indicates too many decisions in a single function.
3. It harms readability, maintainability, debugging, and unit testing.
4. It is a PR-rejection rule under Syntax.

# Construction / Recognition

## To Apply

1. Count the nesting depth of `case`/`try`/`receive` in a function.
2. When it exceeds three, extract the inner blocks into named functions.

## To Recognize a Violation

1. A function contains a `case` inside a `try` inside a `receive`, etc.

# Context & Application

A PR-blocking convention under Syntax.

- **Typical contexts**: functions that handle several decision points inline.
- **Common applications**: pulling the inner `try` of a nested `case`/`try`/`receive` into its own function.

# Examples

**Example 1** — bad: a function nesting `case` → `try` → `receive` to four levels.

**Example 2** — good: the same logic flattened, with inner work moved into other functions.

# Relationships

## Related

- **More, smaller functions over case expressions** — the primary refactoring that reduces nesting (cross-referenced by the source itself).
- **Keep functions small** — small functions naturally nest shallowly.
- **Don't write spaghetti code** — deep nesting is a spaghetti symptom.
- **Spaces over tabs** — 2-space indentation is explicitly *not* a license to nest deeply.

# Common Errors

- **Error**: Adding "just one more" `case`/`try` inside an already-nested function.
  **Correction**: Extract a named function instead of nesting another level.

# Common Confusions

- **Confusion**: Reading "3 levels" as a hard compiler limit.
  **Clarification**: It is a guideline ("try not to"); the point is the maintainability cost, not a mechanical cap.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Syntax", guideline "Avoid deep nesting". The source explicitly cross-references "More, smaller functions over case expressions".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
