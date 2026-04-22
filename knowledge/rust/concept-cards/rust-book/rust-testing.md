---
# === CORE IDENTIFICATION ===
concept: Writing Automated Tests
slug: rust-testing

# === CLASSIFICATION ===
category: testing
subcategory: test-framework
tier: intermediate

# === PROVENANCE ===
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "Writing Automated Tests"
chapter_number: 11
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "cargo test"
  - "unit tests"
  - "integration tests"
  - "test organization"
  - "#[test] attribute"
  - "#[should_panic]"
  - "#[cfg(test)]"
  - "doc tests"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rust-common-programming-concepts
  - rust-structs
  - rust-modules-and-crates
extends: []
related:
  - rust-generics-traits-lifetimes
  - rust-error-handling
  - rust-cargo-advanced
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write a test function in Rust?"
  - "What are the assert macros available in Rust?"
  - "How do I test that code panics correctly?"
  - "How do I run a subset of tests by name?"
  - "What is the difference between unit tests and integration tests in Rust?"
  - "Where do integration test files go?"
  - "Can I test private functions in Rust?"
  - "How do I share helper code between integration tests?"
  - "How do I ignore slow tests?"
  - "Can test functions return Result<T, E>?"
---

# Quick Definition

Rust's built-in test framework uses the `#[test]` attribute to mark functions as tests, assertion macros (`assert!`, `assert_eq!`, `assert_ne!`) to verify behavior, and `cargo test` to discover and run them. Tests are organized as unit tests (in `#[cfg(test)]` modules alongside source code) and integration tests (in a top-level `tests/` directory).

# Core Definition

The source defines tests as "Rust functions that verify that the non-test code is functioning in the expected manner." Test function bodies "typically perform these three actions: Set up any needed data or state. Run the code you want to test. Assert that the results are what you expect" (Ch. 11, "How to Write Tests").

A test function is created by adding `#[test]` before `fn`. The `cargo test` command "compiles your code in test mode and runs the resultant test binary." Tests fail "when something in the test function panics. Each test is run in a new thread, and when the main thread sees that a test thread has died, the test is marked as failed" (Ch. 11, "Structuring Test Functions").

The Rust community organizes tests into two categories: "_Unit tests_ are small and more focused, testing one module in isolation at a time, and can test private interfaces. _Integration tests_ are entirely external to your library and use your code in the same way any other external code would, using only the public interface" (Ch. 11, "Test Organization").

# Prerequisites

- **Common Programming Concepts** -- functions, control flow, and basic types are needed to write test logic
- **Structs** -- deriving `PartialEq` and `Debug` (required by `assert_eq!`/`assert_ne!`) is explained in the structs chapter
- **Modules and Crates** -- test organization relies on module visibility rules (`use super::*`) and the distinction between library and binary crates

# Key Properties

1. **`#[test]` attribute** marks a function as a test; without it, the function is not executed by the test runner
2. **`assert!` macro** checks a boolean condition; panics with failure if `false`
3. **`assert_eq!` and `assert_ne!`** compare two values for equality/inequality using `==`/`!=`; print both values on failure (requires `PartialEq` and `Debug` traits)
4. **Custom failure messages** can be added as additional arguments to any assert macro using `format!` syntax
5. **`#[should_panic]`** attribute makes a test pass only if the code panics; accepts an optional `expected` parameter for substring matching on the panic message
6. **`Result<T, E>` return type** in tests enables the `?` operator; test fails on `Err`, passes on `Ok`
7. **Tests run in parallel** by default using threads; `--test-threads=1` forces sequential execution
8. **Output capture**: passing test output is suppressed; `--show-output` flag displays it
9. **Test filtering**: passing a string to `cargo test` runs only tests whose names contain that string
10. **`#[ignore]`** attribute excludes tests from default runs; `cargo test -- --ignored` runs only ignored tests; `--include-ignored` runs all
11. **`#[cfg(test)]`** compiles the annotated module only during `cargo test`, not during `cargo build`
12. **Unit tests** live in `src/` files in a `#[cfg(test)] mod tests` module and can test private functions via `use super::*`
13. **Integration tests** live in a top-level `tests/` directory; each file is compiled as a separate crate and can only access the public API
14. **Shared test helpers** go in `tests/common/mod.rs` (not `tests/common.rs`) to avoid being treated as a test crate
15. **Binary crates** (with only `src/main.rs`) cannot have integration tests; the idiomatic solution is to put logic in `src/lib.rs`
16. **Doc tests** run code examples in `///` documentation comments as tests during `cargo test`

# Construction / Recognition

## Writing a Basic Test:
```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_adds_two() {
        let result = add_two(2);
        assert_eq!(result, 4);
    }
}
```

## Testing for Panics with Expected Message:
```rust
#[test]
#[should_panic(expected = "less than or equal to 100")]
fn greater_than_100() {
    Guess::new(200);
}
```

## Using Result<T, E> in Tests:
```rust
#[test]
fn it_works() -> Result<(), String> {
    let result = add(2, 2);
    if result == 4 {
        Ok(())
    } else {
        Err(String::from("two plus two does not equal four"))
    }
}
```

## Creating an Integration Test:
```text
project/
  src/lib.rs
  tests/
    integration_test.rs
    common/
      mod.rs          # shared helpers, not a test crate
```

```rust
// tests/integration_test.rs
use adder::add_two;

#[test]
fn it_adds_two() {
    assert_eq!(4, add_two(2));
}
```

## Running Tests Selectively:
```console
$ cargo test              # run all tests
$ cargo test add          # run tests with "add" in name
$ cargo test -- --ignored # run only ignored tests
$ cargo test -- --test-threads=1  # run sequentially
$ cargo test --test integration_test  # run one integration test file
```

