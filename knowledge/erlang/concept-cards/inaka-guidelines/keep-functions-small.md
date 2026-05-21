---
concept: Keep Functions Small
slug: keep-functions-small
category: core-idioms
subcategory: suggestions
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Suggestions & Great Ideas"
chapter_number: null
pdf_page: null
section: "Keep functions small"
extraction_confidence: high
aliases:
  - "small functions"
  - "12 expressions per function"
prerequisites: []
extends: []
related:
  - avoid-deep-nesting
  - functions-over-case-expressions
  - no-god-modules
  - simple-unit-tests
contrasts_with: []
answers_questions:
  - "How large should an Erlang function be?"
  - "How does \"keep functions small\" relate to avoiding deep nesting?"
---

# Quick Definition

Write small functions that do only one thing — about 12 expressions per function is a good measure (integration tests excepted).

# Core Definition

"Try to write functions with a small number of expressions, and that do only one thing. **12** expressions per function except for integration tests is a good measure" (Inaka, "Keep functions small"). A small, single-purpose function is easy to read, verify, test, trace, and reuse.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A function does only one thing.
2. ~12 expressions is the suggested size guide; integration tests are exempt.
3. Small functions aid readability, reuse, testing, and runtime tracing.
4. This is a "Suggestion & Great Idea" — advisory, not a PR-blocking rule.

# Construction / Recognition

## To Apply

1. Extract distinct steps into named helpers (`find_or_create_user/1`, `clean_message/1`, `deliver_message/2`).
2. Structure clauses so a tail call to a `continue_*` function resets indentation.

## To Recognize a Candidate

1. A function spans many expressions and performs several distinct tasks.

# Context & Application

A "Suggestion & Great Idea" — advisory; does not by itself block a PR.

- **Typical contexts**: functions that grew to orchestrate several steps.
- **Common applications**: splitting a large `bad/2` into `find_or_create_user/1`, `clean_message/1`, `deliver_message/2`, `send_message/2`.

# Examples

**Example 1** — bad: a `bad/2` function that finds-or-creates a user, cleans a message, stores it, and delivers it via nested `case`s and a `foreach` — all inline.

**Example 2** — good: `good/2` delegates each step to a named helper, each small and single-purpose.

# Relationships

## Related

- **Avoid deep nesting** — the source pairs the two; small functions nest shallowly.
- **More, smaller functions over case expressions** — the source explicitly cross-references it.
- **No God modules** — single responsibility at the module level.
- **Simple unit tests** — small functions create natural testing hinge points.

# Common Errors

- **Error**: Letting one function orchestrate every step of a workflow inline.
  **Correction**: Extract each step into a small, named, single-purpose function.

# Common Confusions

- **Confusion**: Reading "12 expressions" as a hard limit.
  **Clarification**: It is "a good measure," and integration tests are explicitly exempt.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Suggestions & Great Ideas", guideline "Keep functions small". Cross-references "Avoid deep nesting" and "More, smaller functions over case expressions".

# Verification Notes

- Definition source: Direct quote plus paraphrase of the reasoning and notes.
- Confidence rationale: HIGH — explicit suggestion with a detailed bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
