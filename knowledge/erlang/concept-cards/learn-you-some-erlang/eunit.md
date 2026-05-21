---
concept: EUnit
slug: eunit
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
  - "EUnit"
  - "eunit"
  - "EUnit framework"
prerequisites:
  - module
extends: []
related:
  - eunit-assertion-macro
  - eunit-test-generator
  - eunit-fixture
  - test-organization
contrasts_with:
  - common-test
answers_questions:
  - "What is EUnit?"
  - "How do I write EUnit tests?"
  - "How do I run EUnit tests?"
  - "What distinguishes EUnit from Common Test?"
---

# EUnit

## Quick Definition

EUnit is Erlang's lightweight unit-testing framework. In its simplest form it automatically runs functions ending in `_test()` in a module, treating them as unit tests.

## Core Definition

"EUnit, in its simplest form, is just a way to automate running functions that end in `_test()` in a module by assuming they are unit tests" (Ch. 24, "EUnit—What's an EUnit?"). Tests are run by calling `eunit:test(Module)`. EUnit does more than auto-running `_test()` functions: tests can be moved into a separate `Mod_tests` module (so code and tests are not mixed), it provides assertion macros for clear failure reporting, test generators for finer-grained control, and fixtures for setup/teardown scaffolding. The book recommends EUnit for unit tests and Common Test for larger integration and system tests.

## Prerequisites

- **Module** — Tests are functions inside a module; the framework includes `eunit/include/eunit.hrl`

## Key Properties

1. Functions ending in `_test()` are automatically treated as tests
2. `eunit:test(Module)` runs the tests; `eunit:test(Mod)` also looks for and runs `Mod_tests`
3. Tests can live in a separate `Mod_tests` module, which means private functions cannot be tested but tests survive refactoring
4. The module must `-include_lib("eunit/include/eunit.hrl")` to use macros
5. A failing assertion fails the whole `_test()` function unless test generators are used
6. The `verbose` option adds test descriptions and runtime info to reports
7. EUnit supports test representations: `{module, Mod}`, `{dir, Path}`, `{file, Path}`, `{generator, Fun}`, `{application, AppName}`

## Construction / Recognition

### To write and run EUnit tests

1. Create a `Mod_tests` module and `-include_lib("eunit/include/eunit.hrl")`
2. Write functions ending in `_test()` (or `_test_()` for generators)
3. Use assertion macros inside them
4. Run with `eunit:test(Mod)` or `eunit:test(Mod, [verbose])`

## Context & Application

EUnit is for unit tests; Common Test handles integration up to system tests and even non-Erlang software (covered later in the book). EUnit is favored for its simplicity and good results.

## Examples

**Example** (Ch. 24): Running the RPN calculator's test —

```erlang
2> eunit:test(calc).
  Test passed.
ok
```

**Example** (Ch. 24): Separated code and tests — module `ops` with `add/2`, and module `ops_tests` with `add_test() -> 4 = ops:add(2,2).`; `eunit:test(ops)` finds and runs `ops_tests`.

## Relationships

### Enables

- **Eunit-assertion-macro** — Macros that produce clear failure reports
- **Eunit-test-generator** — Functions returning runnable test sets
- **Eunit-fixture** — Setup/teardown scaffolding

### Related

- **Test-organization** — How a test module's sections are structured

### Contrasts With

- **Common-test** — Heavier framework for integration and system tests

## Common Errors

- **Error**: Forgetting `-include_lib("eunit/include/eunit.hrl")`.
  **Correction**: Without it the assertion and generator macros are undefined.
- **Error**: Putting tests in the same module and then trying to keep testing private functions after refactoring.
  **Correction**: Separate-module tests can only see exported functions, which is the point — test the interface.

## Common Confusions

- **Confusion**: Thinking EUnit only runs `_test()` functions.
  **Clarification**: It also supports generators, fixtures, descriptions, and multiple test representations.
- **Confusion**: Believing EUnit covers system and integration testing fully.
  **Clarification**: Common Test is the tool for larger integration/system tests.

## Source Reference

Chapter 24, "EUnited Nations Council," section "EUnit—What's an EUnit?" and "Test Generators."

## Verification Notes

- Definition: Direct adaptation from "EUnit—What's an EUnit?"
- Key Properties: All explicit in source
- Confidence: HIGH — the chapter is dedicated to EUnit
- Cross-references: `eunit-assertion-macro`, `eunit-test-generator`, `eunit-fixture`, `test-organization` planned this chapter; `common-test` referenced as a future concept
