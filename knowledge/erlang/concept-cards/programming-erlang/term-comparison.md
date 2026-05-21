---
# === CORE IDENTIFICATION ===
concept: Term Comparison and Ordering
slug: term-comparison

# === CLASSIFICATION ===
category: core-idioms
subcategory: expressions
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "Term Comparisons"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - term ordering
  - total order of terms
  - "=:="
  - "=="

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - operator-precedence
  - numbers
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are Erlang terms ordered and compared?"
  - "What is the difference between == and =:=?"
  - "What is the total ordering of term types?"
---

# Quick Definition

Erlang defines a total order over all terms and eight comparison operators; `==` compares for equality (coercing numbers) while `=:=` tests that two terms are identical.

# Core Definition

"There are eight possible term comparison operations" ("The Rest of Sequential Erlang", *Term Comparisons*): `>`, `<`, `=<`, `>=`, `==` (equal), `/=` (not equal), `=:=` (identical), `=/=` (not identical). For comparison, a total ordering is defined over all terms: `number < atom < reference < fun < port < pid < tuple (and record) < map < list < binary`. All comparison operators except `=:=` and `=/=` coerce: if one argument is an integer and the other a float, the integer is converted to a float before comparing. The book warns: "In 99 out of 100 cases, you should be using `=:=`. `==` is useful *only* when comparing floats with integers. `=:=` is for testing whether two terms are *identical*." Identical means having the same value (like Common Lisp `EQUAL`); since values are immutable, this implies no pointer identity. Function clause matching always implies exact matching, so a fun `F = fun(12) -> ... end` fails on `F(12.0)`.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. There are eight comparison operators: `> < =< >= == /= =:= =/=`.
2. A total order is defined over all terms: `number < atom < reference < fun < port < pid < tuple (and record) < map < list < binary`.
3. All operators except `=:=` and `=/=` coerce a mixed integer/float pair to floats before comparing.
4. `==` is equality with coercion; `=:=` tests identity (same value, no coercion).
5. `/=` is "not equal"; `=/=` is "not identical".
6. The total order lets lists of any type be sorted and efficient key-ordered data structures be built.
7. Function clause matching always uses exact (identical) matching.

# Construction / Recognition

## To Construct/Create:
1. Use `=:=`/`=/=` for identity tests (the usual choice).
2. Use `==`/`/=` only when deliberately comparing floats with integers.

## To Identify/Recognize:
1. Seeing `==` in code is a signal to check whether `=:=` was intended.

# Context & Application

- **Typical contexts**: comparisons, sorting, ordered data structures.
- **Common applications**: a total order over all terms enables sorting heterogeneous lists and building key-ordered access structures.
- **Historical/stylistic notes**: much library and published code uses `==` where `=:=` was meant; the error is usually harmless because the operators behave identically when no floats are involved.

# Examples

**Example 1** (*Term Comparisons*): the total ordering means a number (any number) is smaller than an atom (any atom), and a tuple is greater than an atom.

**Example 2** (*Term Comparisons*): exact matching in funs — for `F = fun(12) -> ... end`, evaluating `F(12.0)` fails, because function clause matching is exact and `12` is not identical to `12.0`.

# Relationships

## Builds Upon
- This is a foundational concept.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Operator precedence** — The comparison operators form one row of the precedence table.
- **Numbers** — Integer/float coercion in `==` depends on the numeric types.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Using `==` for a general equality test.
  **Correction**: Use `=:=` for identity; reserve `==` for deliberately comparing floats with integers.

# Common Confusions

- **Confusion**: Thinking `==` and `=:=` always behave the same.
  **Clarification**: They differ when comparing an integer with a float — `==` coerces, `=:=` does not (so `1 == 1.0` is true but `1 =:= 1.0` is false).

- **Confusion**: Believing "identical" implies pointer identity.
  **Clarification**: Identical means same value; since Erlang values are immutable there is no separate pointer-identity notion.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Term Comparisons" (Table 6).

# Verification Notes

- Definition source: Direct quotation and adaptation from *Term Comparisons*.
- Confidence rationale: HIGH — the source enumerates every operator, the total order, and the `==`/`=:=` distinction.
- Uncertainties: None.
- Cross-reference status: Slugs `operator-precedence`, `numbers` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
