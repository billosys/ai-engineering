---
concept: Avoid Nested Try...Catches
slug: avoid-nested-try-catches
category: error-handling
subcategory: syntax
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Syntax"
chapter_number: null
pdf_page: null
section: "Avoid nested try...catches"
extraction_confidence: high
aliases:
  - "nested try catch"
  - "no nested try...catch"
prerequisites: []
extends: []
related:
  - avoid-deep-nesting
  - avoid-non-local-returns
  - avoid-case-catch
contrasts_with: []
answers_questions:
  - "Why shouldn't try...catch blocks be nested?"
  - "How do I handle multiple exception types without nesting try...catch?"
---

# Quick Definition

Don't nest `try…catch` clauses inside one another.

# Core Definition

"Don't nest `try…catch` clauses" (Inaka, "Avoid nested try...catches"). Nesting them defeats their purpose, which is to isolate error-handling code from the expected ("nice and shiny") execution path.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A `try…catch` must not appear inside another `try…catch`.
2. Multiple exception types are handled with multiple `catch` clauses in one `try`.
3. Alternatively, inner risky work is delegated to a function that handles its own exception.
4. It is a PR-rejection rule under Syntax.

# Construction / Recognition

## To Apply

1. Collapse nested `try`s into a single `try` with several `catch` clauses (one per exception).
2. Or move the inner risky operation into a separate function that catches its own exception.

## To Recognize a Violation

1. A `try` body textually contains another `try`.

# Context & Application

A PR-blocking convention under Syntax.

- **Typical contexts**: code that must handle two distinct failures from a sequence of risky calls.
- **Common applications**: turning nested `try`s for `exception1`/`exception2` into one `try` with two `catch` clauses.

# Examples

**Example 1** — bad: an outer `try` catching `exception1` wrapping an inner `try` catching `exception2`.

**Example 2** — good1: one `try` with two `catch` clauses, `_:exception1` and `_:exception2`.

**Example 3** — good2: the inner risky work is delegated to `a_function:that_deals(with, exception2)`.

# Relationships

## Related

- **Avoid deep nesting** — nested `try`s are a nesting violation.
- **Avoid non-local returns** — both keep error control flow disciplined.
- **Don't use case catch** — companion rule on disciplined exception handling.

# Common Errors

- **Error**: Wrapping a second `try` inside the first to catch a different exception.
  **Correction**: Add another `catch` clause to the single `try`, or delegate to a helper.

# Common Confusions

- **Confusion**: Believing each exception type needs its own `try`.
  **Clarification**: One `try` can carry many `catch` clauses; nesting is unnecessary.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Syntax", guideline "Avoid nested try...catches".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with three examples.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
