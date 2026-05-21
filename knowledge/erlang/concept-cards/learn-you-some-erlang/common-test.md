---
concept: Common Test
slug: common-test
category: testing
subcategory: common-test
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Common Test for Uncommon Tests"
chapter_number: 28
pdf_page: null
section: "What Is Common Test?"
extraction_confidence: high
aliases:
  - "ct"
  - "common_test"
prerequisites:
  - eunit
related:
  - ct-test-suite
  - ct-test-case
  - ct-test-group
  - ct-configuration
  - large-scale-testing
contrasts_with:
  - eunit
answers_questions:
  - "What is Common Test?"
  - "What distinguishes EUnit from Common Test?"
---

# Common Test

## Quick Definition

Common Test is an Erlang/OTP testing framework built for system testing — testing whole applications and distributed systems — that complements EUnit's strength at small-scale module testing.

## Core Definition

Common Test is a test framework that ships with Erlang/OTP and is "pretty damn good at system testing." Where EUnit excels at white-box testing at the module level, Common Test is appropriate for testing complete systems, with decent support for libraries and OTP applications and the ability (though not optimal) to test individual modules. The rule of thumb: the smaller the unit under test, the more appropriate EUnit is; the larger the test, the more appropriate Common Test is. Common Test also provides facilities EUnit lacks, including support for distributed Erlang testing (Chapter 28, "What Is Common Test?").

## Prerequisites

- **EUnit** — Common Test is introduced as the next step beyond EUnit; understanding EUnit's limits motivates Common Test

## Key Properties

1. Optimized for system testing and black-box testing of whole systems
2. Assumes tests need data to instantiate things and a place to store side effects
3. Test code is organized into suites of test cases, optionally grouped, in test object directories under a test root
4. Produces detailed HTML logs (`index.html`, `all_runs.html`) recording every test run
5. Runnable from the command line (`ct_run`) or the Erlang shell (`ct:run_test/1`)
6. Supports distributed testing via a central CT master node
7. Has a long, reference-style user guide that is hard to read without first learning the basics

## Construction / Recognition

## To Use Common Test

1. Create a test root directory, and a test object directory inside it
2. Write one or more `*_SUITE.erl` test suite modules, each including `common_test/include/ct.hrl`
3. Run with `ct_run -suite Name_SUITE` from the shell, or `ct:run_test([{suite, Name_SUITE}])` from the Erlang shell
4. Inspect the generated HTML logs for results

## Context & Application

Common Test is the heavy-lifting counterpart to EUnit, used when complex setups, interacting tests, or distributed Erlang make EUnit unwieldy. The chapter notes its documentation originated as Ericsson-internal material and reads as a reference manual rather than a tutorial. EUnit tests can be embedded inside Common Test suites by calling `eunit:test/1` and matching on its `ok`/`error` return.

## Examples

**Example** (Chapter 28, "Creating a Simple Test Suite"): `basic_SUITE.erl` defines `all() -> [test1, test2].` with two single-argument test functions; running `ct_run -suite basic_SUITE` reports "1 ok, 1 failed of 2 test cases."

## Relationships

## Related

- **CT test suite**, **CT test case**, **CT test group** — The structural units Common Test organizes tests into
- **CT configuration** — Per-suite configuration data and test specifications
- **Large-scale testing** — Common Test's distributed testing capability

## Contrasts With

- **EUnit** — EUnit is best for white-box module-level testing with rich assertion macros; Common Test is best for system testing, offers fancier HTML reports and distributed support, but lacks EUnit's assertion macros and is awkward from the shell

## Common Errors

- **Error**: Using `io:format/1-2` to print debugging output and expecting it in the shell
  **Correction**: `io:format` prints only to the HTML logs; use `ct:pal/1-2` to print to both shell and logs

## Common Confusions

- **Confusion**: Treating Common Test as a replacement for EUnit
  **Clarification**: They are complementary — Common Test for system tests, EUnit for module-level tests; either can run inside the other (EUnit inside CT is easy)

## Source Reference

Chapter 28: Common Test for Uncommon Tests, sections "What Is Common Test?", "Common Test Structure," and "Integrating EUnit Within Common Test."

## Verification Notes

- Definition: Direct adaptation from "What Is Common Test?"
- Key Properties: All explicit in the chapter
- Confidence: HIGH — explicitly introduced and contrasted with EUnit
- Cross-references: `eunit` is a shared slug from Agent 4
