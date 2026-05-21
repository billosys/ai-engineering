---
# === CORE IDENTIFICATION ===
concept: EUnit Test
slug: eunit-test

# === CLASSIFICATION ===
category: testing
subcategory: unit-testing
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Writing a TCP-based RPC service"
chapter_number: 3
pdf_page: null
section: "3.4 A few words on testing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - eunit
  - EUnit

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
  - pattern-matching
extends: []
related:
  - gen-server
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is EUnit?"
  - "How do you write a simple EUnit test?"
  - "How does EUnit detect test functions?"
---

# Quick Definition

EUnit is the Erlang/OTP unit-testing framework. A test is a zero-argument function whose name ends in `_test`; it passes if it returns a value and fails if it throws an exception.

# Core Definition

The Erlang/OTP standard distribution includes two testing frameworks: EUnit and Common Test. EUnit is mainly for unit testing and focuses on making it as simple as possible to write and run tests during development (Ch. 3, Section 3.4). To use it, you include the header `eunit/include/eunit.hrl` just after the `-module(...)` declaration. A test is put in a function that takes no arguments and whose name ends with `_test`; EUnit detects all such functions and assumes they are tests. A test succeeds if it returns some value and fails if it throws an exception. Tests are run with `eunit:test(Module)` or the auto-generated `Module:test()`.

# Prerequisites

- **Erlang module** — Tests are functions in a module.
- **Pattern matching** — The `=` match operator is commonly used to make a test fail (a `badmatch` exception) when a result is wrong.

# Key Properties

1. Ships with the standard Erlang/OTP distribution.
2. Enabled by including `eunit/include/eunit.hrl`.
3. A test is a zero-argument function whose name ends in `_test`.
4. A test passes if it returns a value, fails if it throws an exception.
5. Run via `eunit:test(Module)` or the auto-generated `Module:test()`.
6. EUnit auto-exports test functions and creates the `test()` function.

# Construction / Recognition

## To Write an EUnit Test:
1. Add `-include_lib("eunit/include/eunit.hrl").` after `-module(...)`.
2. Write a function named `something_test()` taking no arguments.
3. Use a pattern match (e.g. `{ok, _} = ...`) so a wrong result throws an exception.
4. Recompile, then run `eunit:test(Module)` or `Module:test()`.

# Context & Application

EUnit covers unit testing — fast, button-press tests of specific properties. Common Test, the other framework, is heavier and suited to large-scale integration testing.

- **Typical contexts**: Testing individual modules during development.
- **Common applications**: A `start_test()` function verifying that `tr_server:start_link/1` succeeds.

# Examples

**Example 1** (Ch. 3): `start_test() -> {ok, _} = tr_server:start_link(1055).` — the match operator throws `badmatch` if the start fails, so the test only returns normally on success.

**Example 2** (Ch. 3): Running `eunit:test(tr_server)` or `tr_server:test()` runs all `_test` functions in the module.

# Relationships

## Related
- **gen-server** — The book's EUnit example tests a `gen_server` module.

## Contrasts With
- The source contrasts EUnit (unit testing) with Common Test (integration testing) in prose, but Common Test is out of this chapter group's scope.

# Common Errors

- **Error**: Naming a test function without the `_test` suffix.
  **Correction**: EUnit only detects functions whose names end in `_test`.

# Common Confusions

- **Confusion**: Thinking you must write and export a `test()` function yourself.
  **Clarification**: EUnit creates `test()` automatically and ensures test functions are exported.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.4 "A few words on testing."

# Verification Notes

- Definition source: Direct adaptation of Section 3.4.
- Confidence rationale: HIGH — explicit, concrete treatment in the source.
- Uncertainties: None.
- Cross-reference status: References Agent-1 slugs `erlang-module`, `pattern-matching`.
- Re-extraction notes: Fresh extraction; no prior card existed.
