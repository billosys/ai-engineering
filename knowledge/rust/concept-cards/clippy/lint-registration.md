---
# === CORE IDENTIFICATION ===
concept: Lint Registration
slug: lint-registration

# === CLASSIFICATION ===
category: lint-development
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Clippy Documentation"
source_slug: clippy
authors: "The Clippy Contributors"
chapter: "03-lint-basics"
chapter_number: 3
pdf_page: null
section: "Lint registration"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "register_early_pass"
  - "register_late_pass"
  - "lint pass registration"
  - "registering a lint"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lint-declaration
  - lint-pass
extends: []
related:
  - adding-a-lint
  - early-lint-pass
  - late-lint-pass
  - cargo-dev
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I register a lint pass with the Clippy compiler?"
  - "What is the difference between register_early_pass and register_late_pass?"
  - "Why isn't my lint running even though I declared it?"
  - "Does cargo dev new_lint handle registration automatically?"
  - "Why does registration order matter?"
---

# Quick Definition

Lint registration is the process of connecting a declared lint pass to the Clippy compiler pipeline by calling `store.register_early_pass()` or `store.register_late_pass()` in `clippy_lints/src/lib.rs`. Without registration, a lint pass will not execute.

# Core Definition

The source explains: "Without a call to one of `register_early_pass` or `register_late_pass`, the lint pass in question will not be run."

Registration happens in the `register_lints` function in `clippy_lints/src/lib.rs`. When using `cargo dev new_lint`, registration is handled automatically. When declaring a lint by hand, you must either register manually or run `cargo dev update_lints`.

For an early pass:
```rust
store.register_early_pass(|| Box::new(foo_functions::FooFunctions));
```

For a late pass:
```rust
store.register_late_pass(|_| Box::new(foo_functions::FooFunctions));
```

The source identifies two reasons why `cargo dev update_lints` does not always automate registration of the lint pass:

1. **Multiple lints per pass**: Multiple lints can share the same lint pass struct, so the pass may already be registered when adding a new lint to an existing group.
2. **Ordering matters**: The order that passes are registered determines the order they run, which affects the order of emitted lint output.

For lints with configuration, registration passes the configuration:
```rust
store.register_late_pass(move || Box::new(module::StructName::new(conf)));
```

# Prerequisites

- **lint-declaration** -- A lint must be declared with `declare_clippy_lint!` before it can be registered.
- **lint-pass** -- The pass struct (from `declare_lint_pass!` or manual definition) must exist before registration.

# Key Properties

1. Registration is required -- without it, the lint pass will not run
2. `cargo dev new_lint` handles registration automatically for new standalone lints
3. `cargo dev update_lints` can assist with registration but may require manual steps
4. Registration happens in `clippy_lints/src/lib.rs` in the `register_lints` function
5. `register_early_pass` takes a closure returning `Box::new(YourStruct)` with no arguments
6. `register_late_pass` takes a closure with `|_|` (ignoring the config parameter) returning `Box::new(YourStruct)`
7. Registration order determines the order lints appear in output
8. Multiple lints can share one registered pass (type-specific lint groups do this)
9. For configured lints, the closure captures `conf` with `move` and passes it to the constructor
10. Type-specific lints (created with `--type`) are not registered in the traditional sense; they are called from the type group's existing pass

# Construction / Recognition

## To Register a Lint Pass Manually:
1. Open `clippy_lints/src/lib.rs`
2. Find the `register_lints` function
3. Add `store.register_early_pass(|| Box::new(module::LintStruct));` for early passes
4. Or add `store.register_late_pass(|_| Box::new(module::LintStruct));` for late passes
5. For configured lints: `store.register_late_pass(move || Box::new(module::LintStruct::new(conf)));`

## To Register a Lint Automatically:
1. Use `cargo dev new_lint` which handles registration as part of scaffolding
2. If adding a lint by hand, run `cargo dev update_lints` afterwards
3. Verify registration by searching for your struct name in `lib.rs`

## To Diagnose a Lint Not Running:
1. Check that `register_early_pass` or `register_late_pass` is called with your struct
2. Verify the correct pass type (early vs. late) matches your trait implementation
3. For type-specific lints, verify the lint is called from the type group's `mod.rs`

# Context & Application

Registration is the critical bridge between lint declaration and lint execution. A fully implemented lint that is not registered is effectively invisible to the compiler. This is a common source of confusion for new contributors.

