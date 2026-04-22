---
# === CORE IDENTIFICATION ===
concept: Doc Comments
slug: doc-comments

# === CLASSIFICATION ===
category: documentation
subcategory: comment-syntax
tier: foundational

# === PROVENANCE ===
source: "Rustdoc Book"
source_slug: rustdoc
authors: "The Rust Project"
chapter: "How to Write Documentation"
chapter_number: 4
pdf_page: null
section: "Getting Started / Documenting components"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "documentation comments"
  - "/// comments"
  - "//! comments"
  - "outer doc comments"
  - "inner doc comments"
  - "rustdoc comments"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - doc-attribute
  - writing-documentation-sections
  - doc-tests
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the different doc comment styles in Rust?"
  - "When should I use /// versus //!?"
  - "Where do inner doc comments (//!) apply?"
  - "What is the relationship between /// and #[doc]?"
  - "What Markdown features are supported in doc comments?"
  - "How does rustdoc use the first line/paragraph of a doc comment?"
  - "How do I write crate-level documentation?"
---

# Quick Definition

Rust doc comments are special comment syntax (`///` for outer, `//!` for inner) that rustdoc extracts to generate HTML documentation. They support CommonMark Markdown with extensions (strikethrough, footnotes, tables, task lists, smart punctuation), and the first paragraph serves as the item's summary in module overviews and search results.

# Core Definition

Rust provides two styles of documentation comments, both of which are syntactic sugar for the `#[doc]` attribute:

- **Outer doc comments** (`///`): Placed before an item (function, struct, enum, module, etc.) to document that item. Equivalent to `#[doc = "..."]`.
- **Inner doc comments** (`//!`): Placed at the beginning of a module or crate to document the enclosing item. Equivalent to `#![doc = "..."]`. Typically used in `lib.rs` for crate-level front-page documentation.

As the source explains: "Lines should start with `//!` which indicate module-level or crate-level documentation." Meanwhile `///` is used to document individual items: "This module makes it easy" on a `pub mod`, or "Use the abstraction function to do this specific thing" on a `pub fn`.

Doc comments support the full CommonMark Markdown specification plus several extensions: strikethrough (`~~text~~`), footnotes (`[^note]`), tables (pipe-delimited), task lists (`- [x]`/`- [ ]`), and smart punctuation (converting `--` to en-dash, `---` to em-dash, `...` to ellipsis).

# Prerequisites

None -- doc comments are one of the most basic Rust features.

# Key Properties

1. **`///` documents the next item**: Placed directly before functions, structs, enums, traits, modules, constants, etc.
2. **`//!` documents the enclosing item**: Used at the top of `lib.rs` for crate docs, or at the top of a `mod` block for module docs.
3. **Desugars to `#[doc]`**: `/// text` is equivalent to `#[doc = r" text"]`, and `//!` is equivalent to `#![doc]`.
4. **First paragraph is the summary**: Everything before the first blank line is reused in search results and module overviews. Keep it to one concise sentence.
5. **CommonMark plus extensions**: Strikethrough, footnotes, tables, task lists, and smart punctuation are all supported.
6. **Warning blocks**: You can embed `<div class="warning">` in doc comments for prominent warnings, with an empty line between HTML and Markdown content.
7. **Code blocks are doc tests**: Fenced code blocks in doc comments are compiled and run as tests by default (see doc-tests).

# Construction / Recognition

## Outer Doc Comments (///):
```rust
/// Short summary of what this function does.
///
/// More detailed explanation with examples.
///
/// # Examples
///
/// ```
/// let result = my_crate::add(2, 3);
/// assert_eq!(result, 5);
/// ```
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

## Inner Doc Comments (//!):
```rust
//! Fast and easy queue abstraction.
//!
//! Provides an abstraction over a queue. When the abstraction is used
//! there are these advantages:
//! - Fast
//! - [`Easy`]
//!
//! [`Easy`]: http://thatwaseasy.example.com

/// This module makes it easy.
pub mod easy {
    /// Use the abstraction function to do this specific thing.
    pub fn abstraction() {}
}
```

