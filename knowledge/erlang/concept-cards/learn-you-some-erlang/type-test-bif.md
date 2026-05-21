---
concept: Type-Test BIF
slug: type-test-bif
category: data-types
subcategory: type-system
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Types (or Lack Thereof)"
chapter_number: 4
pdf_page: null
section: "To Guard a Data Type"
extraction_confidence: high
aliases:
  - "type-test function"
  - "is_integer"
  - "is_atom"
  - "type-checking guard function"
prerequisites:
  - guard
  - dynamic-typing
extends:
  - guard
related:
  - type-conversion
contrasts_with: []
answers_questions:
  - "What is a guard?"
---

# Type-Test BIF

## Quick Definition

Type-test BIFs are functions like `is_integer/1` and `is_atom/1` that take one argument and return `true` if it is of the given type. They are among the few functions allowed in guards.

## Core Definition

Type-test BIFs are functions dedicated to guarding data types. Each takes a single argument and returns `true` if the type is correct, `false` otherwise. They are part of the few functions allowed in guard expressions. The Erlang type-test BIFs include `is_atom/1`, `is_binary/1`, `is_bitstring/1`, `is_boolean/1`, `is_float/1`, `is_function/1`, `is_function/2`, `is_integer/1`, `is_list/1`, `is_number/1`, `is_pid/1`, `is_port/1`, `is_record/2`, `is_record/3`, `is_reference/1`, and `is_tuple/1`. There is deliberately no general `type_of(X)` function, because that would encourage conditional branching on type rather than Erlang's preferred declarative branching through function heads (Hébert, ch. 4, "To Guard a Data Type").

## Prerequisites

- **Guard** — Type-test BIFs are used inside guards
- **Dynamic typing** — Type tests check a term's runtime type

## Key Properties

1. Each takes one argument and returns `true` or `false`.
2. Allowed inside guard expressions (unlike user functions).
3. Cover atoms, binaries, bitstrings, booleans, floats, functions, integers, lists, numbers, pids, ports, records, references, and tuples.
4. Type-test BIFs make up more than half the functions allowed in guards.
5. Erlang intentionally has no `type_of/1` function.

## Construction / Recognition

To restrict a function clause to one type:

1. Add a guard `when is_TYPE(Arg)` to the clause head.
2. Provide separate clauses for each type you handle.

## Context & Application

Type-test BIFs let guards enforce that arguments are of a specific type — something plain pattern matching cannot do for primitives. The declarative style (`my_function(Exp) when is_binary(Exp) -> ...`) is favored over a `case type_of(Exp) of ...` branch.

## Examples

**Example** (ch. 4): `my_function(Exp) when is_binary(Exp) -> Expression1; my_function(Exp) when is_list(Exp) -> Expression2.`

## Relationships

### Prerequisites

- **Guard** — Type-test BIFs run inside guards
- **Dynamic typing** — They inspect runtime types

### Builds Upon

- **Guard** — Type-test BIFs are guard-allowed functions

### Related

- **Type conversion** — Conversion BIFs change a type; type-test BIFs check it

## Common Errors

- **Error**: Looking for a `type_of/1` function
  **Correction**: There is none by design; branch on type with `is_TYPE` guards in function heads

## Common Confusions

- **Confusion**: Thinking any function can be used in a guard
  **Clarification**: Only certain BIFs, including the type-test BIFs, are permitted in guards

## Source Reference

Chapter 4: "Types (or Lack Thereof)," section "To Guard a Data Type."

## Verification Notes

- Definition: Adapted from the "To Guard a Data Type" section and BIF table
- Confidence: HIGH — explicit section
- Uncertainties: None
