---
# === CORE IDENTIFICATION ===
concept: Parser Derive Macro
slug: parser-derive

# === CLASSIFICATION ===
category: derive-api
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Clap Documentation"
source_slug: clap
authors: "The Clap Contributors"
chapter: "clap-source-docs"
chapter_number: null
pdf_page: null
section: "Derive API - Parser"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "derive(Parser)"
  - "#[derive(Parser)]"
  - "Parser trait"
  - "Parser macro"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clap-derive-api
  - command
extends: []
related:
  - command-factory-trait
  - arg-matches
  - subcommand-derive
  - args-derive
  - derive-attributes
contrasts_with:
  - clap-builder-api

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use #[derive(Parser)] to define a CLI?"
  - "What traits does #[derive(Parser)] implement?"
  - "What methods does the Parser trait provide?"
  - "How do I parse arguments from the environment or a custom iterator?"
---

# Quick Definition

`#[derive(Parser)]` is the main entry-point derive macro in clap that generates a complete CLI parser from a Rust struct, implementing the `Parser`, `CommandFactory`, and `FromArgMatches` traits to handle command building, argument parsing, and type-safe result extraction in one step.

# Core Definition

The `Parser` trait is "the primary one-stop-shop trait used to create an instance of a `clap` `Command`, conduct the parsing, and turn the resulting `ArgMatches` back into concrete instance of the user struct." It is "primarily a convenience on top of `FromArgMatches` + `CommandFactory` which uses those two underlying traits to build the two fundamental functions `parse` which uses the `std::env::args_os` iterator, and `parse_from` which allows the consumer to supply the iterator (along with fallible options for each)" (Trait: Parser, derive.rs:10). Deriving `Parser` on a struct generates implementations of `Parser`, `CommandFactory`, and `FromArgMatches`. The `Parser` procedural macro accepts helper attributes `#[clap]`, `#[structopt]`, `#[command]`, `#[arg]`, and `#[group]` (clap-derive.md, Procedural Macro Parser).

# Prerequisites

- **clap-derive-api** -- Understanding the derive approach is needed to know why and when to use `#[derive(Parser)]`
- **command** -- The `Parser` trait builds on the `Command` struct, so understanding `Command` helps explain what `Parser` generates

# Key Properties

1. Applied to structs (not enums) to define the top-level CLI entry point
2. Automatically implements three traits: `Parser`, `CommandFactory`, and `FromArgMatches`
3. Provides `parse()` -- parses from `std::env::args_os()`, exits on error
4. Provides `try_parse()` -- parses from `std::env::args_os()`, returns `Err` on error
5. Provides `parse_from(iter)` -- parses from a custom iterator, exits on error
6. Provides `try_parse_from(iter)` -- parses from a custom iterator, returns `Err` on error
7. Provides `update_from(iter)` -- updates an existing instance from an iterator (for REPL-like scenarios)
8. Provides `try_update_from(iter)` -- fallible version of `update_from`
9. The `update_from` family assumes all required fields are already provided; user-supplied args only modify specified fields
10. Requires the `derive` feature flag

# Construction / Recognition

## To Define a Parser:
1. Import the trait: `use clap::Parser;`
2. Annotate a struct with `#[derive(Parser)]` (optionally also `Debug`, `Clone`, etc.)
3. Add `#[command(...)]` for command-level settings (version, about, author, name)
4. Define fields for arguments with `#[arg(...)]` attributes
5. Use doc comments on the struct for the command description and on fields for argument help text

## To Parse Arguments:
1. Call `YourStruct::parse()` in `main()` for the standard case (exits on error with help)
2. Call `YourStruct::try_parse()` when you need to handle errors programmatically
3. Call `YourStruct::parse_from(["app", "--flag", "value"])` for testing or custom input
4. Call `instance.update_from(["app", "--flag", "new_value"])` to update an existing parsed instance

## To Recognize:
1. Look for `#[derive(Parser)]` on a struct definition
2. Check for `use clap::Parser;` in imports
3. Look for `::parse()` or `::try_parse()` calls on the struct type

# Context & Application

`#[derive(Parser)]` is the recommended starting point for any CLI application using clap's derive API. It is the most commonly used derive macro and the first one developers encounter in clap's tutorials and documentation.

**Typical usage patterns:**
- Simple CLI tools: derive `Parser` on a single struct, call `.parse()` in `main()`
- Tools with subcommands: derive `Parser` on the top-level struct, add an enum field with `#[command(subcommand)]`
- Testing: use `parse_from` to test CLI parsing without modifying environment arguments
- REPLs and interactive tools: use `update_from` to re-parse arguments on an existing instance across multiple iterations

