---
# === CORE IDENTIFICATION ===
concept: Subcommand Derive Macro
slug: subcommand-derive

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
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "derive(Subcommand)"
  - "#[derive(Subcommand)]"
  - "Subcommand trait"
  - "Subcommand macro"
  - "enum subcommands"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clap-derive-api
  - parser-derive
  - subcommand
extends:
  - subcommand
related:
  - args-derive
  - derive-attributes
  - command
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define subcommands using clap's derive API?"
  - "What does #[derive(Subcommand)] do?"
  - "How do I connect a Subcommand enum to a Parser struct?"
  - "How do I flatten subcommands from one enum into another?"
---

# Quick Definition

`#[derive(Subcommand)]` is applied to Rust enums to define CLI subcommands, where each enum variant represents a distinct subcommand with its own arguments. The enum is connected to a `Parser`-derived struct via the `#[command(subcommand)]` field attribute.

# Core Definition

The `Subcommand` trait enables parsing "a sub-command into a user-defined enum." Implementing this trait "lets a parent container delegate subcommand behavior to `Self`" through two mechanisms: "`#[command(subcommand)] field: SubCmd`: Attribute can be used with either struct fields or enum variants that impl `Subcommand`" and "`#[command(flatten)] Variant(SubCmd)`: Attribute can only be used with enum variants that impl `Subcommand`" (Trait: Subcommand, derive.rs:248). The derive macro generates the `Subcommand` trait implementation including the methods `augment_subcommands`, `augment_subcommands_for_update`, and `has_subcommand`. The procedural macro accepts helper attributes `#[clap]`, `#[command]`, `#[arg]`, and `#[group]` (clap-derive.md, Procedural Macro Subcommand).

# Prerequisites

- **clap-derive-api** -- Understanding the derive approach is needed to know the context for `#[derive(Subcommand)]`
- **parser-derive** -- `Subcommand` enums are used within `Parser`-derived structs, so understanding the top-level entry point is required
- **subcommand** -- The builder-level concept of subcommands (as child `Command` instances) underlies what the derive macro generates

# Key Properties

1. Applied to enums, where each variant becomes a subcommand
2. Each variant can contain fields that become the subcommand's arguments
3. Variant names are converted to lowercase kebab-case by default (following `DEFAULT_CASING`)
4. Connected to the parent `Parser` struct via a field annotated with `#[command(subcommand)]`
5. Can be nested: a `Subcommand` variant can contain another `Subcommand` enum for multi-level command hierarchies
6. Supports flattening via `#[command(flatten)] Variant(SubCmd)` to merge another enum's subcommands into the current level
7. The `has_subcommand` method tests whether `Self` can parse a specific subcommand name
8. Requires the `derive` feature flag

# Construction / Recognition

## To Define Subcommands:
1. Create an enum and annotate it with `#[derive(Subcommand)]`
2. Define one variant per subcommand
3. Add fields to variants for subcommand-specific arguments (named fields for named args, tuple variants for positional)
4. Use `#[command(...)]` on variants for subcommand-level settings (about, alias, etc.)
5. Use `#[arg(...)]` on variant fields for argument-level settings

## To Connect to a Parser:
1. In the `Parser`-derived struct, add a field of the enum type
2. Annotate that field with `#[command(subcommand)]`
3. The field type can be `SubCmd` (subcommand required) or `Option<SubCmd>` (subcommand optional)

## To Flatten Subcommands:
1. In one `Subcommand` enum, add a variant with `#[command(flatten)]`
2. The variant's payload must be another type that implements `Subcommand`
3. The flattened type's variants are merged into the parent enum's subcommand list

## To Recognize:
1. Look for `#[derive(Subcommand)]` on an enum
2. Check for `#[command(subcommand)]` on a struct field referencing that enum

# Context & Application

`#[derive(Subcommand)]` is the derive-API equivalent of calling `.subcommand(Command::new(...))` in the builder API. It maps naturally to the Rust enum type, providing exhaustive pattern matching on subcommands at compile time.

