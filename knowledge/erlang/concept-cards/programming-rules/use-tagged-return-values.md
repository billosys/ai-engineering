---
concept: Use Tagged Return Values
slug: use-tagged-return-values
category: error-handling
subcategory: erlang-specific-conventions
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Various Erlang Specific Conventions"
chapter_number: 6
pdf_page: null
section: "6.3 Use tagged return values"
extraction_confidence: high
aliases:
  - "tagged return values"
  - "{value, V} vs false"
prerequisites: []
extends: []
related:
  - dont-assume-caller-intent
  - function-names
contrasts_with: []
answers_questions:
  - "What is a tagged return value?"
  - "What distinguishes a tagged return value from an untagged one?"
---

# Quick Definition

Return tagged values from functions, so that a successful result can never be confused with a "not found" or error value.

# Core Definition

"Use tagged return values" (Programming Rules, 6.3). If `keysearch` returns a bare `Value` on success and `false` on failure, then a stored value of `false` cannot be distinguished from "not found". Returning `{value, Value}` on success (and `false` on failure) tags the result so the two cases are always distinguishable.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A successful result is wrapped in a tag (e.g. `{value, Value}`).
2. A tag keeps the success value distinct from sentinel values like `false`.
3. Untagged returns fail when a legitimate result coincides with the sentinel.

# Construction / Recognition

## To Apply

1. Return `{value, Value}` (or `{ok, Value}`) on success and a distinct atom on failure.

## To Recognize a Violation

1. A function returns a bare value on success and a sentinel atom on failure, so the two can collide.

# Context & Application

A core Erlang-specific convention (section 6).

- **Typical contexts**: lookup and search functions.
- **Common applications**: `keysearch/2` returning `{value, Value}` or `false`.

# Examples

**Example** (from source): the bad `keysearch/2` returns a bare `Value` (so `{Key, Value}` cannot hold `false`); the correct version returns `{value, Value}` — "Return a tagged value".

# Relationships

## Related

- **Don't make assumptions about what the caller will do with the results** — error descriptors are likewise tagged.
- **Function names** — the `check_...() -> {ok, ...} | {error, ...}` naming convention pairs with tagged returns.

# Common Errors

- **Error**: Returning a bare value on success and `false` on failure.
  **Correction**: Tag the success case (`{value, Value}`) so it cannot collide with the sentinel.

# Common Confusions

- **Confusion**: Thinking an untagged return is fine if the value "would never be `false`".
  **Clarification**: Assumptions like that break silently; tagging removes the ambiguity entirely.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 6.3 "Use tagged return values".

# Verification Notes

- Definition source: Direct adaptation of section 6.3.
- Confidence rationale: HIGH — the rule is stated explicitly with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
