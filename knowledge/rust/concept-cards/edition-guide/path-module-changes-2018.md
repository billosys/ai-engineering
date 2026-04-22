---
# === CORE IDENTIFICATION ===
concept: Path and Module System Changes in Rust 2018
slug: path-module-changes-2018

# === CLASSIFICATION ===
category: edition-2018
subcategory: module-system
tier: intermediate

# === PROVENANCE ===
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "Rust 2018"
chapter_number: 3
pdf_page: null
section: "Path and module system changes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Rust 2018 module changes"
  - "Rust 2018 path changes"
  - "uniform paths"
  - "no more extern crate"
  - "no more mod.rs"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rust-editions
  - rust-2015-edition
extends: []
related:
  - rust-2018-edition
  - edition-migration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What changed about the module system in Rust 2018?"
  - "Do I still need extern crate in Rust 2018?"
  - "How do use paths work differently in Rust 2018?"
  - "What does the crate:: prefix mean?"
  - "Can I use foo.rs instead of foo/mod.rs in Rust 2018?"
  - "How do I reference external crates in submodules in Rust 2018?"
---

# Quick Definition

Rust 2018 overhauled the path and module system to simplify and unify how paths work across the language. The key changes are: `extern crate` is no longer needed, the `crate::` prefix refers to the current crate, paths in `use` declarations work the same as paths elsewhere, `::` unambiguously refers to external crates, and `mod.rs` is no longer required for modules with submodules.

# Core Definition

The module system was "often one of the hardest things for people new to Rust" (Ch. 3: Path and module system changes). The 2018 edition addressed this by making paths consistent and eliminating special cases. The source summarizes the changes:

- `extern crate` is no longer needed in 99% of circumstances
- The `crate` keyword refers to the current crate
- Paths may start with a crate name, even within submodules
- Paths starting with `::` must reference an external crate
- A `foo.rs` and `foo/` subdirectory may coexist; `mod.rs` is no longer needed
- Paths in `use` declarations work the same as other paths

The underlying principle is unification: "In Rust 2018, paths in `use` declarations and in other code work the same way, both in the top-level module and in any submodule."

# Prerequisites

- **rust-editions** -- Understanding the edition system and how to opt into 2018
- **rust-2015-edition** -- Understanding the 2015 module system that these changes replaced

# Key Properties

1. **No more `extern crate`**: External crates are automatically in scope; just add them to `Cargo.toml`
2. **`crate::` prefix**: Unambiguously refers to the root of the current crate (e.g., `crate::foo::bar`)
3. **`::` means external**: The `::` prefix now exclusively refers to external crates, no longer the crate root
4. **Uniform `use` paths**: Paths in `use` declarations behave identically to paths in other code
5. **No more `mod.rs`**: Modules can use `foo.rs` alongside a `foo/` directory for submodules
6. **Crate names in submodules**: External crate names are in scope everywhere, not just the crate root

# Construction / Recognition

## Eliminating `extern crate`:

Rust 2015:
```rust
extern crate futures;
mod submodule {
    use futures::Future;
}
```

Rust 2018:
```rust
mod submodule {
    use futures::Future;
}
```

Exception: Sysroot crates (`std`, `core`, `alloc`, `proc_macro`, `test`) may still need `extern crate` in specialized situations, though most are auto-imported.

## Using `crate::` and `::`:

- `crate::foo::bar` -- always refers to `bar` inside module `foo` of the current crate
- `::foo::bar` -- always refers to `bar` inside the external crate `foo`

## Module File Layout:

Rust 2015 (required `mod.rs`):
```
.
├── lib.rs
└── foo/
    ├── mod.rs
    └── bar.rs
```

Rust 2018 (no `mod.rs` needed):
```
.
├── lib.rs
├── foo.rs
└── foo/
    └── bar.rs
```

# Context & Application

