---
concept: Avoid Unnecessary Calls To length/1
slug: avoid-length-1-calls
category: performance
subcategory: suggestions
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Suggestions & Great Ideas"
chapter_number: null
pdf_page: null
section: "Avoid unnecessary calls to length/1"
extraction_confidence: high
aliases:
  - "length/1"
  - "avoid length calls"
prerequisites: []
extends: []
related:
  - prefer-pattern-matching-over-equality
  - iolists-over-string-concatenation
contrasts_with: []
answers_questions:
  - "How do I avoid an unnecessary call to length/1?"
  - "How do I check whether a list has at least one element?"
---

# Quick Definition

Replace unnecessary `length/1` calls with pattern matching — especially when checking whether a list is empty or has at least one element.

# Core Definition

"Lots of use cases of length/1 can be replaced by pattern matching, this is specially true when checking if the list has at least one element" (Inaka, "Avoid unnecessary calls to length/1"). `length/1` traverses the whole list; matching on `[]` versus `[_|_]` answers emptiness in constant time.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Many `length/1` calls exist only to test emptiness or non-emptiness.
2. Such tests are better expressed by matching `[]` vs `[_|_]` (or a head pattern).
3. `length/1` is O(n); a pattern match is O(1).
4. This is a "Suggestion & Great Idea" — advisory, not a PR-blocking rule.

# Construction / Recognition

## To Apply

1. Replace `case length(L) of 0 -> ...; _ -> ... end` with clauses matching `[]` and `[_|_]` (or `_L`).

## To Recognize a Candidate

1. `length/1` is called only to compare against `0` or to test "non-empty."

# Context & Application

A "Suggestion & Great Idea" — advisory; does not by itself block a PR.

- **Typical contexts**: emptiness checks on lists.
- **Common applications**: `good([]) -> error; good(_L) -> ok.`

# Examples

**Example 1** — bad: `bad(L) -> case length(L) of 0 -> error; _ -> ok end.`

**Example 2** — good: `good([]) -> error; good(_L) -> ok.`

# Relationships

## Related

- **Prefer pattern-matching over testing for equality** — same preference for matching over computed tests.
- **IOLists over string concatenation** — both concern efficient handling of list-shaped data.

# Common Errors

- **Error**: Calling `length(L)` and comparing to `0` to test emptiness.
  **Correction**: Match `[]` vs `[_|_]`; it is constant-time and more flexible.

# Common Confusions

- **Confusion**: Thinking `length/1` is cheap.
  **Clarification**: It traverses the entire list; matching the list's shape avoids that traversal.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Suggestions & Great Ideas", guideline "Avoid unnecessary calls to length/1".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit suggestion with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
