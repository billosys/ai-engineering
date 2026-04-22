---
# === CORE IDENTIFICATION ===
concept: cargo dev
slug: cargo-dev

# === CLASSIFICATION ===
category: tooling
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Clippy Documentation"
source_slug: clippy
authors: "The Clippy Contributors"
chapter: "03-lint-basics"
chapter_number: 3
pdf_page: null
section: "cargo dev"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "cargo dev tools"
  - "Clippy dev tools"
  - "cargo dev new_lint"
  - "cargo dev update_lints"
  - "cargo dev fmt"
  - "cargo dev dogfood"
  - "cargo dev deprecate"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clippy
extends: []
related:
  - adding-a-lint
  - lint-testing
  - lint-registration
  - cargo-clippy
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the cargo dev tool in Clippy?"
  - "What commands does cargo dev provide?"
  - "How do I scaffold a new lint?"
  - "How do I format the Clippy codebase?"
  - "How do I set up Clippy for local development?"
  - "How do I deprecate a lint?"
---

# Quick Definition

`cargo dev` is the Clippy developer toolchain providing commands for creating lints (`new_lint`), updating registrations (`update_lints`), formatting code (`fmt`), running dogfood tests (`dogfood`), deprecating lints (`deprecate`), setting up git hooks (`setup git-hook`), configuring IDE support (`setup intellij`), setting up local toolchains (`setup toolchain`), and running Clippy on arbitrary code (`lint`).

# Core Definition

The source describes `cargo dev` as "dev tools to make working on Clippy more convenient." These tools are accessed through the `cargo dev` command, with `--help` available on each subcommand.

The primary commands are:

| Command | Purpose |
|---------|---------|
| `cargo dev new_lint` | Create a new lint with all boilerplate and register it |
| `cargo dev update_lints` | Register or update lint names, groups, and related metadata |
| `cargo dev fmt` | Format the entire Clippy codebase and all tests |
| `cargo dev dogfood` | Run dogfood tests (ensure Clippy does not lint itself) |
| `cargo dev deprecate` | Deprecate a lint and attempt to remove its code |
| `cargo dev setup git-hook` | Auto-format code before each commit |
| `cargo dev setup intellij` | (Experimental) Set up Clippy for RustRover IDE |
| `cargo dev setup toolchain` | Build Clippy and install it as a rustup toolchain |
| `cargo dev lint` | Run Clippy with local modifications on a file or project |
| `cargo dev serve` | Render and serve lint documentation locally in a browser |

The `new_lint` command is the most important for lint development. It accepts:
- `--name=<name>`: The lint name in snake_case
- `--pass=early|late`: The lint pass type (default: `late`)
- `--type=<type>`: Place the lint in a type group directory (mutually exclusive with `--pass`)
- `--category=<cat>`: The lint category (default: `nursery`)

# Prerequisites

- **clippy** -- The `cargo dev` tools operate within a Clippy development checkout.

# Key Properties

1. `cargo dev new_lint` generates the lint file, test file, and all registration boilerplate
2. `cargo dev update_lints` synchronizes lint registrations after manual changes
3. `cargo dev fmt` formats code using nightly rustfmt -- required before PR submission
4. `cargo dev dogfood` validates that Clippy does not produce warnings on its own codebase
5. `cargo dev deprecate` handles the boilerplate of deprecating a lint
6. `cargo dev setup toolchain` creates a `clippy` rustup toolchain for local testing
7. `cargo dev lint input.rs` runs Clippy on a single file with local modifications
8. `cargo dev lint /path/to/project` runs Clippy on an entire project
9. `cargo dev serve` renders lint documentation locally for preview
10. All subcommands support `--help` for detailed usage information

# Construction / Recognition

## To Scaffold a New Standalone Lint:
1. `cargo dev new_lint --name=foo_functions --pass=early --category=pedantic`
2. This creates `clippy_lints/src/foo_functions.rs` and `tests/ui/foo_functions.rs`
3. It also modifies `CHANGELOG.md`, registration files, and `lib.rs`

## To Scaffold a Type-Specific Lint:
1. `cargo dev new_lint --name=foo_functions --type=functions --category=pedantic`
2. This creates `clippy_lints/src/functions/foo_functions.rs` and `tests/ui/foo_functions.rs`
3. It modifies `CHANGELOG.md`, `declared_lints.rs`, and `functions/mod.rs`

## To Set Up a Local Testing Environment:
1. `cargo dev setup toolchain` -- creates a `clippy` toolchain
2. In any project: `cargo +clippy clippy` -- runs your local Clippy build
3. To uninstall: `rustup toolchain uninstall clippy`

## To Format and Validate Before a PR:
1. `cargo dev fmt` -- format all code
2. `cargo dev dogfood` -- verify no self-linting issues
3. `cargo dev update_lints` -- ensure registrations are up to date

