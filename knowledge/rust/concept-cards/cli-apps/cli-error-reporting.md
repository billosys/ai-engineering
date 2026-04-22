---
# === CORE IDENTIFICATION ===
concept: CLI Error Reporting
slug: cli-error-reporting

# === CLASSIFICATION ===
category: cli-development
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Command Line Apps in Rust"
source_slug: cli-apps
authors: "The Rust CLI Working Group"
chapter: "05-error-reporting.md"
chapter_number: 5
pdf_page: null
section: "Nicer error reporting"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Rust CLI error handling"
  - "anyhow error context"
  - "CLI error reporting"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cli-rust-getting-started
  - cli-argument-parsing
extends: []
related:
  - cli-output
  - cli-testing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Rust's Result type work for error handling?"
  - "What is the ? operator and how does it propagate errors?"
  - "How does the anyhow crate improve CLI error messages?"
  - "What is the progression from unwrap to proper error handling?"
---

# Quick Definition

Rust CLI error handling progresses from `unwrap()`/`expect()` through `match` on `Result`, to the `?` operator with `Box<dyn Error>`, and finally to the `anyhow` crate which provides contextual error chains. The `anyhow::Context` trait adds human-readable descriptions that form a causal chain from high-level operation to root cause.

# Core Definition

Rust encodes all possible error states in function return types using `Result<T, E>`, an enum with `Ok(value)` and `Err(error)` variants. The chapter presents a deliberate progression of error handling approaches for CLI applications:

1. **`unwrap()` / `expect()`**: Panic on error with an optional message. Quick but crashes the program ungracefully.
2. **`match` on Result**: Explicitly handle both Ok and Err variants. Verbose but gives full control.
3. **`return Err(error.into())`**: Early return from functions, requiring `main` to return `Result<(), Box<dyn std::error::Error>>`.
4. **The `?` operator**: Syntactic sugar for the match-and-return pattern. Appending `?` to a `Result` expression returns the error if present, or unwraps the value if Ok.
5. **`anyhow` with `Context`**: The `anyhow` crate's `Context` trait (`.with_context()` / `.context()`) wraps errors with descriptive messages while preserving the original error chain.

The final recommended pattern for CLI apps uses `anyhow::Result` as the return type of `main` and `.context()` calls at each operation boundary to produce error output like "could not read file `test.txt`\n\nCaused by:\n    No such file or directory".

# Prerequisites

- **cli-rust-getting-started**: Understanding of `Result` from file reading with `.expect()`
- **cli-argument-parsing**: A working CLI that produces arguments to operate on
- Familiarity with Rust's `enum` and `match` syntax

# Key Properties

1. `Result<T, E>` is an enum: `Ok(T)` for success, `Err(E)` for errors
2. `unwrap()` panics on `Err`; `expect("msg")` panics with a custom message
3. `match` on a `Result` requires both arms to return the same type
4. `panic!` in an error arm allows the Ok arm's type to be used after the match
5. `main` can return `Result<(), Box<dyn std::error::Error>>` to use `?` throughout
6. `Box<dyn std::error::Error>` is a trait object that accepts any error type implementing `Error`
7. `?` auto-converts error types using `Into` (e.g., `io::Error` into `Box<dyn Error>`)
8. The last expression in a block is its return value; `Ok(())` at the end of main means success
9. `anyhow::Context` adds `.context("description")` to `Result` types
10. Anyhow preserves the full error chain with "Caused by:" output

# Construction / Recognition

## Error Handling Progression:
1. **Start**: `read_to_string("test.txt").expect("could not read file")`
2. **Improve**: Use `match result { Ok(content) => ..., Err(error) => ... }`
3. **Simplify**: Change `main` to return `Result`, use `?` operator
4. **Contextualize**: Add `anyhow`, use `.with_context(|| format!("could not read file `{}`", path))`

## To Add anyhow:
1. Add `anyhow = "1.0"` to `[dependencies]` in `Cargo.toml`
2. Use `use anyhow::{Context, Result};` in source files
3. Change `main` return type to `anyhow::Result<()>`
4. Append `.context("description")` to fallible operations

# Context & Application

Error handling in CLI applications differs from library code. CLI users need clear, actionable error messages -- not stack traces or debug representations. The progression from `unwrap()` to `anyhow` context chains reflects increasing maturity: prototypes can use `expect()` to fail fast, but released tools should provide error messages that help users fix the problem. The `anyhow` crate is the community-standard choice for application-level error handling (as opposed to `thiserror` for library error types).

