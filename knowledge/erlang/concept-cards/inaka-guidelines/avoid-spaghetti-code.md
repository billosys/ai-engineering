---
concept: Avoid Spaghetti Code
slug: avoid-spaghetti-code
category: core-idioms
subcategory: syntax
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Syntax"
chapter_number: null
pdf_page: null
section: "Don't write spaghetti code"
extraction_confidence: high
aliases:
  - "spaghetti code"
  - "no spaghetti code"
prerequisites: []
extends: []
related:
  - avoid-deep-nesting
  - functions-over-case-expressions
  - keep-functions-small
contrasts_with: []
answers_questions:
  - "What is spaghetti code in Erlang?"
  - "How do I avoid spaghetti code in Erlang?"
---

# Quick Definition

Don't write spaghetti code — such as a list comprehension with a `case` inside it, `begin/end` blocks, or other deeply nested constructs.

# Core Definition

"Don't write spaghetti code (A list comprehension with a case inside, or blocks with begin/end, and nested stuff)" (Inaka, "Don't write spaghetti code"). Spaghetti code tangles control flow inside expressions; the fix is to extract the tangled parts into named helper functions so the call graph stays a directed acyclic graph.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A `case` nested inside a list comprehension's generator is a typical spaghetti pattern.
2. `begin/end` blocks and other in-expression nesting are also flagged.
3. The remedy is extracting helper functions and binding intermediate results.
4. The program's function call graph should strive to be a DAG.

# Construction / Recognition

## To Apply

1. Extract any `case`/block embedded inside an expression into a named function.
2. Bind intermediate results to variables before using them.

## To Recognize a Violation

1. A list comprehension contains a `case` in its generator expression.
2. Logic is buried inside `begin/end` blocks rather than functions.

# Context & Application

A PR-blocking convention under Syntax.

- **Typical contexts**: data-transformation pipelines, comprehensions over computed sources.
- **Common applications**: pulling a `case` out of `autocomplete_db:members(...)` into a `client_ac_key/1` helper.

# Examples

**Example 1** — bad: a comprehension `[binary_to_list(Org) || Org <- autocomplete_db:members(case Client of ... end)]`.

**Example 2** — good: `RawOrgs` is bound from `autocomplete_db:members(client_ac_key(Client))`, with `client_ac_key/1` a separate clause-based function.

# Relationships

## Related

- **Avoid deep nesting** — spaghetti code is a nesting symptom.
- **More, smaller functions over case expressions** — the extraction technique that untangles it.
- **Keep functions small** — small functions resist becoming spaghetti.

# Common Errors

- **Error**: Embedding a `case` in a comprehension's generator.
  **Correction**: Move the `case` into a named helper and call that from the generator.

# Common Confusions

- **Confusion**: Thinking comprehensions are inherently bad.
  **Clarification**: Comprehensions are fine — embedding control flow *inside* them is the problem.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Syntax", guideline "Don't write spaghetti code".

# Verification Notes

- Definition source: Direct quote plus paraphrase of the reasoning.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
