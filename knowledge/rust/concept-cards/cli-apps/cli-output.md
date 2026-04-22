---
# === CORE IDENTIFICATION ===
concept: CLI Output
slug: cli-output

# === CLASSIFICATION ===
category: cli-development
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Command Line Apps in Rust"
source_slug: cli-apps
authors: "The Rust CLI Working Group"
chapter: "06-output.md"
chapter_number: 6
pdf_page: null
section: "Output"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "CLI output handling"
  - "stdout and stderr in Rust"
  - "Rust CLI logging and progress"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cli-rust-getting-started
  - cli-error-reporting
extends: []
related:
  - cli-signal-handling
  - cli-human-communication
  - cli-machine-communication
  - cli-testing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you write to stdout vs stderr in Rust?"
  - "How do you improve println! performance for high-throughput output?"
  - "How do you add progress bars to a Rust CLI?"
  - "How do you add structured logging to a Rust CLI?"
---

# Quick Definition

CLI output in Rust uses `println!` for stdout and `eprintln!` for stderr. Performance-sensitive output benefits from `BufWriter` and explicit `stdout().lock()`. The `log` + `env_logger` crates provide leveled logging, while `indicatif` adds progress bars and spinners.

# Core Definition

The chapter covers four output concerns for CLI applications:

1. **stdout vs stderr**: `println!` writes to stdout (program data), `eprintln!` writes to stderr (errors and diagnostics). This separation allows piping program output to files or other programs while errors remain visible.

2. **Print formatting**: The `{}` placeholder uses the `Display` trait for human-readable output; `{:?}` uses `Debug` for developer-oriented output. Custom types need `#[derive(Debug)]` for debug printing.

3. **Performance**: `println!` flushes on every call, which is slow in loops. Two optimizations: wrap stdout in a `BufWriter` (buffers up to 8 kB), and acquire a `stdout().lock()` to avoid repeated lock/unlock overhead. Both use `writeln!` instead of `println!`.

4. **Logging**: The `log` crate provides level-based macros (`error!`, `warn!`, `info!`, `debug!`, `trace!`) and `env_logger` routes them to stderr, controlled by the `RUST_LOG` environment variable. The `clap-verbosity-flag` crate integrates `--verbose` flags with log levels.

5. **Progress indicators**: The `indicatif` crate provides progress bars and spinners for long-running operations.

# Prerequisites

- **cli-rust-getting-started**: Basic `println!` usage in a CLI context
- **cli-error-reporting**: Understanding of why errors should go to stderr

# Key Properties

1. `println!` writes to stdout; `eprintln!` writes to stderr
2. stdout is for program output; stderr is for errors and diagnostics
3. `{}` uses `Display` trait; `{:?}` uses `Debug` trait; `#[derive(Debug)]` enables debug printing
4. `println!` flushes every call -- slow in tight loops
5. `BufWriter::new(stdout())` buffers output, flushing at 8 kB by default
6. `stdout().lock()` acquires a lock once instead of per-write
7. `writeln!(handle, "fmt", args)` writes to any `Write` implementor
8. `log` crate defines five levels: error, warn, info, debug, trace
9. `env_logger` reads `RUST_LOG` environment variable for log filtering
10. `indicatif` provides `ProgressBar` with customizable styles
11. Escape codes should be handled via crates (e.g., `ansi_term`), not manually

# Construction / Recognition

## To Add Logging:
1. Add `log = "0.4"` and `env_logger = "0.9"` to `[dependencies]`
2. Call `env_logger::init();` early in `main()`
3. Use `log::info!("message")`, `log::warn!("message")`, etc.
4. Run with `RUST_LOG=info cargo run` to see info-level and above

## To Add Progress Bars:
1. Add `indicatif = "0.17"` to `[dependencies]`
2. Create a `ProgressBar::new(total)` with the total count
3. Call `pb.inc(1)` in each iteration
4. Call `pb.finish_with_message("done")` when complete

## To Optimize Output Performance:
1. Get a locked handle: `let mut handle = io::stdout().lock();`
2. Optionally wrap in BufWriter: `let mut handle = BufWriter::new(io::stdout());`
3. Use `writeln!(handle, "format", args)` instead of `println!`

# Context & Application

Output handling is often overlooked in CLI development but significantly impacts usability. The stdout/stderr separation is a Unix convention that enables shell pipelines -- if a tool writes errors to stdout, piping its output corrupts the receiving program's input. Performance matters when a CLI processes millions of lines; the difference between `println!` and buffered `writeln!` can be orders of magnitude. Logging supports both debugging during development and troubleshooting in production. Progress bars transform a silent long-running tool into one that communicates its status.

