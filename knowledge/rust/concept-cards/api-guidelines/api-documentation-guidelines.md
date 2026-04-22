---
concept: API Documentation Guidelines
slug: api-documentation-guidelines
category: api-design
subcategory: null
tier: foundational
source: "Rust API Guidelines"
source_slug: api-guidelines
authors: "The Rust Library Team"
chapter: "04-documentation"
chapter_number: 4
pdf_page: null
section: "Documentation"
extraction_confidence: high
aliases:
  - "rust documentation guidelines"
  - "rustdoc guidelines"
  - "C-CRATE-DOC C-EXAMPLE C-QUESTION-MARK C-FAILURE C-LINK C-METADATA C-RELNOTES C-HIDDEN"
prerequisites:
  - api-guidelines-overview
extends:
  - api-guidelines-overview
related:
  - api-naming-guidelines
  - api-predictability-guidelines
contrasts_with: []
answers_questions:
  - "What documentation should a Rust crate provide?"
  - "How should rustdoc examples be written?"
  - "What should function documentation cover?"
  - "How should links work in rustdoc?"
  - "What metadata belongs in Cargo.toml?"
  - "How should release notes be managed?"
  - "How do I hide implementation details from rustdoc?"
---

# Quick Definition

The Documentation chapter of the Rust API Guidelines defines 8 guidelines (C-CRATE-DOC, C-EXAMPLE, C-QUESTION-MARK, C-FAILURE, C-LINK, C-METADATA, C-RELNOTES, C-HIDDEN) establishing that crates should be abundantly documented. Every public item should have examples, error conditions must be documented, prose should be hyperlinked, and implementation details should be hidden from rustdoc.

# Core Definition

**C-CRATE-DOC** -- Crate level docs are thorough and include examples. Per RFC 1687, crate-level documentation should provide an overview and examples that orient users.

**C-EXAMPLE** -- All items have a rustdoc example. Every public module, trait, struct, enum, function, method, macro, and type definition should have an example. The purpose is often to show *why someone would want to use* the item, not merely *how to call* it. A link to an example on a related item may suffice when appropriate.

**C-QUESTION-MARK** -- Examples use `?`, not `try!`, not `unwrap`. Example code is often copied verbatim by users. Unwrapping should be a conscious decision. The canonical pattern hides the boilerplate:
```
/// ```rust
/// # use std::error::Error;
/// # fn main() -> Result<(), Box<dyn Error>> {
/// your;
/// example?;
/// code;
/// #     Ok(())
/// # }
/// ```
```

**C-FAILURE** -- Function docs include error, panic, and safety considerations. Error conditions go in an "Errors" section, panic conditions in a "Panics" section, and unsafe function invariants in a "Safety" section. It is not necessary to document all conceivable panic cases (e.g., panics in caller-provided Display impls), but when in doubt, document more.

**C-LINK** -- Prose contains hyperlinks to relevant things. Use markdown links for URLs and rustdoc-style `` [`Type`] `` links for cross-references to other types, methods, and modules. This is officially recommended by RFC 1574: "Link all the things."

**C-METADATA** -- Cargo.toml includes all common metadata in the `[package]` section: authors, description, license, repository, keywords, categories. The `documentation` field is only needed if docs are hosted somewhere other than docs.rs. The `homepage` field should only be set for a unique website (not redundant with documentation or repository).

**C-RELNOTES** -- Release notes document all significant changes. Breaking changes (per RFC 1105) should be clearly identified. Every published release should have a corresponding Git tag. Use annotated tags because some Git commands ignore unannotated tags.

**C-HIDDEN** -- Rustdoc does not show unhelpful implementation details. Use `#[doc(hidden)]` to hide impls that users can never interact with (e.g., `From<PrivateError> for PublicError` where `PrivateError` is not public). Use `pub(crate)` to keep items usable within the crate but out of the public API.

# Prerequisites

- **api-guidelines-overview** -- understanding the overall guidelines framework

# Key Properties

1. Examples should demonstrate *why* to use an item, not just *how* to call it
2. The `?` operator in examples teaches good error handling habits; `unwrap` in examples teaches bad ones
3. Three mandatory documentation sections for functions: "Errors" (for Result-returning functions), "Panics" (for functions that may panic), "Safety" (for unsafe functions)
4. Hyperlinks between documentation items enable navigable, web-like documentation
5. Cargo.toml metadata enables discoverability on crates.io
6. Annotated Git tags are preferred over unannotated tags for releases
7. `#[doc(hidden)]` and `pub(crate)` are complementary tools for hiding implementation details

# Construction / Recognition

## Applying the Documentation Guidelines:
1. **Crate docs** (C-CRATE-DOC): Write a `//!` doc comment at the top of lib.rs with an overview, key concepts, and usage examples
2. **Item examples** (C-EXAMPLE): Add a `# Examples` section to every public item showing a motivating use case, not just a mechanical invocation
3. **Error handling in examples** (C-QUESTION-MARK): Use the `# fn main() -> Result<(), Box<dyn Error>>` pattern with `?` instead of `unwrap`
4. **Failure documentation** (C-FAILURE): Add "Errors", "Panics", and "Safety" sections to function docs as appropriate
5. **Links** (C-LINK): Link to related types, methods, and external resources throughout prose. Use `` [`Type`]: path `` syntax
6. **Metadata** (C-METADATA): Fill in all required Cargo.toml fields; only set `documentation` if not on docs.rs; only set `homepage` if distinct from repo/docs
7. **Release notes** (C-RELNOTES): Maintain release notes, tag releases with annotated Git tags, clearly identify breaking changes
8. **Hidden details** (C-HIDDEN): Apply `#[doc(hidden)]` to impls involving private types; use `pub(crate)` for internal-only items

