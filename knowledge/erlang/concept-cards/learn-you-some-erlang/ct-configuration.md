---
concept: Common Test Configuration
slug: ct-configuration
category: testing
subcategory: common-test
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Common Test for Uncommon Tests"
chapter_number: 28
pdf_page: null
section: "Testing with State"
extraction_confidence: high
aliases:
  - "Config proplist"
  - "test specification"
  - ".spec file"
prerequisites:
  - common-test
  - ct-test-case
related:
  - ct-test-suite
  - ct-data-directory
  - large-scale-testing
contrasts_with: []
answers_questions:
  - "How does Common Test pass state to test cases?"
  - "What is a Common Test test specification?"
---

# Common Test Configuration

## Quick Definition

Common Test configuration covers the `Config` proplist that carries per-test state through setup, cases, and teardown, and the test specification (`.spec`) files that declare how and where suites are run.

## Core Definition

Common Test threads test state through a `Config` proplist. It is supplied to `init_per_suite/1`, `init_per_group/2`, `init_per_testcase/2`, the test case itself, and the matching teardown functions; setup functions may add key/value pairs to it. Initially `Config` contains `data_dir` and `priv_dir`. Reading is done with the `?config(Key, List)` macro (a documented wrapper over `proplists:get_value/2`). Separately, *test specifications* are `.spec` files containing Erlang tuples (consult-file style) that declare aliases, log directories, which suites/groups/cases to run, and what to skip — letting tests be configured once rather than re-specified on every run (Chapter 28, "Testing with State" and "Test Specifications").

## Prerequisites

- **Common Test** — Configuration is part of the Common Test framework
- **CT test case** — `Config` is the argument every case receives

## Key Properties

1. `Config` is a proplist; it always starts with `data_dir` and `priv_dir`
2. `init_per_*` functions may add entries to `Config`; entries flow to the matching case and teardown
3. `init_per_testcase/2`/`end_per_testcase/2` run in the same process as the case; they are called for all cases in the module unless filtered by argument
4. The `?config(Key, List)` macro reads values safely; `ct:pal/1-2` logs to both shell and HTML
5. A test specification `.spec` file holds tuples such as `{alias, A, Dir}`, `{logdir, Dir}`, `{suites, Dir, Suites}`, `{skip_cases, Dir, Suite, Cases, Comment}`, `{groups, ...}`, `{cases, ...}`
6. Tests in `all/0` (and a spec's entries) run in declared order by default
7. Spec files work identically from the command line (`ct_run -spec`) and the shell (`ct:run_test([{spec, ...}])`)

## Construction / Recognition

## To Use Configuration

1. In `init_per_testcase/2`, return `[{key, Value} | Config]` to add state
2. In the case, read it with `?config(key, Config)`
3. To configure runs, write a `.spec` file with `{alias, ...}`, `{logdir, ...}`, `{suites, ...}` tuples
4. Run with `ct_run -spec spec.spec` or `ct:run_test([{spec, "spec.spec"}])`

## Context & Application

The `Config` proplist is Common Test's fixture mechanism, analogous to EUnit's setup/teardown fixtures. Test specifications keep log files tidy (via `logdir`), run many suites at once, and selectively skip cases — for example, skipping a test that fails on purpose. Skipped counts appear as `TotalSkipped (IntentionallySkipped/SkippedDueToError)`.

## Examples

**Example** (Chapter 28, "Testing with State"): `init_per_testcase(ets_tests, Config) -> TabId = ets:new(...), [{table,TabId} | Config].` and the case reads `?config(table, Config)`.

**Example** (Chapter 28, "Creating a Spec File"): `spec.spec` contains `{alias, demo, "./demo/"}.`, `{logdir, "./logs/"}.`, `{suites, demo, all}.`, `{skip_cases, demo, basic_SUITE, test2, "This test fails on purpose"}.`

## Relationships

## Builds Upon

- **Common Test** — Configuration is the framework's state-passing and run-control mechanism

## Related

- **CT test suite** / **CT test case** — Receive and use `Config`
- **CT data directory** — `data_dir` is one of the standard `Config` entries
- **Large-scale testing** — Distributed test specifications extend the `.spec` format with `{node, ...}` and `{init, ...}` tuples

## Common Errors

- **Error**: Pointing `{logdir, Dir}` at a directory that does not exist
  **Correction**: The log directory must exist before tests run, or Common Test complains

- **Error**: Reading `Config` with `proplists:get_value/2` directly
  **Correction**: Use the `?config(Key, List)` macro from `ct.hrl` so the implementation stays stable

## Common Confusions

- **Confusion**: Thinking `data_dir` and `priv_dir` are the same
  **Clarification**: `data_dir` holds static input data; `priv_dir` is a fresh per-run directory safe to write to

## Source Reference

Chapter 28: Common Test for Uncommon Tests, sections "Testing with State" and "Test Specifications" (subsections "Specification File Contents," "Creating a Spec File," "Running Tests with a Spec File").

## Verification Notes

- Definition: Synthesized from two related sections — the `Config` proplist and `.spec` files — both forms of test configuration
- Key Properties: All explicit in the chapter
- Confidence: HIGH — both aspects explicitly documented with examples
- Cross-references: verified against planned cards in this extraction
