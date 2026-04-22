---
# === CORE IDENTIFICATION ===
concept: Clap Derive API
slug: clap-derive-api

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
section: "Derive API - Overview"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "derive API"
  - "clap derive"
  - "declarative CLI"
  - "derive-based parsing"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clap-crate
extends:
  - clap-builder-api
related:
  - parser-derive
  - subcommand-derive
  - args-derive
  - value-enum-derive
  - derive-attributes
  - command-factory-trait
contrasts_with:
  - clap-builder-api

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the clap derive API?"
  - "How does the derive API differ from the builder API?"
  - "When should I use the derive API vs the builder API?"
  - "What feature flag enables the derive API?"
---

# Quick Definition

The clap derive API is a declarative, macro-based approach to defining CLI interfaces using Rust's `#[derive(...)]` procedural macros on structs and enums, generating the equivalent builder API code at compile time. It is clap's recommended approach for most use cases.

# Core Definition

The derive API lets developers define CLI structure using annotated Rust types rather than builder method chains. By placing `#[derive(Parser)]` on a struct (along with helper attributes like `#[command(...)]` and `#[arg(...)]`), the procedural macros in the `clap_derive` crate generate implementations of the `Parser`, `CommandFactory`, `FromArgMatches`, `Args`, `Subcommand`, and `ValueEnum` traits. This is described as "far less verbose than defining the `clap::Command` struct manually, receiving an instance of `clap::ArgMatches` from conducting parsing, and then implementing a conversion code to instantiate an instance of the user context struct" (clap_derive, Procedural Macro `Parser`). The derive API requires enabling the `derive` feature flag via `cargo add clap --features derive` (Derive Reference, Overview).

# Prerequisites

- **clap-crate** -- Understanding the clap crate and its ecosystem is required to understand where the derive API fits

# Key Properties

1. Requires the `derive` feature flag to be enabled in `Cargo.toml`
2. Uses Rust's procedural macro system (`#[derive(...)]`) to generate trait implementations at compile time
3. Generates builder API code under the hood -- the derive API is a layer on top of the builder API, not a replacement
4. Four derive macros are available: `Parser`, `Subcommand`, `Args`, and `ValueEnum`
5. Three categories of helper attributes configure behavior: `#[command(...)]`, `#[arg(...)]`, and `#[value(...)]`
6. Doc comments on structs and fields are automatically converted to help text (first paragraph becomes short help, full text becomes long help)
7. Field types drive argument behavior: `String` becomes a required positional, `Option<T>` becomes optional, `bool` becomes a flag, `Vec<T>` accepts multiple values
8. Can be mixed with the builder API when needed for advanced customization
9. The default casing style for generated argument names is kebab-case (`DEFAULT_CASING`) and SCREAMING_SNAKE_CASE for environment variables (`DEFAULT_ENV_CASING`)

# Construction / Recognition

## To Define a CLI with the Derive API:
1. Enable the `derive` feature: `cargo add clap --features derive`
2. Import the `Parser` trait: `use clap::Parser;`
3. Define a struct with `#[derive(Parser)]`
4. Add `#[command(...)]` attributes for command-level settings (name, version, about)
5. Define fields for each argument, using `#[arg(...)]` attributes for argument configuration
6. For subcommands, define an enum with `#[derive(Subcommand)]` and reference it via `#[command(subcommand)]`
7. Call `YourStruct::parse()` to parse from `std::env::args_os()` and get a populated struct instance

## To Recognize Derive API Usage:
1. Look for `#[derive(Parser)]` on a struct
2. Check for `#[command(...)]` and `#[arg(...)]` helper attributes
3. Look for `.parse()` called on the derived struct type
4. Check for `use clap::Parser;` imports

# Context & Application

The derive API is clap's recommended approach for most use cases. It provides a more concise, type-safe, and Rust-idiomatic way to define CLIs compared to the builder API. The struct-based definition naturally maps to the application's configuration, and the compiler catches type mismatches at compile time rather than runtime.

**When to use the derive API:**
- Most CLI applications where arguments map naturally to a struct
- When you want the most concise, readable CLI definition
- When type safety at compile time is a priority
- When doc comments should serve as help text automatically

**When to prefer the builder API instead:**
- When you need runtime-dynamic argument construction
- When you need fine-grained control not exposed through derive attributes
- When building plugins or frameworks that construct CLIs programmatically

