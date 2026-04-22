---
# === CORE IDENTIFICATION ===
concept: Args Derive Macro
slug: args-derive

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
  - "derive(Args)"
  - "#[derive(Args)]"
  - "Args trait"
  - "Args macro"
  - "argument groups"
  - "flatten args"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clap-derive-api
  - parser-derive
  - arg
extends:
  - arg-group
related:
  - subcommand-derive
  - derive-attributes
  - command
contrasts_with:
  - subcommand-derive

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create reusable argument groups in clap's derive API?"
  - "What does #[derive(Args)] do?"
  - "How do I share arguments between multiple commands or subcommands?"
  - "How do I flatten argument groups into a parent parser?"
---

# Quick Definition

`#[derive(Args)]` is applied to Rust structs to define reusable groups of CLI arguments that can be flattened into a `Parser` struct or used as a `Subcommand` variant payload, enabling argument composition and sharing across commands.

# Core Definition

The `Args` trait enables parsing "a set of arguments into a user-defined container." Implementing this trait "lets a parent container delegate argument parsing behavior to `Self`" through two mechanisms: "`#[command(flatten)] args: ChildArgs`: Attribute can only be used with struct fields that impl `Args`" and "`Variant(ChildArgs)`: No attribute is used with enum variants that impl `Args`" (Trait: Args, derive.rs:214). The derive generates `Args` and `FromArgMatches` implementations, along with methods `group_id` (which reports the `ArgGroup::id` for the argument set), `augment_args`, and `augment_args_for_update`. The `gen_augment` function in the derive crate "generate[s] a block of code to add arguments/subcommands corresponding to the `fields` to an cmd" (derives/args.rs:167). The procedural macro accepts helper attributes `#[clap]`, `#[command]`, `#[arg]`, and `#[group]` (clap-derive.md, Procedural Macro Args).

# Prerequisites

- **clap-derive-api** -- Understanding the derive approach is needed to know the context for `#[derive(Args)]`
- **parser-derive** -- `Args` structs are used within `Parser`-derived structs, so the top-level entry point must be understood
- **arg** -- The builder-level concept of arguments underlies what `Args` generates

# Key Properties

1. Applied to structs to define a set of related arguments as a reusable group
2. Integrated into a `Parser` struct via `#[command(flatten)]` on a field of the `Args` type
3. Can be used as the payload of a `Subcommand` enum variant without any special attribute
4. Generates a `group_id()` method that reports the `ArgGroup::id` for the argument set, enabling group-level validation
5. Each `Args` struct generates its own `ArgGroup`, allowing constraints like "at least one of these arguments is required"
6. Multiple `Args` types can be flattened into the same parent, enabling composition of independent argument groups
7. The `augment_args` and `augment_args_for_update` methods append arguments to the parent `Command`
8. Requires the `derive` feature flag

# Construction / Recognition

## To Define an Argument Group:
1. Create a struct and annotate it with `#[derive(Args)]`
2. Define fields for each argument in the group
3. Use `#[arg(...)]` attributes on fields for argument-level configuration
4. Use `#[command(...)]` or `#[group(...)]` attributes on the struct for group-level settings

## To Use in a Parser:
1. In the `Parser`-derived struct, add a field of the `Args` type
2. Annotate that field with `#[command(flatten)]`
3. The arguments from the `Args` struct are merged into the parent command as if defined directly on it

## To Use in a Subcommand:
1. In a `Subcommand` enum, use the `Args` type as a tuple variant payload: `Variant(MyArgs)`
2. No special attribute is needed on the variant -- clap recognizes the `Args` implementation automatically

## To Recognize:
1. Look for `#[derive(Args)]` on a struct
2. Check for `#[command(flatten)]` on a field referencing that struct in a `Parser` or `Args` parent

# Context & Application

`#[derive(Args)]` enables the composition pattern for CLI definitions. Rather than defining all arguments in a single monolithic `Parser` struct, developers can group related arguments into separate `Args` structs and flatten them into the parent.

**Typical usage patterns:**
- Shared arguments across subcommands: define common args (verbosity, output format) in an `Args` struct and flatten into each subcommand variant
- Library-provided arguments: crates like `clap-cargo` and `clap-verbosity-flag` publish `Args` types that users can flatten into their CLIs
- Logical grouping: separate authentication args, output args, and connection args into distinct structs
- Argument group validation: each `Args` struct gets its own `ArgGroup`, enabling "require at least one" or "conflicts" constraints at the group level

