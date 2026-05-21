---
concept: Comment Each Function
slug: comment-each-function
category: documentation
subcategory: documenting-code
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Documenting Code"
chapter_number: 8
pdf_page: null
section: "8.6 Comment each function"
extraction_confidence: high
aliases:
  - "comment each function"
  - "function documentation"
prerequisites: []
extends: []
related:
  - comment-conventions
  - document-data-structures
contrasts_with: []
answers_questions:
  - "What should the comment for a function document?"
---

# Quick Definition

Document every function — its purpose, the domain of its inputs and outputs, any complicated algorithm, its causes of failure, and any side effects.

# Core Definition

Per Programming Rules 8.6, the important things to document for a function are: its purpose; the domain of valid inputs (the argument data structures and their meaning); the domain of outputs (all possible return data structures and their meaning); the algorithm, if complicated; the possible causes of failure and exit signals from `exit/1`, `throw/1`, or non-obvious runtime errors (noting the difference between failure and returning an error); and any side effects.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The function's purpose is documented.
2. The input domain — argument data structures and meanings — is documented.
3. The output domain — all return data structures and meanings — is documented.
4. A complicated algorithm is described.
5. Causes of failure and exit signals are documented, distinguished from returned errors.
6. Side effects are documented.

# Construction / Recognition

## To Apply

1. Write a `%%`-level comment block covering purpose, args, returns, failures, and side effects.

## To Recognize a Violation

1. A function's comment omits its input/output domains, failure modes, or side effects.

# Context & Application

A core documentation rule (section 8).

- **Typical contexts**: every function definition.
- **Common applications**: a boxed `%% Function/Purpose/Args/Returns` comment header.

# Examples

**Example** (from source): a comment block for `get_server_statistics/2` documenting Function, Purpose, Args (`Option is normal|all`), and Returns (`A list of {Key, Value}` or `{error, Reason}`).

# Relationships

## Related

- **Comments** — function comments use the `%%` convention.
- **Data structures** — argument/return data structures are documented alongside their records.

# Common Errors

- **Error**: Documenting only what a function does, omitting failure modes and side effects.
  **Correction**: Cover purpose, input/output domains, failures/exit signals, and side effects.

# Common Confusions

- **Confusion**: Conflating "failure" with "returning an error".
  **Clarification**: The source explicitly distinguishes them — both should be documented, separately.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 8.6 "Comment each function".

# Verification Notes

- Definition source: Direct adaptation of section 8.6.
- Confidence rationale: HIGH — the rule is stated explicitly with an example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
