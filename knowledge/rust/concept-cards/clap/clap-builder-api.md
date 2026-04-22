---
# === CORE IDENTIFICATION ===
concept: Clap Builder API
slug: clap-builder-api

# === CLASSIFICATION ===
category: builder-api
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Clap Documentation"
source_slug: clap
authors: "The Clap Contributors"
chapter: "clap-source-docs"
chapter_number: null
pdf_page: null
section: "Core Concepts - Command"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - builder pattern
  - builder API
  - clap builder
  - "clap_builder"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clap-crate
extends: []
related:
  - command
  - arg
  - arg-group
  - arg-matches
  - clap-derive-api
contrasts_with:
  - clap-derive-api

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the clap builder API?"
  - "How do I define a CLI using clap's builder pattern?"
  - "What is the workflow for building and parsing with the builder API?"
  - "When should I use the builder API vs the derive API?"
---

# Quick Definition

The clap builder API is an imperative, method-chaining approach to defining CLI interfaces using `Command::new()`, `.arg()`, `.subcommand()`, and related methods, culminating in a `get_matches()` call that parses arguments and returns `ArgMatches`.

# Core Definition

The builder API is one of clap's two main approaches to CLI definition (the other being the derive API). It is centered on the `Command` struct, which uses the builder pattern: nearly every configuration method consumes and returns `Self`, enabling fluent method chaining. The API is provided by the `clap_builder` crate, which `clap` re-exports via `pub use clap_builder::*` (clap.md, Re-exports section).

The builder API workflow is: construct a `Command`, configure it with arguments and settings via chained methods, then call a `get_matches` variant to parse. The result is an `ArgMatches` value from which parsed argument values are extracted by name.

# Prerequisites

- **clap-crate** -- The builder API is part of the clap crate; understanding the crate's role and installation is needed.

# Key Properties

1. Uses the builder pattern with method chaining on `Command`
2. Core types: `Command` (CLI definition), `Arg` (argument definition), `ArgGroup` (argument grouping), `ArgMatches` (parsed results)
3. All configuration is explicit through method calls -- no macros or annotations
4. Arguments are referenced by string ID in `ArgMatches` (e.g., `matches.get_one::<String>("name")`)
5. The `clap_builder` crate is the underlying implementation; `clap` re-exports it
6. Can be combined with the derive API via `CommandFactory::command()`
7. Provides the `arg!()` macro as a shorthand for common argument patterns
8. Supports runtime-dynamic CLI definitions (arguments determined at runtime)

# Construction / Recognition

## Builder API Workflow:
1. Create a command: `Command::new("myapp")`
2. Set metadata: `.version("1.0")`, `.author(...)`, `.about(...)`
3. Add arguments: `.arg(Arg::new("input").required(true))` or `.arg(arg!(-v --verbose))`
4. Add subcommands: `.subcommand(Command::new("sub")...)`
5. Add groups: `.group(ArgGroup::new("grp")...)`
6. Configure settings: `.color(...)`, `.styles(...)`, `.help_template(...)`
7. Parse: `let matches = cmd.get_matches();`
8. Extract values: `matches.get_one::<String>("input")`

## To Recognize Builder API Usage:
1. Imports from `clap::{Command, Arg}` (not `clap::Parser`)
2. `Command::new(...)` as the starting point
3. Chain of `.arg()`, `.subcommand()`, `.version()` calls
4. `get_matches()` or `try_get_matches()` to trigger parsing
5. `ArgMatches` used to retrieve values by string name

# Context & Application

The builder API is clap's original and most flexible approach. It is preferred when:
- CLI structure needs to be determined at runtime (dynamic arguments)
- Maximum control over every aspect of the CLI is needed
- The derive API's attributes are insufficient for a particular configuration
- Building tools that programmatically generate CLIs

The derive API is generally preferred for static CLI definitions because it reduces boilerplate and provides compile-time type safety for argument access. However, the builder API remains essential for dynamic use cases and is the foundation that the derive API generates code into.

**Quick links from the source:** Builder [tutorial] and [reference (Command)].

# Examples

**Example 1** (command.rs, line 36): Complete builder API pattern:
```rust
use clap::{Command, Arg};

let m = Command::new("My Program")
    .author("Me, me@mail.com")
    .version("1.0.2")
    .about("Explains in brief what the program does")
    .arg(Arg::new("in_file"))
    .after_help("Longer explanation to appear after the options")
    .get_matches();
```

**Example 2** (command.rs, line 148): Using the `arg!` macro shorthand:
```rust
use clap::{Command, arg, Arg};

Command::new("myprog")
    .arg(
        Arg::new("debug")
            .short('d')
            .help("turns on debugging mode")
    )
    .arg(
        arg!(-c --config <CONFIG> "Optionally sets a config file to use")
    );
```

**Example 3** (command.rs, line 191): Adding multiple arguments at once:
```rust
use clap::{Command, arg, Arg};

Command::new("myprog")
    .args([
        arg!(-d --debug "turns on debugging info"),
        Arg::new("input").help("the input file to use")
    ]);
```

# Relationships

## Enables
- **command** -- the central type in the builder API
- **arg** -- argument definitions composed into Commands
- **arg-group** -- argument groupings for mutual exclusion and co-occurrence
- **arg-matches** -- the parse result type

## Related
- **clap-crate** -- the builder API is provided by the clap crate
- **help-generation** -- auto-generated from builder API definitions
- **command-settings** -- configured through builder methods

## Contrasts With
- **clap-derive-api** -- the alternative annotation-based approach; derive generates builder API code under the hood

# Common Errors

- **Error**: Using string argument names in `get_one`/`get_many` that don't match the `Arg::new("name")` ID.
  **Correction**: Argument lookup is by the exact string passed to `Arg::new()`. Typos cause `None` results or panics.

- **Error**: Forgetting to specify `.action()` on arguments, leading to unexpected default behavior.
  **Correction**: Clap defaults to `ArgAction::Set` for arguments with values and `ArgAction::SetTrue` for flags. Be explicit when the default doesn't match intent.

# Common Confusions

- **Confusion**: Thinking the builder and derive APIs produce different parse results.
  **Clarification**: Both produce `ArgMatches` under the hood. The derive API adds a typed layer on top via `FromArgMatches`, but the underlying mechanism is identical.

- **Confusion**: Believing the `arg!()` macro is the derive API.
  **Clarification**: The `arg!()` macro is a builder API convenience for creating `Arg` instances with a compact syntax. It is unrelated to `#[derive(Parser)]`.

- **Confusion**: Thinking `clap_builder` is a separate, optional crate.
  **Clarification**: `clap_builder` is the core implementation. The `clap` crate re-exports everything from it. Most users should depend on `clap`, not `clap_builder` directly.

# Source Reference

Section 1: Core Concepts - Command, from `clap_builder/src/builder/command.rs`. The entire Command struct and its impl blocks constitute the builder API. Crate-level overview in `clap.md` (Module: clap, Quick Links, Re-exports).

# Verification Notes

- Builder pattern: Evident from every method returning `Self` in the Command impl blocks
- Re-export relationship: Explicitly stated in clap.md "Re-export `clap_builder::*`"
- Quick Links: Directly from source referencing builder tutorial and reference
- Confidence: HIGH -- the builder API is the explicitly documented primary API with extensive examples
- Cross-references: `arg`, `arg-group`, `arg-matches` are in Agent 2/3 scope; `clap-derive-api` in Agent 4
