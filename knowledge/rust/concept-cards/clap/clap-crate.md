---
# === CORE IDENTIFICATION ===
concept: Clap Crate
slug: clap-crate

# === CLASSIFICATION ===
category: cli-framework
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Clap Documentation"
source_slug: clap
authors: "The Clap Contributors"
chapter: "clap"
chapter_number: null
pdf_page: null
section: "Module clap"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - clap
  - "clap-rs"
  - "Command Line Argument Parser"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - command
  - clap-builder-api
  - clap-derive-api
  - arg
  - arg-matches
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the clap crate?"
  - "What are clap's main features?"
  - "What are the two main APIs for defining CLIs with clap?"
---

# Quick Definition

Clap is Rust's full-featured Command Line Argument Parser crate, providing both a builder API and a derive-macro API for defining CLI interfaces with automatic help generation, argument validation, shell completions, and colored output.

# Core Definition

Clap (version 4.5.54 as documented) is described as a "Command Line Argument Parser for Rust" that provides two complementary approaches to defining CLIs: a **builder API** centered on the `Command` struct and a **derive API** using procedural macros. The crate re-exports everything from `clap_builder` and optionally from `clap_derive`. Clap aims to give users a polished CLI experience out of the box, including common argument behavior, help generation, suggested fixes, colored output, and shell completions (Module: clap).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Provides two main APIs: the builder API (`Command`, `Arg`) and the derive API (`#[derive(Parser)]`)
2. Auto-generates help output, version display, and usage messages
3. Supports subcommands with their own arguments, settings, and help
4. Includes argument validation, type parsing, and error reporting with suggested fixes
5. Offers colored terminal output and shell completion generation via companion crates
6. Re-exports `clap_builder::*` as its public API surface
7. Follows semver with 6-9 months between major breaking changes
8. Supports the last two minor Rust releases (MSRV currently 1.74)
9. Includes a cookbook, tutorials, and CLI concept documentation

# Construction / Recognition

## To Add Clap to a Project:
1. Run `cargo add clap --features derive` (for the derive API)
2. Or add `clap` to `[dependencies]` in `Cargo.toml`
3. Import the needed types (e.g., `use clap::Parser;` or `use clap::{Command, Arg};`)

## To Recognize Clap Usage:
1. Look for `use clap::` imports in Rust source files
2. Check for `#[derive(Parser)]` annotations (derive API)
3. Check for `Command::new(...)` builder chains (builder API)
4. Look for `clap` in `Cargo.toml` dependencies

# Context & Application

Clap is the dominant CLI argument parsing crate in the Rust ecosystem. Its aspirations include: providing a polished out-of-the-box CLI experience, being flexible enough to port existing CLI interfaces, delivering reasonable parse performance, and maintaining resilient maintainership under the WG-CLI working group. The crate acknowledges a trade-off between flexibility and build time/binary size, pointing users to `argparse-benchmarks` for alternatives optimized for other use cases.

**Ecosystem:**
- Augmentation crates: `wild` (Windows wildcards), `argfile` (response files), `shadow-rs` (version generation), `clap_mangen` (man pages), `clap_complete` (shell completions)
- CLI helpers: `clio`, `clap-verbosity-flag`, `clap-cargo`, `colorchoice-clap`
- Testing: `trycmd`, `snapbox`, `assert_cmd`

# Examples

**Example 1** (Module: clap): Derive API usage:
```rust
use clap::Parser;

#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
struct Args {
    #[arg(short, long)]
    name: String,

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

**Example 2** (Module: clap): Generated help output:
```console
$ demo --help
Usage: demo [OPTIONS] --name <NAME>

Options:
  -n, --name <NAME>    Name of the person to greet
  -c, --count <COUNT>  Number of times to greet [default: 1]
  -h, --help           Print help
  -V, --version        Print version
```

# Relationships

## Enables
- **command** -- the central builder struct for CLI definition
- **arg** -- argument definition within commands
- **arg-matches** -- parsed argument results
- **clap-builder-api** -- the builder pattern approach
- **clap-derive-api** -- the derive macro approach

## Related
- **shell-completions** -- provided by the `clap_complete` companion crate
- **help-generation** -- automatic help output generation
- **clap-styling** -- terminal output styling

# Common Errors

- **Error**: Adding `clap` without the `derive` feature flag and trying to use `#[derive(Parser)]`.
  **Correction**: Run `cargo add clap --features derive` or add `features = ["derive"]` in `Cargo.toml`.

- **Error**: Importing from `clap_builder` directly instead of `clap`.
  **Correction**: Use `use clap::{Command, Arg};` -- `clap` re-exports everything from `clap_builder`.

# Common Confusions

- **Confusion**: Thinking the builder API and derive API are mutually exclusive.
  **Clarification**: They can be mixed. The derive API generates builder API code under the hood. You can access the `Command` from a derived `Parser` via `CommandFactory::command()`.

- **Confusion**: Assuming clap handles all CLI concerns (file I/O, logging, etc.).
  **Clarification**: Clap handles argument parsing and help/error display. File handling, logging, and other concerns require separate crates (e.g., `clio`, `clap-verbosity-flag`).

# Source Reference

Module-level documentation for `clap` crate version 4.5.54. Sections: Aspirations, Example, Related Projects, Re-exports.

# Verification Notes

- Definition: Directly from the module-level doc header "Command Line Argument Parser for Rust"
- Aspirations list: Quoted directly from source
- Example: Taken verbatim from the crate documentation
- Related projects: Listed directly from the source
- Confidence: HIGH -- this is the crate-level documentation with explicit descriptions
- Cross-references: All slugs reference planned cards in this or other agent extraction sets