**Typical usage patterns:**
- Git-like tools: `enum Commands { Clone { url: String }, Push { remote: String }, Commit { message: String } }`
- Tools with optional subcommands: use `Option<Commands>` in the parser struct so the tool can run without a subcommand
- Multi-level hierarchies: nest `Subcommand` enums for `app module create`, `app module delete`, etc.
- Composable CLIs: flatten shared subcommand sets from library enums into application enums

The derive approach provides exhaustive match checking -- when you add a new subcommand variant, the compiler forces you to handle it everywhere it is matched.

# Examples

**Example 1** (synthesized from Trait: Subcommand, derive.rs:248 and cookbook git_derive): Basic subcommand definition:
```rust
use clap::{Parser, Subcommand};

#[derive(Parser)]
#[command(version, about)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Clone a repository
    Clone {
        /// The URL to clone from
        url: String,
    },
    /// Push changes to remote
    Push {
        /// Remote name
        #[arg(default_value = "origin")]
        remote: String,
    },
}
```

**Example 2** (Trait: Subcommand, derive.rs:248): The two ways to integrate subcommands:
- `#[command(subcommand)] field: SubCmd` -- used on struct fields or enum variants
- `#[command(flatten)] Variant(SubCmd)` -- used on enum variants only, merges subcommands from another `Subcommand` enum

# Relationships

## Builds Upon
- **subcommand** -- the builder-level concept of subcommands as child `Command` instances
- **parser-derive** -- subcommand enums are used within `Parser`-derived structs

## Enables
- **args-derive** -- enum variants with named fields are analogous to `Args` groups per subcommand

## Related
- **command** -- each subcommand variant generates a child `Command`
- **derive-attributes** -- `#[command(...)]` and `#[arg(...)]` configure subcommand variants and their fields

# Common Errors

- **Error**: Using `#[derive(Subcommand)]` on a struct instead of an enum.
  **Correction**: `Subcommand` is for enums only. For structs, use `#[derive(Parser)]` (top-level) or `#[derive(Args)]` (reusable argument groups).

- **Error**: Forgetting the `#[command(subcommand)]` attribute on the parent struct field, causing the enum to be treated as a regular argument type.
  **Correction**: Always annotate the field referencing a `Subcommand` enum with `#[command(subcommand)]`.

- **Error**: Using `#[command(flatten)]` on a struct field that holds a `Subcommand` enum.
  **Correction**: `#[command(flatten)]` for subcommands can only be used on enum variants, not struct fields. Use `#[command(subcommand)]` on struct fields.

# Common Confusions

- **Confusion**: Thinking each subcommand variant needs its own `#[derive(Parser)]`.
  **Clarification**: Only the top-level struct needs `#[derive(Parser)]`. Subcommand enums use `#[derive(Subcommand)]`. Individual variants with complex arguments can use `#[derive(Args)]` on a separate struct.

- **Confusion**: Confusing `Subcommand` with `Args` -- both are derive macros applied to types referenced from a `Parser` struct.
  **Clarification**: `Subcommand` is for enums representing mutually exclusive command paths. `Args` is for structs representing reusable groups of arguments that can be flattened into any command.

# Source Reference

Trait: Subcommand (derive.rs:248) and its methods (derive.rs:263-277) in clap-source-docs.md; Procedural Macro `Subcommand` in clap-derive.md; Section 5 "Derive API - Overview" (line 19649) in clap-source-docs.md for the derive crate overview; cookbook examples `git_derive` and `repl_derive`.

# Verification Notes

- Definition: Direct quotation from Trait: Subcommand documentation at derive.rs:248
- The two integration patterns (`#[command(subcommand)]` and `#[command(flatten)]`) are quoted directly from source
- Helper attributes from clap-derive.md proc macro definition
- `has_subcommand` method documented at derive.rs:277
- Confidence: HIGH -- the Subcommand trait has explicit documentation with clear usage patterns
- Cross-references: All slugs verified against existing cards and planned extractions
