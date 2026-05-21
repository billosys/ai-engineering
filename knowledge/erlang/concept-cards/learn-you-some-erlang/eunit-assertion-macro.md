---
concept: EUnit Assertion Macro
slug: eunit-assertion-macro
category: testing
subcategory: unit-testing
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "EUnited Nations Council"
chapter_number: 24
pdf_page: null
section: "EUnit—What's an EUnit?"
extraction_confidence: high
aliases:
  - "assertion macro"
  - "?assert"
  - "?assertEqual"
  - "?assertMatch"
  - "?assertError"
prerequisites:
  - eunit
extends: []
related:
  - eunit-test-generator
contrasts_with: []
answers_questions:
  - "What are EUnit assertion macros?"
  - "How do I get clear failure reports from EUnit tests?"
  - "Which EUnit macro should I use to test for exceptions?"
---

# EUnit Assertion Macro

## Quick Definition

EUnit assertion macros (`?assert`, `?assertEqual`, `?assertMatch`, `?assertError`, etc.) are macros that test conditions and produce clear failure reports including line numbers and expected/actual values.

## Core Definition

EUnit introduces assertion macros because a plain pattern match like `4 = ops:add(2,2)` gives crash-style output with no clear explanation. The macros "give us cleaner reporting (including line numbers) and clearer semantics... the difference between knowing that something goes wrong and knowing why something goes wrong" (Ch. 24, "EUnit—What's an EUnit?"). Each macro corresponds to a kind of check, from boolean truth to pattern matching to exception expectations.

## Prerequisites

- **Eunit** — Macros require `-include_lib("eunit/include/eunit.hrl")` and run inside EUnit tests

## Key Properties

1. `?assert(Expression)` / `?assertNot(Expression)` — test boolean values; roughly `true = X` / `false = Y`
2. `?assertEqual(A, B)` — strict `=:=` comparison; `?assertNotEqual` is the inverse
3. `?assertMatch(Pattern, Expression)` — matches `Pattern` against `Expression` without ever binding variables; `?assertNotMatch` is the inverse
4. `?assertError(Pattern, Expression)` — asserts `Expression` raises an error (e.g. `?assertError(badarith, 1/0)`)
5. `?assertThrow(Pattern, Expression)` — asserts a `throw`
6. `?assertExit(Pattern, Expression)` — asserts an `exit` (not `exit/2`)
7. `?assertException(Class, Pattern, Expression)` — general form covering error/throw/exit
8. Failure reports include module, line, expression text, expected and actual values

## Construction / Recognition

### To choose an assertion macro

1. Boolean condition → `?assert` / `?assertNot`
2. Exact value equality → `?assertEqual`
3. Structural match without binding → `?assertMatch`
4. Expected exception → `?assertError` / `?assertThrow` / `?assertExit` / `?assertException`

## Context & Application

Macros are used inside `_test()` functions; their generator counterparts (`?_assert`, etc.) are used inside `_test_()` test generators.

## Examples

**Example** (Ch. 24): A test using several macros —

```erlang
new_add_test() ->
    ?assertEqual(4, ops:add(2,2)),
    ?assert(is_number(ops:add(1,2))),
    ?assertError(badarith, 1/0).
```

**Example** (Ch. 24): A failed `?assertEqual` reports `{assertEqual_failed, [{module, ops_tests}, {line, 11}, {expression, "ops : add ( 1 , 1 )"}, {expected, 3}, {value, 2}]}`.

## Relationships

### Builds Upon

- **Eunit** — Macros are part of the EUnit framework

### Related

- **Eunit-test-generator** — Provides `?_assert`-style macros that wrap assertions in funs

## Common Errors

- **Error**: Expecting `?assertMatch` to bind pattern variables for later use.
  **Correction**: Variables in the pattern head never bind across assertions.
- **Error**: Using a plain `=` match instead of a macro and getting opaque crash output.
  **Correction**: Use assertion macros for line numbers and expected/actual reporting.

## Common Confusions

- **Confusion**: Thinking `?assertExit` covers `exit/2`.
  **Clarification**: It asserts `exit(Pattern)`, not the two-argument `exit/2`.
- **Confusion**: Believing one failed assertion in a `_test()` function is isolated.
  **Clarification**: In a plain `_test()`, a failed assertion fails the whole function; test generators give per-assertion granularity.

## Source Reference

Chapter 24, "EUnited Nations Council," section "EUnit—What's an EUnit?" (assertion macro list).

## Verification Notes

- Definition: Direct adaptation from the assertion macro discussion
- Key Properties: All macros explicit in source
- Confidence: HIGH — the chapter enumerates every macro with semantics
- Cross-references: `eunit`, `eunit-test-generator` planned this chapter
