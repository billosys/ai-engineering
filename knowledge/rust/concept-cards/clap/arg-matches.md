---
concept: ArgMatches
slug: arg-matches
category: builder-api
subcategory: argument-matching
tier: foundational
source: "Clap Documentation"
source_slug: clap
authors: "The Clap Contributors"
chapter: "clap-source-docs"
chapter_number: null
pdf_page: null
section: "Argument Matching (ArgMatches)"
extraction_confidence: high
aliases:
  - "ArgMatches"
  - "arg matches"
  - "parse results"
  - "match results"
prerequisites: []
extends: []
related:
  - command
  - arg
  - arg-action
  - value-parser
contrasts_with: []
answers_questions:
  - "How do I access parsed argument values after clap processes the command line?"
  - "What is ArgMatches and how do I use it?"
  - "How do I check if an argument was provided by the user vs. defaulted?"
---

# Quick Definition

`ArgMatches` is clap's container for parse results. It holds all the values, flags, and subcommand information extracted from the command line, and provides typed accessor methods like `get_one`, `get_many`, and `contains_id` for retrieving them.

# Core Definition

`ArgMatches` is the "container for parse results" that is "used to get information about the arguments that were supplied to the program at runtime by the user." New instances are obtained by calling the `Command::get_matches` family of methods. Once obtained, callers use typed accessor methods to extract individual values (`get_one::<T>`), collections of values (`get_many::<T>`), check for presence (`contains_id`), and determine where a value originated (`value_source`). The struct also provides subcommand matching via `subcommand`, `subcommand_matches`, and `subcommand_name` (Clap Documentation, Section 3: Argument Matching).

# Prerequisites

This is a foundational concept with no prerequisites within this source. Understanding `Command` and `Arg` from earlier sections provides context for how `ArgMatches` is produced, but `ArgMatches` itself is the entry point for working with parsed results.

# Key Properties

1. Produced by `Command::get_matches()`, `Command::try_get_matches()`, and related methods
2. Values are accessed via turbofish-typed methods: `get_one::<T>("name")` for single values, `get_many::<T>("name")` for multi-valued arguments
3. `get_one` returns `Option<&T>` — `None` when the argument was not provided and has no default
4. `contains_id("name")` checks whether an argument's value is present (including defaults)
5. `value_source("name")` returns a `ValueSource` enum indicating whether the value came from the command line, a default, or an environment variable
6. Subcommand results are accessed via `subcommand()` (returns name + matches tuple) or `subcommand_matches("name")`
7. The type parameter `T` in `get_one::<T>` must match the type produced by the argument's `ValueParser`

# Construction / Recognition

## To Obtain an ArgMatches Instance

1. Define a `Command` with `Arg` definitions
2. Call `cmd.get_matches()` (exits on error) or `cmd.try_get_matches()` (returns `Result`)
3. The returned `ArgMatches` struct contains all parsed values

## To Extract Values from ArgMatches

1. For a single required value: `matches.get_one::<T>("arg_id").unwrap()`
2. For an optional value: `if let Some(val) = matches.get_one::<T>("arg_id") { ... }`
3. For multi-valued arguments: `matches.get_many::<T>("arg_id")` returns an iterator
4. For flag presence: `matches.contains_id("arg_id")`
5. For value origin: `matches.value_source("arg_id")` returns `ValueSource::CommandLine`, `ValueSource::DefaultValue`, or `ValueSource::EnvVariable`

# Context & Application

`ArgMatches` is the primary interface between clap's parsing and your application logic. Every clap program follows the pattern: define arguments, parse, then inspect `ArgMatches` to drive behavior. It bridges the gap between raw command-line strings and typed Rust values.

**Typical contexts:**

- Retrieving typed values from command-line arguments in the builder API
- Dispatching to subcommand handlers based on `subcommand_matches`
- Checking whether optional arguments were provided
- Distinguishing user-supplied values from defaults via `ValueSource`

**Note:** When using the derive API, `ArgMatches` is used internally; the derive macros generate code that calls these same methods to populate your structs.

# Examples

**Example 1** (Section 3, ArgMatches struct doc): Basic usage showing `get_one` for both optional and required arguments:

```rust
let matches = Command::new("MyApp")
    .arg(Arg::new("out")
        .long("output")
        .required(true)
        .action(ArgAction::Set)
        .default_value("-"))
    .arg(Arg::new("cfg")
        .short('c')
        .action(ArgAction::Set))
    .get_matches();

if let Some(c) = matches.get_one::<String>("cfg") {
    println!("Value for -c: {c}");
}
println!("Value for --output: {}", matches.get_one::<String>("out").unwrap());
```

**Example 2** (Section 3, ArgMatches struct doc): Checking value source to distinguish user-provided from defaulted values:

```rust
if matches.contains_id("out") {
    if matches.value_source("out").expect("checked contains_id")
        == ValueSource::CommandLine
    {
        println!("`out` set by user");
    } else {
        println!("`out` is defaulted");
    }
}
```

# Relationships

## Builds Upon

- (none within this source — foundational)

## Enables

- **value-parser** — The type parameter in `get_one::<T>` must match the ValueParser's output type

## Related

- **command** — `ArgMatches` is produced by `Command::get_matches()`
- **arg** — `Arg` definitions determine what values are available in `ArgMatches`
- **arg-action** — `ArgAction` controls how values are stored in `ArgMatches`

## Contrasts With

- (none)

# Common Errors

- **Error**: Using `get_one::<String>("name")` when the argument's value parser produces a different type (e.g., `u16`).
  **Correction**: The type parameter in `get_one::<T>` must exactly match the type produced by the argument's `ValueParser`. Use `get_one::<u16>("port")` if the parser produces `u16`.

- **Error**: Calling `unwrap()` on `get_one` for an optional argument that was not provided.
  **Correction**: Only `unwrap()` on `get_one` for arguments marked `.required(true)` or that have `.default_value(...)`. Use `if let Some(val) = ...` for truly optional arguments.

# Common Confusions

- **Confusion**: Thinking `contains_id` means the user supplied the argument on the command line.
  **Clarification**: `contains_id` returns `true` if ANY value is present, including defaults. Use `value_source` to distinguish `CommandLine` from `DefaultValue`.

- **Confusion**: Expecting `get_one` to return an owned value.
  **Clarification**: `get_one::<T>` returns `Option<&T>` (a reference). For `Copy` types like `u16`, dereference with `*`. For `String`, you get `&String`.

# Source Reference

Section 3: Argument Matching (ArgMatches), from `repos/clap/clap_builder/src/parser/matches/arg_matches.rs`, lines 20-1078. Covers the `ArgMatches` struct definition, the Arguments impl block (line 76), the Subcommands impl block (line 865), and the Advanced impl block (line 1078).

# Verification Notes

- Definition: Directly quoted from the struct-level doc comment on `ArgMatches` (line 20)
- Key methods (`get_one`, `get_many`, `contains_id`, `value_source`): Documented in the struct's code examples
- The subcommand methods are listed in the "Subcommands" impl block heading
- Confidence: HIGH — the source provides an explicit definition with comprehensive code examples
- Cross-references: `command`, `arg`, `arg-action`, `value-parser` are planned or extracted by other agents
- Uncertainties: None
