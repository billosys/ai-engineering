---
concept: EUnit Test Generator
slug: eunit-test-generator
category: testing
subcategory: unit-testing
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "EUnited Nations Council"
chapter_number: 24
pdf_page: null
section: "Test Generators"
extraction_confidence: high
aliases:
  - "test generator"
  - "_test_ function"
  - "test set"
  - "test representation"
prerequisites:
  - eunit
  - eunit-assertion-macro
extends: []
related:
  - eunit-fixture
contrasts_with: []
answers_questions:
  - "What is an EUnit test generator?"
  - "How do I get per-assertion test granularity in EUnit?"
  - "What is a test set?"
---

# EUnit Test Generator

## Quick Definition

An EUnit test generator is a function ending in `_test_()` that returns a test set — a possibly deeply nested list of `?_assert`-style test funs that EUnit runs individually.

## Core Definition

Test generators are "shorthand for assertions wrapped in functions that can be run later, in clever manners" (Ch. 24, "Test Generators"). Instead of `_test()` functions with `?assertSomething` macros, you write `_test_()` functions with `?_assertSomething` macros. A `_test_()` function is a *test generator function*; a `?_assert(...)` is a *test generator*, because `?_assert(A == B)` is secretly `fun() -> ?assert(A==B) end` — a function that generates a test. Because generators are funs, they can be manipulated without being executed, and grouped into *test sets* (deeply nested lists of generators).

## Prerequisites

- **Eunit** — Generators are an EUnit feature
- **Eunit-assertion-macro** — `?_assert`-style macros are the generator forms of assertions

## Key Properties

1. A *test generator function* ends in `_test_()` (note the trailing underscore)
2. A *test generator* is a `?_assertSomething` macro — a fun producing a test
3. `function_test() -> ?assert(A == B)` and `function_test_() -> ?_assert(A == B)` are equivalent
4. A *test set* is a (possibly deeply nested) list of test generators
5. Functions that are not `_test_()` are not treated as tests but can be called by generator functions to build test sets
6. Each generated assertion counts and reports as a separate test, so one failure does not mask the rest
7. EUnit can run a single generator via the `{generator, Fun}` test representation

## Construction / Recognition

### To build test generators

1. Write a `_test_()` function
2. Return a list of `?_assert*` test generators (or call helper functions that return test sets)
3. Helper functions need not end in `_test_()`; only the top-level generator function does
4. Run all with `eunit:test(Mod)` or one with `eunit:test({generator, fun Mod:gen_test_/0})`

## Context & Application

Test generators solve the problem that a plain `_test()` function fails entirely on the first failed assertion. With generators each assertion reports independently.

## Examples

**Example** (Ch. 24): A generator that delegates to helper functions —

```erlang
add_test_() ->
    [test_them_types(),
     test_them_values(),
     ?_assertError(badarith, 1/0)].

test_them_values() ->
    [?_assertEqual(4, ops:add(2,2)),
     ?_assertEqual(3, ops:add(1,2)),
     ?_assertEqual(3, ops:add(1,1))].
```

**Example** (Ch. 24): A nested test set — `[?_assert(A), [?_assert(B), ?_assert(C), [?_assert(D)]], [[?_assert(E)]]]`.

## Relationships

### Builds Upon

- **Eunit** — Generators extend EUnit's basic test running
- **Eunit-assertion-macro** — `?_assert*` macros are the generator forms

### Related

- **Eunit-fixture** — Fixtures wrap generators with setup/teardown; instantiators return test sets

## Common Errors

- **Error**: Writing a generator function ending in `_test()` instead of `_test_()`.
  **Correction**: Only `_test_()` functions are treated as test generators.
- **Error**: Expecting a non-`_test_()` helper to be auto-run.
  **Correction**: Helpers are only run when called by a generator function to build a test set.

## Common Confusions

- **Confusion**: Thinking `?_assert` runs the assertion immediately.
  **Clarification**: It produces a fun; EUnit runs it later.
- **Confusion**: Believing a test set must be a flat list.
  **Clarification**: Test sets can be deeply nested lists of generators.

## Source Reference

Chapter 24, "EUnited Nations Council," section "Test Generators."

## Verification Notes

- Definition: Direct adaptation from "Test Generators"
- Key Properties: All explicit in source
- Confidence: HIGH — the section defines generators, generator functions, and test sets precisely
- Cross-references: `eunit`, `eunit-assertion-macro`, `eunit-fixture` planned this chapter
