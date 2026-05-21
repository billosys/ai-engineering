---
concept: Avoid Non-Local Returns
slug: avoid-non-local-returns
category: error-handling
subcategory: syntax
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Syntax"
chapter_number: null
pdf_page: null
section: "Avoid non-local returns"
extraction_confidence: high
aliases:
  - "non-local returns"
  - "no throw and catch"
  - "throw/catch for control flow"
prerequisites: []
extends: []
related:
  - avoid-nested-try-catches
  - higher-order-functions-over-recursion
  - loud-errors
contrasts_with: []
answers_questions:
  - "What is a non-local return in Erlang?"
  - "Why should I avoid throw and catch for control flow?"
---

# Quick Definition

Don't use `throw` and `catch` to implement non-local returns.

# Core Definition

"Don't use `throw` and `catch`" (Inaka, "Avoid non-local returns"). `throw` is not meant for throwing exceptions, and using it for non-local returns produces complex code that is hard to reason about — especially when the thrown value is caught in a distant part of the application. Recursion (typically tail recursion) is the preferred alternative.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. `throw`/`catch` should not be used to return a value early from deep in a computation.
2. `throw` is intended for non-local returns, but the guideline discourages even that use.
3. The result being thrown in one place and caught far away makes code hard to follow.
4. Recursion (a recursive search function) is the recommended replacement.

# Construction / Recognition

## To Apply

1. Replace a `catch`-around-`foreach`-with-`throw` pattern with an explicit recursive function.
2. Let the recursive function return the result directly via its base/match clauses.

## To Recognize a Violation

1. `throw/1` is used to break out of an iteration, with a matching `catch`.

# Context & Application

A PR-blocking convention under Syntax.

- **Typical contexts**: "find the first element matching a predicate" implemented with `throw`.
- **Common applications**: rewriting such a search as a two-clause recursive function.
- **Acknowledged rare exception**: the source quotes a discussion noting `throw` can occasionally break out of deep recursion when a tail-recursive rewrite would be too cumbersome.

# Examples

**Example 1** — bad: `catch lists:foreach(fun(Elem) -> case Pred(Elem) of true -> throw(Elem); _ -> noop end end, List)`.

**Example 2** — good: a recursive `good(Pred, [Elem|Elems])` that returns `Elem` on a match and recurses otherwise.

# Relationships

## Related

- **Avoid nested try...catches** — both keep exception/error control flow disciplined.
- **Favor higher-order functions over manual use of recursion** — the recommended replacement uses recursion or folds.
- **Loud errors** — both concern using exceptions for their intended purpose.

# Common Errors

- **Error**: Using `throw` to short-circuit a `foreach`/`map`.
  **Correction**: Write a recursive function that returns the value directly.

# Common Confusions

- **Confusion**: Thinking `throw` is the right tool because it is "meant for non-local returns."
  **Clarification**: Even though that is `throw`'s nominal purpose, the guideline discourages returning values via side effects in a functional language.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Syntax", guideline "Avoid non-local returns". Includes quoted discussion from the Erlang Forums.

# Verification Notes

- Definition source: Direct quote plus paraphrase of the reasoning and quoted forum discussion.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: The source itself notes a rare acceptable exception (breaking out of deep recursion); captured in Context & Application.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
