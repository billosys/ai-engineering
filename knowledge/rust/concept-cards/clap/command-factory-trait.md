---
# === CORE IDENTIFICATION ===
concept: CommandFactory Trait
slug: command-factory-trait

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
section: "Core Concepts - Command"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "clap::CommandFactory"
  - CommandFactory

# === TYPED RELATIONSHIPS ===
prerequisites:
  - command
  - parser-derive
extends: []
related:
  - clap-derive-api
  - subcommand-derive
  - arg-matches
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the CommandFactory trait?"
  - "How do I access the underlying Command from a derived Parser?"
  - "What is the difference between command() and command_for_update()?"
---

# Quick Definition

`CommandFactory` is a trait derived as part of `#[derive(Parser)]` that bridges clap's derive API to the builder API by providing methods to construct a `Command` from a user-defined struct.

# Core Definition

The `CommandFactory` trait is documented as: "Create a `Command` relevant for a user-defined container. Derived as part of `Parser`." It provides two methods: `command()` to "Build a `Command` that can instantiate `Self`" and `command_for_update()` to "Build a `Command` that can update `self`" (derive.rs, line 113).

This trait is the key integration point between the derive and builder APIs. When you derive `Parser` on a struct, `CommandFactory` is automatically implemented, allowing you to obtain the `Command` that the derive macro generates.

# Prerequisites

- **command** -- `CommandFactory` produces a `Command` instance; understanding `Command` is necessary to use the result.
- **parser-derive** -- `CommandFactory` is derived as part of `#[derive(Parser)]`; understanding the derive API is needed.

# Key Properties

1. Automatically derived when using `#[derive(Parser)]`
2. Provides `command() -> Command` to build a `Command` that can instantiate `Self` via `FromArgMatches`
3. Provides `command_for_update() -> Command` to build a `Command` that can update an existing `self`
4. Both methods return a fully-configured `Command` with all arguments, subcommands, and settings defined by the derive attributes

# Construction / Recognition

## To Use CommandFactory:
1. Derive `Parser` on a struct: `#[derive(Parser)]`
2. Call `MyStruct::command()` to get the generated `Command`
3. Optionally modify the `Command` before parsing
4. Parse with `FromArgMatches::from_arg_matches_mut` or the usual `Parser::parse()`

## To Recognize CommandFactory:
1. Look for `::command()` or `::command_for_update()` called as associated functions on derive structs
2. Look for trait bounds requiring `CommandFactory`

# Context & Application

`CommandFactory` is essential when you need to customize the derived `Command` beyond what attributes support, or when you need to access command metadata programmatically (e.g., generating completions, rendering help in tests, or introspecting the argument structure). It provides the escape hatch from pure derive usage into the builder API.

**Typical use cases:**
- Generating shell completions from a derived CLI definition
- Rendering help output in tests without parsing arguments
- Modifying the derived command with builder API methods before parsing
- Inspecting the argument structure programmatically

# Examples

**Example 1** (derive.rs, line 113): Accessing Command from a derived Parser:
```rust
use clap::{Parser, CommandFactory};

#[derive(Parser)]
struct Cli {
    #[arg(short, long)]
    name: String,
}

// Get the Command to inspect or modify
let cmd = Cli::command();
// Render help without parsing
let help = cmd.render_help();
```

# Relationships

## Builds Upon
- **command** -- `CommandFactory` produces `Command` instances
- **parser-derive** -- `CommandFactory` is derived alongside `Parser`

## Related
- **clap-derive-api** -- `CommandFactory` is part of the derive API's trait hierarchy
- **subcommand-derive** -- works alongside `CommandFactory` for nested command enums
- **arg-matches** -- the `Command` produced is used with `FromArgMatches` for instantiation

# Common Errors

- **Error**: Trying to call `CommandFactory::command()` on a type that only derives `Args` or `Subcommand` (not `Parser`).
  **Correction**: `CommandFactory` is derived as part of `Parser`. Ensure the top-level struct uses `#[derive(Parser)]`.

- **Error**: Modifying the `Command` from `command()` but then calling `Parser::parse()` which builds a fresh `Command`.
  **Correction**: If you modify the `Command`, use it directly with `get_matches()` and then `FromArgMatches::from_arg_matches()` to instantiate the struct.

# Common Confusions

- **Confusion**: Thinking `command()` and `command_for_update()` return the same thing.
  **Clarification**: `command()` builds a `Command` for creating a new instance of `Self`. `command_for_update()` builds one configured for updating an existing instance, which may differ in required-ness of arguments.

- **Confusion**: Believing `CommandFactory` must be explicitly derived.
  **Clarification**: It is automatically derived when you use `#[derive(Parser)]`. No separate derive annotation is needed.

# Source Reference

Section 1: Core Concepts - Command, from `clap_builder/src/derive.rs`. Trait definition at line 113, methods `command` at line 117 and `command_for_update` at line 121.

# Verification Notes

- Definition: Directly quoted from trait-level documentation at line 113
- Method descriptions: Taken verbatim from method docs
- Confidence: HIGH -- trait is explicitly documented with clear purpose
- Cross-references: `parser-derive` and `clap-derive-api` are in Agent 4's scope
