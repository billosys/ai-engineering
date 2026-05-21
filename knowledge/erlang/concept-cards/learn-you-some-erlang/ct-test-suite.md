---
concept: Common Test Test Suite
slug: ct-test-suite
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
  - "test suite"
  - "_SUITE module"
prerequisites:
  - common-test
  - ct-test-case
related:
  - ct-test-group
  - ct-data-directory
  - ct-configuration
contrasts_with: []
answers_questions:
  - "What is a Common Test test suite?"
  - "How do I write a Common Test suite?"
---

# Common Test Test Suite

## Quick Definition

A Common Test test suite is a module ending in `_SUITE` that groups related test cases and declares which of them to run via an `all/0` function.

## Core Definition

In Common Test, test cases are single functions that all live in a *test suite* — a module that regroups related test cases together. Each test suite module's name ends with `_SUITE` (for example, `m8ball_SUITE`). The suite must include `common_test/include/ct.hrl` and export an `all/0` function returning the list of test cases (and groups) to run. Unlike EUnit, which discovers tests by name convention, Common Test requires this explicit `all/0` declaration. Suites live inside a test object directory, which sits under a test root (Chapter 28, "Common Test Structure" and "Creating a Simple Test Suite").

## Prerequisites

- **Common Test** — The suite is the unit of organization within the Common Test framework
- **CT test case** — A suite exists to hold test cases

## Key Properties

1. Module name must end with `_SUITE`
2. Should include `common_test/include/ct.hrl` (provides useful macros like `?config`)
3. Must export and define `all/0`, returning a list of test cases and `{group, Name}` tuples
4. May define suite-level setup/teardown via `init_per_suite/1` and `end_per_suite/1`, which run once before and after all groups and cases
5. May define per-case setup/teardown via `init_per_testcase/2` and `end_per_testcase/2`
6. May define `groups/0` to declare test groups
7. May have an associated data directory named `<Module>_SUITE_data/`

## Construction / Recognition

## To Write a Test Suite

1. Create `name_SUITE.erl` and add `-include_lib("common_test/include/ct.hrl").`
2. Export `all/0` and each test case function
3. Define `all() -> [case1, case2, ...].`
4. Optionally export and define `init_per_suite/1`, `end_per_suite/1`, `init_per_testcase/2`, `end_per_testcase/2`, and `groups/0`

## Context & Application

`init_per_suite/1` and `end_per_suite/1` run only once and are useful for general state and dependencies needed by all tests — for example, manually starting applications the tests depend on. The Common Test structure layers test root > test object directory > suite > group > test case.

## Examples

**Example** (Chapter 28, "Creating a Simple Test Suite"): `basic_SUITE` declares `-export([all/0]).`, `-export([test1/1, test2/1]).`, and `all() -> [test1, test2].`

**Example** (Chapter 29): `mafiapp_SUITE` uses `init_per_suite/1` to set the Mnesia `dir`, install the database, and start applications, with `end_per_suite/1` stopping Mnesia.

## Relationships

## Builds Upon

- **Common Test** — A suite is the framework's module-level container

## Related

- **CT test case** — The functions a suite contains
- **CT test group** — Optional hierarchical grouping declared via `groups/0`
- **CT data directory** — The optional `<Module>_SUITE_data/` directory for static test data

## Common Errors

- **Error**: Forgetting to add a test case to `all/0`
  **Correction**: Common Test runs only what `all/0` returns; name conventions do not auto-discover cases

## Common Confusions

- **Confusion**: Expecting EUnit-style name-based test discovery
  **Clarification**: Common Test requires an explicit `all/0` call listing the cases and groups to run

## Source Reference

Chapter 28: Common Test for Uncommon Tests, sections "Common Test Structure," "Creating a Simple Test Suite," and "Test Suites Redux."

## Verification Notes

- Definition: Direct adaptation from "Common Test Structure"
- Key Properties: All explicit across the chapter
- Confidence: HIGH — explicitly defined with multiple code examples
- Cross-references: verified against planned cards in this extraction
