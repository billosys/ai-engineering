---
# === CORE IDENTIFICATION ===
concept: List Comprehension
slug: list-comprehension

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: comprehensions
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Comprehensions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "list comprehension expression"
  - "LC"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
  - guard-sequences
extends: []
related:
  - binary-comprehension
  - map-comprehension
  - list
contrasts_with:
  - binary-comprehension
  - map-comprehension

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use list comprehensions in Erlang?"
  - "What are generators and filters in a list comprehension?"
  - "What is the difference between relaxed and strict generators?"
  - "What are zip generators in Erlang?"
  - "How do I filter elements in a list comprehension?"
---

# Quick Definition

A list comprehension `[Expr || Qualifier1, ..., QualifierN]` constructs a list by evaluating `Expr` for each combination of generator elements for which all filters are true.

# Core Definition

List comprehensions have the syntax `[Expr || Qualifier1, ..., QualifierN]` where `Expr` is an arbitrary expression and each `Qualifier` is either a generator or a filter. A list generator `Pattern <- ListExpr` (relaxed) or `Pattern <:- ListExpr` (strict, OTP 28+) iterates over the elements of a list. A filter is an expression evaluating to `true` or `false`. The comprehension returns a list of results from evaluating `Expr` for each combination of generator bindings where all filters are true. Variables in generator patterns shadow previously bound variables. With relaxed generators (`<-`), non-matching elements are silently skipped; with strict generators (`<:-`), a non-matching element raises an error. Zip generators (`Gen1 && Gen2`) iterate generators in parallel (OTP 28+). When there are no generators, the comprehension returns `[Expr]` if all filters are true, or `[]` otherwise (Erlang Reference Manual, "Comprehensions" section).

# Prerequisites

- **pattern-matching** — Generators use patterns to match and bind values.
- **guard-sequences** — Guard expressions used as filters have special behavior (failure = false).

# Key Properties

1. Syntax: `[Expr || Qualifier1, ..., QualifierN]`.
2. Generators: list (`<-` / `<:-`), bit string (`<=` / `<:=`), map (`K := V <-` / `K := V <:-`).
3. Filters: expressions evaluating to `true` or `false`.
4. Relaxed generators (`<-`) silently skip non-matching elements.
5. Strict generators (`<:-`, OTP 28+) raise an error on non-matching elements.
6. Zip generators (`&&`, OTP 28+) iterate multiple generators in parallel.
7. Variables in generator patterns shadow outer variables.
8. Variables bound in generator expressions are not visible outside the expression.
9. Guard expression filters treat evaluation failure as `false`; non-guard filters raise exceptions on non-boolean results.

# Construction / Recognition

## To Construct:
```erlang
[Expr || Pattern <- List]
[Expr || Pattern <:- List, Filter]
[Expr || P1 <:- List1 && P2 <:- List2]
```

## To Recognize:
1. Look for `[ ... || ... ]` syntax.
2. Contains generators (with `<-`, `<:-`, `<=`, `<:=`) and/or filters after `||`.

# Context & Application

List comprehensions are a concise and declarative way to construct lists by transformation and filtering. They replace explicit recursive functions for many common patterns (mapping, filtering, combining). Strict generators (OTP 28+) are recommended as better practice when either strict or relaxed would work, because they catch unexpected data shapes.

# Examples

**Example 1** (Comprehensions section): Doubling each element:

```erlang
1> [X*2 || X <:- [1,2,3]].
[2,4,6]
```

**Example 2** (Comprehensions section): Filtering odd numbers:

```erlang
1> [X || X <:- [1,2,3,4,5], X rem 2 =:= 1].
[1,3,5]
```

**Example 3** (Comprehensions section): Relaxed generator silently skipping non-matching:

```erlang
1> [X || {_,_}=X <- [{a,b}, [a], {x,y,z}, {1,2}]].
[{a,b},{1,2}]
```

**Example 4** (Comprehensions section): Strict generator raising on non-match:

```erlang
1> [X || {_,_}=X <:- [{a,b}, [a], {x,y,z}, {1,2}]].
** exception error: no match of right hand side value [a]
```

**Example 5** (Comprehensions section): Cartesian product with multiple generators:

```erlang
1> [{P,Q} || P <:- [a,b,c], Q <:- [1,2]].
[{a,1},{a,2},{b,1},{b,2},{c,1},{c,2}]
```

**Example 6** (Comprehensions section): Zip generator for parallel iteration:

```erlang
1> [{P,Q} || P <:- [a,b,c] && Q <:- [1,2,3]].
[{a,1},{b,2},{c,3}]
```

# Relationships

## Builds Upon
- **pattern-matching** — Generators use patterns for destructuring.
- **guard-sequences** — Guard expression filters silently fail to false.

## Enables
- Declarative list construction and transformation.

## Related
- **binary-comprehension** — Same syntax pattern but constructs bit strings.
- **map-comprehension** — Same syntax pattern but constructs maps.
- **list** — List comprehensions produce lists.

## Contrasts With
- **binary-comprehension** — Uses `<< ... || ... >>` instead of `[ ... || ... ]`.
- **map-comprehension** — Uses `#{ ... || ... }` instead of `[ ... || ... ]`.

# Common Errors

- **Error**: Using a non-guard function call as a filter and getting `{bad_filter, Val}`.
  **Correction**: Ensure filter expressions return boolean values. Non-guard expression filters that return non-boolean values raise `{bad_filter, Val}`.

- **Error**: Using a relaxed generator when data should always match, hiding bugs.
  **Correction**: Use strict generators (`<:-`) when elements should always match the pattern. Strict generators raise errors on mismatches, catching bugs early.

# Common Confusions

- **Confusion**: Thinking generator variables are accessible after the comprehension.
  **Clarification**: Variables bound in generators shadow outer variables and the shadowed bindings are not visible outside the comprehension.

- **Confusion**: Expecting a guard-expression filter and a non-guard filter to behave the same on failure.
  **Clarification**: Guard expression filters treat failure as `false` (element skipped). Non-guard expression filters that fail to evaluate raise the exception.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Comprehensions" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — comprehensive syntax, generator types, and examples from source
- Uncertainties: None
- Cross-reference status: Verified against binary-comprehension and map-comprehension sections
