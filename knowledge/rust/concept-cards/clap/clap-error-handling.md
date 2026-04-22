---
concept: Clap Error Handling
slug: clap-error-handling
category: cli-framework
subcategory: error-reporting
tier: intermediate

source: "Clap Documentation"
source_slug: clap
authors: "The Clap Contributors"
chapter: "clap-source-docs"
chapter_number: null
pdf_page: null
section: "Error Handling"

extraction_confidence: high

aliases:
  - "clap errors"
  - "clap Error type"
  - "clap ErrorKind"
  - "CLI error formatting"

prerequisites:
  - command
  - clap-builder-api

extends:
  - clap-validation

related:
  - arg-matches
  - clap-styling
  - help-generation

contrasts_with: []

answers_questions:
  - "How does clap report parsing errors to users?"
  - "What error types and kinds does clap provide?"
  - "How do I create custom errors in clap?"
  - "How do I customize the format of clap error messages?"
  - "What is the difference between RichFormatter and KindFormatter?"
---

## Quick Definition

Clap's error handling system provides a structured `Error` type with `ErrorKind` variants for categorizing parse failures, `ContextKind`/`ContextValue` for enriching error messages, and pluggable `ErrorFormatter` implementations (`RichFormatter` and `KindFormatter`) for controlling error output.

## Core Definition

The `clap::Error` struct represents command-line argument parsing errors. Each error carries an `ErrorKind` enum variant that classifies the error (e.g., `MissingRequiredArgument`, `ArgumentConflict`, `ValueValidation`, `UnknownArgument`) for programmatic processing. Errors are enriched with `ContextKind`/`ContextValue` pairs that provide semantic detail such as the invalid argument name, invalid value, suggested corrections, and valid values. The `ErrorFormatter` trait defines how errors render for display, with two built-in implementations: `RichFormatter` (default, follows the rustc diagnostic style guide) and `KindFormatter` (minimal, reports only the `ErrorKind` with no context). Errors automatically route to `stdout` (exit code 0) for help/version requests or `stderr` (exit code 2) for actual errors (Section 9: Error Handling, `clap_builder/src/error/`).

## Prerequisites

- **Command** -- Errors are generated during `Command` parsing and `Command::error` creates custom errors
- **Builder API** -- Understanding the builder API is needed to use `try_get_matches_from` for fallible parsing

## Key Properties

1. `Error::kind()` returns the `ErrorKind` for programmatic error handling
2. `ErrorKind` variants include `MissingRequiredArgument`, `ArgumentConflict`, `ValueValidation`, `UnknownArgument`, `WrongNumberOfValues`, and more
3. `Error::context()` returns an iterator of `(ContextKind, ContextValue)` pairs
4. `ContextKind` variants include `InvalidArg`, `InvalidValue`, `SuggestedValue`, `SuggestedCommand`, etc.
5. `ContextValue` variants include `String`, `Strings`, `StyledStr`, and `Number`
6. `Error::new(ErrorKind)` creates errors with pre-defined messages; prefer `Command::error` for generating errors
7. `Error::with_cmd(&cmd)` applies Command formatting (styling, usage) to an error
8. `Error::insert(ContextKind, ContextValue)` adds or replaces context information
9. `Error::apply::<F>()` switches the error formatter (e.g., from `RichFormatter` to `KindFormatter`)
10. `Error::exit()` prints to stderr (exit 2) for errors or stdout (exit 0) for help/version
11. `Error::render()` returns a `StyledStr` for custom display handling
12. `RichFormatter` follows the rustc diagnostic style guide with full context
13. `KindFormatter` reports only the `ErrorKind` with no context; consider removing the `error-context` feature when using it

## Construction / Recognition

### To Handle Parsing Errors Gracefully

1. Use `Command::try_get_matches_from(args)` instead of `get_matches_from`
2. Match on the `Result`: `Ok(matches)` for success, `Err(err)` for failure
3. Use `err.kind()` to determine the error category programmatically
4. Use `err.print()` to display the formatted error, or `err.exit()` to print and exit

### To Create Custom Errors

1. Call `Command::error(ErrorKind, message)` for simple custom errors (preferred)
2. Or use `Error::new(ErrorKind).with_cmd(&cmd)` for more control
3. Add context with `err.insert(ContextKind::InvalidArg, ContextValue::String(...))`
4. Print or exit with `err.print()` or `err.exit()`

### To Customize Error Formatting

1. Use `err.apply::<KindFormatter>()` to switch to minimal formatting
2. Or implement the `ErrorFormatter` trait with a custom `format_error` method
3. Apply via `.map_err(|e| e.apply::<MyFormatter>())`

## Context & Application

