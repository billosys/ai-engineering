---
concept: EUnit Fixture
slug: eunit-fixture
category: testing
subcategory: unit-testing
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "EUnited Nations Council"
chapter_number: 24
pdf_page: null
section: "Fixtures"
extraction_confidence: high
aliases:
  - "fixture"
  - "setup fixture"
  - "foreach fixture"
  - "instantiator"
prerequisites:
  - eunit
  - eunit-test-generator
extends: []
related:
  - test-organization
contrasts_with: []
answers_questions:
  - "What is an EUnit fixture?"
  - "How do I set up and tear down state around EUnit tests?"
  - "What is the difference between a setup and a foreach fixture?"
---

# EUnit Fixture

## Quick Definition

An EUnit fixture is scaffolding that defines setup and teardown functions around tests, building the state and environment each test needs. The two main types are the setup fixture and the foreach fixture.

## Core Definition

Fixtures "allow you to build a certain scaffolding around tests... a general structure that allows you to define setup and teardown functions for each of the tests" (Ch. 24, "Fixtures"). The scaffolding also specifies how to run the tests (locally, in spawned processes, etc.). Fixtures rely on four roles: a *setup* function (no arguments, returns state passed to tests), a *cleanup* function (takes the setup result, undoes it), an *instantiator* (takes the setup result, returns a test set), and *Where* (specifies how to run tests: `local`, `spawn`, `{spawn, node()}`).

## Prerequisites

- **Eunit** — Fixtures are an EUnit feature
- **Eunit-test-generator** — Instantiators return test sets, which are made of test generators

## Key Properties

1. Setup fixture forms: `{setup, Setup, Instantiator}` and variants with `Cleanup` and/or `Where`
2. `Setup` takes no arguments and returns a value passed to each test; called once per instantiator
3. `Cleanup` takes the setup result and undoes it; called once per setup call (the opposite of setup)
4. `Instantiator` takes the setup result and returns a test set
5. Foreach fixture forms: `{foreach, [Where,] Setup, [Cleanup,] [Instantiator]}` — takes a *list* of instantiators, running setup/teardown for each
6. A whole fixture can itself be placed inside a test set
7. A fixture can be wrapped with a description: `{Comment, Fixture}`
8. More test-control options apply inside fixtures: `{spawn, TestSet}`, `{timeout, Seconds, TestSet}`, `{inorder, TestSet}`, `{inparallel, Tests}`

## Construction / Recognition

### To write a setup fixture

1. Write `start/0` (setup) returning needed state, and `stop/1` (cleanup)
2. Write an instantiator that takes the setup result and returns a test set
3. Return `{setup, fun start/0, fun stop/1, fun instantiator/1}` from a `_test_()` function

### To avoid repeating setup/teardown

Use a `foreach` fixture with a list of instantiators sharing one `start`/`stop` pair.

## Context & Application

Fixtures scale EUnit toward application-level testing. The book's `regis_server_tests` defines a `?setup(F)` macro expanding to `{setup, fun start/0, fun stop/1, F}` to reduce boilerplate.

## Examples

**Example** (Ch. 24): A described setup fixture —

```erlang
double_register_test_() ->
    {"Verifies that the registry doesn't allow a single process to "
     "be registered under two names",
     {setup, fun start/0, fun stop/1, fun two_names_one_pid/1}}.
```

**Example** (Ch. 24): The `foreach` form sharing `start`/`stop` across many instantiators —

```erlang
some2_test_() ->
    {foreach, fun start/0, fun stop/1,
     [fun some_instantiator1/1, fun some_instantiator2/1]}.
```

## Relationships

### Builds Upon

- **Eunit** — Fixtures are part of EUnit
- **Eunit-test-generator** — Instantiators return test sets of generators

### Related

- **Test-organization** — Fixtures shape how a test module is structured

## Common Errors

- **Error**: Using a `setup` fixture and repeating the same setup/teardown for many instantiators.
  **Correction**: Use a `foreach` fixture, which takes a list of instantiators with one setup/cleanup pair.
- **Error**: Writing a setup function that takes arguments.
  **Correction**: Setup functions take no arguments; their return value is passed to tests.

## Common Confusions

- **Confusion**: Thinking `setup` and `foreach` differ only in syntax.
  **Clarification**: `setup` takes one instantiator; `foreach` takes a list, running setup/teardown for each.
- **Confusion**: Believing one setup call serves many instantiators in a `foreach`.
  **Clarification**: `foreach` runs setup/teardown per instantiator; to share one setup across many, nest instantiators inside a single instantiator fun.

## Source Reference

Chapter 24, "EUnited Nations Council," section "Fixtures" (including "More Test Control" and "Test Documentation").

## Verification Notes

- Definition: Direct adaptation from "Fixtures"
- Key Properties: All explicit in source
- Confidence: HIGH — the section defines fixture vocabulary and forms precisely
- Cross-references: `eunit`, `eunit-test-generator`, `test-organization` planned this chapter
