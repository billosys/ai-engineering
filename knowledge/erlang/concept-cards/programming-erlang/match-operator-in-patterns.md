---
# === CORE IDENTIFICATION ===
concept: Match Operator in Patterns
slug: match-operator-in-patterns

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: pattern-matching
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "Match Operator in Patterns"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "= in patterns"
  - bind-whole pattern
  - "Pattern=Var"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
extends:
  - pattern-matching
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can the match operator be used inside a pattern?"
  - "How do I bind a whole subterm while also destructuring it?"
---

# Quick Definition

The match operator `=` can be used inside a pattern, written `Pattern=Var`, to bind a variable to an entire subterm while still pattern matching its structure.

# Core Definition

When code matches a term such as `{tag1, A, B}` in a function head and then needs to pass that same term to another function, rebuilding the term is inefficient and error-prone. "A much more efficient and less error-prone way to do this is to assign the pattern to a temporary variable, `Z`, and pass this into `f`" ("The Rest of Sequential Erlang", *Match Operator in Patterns*): write `func1([{tag1, A, B}=Z|T]) -> ... f(... Z, ...)`. The match operator can be used at any point in the pattern, so multiple subterms can each be captured with their own variable, e.g. `func1([{tag, {one, A}=Z1, B}=Z2|T]) -> ...` binds both the inner `{one, A}` (as `Z1`) and the outer tuple (as `Z2`).

# Prerequisites

- **Pattern matching** — Using `=` inside a pattern extends ordinary pattern matching.

# Key Properties

1. `Pattern=Var` in a pattern matches `Pattern` and also binds `Var` to the whole matched subterm.
2. The match operator can be used at any point within a pattern.
3. Multiple subterms can each be captured with separate variables in one pattern.
4. It avoids rebuilding a term that was already pattern matched.

# Construction / Recognition

## To Construct/Create:
1. Capture a whole subterm: `func1([{tag1, A, B}=Z|T]) -> ...` binds `Z` to `{tag1, A, B}`.
2. Capture nested subterms: `func1([{tag, {one, A}=Z1, B}=Z2|T]) -> ...`.

## To Identify/Recognize:
1. A `=` appearing inside a pattern (not at the top level of a match) is the match-operator-in-pattern construct.

# Context & Application

- **Typical contexts**: function heads that destructure a term and also need to pass it on whole.
- **Common applications**: avoiding the cost and error risk of rebuilding `{tag1, A, B}` to pass to another function.
- **Historical/stylistic notes**: rebuilding a matched term wastes work and risks subtle mistakes; capturing it with `=` is preferred.

# Examples

**Example 1** (*Match Operator in Patterns*): capturing a whole subterm:

```erlang
func1([{tag1, A, B}=Z|T]) ->
    ... f(... Z, ...)
    ...
```

**Example 2** (*Match Operator in Patterns*): capturing nested subterms with `Z1` and `Z2`:

```erlang
func1([{tag, {one, A}=Z1, B}=Z2|T]) ->
    ... f(..., Z2, ...),
    ... g(..., Z1, ...),
    ...
```

# Relationships

## Builds Upon
- **Pattern matching** — This construct extends ordinary pattern matching.

## Enables
- This concept does not have downstream cards in scope.

## Related
- No directly related concept in scope.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Rebuilding a term in a function body that was already matched in the head.
  **Correction**: Capture the matched term with `Pattern=Var` and pass `Var` instead.

# Common Confusions

- **Confusion**: Thinking the match operator can only appear at the top level of a match expression.
  **Clarification**: `=` may be used at any point within a pattern to bind a subterm.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Match Operator in Patterns".

# Verification Notes

- Definition source: Direct adaptation of the *Match Operator in Patterns* section.
- Confidence rationale: HIGH — the source explicitly demonstrates the construct with worked examples.
- Uncertainties: None.
- Cross-reference status: Slug `pattern-matching` assumed canonical.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
