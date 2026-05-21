---
concept: Common Test Test Case
slug: ct-test-case
category: testing
subcategory: common-test
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Common Test for Uncommon Tests"
chapter_number: 28
pdf_page: null
section: "Common Test Structure"
extraction_confidence: high
aliases:
  - "test case"
prerequisites:
  - common-test
  - ct-test-suite
related:
  - ct-configuration
  - ct-data-directory
contrasts_with: []
answers_questions:
  - "What is a Common Test test case?"
  - "How does a Common Test test case signal success or failure?"
---

# Common Test Test Case

## Quick Definition

A Common Test test case is a single one-argument function in a test suite that succeeds if it runs to completion and fails if it crashes.

## Core Definition

The test case is the simplest part of Common Test: a bit of code that either fails or succeeds. If the case crashes, the test is unsuccessful; otherwise it is considered successful. In Common Test, test cases are single functions of arity 1, living inside a test suite module. The single argument is a `Config` proplist carrying the case's initial state — including `data_dir` (the static data directory) and `priv_dir` (a fresh per-run private directory the case may write to) (Chapter 28, "Common Test Structure" and "Creating a Simple Test Suite").

## Prerequisites

- **Common Test** — A test case is the atomic test unit of the framework
- **CT test suite** — Test cases live inside suites and must be listed in `all/0`

## Key Properties

1. Implemented as a single function taking one argument, the `Config` proplist
2. Succeeds by running to completion; fails by crashing (e.g., a `badmatch` or `badarith`)
3. Receives `Config`, a proplist containing at least `data_dir` and `priv_dir`
4. Must be listed in the suite's `all/0` (directly or via a group) to be run
5. Per-case setup/teardown is provided by `init_per_testcase/2` and `end_per_testcase/2`, which run in the same process as the case
6. A crash in the test case still triggers `end_per_testcase/2` cleanup, except on `kill` exit signals
7. Failures are recorded in the HTML log with the failing line and reason

## Construction / Recognition

## To Write a Test Case

1. Define a function `my_case(Config) -> ...` in the suite
2. Make assertions by pattern matching (e.g., `1 = 1` succeeds, `1/0` crashes)
3. Read state from `Config` using the `?config(Key, Config)` macro
4. Export the function and add its name to `all/0`

## Context & Application

Because `init_per_testcase/2` and `end_per_testcase/2` run in the same process as the case, you can safely set links or start ETS tables in setup without cross-process ownership problems. Test cases assert by ordinary pattern matching rather than EUnit-style assertion macros.

## Examples

**Example** (Chapter 28, "Creating a Simple Test Suite"): `test1(_Config) -> 1 = 1.` always succeeds; `test2(_Config) -> A = 0, 1/A.` fails with `badarith` on line 13.

## Relationships

## Builds Upon

- **CT test suite** — Test cases are contained in and listed by a suite

## Related

- **CT configuration** — The `Config` proplist passed to every case
- **CT data directory** — `data_dir` in `Config` points to the suite's static data

## Common Errors

- **Error**: Defining a test case with the wrong arity
  **Correction**: Common Test test cases must take exactly one argument, the `Config` proplist

## Common Confusions

- **Confusion**: Expecting a test case to need explicit assertions to "pass"
  **Clarification**: A case passes simply by not crashing; assertions are pattern matches that crash on failure

## Source Reference

Chapter 28: Common Test for Uncommon Tests, sections "Common Test Structure," "Creating a Simple Test Suite," and "Testing with State."

## Verification Notes

- Definition: Direct adaptation from "Common Test Structure"
- Key Properties: All explicit in the chapter
- Confidence: HIGH — explicitly defined with code examples
- Cross-references: verified against planned cards in this extraction
