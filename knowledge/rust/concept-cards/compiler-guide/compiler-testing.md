---
# === CORE IDENTIFICATION ===
concept: Rust Compiler Testing Infrastructure
slug: compiler-testing

# === CLASSIFICATION ===
category: compiler-development
subcategory: testing
tier: foundational

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "Testing the Compiler"
chapter_number: 2
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "compiletest"
  - "UI tests"
  - "compiler test suite"
  - "tests/ui"
  - "run-make tests"
  - "bless tests"
  - "rustc CI"
  - "bors"
  - "try builds"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - building-rustc
extends: []
related:
  - compiler-guide-overview
  - compiler-debugging
  - contributing-to-rustc
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What kinds of tests exist in the Rust compiler repository?"
  - "What is compiletest and how does it work?"
  - "How do I run a specific subset of the compiler test suite?"
  - "How do I create a new UI test?"
  - "What is the --bless flag and when do I use it?"
  - "How does Rust CI work (PR builds, auto builds, try builds)?"
  - "What are the different compiletest test suites and their purposes?"
  - "How do I run tests on remote machines or emulators?"
  - "What is bors and how does the merge queue work?"
  - "What are best practices for writing compiler tests?"
---

# Quick Definition

The Rust compiler has an extensive testing infrastructure centered on **compiletest**, the main test harness that supports dozens of test suites organized under the `tests/` directory. Tests are driven by `./x test`, with the most common suite being **UI tests** (`tests/ui`) that compile Rust code and check stdout/stderr output against snapshot files. The CI system uses GitHub Actions with **bors** managing a merge queue, running PR builds (quick ~40-minute checks), auto builds (full test suite, ~2 hours), and try builds (on-demand testing/benchmarking). Every PR fixing a bug is expected to include a regression test.

# Core Definition

The testing infrastructure spans multiple layers:

**Compiletest** is the primary test harness. It organizes tests into **test suites** (subdirectories of `tests/`), each with different compiler behavior and correctness checks. Tests are annotated with **directives** (comments like `//@ edition:2018`) that control how compiletest builds and evaluates each test. Key test suites include:

- **`ui`** -- the most common; checks stdout/stderr snapshots from compilation
- **`debuginfo`** -- tests debuginfo generation by launching debuggers (gdb, lldb, cdb)
- **`codegen-llvm`** -- checks LLVM IR output using FileCheck
- **`mir-opt`** -- checks MIR generation and optimizations
- **`incremental`** -- tests incremental compilation using revisions
- **`run-make`** -- general purpose tests using Rust programs for complex scenarios
- **`assembly-llvm`** -- checks assembly output using FileCheck
- **`crashes`** -- tracks inputs that cause ICEs to catch accidental fixes
- **`pretty`** -- tests pretty-printing functionality
- **Rustdoc suites** -- `rustdoc-html`, `rustdoc-gui`, `rustdoc-js`, `rustdoc-json`, `rustdoc-ui`

**Package tests** use standard `#[test]` unit tests, integration tests, and doctests for the standard library and compiler packages, invoked with `./x test library/std` or `./x test compiler/rustc_data_structures`.

**CI** executes on GitHub Actions with three build types:
- **PR builds**: Quick ~40-minute subset (tidy, lints, cross-compile check to Windows, LLVM system tests)
- **Auto builds**: Full test suite on all platforms (~2 hours); run before merging via bors
- **Try builds**: On-demand builds for performance benchmarks or crater runs, triggered by `@bors try`

# Prerequisites

- A built compiler (see building-rustc)
- For debuginfo tests: Python-enabled gdb may be required
- For Docker-based testing: Docker installed on Linux (or VM on macOS/Windows)

# Key Properties

1. **UI tests are the default for compiler changes**: "The majority of compiler tests are done with compiletest... The majority of compiletest tests are UI tests in the `tests/ui` directory"
2. **`--bless` auto-updates expected output**: Running `./x test tests/ui --bless` automatically adjusts `.stderr`, `.stdout`, or `.fixed` files to match current compiler output
3. **Error annotations are required in UI tests**: Each expected error must have a `//~` comment annotation (e.g., `//~^ ERROR message`) matching the compiler output
4. **Output normalization for portability**: `$DIR` replaces file paths, `LL` replaces line numbers in `.stderr` files to avoid spurious diffs across systems
5. **Tests are cached**: Previously successful tests are skipped; use `--force-rerun` to override
6. **Every bug fix should have a regression test**: "We expect every PR that fixes a bug in rustc to come accompanied by a regression test of some kind"
7. **Bors serializes merges**: All PRs merge through the bors queue; at most one auto build runs at a time, limiting throughput to ~10 PRs/day
8. **Rollups batch trivial PRs**: Low-risk PRs can be batched together in a "rollup" to improve merge throughput
9. **Toolstate tracks allowed failures**: Some tools/docs are allowed to fail on CI; their status is recorded in `rust-toolstate` and failures auto-ping maintainers
10. **Try builds support custom job selection**: Use `try-job: <pattern>` directives in PR descriptions or `@bors try jobs=<pattern>` to run specific CI jobs

# Construction / Recognition

## Creating a UI Test:

1. Create a `.rs` file in `tests/ui/` (in an appropriate subdirectory):
```rust
// Regression test for #12345: descriptive summary here.
//@ edition:2018

async fn foo() {}

fn bar() {
    foo().await
    //~^ ERROR `await` is only allowed inside `async` functions and blocks
}

fn main() {}
```

2. Generate expected output: `./x test tests/ui/async-await/your-test.rs --bless`
3. Add error annotations matching compiler output
4. Verify the test passes: `./x test tests/ui/async-await/your-test.rs`
5. Check broader impact: `./x test tests/ui`