Error handling is essential for CLI applications that need to provide helpful feedback to users. Clap's structured error system serves two audiences: end users who see formatted error messages with suggestions, and application developers who can programmatically inspect `ErrorKind` to take different actions. The `try_get_matches_from` pattern is critical for testing (avoiding process exit) and for applications that need custom error recovery. The `ContextKind`/`ContextValue` system allows building rich error messages that include the offending argument, the invalid value, and suggestions for valid alternatives. Custom errors via `Command::error` are used for post-parsing validation that cannot be expressed through declarative constraints.

## Examples

**Example 1** (Section 9, Error::new): Creating a custom error with context:
```rust
let cmd = clap::Command::new("prog");

let mut err = clap::Error::new(ErrorKind::ValueValidation)
    .with_cmd(&cmd);
err.insert(ContextKind::InvalidArg, ContextValue::String("--foo".to_owned()));
err.insert(ContextKind::InvalidValue, ContextValue::String("bar".to_owned()));

err.print();
```

**Example 2** (Section 9, Error::apply): Switching to KindFormatter for minimal output:
```rust
let cmd = Command::new("foo")
    .arg(Arg::new("input").required(true));
let matches = cmd
    .try_get_matches_from(["foo", "input.txt"])
    .map_err(|e| e.apply::<KindFormatter>())
    .unwrap_or_else(|e| e.exit());
```

**Example 3** (Section 9, Error::print): Basic error handling with print:
```rust
match Command::new("Command").try_get_matches() {
    Ok(matches) => {
        // do_something
    },
    Err(err) => {
        err.print().expect("Error writing Error");
        // do_something
    },
};
```

**Example 4** (Section 9, Error::render): Rendering error to StyledStr:
```rust
match Command::new("Command").try_get_matches() {
    Ok(matches) => { /* ... */ },
    Err(err) => {
        let err = err.render();
        println!("{err}");
    },
};
```

## Relationships

### Builds Upon

- **Command** -- Errors are produced by Command parsing and `Command::error` creates custom errors
- **clap-validation** -- Validation constraint violations produce specific Error/ErrorKind values

### Enables

- **clap-testing** -- Testing CLIs requires `try_get_matches_from` and Error inspection

### Related

- **clap-styling** -- `StyledStr` and `Styles` affect error message appearance
- **help-generation** -- Help/version "errors" route to stdout with exit code 0
- **ArgMatches** -- `MatchesError` represents violations of ArgMatches assumptions (separate from parse errors)

## Common Errors

- **Error**: Using `get_matches_from` instead of `try_get_matches_from` in tests or recoverable contexts
  **Correction**: `get_matches_from` calls `process::exit` on failure; use `try_get_matches_from` to get a `Result`

- **Error**: Forgetting to call `.with_cmd(&cmd)` on manually created errors
  **Correction**: Without `.with_cmd`, the error lacks formatting context (styling, usage string); always attach the Command

- **Error**: Using `Error::raw` without later calling `Error::format`
  **Correction**: `Error::raw` creates an unformatted error; it must be formatted with `Error::format` at a point where the `Command` is accessible

## Common Confusions

- **Confusion**: Thinking all errors go to stderr
  **Clarification**: Help and version "errors" are printed to stdout with exit code 0; only actual parsing errors go to stderr with exit code 2

- **Confusion**: Confusing `Error` (parse error) with `MatchesError` (ArgMatches usage error)
  **Clarification**: `Error` represents parse failures; `MatchesError` represents violations of `ArgMatches` assumptions (e.g., wrong type retrieval) and is a separate enum

- **Confusion**: Thinking `KindFormatter` and `RichFormatter` produce the same information at different verbosity levels
  **Clarification**: `KindFormatter` includes no context at all (no argument names, no values, no suggestions); `RichFormatter` follows the rustc diagnostic style with full context

## Source Reference

Clap Documentation, Section 9: "Error Handling" (clap-source-docs). Source files: `clap_builder/src/error/mod.rs` (Error struct, Result type alias), `clap_builder/src/error/kind.rs` (ErrorKind enum), `clap_builder/src/error/context.rs` (ContextKind, ContextValue), `clap_builder/src/error/format.rs` (ErrorFormatter trait, KindFormatter, RichFormatter), `clap_builder/src/parser/error.rs` (MatchesError).

## Verification Notes

- Definition: Synthesized from module-level docs and individual type/method documentation in Section 9
- Key Properties: All items directly stated in source documentation
- Examples: All four examples taken directly from source code examples
- Confidence: HIGH -- Section 9 provides extensive explicit documentation with clear type definitions, method signatures, and code examples
- Cross-references: `command`, `clap-builder-api`, `clap-validation` verified against other agents' planned extractions
- Uncertainties: None; the error handling API is thoroughly documented
