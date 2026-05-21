---
# === CORE IDENTIFICATION ===
concept: Erlang Type Notation
slug: erlang-type-notation

# === CLASSIFICATION ===
category: data-types
subcategory: typespecs
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Types"
chapter_number: 9
pdf_page: null
section: "Erlang Type Notation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "type grammar"
  - "type syntax"
  - "type notation"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - type-declaration
  - type-specification
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Erlang type notation?"
  - "How are types written in Erlang?"
  - "What do I need to know before using the type system and Dialyzer?"
---

# Quick Definition

The Erlang type notation is the grammar used to write type expressions — unions, tuples, lists, ranges, and predefined types. It is the vocabulary in which both `-type` declarations and `-spec` function specifications are written.

# Core Definition

Types are defined informally with the syntax `T1 :: A | B | C ...`, meaning `T1` is one of `A`, `B`, or `C`. A subset of Erlang types is given as: `Type :: any() | none() | pid() | port() | reference() | [] | Atom | binary() | float() | Fun | Integer | [Type] | Tuple | Union | UserDefined` (Armstrong, "Types," "The Grammar of Types"). `any()` means any Erlang term; `X()` means an object of type `X`; `none()` denotes the type of a function that never returns. `[X]` denotes a list of type `X`; `{T1, ..., Tn}` denotes a tuple of size `n`; `Min..Max` denotes an integer range; `fun((...) -> Type)` denotes a function type.

# Prerequisites

This is a foundational concept with no prerequisites within this source — the notation is introduced before type declarations and specs depend on it.

# Key Properties

1. `::` reads as "is defined to be"; `|` separates alternatives in a union.
2. `any()` is the universal type; `none()` is the type of a function that never returns.
3. `[X]` is a list of `X`; `[X,...]` is a non-empty list of `X`.
4. `{T1, ..., Tn}` is a fixed-size tuple type; `tuple()` is any tuple.
5. Integer ranges are written `Min..Max` (e.g. `0..255`).
6. Function types are written `fun((ArgTypes) -> RetType)`; `fun()` is any function.
7. Predefined aliases (`boolean()`, `byte()`, `char()`, `number()`, `string()`, `iolist()`, `mfa()`, `node()`, `timeout()`, `no_return()`) are part of the notation.

# Construction / Recognition

## To Construct/Create:
1. For a fixed value set, list alternatives joined by `|` (a union).
2. For structured data, use `{...}` for tuples and `[X]` for lists.
3. For bounded integers, use `Min..Max`.
4. Compose these to describe arbitrary data shapes.

## To Identify/Recognize:
1. The `::` operator and `|` alternation mark a type expression.
2. Parentheses after a name (`integer()`, `point()`) indicate a type reference, not a value.

# Context & Application

- **Typical contexts**: Inside `-type` and `-spec` attributes; the standard library documentation uses it to describe every public function.
- **Common applications**: Describing data shapes precisely enough for Dialyzer to find inconsistencies.
- **Historical/stylistic notes**: The notation supports type variables, so generic container types can be expressed.

# Examples

**Example 1** ("The Grammar of Types"): `Integer :: integer() | Min .. Max` — the integer type is either the general `integer()` or a bounded range.

**Example 2** ("The Grammar of Types"): `Tuple :: tuple() | {T1, T2, ... Tn}` — a tuple type is either any tuple or a fixed-arity tuple of specified element types.

**Example 3** ("Predefined Types"): `-type boolean() :: true | false.` and `-type byte() :: 0..255.` — predefined aliases written in the same notation.

# Relationships

## Builds Upon
- This is foundational; it builds on no other typed concept in this source.

## Enables
- **Type declaration** — `-type` bodies are written in this notation.
- **Type specification** — `-spec` argument and return types are written in this notation.

## Related
- **Dialyzer** — Dialyzer consumes types written in this notation (and infers types in it).

## Contrasts With
- None.

# Common Errors

- **Error**: Writing `[X, Y]` to mean "a list of X or Y" — that is actually a 2-element list type.
  **Correction**: Use `[X | Y]` for a list whose elements are of either type.

- **Error**: Confusing `{T1, T2}` (a 2-tuple type) with a union.
  **Correction**: Use `|` for unions; braces always denote tuple structure.

# Common Confusions

- **Confusion**: Thinking `any()` and `none()` are the same kind of "wildcard."
  **Clarification**: `any()` is every term; `none()` is the empty type — the type of functions that never return.

- **Confusion**: Believing `[X]` means exactly one element.
  **Clarification**: `[X]` is a list of zero or more elements of type `X`; `[X,...]` is one or more.

# Source Reference

Chapter 9: "Types," section "Erlang Type Notation" (subsections "The Grammar of Types" and "Predefined Types"). EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the type grammar listing from "The Grammar of Types."
- Confidence rationale: HIGH — the source gives the grammar explicitly.
- Uncertainties: None.
- Cross-reference status: Verified slugs against planned chapter-9 cards.
- Re-extraction notes: Fresh extraction; prior card for this slug overwritten.