**Relationship to underlying traits:** `Parser` composes `CommandFactory` (which builds the `Command`) and `FromArgMatches` (which converts `ArgMatches` into the struct). When you need access to the underlying `Command` for builder-style modifications, use `<YourStruct as CommandFactory>::command()`.

# Examples

**Example 1** (clap.md, Module: clap): Standard Parser usage:
```rust
use clap::Parser;

/// Simple program to greet a person
#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
struct Args {
    /// Name of the person to greet
    #[arg(short, long)]
    name: String,

    /// Number of times to greet
    #[arg(short, long, default_value_t = 1)]
    count: u8,
}

fn main() {
    let args = Args::parse();
    for _ in 0..args.count {
        println!("Hello {}!", args.name);
    }
}
```

**Example 2** (Trait: Parser, derive.rs): The six methods provided by the Parser trait:
- `Parser::parse()` -- parse from env, exit on error
- `Parser::try_parse()` -- parse from env, return Result
- `Parser::parse_from(iter)` -- parse from iterator, exit on error
- `Parser::try_parse_from(iter)` -- parse from iterator, return Result
- `Parser::update_from(&mut self, iter)` -- update existing instance, exit on error
- `Parser::try_update_from(&mut self, iter)` -- update existing instance, return Result

# Relationships

## Builds Upon
- **command** -- `Parser` generates a `Command` internally via the `CommandFactory` trait
- **arg-matches** -- `Parser` converts `ArgMatches` into the user struct via `FromArgMatches`

## Enables
- **subcommand-derive** -- subcommand enums are used within a `Parser`-derived struct
- **args-derive** -- argument groups can be flattened into a `Parser`-derived struct

## Related
- **command-factory-trait** -- derived alongside `Parser`, provides access to the underlying `Command`
- **derive-attributes** -- `#[command(...)]` and `#[arg(...)]` configure the generated parser

## Contrasts With
- **clap-builder-api** -- the manual approach using `Command::new()` and `Arg::new()` method chains

# Common Errors

- **Error**: Deriving `Parser` on an enum, which causes a compilation error.
  **Correction**: Use `#[derive(Subcommand)]` for enums. `Parser` is only for structs.

- **Error**: Calling `.parse()` in tests, which reads from `std::env::args_os()` and picks up test runner arguments.
  **Correction**: Use `YourStruct::parse_from(["test", "--arg", "value"])` in tests to supply a controlled argument list.

- **Error**: Using `parse()` when you need to display a custom error or recover from parse failures.
  **Correction**: Use `try_parse()` or `try_parse_from()` to get a `Result` that you can match on and handle gracefully.

# Common Confusions

- **Confusion**: Thinking `Parser` is a separate parsing engine from the builder API.
  **Clarification**: `Parser` is a convenience trait layered on `CommandFactory` + `FromArgMatches`. It generates the same `Command` and `ArgMatches` pipeline as the builder API.

- **Confusion**: Assuming `update_from` re-parses all arguments from scratch.
  **Clarification**: `update_from` assumes all required fields already have values. It only modifies fields corresponding to arguments the user provides in the new input, making it suitable for REPL-style re-parsing.

- **Confusion**: Thinking the `#[structopt]` helper attribute listed in the macro is the recommended syntax.
  **Clarification**: `#[structopt]` is retained for backward compatibility with the structopt crate migration. Use `#[command(...)]` and `#[arg(...)]` for new code.

# Source Reference

Trait: Parser (derive.rs:10) and its methods (derive.rs:30-100) in clap-source-docs.md, Section 6 "Derive API - Parser" (line 19823); Procedural Macro `Parser` in clap-derive.md; Module: clap example from clap.md; Derive Tutorial from `repos/clap/src/_derive/_tutorial.rs`.

# Verification Notes

- Definition: Direct quotation from Trait: Parser documentation at derive.rs:10
- "far less verbose" description quoted from clap_derive proc macro docs and Section 6
- Method list (parse, try_parse, parse_from, try_parse_from, update_from, try_update_from) enumerated explicitly in source
- Helper attributes list from clap-derive.md Procedural Macro Parser definition
- Confidence: HIGH -- the Parser trait has extensive, explicit documentation with clear trait hierarchy
- Cross-references: All slugs verified against existing cards and planned extractions
