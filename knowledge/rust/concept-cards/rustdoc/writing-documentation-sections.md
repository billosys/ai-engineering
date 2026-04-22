---
# === CORE IDENTIFICATION ===
concept: Writing Documentation Sections
slug: writing-documentation-sections

# === CLASSIFICATION ===
category: documentation
subcategory: conventions
tier: foundational

# === PROVENANCE ===
source: "Rustdoc Book"
source_slug: rustdoc
authors: "The Rust Project"
chapter: "How to Write Documentation"
chapter_number: 4
pdf_page: null
section: "Documenting components / What to include"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "doc comment sections"
  - "documentation structure"
  - "Panics section"
  - "Safety section"
  - "Errors section"
  - "Examples section"
  - "conventional documentation sections"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - doc-comments
extends: []
related:
  - doc-tests
  - doc-attribute
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What sections should I include in Rust documentation?"
  - "When should I add a Panics section?"
  - "What is the conventional structure for documenting a Rust item?"
  - "How should I document unsafe functions?"
  - "When should I use the Errors section?"
  - "How should I write examples in documentation?"
  - "What does the #![warn(missing_docs)] lint do?"
  - "When should I use #[doc(hidden)]?"
---

# Quick Definition

Rust documentation follows conventional sections that help users quickly understand an item's behavior, requirements, and edge cases. The standard sections include a short summary, detailed explanation, **Examples** (runnable code), **Panics** (conditions that cause panics), **Errors** (when `Result::Err` is returned), and **Safety** (invariants for `unsafe` functions). The `#![warn(missing_docs)]` lint enforces documentation on public items.

# Core Definition

The Rustdoc Book establishes a recommended structure for documenting each public item:

1. **Short sentence** explaining what the item is (becomes the summary in module overviews)
2. **More detailed explanation** of behavior, context, and usage
3. **At least one code example** that users can copy/paste to try it
4. **Advanced explanations** if necessary

Beyond this basic structure, the standard library conventions include named sections introduced with Markdown `#` headings:

- **`# Panics`**: Documents conditions under which the function panics. "A panic section is recommended every time edge cases in your code can be reached if known."
- **`# Examples`**: Runnable code examples. "Part of the power of documentation is showing code that is easy to follow, rather than being realistic."
- **`# Errors`**: Documents when a function returns `Err` and what error types to expect.
- **`# Safety`**: For `unsafe` functions, documents the invariants the caller must uphold.

The source also emphasizes using `#![warn(missing_docs)]` or `#![deny(missing_docs)]` to ensure comprehensive documentation, and using `#[doc(hidden)]` to exclude implementation details from the public API surface.

# Prerequisites

- **doc-comments** -- understanding `///` and `//!` syntax is needed before structuring their content

# Key Properties

1. **First line is the summary**: Everything before the first blank line appears in module overviews and search results. Keep it concise.
2. **Panics section is strongly recommended**: Whenever a function can panic, document the conditions. This helps users avoid runtime failures.
3. **Examples should be simple**: "It is preferred that `unwrap()` not be used inside an example." Use `#` to hide boilerplate setup code.
4. **Error handling in examples**: Hide `fn main() -> Result<...>` wrappers with `# ` lines so readers see clean code that actually compiles.
5. **`#[doc(hidden)]` for implementation details**: Internal macros, error types, and impl details that shouldn't appear in public docs.
6. **Type signatures are auto-linked**: "There is no benefit of explicitly writing [types] into the documentation, especially since `rustdoc` adds hyper links to all types in the function signature."
7. **`missing_docs` lint enforcement**: Use `#![warn(missing_docs)]` to get warnings, or `#![deny(missing_docs)]` to make missing docs a compile error.

# Construction / Recognition

