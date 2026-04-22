---
# === CORE IDENTIFICATION ===
concept: Advanced Cargo and Crates.io
slug: rust-cargo-advanced

# === CLASSIFICATION ===
category: tooling
subcategory: cargo
tier: intermediate

# === PROVENANCE ===
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "More About Cargo and Crates.io"
chapter_number: 14
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "release profiles"
  - "cargo publish"
  - "crates.io publishing"
  - "cargo workspaces"
  - "cargo install"
  - "pub use re-exports"
  - "doc comments"
  - "documentation comments"
  - "cargo doc"
  - "cargo yank"
  - "custom cargo commands"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rust-modules-and-crates
  - rust-common-programming-concepts
extends:
  - cargo-dependencies
  - cargo-project-layout
related:
  - rust-testing
  - rust-generics-traits-lifetimes
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I customize build optimization levels for development and release?"
  - "How do I write documentation comments in Rust?"
  - "How do documentation tests work?"
  - "What is pub use and when should I use it?"
  - "How do I publish a crate to crates.io?"
  - "What metadata is required to publish a crate?"
  - "What is a Cargo workspace and when should I use one?"
  - "How do I install binary crates from crates.io?"
  - "How do I yank a version from crates.io?"
  - "Can I extend Cargo with custom subcommands?"
---

# Quick Definition

Chapter 14 covers advanced Cargo features beyond basic build/run/test: release profiles for build customization, documentation comments (`///` and `//!`) that generate HTML and run as tests, `pub use` for re-exporting a clean public API, publishing to crates.io, workspaces for managing multi-crate projects, `cargo install` for binary tools, and custom Cargo subcommands.

# Core Definition

The source introduces release profiles as "predefined, customizable profiles with different configurations that allow a programmer to have more control over various options for compiling code. Each profile is configured independently of the others" (Ch. 14, "Customizing Builds with Release Profiles"). Cargo provides two main profiles: `dev` (used by `cargo build`) and `release` (used by `cargo build --release`), with `opt-level` defaulting to 0 and 3 respectively.

**Documentation comments** use `///` (for the following item) or `//!` (for the containing item) and "support Markdown notation for formatting the text." Running `cargo test` executes code examples in documentation comments as tests: "Nothing is better than documentation with examples. But nothing is worse than examples that don't work because the code has changed since the documentation was written" (Ch. 14, "Documentation Comments as Tests").

**`pub use` re-exports** allow crate authors to decouple internal module structure from the public API: "Re-exporting takes a public item in one location and makes it public in another location, as if it were defined in the other location instead" (Ch. 14, "Exporting a Convenient Public API").

A **workspace** is "a set of packages that share the same _Cargo.lock_ and output directory" (Ch. 14, "Creating a Workspace"). Crates within a workspace share a single `Cargo.lock` for dependency version consistency and a single `target/` directory to avoid redundant recompilation.

Publishing is permanent: "The version can never be overwritten, and the code cannot be deleted" except through yanking. **Yanking** "prevents new projects from depending on that version while allowing all existing projects that depend on it to continue" (Ch. 14, "Deprecating Versions from Crates.io").

# Prerequisites

- **Modules and Crates** -- understanding the module system, `pub`, and `use` is essential for `pub use` re-exports and workspace organization
- **Common Programming Concepts** -- basic Rust syntax is needed to write doc comment examples and understand profile settings

# Key Properties

1. **`dev` profile**: `opt-level = 0` (no optimization, fast compile); used by `cargo build`
2. **`release` profile**: `opt-level = 3` (maximum optimization, slower compile); used by `cargo build --release`
3. **Profile customization**: override defaults via `[profile.dev]` or `[profile.release]` in `Cargo.toml`
4. **`///` doc comments**: generate HTML documentation for the following item; support Markdown; commonly include `# Examples`, `# Panics`, `# Errors`, `# Safety` sections
5. **`//!` doc comments**: document the containing item (crate root or module)
6. **`cargo doc --open`**: generates HTML documentation and opens it in a browser
7. **Doc tests**: code blocks in `///` comments are compiled and run by `cargo test`
8. **`pub use` re-exports**: make deeply nested items accessible at the crate root without restructuring internals
9. **Publishing requirements**: unique crate name, `description`, and `license` (SPDX identifier) in `Cargo.toml`
10. **`cargo login`**: authenticates with crates.io using an API token stored in `~/.cargo/credentials.toml`
11. **`cargo publish`**: uploads the crate; the publish is permanent
12. **SemVer versioning**: version field in `Cargo.toml` follows semantic versioning; change it before republishing
13. **`cargo yank --vers X.Y.Z`**: prevents new projects from depending on a version; `--undo` reverses it; does not delete code
14. **Workspace `Cargo.toml`**: has `[workspace]` with `members` list instead of `[package]`; `resolver = "3"` recommended
15. **Shared `Cargo.lock`**: all workspace crates use the same dependency versions, ensuring compatibility
16. **Shared `target/`**: workspace crates compile into one directory, avoiding redundant rebuilds
17. **`-p` flag**: selects a specific package in a workspace for `cargo run`, `cargo test`, or `cargo publish`
18. **`cargo install`**: installs binary crates to `$HOME/.cargo/bin`; only works for packages with binary targets
19. **Custom subcommands**: any binary named `cargo-something` in `$PATH` becomes `cargo something`

