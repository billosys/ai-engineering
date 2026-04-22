---
# === CORE IDENTIFICATION ===
concept: New Keywords in Rust 2018 (async, await, dyn, try)
slug: async-await-keywords-2018

# === CLASSIFICATION ===
category: edition-2018
subcategory: keywords
tier: intermediate

# === PROVENANCE ===
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "Rust 2018"
chapter_number: 3
pdf_page: null
section: "New keywords"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Rust 2018 new keywords"
  - "dyn keyword"
  - "async/await keywords"
  - "try keyword reservation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rust-editions
extends: []
related:
  - rust-2018-edition
  - path-module-changes-2018
  - edition-migration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What new keywords were introduced in Rust 2018?"
  - "Why does Rust 2018 require dyn before trait objects?"
  - "When were async and await reserved as keywords?"
  - "What is the dyn Trait syntax?"
  - "What happens to code that uses async, await, or dyn as identifiers?"
  - "What is the try keyword reserved for?"
---

# Quick Definition

Rust 2018 introduced three new keyword reservations: `dyn` became a strict keyword (for trait object syntax `dyn Trait`), `async` and `await` became strict keywords (for async programming, stabilized in Rust 1.39.0), and `try` was reserved for future `try` blocks. Code using these as identifiers must migrate to raw identifier syntax (`r#async`) or rename them.

# Core Definition

Introducing new keywords is a backwards-incompatible change because existing code may use those words as identifiers. The edition system was specifically designed to handle this case. As the source explains: "Early versions of Rust didn't feature the `async` and `await` keywords. If Rust had suddenly introduced these new keywords, some code would have broken: `let async = 1;` would no longer work." (Ch. 1: What Are Editions).

In the 2018 edition:
- **`dyn`**: Becomes a strict keyword. In 2015 it was a weak keyword. The new `dyn Trait` syntax replaces bare `Trait` in type position for trait objects.
- **`async` and `await`**: Become strict keywords, reserved for async programming (stabilized in Rust 1.39.0).
- **`try`**: Becomes a reserved keyword for future use with `try` blocks (not yet stabilized as of the source).

# Prerequisites

- **rust-editions** -- Understanding that new keywords require edition opt-in to avoid breaking existing code

# Key Properties

1. **`dyn` is strict in 2018**: `Box<Trait>` becomes `Box<dyn Trait>`, `&Trait` becomes `&dyn Trait>`
2. **`dyn` is weak in 2015**: In edition 2015, `dyn` can still be used as an identifier
3. **`async`/`await` are strict in 2018**: Cannot be used as identifiers; enable async programming syntax
4. **`try` is reserved**: Cannot be used as an identifier; reserved for future `try` block syntax
5. **Raw identifiers as escape hatch**: Code that used these words as identifiers can use `r#async`, `r#dyn`, etc.
6. **Migration automated**: `cargo fix --edition` converts conflicting identifiers to raw identifier syntax

# Construction / Recognition

## `dyn Trait` Syntax Change:
```rust
// Rust 2015 (bare trait name)
fn function1() -> Box<Trait> { ... }

// Rust 2018 (dyn keyword required)
fn function2() -> Box<dyn Trait> { ... }
```

Common transformations:
- `Box<Trait>` becomes `Box<dyn Trait>`
- `&Trait` becomes `&dyn Trait`
- `&mut Trait` becomes `&mut dyn Trait`

## Raw Identifier Escape Hatch:
```rust
// If code used 'async' as a variable name:
// Rust 2015: let async = 1;
// Rust 2018: let r#async = 1;
```

# Context & Application

The `dyn Trait` syntax was introduced to resolve ambiguity between trait objects and `impl Trait`. As the source notes: "Using just the trait name for trait objects turned out to be a bad decision. The current syntax is often ambiguous and confusing, even to veterans, and favors a feature that is not more frequently used than its alternatives, is sometimes slower, and often cannot be used at all when its alternatives can." The `dyn` keyword makes the distinction between `impl Trait` (static dispatch) and `dyn Trait` (dynamic dispatch) symmetric and explicit.