The path and module changes were the most significant backwards-incompatible changes in the 2018 edition and were the primary motivation for creating the edition system (RFC #2052). These changes make Rust's module system more intuitive, especially for newcomers, by eliminating the inconsistency where `use` paths behaved differently from paths in other code, and by removing the need for boilerplate `extern crate` declarations. The changes also eliminate confusion about when `::` refers to the crate root vs. an external crate.

# Examples

**Example 1** (Ch 3): Removing `extern crate`:
```rust
// Rust 2015
extern crate futures;
mod submodule {
    use futures::Future;
}

// Rust 2018
mod submodule {
    use futures::Future;
}
```

**Example 2** (Ch 3): External crate paths in submodules:
```rust
// Rust 2015 -- required :: prefix in submodules
mod submodule {
    fn function() {
        let x = ::chrono::Utc::now();
    }
}

// Rust 2018 -- crate names in scope everywhere
mod submodule {
    fn function() {
        let x = chrono::Utc::now();
    }
}
```

**Example 3** (Ch 3): Importing macros without `#[macro_use]`:
```rust
// Rust 2015
#[macro_use]
extern crate bar;
fn main() { baz!(); }

// Rust 2018
use bar::baz;
fn main() { baz!(); }
```

**Example 4** (Ch 3): Renaming crates without `extern crate`:
```rust
// Rust 2015
extern crate futures as f;
use f::Future;

// Rust 2018
use futures as f;
use self::f::Future;
```

**Example 5** (Ch 3): Uniform paths in submodules:
```rust
// Rust 2018 -- this code works identically at the crate root
// and in any submodule:
mod submodule {
    use futures::Future;
    mod foo { pub struct Bar; }
    use foo::Bar;
    fn func() {
        let five = std::sync::Arc::new(5);
    }
}
```

# Relationships

## Builds Upon
- **rust-editions** -- these changes require opting into the 2018 edition
- **rust-2015-edition** -- changes are defined relative to the 2015 module system

## Enables
- **rust-2018-edition** -- path/module changes are the centerpiece of the 2018 edition

## Related
- **edition-migration** -- `cargo fix --edition` handles most of these changes automatically

## Contrasts With
- None explicitly within this source

# Common Errors

- **Error**: Removing `extern crate` for sysroot crates that still need it.
  **Correction**: In specialized cases, `extern crate` may still be needed for `alloc`, `test`, or older versions of `proc_macro`. Check the sysroot crate documentation.

- **Error**: Using `::` to refer to the current crate root (2015 behavior) in 2018.
  **Correction**: In 2018, `::` exclusively refers to external crates. Use `crate::` to refer to the current crate root.

- **Error**: Forgetting `self::` when renaming crates with `use futures as f`.
  **Correction**: After `use futures as f;`, subsequent references must use `self::f::` in the same module, e.g., `use self::f::Future;`.

# Common Confusions

- **Confusion**: Thinking both `foo.rs` and `foo/mod.rs` can coexist.
  **Clarification**: The 2018 change allows `foo.rs` alongside a `foo/` directory. You should not have both `foo.rs` and `foo/mod.rs` -- use one pattern or the other.

- **Confusion**: Believing `extern crate` is an error in Rust 2018.
  **Clarification**: `extern crate` is not forbidden, merely unnecessary in most cases. It still works and is occasionally needed for sysroot crates.

- **Confusion**: Thinking the path changes affect how compiled code works.
  **Clarification**: These are purely syntactic changes. "All Rust code -- regardless of edition -- will ultimately compile down to the same internal representation within the compiler."

# Source Reference

Chapter 3: Rust 2018; section "Path and module system changes." No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch 3 -- "The 2018 edition of Rust introduces a few new module system features, but they end up simplifying the module system."
- Confidence rationale: HIGH -- the source provides extensive before/after examples and detailed explanations
- Uncertainties: None for core changes; some edge cases around sysroot crates and crate renaming
- Cross-reference status: rust-editions, rust-2015-edition, rust-2018-edition, edition-migration are in this extraction set