# Context & Application

Chapter 11 provides the complete testing toolkit built into Rust and Cargo. Unlike many languages that require external testing frameworks, Rust's test support is first-class: the compiler itself provides `#[test]`, `#[cfg(test)]`, and the assertion macros, while Cargo handles test discovery, compilation, and execution.

**Practical contexts:**
- Writing unit tests alongside implementation code in every module
- Creating integration tests to verify public API behavior
- Using `#[should_panic]` for validating error conditions and invariant enforcement
- Using doc tests to keep documentation examples synchronized with code
- Structuring CI pipelines around `cargo test` with appropriate flags

**The chapter emphasizes** that Rust's type system and ownership rules prevent many bugs, "but tests are still important to reduce logic bugs having to do with how your code is expected to behave" (Ch. 11, "Summary").

# Examples

**Example 1** (Ch. 11, Listing 11-6): Testing `Rectangle::can_hold` with `assert!`:
```rust
#[test]
fn larger_can_hold_smaller() {
    let larger = Rectangle { width: 8, height: 7 };
    let smaller = Rectangle { width: 5, height: 1 };
    assert!(larger.can_hold(&smaller));
}
```

**Example 2** (Ch. 11, Listing 11-7): Using `assert_eq!` to test `add_two`:
```rust
#[test]
fn it_adds_two() {
    let result = add_two(2);
    assert_eq!(result, 4);
}
```

**Example 3** (Ch. 11, "Adding Custom Failure Messages"): Custom failure message with format arguments:
```rust
assert!(
    result.contains("Carol"),
    "Greeting did not contain name, value was `{result}`"
);
```

**Example 4** (Ch. 11, Listing 11-9): `should_panic` with `expected` substring to ensure the correct panic branch fires.

**Example 5** (Ch. 11, Listing 11-12): Testing a private function -- `internal_adder` is not `pub`, but the `tests` module accesses it via `use super::*` because child modules can use ancestor items.

**Example 6** (Ch. 11, "Submodules in Integration Tests"): Shared helper code placed in `tests/common/mod.rs` instead of `tests/common.rs` to prevent Cargo from treating it as an integration test file.

# Relationships

## Builds Upon
- **Modules and Crates** -- test organization relies on module visibility and the library/binary crate distinction

## Enables
- **Cargo Advanced** -- doc tests connect testing to documentation comments and `cargo doc`
- **CI workflows** -- `cargo test` is the foundation for automated quality assurance

## Related
- **Generics, Traits, and Lifetimes** -- `assert_eq!`/`assert_ne!` require `PartialEq` + `Debug` traits, commonly derived
- **Error Handling** -- `Result<T, E>` return type in tests enables `?` operator usage

## Contrasts With
- None within this source

# Common Errors

- **Error**: Placing a shared helper file at `tests/common.rs` instead of `tests/common/mod.rs`.
  **Correction**: Files directly in the `tests/` directory are treated as separate test crates. Use `tests/common/mod.rs` for shared helpers.

- **Error**: Expecting `#[should_panic]` to work on tests that return `Result<T, E>`.
  **Correction**: `should_panic` cannot be used with `Result`-returning tests. Use `assert!(value.is_err())` instead.

- **Error**: Writing integration tests for a binary-only crate (only `src/main.rs`, no `src/lib.rs`).
  **Correction**: Integration tests can only access library crate APIs. Move logic into `src/lib.rs` and have `src/main.rs` call it.

- **Error**: Tests interfering with each other due to shared state (e.g., files, environment variables) when running in parallel.
  **Correction**: Ensure tests are independent, or run with `-- --test-threads=1` for sequential execution.

# Common Confusions

- **Confusion**: Thinking `assert_eq!` arguments must be in a specific order (expected, actual).
  **Clarification**: Rust calls them `left` and `right`, and order does not matter. The failure message shows both values regardless of argument order.

- **Confusion**: Believing all output from passing tests is lost.
  **Clarification**: Passing test output is captured by default but can be shown with `cargo test -- --show-output`.

- **Confusion**: Thinking `#[cfg(test)]` is needed in integration test files.
  **Clarification**: Integration tests in the `tests/` directory are only compiled during `cargo test` by Cargo convention; `#[cfg(test)]` is unnecessary there. It is needed for unit test modules in `src/` files.

- **Confusion**: Believing private functions cannot be tested in Rust.
  **Clarification**: Because the `tests` module is a child module, `use super::*` brings private items from the parent module into scope, allowing direct testing.

# Source Reference

Chapter 11: Writing Automated Tests. Sections: "How to Write Tests" (structuring test functions, `assert!`, `assert_eq!`, `assert_ne!`, custom messages, `should_panic`, `Result<T,E>` in tests), "Controlling How Tests Are Run" (parallel/sequential, showing output, filtering, ignoring), "Test Organization" (unit tests, `#[cfg(test)]`, private functions, integration tests, `tests/` directory, submodules, binary crates). No page numbers (online documentation source).

# Verification Notes

- Test function definition: directly quoted from Ch. 11 "How to Write Tests" opening
- Three-action pattern (setup, run, assert): directly quoted from source
- Unit vs integration test distinction: directly quoted from "Test Organization" section
- `assert_eq!` left/right semantics: explicitly described in source
- Confidence: HIGH -- Ch. 11 provides complete, explicit definitions for every testing concept with working code examples and compiler output
- Cross-references: all slug references correspond to planned or existing concept cards
- Uncertainties: benchmark tests are mentioned as nightly-only and not detailed