# Construction / Recognition

## Customizing Release Profiles:
```toml
[profile.dev]
opt-level = 1

[profile.release]
opt-level = 3
```

## Writing Documentation Comments:
```rust
/// Adds one to the number given.
///
/// # Examples
///
/// ```
/// let arg = 5;
/// let answer = my_crate::add_one(arg);
/// assert_eq!(6, answer);
/// ```
pub fn add_one(x: i32) -> i32 {
    x + 1
}
```

## Crate-Level Documentation:
```rust
//! # My Crate
//!
//! `my_crate` is a collection of utilities to make performing
//! certain calculations more convenient.
```

## Re-Exporting with `pub use`:
```rust
// src/lib.rs
pub use self::kinds::PrimaryColor;
pub use self::kinds::SecondaryColor;
pub use self::utils::mix;

pub mod kinds { /* ... */ }
pub mod utils { /* ... */ }
```
Users can then write `use art::PrimaryColor;` instead of `use art::kinds::PrimaryColor;`.

## Setting Up a Workspace:
```toml
# Cargo.toml (workspace root)
[workspace]
resolver = "3"
members = ["adder", "add_one"]
```

```text
add/
  Cargo.lock          # shared
  Cargo.toml          # workspace definition
  target/             # shared output
  adder/
    Cargo.toml
    src/main.rs
  add_one/
    Cargo.toml
    src/lib.rs
```

## Inter-Crate Dependencies in a Workspace:
```toml
# adder/Cargo.toml
[dependencies]
add_one = { path = "../add_one" }
```

## Publishing a Crate:
```toml
[package]
name = "guessing_game"
version = "0.1.0"
edition = "2024"
description = "A fun game where you guess what number the computer has chosen."
license = "MIT OR Apache-2.0"
```
```console
$ cargo publish
```

## Installing a Binary Crate:
```console
$ cargo install ripgrep
```

# Context & Application

Chapter 14 covers the Cargo features needed to take a Rust project from local development to production and publication. These are the tools for building release binaries, maintaining documentation that stays synchronized with code, organizing large codebases, and sharing work with the Rust ecosystem.

**Practical contexts:**
- Configuring optimization levels for development speed vs. release performance
- Writing documentation that doubles as tested examples
- Using `pub use` to present a clean API without constraining internal architecture
- Managing monorepo-style projects with workspaces
- Publishing and versioning open-source crates
- Installing community tools like `ripgrep`, `cargo-edit`, `cargo-watch`

**The dual license convention:** "Many people in the Rust community license their projects in the same way as Rust by using a dual license of `MIT OR Apache-2.0`" (Ch. 14, "Adding Metadata to a New Crate").

**Workspace design guidance:** "As your project grows, consider using a workspace: It enables you to work with smaller, easier-to-understand components than one big blob of code" (Ch. 14, "Cargo Workspaces").

# Examples

**Example 1** (Ch. 14, "Customizing Builds with Release Profiles"): Default `opt-level` values -- `0` for dev, `3` for release. Overriding to `opt-level = 1` in `[profile.dev]` applies moderate optimization during development.

**Example 2** (Ch. 14, Listing 14-1): A documentation comment for `add_one` with an `# Examples` section containing `assert_eq!(6, answer)`. Running `cargo test` compiles and executes this code block as a doc test.

**Example 3** (Ch. 14, Listing 14-2): Using `//!` at the top of `src/lib.rs` to document the crate as a whole. These comments display on the front page of the generated documentation.