**Standalone vs. type-specific registration**: Standalone lints are registered directly in `lib.rs`. Type-specific lints (created with `cargo dev new_lint --type=<type>`) do not get their own registration; instead, they are called from within the type group's shared lint pass in `clippy_lints/src/<type>/mod.rs`. The type group's pass is already registered.

**Registration ordering**: Since registration order affects output order, maintainers care about where new registrations are placed. This is another reason the step is not fully automated -- positioning matters.

**Files modified by `cargo dev new_lint` (standalone)**:
- `clippy_lints/src/lib.register_lints.rs` -- lint constant registration
- `clippy_lints/src/lib.register_<category>.rs` -- category-specific registration
- `clippy_lints/src/lib.rs` -- pass registration

**Files modified by `cargo dev new_lint --type=<type>`**:
- `clippy_lints/src/declared_lints.rs` -- lint constant declaration
- `clippy_lints/src/<type>/mod.rs` -- lint called from shared pass

# Examples

**Example 1**: Registering an early lint pass:
```rust
store.register_early_pass(|| Box::new(foo_functions::FooFunctions));
```

**Example 2**: Registering a late lint pass:
```rust
store.register_late_pass(|_| Box::new(foo_functions::FooFunctions));
```

**Example 3**: Registering a configured late lint pass:
```rust
store.register_late_pass(move || Box::new(module::StructName::new(conf)));
```

# Relationships

## Builds Upon
- **lint-declaration** -- The lint constant and pass struct must be declared before registration
- **lint-pass** -- Registration connects the pass struct to the compiler pipeline

## Enables
- **lint-emission** -- Without registration, the pass never runs and no diagnostics are emitted

## Related
- **early-lint-pass** -- Early passes are registered with `register_early_pass`
- **late-lint-pass** -- Late passes are registered with `register_late_pass`
- **cargo-dev** -- `cargo dev new_lint` and `cargo dev update_lints` automate registration
- **adding-a-lint** -- Registration is a step in the lint creation workflow

# Common Errors

- **Error**: Declaring a lint and implementing the pass but forgetting to register it.
  **Correction**: Add `store.register_early_pass(|| Box::new(...))` or `store.register_late_pass(|_| Box::new(...))` in `clippy_lints/src/lib.rs`. The lint will silently not run without this.

- **Error**: Registering a lint pass with `register_early_pass` when the trait implementation is `LateLintPass` (or vice versa).
  **Correction**: The registration function must match the implemented trait. `EarlyLintPass` -> `register_early_pass`; `LateLintPass` -> `register_late_pass`.

- **Error**: Adding a new registration for a type-specific lint that already has its pass registered.
  **Correction**: Type-specific lints share a pass. Instead of registering a new pass, call your lint logic from the existing type group's `check_*` methods in `mod.rs`.

# Common Confusions

- **Confusion**: Thinking `cargo dev update_lints` fully automates registration in all cases.
  **Clarification**: It handles lint constant registration and category assignment, but the lint pass may need to be registered manually because multiple lints can share a pass and ordering matters.

- **Confusion**: Believing each lint needs its own registered pass.
  **Clarification**: Multiple lints can and often do share a single pass struct. `declare_lint_pass!(MyPass => [LINT_A, LINT_B])` links multiple lints to one pass with one registration call.

- **Confusion**: Wondering why registration order matters when the output seems random.
  **Clarification**: The registration order in `lib.rs` determines the execution order of passes, which determines the order lint diagnostics appear in compiler output. This is visible in test `.stderr` files.

# Source Reference

Chapter 3: Lint Basics, section "Lint registration" (appears twice -- once in the "Adding a new lint" walkthrough and once in the "Define New Lints" chapter). The configuration registration pattern is from the "Adding configuration to a lint" section.

# Verification Notes

- Core requirement: Directly quoted -- "Without a call to one of register_early_pass or register_late_pass, the lint pass in question will not be run"
- Two reasons for non-automation: Directly quoted from source -- multiple lints per pass and ordering
- Registration syntax: Both `register_early_pass` and `register_late_pass` examples come from the source
- Configuration pattern: `move || Box::new(module::StructName::new(conf))` from "Adding configuration to a lint" section
- Files modified: Reconstructed from `git status` examples in the source
- Confidence: HIGH -- registration is discussed in detail with concrete code examples
- Cross-references: All slugs verified against planned extractions across agents