The `async`/`await` keywords enabled Rust's async programming model, which was ultimately stabilized in Rust 1.39.0 (November 2019). Reserving these keywords in the 2018 edition (released December 2018 with Rust 1.31.0) ensured the syntax was available when the feature landed.

# Examples

**Example 1** (Ch 3): Trait object syntax change:
```rust
trait Trait {}
impl Trait for i32 {}

// Rust 2015 (old)
fn function1() -> Box<Trait> { ... }

// Rust 2018 (new)
fn function2() -> Box<dyn Trait> { ... }
```

**Example 2** (Ch 1): Why keywords need editions:
> "Early versions of Rust didn't feature the `async` and `await` keywords. If Rust had suddenly introduced these new keywords, some code would have broken: `let async = 1;` would no longer work."

**Example 3** (Ch 1): Automated migration using raw identifiers:
> "When migrating to Rust 2018, anything named `async` will now use the equivalent raw identifier syntax: `r#async`."

**Example 4** (Ch 3): Keyword classification:
- `dyn`: strict keyword in 2018+, weak keyword in 2015
- `async`, `await`: strict keywords in 2018+
- `try`: reserved keyword in 2018+

# Relationships

## Builds Upon
- **rust-editions** -- keyword reservations are a primary use case for the edition mechanism

## Enables
- **rust-2018-edition** -- these keywords are part of the 2018 edition changes

## Related
- **path-module-changes-2018** -- another major 2018 edition change
- **edition-migration** -- `cargo fix --edition` automates keyword migration using raw identifiers

## Contrasts With
- None explicitly within this source

# Common Errors

- **Error**: Using `dyn` as a variable or function name in edition 2018+ code.
  **Correction**: `dyn` is a strict keyword in 2018+. Use a different name, or if interfacing with older code, use `r#dyn`.

- **Error**: Writing trait objects without `dyn` in edition 2018 code (e.g., `Box<Trait>`).
  **Correction**: Use `Box<dyn Trait>`. While 2015 allowed bare trait names, 2018 requires the `dyn` keyword.

- **Error**: Using `try` as an identifier in edition 2018+.
  **Correction**: `try` is a reserved keyword. Use a different name like `try_run` or `attempt`, or use `r#try`.

# Common Confusions

- **Confusion**: Thinking `dyn Trait` and `impl Trait` are interchangeable.
  **Clarification**: `impl Trait` uses static dispatch (monomorphization) while `dyn Trait` uses dynamic dispatch (vtable). The `dyn` keyword was introduced to make this distinction explicit: "`impl Trait` vs `dyn Trait` is much more symmetric, and therefore a bit nicer, than `impl Trait` vs `Trait`."

- **Confusion**: Thinking `async`/`await` were usable immediately with the 2018 edition.
  **Clarification**: The 2018 edition (Rust 1.31.0, December 2018) reserved the keywords. The actual async/await feature was stabilized later in Rust 1.39.0 (November 2019).

- **Confusion**: Thinking the `try` keyword is currently functional.
  **Clarification**: `try` is only reserved. The `try` blocks feature has not been stabilized (tracking issue rust-lang/rust#31436).

# Source Reference

Chapter 3: Rust 2018; section "New keywords." Also references Chapter 1 for the motivating example. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch 3 -- "`dyn` is a strict keyword, in 2015 it is a weak keyword. `async` and `await` are strict keywords. `try` is a reserved keyword."
- Confidence rationale: HIGH -- the source provides clear keyword classification and migration examples
- Uncertainties: The `try` keyword's future is uncertain as the feature remains unstabilized
- Cross-reference status: rust-editions, rust-2018-edition, path-module-changes-2018, edition-migration are in this extraction set