The `Args` derive is what makes clap's derive API composable. It parallels the builder API pattern of programmatically adding arguments from helper functions, but with compile-time type safety.

# Examples

**Example 1** (synthesized from Trait: Args, derive.rs:214 and clap-cargo): Reusable argument group:
```rust
use clap::{Args, Parser};

#[derive(Args)]
struct OutputArgs {
    /// Output format
    #[arg(short, long, default_value = "text")]
    format: String,

    /// Write output to file
    #[arg(short, long)]
    output: Option<String>,
}

#[derive(Parser)]
struct Cli {
    /// Input file
    input: String,

    #[command(flatten)]
    output: OutputArgs,
}
```

**Example 2** (Trait: Args, derive.rs:214): The two ways to integrate `Args`:
- `#[command(flatten)] args: ChildArgs` -- on struct fields, merges child arguments into the parent command
- `Variant(ChildArgs)` -- on enum variants in a `Subcommand` enum, no attribute needed

**Example 3** (clap-cargo integration, clap-source-docs.md): Library-provided `Args`:
```rust
use clap::Parser;

#[derive(Debug, Parser)]
#[command(styles = clap_cargo::style::CLAP_STYLING)]
struct Cli {
    #[command(flatten)]
    manifest: clap_cargo::Manifest,
    #[command(flatten)]
    workspace: clap_cargo::Workspace,
    #[command(flatten)]
    features: clap_cargo::Features,
}
```

# Relationships

## Builds Upon
- **arg** -- each field in an `Args` struct generates an `Arg`
- **arg-group** -- each `Args` struct generates an `ArgGroup` with a group ID

## Enables
- Composable CLI definitions through flattening

## Related
- **parser-derive** -- `Args` structs are flattened into `Parser`-derived structs
- **subcommand-derive** -- `Args` structs can serve as subcommand variant payloads
- **derive-attributes** -- `#[arg(...)]` and `#[command(...)]` configure `Args` fields and groups

## Contrasts With
- **subcommand-derive** -- `Args` groups multiple arguments into one struct (additive), while `Subcommand` defines mutually exclusive command paths

# Common Errors

- **Error**: Using `#[derive(Args)]` on an enum instead of a struct.
  **Correction**: `Args` is for structs only. For enums, use `#[derive(Subcommand)]` or `#[derive(ValueEnum)]`.

- **Error**: Referencing an `Args` field in a `Parser` struct without `#[command(flatten)]`, causing clap to try to parse the struct type as a single argument value.
  **Correction**: Always use `#[command(flatten)]` when embedding an `Args` struct into a parent struct.

- **Error**: Name collisions when flattening multiple `Args` types that have fields with the same argument name.
  **Correction**: Ensure argument names (derived from field names or explicit `#[arg(long = "...")]`) are unique across all flattened groups.

# Common Confusions

- **Confusion**: Thinking `Args` is required for defining arguments -- believing you cannot put `#[arg(...)]` fields directly on a `Parser` struct.
  **Clarification**: You can define arguments directly on a `Parser` struct. `Args` is only needed when you want to reuse or compose argument groups across multiple commands.

- **Confusion**: Confusing `#[command(flatten)]` (for `Args` structs on struct fields) with `#[command(subcommand)]` (for `Subcommand` enums on struct fields).
  **Clarification**: `flatten` merges arguments into the current command level. `subcommand` creates a new command level. They serve fundamentally different purposes.

# Source Reference

Trait: Args (derive.rs:214) and its methods (derive.rs:228-239) in clap-source-docs.md; Procedural Macro `Args` in clap-derive.md; Fn: gen_augment (derives/args.rs:167) in Section 5 "Derive API - Overview"; clap-cargo integration example from clap-source-docs.md.

# Verification Notes

- Definition: Direct quotation from Trait: Args documentation at derive.rs:214
- The two integration patterns (flatten and variant payload) quoted directly from source
- `group_id`, `augment_args`, `augment_args_for_update` methods documented in source
- `gen_augment` description from derives/args.rs:167
- clap-cargo example from clap-source-docs.md lines 6737-6747
- Confidence: HIGH -- the Args trait has explicit documentation with clear usage patterns
- Cross-references: All slugs verified against existing cards and planned extractions
