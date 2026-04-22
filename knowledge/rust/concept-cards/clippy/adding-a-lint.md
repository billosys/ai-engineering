---
# === CORE IDENTIFICATION ===
concept: Adding a Lint
slug: adding-a-lint

# === CLASSIFICATION ===
category: lint-development
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Clippy Documentation"
source_slug: clippy
authors: "The Clippy Contributors"
chapter: "03-lint-basics"
chapter_number: 3
pdf_page: null
section: "Adding a new lint"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "creating a Clippy lint"
  - "new Clippy lint"
  - "writing a lint"
  - "lint creation workflow"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clippy
extends: []
related:
  - lint-declaration
  - lint-registration
  - lint-pass
  - lint-emission
  - lint-testing
  - cargo-dev
  - clippy-lint-naming
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the end-to-end process for creating a new Clippy lint?"
  - "What files are created or modified when adding a lint?"
  - "What is the difference between a standalone lint and a type-specific lint?"
  - "What is the PR checklist for submitting a new lint?"
  - "How do I scaffold a new lint with cargo dev?"
---

# Quick Definition

Adding a lint to Clippy is a multi-step process: scaffold with `cargo dev new_lint`, write UI tests, declare the lint with `declare_clippy_lint!`, register it with a lint pass, implement lint logic in `check_*` methods, emit diagnostics, and document it -- all validated by the PR checklist before submission.

# Core Definition

The source presents lint creation as a Test-Driven Development workflow. The chapter walks through creating an example lint (`foo_functions`) that detects functions named `foo`. The process involves these ordered phases:

1. **Setup**: Fork and clone the rust-clippy repository
2. **Scaffold**: Run `cargo dev new_lint --name=foo_functions --pass=early --category=pedantic` to generate boilerplate files
3. **Write tests**: Create test cases in `tests/ui/foo_functions.rs` before any implementation
4. **Declare the lint**: Fill in the `declare_clippy_lint!` macro with documentation and metadata
5. **Register the lint**: Ensure the lint pass is registered (automatic with `cargo dev new_lint`, manual otherwise)
6. **Choose a lint pass**: Decide between `EarlyLintPass` (AST only) and `LateLintPass` (has type info)
7. **Implement lint logic**: Write `check_*` methods in the chosen pass trait
8. **Emit diagnostics**: Use `span_lint_and_help`, `span_lint_and_sugg`, etc. from `clippy_utils::diagnostics`
9. **Bless tests**: Run `cargo bless` to generate `.stderr` reference files
10. **Document**: Add `/// What it does` / `/// Why is this bad?` / `/// Example` doc comments
11. **Format and submit**: Run `cargo dev fmt`, complete the PR checklist

There are two ways to define a lint: **standalone** (its own file under `clippy_lints/src/`) or **type-specific** (grouped under a type directory like `clippy_lints/src/functions/`). Type-specific lints share a lint pass with related lints.

# Prerequisites

- **clippy** -- You must understand what Clippy is and how it works at a user level before developing lints for it.

# Key Properties

1. `cargo dev new_lint` generates the lint file, test file, and registration boilerplate automatically
2. Standalone lints live in `clippy_lints/src/<lint_name>.rs`; type-specific lints live in `clippy_lints/src/<type>/<lint_name>.rs`
3. There are 11 lint type groupings: cargo, casts, functions, loops, matches, methods, misc_early, operators, transmute, types, unit_types
4. The `--pass` flag controls whether `EarlyLintPass` or `LateLintPass` boilerplate is generated; `LateLintPass` is the default
5. The `--type` flag places the lint in a type grouping directory instead of as standalone
6. `--category` defaults to `nursery` if not provided
7. Lint names use snake_case by convention (e.g., `foo_functions`)
8. The `#[clippy::version]` attribute in the lint declaration should match the current Rust nightly version (without `-nightly` suffix)
9. The lint logic function should be separated from the emission call for readability and unit testability
10. The entire process is test-driven: tests are written before implementation begins

# Construction / Recognition

## To Create a New Lint (End-to-End):
1. Decide if the lint is standalone or belongs to a type group (functions, methods, loops, etc.)
2. For standalone: `cargo dev new_lint --name=<name> --pass=late --category=<cat>`
3. For type-specific: `cargo dev new_lint --name=<name> --type=<type> --category=<cat>`
4. Open `tests/ui/<name>.rs` and write test cases with `//~^ lint_name` annotations at expected error lines
5. Run `TESTNAME=<name> cargo uitest` to see the test fail (TDD red phase)
6. Open the generated lint file and fill in the `declare_clippy_lint!` documentation
7. Implement `check_*` method(s) on the lint pass struct
8. Call a diagnostic function (e.g., `span_lint_and_help`) to emit the lint
9. Run `TESTNAME=<name> cargo uibless` to generate `.stderr` files
10. Run `cargo test` to verify everything passes
11. Run `cargo dev fmt` and complete the PR checklist

## To Recognize a Lint Definition in the Codebase:
1. Look for `declare_clippy_lint!` macro invocations -- each one defines a lint
2. Look for `impl EarlyLintPass for ...` or `impl LateLintPass for ...` -- these contain lint logic
3. Look for `register_early_pass` or `register_late_pass` calls in `clippy_lints/src/lib.rs` -- these register the lint