**Mixing the two APIs:** The derive and builder APIs can be combined. You can use `CommandFactory::command()` on a derived type to get the underlying `Command` and modify it with builder methods before parsing.

# Examples

**Example 1** (clap.md, Module: clap): Basic derive API usage:
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

**Example 2** (Derive Reference): The four derive macros correspond to different trait implementations:
- `#[derive(Parser)]` on a struct -- main entry point, implements `Parser`, `CommandFactory`, `FromArgMatches`
- `#[derive(Subcommand)]` on an enum -- implements `Subcommand`, used with `#[command(subcommand)]` on a field
- `#[derive(Args)]` on a struct -- implements `Args`, used with `#[command(flatten)]` for reusable argument groups
- `#[derive(ValueEnum)]` on an enum -- implements `ValueEnum`, for enumerated argument values

# Relationships

## Builds Upon
- **clap-builder-api** -- the derive API generates builder API code under the hood

## Enables
- **parser-derive** -- the primary derive macro for CLI entry points
- **subcommand-derive** -- derive macro for enum-based subcommands
- **args-derive** -- derive macro for reusable argument groups
- **value-enum-derive** -- derive macro for enumerated argument values
- **derive-attributes** -- the helper attributes that configure derive behavior

## Related
- **command** -- the underlying `Command` struct that derives generate
- **arg** -- the underlying `Arg` struct that field annotations generate
- **command-factory-trait** -- trait derived as part of `Parser`, bridges derive and builder

## Contrasts With
- **clap-builder-api** -- the imperative, method-chaining approach to CLI definition

# Common Errors

- **Error**: Forgetting to enable the `derive` feature flag, resulting in `cannot find derive macro Parser in this scope`.
  **Correction**: Add `features = ["derive"]` to the clap dependency in `Cargo.toml` or run `cargo add clap --features derive`.

- **Error**: Trying to derive `Parser` on an enum instead of a struct.
  **Correction**: `Parser` is derived on structs. For enum-based subcommands, derive `Subcommand` on the enum and reference it from a struct field with `#[command(subcommand)]`.

- **Error**: Using `#[clap(...)]` instead of the specific `#[command(...)]` or `#[arg(...)]` attributes.
  **Correction**: While `#[clap(...)]` is still supported for backward compatibility, the idiomatic approach uses `#[command(...)]` for command-level settings and `#[arg(...)]` for argument-level settings.

# Common Confusions

- **Confusion**: Believing the derive API and builder API are completely separate systems.
  **Clarification**: The derive API generates builder API code at compile time. They share the same underlying types (`Command`, `Arg`, `ArgMatches`) and can be mixed freely.

- **Confusion**: Thinking the derive API is less powerful than the builder API.
  **Clarification**: The derive API exposes nearly all builder functionality through attributes. For the rare cases where an attribute is not available, you can drop down to the builder API via `CommandFactory::command()`.

- **Confusion**: Assuming doc comments are ignored by the derive macros.
  **Clarification**: Doc comments on derived types and fields are processed into help text. The first paragraph becomes the short help (`about`/`help`), and the full comment becomes the long help.

# Source Reference

Sections 5-6 of clap-source-docs.md ("Derive API - Overview" starting at line 19649 and "Derive API - Parser" starting at line 19823); clap-derive.md (crate documentation for `clap_derive` v4.5.49); Module: clap overview from clap.md (example and derive quick links); Derive Reference from `repos/clap/src/_derive/mod.rs` and Derive Tutorial from `repos/clap/src/_derive/_tutorial.rs`.

# Verification Notes

- Definition: Synthesized from the Parser proc macro description in clap-derive.md and the crate overview in clap.md
- The "far less verbose" quote is directly from the clap_derive source documentation
- Feature flag requirement documented explicitly in Derive Reference and Tutorial
- Doc comment processing documented in `repos/clap/clap_derive/src/utils/doc_comments.rs`
- Default casing styles from `clap_derive/src/item.rs` (DEFAULT_CASING, DEFAULT_ENV_CASING)
- Confidence: HIGH -- the derive API is extensively documented across multiple source files with explicit descriptions and examples
- Cross-references: All slugs verified against existing cards and planned extractions in this batch