## Markdown Extensions:
```markdown
~~strikethrough~~ or ~single tildes~

A footnote[^note].
[^note]: Footnote content here.

| Header1 | Header2 |
|---------|---------|
| abc     | def     |

- [x] Complete task
- [ ] Incomplete task
```

# Context & Application

Doc comments are the primary mechanism for documenting Rust code. The `#![warn(missing_docs)]` or `#![deny(missing_docs)]` lint can enforce that all public items are documented. The `//!` style is used in `lib.rs` to create the crate's front page, which should include an introduction, a usage example, and feature descriptions. Individual items use `///` and should follow the structure: short summary, detailed explanation, code examples, advanced notes.

# Examples

**Example 1** (Ch 4): Crate-level documentation in `lib.rs`:
```rust
//! Fast and easy queue abstraction.
//!
//! Provides an abstraction over a queue. When the abstraction is used
//! there are these advantages:
//! - Fast
//! - [`Easy`]
```

**Example 2** (Ch 4): Item documentation with conventional structure:
```text
[short sentence explaining what it is]

[more detailed explanation]

[at least one code example that users can copy/paste to try it]

[even more advanced explanations if necessary]
```

**Example 3** (Ch 4): The first line becomes the summary:
> "Everything before the first empty line will be reused to describe the component in searches and module overviews."

**Example 4** (Ch 4): Warning block in doc comments:
```rust
/// documentation
///
/// <div class="warning">A big warning!</div>
///
/// more documentation
```

# Relationships

## Builds Upon
- None

## Enables
- **doc-tests** -- code blocks in doc comments become executable tests
- **writing-documentation-sections** -- doc comments contain conventional sections (Panics, Examples, etc.)

## Related
- **doc-attribute** -- `///` is syntactic sugar for `#[doc = "..."]`
- **intra-doc-links** -- doc comments support linking to other items by path
- **rustdoc** -- the tool that processes doc comments into HTML

## Contrasts With
- None explicitly

# Common Errors

- **Error**: Placing `//!` after items instead of at the top of a module/crate.
  **Correction**: `//!` documents the enclosing item. It must appear at the beginning of `lib.rs` or at the top of a `mod` block, before any items.

- **Error**: Writing a multi-sentence first paragraph, making module overviews cluttered.
  **Correction**: Keep the first line/paragraph to one concise sentence. Put details after a blank line.

- **Error**: Using `///` at the top of `lib.rs` instead of `//!` for crate documentation.
  **Correction**: `///` documents the next item, not the crate. Use `//!` for crate-level docs.

# Common Confusions

- **Confusion**: Thinking `///` and `//!` are just regular comments that happen to be displayed.
  **Clarification**: Doc comments desugar to `#[doc]` attributes and are processed by the compiler and rustdoc. They affect compilation (doc tests) and are part of the crate's public API contract.

- **Confusion**: Not realizing that code blocks in doc comments are tested.
  **Clarification**: By default, every fenced code block in a doc comment is compiled and run as a test. Use attributes like `no_run`, `ignore`, or `text` to change this behavior.

- **Confusion**: Thinking Markdown in doc comments uses GitHub-Flavored Markdown.
  **Clarification**: Rustdoc uses CommonMark with specific extensions (strikethrough, footnotes, tables, task lists, smart punctuation). While similar to GFM, the specifications differ in edge cases.

# Source Reference

Chapter 4: How to Write Documentation; sections "Getting Started," "Documenting components," and "Markdown." Rustdoc Book, The Rust Project. No page numbers (online documentation).

# Verification Notes

- Definition source: Directly from Ch 4 -- "Lines should start with `//!` which indicate module-level or crate-level documentation" and the `///` vs `#[doc]` equivalence
- Confidence rationale: HIGH -- doc comments are exhaustively documented with clear syntax and usage examples
- Uncertainties: None for the core syntax; Markdown extension details may evolve with the CommonMark spec
- Cross-reference status: doc-attribute, doc-tests, writing-documentation-sections, intra-doc-links are in this extraction set
