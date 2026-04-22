---
# === CORE IDENTIFICATION ===
concept: ValueEnum Derive Macro
slug: value-enum-derive

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
  - "derive(ValueEnum)"
  - "#[derive(ValueEnum)]"
  - "ValueEnum trait"
  - "ValueEnum macro"
  - "enumerated values"
  - "enum argument values"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clap-derive-api
  - possible-value
extends:
  - possible-value
related:
  - parser-derive
  - value-parser
  - derive-attributes
contrasts_with:
  - subcommand-derive

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I restrict an argument to a fixed set of values using the derive API?"
  - "What does #[derive(ValueEnum)] do?"
  - "How do I map CLI string values to Rust enum variants?"
  - "How do I skip certain enum variants from being valid CLI values?"
---

# Quick Definition

`#[derive(ValueEnum)]` is applied to Rust enums to parse argument values into a fixed set of typed variants, automatically generating the list of possible values for help text and validation. Each enum variant becomes a valid string the user can provide on the command line.

# Core Definition

The `ValueEnum` trait enables parsing "arguments into enums." When deriving `Parser`, "a field whose type implements `ValueEnum` can have the attribute `#[arg(value_enum)]` which will call `EnumValueParser` [and allow] using the `#[arg(default_value_t)]` attribute without implementing `Display`" (Trait: ValueEnum, derive.rs:281). The trait provides three methods: `value_variants()` which returns "all possible argument values, in display order"; `from_str()` which parses "an argument into `Self`"; and `to_possible_value()` which returns "the canonical argument value" as a `PossibleValue`, with `None` for skipped variants (derive.rs:294-310). The procedural macro accepts helper attributes `#[clap]` and `#[value]` (clap-derive.md, Procedural Macro ValueEnum).

# Prerequisites

- **clap-derive-api** -- Understanding the derive approach is needed for context
- **possible-value** -- `ValueEnum` generates `PossibleValue` instances, so understanding that type is important

# Key Properties

1. Applied to enums where each variant represents a valid argument value (not a subcommand)
2. Variants are converted to lowercase kebab-case strings by default for matching
3. Provides `value_variants()` for listing all possible values (used in help text)
4. Provides `from_str()` for parsing a string into the enum
5. Provides `to_possible_value()` for getting the canonical `PossibleValue` (returns `None` for skipped variants)
6. Automatically integrates with `EnumValueParser` when used via `#[arg(value_enum)]`
7. Allows `#[arg(default_value_t)]` without implementing `Display` (the derive handles display)
8. Variants can be skipped (excluded from valid values) by having `to_possible_value()` return `None`
9. Uses `#[value(...)]` helper attributes (not `#[arg(...)]`) for value-level configuration
10. Requires the `derive` feature flag

# Construction / Recognition

## To Define Enumerated Values:
1. Create an enum and annotate it with `#[derive(ValueEnum)]`
2. Optionally also derive `Clone` (required for most uses)
3. Each variant becomes a valid string value (auto-converted to lowercase kebab-case)
4. Use `#[value(...)]` attributes on variants to customize names, aliases, or hide values
5. Optionally annotate variants with `#[value(skip)]` to exclude them from the CLI

## To Use in a Parser:
1. In a `Parser` or `Args` struct, declare a field of the `ValueEnum` type
2. Clap automatically detects the `ValueEnum` implementation and uses `EnumValueParser`
3. Optionally use `#[arg(value_enum)]` to be explicit (though detection is automatic)
4. Use `#[arg(default_value_t = MyEnum::Variant)]` for defaults

## To Recognize:
1. Look for `#[derive(ValueEnum)]` on an enum (often also with `Clone`)
2. Check for `#[value(...)]` attributes on enum variants
3. Look for fields of that enum type in `Parser` or `Args` structs

# Context & Application

`#[derive(ValueEnum)]` is the derive-API equivalent of using `PossibleValuesParser` or `EnumValueParser` in the builder API. It provides compile-time exhaustive handling of all valid values through Rust's pattern matching.