**Example 4** (Ch. 14, Listings 14-3 through 14-6): The `art` crate uses `pub use` to re-export `PrimaryColor`, `SecondaryColor`, and `mix` from nested modules to the crate root. Users benefit from `use art::PrimaryColor` instead of `use art::kinds::PrimaryColor`.

**Example 5** (Ch. 14, "Creating a Workspace"): A workspace with `adder` (binary) and `add_one` (library) sharing a `Cargo.lock` and `target/` directory. Running `cargo run -p adder` targets a specific package.

**Example 6** (Ch. 14, "Depending on an External Package"): Adding `rand` to `add_one/Cargo.toml` within a workspace does not make it available to `adder` -- each crate must declare its own dependencies, but Cargo resolves them to a single version.

**Example 7** (Ch. 14, "Installing Binaries"): `cargo install ripgrep` compiles and installs the `rg` binary to `$HOME/.cargo/bin`.

# Relationships

## Builds Upon
- **Modules and Crates** -- `pub use`, workspace member organization, and crate publication depend on understanding the module system
- **Cargo Dependencies** -- workspaces extend the dependency model to multi-crate projects

## Enables
- **Crate publication** -- the full publishing workflow from documentation to crates.io
- **Monorepo management** -- workspaces enable multi-crate development with shared dependencies

## Related
- **Testing** -- doc tests bridge documentation and testing; workspace `cargo test` runs all crate tests
- **Generics, Traits, and Lifetimes** -- doc comment examples often demonstrate generic APIs

## Contrasts With
- None within this source

# Common Errors

- **Error**: Expecting `cargo publish` to work without a `description` and `license` in `Cargo.toml`.
  **Correction**: Both fields are required by crates.io. The `license` field uses SPDX identifiers (e.g., `MIT`, `MIT OR Apache-2.0`).

- **Error**: Assuming crates in a workspace automatically depend on each other.
  **Correction**: Dependencies between workspace members must be explicitly declared with path dependencies in each crate's `Cargo.toml`.

- **Error**: Placing `pub use` in the wrong file -- expecting re-exports in a binary crate to be usable by external consumers.
  **Correction**: `pub use` re-exports are meaningful in library crates (`src/lib.rs`). Binary crates don't expose a public API.

- **Error**: Trying to delete a published crate version from crates.io.
  **Correction**: Published versions are permanent. Use `cargo yank` to prevent new projects from depending on a broken version. Yanked versions remain available for existing users.

# Common Confusions

- **Confusion**: Thinking `cargo yank` deletes code from crates.io.
  **Clarification**: Yanking only prevents new `Cargo.lock` files from including that version. Existing projects with the yanked version in their `Cargo.lock` continue to work. Accidentally uploaded secrets must be rotated immediately.

- **Confusion**: Believing workspace crates share dependencies implicitly.
  **Clarification**: Each crate in a workspace must declare its own dependencies. The shared `Cargo.lock` ensures version consistency, but `use` statements only work for declared dependencies.

- **Confusion**: Thinking `///` and `//!` are interchangeable.
  **Clarification**: `///` documents the item that follows the comment (functions, structs, etc.). `//!` documents the item that contains the comment (the crate root or a module).

- **Confusion**: Assuming doc test code blocks run in isolation without access to the crate.
  **Clarification**: Doc tests are compiled as external tests that `use` the crate. They test the public API and verify that examples actually work.

# Source Reference

Chapter 14: More About Cargo and Crates.io. Sections: "Customizing Builds with Release Profiles," "Publishing a Crate to Crates.io" (documentation comments, doc sections, doc tests, contained item comments, `pub use`, account setup, metadata, publishing, new versions, yanking), "Cargo Workspaces" (creating, second package, external dependencies, testing), "Installing Binaries with `cargo install`," "Extending Cargo with Custom Commands." No page numbers (online documentation source).

# Verification Notes

- Release profile definition: directly quoted from Ch. 14 "Customizing Builds with Release Profiles" opening
- Doc test quote: directly quoted from "Documentation Comments as Tests" section
- `pub use` definition: directly quoted from "Exporting a Convenient Public API" section
- Workspace definition: directly quoted from "Creating a Workspace" section
- Publishing permanence and yanking: directly quoted from "Publishing to Crates.io" and "Deprecating Versions" sections
- Confidence: HIGH -- Ch. 14 provides explicit definitions, complete command examples, and working project structures for every feature
- Cross-references: all slug references correspond to planned or existing concept cards
- Uncertainties: Full list of profile configuration options is deferred to Cargo documentation; custom commands section is brief
