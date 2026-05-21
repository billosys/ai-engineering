---
concept: ETS Match Specification
slug: ets-match-specification
category: performance
subcategory: in-memory-storage
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Bears, ETS, Beets: In-Memory NoSQL for Free!"
chapter_number: 25
pdf_page: null
section: "You Have Been Selected"
extraction_confidence: high
aliases:
  - "match specification"
  - "match_spec"
  - "fun2ms"
  - "ets:fun2ms"
prerequisites:
  - ets-table
  - ets-select-and-match
extends: []
related:
  - ets-select-and-match
contrasts_with: []
answers_questions:
  - "What is an ETS match specification?"
  - "How do I write a match specification with fun2ms?"
  - "How do I read a match specification?"
---

# ETS Match Specification

## Quick Definition

A match specification is a data-structure encoding of function-head pattern matching with guards, used by ETS `select` functions. It is most easily produced from a `fun` via the `ets:fun2ms` parse transform.

## Core Definition

A match specification gives ETS "something more equivalent to true function heads−level pattern matching, including very simple guards" (Ch. 25, "You Have Been Selected"). Its high-level form is a list of clauses, each `{InitialPattern, Guards, ReturnedValue}` — roughly the pattern, guards, and body of a function. Patterns use `'$N'` variables; guards use a prefix notation where operators and functions become atoms (`{'<', '$3', 4.0}`, `{is_float, '$3'}`, `{'andalso', X, Y}`). The book teaches reading them but writing them via `ets:fun2ms`, a parse transform that converts a `fun` into a match specification at compile time with no runtime overhead.

## Prerequisites

- **Ets-table** — Match specifications query ETS tables
- **Ets-select-and-match** — Match specifications are consumed by the `select` family of functions

## Key Properties

1. A match specification is a list of clauses `[{Pattern1, Guards1, Return1}, ...]`
2. Each clause maps to a function head, its guards, and its body
3. Patterns use `'$1'`, `'$2'`, ... variables and `'_'` for "don't care"
4. Guards use prefix notation: `{'<', '$3', 4.0}`, `{is_float, '$3'}`, `{'andalso', G1, G2}`, `{'orelse', G1, G2}`
5. The return section lists variables to return; `'$_'` returns the whole matched input
6. `ets:fun2ms(Fun)` converts a fun into a match specification via a parse transform
7. Using `fun2ms` requires `-include_lib("stdlib/include/ms_transform.hrl")` in compiled modules
8. Not every fun is valid: the head must be a single variable or tuple, no nonguard function calls in the body, no bit-syntax binding

## Construction / Recognition

### To produce a match specification

1. Add `-include_lib("stdlib/include/ms_transform.hrl")` to the module
2. Write the query as `ets:fun2ms(fun(Pattern) when Guards -> Return end)`
3. The parse transform replaces the call with the literal match specification at compile time

### To read a match specification

Map each `{Pattern, Guards, Return}` clause to `f(Pattern) when Guards -> Return`, translating prefix operators back to infix.

## Context & Application

Match specifications power `ets:select/2` and related functions. Higher-order pattern matching is not available in Erlang, so match specifications are the agreed-upon sublanguage for it.

## Examples

**Example** (Ch. 25): `fun2ms` in the shell —

```erlang
3> ets:fun2ms(fun({X,Y}) when X < Y -> X+Y end).
[{{'$1','$2'},[{'<','$1','$2'}],[{'+','$1','$2'}]}]
```

**Example** (Ch. 25): Invalid funs are rejected — `ets:fun2ms(fun(X) -> my_own_function(X) end)` errors because a local function call cannot be translated into a match spec.

## Relationships

### Builds Upon

- **Ets-table** — Match specs query ETS tables

### Related

- **Ets-select-and-match** — `select/2`, `select_count/2`, `select_delete/2` consume match specifications

## Common Errors

- **Error**: Forgetting the `ms_transform.hrl` include in a compiled module.
  **Correction**: Without it `fun2ms` fails with a `badarg` error about the fun needing the parse transform.
- **Error**: Passing a compiled fun to `fun2ms` in the shell, or vice versa.
  **Correction**: Shell funs and module funs are not interchangeable; `fun2ms` has separate compiled and shell versions.

## Common Confusions

- **Confusion**: Thinking you must hand-write match specifications.
  **Clarification**: `ets:fun2ms` generates them from readable funs at compile time with no overhead.
- **Confusion**: Believing `fun2ms` runs at runtime as a higher-order function.
  **Clarification**: In compiled modules it is a parse transform applied during compilation.

## Source Reference

Chapter 25, "Bears, ETS, Beets: In-Memory NoSQL for Free!", section "You Have Been Selected." See the official match_spec docs referenced there.

## Verification Notes

- Definition: Direct adaptation from "You Have Been Selected"
- Key Properties: All explicit in source
- Confidence: HIGH — the section explains the format and `fun2ms` in depth
- Cross-references: `ets-table`, `ets-select-and-match` planned this chapter
