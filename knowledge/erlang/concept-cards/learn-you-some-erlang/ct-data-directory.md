---
concept: Common Test Data Directory
slug: ct-data-directory
category: testing
subcategory: common-test
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Common Test for Uncommon Tests"
chapter_number: 28
pdf_page: null
section: "Common Test Structure"
extraction_confidence: high
aliases:
  - "data_dir"
  - "priv_dir"
  - "SUITE_data directory"
prerequisites:
  - common-test
  - ct-test-suite
related:
  - ct-configuration
  - ct-test-case
contrasts_with: []
answers_questions:
  - "What is the Common Test data directory?"
  - "Where does a Common Test case store its side effects?"
---

# Common Test Data Directory

## Quick Definition

The Common Test data directory (`data_dir`) holds a suite's static input data, while the private directory (`priv_dir`) is a fresh per-run directory where test cases can safely write side effects.

## Core Definition

Common Test assumes tests need data to instantiate things and a place to store "side effect-y" stuff. Each test suite is allowed a *data directory*, conventionally named `<Module>_SUITE_data/`, which contains anything useful to the tests. Separately, on every run Common Test creates a unique *private directory* (`priv dir`) for storing output. Both the data directory and the private directory are passed to each test case as part of the `Config` proplist, under the keys `data_dir` and `priv_dir`. Because the private directory is unique per run, a case can write freely to it without overwriting important files or earlier results (Chapter 28, "Common Test Structure").

## Prerequisites

- **Common Test** — These directories are a Common Test convention
- **CT test suite** — The data directory is named after and associated with a suite

## Key Properties

1. The data directory is conventionally named `<Module>_SUITE_data/` (e.g., `m8ball_SUITE_data/`)
2. The data directory holds static input data; it is optional and Common Test does not complain if absent
3. The private directory (`priv_dir`) is created fresh for every test run, ensuring isolation
4. Both directories are delivered to test cases via the `Config` proplist keys `data_dir` and `priv_dir`
5. Writing to `priv_dir` cannot overwrite prior runs' results

## Construction / Recognition

## To Use the Data Directories

1. Create `<Module>_SUITE_data/` next to the suite and put static fixtures inside it
2. In a test case, read the path with `?config(data_dir, Config)`
3. Write output files to `?config(priv_dir, Config)`

## Context & Application

The data directory and private directory implement Common Test's two structural assumptions — that tests need instantiation data and a scratch space. Mnesia tests, for example, set `application:set_env(mnesia, dir, ?config(priv_dir, Config))` so each run gets a private schema location and earlier runs cannot clash.

## Examples

**Example** (Chapter 28, "Creating a Simple Test Suite"): `basic_SUITE` omits `basic_SUITE_data/` and Common Test runs fine without it.

**Example** (Chapter 29, "Installing the Database"): `init_per_suite/1` uses `Priv = ?config(priv_dir, Config)` and sets the Mnesia `dir` to `Priv` so each test run installs its schema in a private location.

## Relationships

## Builds Upon

- **Common Test** — The directories satisfy the framework's data/side-effect assumptions

## Related

- **CT configuration** — Both directory paths are entries in the `Config` proplist
- **CT test case** — Cases consume `data_dir` and `priv_dir` from `Config`

## Common Errors

- **Error**: Writing test output into the suite directory instead of `priv_dir`
  **Correction**: Write to `priv_dir` so runs are isolated and prior results are not clobbered

## Common Confusions

- **Confusion**: Thinking `data_dir` is where test output goes
  **Clarification**: `data_dir` is for static inputs; output belongs in the per-run `priv_dir`

## Source Reference

Chapter 28: Common Test for Uncommon Tests, section "Common Test Structure"; usage example in Chapter 29, "Installing the Database."

## Verification Notes

- Definition: Direct adaptation from "Common Test Structure"
- Key Properties: All explicit in the chapter
- Confidence: HIGH — explicitly described
- Cross-references: verified against planned cards in this extraction