## The Canonical Example Pattern (C-QUESTION-MARK):
Lines prefixed with `#` are compiled by `cargo test` but hidden from users in rendered documentation. This enables fallible examples without `unwrap`.

# Context & Application

Documentation is what makes an API usable. The Rust ecosystem benefits from a strong documentation culture reinforced by `cargo doc` and docs.rs. These guidelines ensure that:
- New users can orient themselves through crate-level docs and examples
- Error handling patterns in examples teach good habits
- Failure modes are discoverable before runtime
- The documentation graph is navigable via hyperlinks
- Crates are discoverable on crates.io through proper metadata
- Version history is traceable through release notes and tags
- Implementation noise does not obscure the public API

# Examples

**Example 1** (C-EXAMPLE): A poor example of `clone()` merely calls the method without showing why:
```rust
fn main() {
    let hello = "hello";
    hello.clone();
}
```
A good example would show a scenario where cloning is necessary, such as retaining a value while passing ownership to another function.

**Example 2** (C-FAILURE): The `Vec::insert` documentation includes a "Panics" section:
```
/// Inserts an element at position `index` within the vector, shifting all
/// elements after it to the right.
///
/// # Panics
///
/// Panics if `index` is out of bounds.
```

**Example 3** (C-FAILURE): The `std::ptr::read` documentation includes a "Safety" section explaining all invariants the caller must uphold, including that `T` must not be used before overwriting if not Copy, and that the pointer must be aligned.

**Example 4** (C-HIDDEN): Hiding an impl that involves a private type:
```rust
pub struct PublicError { /* ... */ }
struct PrivateError { /* ... */ }

#[doc(hidden)]
impl From<PrivateError> for PublicError {
    fn from(err: PrivateError) -> PublicError { /* ... */ }
}
```

**Example 5** (C-RELNOTES): Tagging a release with an annotated Git tag:
```bash
GIT_COMMITTER_DATE=$(git log -n1 --pretty=%aD) git tag -a -m "Release 0.3.0" 0.3.0
git push --tags
```

# Relationships

## Builds Upon
- **api-guidelines-overview** -- this is one of the 10 guideline categories
- RFC 1687 (crate-level documentation)
- RFC 1574 (API documentation conventions, "Link all the things")
- RFC 1105 (API evolution, defines breaking changes for release notes)

## Enables
- Discoverable and navigable API documentation via docs.rs
- Safe-by-default example code that uses `?` instead of `unwrap`
- Traceable version history through tagged releases and changelogs

## Related
- **api-naming-guidelines** -- good names reduce documentation burden
- **api-predictability-guidelines** -- predictable APIs need less explanation

## Contrasts With
- Undocumented APIs that require source code reading
- Examples that use `unwrap` throughout, teaching unsafe error handling patterns

# Common Errors

- **Error**: Writing examples that mechanically demonstrate how to call a function without showing why.
  **Correction**: Focus examples on motivating use cases. "Readers can be expected to understand how to invoke functions" -- show them *why* they would want to.

- **Error**: Using `unwrap()` in documentation examples for convenience.
  **Correction**: Use the `?` operator with the hidden `fn main() -> Result<(), Box<dyn Error>>` pattern. Example code is often copied verbatim.

- **Error**: Omitting "Errors", "Panics", or "Safety" sections from function documentation.
  **Correction**: Every function returning Result should document error conditions. Every function that can panic should document panic conditions. Every unsafe function must document safety requirements.

# Common Confusions

- **Confusion**: Thinking `#[doc(hidden)]` and `pub(crate)` are interchangeable.
  **Clarification**: `#[doc(hidden)]` hides an item from documentation but keeps it public (accessible by any crate). `pub(crate)` limits visibility to the current crate. They serve different purposes and can be complementary.

- **Confusion**: Thinking the `documentation` field in Cargo.toml is always required.
  **Clarification**: By default, crates.io links to docs.rs. The `documentation` field is only needed if documentation is hosted elsewhere. Similarly, `homepage` is only for a unique dedicated website, not a duplicate of the repo URL.

- **Confusion**: Thinking every conceivable panic must be documented.
  **Clarification**: Panics in caller-provided logic (e.g., a Display impl panicking) need not be exhaustively documented. "When in doubt, err on the side of documenting more panic cases," but use judgment.

# Source Reference

Chapter 4: Documentation. All 8 guidelines (C-CRATE-DOC, C-EXAMPLE, C-QUESTION-MARK, C-FAILURE, C-LINK, C-METADATA, C-RELNOTES, C-HIDDEN) are covered with examples from the standard library (Vec::insert, std::ptr::read, std::io::Read::read) and ecosystem practices (Serde release notes, Diesel changelog).

# Verification Notes

- Definition: All guideline descriptions drawn directly from the chapter text
- Key Properties: Extracted from explicit statements and rationale in each section
- Confidence: HIGH -- the documentation guidelines are concrete with clear examples and referenced RFCs
- Uncertainties: C-CRATE-DOC section is brief (refers to RFC 1687 for detail)
- Cross-reference status: All slugs reference cards in this extraction set
