---
# === CORE IDENTIFICATION ===
concept: List Comprehension
slug: list-comprehension

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: list-processing
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Modules and Functions"
chapter_number: 4
pdf_page: null
section: "List Comprehensions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "[X || ...]"
  - generator
  - comprehension

# === TYPED RELATIONSHIPS ===
prerequisites:
  - list
  - pattern-matching
extends: []
related:
  - higher-order-function
  - fun
contrasts_with:
  - higher-order-function

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a list comprehension?"
  - "How do I build a list without using map or filter?"
---

# Quick Definition

A list comprehension is an expression that builds a list directly, written `[Expression || Qualifiers]`. It expresses map-and-filter logic without explicitly using funs, `map`, or `filter`.

# Core Definition

"*List comprehensions* are expressions that create lists without having to use funs, maps, or filters. This makes our programs even shorter and easier to understand" (Chapter 4, "List Comprehensions"). "The notation `[ F(X) || X <- L]` means 'the list of `F(X)` where `X` is taken from the list `L`.'" The most general form is `[X || Qualifier1, Qualifier2, ...]` where "`X` is an arbitrary expression, and each qualifier is either a generator, a bitstring generator, or a filter":

- "Generators are written as `Pattern <- ListExpr`" — `ListExpr` must evaluate to a list of terms.
- "Bitstring generators are written as `BitStringPattern <= BitStringExpr`."
- "Filters are either predicates ... or boolean expressions."

The generator pattern also acts as a filter: in `[X || {a, X} <- [{a,1},{b,2},{c,3},{a,4},hello,"wow"]]`, only the elements matching `{a, X}` contribute, producing `[1,4]`.

# Prerequisites

- **List** — A comprehension consumes and produces lists.
- **Pattern matching** — A generator's left side is a pattern matched against each element.

# Key Properties

1. Written `[Expression || Qualifiers]`.
2. It builds a list without explicit funs, `map`, or `filter`.
3. A qualifier is a generator, a bitstring generator, or a filter.
4. A generator `Pattern <- ListExpr` draws values from a list.
5. A filter is a predicate or boolean expression that keeps or drops candidates.
6. A generator pattern also acts as a filter — non-matching elements are skipped.
7. Multiple generators produce all combinations of their values.

# Construction / Recognition

## To Write a List Comprehension:
1. Write `[` then the result expression, then `||`.
2. Add one or more generators `Pattern <- List`.
3. Add filters (boolean expressions) to keep only wanted combinations.
4. Close with `]`.

## To Recognize It:
1. The `[ ... || ... ]` form with the double-bar `||`.

# Context & Application

- **Typical contexts**: Transforming, filtering, and combining lists concisely.
- **Common applications**: `[2*X || X <- L]` doubles a list; `total(L) -> lists:sum([shop:cost(A) * B || {A, B} <- L])` computes a shopping total; `pythag/1` uses three generators and filters.
- **Historical/stylistic notes**: Comprehensions "will make your code really short and easy to read" — e.g., `map(F, L) -> [F(X) || X <- L]`.

# Examples

**Example 1** (Chapter 4, "List Comprehensions"): `[2*X || X <- L]` with `L = [1,2,3,4,5]` produces `[2,4,6,8,10]` — the comprehension form of `lists:map(fun(X) -> 2*X end, L)`.

**Example 2** (Chapter 4, "Pythagorean Triplets"): `pythag(N) -> [ {A,B,C} || A <- lists:seq(1,N), B <- lists:seq(1,N), C <- lists:seq(1,N), A+B+C =< N, A*A+B*B =:= C*C ].` — three generators plus two filters.

# Relationships

## Builds Upon
- **List** — Comprehensions are built over lists.
- **Pattern matching** — Generators match a pattern against each list element.

## Enables
- Concise quicksort, permutations, and the final shopping-`total` definition.

## Related
- **Higher-order function** — Comprehensions and `map`/`filter` solve overlapping problems.
- **Fun** — Comprehensions express map/filter logic without writing an explicit fun.

## Contrasts With
- **Higher-order function** — `map`/`filter` pass an explicit fun; a comprehension inlines the transformation and filtering in `[X || ...]` notation, often more concisely.

# Common Errors

- **Error**: Writing a generator over something that is not a list.
  **Correction**: A generator `Pattern <- ListExpr` requires `ListExpr` to evaluate to a list (use `<=` for bitstrings).

- **Error**: Forgetting that a generator pattern silently filters.
  **Correction**: Elements not matching the generator pattern are skipped; this is intended behavior, e.g. `[X || {a, X} <- Mixed]`.

# Common Confusions

- **Confusion**: Thinking a list comprehension mutates the source list.
  **Clarification**: It builds and returns a *new* list; the source is unchanged.

- **Confusion**: Believing `<-` is an assignment.
  **Clarification**: `<-` is a generator — it draws each value of the pattern from the list, one at a time.

# Source Reference

"Programming Erlang, Second Edition," Chapter 4: Modules and Functions, section "List Comprehensions" (subsections "Quicksort," "Pythagorean Triplets," "Anagrams"). EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations from Chapter 4, "List Comprehensions."
- Confidence rationale: HIGH — the notation and the generator/filter forms are explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
