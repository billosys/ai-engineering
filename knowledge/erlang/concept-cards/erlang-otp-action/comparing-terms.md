---
# === CORE IDENTIFICATION ===
concept: Comparing Terms
slug: comparing-terms

# === CLASSIFICATION ===
category: data-types
subcategory: term-comparison
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.2.9 Comparing terms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - term ordering
  - comparison operators
  - exact equality
  - arithmetic equality

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-term
extends: []
related:
  - number
  - atom
  - pattern-matching
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are Erlang terms compared and ordered?"
  - "What is the difference between =:= and ==?"
  - "Why is less-than-or-equal written =< in Erlang?"
---

# Quick Definition

All Erlang terms can be compared and ordered with the same operators, across types, in a single total order. Erlang distinguishes exact equality (`=:=`) from arithmetic equality (`==`).

# Core Definition

"The different data types in Erlang have one thing in common: they can all be compared and ordered, using built-in operators like `<`, `>`, and `==`" (Chapter 2, section 2.2.9). Numbers order normally; atoms, strings, and other lists, and tuples, order lexicographically. There is also an ordering *between* types: all numbers come before all atoms, all atoms before all tuples and lists, and all tuples before all lists. Any two terms can therefore be compared and always give the same result. Less-than-or-equal is written `=<` (not `<=`, which would look like a left arrow); greater-than-or-equal is `>=`. **Exact equality** `=:=` returns `true` only if both sides are exactly the same (so `2 =:= 2.0` is `false`); its negation is `=/=`. **Arithmetic equality** `==` coerces integers to float (so `2 == 2.0` is `true`); its negation is `/=`. The book recommends exact equality for general comparison and warns that `==` masks type errors and hinders tools like Dialyzer.

# Prerequisites

- **Erlang term** — comparison applies to all terms.

# Key Properties

1. All terms can be compared and ordered with the same operators.
2. There is a total order across types: number < atom < tuple < list.
3. Atoms, strings, other lists, and tuples order lexicographically.
4. Less-than-or-equal is `=<`; greater-than-or-equal is `>=` — comparisons never look like arrows.
5. Exact equality `=:=` requires exact sameness; `2 =:= 2.0` is `false`. Negation is `=/=`.
6. Arithmetic equality `==` coerces integers to floats; `2 == 2.0` is `true`. Negation is `/=`.
7. Ordering operators (`<`, `>`, `=<`, `>=`) are arithmetic — they coerce integers to floats.

# Construction / Recognition

## To Identify/Recognize:
1. To test exact sameness, use `=:=` / `=/=`.
2. To compare numbers mathematically, use `==` / `/=` or the ordering operators.
3. `lists:sort/1` orders a list of mixed terms using the total order.

# Context & Application

- **Typical contexts**: Conditions, guards, sorting heterogeneous data.
- **Common applications**: `lists:sort/1` on mixed terms; choosing the right equality operator.
- **Historical/stylistic notes**: Seasoned Erlang programmers usually avoid equality operators altogether and use pattern matching instead, which uses exact equivalence.

# Examples

**Example 1** (section 2.2.9): `1 < 2`, `3.14 > 3`, `'abacus' < 'abba'`, `[1,2,3] > [1,2,2,1]`, and `42 < 'aardvark'` all hold; `lists:sort([b,3,a,"z",1,c,"x",2.5,"y"])` yields a fully sorted list.

**Example 2** (section 2.2.9): `42 =:= 42` is `true`; `2 =:= 2.0` is `false`; `2 == 2.0` is `true`; `2 /= 2.0` is `false`.

# Relationships

## Builds Upon
- **Erlang term** — every term participates in the total order.

## Enables
- Sorting and ordering of heterogeneous data.

## Related
- **Number** — has both exact and arithmetic comparison semantics.
- **Atom** — atoms order lexicographically and after all numbers.
- **Pattern matching** — uses exact equivalence, like `=:=`.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Writing less-than-or-equal as `<=`.
  **Correction**: It is written `=<`; `<=` is reserved as a left arrow. Comparisons never look like arrows.

- **Error**: Using `==` for general term comparison.
  **Correction**: Use `=:=`; `==` coerces integers to floats, masks type errors, and hinders Dialyzer.

# Common Confusions

- **Confusion**: Believing `=:=` and `==` are interchangeable.
  **Clarification**: `=:=` is exact (`2 =:= 2.0` is `false`); `==` is arithmetic and coerces (`2 == 2.0` is `true`).

- **Confusion**: Thinking only same-type values can be compared.
  **Clarification**: Any two terms can be compared; Erlang defines a total order across all types.

# Source Reference

Chapter 2: Erlang language essentials, section 2.2.9 "Comparing terms" (Less-than/greater-than or equals, and Equality comparisons subsections).

# Verification Notes

- Definition source: Direct adaptation from section 2.2.9.
- Confidence rationale: HIGH — term ordering and the equality operators are explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