**Key Principle**: CLI errors should tell the user what went wrong and ideally what to do about it. Raw OS errors like "No such file or directory (os error 2)" are insufficient -- wrapping them with context like "could not read file `test.txt`" makes the error actionable.

# Examples

**Example 1** (Ch 5): Pattern matching on a Result:
```rust,no_run
let result = std::fs::read_to_string("test.txt");
match result {
    Ok(content) => { println!("File content: {}", content); }
    Err(error) => { println!("Oh noes: {}", error); }
}
```

**Example 2** (Ch 5): Using the `?` operator with a Result-returning main:
```rust,no_run
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let content = std::fs::read_to_string("test.txt")?;
    println!("file content: {}", content);
    Ok(())
}
```

**Example 3** (Ch 5): Adding context with anyhow -- the recommended approach:
```rust,ignore
use anyhow::{Context, Result};

fn main() -> Result<()> {
    let path = "test.txt";
    let content = std::fs::read_to_string(path)
        .with_context(|| format!("could not read file `{}`", path))?;
    println!("file content: {}", content);
    Ok(())
}
```

Produces the error output:
```text
Error: could not read file `test.txt`

Caused by:
    No such file or directory (os error 2)
```

**Example 4** (Ch 5): Custom error type (before discovering anyhow):
```rust,ignore
#[derive(Debug)]
struct CustomError(String);

impl std::fmt::Display for CustomError {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "{}", self.0)
    }
}

impl std::error::Error for CustomError {}
```

# Relationships

## Enables
- **cli-output** -- good error reporting feeds into the output strategy (stderr for errors)
- **cli-testing** -- tests verify that errors are reported correctly

## Related
- **cli-rust-getting-started** -- introduces `.expect()` as the initial error strategy
- **cli-argument-parsing** -- clap handles argument validation errors separately

## Contrasts With
- Panic-based error handling (`unwrap`, `expect`) -- suitable for prototypes, not released tools
- Custom error types -- more boilerplate than `anyhow` for application code

# Common Errors

- **Error**: Using `unwrap()` in released CLI code, causing panic messages with stack traces.
  **Correction**: Use `?` with `anyhow::Result` and `.context()` to produce clean error messages.

- **Error**: Forgetting `Ok(())` at the end of a `main` function that returns `Result`.
  **Correction**: The last expression must be `Ok(())` to indicate success. Without it, the function has no return value.

- **Error**: Using `?` in a function that returns `()` instead of `Result`.
  **Correction**: Change the function signature to return `Result<(), Box<dyn std::error::Error>>` or `anyhow::Result<()>`.

# Common Confusions

- **Confusion**: Thinking `?` and `unwrap()` are equivalent.
  **Clarification**: `unwrap()` panics on error (crashes the program). `?` returns the error to the caller, allowing graceful handling. They both extract the `Ok` value but differ completely on the error path.

- **Confusion**: Not understanding why `Box<dyn std::error::Error>` works as a universal error type.
  **Clarification**: `Box<dyn Error>` is a heap-allocated trait object. Any type implementing the `Error` trait can be boxed into it. The `?` operator automatically calls `.into()` to perform this conversion.

- **Confusion**: Thinking `anyhow` is needed for libraries.
  **Clarification**: `anyhow` is designed for applications where you want to add context and report errors to users. Libraries should use concrete error types (often via `thiserror`) so callers can match on specific error variants.

# Source Reference

Chapter 5 (Nicer error reporting) from the CLI Apps in Rust book. Covers Result basics, unwrap, match, the `?` operator, `Box<dyn Error>`, custom errors, and anyhow context chains.

# Verification Notes

- Result/match examples: Taken directly from Chapter 5 code blocks
- `?` operator explanation: Matches the chapter's description as "a shortcut for the `match` that `return`s in the error arm"
- `Box<dyn Error>` explanation: From the aside about how `?` converts error types
- anyhow usage: `anyhow = "1.0"` dependency and `Context` trait from the chapter
- Error output format: "Caused by:" chain output taken verbatim from the chapter
- Custom error: Example from the chapter's intermediate step before introducing anyhow
- Confidence: HIGH -- chapter provides a clear progression with explicit code examples
- Cross-references: All slugs reference cards in this extraction set
