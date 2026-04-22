---
concept: Documentation Guidelines
slug: documentation-guidelines
category: documentation
subcategory: null
tier: intermediate
source: "Pragmatic Rust"
source_slug: pragmatic-rust
authors: "Pragmatic Rust Contributors"
chapter: "07-documentation"
chapter_number: 7
pdf_page: null
section: "Documentation"
extraction_confidence: high
aliases:
  - "doc guidelines"
  - "rustdoc guidelines"
  - "API documentation rules"
  - "module docs"
  - "doc inline"
prerequisites:
  - pragmatic-rust-overview
extends: []
related:
  - library-ux-guidelines
  - ai-design-guidelines
contrasts_with: []
answers_questions:
  - "What sections should Rust doc comments include?"
  - "How long should the first doc sentence be?"
  - "When should I use #[doc(inline)] in Rust?"
  - "What should module documentation cover in Rust?"
  - "Should I document parameters in a table in Rust?"
---

# Quick Definition

Documentation guidelines covering four areas: public items must include canonical doc sections with a summary under 15 words plus Errors, Panics, Safety, and Abort sections when applicable (M-CANONICAL-DOCS); re-exported items should use `#[doc(inline)]` to appear organically in documentation (M-DOC-INLINE); the first doc sentence must be a single line of approximately 15 words for skimmability (M-FIRST-DOC-SENTENCE); and every public module must have comprehensive `//!` documentation (M-MODULE-DOCS).

# Core Definition

The documentation guidelines establish standards for Rust library documentation quality. M-CANONICAL-DOCS requires a summary sentence, optional extended documentation, and mandatory sections when applicable: Examples, Errors (for Result-returning functions), Panics, Safety (for unsafe functions), and Abort. Parameters should be explained in plain text woven into the description, not in a table. M-DOC-INLINE requires `#[doc(inline)]` on `pub use` items so they render organically alongside non-re-exported siblings, except for `std` or third-party types which should remain un-inlined to signal their external origin. M-FIRST-DOC-SENTENCE sets a 15-word limit for the first sentence because it becomes the summary shown in module listings; exceeding this creates "widows" and poor reading flow. M-MODULE-DOCS requires every public module to have `//!` documentation covering what it contains, when to use it, examples, subsystem specifications, observable side effects, and implementation details. (Ch. 7, "Documentation")

# Prerequisites

- **pragmatic-rust-overview** -- understanding the overall guideline framework provides context for documentation requirements

# Key Properties

1. **M-CANONICAL-DOCS**: Public library items must have: summary sentence (always), extended docs (strongly encouraged), Examples (strongly encouraged), Errors (if returns Result), Panics (if may panic), Safety (if unsafe or may cause UB), Abort (if may abort)
2. Parameters are explained in plain text, not tables: write `Copies a file from \`src\` to \`dst\`` not a Parameters section with `src: The source`
3. **M-DOC-INLINE**: Annotate `pub use foo::Foo` or `pub use foo::*` with `#[doc(inline)]` at the use site; this does not apply to `std` or third-party types
4. The `#[doc(inline)]` trick does not change the M-NO-GLOB-REEXPORTS guideline -- glob re-exports should still generally be avoided
5. **M-FIRST-DOC-SENTENCE**: The first sentence should not exceed ~15 words; it is extracted as the summary shown in module listings
6. Keeping first sentences short makes API docs skimmable; the source contrasts good (std library style) with bad (widowed text) examples
7. **M-MODULE-DOCS**: Every public module needs `//!` documentation; the first sentence must follow M-FIRST-DOC-SENTENCE
8. Module docs should cover: contents, usage guidance, examples, subsystem specifications, observable side effects, implementation details
9. Exemplary module documentation: `std::fmt`, `std::pin`, `std::option`

# Construction / Recognition

## To Apply M-CANONICAL-DOCS:
1. Write a summary sentence under 15 words for every public item
2. Add extended documentation explaining purpose and behavior
3. Add `# Examples` with runnable code when possible
4. Add `# Errors` listing known error conditions for Result-returning functions
5. Add `# Panics` listing panic conditions
6. Add `# Safety` for unsafe functions listing all caller obligations
7. Add `# Abort` if the function may abort the process
8. Weave parameter explanations into prose, not tables

## To Apply Other Guidelines:
1. Add `#[doc(inline)]` to all `pub use` items from internal modules
2. Keep first doc sentences to ~15 words on a single line
3. Add `//!` documentation to every public module covering contents, usage, examples, and relevant technical details