## Standard Section Structure:
```rust
/// Returns the arguments which this program was started with.
///
/// The first element is traditionally the path of the executable,
/// but it can be set to arbitrary text, and may not even exist.
///
/// # Panics
///
/// The returned iterator will panic during iteration if any argument
/// to the process is not valid unicode.
///
/// # Examples
///
/// ```
/// use std::env;
///
/// for argument in env::args() {
///     println!("{argument}");
/// }
/// ```
pub fn args() -> Args { /* ... */ }
```

## Hiding Error-Handling Boilerplate:
```rust
/// ```
/// # fn main() -> Result<(), std::num::ParseIntError> {
/// let fortytwo = "42".parse::<u32>()?;
/// println!("{} + 10 = {}", fortytwo, fortytwo+10);
/// #     Ok(())
/// # }
/// ```
```

## Enforcing Documentation:
```rust
#![warn(missing_docs)]  // Warn on undocumented public items
#![deny(missing_docs)]  // Error on undocumented public items
```

# Context & Application

These documentation conventions are the standard followed by the Rust standard library and the broader ecosystem. The API Guidelines (linked in the source) provide additional rules, such as using `#[doc(hidden)]` to hide unhelpful implementation details. Crate authors should aim for every public item to have at minimum a summary and an example. The Panics and Errors sections are critical for correctness, as they document failure modes that users must handle.

# Examples

**Example 1** (Ch 4): Full documentation following the standard structure, from `std::env::args()`:

> Returns the arguments which this program was started with (normally passed via the command line).
>
> The first element is traditionally the path of the executable...
>
> **Panics**: The returned iterator will panic during iteration if any argument to the process is not valid unicode. If this is not desired, use the `args_os` function instead.
>
> **Examples**: `use std::env; for argument in env::args() { println!("{argument}"); }`

**Example 2** (Ch 4): Using `#[doc(hidden)]` to exclude implementation details:
> "An internal `macro!` that makes the crate easier to implement can become a footgun for users when it appears in the public documentation."

**Example 3** (Ch 4): Hiding setup code so the example reads cleanly:
```rust
/// Example
/// ```rust
/// # fn main() -> Result<(), std::num::ParseIntError> {
/// let fortytwo = "42".parse::<u32>()?;
/// println!("{} + 10 = {}", fortytwo, fortytwo+10);
/// #     Ok(())
/// # }
/// ```
```

# Relationships

## Builds Upon
- **doc-comments** -- sections are written inside `///` doc comments

## Enables
- **doc-tests** -- the Examples section creates runnable doc tests

## Related
- **doc-attribute** -- `#[doc(hidden)]` controls documentation visibility
- **rustdoc-lints** -- `missing_docs` and related lints enforce documentation coverage

## Contrasts With
- None explicitly

# Common Errors

- **Error**: Writing a Panics section that says "This function panics" without specifying when.
  **Correction**: Document the specific conditions: "Panics if `index` is out of bounds" or "Panics if the lock is poisoned."

- **Error**: Including `unwrap()` in documentation examples without hiding the error handling.
  **Correction**: Use `# ` hidden lines to wrap the example in `fn main() -> Result<...>` and use `?` instead of `unwrap()`.

- **Error**: Not documenting a function's panic conditions because "it's obvious from the code."
  **Correction**: Users read docs, not source. Always document panic conditions explicitly.

# Common Confusions

- **Confusion**: Thinking the section headings (Panics, Safety, Errors, Examples) are enforced by the compiler.
  **Clarification**: These are conventions, not enforced syntax. However, following them is strongly expected in the Rust ecosystem, and tools like clippy have lints for missing Panics/Safety sections.

- **Confusion**: Thinking `#[doc(hidden)]` makes an item private.
  **Clarification**: `#[doc(hidden)]` only hides the item from generated documentation. The item remains public and accessible in code. Use `pub(crate)` or private visibility for actual access control.

- **Confusion**: Thinking that documenting types in prose is necessary.
  **Clarification**: "There is no benefit of explicitly writing [types] into the documentation, especially since `rustdoc` adds hyper links to all types in the function signature." Focus on behavior, not signatures.

# Source Reference

Chapter 4: How to Write Documentation; sections "Documenting components," "What to include (and exclude)," and "Examples." Rustdoc Book, The Rust Project. No page numbers (online documentation).

# Verification Notes

- Definition source: Directly from Ch 4 -- the `std::env::args()` example with Panics and Examples sections, and the recommendation "A panic section is recommended every time edge cases in your code can be reached if known"
- Confidence rationale: HIGH -- well-established conventions with concrete examples from the standard library
- Uncertainties: None for the conventions; specific section names may evolve but Panics/Examples/Errors/Safety are deeply established
- Cross-reference status: doc-comments, doc-tests, doc-attribute are in this extraction set
