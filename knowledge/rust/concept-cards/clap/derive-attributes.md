---
# === CORE IDENTIFICATION ===
concept: Derive Helper Attributes
slug: derive-attributes

# === CLASSIFICATION ===
category: derive-api
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Clap Documentation"
source_slug: clap
authors: "The Clap Contributors"
chapter: "clap-source-docs"
chapter_number: null
pdf_page: null
section: "Derive API - Overview"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "helper attributes"
  - "#[command(...)]"
  - "#[arg(...)]"
  - "#[value(...)]"
  - "#[group(...)]"
  - "derive attributes"
  - "clap attributes"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clap-derive-api
  - command
  - arg
extends: []
related:
  - parser-derive
  - subcommand-derive
  - args-derive
  - value-enum-derive
  - arg-group
  - possible-value
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the helper attributes used with clap's derive macros?"
  - "What is the difference between #[command(...)], #[arg(...)], and #[value(...)]?"
  - "How do doc comments interact with clap's derive macros?"
  - "How do I configure command settings, argument properties, and value options in the derive API?"
---

# Quick Definition

Clap's derive helper attributes -- `#[command(...)]`, `#[arg(...)]`, `#[value(...)]`, and `#[group(...)]` -- configure how derive macros translate Rust types into CLI definitions. Each attribute category targets a different level: commands, arguments, enumerated values, and argument groups respectively.

# Core Definition

The clap derive macros accept several categories of helper attributes that map to the builder API's method calls. The Derive Reference documents five attribute categories: Command Attributes (`#[command(...)]`), Arg Attributes (`#[arg(...)]`), ArgGroup Attributes (`#[group(...)]`), ValueEnum Attributes (on `#[derive(ValueEnum)]` types), and Possible Value Attributes (`#[value(...)]`). The `Parser` proc macro registers helpers `#[clap]`, `#[structopt]`, `#[command]`, `#[arg]`, and `#[group]` (clap-derive.md, Procedural Macro Parser). The `Subcommand` and `Args` macros register `#[clap]`, `#[command]`, `#[arg]`, and `#[group]`. The `ValueEnum` macro registers `#[clap]` and `#[value]`. Additionally, doc comments are preprocessed by the derive macros: "#[derive(Parser)] works in terms of 'paragraphs'. Paragraph is a sequence of non-empty adjacent lines, delimited by sequences of blank (whitespace only) lines" (doc_comments.rs:1). The `initial_top_level_methods` function "generate[s] methods from attributes on top of struct or enum" and `field_methods` "generate[s] methods on top of a field" (item.rs:966, 983).

# Prerequisites

- **clap-derive-api** -- Understanding the derive approach is required to use helper attributes
- **command** -- `#[command(...)]` attributes map to `Command` builder methods
- **arg** -- `#[arg(...)]` attributes map to `Arg` builder methods

# Key Properties

1. `#[command(...)]` configures command-level settings (name, version, about, author, styles, propagate_version, subcommand_required, etc.) -- maps to `Command` methods
2. `#[arg(...)]` configures argument-level settings (short, long, default_value, value_parser, required, help, env, etc.) -- maps to `Arg` methods
3. `#[value(...)]` configures value-level settings on `ValueEnum` variants (name, alias, skip, hide) -- maps to `PossibleValue` methods
4. `#[group(...)]` configures argument group settings (id, required, multiple) -- maps to `ArgGroup` methods
5. `#[command(subcommand)]` on a field marks it as holding a `Subcommand` enum
6. `#[command(flatten)]` on a field or variant merges arguments or subcommands from another type
7. Doc comments become help text: the first paragraph becomes `about`/`help` (short), the full text becomes `long_about`/`long_help`
8. `#[clap(...)]` is the legacy catch-all attribute (still supported for backward compatibility) that accepts any of the above
9. `#[structopt(...)]` is supported for migration from the structopt crate but is not recommended for new code
10. The default casing for long argument names is kebab-case; for environment variables, SCREAMING_SNAKE_CASE

# Construction / Recognition

## To Use Command Attributes:
1. Place `#[command(...)]` on the struct/enum or on individual variants
2. Common settings: `#[command(version, about)]`, `#[command(name = "myapp")]`, `#[command(author)]`
3. For propagating settings: `#[command(propagate_version = true)]`
4. For subcommand fields: `#[command(subcommand)]`
5. For flattening: `#[command(flatten)]`

## To Use Arg Attributes:
1. Place `#[arg(...)]` on struct fields
2. Common settings: `#[arg(short, long)]`, `#[arg(default_value_t = 42)]`, `#[arg(required = true)]`
3. For value parsing: `#[arg(value_parser = ...)]`
4. For environment variables: `#[arg(env = "MY_VAR")]`
5. For help text override: `#[arg(help = "Custom help")]`

## To Use Value Attributes:
1. Place `#[value(...)]` on `ValueEnum` enum variants
2. For custom names: `#[value(name = "custom-name")]`
3. For aliases: `#[value(alias = "alt")]`
4. For skipping: `#[value(skip)]`

## To Recognize:
1. Look for `#[command(...)]`, `#[arg(...)]`, `#[value(...)]`, or `#[group(...)]` in derive-based code
2. The legacy `#[clap(...)]` attribute serves the same role

# Context & Application

The helper attributes are how developers configure the generated CLI without dropping to the builder API. Each attribute category corresponds to a builder type, and each key-value pair within the attribute typically maps to a method call on that builder type.

