---
concept: Clap Cargo
slug: clap-cargo
category: tooling
subcategory: cargo-integration
tier: advanced

source: "Clap Documentation"
source_slug: clap
authors: "The Clap Contributors"
chapter: "clap-cargo"
chapter_number: null
pdf_page: null
section: null

extraction_confidence: medium

aliases:
  - "clap_cargo"
  - "cargo plugin CLI flags"
  - "cargo workspace flags"
  - "Manifest struct"
  - "Workspace struct"
  - "Features struct"

prerequisites:
  - clap-derive-api
  - command

extends: []

related:
  - clap-styling
  - arg-group

contrasts_with: []

answers_questions:
  - "How do I build a cargo plugin with standard cargo CLI flags?"
  - "What reusable CLI structures does clap-cargo provide?"
  - "How do I handle workspace package selection in a cargo plugin?"
  - "How do I forward feature flags to cargo metadata?"
---

## Quick Definition

`clap_cargo` is a companion crate providing reusable CLI flag structs (`Manifest`, `Workspace`, `Features`) and cargo-compatible styling for building `cargo` subcommand plugins with standard cargo conventions.

## Core Definition

The `clap_cargo` crate (v0.18.3) provides three main derive-compatible structs that implement standard cargo CLI conventions: `Manifest` for manifest path handling and `cargo_metadata` integration, `Workspace` for workspace package selection (partitioning packages into selected and excluded sets), and `Features` for feature flag forwarding to cargo metadata commands. These structs are designed to be flattened into a derive-based CLI struct using `#[command(flatten)]`. The crate also provides a `style` module with cargo-compatible terminal styling constants (e.g., `HEADER`, `USAGE`, `LITERAL`, `PLACEHOLDER`, `ERROR`, `WARN`, `NOTE`, `GOOD`, `VALID`, `INVALID`) and a `CLAP_STYLING` constant for use with `Command::styles` to match cargo's visual style (clap-cargo.md).

## Prerequisites

- **Derive API** -- `clap_cargo` structs are designed for use with `#[command(flatten)]` in derive-based CLIs
- **Command** -- Understanding Command structure is needed to integrate clap_cargo structs

## Key Properties

1. `Manifest` struct handles manifest path (`--manifest-path`) and provides `metadata()` for `cargo_metadata` integration
2. `Workspace` struct provides workspace package selection via `partition_packages(&metadata)` returning `(selected, excluded)` tuples
3. `Features` struct captures feature flags and provides `forward_metadata(&mut metadata)` to pass them to cargo metadata commands
4. All three structs are designed for `#[command(flatten)]` integration
5. `style::CLAP_STYLING` constant provides cargo-compatible styling for `Command::styles`
6. Style constants include `HEADER`, `USAGE`, `LITERAL`, `PLACEHOLDER`, `ERROR`, `WARN`, `NOTE`, `GOOD`, `VALID`, `INVALID`, `TRANSIENT`, `CONTEXT`
7. Additional style constants for dependency types: `DEP_NORMAL`, `DEP_BUILD`, `DEP_DEV`, `DEP_FEATURE`
8. Update status constants: `UPDATE_ADDED`, `UPDATE_REMOVED`, `UPDATE_UPGRADED`, `UPDATE_DOWNGRADED`, `UPDATE_UNCHANGED`
9. The `Manifest` struct requires the `cargo_metadata` feature for full functionality
10. The style module requires the `clap` feature for `CLAP_STYLING`

## Construction / Recognition

### To Build a Cargo Plugin with clap_cargo

1. Add `clap_cargo` to dependencies with desired features (`clap`, `cargo_metadata`)
2. Create a derive-based CLI struct
3. Flatten the three structs: `Manifest`, `Workspace`, `Features`
4. Apply cargo styling with `#[command(styles = clap_cargo::style::CLAP_STYLING)]`
5. In main, use `cli.manifest.metadata()` to get a metadata command
6. Forward features with `cli.features.forward_metadata(&mut metadata)`
7. Execute metadata and partition packages with `cli.workspace.partition_packages(&metadata)`

## Context & Application

Building cargo subcommand plugins (invoked as `cargo <plugin-name>`) requires adhering to cargo's conventions for flags like `--manifest-path`, `--workspace`, `--package`, `--features`, `--all-features`, and `--no-default-features`. Manually implementing these flags is tedious and error-prone. `clap_cargo` encapsulates these conventions in reusable structs. The styling module ensures the plugin's help and error output matches cargo's visual style, providing a cohesive user experience.

**Related crates mentioned in documentation:**
- `escargot` for wrapping `cargo build`, `cargo run`, `cargo test`, etc.
- `cargo_metadata` for getting crate/workspace information
- `clap-verbosity-flag` for adding logging flags to your CLI

## Examples

**Example 1** (clap-cargo.md, main example): Complete cargo plugin CLI definition:
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

let cli = Cli::parse();
let mut metadata = cli.manifest.metadata();
cli.features.forward_metadata(&mut metadata);
let metadata = metadata.exec().unwrap();
let (selected, excluded) = cli.workspace.partition_packages(&metadata);
```

## Relationships

### Related

- **clap-styling** -- `CLAP_STYLING` bridges clap_cargo's style system with `Command::styles`
- **ArgGroup** -- The flattened structs effectively create argument groups for manifest, workspace, and feature flags
- **Derive API** -- All structs are designed for the derive API's `#[command(flatten)]` pattern

## Common Errors

- **Error**: Forgetting to enable the `cargo_metadata` feature when using `Manifest::metadata()`
  **Correction**: The `Manifest.metadata()` method requires the `cargo_metadata` feature flag

- **Error**: Forgetting to forward features before executing metadata
  **Correction**: Call `cli.features.forward_metadata(&mut metadata)` before `metadata.exec()`

- **Error**: Calling `partition_packages` without the `cargo_metadata` feature and `MetadataCommand` integration
  **Correction**: `Workspace::partition_packages` requires a `Metadata` object from `cargo_metadata`

## Common Confusions

- **Confusion**: Thinking `clap_cargo` is part of the core `clap` crate
  **Clarification**: `clap_cargo` is a separate companion crate maintained independently from clap

- **Confusion**: Believing the styling constants require `clap` integration
  **Clarification**: The `anstyle::Style` constants (HEADER, ERROR, etc.) can be used independently of clap, but the `CLAP_STYLING` constant specifically requires the `clap` feature

## Source Reference

Companion file `clap-cargo.md` (clap_cargo crate v0.18.3). Module documentation for `clap_cargo` (main module with Manifest, Workspace, Features re-exports) and `clap_cargo::style` module (styling constants and CLAP_STYLING).

## Verification Notes

- Definition: Synthesized from clap-cargo.md module-level documentation and example code
- Key Properties: Struct names and style constants directly from source; method details (metadata, forward_metadata, partition_packages) from example code
- Examples: Example taken directly from source code in clap-cargo.md
- Confidence: MEDIUM -- The source documentation is an API reference with one main example; struct method details are shown in usage but not individually documented with descriptions
- Cross-references: `clap-derive-api`, `command`, `clap-styling` verified against planned extractions
- Uncertainties: Individual method documentation for Manifest, Workspace, and Features is not included in the extracted source; behavior is inferred from the usage example
