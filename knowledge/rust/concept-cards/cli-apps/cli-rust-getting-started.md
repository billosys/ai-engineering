---
# === CORE IDENTIFICATION ===
concept: CLI Apps in Rust - Getting Started
slug: cli-rust-getting-started

# === CLASSIFICATION ===
category: cli-development
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Command Line Apps in Rust"
source_slug: cli-apps
authors: "The Rust CLI Working Group"
chapter: "01-getting-started.md"
chapter_number: 1
pdf_page: null
section: "Getting Started, Project Setup, First Implementation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Rust CLI getting started"
  - "grrs tutorial"
  - "Rust command-line apps"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - cli-argument-parsing
  - cli-error-reporting
  - cli-output
  - clap-crate
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why is Rust a good fit for writing command-line applications?"
  - "How do you set up a new Rust CLI project with cargo?"
  - "How do you write a basic grep-like tool in Rust?"
  - "What does a minimal Rust CLI implementation look like?"
---

# Quick Definition

Rust is well-suited for CLI applications because of its static compilation, speed, great tooling, and growing ecosystem. A new CLI project is scaffolded with `cargo new`, and a basic file-searching tool can be implemented in a few lines using `std::fs::read_to_string` and string matching.

# Core Definition

The "Command Line Apps in Rust" book teaches CLI development through building `grrs` (pronounced "grass"), a small `grep` clone that takes a search pattern and file path, then prints matching lines. The tutorial covers the full lifecycle: project setup with `cargo new`, argument parsing, file reading, error handling, output formatting, testing, and packaging. Rust's advantages for CLI tools include: programs are small and portable, compile to native binaries, start quickly with no runtime overhead, and benefit from Cargo's dependency management and Rust's safety guarantees. The book uses a progressive approach where each chapter adds a new concern to the working tool.

# Prerequisites

This is a foundational concept. Familiarity with basic Rust syntax and a working Rust installation (via `rustup`) are assumed.

# Key Properties

1. CLI projects are created with `cargo new <name>`, producing `Cargo.toml` and `src/main.rs`
2. `cargo run` compiles and runs the project; arguments are passed after `--` (e.g., `cargo run -- pattern file.txt`)
3. `Cargo.toml` holds project metadata and dependency declarations
4. `src/main.rs` contains the `fn main()` entry point for binary crates
5. File contents are read with `std::fs::read_to_string()`, which returns a `Result`
6. `.expect("message")` is a quick way to unwrap a `Result` or panic with a message
7. Line-by-line searching uses `.lines()` iterator and `.contains()` for string matching
8. Rust compiles to statically-linked native binaries with no runtime dependencies
9. The standard library's `std::env::args()` provides raw access to CLI arguments

# Construction / Recognition

## To Create a New CLI Project:
1. Run `cargo new grrs` to scaffold the project
2. Verify with `cd grrs && cargo run` -- should print "Hello, world!"
3. Add dependencies to `Cargo.toml` under `[dependencies]`
4. Implement logic in `src/main.rs`

## Basic grep Implementation Pattern:
1. Parse command-line arguments (pattern and file path)
2. Read the file contents into a string
3. Iterate over lines, checking each for the search pattern
4. Print matching lines to stdout

# Context & Application

This tutorial demonstrates the pragmatic approach to Rust CLI development: start with a working prototype, then iteratively improve error handling, output, testing, and distribution. The `grrs` tool mirrors real-world CLI patterns -- it accepts positional arguments, reads files, filters content, and produces line-oriented output. This foundation applies to any CLI tool from simple utilities to complex multi-subcommand applications.

**When to Use Rust for CLIs:**
- Tools that need fast startup and execution (no VM/interpreter)
- Cross-platform utilities that should ship as single binaries
- Programs where type safety and memory safety prevent subtle bugs
- Tools distributed to users who may not have Rust installed (via compiled binaries)

# Examples

**Example 1** (Ch 2): Creating a new CLI project:
```console
$ cargo new grrs
     Created binary (application) `grrs` package
$ cd grrs/
$ cargo run
   Compiling grrs v0.1.0 (/Users/pascal/code/grrs)
    Finished dev [unoptimized + debuginfo] target(s) in 0.70s
     Running `target/debug/grrs`
Hello, world!
```

**Example 2** (Ch 4): First implementation of the grep logic:
```rust,ignore
// After parsing args into an `args` struct with `pattern` and `path` fields:
let content = std::fs::read_to_string(&args.path)
    .expect("could not read file");

for line in content.lines() {
    if line.contains(&args.pattern) {
        println!("{}", line);
    }
}
```

**Example 3** (Ch 1): Expected CLI usage:
```console
$ cat test.txt
foo: 10
bar: 20
baz: 30
$ grrs foo test.txt
foo: 10
```

# Relationships

## Enables
- **cli-argument-parsing** -- structured argument handling replaces manual `std::env::args()`
- **cli-error-reporting** -- proper error handling replaces `.expect()` calls
- **cli-output** -- output control replaces bare `println!`

## Related
- **clap-crate** -- the recommended library for argument parsing in Rust CLIs
- **cli-testing** -- testing strategies for the tool built in this tutorial
- **cli-packaging** -- distributing the finished CLI tool

# Common Errors

- **Error**: Running `cargo run pattern file.txt` without `--` separator.
  **Correction**: Use `cargo run -- pattern file.txt`. The `--` tells cargo that subsequent arguments belong to the program, not to cargo itself.

- **Error**: Using `.expect()` in production code for file reading, producing panic messages instead of user-friendly errors.
  **Correction**: Use `Result` propagation with `?` and the `anyhow` crate for contextual error messages (covered in the error reporting chapter).

- **Error**: Reading entire large files into memory with `read_to_string()`.
  **Correction**: Use `BufReader` for line-by-line reading to handle large files without excessive memory use.

# Common Confusions

- **Confusion**: Thinking `cargo new` creates a library by default.
  **Clarification**: `cargo new <name>` creates a binary (application) crate with `src/main.rs`. Use `cargo new --lib <name>` to create a library with `src/lib.rs`.

- **Confusion**: Assuming Rust CLIs need a complex framework to get started.
  **Clarification**: A working CLI tool can be built with just the standard library. Crates like `clap` and `anyhow` are added incrementally to improve the developer and user experience.

# Source Reference

Chapters 1 (Command line apps in Rust / Learning Rust by Writing a Command Line App in 15 Minutes), 2 (Project setup), and 4 (First implementation of grrs) from the CLI Apps in Rust book by The Rust CLI Working Group.

# Verification Notes

- Definition: Derived from the book's introduction stating Rust is "a great fit for writing command line applications"
- Project setup: `cargo new grrs` example taken directly from Chapter 2
- Implementation: File reading and line matching code from Chapter 4
- `.expect()` caveat: Explicitly noted in Chapter 4 as "not very pretty" with reference to the error chapter
- `BufReader` suggestion: Exercise from Chapter 4
- Confidence: HIGH -- content closely follows the source tutorial structure
- Cross-references: All slugs reference cards in this extraction set or the clap source set
