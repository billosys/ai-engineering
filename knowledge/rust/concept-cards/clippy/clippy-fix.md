---
# === CORE IDENTIFICATION ===
concept: Clippy Fix
slug: clippy-fix

# === CLASSIFICATION ===
category: tooling
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Clippy Documentation"
source_slug: clippy
authors: "The Clippy Contributors"
chapter: "01-getting-started"
chapter_number: 1
pdf_page: null
section: "Usage"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "cargo clippy --fix"
  - "auto-fix"
  - "automatic suggestions"
  - "machine-applicable fix"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clippy
  - cargo-clippy
extends: []
related:
  - clippy-lint-levels
  - clippy-lint-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I automatically fix Clippy warnings?"
  - "What does cargo clippy --fix do?"
  - "Does --fix apply all Clippy suggestions?"
  - "What does --fix imply about build targets?"
---

# Quick Definition

`cargo clippy --fix` automatically applies machine-applicable Clippy lint suggestions to source code, modifying files in place. It implies `--all-targets`, so it attempts to fix as much code as possible across all build targets.

# Core Definition

Clippy can automatically apply some of its lint suggestions, similar to how the Rust compiler's `cargo fix` command works. The `--fix` flag is passed to `cargo clippy`, which then modifies source files in place to resolve lint violations that have machine-applicable suggestions.

The documentation notes that `--fix` implies `--all-targets`, meaning it will check and fix code across all build targets (lib, bin, tests, examples, benches) in a single invocation.

Not all Clippy lints have automatic fixes. Only lints where the suggested replacement is unambiguous and safe to apply automatically (machine-applicable suggestions) will be fixed. Other lints will still be reported as warnings or errors but must be fixed manually.

# Prerequisites

- **clippy** -- Clippy must be installed to use the fix feature
- **cargo-clippy** -- The fix flag is passed through `cargo clippy`

# Key Properties

1. Invoked with `cargo clippy --fix`
2. Modifies source files in place -- changes are written directly to disk
3. Implies `--all-targets` to fix as much code as possible
4. Only applies machine-applicable suggestions -- not all lints can be auto-fixed
5. Works like the compiler's `cargo fix` but applies Clippy-specific lints
6. Can be combined with other cargo flags (e.g., `--allow-dirty`, `--allow-staged`)

# Construction / Recognition

## To Auto-Fix Clippy Warnings:
1. Run `cargo clippy --fix` to apply all machine-applicable suggestions
2. Review the changes made to source files
3. Any remaining warnings must be fixed manually

## To Recognize Auto-Fixable Lints:
1. Run `cargo clippy` normally first
2. Lints with the "help: try" suggestion followed by code are typically machine-applicable
3. The Clippy lint list indicates which lints have auto-fix support

# Context & Application

Auto-fixing is particularly useful when adopting new lint groups or upgrading Clippy versions that introduce new lints. Instead of manually fixing dozens or hundreds of style issues, `cargo clippy --fix` can handle the mechanical changes, leaving developers to focus on lints that require judgment.

Because `--fix` modifies files in place, it is best used on a clean working tree (no uncommitted changes) or with version control so changes can be reviewed and reverted if needed.

The `--all-targets` implication means that test-only code, example code, and benchmark code are also fixed, providing comprehensive coverage in a single command.

# Examples

**Example 1**: Running Clippy auto-fix:
```bash
cargo clippy --fix
```

**Example 2**: Running auto-fix on a dirty working tree:
```bash
cargo clippy --fix --allow-dirty
```

**Example 3**: Typical workflow -- run fix, then verify no remaining warnings:
```bash
cargo clippy --fix
cargo clippy  # verify all fixable issues are resolved
```

# Relationships

## Builds Upon
- **clippy** -- Auto-fix is a Clippy feature
- **cargo-clippy** -- The `--fix` flag is passed through `cargo clippy`

## Related
- **clippy-lint-levels** -- Fixed lints must still be at warn or deny level to trigger auto-fix
- **clippy-lint-groups** -- Enabling additional groups may reveal more auto-fixable issues

# Common Errors

- **Error**: Running `cargo clippy --fix` on a dirty working tree and getting an error about uncommitted changes.
  **Correction**: Either commit or stash your changes first, or pass `--allow-dirty` (and/or `--allow-staged`) to override the safety check.

- **Error**: Expecting `--fix` to resolve all Clippy warnings automatically.
  **Correction**: Only machine-applicable suggestions are auto-fixed. Manual intervention is required for lints without a clear automatic fix.

# Common Confusions

- **Confusion**: Thinking `cargo clippy --fix` and `cargo fix` are the same command.
  **Clarification**: `cargo fix` applies rustc compiler suggestions. `cargo clippy --fix` applies Clippy lint suggestions. They target different sets of diagnostics, though both modify source files in place.

- **Confusion**: Assuming `--fix` only fixes code in the lib/bin targets.
  **Clarification**: `--fix` implies `--all-targets`, so it fixes code across all targets including tests, examples, and benchmarks.

# Source Reference

Chapter 1 (Getting Started), "Usage" section, subsection "Automatically applying Clippy suggestions" at lines 139-146 of 01-getting-started.md.

# Verification Notes

- Command syntax: Directly from source -- `cargo clippy --fix`
- `--all-targets` implication: Directly stated -- "--fix implies --all-targets, so it can fix as much code as it can"
- Machine-applicable limitation: Standard behavior consistent with cargo fix and documented Clippy behavior
- Confidence: HIGH -- command and behavior directly from source
- Cross-references: All slugs verified against planned extractions