# Context & Application

These guidelines build on the Rust API Guidelines (C-FAILURE, C-EXAMPLE, C-QUESTION-MARK) but add specific quantitative thresholds (15-word first sentences) and visual quality concerns (avoiding widows in rendered docs). The inline doc guideline addresses a common rendering problem where re-exported items appear in opaque blocks instead of being listed alongside their siblings. The module docs guideline sets a higher bar than many Rust projects achieve, pointing to `std::fmt` and `std::pin` as gold standards.

# Examples

**Example 1** (Ch. 7, M-CANONICAL-DOCS -- Complete doc template):
```rust
/// Summary sentence < 15 words.
///
/// Extended documentation in free form.
///
/// # Examples
/// # Errors
/// # Panics
/// # Safety
/// # Abort
pub fn foo() {}
```

**Example 2** (Ch. 7, M-CANONICAL-DOCS -- Parameter style): Instead of a `# Parameters` section with `src: The source` and `dst: The destination`, write: `/// Copies a file from \`src\` to \`dst\`.`

**Example 3** (Ch. 7, M-DOC-INLINE -- Usage): `#[doc(inline)] pub use foo::*;` or `#[doc(inline)] pub use foo::Foo;` causes re-exported items to render alongside native items in the documentation instead of appearing in a separate re-export block.

**Example 4** (Ch. 7, M-MODULE-DOCS -- Module doc): `pub mod ffi { //! Contains FFI abstractions. pub struct String {}; }` -- every public module gets a `//!` doc comment with a concise first sentence.

# Relationships

## Builds Upon
- **pragmatic-rust-overview** -- documentation requirements operate within the overall guideline framework

## Enables
- Skimmable, consistent API documentation across a codebase
- Better navigation of complex library documentation

## Related
- **library-ux-guidelines** -- documentation quality is part of the overall library UX
- **ai-design-guidelines** -- M-DESIGN-FOR-AI explicitly references these documentation guidelines as critical for AI effectiveness

## Contrasts With
- Parameter-table documentation style common in languages like Java or C#
- Minimal documentation approaches that skip module-level docs

# Common Errors

- **Error**: Writing first doc sentences that wrap to multiple lines in rendered documentation, creating orphaned "widow" words.
  **Correction**: Keep the first sentence to approximately 15 words so it fits on a single line in the rendered module summary.

- **Error**: Documenting parameters in a table format (`# Parameters` with bullet points for each parameter).
  **Correction**: Weave parameter descriptions into the summary sentence using backtick-quoted parameter names: `Copies a file from \`src\` to \`dst\`.`

- **Error**: Using `pub use foo::Bar` without `#[doc(inline)]`, causing `Bar` to appear in an opaque re-export block in the docs.
  **Correction**: Add `#[doc(inline)]` before the re-export. Exception: do not inline `std` or third-party types.

# Common Confusions

- **Confusion**: Thinking `#[doc(inline)]` makes glob re-exports acceptable.
  **Clarification**: The source explicitly notes: "The `#[doc(inline)]` trick above does not change M-NO-GLOB-REEXPORTS; you generally should not re-export items via wildcards."

- **Confusion**: Believing every module needs all the listed documentation categories (contents, usage, examples, specifications, side effects, implementation details).
  **Clarification**: The source states: "This does not mean every module should contain all of these items. But if there is something to say about the interaction of the contained types, their module documentation is the right place."

# Source Reference

Chapter 7: Documentation. Contains four guidelines: M-CANONICAL-DOCS (v1.0), M-DOC-INLINE (v1.0), M-FIRST-DOC-SENTENCE (v1.0), M-MODULE-DOCS (v1.1). Includes rendered screenshot comparisons showing good vs bad first-sentence lengths and inline vs non-inline re-exports. References: C-FAILURE from the Rust API Guidelines. Exemplary modules: `std::fmt`, `std::pin`, `std::option`.

# Verification Notes

- Definition source: Direct from section headings and `<why>` tags for each guideline
- Key Properties: Derived from code templates, rendered documentation screenshots, and explicit word-count thresholds
- Confidence rationale: HIGH -- all four guidelines have clear definitions, visual examples, and concrete thresholds
- Uncertainties: The 15-word limit is described as approximate ("rule of thumb")
- Cross-reference status: pragmatic-rust-overview, library-ux-guidelines, ai-design-guidelines are from sibling extraction sets