# Context & Application

`cargo dev` centralizes the developer experience for Clippy contributors. Without it, creating a new lint would require manually creating files, adding imports, declaring the lint, registering it, and setting up test infrastructure. The toolchain reduces this to a single command.

**Key workflow integration points**:

- **PR checklist**: The checklist requires running `cargo dev update_lints` and `cargo dev fmt` before submission
- **Manual testing**: `cargo dev lint` provides an alternative to the test suite when debugging with `println!` makes test output unreadable
- **Local installation**: `cargo dev setup toolchain` is the safe way to test Clippy locally. The source explicitly warns: "DO NOT install using `cargo install --path . --force` since this will overwrite rustup proxies."
- **Documentation preview**: `cargo dev serve` lets you view how your lint documentation will appear on the Clippy lint list before submitting

**Lintcheck** is a related but separate tool accessed via `cargo lintcheck` (not `cargo dev lintcheck`). It builds and runs Clippy on a fixed set of real-world crates to validate against false positives.

# Examples

**Example 1**: Creating a standalone pedantic lint:
```bash
cargo dev new_lint --name=foo_functions --pass=early --category=pedantic
```

**Example 2**: Creating a type-specific lint:
```bash
cargo dev new_lint --name=foo_functions --type=functions --category=pedantic
```

**Example 3**: Development workflow commands:
```bash
# Format code
cargo dev fmt

# Run dogfood tests
cargo dev dogfood

# Test against a single file
cargo dev lint input.rs

# Test against a project
cargo dev lint /path/to/project

# Set up local toolchain
cargo dev setup toolchain

# Preview documentation
cargo dev serve
```

# Relationships

## Builds Upon
- **clippy** -- `cargo dev` is the developer toolchain for the Clippy project

## Enables
- **adding-a-lint** -- `cargo dev new_lint` is the first step in creating a lint
- **lint-registration** -- `cargo dev update_lints` synchronizes registrations
- **lint-testing** -- `cargo dev dogfood`, `cargo dev lint`, and toolchain setup support testing

## Related
- **cargo-clippy** -- `cargo +clippy clippy` runs Clippy using the locally built toolchain
- **lint-declaration** -- `cargo dev new_lint` generates the `declare_clippy_lint!` boilerplate

# Common Errors

- **Error**: Using `cargo install --path . --force` to install Clippy locally.
  **Correction**: This overwrites rustup proxies (`~/.cargo/bin/cargo-clippy` and `~/.cargo/bin/clippy-driver`). Use `cargo dev setup toolchain` instead. If proxies are damaged, run `rustup update` to repair.

- **Error**: Forgetting to run `cargo dev fmt` before submitting a PR.
  **Correction**: Clippy CI requires nightly `rustfmt` formatting. Run `cargo dev fmt` and ensure `rustfmt` is installed: `rustup component add rustfmt --toolchain=nightly`.

- **Error**: Using `--pass` and `--type` flags simultaneously with `cargo dev new_lint`.
  **Correction**: These are mutually exclusive. Use `--pass` for standalone lints and `--type` for type-specific lints.

# Common Confusions

- **Confusion**: Thinking `cargo dev update_lints` fully replaces manual registration.
  **Clarification**: It updates lint names, groups, and declared_lints, but may not register the lint pass in `lib.rs` because multiple lints can share a pass and ordering matters.

- **Confusion**: Believing `cargo dev lint` is the same as `cargo clippy`.
  **Clarification**: `cargo dev lint` runs the locally built Clippy with modifications directly. `cargo clippy` runs the installed Clippy. To use your local build via `cargo clippy`, you need `cargo dev setup toolchain` first, then `cargo +clippy clippy`.

- **Confusion**: Thinking `cargo lintcheck` is a `cargo dev` subcommand.
  **Clarification**: Lintcheck is a separate tool invoked directly as `cargo lintcheck`, not as `cargo dev lintcheck`.

# Source Reference

Chapter 3: Lint Basics, sections "cargo dev", "Install from source", "Testing manually", and "Running rustfmt". The command table is reconstructed from the "cargo dev" section. The `new_lint` flags are documented across the "Getting Started", "Standalone", and "Specific Type" sections.

# Verification Notes

- Command list: All commands directly listed in the "cargo dev" section of the source
- new_lint flags: `--name`, `--pass`, `--type`, `--category` all documented with examples
- Installation warning: Directly quoted -- "DO NOT install using cargo install --path . --force"
- PR checklist items: `cargo dev update_lints` and `cargo dev fmt` are on the PR checklist
- cargo lintcheck: Source places this separately from `cargo dev` commands
- Confidence: HIGH -- the section provides a comprehensive command listing with descriptions
- Cross-references: All slugs verified against planned extractions across agents
