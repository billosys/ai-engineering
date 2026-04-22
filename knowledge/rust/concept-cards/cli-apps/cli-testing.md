---
# === CORE IDENTIFICATION ===
concept: CLI Testing
slug: cli-testing

# === CLASSIFICATION ===
category: cli-development
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Command Line Apps in Rust"
source_slug: cli-apps
authors: "The Rust CLI Working Group"
chapter: "07-testing.md"
chapter_number: 7
pdf_page: null
section: "Testing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "CLI testing strategies"
  - "Rust CLI integration tests"
  - "assert_cmd testing"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cli-rust-getting-started
  - cli-argument-parsing
  - cli-output
extends: []
related:
  - cli-error-reporting
  - cli-packaging
  - clap-testing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you write unit tests for a Rust CLI application?"
  - "How do you write integration tests that run the CLI binary?"
  - "How do you make CLI code testable by extracting logic into functions?"
  - "What testing crates are recommended for Rust CLI apps?"
---

# Quick Definition

CLI testing in Rust operates at two levels: unit tests for core logic (extracted into testable functions that accept `impl Write` instead of printing directly) and integration tests using `assert_cmd` to run the compiled binary and verify its output and exit status. Temporary test files are managed with `assert_fs`, and property-based testing with `proptest` and fuzzing cover edge cases.

# Core Definition

The chapter presents a layered testing strategy for CLI applications:

**Unit Testing**: Extract core logic from `main` into separate functions. The key insight is making output testable by accepting `impl std::io::Write` as a parameter instead of using `println!` directly. In tests, pass a `Vec<u8>` as the writer and assert against its contents. This pattern applies broadly: any function that writes output can be made testable by parameterizing the output destination.

**Library/Binary Split**: Move business logic into `src/lib.rs` (as `pub fn`) and keep `src/main.rs` thin. Call library functions via `grrs::find_matches(...)`. This makes the logic importable and testable without running the binary.

**Integration Testing**: Place tests in `tests/cli.rs`. Use `assert_cmd` to run the compiled binary via `Command::cargo_bin("grrs")`, provide arguments with `.arg()`, and assert on output and exit status using `predicates`. Use `assert_fs` to create temporary files with known content for deterministic test inputs.

**Advanced Testing**: `proptest` generates random inputs to discover edge cases in unit logic. Fuzzers (via `cargo-fuzz`) test parsers and file processors with arbitrary data to find crashes.

# Prerequisites

- **cli-rust-getting-started**: A working CLI binary to test
- **cli-argument-parsing**: Understanding of how the CLI accepts arguments
- **cli-output**: Understanding of stdout/stderr distinction and `impl Write` abstraction

# Key Properties

1. `#[test]` attribute marks functions as tests; `cargo test` discovers and runs them
2. `assert_eq!` compares expected and actual values; test panics on mismatch
3. Core logic should be extracted from `main` into named, testable functions
4. `impl std::io::Write` parameter replaces `println!` for testable output
5. `writeln!(writer, ...)` writes to any `Write` implementor (stdout, Vec<u8>, file)
6. In tests, `Vec<u8>` serves as an in-memory buffer; assert with `b"expected"` byte literals
7. `src/lib.rs` holds public functions; `src/main.rs` calls them via `crate_name::function()`
8. Integration tests live in `tests/` directory and test the binary as a black box
9. `assert_cmd` provides `Command::cargo_bin("name")` to invoke the compiled binary
10. `assert_fs` creates temporary files that auto-delete when the test function exits
11. Dependencies used only for testing go in `[dev-dependencies]` in `Cargo.toml`
12. `proptest` generates random inputs; fuzzers find crashes in parsers

# Construction / Recognition

## To Make a Function Testable:
1. Extract logic from `main` into a named function
2. Replace `println!("{}",line)` with `writeln!(writer, "{}", line)`
3. Add `writer: impl std::io::Write` as a parameter
4. In production code: pass `&mut std::io::stdout()`
5. In tests: pass a `Vec::new()` and assert on its contents

## To Write Integration Tests:
1. Add to `[dev-dependencies]`: `assert_cmd`, `predicates`, `assert_fs`
2. Create `tests/cli.rs`
3. Use `Command::cargo_bin("grrs")?.arg("pattern").arg("file").assert()`
4. Chain predicates: `.success()`, `.failure()`, `.stdout(predicate::str::contains("text"))`

## Project Structure for Testability:
```
src/
  main.rs    # thin: parse args, call lib functions, handle exit
  lib.rs     # pub fn find_matches(...) and other business logic
tests/
  cli.rs     # integration tests using assert_cmd
```

# Context & Application

Testing strategy for CLIs reflects a general software engineering principle: test at the right level. Unit tests for pure logic are fast and precise. Integration tests catch wiring bugs (wrong argument passed, wrong output stream) but are slower. The `impl Write` pattern is particularly idiomatic in Rust -- it uses trait-based abstraction to decouple logic from I/O without the overhead of dynamic dispatch (using static dispatch via monomorphization).

**What to test (from the book):**
- Integration tests should cover user-observable behavior: missing file errors, empty output for no matches, correct output for matches, exit codes for missing arguments
- Unit tests should cover edge cases in core logic
- Don't test generated output layout (e.g., exact `--help` format) -- it's clap's responsibility
- Consider `proptest` for functions with many possible inputs
- Consider fuzzers for programs that parse arbitrary file formats

