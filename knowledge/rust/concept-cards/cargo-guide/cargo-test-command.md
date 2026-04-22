---
# === CORE IDENTIFICATION ===
concept: Cargo Test Command
slug: cargo-test-command

# === CLASSIFICATION ===
category: build-system
subcategory: testing
tier: intermediate

# === PROVENANCE ===
source: "Cargo Guide"
source_slug: cargo-guide
authors: "The Cargo Team"
chapter: "07-tests"
chapter_number: 7
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "cargo test"
  - "running Rust tests"
  - "Cargo testing"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - creating-a-cargo-project
  - cargo-project-layout
extends: []
related:
  - cargo-ci
  - cargo-build-performance
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I run tests in a Cargo project?"
  - "Where does Cargo look for tests?"
  - "What types of tests does cargo test run?"
  - "How do I run a specific test by name?"
  - "Does cargo test also check examples and documentation?"
---

# Quick Definition

`cargo test` is the command that discovers and runs all tests in a Cargo package. It looks for unit tests in `src/` files, integration tests in `tests/`, and documentation tests in doc comments. It also compiles examples to verify they still build. A filter argument can limit which tests run.

# Core Definition

The source states: "Cargo can run your tests with the `cargo test` command. Cargo looks for tests to run in two places: in each of your `src` files and any tests in `tests/`." (Ch. 7). Tests in `src/` should be unit tests and documentation tests, while tests in `tests/` should be integration-style tests that import the crate. The source also notes that `cargo test` "runs additional checks as well. It will compile any examples you've included to ensure they still compile. It also runs documentation tests to ensure your code samples from documentation comments compile."

A test filter can be passed as an argument to `cargo test` to run only tests whose names contain the filter string.

# Prerequisites

- **Creating a Cargo Project** -- you need a Cargo project to test
- **Cargo Project Layout** -- understanding where `src/`, `tests/`, and `examples/` directories live

# Key Properties

1. **Two test locations**: Unit tests in `src/` files and integration tests in `tests/`
2. **Documentation tests**: Code samples in doc comments are also compiled and tested
3. **Example compilation**: `cargo test` compiles examples to verify they still build
4. **Test filtering**: `cargo test foo` runs any test with "foo" in its name
5. **Integration test imports**: Tests in `tests/` must import the crate being tested (they are external)
6. **Comprehensive output**: Reports passed, failed, ignored, measured, and filtered counts

# Construction / Recognition

## Running All Tests:
```console
$ cargo test
   Compiling regex v1.5.0 (https://github.com/rust-lang/regex.git#9f9f693)
   Compiling hello_world v0.1.0 (file:///path/to/package/hello_world)
     Running target/test/hello_world-9c2b65bbb79eabce

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```

## Running Specific Tests:
```console
$ cargo test foo
```
This runs any test with `foo` in its name.

# Context & Application

This card provides the guide-level overview of testing with Cargo. The source is deliberately brief, describing the test discovery mechanism and the three types of tests (unit, integration, documentation) without going into detailed test-writing guidance. It points to the Rust book's testing chapter and Cargo's reference documentation for more depth. This card complements the `tests/` directory convention described in the project-layout card and connects to CI practices where `cargo test` is the core verification step.

# Examples

**Example 1** (Ch. 7): Running `cargo test` with no tests defined:
```console
$ cargo test
   Compiling regex v1.5.0 (https://github.com/rust-lang/regex.git#9f9f693)
   Compiling hello_world v0.1.0 (file:///path/to/package/hello_world)
     Running target/test/hello_world-9c2b65bbb79eabce

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```
> "If your package had tests, you would see more output with the correct number of tests."

**Example 2** (Ch. 7): Filtering tests:
```console
$ cargo test foo
```
> "This will run any test with `foo` in its name."

**Example 3** (Ch. 7): Additional checks beyond tests:
> "`cargo test` runs additional checks as well. It will compile any examples you've included to ensure they still compile. It also runs documentation tests to ensure your code samples from documentation comments compile."

# Relationships

## Builds Upon
- **Creating a Cargo Project** -- a project must exist before it can be tested
- **Cargo Project Layout** -- test placement depends on the conventional layout (`src/` for unit tests, `tests/` for integration tests)

## Enables
- **cargo-ci** -- CI pipelines use `cargo test` as their primary verification step

## Related
- **cargo-build-performance** -- test compilation is part of the build process that can be optimized

## Contrasts With
- None within this source

# Common Errors

- **Error**: Writing integration tests in `src/` instead of `tests/`.
  **Correction**: The source distinguishes: "Tests in your `src` files should be unit tests and documentation tests. Tests in `tests/` should be integration-style tests."

- **Error**: Forgetting to import the crate in integration tests.
  **Correction**: "you'll need to import your crates into the files in `tests`." Integration tests are external to the crate and must use `use` statements.

# Common Confusions

- **Confusion**: Thinking `cargo test` only runs unit tests.
  **Clarification**: `cargo test` runs unit tests, integration tests, documentation tests, and also compiles examples to ensure they still build.

- **Confusion**: Thinking `cargo test foo` runs a test named exactly "foo."
  **Clarification**: The filter is a substring match. `cargo test foo` runs "any test with `foo` in its name," which could match `test_foo`, `foo_bar`, etc.

# Source Reference

Chapter 7: Tests. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 7 -- "Cargo can run your tests with the `cargo test` command."
- Confidence rationale: HIGH -- the source clearly describes test discovery locations and filter behavior
- Uncertainties: Detailed test writing, `#[cfg(test)]`, and test organization are not covered in this chapter (the source refers to the Rust book and Cargo reference)
- Cross-reference status: All slugs reference cards within this extraction set
