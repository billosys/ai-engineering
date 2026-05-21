---
concept: Test Organization
slug: test-organization
category: testing
subcategory: unit-testing
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "EUnited Nations Council"
chapter_number: 24
pdf_page: null
section: "Testing Regis"
extraction_confidence: medium
aliases:
  - "test suite organization"
  - "test module structure"
prerequisites:
  - eunit
  - eunit-fixture
extends: []
related:
  - eunit-test-generator
contrasts_with: []
answers_questions:
  - "How should I organize an EUnit test module?"
  - "How do tests serve as documentation?"
  - "How do I test concurrent processes in EUnit?"
---

# Test Organization

## Quick Definition

Test organization is the practice of structuring an EUnit test module into clear sections — test descriptions/fixtures, setup functions, actual tests (instantiators), and helper functions — so the suite is readable and doubles as documentation.

## Core Definition

The book demonstrates organizing the `regis_server_tests` suite into four labeled sections: TESTS DESCRIPTIONS, SETUP FUNCTIONS, ACTUAL TESTS, and HELPER FUNCTIONS (Ch. 24, "Testing Regis"). The top section holds only fixtures and top-level feature descriptions; the second holds setup/cleanup functions; the third holds instantiators returning test sets; the last holds helpers. The book notes "By reading the test generators' definitions, we can know what the module is supposed to be doing. The tests become documentation (although they should not replace proper documentation)."

## Prerequisites

- **Eunit** — Organization applies to EUnit test modules
- **Eunit-fixture** — Fixtures occupy the descriptions section; setup functions form their own section

## Key Properties

1. A test module is divided into four sections: descriptions/fixtures, setup functions, actual tests, helper functions
2. The descriptions section uses described fixtures (`{Comment, Fixture}`) and groups generators by feature
3. Begin TDD by writing a feature list, then turn each feature into a test
4. A `?setup(F)` macro can reduce fixture boilerplate when one setup/teardown pair is reused
5. Tests of concurrent processes often need tiny timers to synchronize code (an acknowledged eyesore)
6. Prefer unique values (e.g. `make_ref()`) over hardcoded names so tests can run in parallel
7. Store time-sensitive state in variables before the test set, since test sets run after the instantiator's active code
8. `sys:get_status/1` inspects a running `gen_server`/`gen_fsm`'s internal state during testing

## Construction / Recognition

### To organize a test suite

1. Write a feature list of everything to cover
2. Lay out four section headers in the module
3. Put feature descriptions and fixtures at the top, grouped by area (e.g. start/stop, register, unregister)
4. Define `start/0` and `stop/1` in the setup section
5. Write instantiators as the actual tests; helpers at the bottom
6. Use `make_ref()` and pre-computed variables for concurrency-safe, timing-correct tests

## Context & Application

The book's `regis` registry was developed test-driven; each feature-list item became a test grouped into `start_stop_test_/0`, `register_test_/0`, and `unregister_test_/0`.

## Examples

**Example** (Ch. 24): The four-section skeleton — comment banners for TESTS DESCRIPTIONS, SETUP FUNCTIONS, ACTUAL TESTS, HELPER FUNCTIONS.

**Example** (Ch. 24): Grouped, described generators —

```erlang
register_test_() ->
    [{"A process can be registered and contacted", ?setup(fun register_contact/1)},
     {"A process cannot have two names", ?setup(fun two_names_one_pid/1)}].
```

## Relationships

### Builds Upon

- **Eunit-fixture** — Fixtures and setup functions are core to the layout

### Related

- **Eunit-test-generator** — Generators grouped by feature form the descriptions section

## Common Errors

- **Error**: Putting time-sensitive function calls directly inside `?_assert*` macros.
  **Correction**: Run the active code first, store results in variables, then assert on the variables — test sets execute after the instantiator's code.
- **Error**: Hardcoding names like `a`, `b`, `c` in tests.
  **Correction**: Use `make_ref()` or other unique-value generators so suites can run in parallel without clashes.

## Common Confusions

- **Confusion**: Thinking tests fully replace documentation.
  **Clarification**: Well-organized tests document behavior but should not replace proper documentation.
- **Confusion**: Believing timers in concurrent tests are sloppy mistakes.
  **Clarification**: They are an acknowledged necessity for synchronizing concurrent, time-sensitive Erlang code.

## Source Reference

Chapter 24, "EUnited Nations Council," sections "Testing Regis" and "He Who Knits EUnits."

## Verification Notes

- Definition: Synthesized from the worked `regis_server_tests` walkthrough
- Key Properties: Items explicit in source; the four-section structure and TDD-from-feature-list are demonstrated
- Confidence: MEDIUM — the concept is a practice synthesized from an extended example rather than a single formal definition
- Cross-references: `eunit`, `eunit-fixture`, `eunit-test-generator` planned this chapter