# Examples

**Example 1** (Ch 7): Extracting logic for testability -- the `impl Write` pattern:
```rust,ignore
fn find_matches(content: &str, pattern: &str, mut writer: impl std::io::Write) {
    for line in content.lines() {
        if line.contains(pattern) {
            writeln!(writer, "{}", line);
        }
    }
}

#[test]
fn find_a_match() {
    let mut result = Vec::new();
    find_matches("lorem ipsum\ndolor sit amet", "lorem", &mut result);
    assert_eq!(result, b"lorem ipsum\n");
}
```

**Example 2** (Ch 7): Calling the testable function from main:
```rust,ignore
fn main() -> Result<()> {
    let args = Cli::parse();
    let content = std::fs::read_to_string(&args.path)
        .with_context(|| format!("could not read file `{}`", args.path.display()))?;
    find_matches(&content, &args.pattern, &mut std::io::stdout());
    Ok(())
}
```

**Example 3** (Ch 7): Integration test with assert_cmd for missing file:
```rust,ignore
use assert_cmd::prelude::*;
use predicates::prelude::*;
use std::process::Command;

#[test]
fn file_doesnt_exist() -> Result<(), Box<dyn std::error::Error>> {
    let mut cmd = Command::cargo_bin("grrs")?;
    cmd.arg("foobar").arg("test/file/doesnt/exist");
    cmd.assert()
        .failure()
        .stderr(predicate::str::contains("could not read file"));
    Ok(())
}
```

**Example 4** (Ch 7): Integration test with temporary files (assert_fs):
```rust,ignore
use assert_cmd::prelude::*;
use assert_fs::prelude::*;
use predicates::prelude::*;
use std::process::Command;

#[test]
fn find_content_in_file() -> Result<(), Box<dyn std::error::Error>> {
    let file = assert_fs::NamedTempFile::new("sample.txt")?;
    file.write_str("A test\nActual content\nMore content\nAnother test")?;

    let mut cmd = Command::cargo_bin("grrs")?;
    cmd.arg("test").arg(file.path());
    cmd.assert()
        .success()
        .stdout(predicate::str::contains("A test\nAnother test"));
    Ok(())
}
```

# Relationships

## Enables
- **cli-packaging** -- well-tested code is ready for distribution

## Related
- **cli-output** -- the `impl Write` pattern connects output design with testability
- **cli-error-reporting** -- integration tests verify error message content
- **clap-testing** -- clap-specific testing patterns for argument parsing

## Contrasts With
- Manual testing (running the binary by hand) -- automated tests are repeatable and catch regressions

# Common Errors

- **Error**: Writing unit tests that call `main()` directly.
  **Correction**: Extract business logic into separate functions. Test those functions, not `main`. Use integration tests (`assert_cmd`) to test the full binary.

- **Error**: Using `println!` in logic functions, making output untestable.
  **Correction**: Accept `impl std::io::Write` and use `writeln!`. Pass `stdout()` in production, `Vec::new()` in tests.

- **Error**: Putting `assert_cmd` and `assert_fs` in `[dependencies]` instead of `[dev-dependencies]`.
  **Correction**: Testing crates belong in `[dev-dependencies]` so they are not compiled into release builds.

# Common Confusions

- **Confusion**: Thinking `b"text"` and `"text"` are the same in assertions.
  **Clarification**: `b"text"` is a byte string literal (`&[u8]`), while `"text"` is a string literal (`&str`). When comparing against `Vec<u8>` output from a `Write` implementor, use `b"text"`.

- **Confusion**: Assuming integration tests in `tests/` can access private functions.
  **Clarification**: Integration tests in `tests/` are separate crates that can only access your `pub` API from `src/lib.rs`. Private functions in `src/main.rs` or `src/lib.rs` are not accessible. Unit tests inside `src/` files can access private items.

- **Confusion**: Thinking `Command::cargo_bin` runs `cargo build` every time.
  **Clarification**: `cargo test` compiles the binary before running tests. `Command::cargo_bin` locates the already-compiled binary. The first run may take longer due to compilation.

# Source Reference

Chapter 7 (Testing) from the CLI Apps in Rust book. Covers unit testing with `#[test]`, the `impl Write` pattern for testable output, library/binary split, integration testing with `assert_cmd`/`assert_fs`/`predicates`, and mentions of `proptest` and fuzzing.

# Verification Notes

- `impl Write` pattern: Directly from the "Making your code testable" section showing the progression from `println!` to `writeln!`
- `Vec<u8>` as test writer: From the test example with `b"lorem ipsum\n"` assertion
- Library/binary split: Steps 1-4 from "Splitting your code into library and binary targets"
- assert_cmd integration: `Command::cargo_bin("grrs")` example from "Testing CLI applications by running them"
- assert_fs usage: `NamedTempFile` example from "Generating test files"
- dev-dependencies: `Cargo.toml` snippet from the chapter
- proptest and fuzzing: Mentioned in "What to test?" section
- Confidence: HIGH -- comprehensive chapter with extensive code examples
- Cross-references: clap-testing references the clap extraction set
