---
concept: Favor Higher-Order Functions Over Manual Recursion
slug: higher-order-functions-over-recursion
category: functions-pattern-matching
subcategory: suggestions
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Suggestions & Great Ideas"
chapter_number: null
pdf_page: null
section: "Favor higher-order functions over manual use of recursion"
extraction_confidence: high
aliases:
  - "higher-order functions"
  - "folds over recursion"
  - "list comprehensions over recursion"
prerequisites: []
extends: []
related:
  - avoid-non-local-returns
  - keep-functions-small
contrasts_with: []
answers_questions:
  - "Should I write a recursive function or use a fold/comprehension?"
  - "What must I understand before favoring higher-order functions over manual recursion?"
---

# Quick Definition

Prefer a fold, map, or list comprehension over hand-written recursion; recursion is occasionally best, but higher-order functions are usually safer and clearer.

# Core Definition

"Occasionally recursion is the best way to implement a function, but often a fold or a list comprehension will yield safer, more comprehensible code" (Inaka, "Favor higher-order functions over manual use of recursion"). Higher-order constructs behave predictably — one action per element — whereas a hand-written recursive function must be scrutinized to verify its control flow and base case.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Folds, maps, and comprehensions are preferred over manual recursion for list processing.
2. Recursion is still occasionally the best choice.
3. A buggy recursive function can miss its base case and take down a whole node.
4. This is a "Suggestion & Great Idea" — advisory, not a PR-blocking rule.

# Construction / Recognition

## To Apply

1. For an accumulation, use `lists:foldl/3`.
2. For a 1:1 transformation, use `lists:map/2` or a list comprehension — whichever is simplest.
3. Reserve explicit recursion for cases the higher-order forms cannot express cleanly.

## To Recognize a Candidate

1. A hand-written two-clause recursive function simply maps or folds over a list.

# Context & Application

A "Suggestion & Great Idea" — advisory; does not by itself block a PR.

- **Typical contexts**: list transformations and accumulations.
- **Common applications**: capitalizing a string via `[string:to_upper(C) || C <- S]` rather than manual recursion.

# Examples

**Example 1** — bad: a manual two-clause `recurse/2` that reverses an accumulator to capitalize a string.

**Example 2** — good/better/best: the same result via `lists:foldl/3`, then `lists:map/2`, then a list comprehension `[string:to_upper(C) || C <- S]`.

# Relationships

## Related

- **Avoid non-local returns** — both steer away from error-prone manual control flow.
- **Keep functions small** — higher-order forms are typically smaller than recursive equivalents.

# Common Errors

- **Error**: Hand-writing recursion for a plain map or fold.
  **Correction**: Use `lists:map/2`, `lists:foldl/3`, or a comprehension.

# Common Confusions

- **Confusion**: Thinking recursion is always the "functional" choice.
  **Clarification**: Folds and comprehensions are equally functional, more predictable, and harder to get wrong.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Suggestions & Great Ideas", guideline "Favor higher-order functions over manual use of recursion".

# Verification Notes

- Definition source: Direct quote plus paraphrase of the reasoning.
- Confidence rationale: HIGH — explicit suggestion with a four-way example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