## Running Tests:

```bash
./x test tests/ui                      # all UI tests
./x test tests/ui/const-generics       # subdirectory of UI tests
./x test tests/ui/specific-test.rs     # single test file
./x test tests/ui --test-args issue-1234  # filter by name
./x test tests/ui --bless              # update expected output
./x test tests/ui --pass check         # run as check-pass only (faster)
./x test library/std                   # standard library tests
./x test compiler/rustc_data_structures  # compiler package tests
./x test tidy                          # code style checks
```

## Test Best Practices:

- Name tests descriptively (e.g., `asm-macro-external-span-ice.rs`, not `issue-123456.rs`)
- Start with a comment explaining what the test exercises and linking to the issue
- Minimize non-critical code; use `#![allow(...)]` for unrelated warnings
- Avoid flaky tests -- they "are the worst kind of tests, arguably even worse than not having the test in the first place"

# Context & Application

- **Compiler contributors**: Running and writing tests is central to every PR
- **Standard library contributors**: Use doctests (primary), unit tests, and integration tests via `./x test library/std`
- **Bug fixers**: Every bug fix needs a regression test, typically a UI test
- **CI/infrastructure contributors**: Modifying CI jobs via `jobs.yml`
- **Performance engineers**: Try builds enable benchmarking via `@bors try @rust-timer queue`

# Examples

**Example 1**: A UI test `.stderr` file showing normalized output:
```text
error[E0728]: `await` is only allowed inside `async` functions and blocks
  --> $DIR/await-without-async.rs:7:10
   |
LL | fn bar() {
   |    --- this is not `async`
LL |     foo().await
   |          ^^^^^^ only allowed inside `async` functions and blocks

error: aborting due to previous error

For more information about this error, try `rustc --explain E0728`.
```

**Example 2**: Debuginfo test with breakpoints and debugger commands:
```rust
//@ compile-flags: -g
//@ lldb-command: run
//@ lldb-command: print foo
//@ lldb-check: $0 = 123

fn main() {
    let foo = 123;
    b(); // #break
}
fn b() {}
```

**Example 3**: Incremental test using revisions:
```rust
//@ revisions: rpass1 rpass2

#[cfg(rpass1)]
fn foo() { println!("one"); }

#[cfg(rpass2)]
fn foo() { println!("two"); }

fn main() { foo(); }
```

**Example 4**: Running tests on a remote machine:
```bash
export TEST_DEVICE_ADDR="1.2.3.4:12345"
./x test tests/ui --target riscv64gc-unknown-linux-gnu
```

**Example 5**: Running CI jobs locally via Docker:
```bash
cargo run --manifest-path src/ci/citool/Cargo.toml run-local dist-x86_64-linux-alt
```

# Relationships

## Builds Upon
- **building-rustc** -- a built compiler is required to run tests

## Enables
- **contributing-to-rustc** -- every contribution needs appropriate tests

## Related
- **compiler-debugging** -- debugging test failures often involves debugging techniques from Ch. 3
- **compiler-guide-overview** -- tests are a key part of the contributor workflow

## Contrasts With
- None within this source

# Common Errors

- **Error**: Running `./x test` without arguments.
  **Correction**: "Running the entire test collection is almost never what you want." Use `./x test tests/ui` or a more targeted subset.

- **Error**: Naming test files only by issue number (e.g., `issue-123456.rs`).
  **Correction**: Use descriptive names like `asm-macro-external-span-ice.rs`. "issue-123456.rs does not tell you immediately anything about what the test is actually exercising."

- **Error**: Forgetting to add error annotations to UI tests.
  **Correction**: Every expected error must have a `//~` annotation. The test will fail with "unexpected error" if annotations are missing.

- **Error**: Running `git add .` after a rebase without running `x` first.
  **Correction**: This can accidentally commit submodule changes. Use specific `git add` commands or run `x` first to update submodules.

# Common Confusions

- **Confusion**: PR CI failure means the test suite fully validates a PR.
  **Clarification**: "PR CI does not try to run `./x doc`. This means that if you have any broken intradoc links... it will happen very late into the full merge queue CI pipeline."

- **Confusion**: Tests must pass with a stage 2 compiler locally.
  **Clarification**: Most development uses stage 1. "While the tests usually work fine with stage 1, there are some limitations." Full stage 2 testing is done by CI.

- **Confusion**: `--bless` alone is sufficient for creating a new test.
  **Clarification**: After `--bless` generates the `.stderr` file, you must add `//~` error annotations in the source file, or the test will fail with "unexpected error."

- **Confusion**: `@bors try` runs the full test suite.
  **Clarification**: By default, try builds run "fast" jobs without tests and with warnings allowed. To run specific test jobs, use `try-job:` directives in the PR description or `@bors try jobs=<pattern>`.

# Source Reference

Chapter 2 (4298 lines) covering: Testing the Compiler overview, Running Tests, Testing with Docker, Testing with CI, Adding New Tests, Best Practices for Writing Tests, and the Compiletest chapter (test suites, directives, UI tests, debuginfo tests, codegen tests, MIR-opt tests, incremental tests, run-make tests, and more). This is the largest chapter in the guide, reflecting the centrality of testing to compiler development.

# Verification Notes

- Definition source: Direct content from Chapter 2 testing documentation
- Key Properties: All items supported by source text with specific commands and examples
- Confidence rationale: HIGH -- detailed, procedural documentation with concrete examples
- Uncertainties: CI job names and configurations evolve; specific job names may change
- Cross-reference status: Related slugs reference other cards in this compiler-guide extraction set