**Attribute-to-builder mapping:**
- `#[command(version)]` generates `.version(...)` on `Command`
- `#[arg(short, long)]` generates `.short('n').long("name")` on `Arg`
- `#[value(name = "json")]` generates `.value("json")` on `PossibleValue`
- `#[group(required = true)]` generates `.required(true)` on `ArgGroup`

**Doc comment processing:** The derive macros treat doc comments as help text with a paragraph-based model. The first paragraph (up to the first blank line) becomes the short help. The entire comment becomes the long help (shown with `--help` vs `-h`). This means formatting matters: blank lines separate paragraphs and control where the short help ends.

**Mixing with builder:** When an attribute is not available, you can use `#[command(after_help = "...")]` for static values or access the `Command` via `CommandFactory::command()` for dynamic modifications.

# Examples

**Example 1** (clap.md and Derive Reference): Common attribute usage:
```rust
use clap::Parser;

/// My application description (becomes about)
///
/// This longer text becomes the long_about, shown with --help.
#[derive(Parser)]
#[command(version, author, propagate_version = true)]
struct Cli {
    /// File to process (becomes arg help text)
    #[arg(short, long, value_name = "FILE")]
    input: String,

    /// Verbosity level
    #[arg(short, long, action = clap::ArgAction::Count)]
    verbose: u8,

    /// Output format
    #[arg(long, default_value = "text")]
    format: String,
}
```

**Example 2** (Derive Reference): The five attribute categories:
- `#[command(...)]` -- Command Attributes (on structs, enums, variants)
- `#[arg(...)]` -- Arg Attributes (on struct fields)
- `#[group(...)]` -- ArgGroup Attributes (on structs with `#[derive(Args)]`)
- `#[value(...)]` -- ValueEnum and Possible Value Attributes (on enum variants)
- `#[clap(...)]` -- Legacy catch-all (maps to the appropriate category by context)

**Example 3** (item.rs): Casing styles available via `#[command(rename_all = "...")]`:
- `kebab-case` (default for arguments)
- `SCREAMING_SNAKE_CASE` (default for env vars)
- `camelCase`, `PascalCase`, `snake_case`, `UPPER_CASE`, `lower_case`

# Relationships

## Related
- **command** -- `#[command(...)]` attributes generate `Command` method calls
- **arg** -- `#[arg(...)]` attributes generate `Arg` method calls
- **arg-group** -- `#[group(...)]` attributes generate `ArgGroup` method calls
- **possible-value** -- `#[value(...)]` attributes generate `PossibleValue` method calls
- **parser-derive** -- all attribute categories are used within `Parser`-derived types
- **subcommand-derive** -- `#[command(...)]` attributes configure subcommand variants
- **args-derive** -- `#[command(flatten)]` and `#[group(...)]` work with `Args`-derived types
- **value-enum-derive** -- `#[value(...)]` attributes configure `ValueEnum` variants

# Common Errors

- **Error**: Using `#[arg(...)]` on an enum variant in a `Subcommand` enum, when `#[command(...)]` is needed.
  **Correction**: At the variant level of a `Subcommand` enum, use `#[command(...)]` for command-level settings. Use `#[arg(...)]` on the variant's fields.

- **Error**: Using `#[value(...)]` on struct fields instead of `#[arg(...)]`.
  **Correction**: `#[value(...)]` is for `ValueEnum` enum variants only. Struct fields use `#[arg(...)]`.

- **Error**: Setting `long_about` via an attribute when a doc comment already provides it, resulting in the attribute overriding the doc comment.
  **Correction**: Either use doc comments (with paragraph separation) or explicit attributes, not both for the same setting.

# Common Confusions

- **Confusion**: Not understanding the difference between `#[command(...)]` and `#[arg(...)]`.
  **Clarification**: `#[command(...)]` configures the command (name, version, about, subcommand settings). `#[arg(...)]` configures individual arguments (short, long, default, help). They target different builder types.

- **Confusion**: Thinking `#[clap(...)]` is deprecated or invalid.
  **Clarification**: `#[clap(...)]` is still supported and works as a catch-all that clap routes to the appropriate attribute handler based on context. However, the specific attributes (`#[command]`, `#[arg]`, `#[value]`, `#[group]`) are preferred for clarity.

- **Confusion**: Expecting doc comments to be ignored by the derive macros.
  **Clarification**: Doc comments are actively processed into help text. The first paragraph becomes short help, the full text becomes long help. Use `#[command(about = "...")]` or `#[arg(help = "...")]` to override.

# Source Reference

Derive Reference from `repos/clap/src/_derive/mod.rs` (Attributes section listing Command, ArgGroup, Arg, ValueEnum, and Possible Value attributes); Procedural Macro definitions in clap-derive.md (helper attribute lists); Module: doc_comments (doc_comments.rs:1); Fns: initial_top_level_methods and field_methods (item.rs:966, 983); CasingStyle enum (item.rs:1376); DEFAULT_CASING and DEFAULT_ENV_CASING constants (item.rs:26, 29).

# Verification Notes

- Attribute categories from Derive Reference table of contents (mod.rs:1)
- Helper attribute registrations from clap-derive.md proc macro definitions (exact lists per macro)
- Doc comment processing from doc_comments.rs:1 (direct quotation about paragraphs)
- Casing defaults from item.rs:26 and item.rs:29
- Attribute-generation functions from item.rs:966 and item.rs:983
- Confidence: MEDIUM -- the Derive Reference outline is available but the full attribute tables are in the mod.rs doc comments which are truncated in the extracted source. Core attribute categories and their purposes are well-documented across multiple files.
- Cross-references: All slugs verified against existing cards and planned extractions