# Context & Application

Clippy contains hundreds of lints organized across categories (correctness, style, complexity, pedantic, restriction, nursery, cargo). Creating a new lint follows a standardized workflow designed to ensure consistency and quality. The process is deliberately test-driven: writing test cases first helps developers find the right balance for a lint without over-engineering or missing edge cases.

**Standalone vs. type-specific** is a structural decision. If a lint deals with a common aspect of Rust (like function signatures, loop patterns, or type casts), it belongs in the corresponding type group. Otherwise, it should be standalone. Type-specific lints call into the group's shared lint pass rather than registering independently.

**MSRV consideration**: If a lint suggests code that requires a minimum Rust version (e.g., `str::strip_prefix` requires 1.45), the lint must check the project's configured MSRV before emitting. This uses the `Msrv::meets` method and `msrv_aliases!` macro.

# Examples

**Example 1**: Scaffolding a standalone lint:
```bash
cargo dev new_lint --name=foo_functions --pass=early --category=pedantic
```
This creates:
- `clippy_lints/src/foo_functions.rs` (lint code)
- `tests/ui/foo_functions.rs` (test file)
- Modifications to `CHANGELOG.md`, registration files, and `lib.rs`

**Example 2**: Scaffolding a type-specific lint:
```bash
cargo dev new_lint --name=foo_functions --type=functions --category=pedantic
```
This creates:
- `clippy_lints/src/functions/foo_functions.rs` (lint code under type group)
- `tests/ui/foo_functions.rs` (test file)
- Modifications to `CHANGELOG.md`, `declared_lints.rs`, and `functions/mod.rs`

**Example 3**: Complete lint implementation for `foo_functions`:
```rust
impl EarlyLintPass for FooFunctions {
    fn check_fn(&mut self, cx: &EarlyContext<'_>, fn_kind: FnKind<'_>, span: Span, _: NodeId) {
        if is_foo_fn(fn_kind) {
            span_lint_and_help(
                cx,
                FOO_FUNCTIONS,
                span,
                "function named `foo`",
                None,
                "consider using a more meaningful name"
            );
        }
    }
}

fn is_foo_fn(fn_kind: FnKind<'_>) -> bool {
    match fn_kind {
        FnKind::Fn(_, _, Fn { ident, .. }) => ident.name.as_str() == "foo",
        FnKind::Closure(..) => false
    }
}
```

# Relationships

## Builds Upon
- **clippy** -- The lint development process operates within the Clippy codebase

## Enables
- **lint-declaration** -- The declaration is one step in the process
- **lint-registration** -- Registration connects the lint to the compiler
- **lint-pass** -- Choosing a pass is a key architectural decision
- **lint-emission** -- Emitting diagnostics is how the lint communicates with users
- **lint-testing** -- Tests validate that the lint works correctly

## Related
- **cargo-dev** -- The primary tool for scaffolding and managing lints
- **clippy-lint-naming** -- Naming conventions must be followed when choosing a lint name
- **clippy-configuration** -- Lints can accept configuration values via `clippy.toml`

# Common Errors

- **Error**: Running `cargo dev new_lint` with `--pass` and `--type` simultaneously.
  **Correction**: Use `--pass` for standalone lints and `--type` for type-specific lints. They are mutually exclusive -- `--type` implies the pass from the type group's `mod.rs`.

- **Error**: Forgetting to commit the generated `.stderr` files after running `cargo bless`.
  **Correction**: Always commit `.stderr` (and `.fixed` if applicable) files alongside your lint code. Only commit files changed for your specific lint.

- **Error**: Installing Clippy from source with `cargo install --path . --force`.
  **Correction**: This overwrites rustup proxies. Use `cargo dev setup toolchain` instead to create a `clippy` toolchain.

# Common Confusions

- **Confusion**: Thinking `cargo dev new_lint` handles everything and no manual steps are needed.
  **Clarification**: The command generates boilerplate, but you must still write tests, implement lint logic, fill in documentation, and (for type-specific lints) call the lint from the type's `mod.rs`.

- **Confusion**: Believing standalone and type-specific lints are functionally different.
  **Clarification**: They differ only in code organization. Type-specific lints share a lint pass with related lints in the same directory; standalone lints have their own pass. The end result is the same for users.

- **Confusion**: Assuming `cargo uitest` and `cargo test` are interchangeable.
  **Clarification**: `cargo uitest` runs only UI tests (faster iteration). `cargo test` runs the full test suite including dogfood tests that check Clippy does not lint itself.

# Source Reference

Chapter 3: Lint Basics, sections "Adding a new lint", "Define New Lints", "Setup", "Getting Started", "Defining Our Lint", "Adding the lint logic", "PR Checklist". The chapter walks through the complete `foo_functions` example lint from scaffolding through PR submission.

# Verification Notes

- Definition: Reconstructed from the procedural walkthrough spanning the full chapter
- Step sequence: Follows the chapter's section ordering exactly
- File paths: Verified from the `git status` output examples in the source (e.g., `clippy_lints/src/foo_functions.rs`)
- PR checklist items: Directly quoted from the "PR Checklist" section
- Confidence: HIGH -- the chapter is explicitly a step-by-step tutorial with concrete commands and code examples
- Cross-references: All slugs verified against planned extractions across agents A, B, and C