**Typical usage patterns:**
- Output format selection: `enum Format { Json, Yaml, Toml, Text }`
- Log level: `enum Level { Error, Warn, Info, Debug, Trace }`
- Color mode: `enum ColorMode { Auto, Always, Never }`
- Any argument with a known, finite set of valid string values

**Contrast with Subcommand:** Both use enums, but `ValueEnum` represents a single argument's possible values (like `--format json`), while `Subcommand` represents top-level command paths that each have their own arguments (like `git clone ...`).

**Integration with help:** The possible values are automatically included in the help text for the argument, showing users what values are valid.

# Examples

**Example 1** (synthesized from Trait: ValueEnum, derive.rs:281 and cookbook typed_derive): Basic value enum:
```rust
use clap::{Parser, ValueEnum};

#[derive(Clone, ValueEnum)]
enum ColorMode {
    Auto,
    Always,
    Never,
}

#[derive(Parser)]
struct Cli {
    /// When to use color
    #[arg(long, default_value_t = ColorMode::Auto)]
    color: ColorMode,
}
```

This generates help text showing `--color <COLOR>` with possible values `[auto, always, never]`.

**Example 2** (Trait: ValueEnum, derive.rs:281): The three trait methods:
- `value_variants() -> &[Self]` -- returns all variants in display order for help generation
- `from_str(s: &str) -> Result<Self, String>` -- parses a user-provided string into an enum variant
- `to_possible_value(&self) -> Option<PossibleValue>` -- returns the canonical value representation; `None` means the variant is skipped

# Relationships

## Builds Upon
- **possible-value** -- each enum variant generates a `PossibleValue` via `to_possible_value()`

## Enables
- Type-safe enumerated argument values in the derive API

## Related
- **parser-derive** -- `ValueEnum` types are used as field types in `Parser`-derived structs
- **value-parser** -- `ValueEnum` integrates with `EnumValueParser` under the hood
- **derive-attributes** -- `#[value(...)]` attributes configure `ValueEnum` variants

## Contrasts With
- **subcommand-derive** -- both use enums, but `ValueEnum` is for argument values while `Subcommand` is for command paths

# Common Errors

- **Error**: Forgetting to derive `Clone` alongside `ValueEnum`, leading to compilation errors when used as a field type.
  **Correction**: Always include `Clone` in the derive list: `#[derive(Clone, ValueEnum)]`.

- **Error**: Using `#[arg(...)]` instead of `#[value(...)]` on `ValueEnum` variants.
  **Correction**: `ValueEnum` variants use `#[value(...)]` attributes, not `#[arg(...)]`. The `#[arg(...)]` attribute applies to the field in the parent struct.

- **Error**: Trying to attach subcommand-like fields to `ValueEnum` variants.
  **Correction**: `ValueEnum` variants cannot have fields with arguments. They represent simple string-to-enum mappings. For variants with their own arguments, use `#[derive(Subcommand)]`.

# Common Confusions

- **Confusion**: Confusing `ValueEnum` (for argument values like `--format json`) with `Subcommand` (for command paths like `git clone`).
  **Clarification**: `ValueEnum` maps a single argument's string value to an enum variant. `Subcommand` defines independent command hierarchies, each with their own set of arguments.

- **Confusion**: Thinking `ValueEnum` requires explicit `#[arg(value_enum)]` on the field.
  **Clarification**: Clap automatically detects fields whose type implements `ValueEnum` and uses the appropriate parser. The `#[arg(value_enum)]` attribute is optional and rarely needed.

# Source Reference

Trait: ValueEnum (derive.rs:281) and its methods (derive.rs:294-310) in clap-source-docs.md; Procedural Macro `ValueEnum` in clap-derive.md; Section 5 "Derive API - Overview" (line 19649); cookbook `typed_derive` example.

# Verification Notes

- Definition: Direct quotation from Trait: ValueEnum documentation at derive.rs:281
- Three method signatures and descriptions from derive.rs:294-310
- EnumValueParser integration and default_value_t note from derive.rs:281 description
- Helper attributes `#[clap]` and `#[value]` from clap-derive.md proc macro definition
- Confidence: HIGH -- the ValueEnum trait has explicit documentation with clear method descriptions
- Cross-references: All slugs verified against existing cards and planned extractions