**Tip from the book**: "Experience has shown that even mildly useful CLI programs can end up being used for years to come. If your application doesn't work and someone needs to figure out why, being able to pass `--verbose` to get additional log output can make the difference between minutes and hours of debugging."

# Examples

**Example 1** (Ch 6): stdout vs stderr:
```rust
println!("This is information");
eprintln!("This is an error! :(");
```

**Example 2** (Ch 6): Display vs Debug formatting:
```rust
let xs = vec![1, 2, 3];
println!("The list is: {:?}", xs);
// Output: The list is: [1, 2, 3]
```

**Example 3** (Ch 6): High-performance buffered output:
```rust
use std::io::{self, Write};

let stdout = io::stdout();
let mut handle = io::BufWriter::new(stdout);
writeln!(handle, "foo: {}", 42);
```

**Example 4** (Ch 6): Locking stdout to avoid per-write overhead:
```rust
use std::io::{self, Write};

let stdout = io::stdout();
let mut handle = stdout.lock();
writeln!(handle, "foo: {}", 42);
```

**Example 5** (Ch 6): Logging with env_logger:
```rust,ignore
use log::{info, warn};

fn main() {
    env_logger::init();
    info!("starting up");
    warn!("oops, nothing implemented!");
}
```

Run with: `RUST_LOG=info cargo run`

Output:
```text
[2018-11-30T20:25:52Z INFO  output_log] starting up
[2018-11-30T20:25:52Z WARN  output_log] oops, nothing implemented!
```

# Relationships

## Enables
- **cli-testing** -- testable output requires `impl Write` abstraction (covered in the testing chapter)
- **cli-human-communication** -- broader patterns for human-friendly CLI output
- **cli-machine-communication** -- structured output formats for programmatic consumption

## Related
- **cli-error-reporting** -- errors should be written to stderr via `eprintln!`
- **cli-signal-handling** -- signal handling interacts with output (e.g., cleaning up progress bars)
- **clap-verbosity-flag** -- integrates `--verbose` flags with the `log` crate

# Common Errors

- **Error**: Writing error messages to stdout with `println!` instead of stderr.
  **Correction**: Use `eprintln!("Error: {}", msg)` for all error and diagnostic output. This preserves clean stdout for piping.

- **Error**: Using `println!` in a loop that processes millions of lines, causing slow performance.
  **Correction**: Wrap stdout in `BufWriter` and/or acquire a lock, then use `writeln!` for each line.

- **Error**: Manually writing ANSI escape codes for colors.
  **Correction**: Use a crate like `ansi_term` to handle escape codes safely. Manual codes can leave the terminal in a broken state.

# Common Confusions

- **Confusion**: Thinking `BufWriter` and `stdout().lock()` are alternatives -- one or the other.
  **Clarification**: They can be combined. `BufWriter::new(stdout().lock())` both buffers writes and avoids repeated lock acquisition.

- **Confusion**: Assuming `RUST_LOG` only controls your application's logs.
  **Clarification**: `RUST_LOG` also controls log output from dependencies that use the `log` crate. You can filter by module: `RUST_LOG=my_app=debug,hyper=warn`.

- **Confusion**: Thinking progress bars and log output can coexist without coordination.
  **Clarification**: Progress bars redraw in-place using terminal escape codes. Intermixed `println!` or log output will corrupt the progress bar display. The `indicatif` crate provides methods to handle this (e.g., `ProgressBar::println`).

# Source Reference

Chapter 6 (Output) from the CLI Apps in Rust book. Covers println/eprintln, Display/Debug formatting, output performance (BufWriter, locking), progress bars (indicatif), and logging (log + env_logger).

# Verification Notes

- stdout/stderr distinction: Directly from the "Printing errors" section
- BufWriter and lock examples: Code taken verbatim from the "A note on printing performance" section
- env_logger example: Code and console output from the "Logging" section
- RUST_LOG usage: Explained in the logging section with platform-specific examples
- clap-verbosity-flag tip: Quoted from the aside at the end of the chapter
- indicatif mention: From the "Showing a progress bar" section with crate reference
- Confidence: HIGH -- all code examples and patterns directly from the source
- Cross-references: cli-signal-handling, cli-human-communication, cli-machine-communication reference Agent B cards
