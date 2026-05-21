---
concept: Boolean and Comparison Operators
slug: boolean-and-comparison-operators
category: core-idioms
subcategory: operators
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Starting Out"
chapter_number: 1
pdf_page: null
section: "Boolean Algebra and Comparison Operators"
extraction_confidence: high
aliases:
  - "Boolean algebra"
  - "equality operators"
  - "andalso"
  - "orelse"
prerequisites:
  - atom
  - number-erlang
extends: []
related:
  - guard
  - variable
contrasts_with: []
answers_questions:
  - "What are the basic data types in Erlang?"
---

# Boolean and Comparison Operators

## Quick Definition

Erlang provides Boolean operators (`and`, `or`, `xor`, `not`, plus short-circuit `andalso`/`orelse`) and comparison operators for equality and ordering. `true` and `false` are atoms, not a special type.

## Core Definition

Boolean algebra in Erlang uses `and`, `or`, `xor`, and `not`. The operators `and` and `or` always evaluate both sides; the short-circuit operators `andalso` and `orelse` evaluate the right side only if necessary. Equality is tested with `=:=` (exact equal) and `=/=` (exact not-equal), and with `==` / `/=` for non-exact equality that ignores the integer/float distinction. Ordering uses `<`, `>`, `>=`, and `=<` (note the backward last one). Any two terms can be compared because Erlang defines a total ordering: `number < atom < reference < fun < port < pid < tuple < list < bit string` (Hébert, ch. 1, "Boolean Algebra and Comparison Operators").

## Prerequisites

- **Atom** — `true` and `false` are atoms, so Boolean values are atoms
- **Numbers in Erlang** — Comparison operators behave differently on integers vs. floats

## Key Properties

1. Boolean operators: `and`, `or`, `xor`, `not`.
2. `andalso` and `orelse` are short-circuit variants.
3. `=:=` / `=/=` test exact equality (distinguishing `5` from `5.0`).
4. `==` / `/=` test non-exact equality (treating `5` and `5.0` as equal).
5. Ordering operators are `<`, `>`, `>=`, and `=<` (less than or equal is written backward).
6. Any term can be compared with any other due to the total ordering of types.
7. Erlang refuses to *add* operands of different types but will *compare* them.

## Construction / Recognition

To choose an equality operator:

1. Start with `=:=` / `=/=` for exact equality by default.
2. Switch to `==` / `/=` only when you knowingly do not need the integer/float distinction.

## Context & Application

The total ordering of types makes it possible to write general sorting algorithms that order any terms. The book recommends defaulting to exact equality to avoid surprises from unexpected number types.

## Examples

**Example** (ch. 1): `5 =:= 5.0.` returns `false`; `5 == 5.0.` returns `true`.

**Example** (ch. 1): `5 =:= true.` returns `false` (comparison across types is allowed), while `5 + llama.` raises a `badarith` error (addition across types is not).

## Relationships

### Prerequisites

- **Atom** — Boolean values `true`/`false` are atoms
- **Numbers in Erlang** — Equality operators treat integers and floats differently

### Related

- **Guard** — Comparison operators are the core of guard expressions
- **Variable** — `=` is a match operator distinct from these comparison operators

## Common Errors

- **Error**: Writing `<=` for "less than or equal to"
  **Correction**: Erlang spells it `=<` (backward)

## Common Confusions

- **Confusion**: Expecting `0 == false` to be `true`, as in C-like languages
  **Clarification**: `false` is an atom, not `0`; `0 == false` is `false`

## Source Reference

Chapter 1: "Starting Out," section "Boolean Algebra and Comparison Operators."

## Verification Notes

- Definition: Adapted from the section, including the type-ordering note quoting Joe Armstrong
- Confidence: HIGH — explicit section with examples
- Uncertainties: None
