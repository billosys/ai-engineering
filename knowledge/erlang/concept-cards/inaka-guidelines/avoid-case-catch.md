---
concept: Don't Use Case Catch
slug: avoid-case-catch
category: error-handling
subcategory: misc
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Misc"
chapter_number: null
pdf_page: null
section: "Don't Use Case Catch"
extraction_confidence: high
aliases:
  - "case catch"
  - "no case catch"
prerequisites: []
extends: []
related:
  - avoid-nested-try-catches
  - avoid-non-local-returns
  - loud-errors
contrasts_with: []
answers_questions:
  - "Why shouldn't I use case catch to handle errors?"
  - "What distinguishes try...of...catch from case catch?"
---

# Quick Definition

Don't capture errors with `case catch ...`; use `try ... of ... catch` instead.

# Core Definition

"Don't capture errors with `case catch`, use `try ... of ... catch` instead" (Inaka, "Don't Use Case Catch"). `case catch` mixes successful results and `'EXIT'` tuples in the same scrutinee, which is confusing; `try...of...catch` keeps the success path and the error-handling path syntactically separate.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. `case catch Expr of ... end` is disallowed for error capture.
2. `try Expr of Pattern -> ... catch Class:Reason -> ... end` is the replacement.
3. `case catch` blends good results with `'EXIT'` error tuples in one match.
4. It is a PR-rejection rule under Misc.

# Construction / Recognition

## To Apply

1. Rewrite `case catch Expr of {'EXIT', ...} -> ...; Ok -> ... end` as a `try Expr of Ok -> ... catch ... -> ... end`.

## To Recognize a Violation

1. A `case` scrutinee is a `catch` expression, with an `{'EXIT', ...}` clause among the patterns.

# Context & Application

A PR-blocking convention under Misc.

- **Typical contexts**: guarding calls that may raise (`hd/1` on a possibly-empty list).
- **Common applications**: replacing `case catch hd(List) of ...` with `try hd(List) of Hd -> Hd catch badarg:T -> {badarg, T} end`.

# Examples

**Example 1** — bad: `case catch hd(List) of {'EXIT', {badarg, Reason}} -> {badarg, Reason}; Hd -> Hd end`.

**Example 2** — good: `try hd(List) of Hd -> Hd catch badarg:T -> {badarg, T} end`.

# Relationships

## Related

- **Avoid nested try...catches** — companion rule on disciplined exception handling.
- **Avoid non-local returns** — both keep error control flow clean.
- **Loud errors** — both concern handling errors deliberately rather than incidentally.

# Common Errors

- **Error**: Using `case catch` so success and `'EXIT'` tuples are matched together.
  **Correction**: Use `try...of...catch`, keeping the golden path separate from error handling.

# Common Confusions

- **Confusion**: Thinking `case catch` is a concise idiom.
  **Clarification**: Its concision comes from blending results and errors — exactly the confusion `try...of...catch` removes.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Misc", guideline "Don't Use Case Catch".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
