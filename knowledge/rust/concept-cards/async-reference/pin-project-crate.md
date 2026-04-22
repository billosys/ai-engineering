---
concept: Pin-Project Crate
slug: pin-project-crate
category: type-system
subcategory: null
tier: advanced
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Pinning"
chapter_number: 2
pdf_page: null
section: "Macros for pin projection"
extraction_confidence: high
aliases:
  - "pin-project"
  - "pin-project-lite"
  - "#[pin_project]"
  - "pin_project! macro"
  - "pin projection macros"
prerequisites:
  - structural-pinning
  - pin-type
extends:
  - structural-pinning
related:
  - pinned-self
  - pin-and-drop
contrasts_with: []
answers_questions:
  - "How do I implement pin projection for a struct?"
  - "What macros are available for pin projection?"
  - "What is the difference between pin-project and pin-project-lite?"
---

# Quick Definition

The `pin-project` and `pin-project-lite` crates provide macros that generate safe pin projection code automatically, eliminating the need for hand-written `unsafe` projection methods on structs with pinned fields.

# Core Definition

"The pin-project crate provides the `#[pin_project]` attribute macro (and the `#[pin]` helper attribute) which implements safe pin projection for you by creating a pinned version of the annotated type which can be accessed using the `project` method on the annotated type." (Ch. 2, "Macros for pin projection")

"Pin-project-lite is an alternative using a declarative macro (`pin_project!`) which works in a very similar way to pin-project. Pin-project-lite is lightweight in the sense that it is not a procedural macro and therefore does not add dependencies for implementing procedural macros to your project. However, it is less expressive than pin-project and does not give custom error messages." (Ch. 2, "Macros for pin projection")

# Prerequisites

- **Structural pinning** — Must understand what pin projection is and why it requires `unsafe` code to appreciate what these crates automate
- **Pin type** — Must understand `Pin<Ptr>` to use the projected types these crates generate

# Key Properties

1. `pin-project` uses a procedural `#[pin_project]` attribute macro with a `#[pin]` helper attribute to mark structurally pinned fields
2. `pin-project` generates a pinned version of the annotated type accessible via the `project` method
3. `pin-project-lite` uses a declarative `pin_project!` macro with similar functionality
4. `pin-project-lite` avoids procedural macro dependencies (lighter compile footprint)
5. `pin-project-lite` is less expressive than `pin-project` and lacks custom error messages
6. `pin-project-lite` is recommended when you want to avoid proc-macro dependencies; `pin-project` is recommended otherwise
7. The older `pin-utils` crate and its `unsafe_pinned` macro are deprecated in favor of these crates and std functionality

# Construction / Recognition

## To Use pin-project

1. Add `pin-project` to your `Cargo.toml` dependencies
2. Annotate your struct with `#[pin_project]`
3. Mark structurally pinned fields with `#[pin]`
4. Use the generated `project()` method on `Pin<&mut Self>` to access fields
5. Structurally pinned fields are projected as `Pin<&mut Field>`, others as `&mut Field`

## To Use pin-project-lite

1. Add `pin-project-lite` to your `Cargo.toml` dependencies
2. Define your struct inside the `pin_project!` macro invocation
3. Mark structurally pinned fields with `#[pin]`
4. Use the generated projection methods similarly to `pin-project`

# Context & Application

Manual pin projection requires `unsafe` code and careful reasoning about safety invariants. These crates exist to make pin projection safe and ergonomic. They are widely used in the async Rust ecosystem — nearly every custom future or stream implementation that needs field access uses one of these crates.

The recommendation from the source: "Pin-project-lite is recommended if you want to avoid adding the procedural macro dependencies, and pin-project is recommended otherwise." (Ch. 2, "Macros for pin projection")

In practice, `pin-project-lite` is very common in library code (e.g., `tokio` uses it) because it minimizes the dependency tree. `pin-project` is preferred in application code or when better error messages and full expressiveness are desired.

# Examples

**pin-project usage pattern** (Ch. 2, "Macros for pin projection"):
> The `#[pin_project]` attribute macro with `#[pin]` helper "implements safe pin projection for you by creating a pinned version of the annotated type which can be accessed using the `project` method."

**pin-project-lite** (Ch. 2, "Macros for pin projection"):
> "Pin-project-lite is an alternative using a declarative macro (`pin_project!`) which works in a very similar way to pin-project."

**Deprecated alternatives** (Ch. 2, "Macros for pin projection"):
> "Pin-utils provides the `unsafe_pinned` macro to help implement pin projection, but the whole crate is deprecated in favor of the above crates and functionality now in std."

# Relationships

## Builds Upon
- **Structural pinning** — These crates automate the unsafe boilerplate of structural pin projection

## Enables
(none specific — these are tooling that enables safe use of structural pinning)

## Related
- **Pinned self** — The projection methods operate on `Pin<&mut Self>`
- **Pin and drop** — pin-project handles the `Drop` implications of structural pinning automatically

## Contrasts With
(none)

# Common Errors

- **Error**: Forgetting to mark a field with `#[pin]` when it should be structurally pinned.
  **Correction**: If a field is address-sensitive or contains a sub-future that needs to be polled, mark it with `#[pin]`. The generated projection will then return `Pin<&mut Field>` for that field.

- **Error**: Using the deprecated `pin-utils` crate's `unsafe_pinned` macro in new code.
  **Correction**: Use `pin-project` or `pin-project-lite` instead. `pin-utils` is deprecated.

# Common Confusions

- **Confusion**: Thinking you must choose between pin-project and writing unsafe code, with no middle ground.
  **Clarification**: `pin-project-lite` provides a lighter-weight alternative that avoids procedural macro dependencies while still generating safe projection code.

- **Confusion**: Believing pin-project and pin-project-lite have identical capabilities.
  **Clarification**: `pin-project` (procedural macro) is more expressive and gives better error messages. `pin-project-lite` (declarative macro) is lighter but less expressive.

# Source Reference

Chapter 2: Pinning, section "Macros for pin projection."

# Verification Notes

- Definition source: Direct quotations from Ch. 2, "Macros for pin projection" section (lines 215-223 of source)
- Confidence rationale: HIGH — the source clearly describes each crate's mechanism, trade-offs, and recommendations
- Uncertainties: None — though the ecosystem evolves, the source's recommendations are current
- Cross-reference status: Slugs verified against co-extracted concepts (structural-pinning, pin-type, pinned-self, pin-and-drop)
