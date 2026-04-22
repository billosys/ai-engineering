---
concept: Pinning Alternatives and Extensions
slug: pinning-alternatives
category: type-system
subcategory: null
tier: advanced
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Pinning"
chapter_number: 2
pdf_page: null
section: "Alternatives and extensions"
extraction_confidence: high
aliases:
  - "Move trait alternative"
  - "pinned places"
  - "UnpinCell"
  - "MinPin"
  - "Overwrite trait"
  - "immovable types"
prerequisites:
  - pinning
  - pin-type
  - unpin-trait
  - move-semantics
extends:
  - pinning
related:
  - pin-and-async
  - structural-pinning
contrasts_with: []
answers_questions:
  - "Why does Rust use Pin instead of immovable types?"
  - "What alternatives to pinning have been considered?"
  - "What proposals exist to improve pinning ergonomics?"
---

# Quick Definition

Rust's pinning design was shaped by post-1.0 backwards-compatibility constraints. Alternatives like a `Move` trait or C++-style move constructors were considered but rejected; proposed extensions like pinned places, `UnpinCell`, MinPin, and the `Overwrite` trait aim to improve pinning ergonomics without breaking existing code.

# Core Definition

The source frames the design space: "If you are designing a brand new language and want to support async/await, self-references, or immovable types there are certainly better ways to do so than Rust's pinning. However, async/await, futures, and pinning were added to Rust after its 1.0 release and designed in the context of a strong backwards-compatibility guarantee." (Ch. 2, "Alternatives and extensions")

**Considered alternatives** (Ch. 2, "Alternatives"):
- **`Move` trait**: A marker trait (like `Copy`) where types not implementing `Move` are immovable. Rejected because "pinning today is a phased concept (a place starts unpinned and becomes pinned) and types apply to the whole lifetime of values," and `Move` bounds would be "infectious" (required in many places).
- **C++ move constructors**: Rejected because it "breaks the fundamental invariant of Rust that objects can always be bit-wise moved" and would "silently break unsafe code."
- **Offset references**: Relative rather than absolute pointers. Rejected because "a field must be either an offset pointer or an absolute pointer. But references in async functions become fields which sometimes reference memory internal to the future object and sometimes reference memory outside it."

**Proposed extensions** (Ch. 2, "Extensions"):
- **Pinned places**: Adds a `pin`/`pinned` modifier to references similar to `mut`, integrating with reborrowing and method resolution.
- **`UnpinCell`**: Extends pinned places to support native pin projection of fields.
- **MinPin**: A more minimal and backwards-compatible proposal for native pin projection and better `drop` support.
- **`Overwrite` trait**: Distinguishes permission to modify part of an object from permission to overwrite the whole object; a sort-of replacement for `Unpin`.

# Prerequisites

- **Pinning** — Must understand the current pinning system to appreciate why alternatives were considered
- **Pin type** — Must understand `Pin<Ptr>` to see what the extensions aim to improve
- **Unpin trait** — Several alternatives and extensions are designed as improvements to or replacements for `Unpin`
- **Move semantics** — The `Move` trait alternative directly relates to Rust's move semantics

# Key Properties

1. Pinning was designed under backwards-compatibility constraints of a post-1.0 language
2. A `Move` trait approach fails because pinning is phased (not a whole-lifetime property) and would cause infectious bounds
3. C++ move constructors would break Rust's fundamental bitwise-move invariant and silently break unsafe code
4. Offset references cannot handle references that sometimes point internally and sometimes externally
5. Pinned places would make pinning a language-level concept with `pin`/`pinned` reference modifiers
6. `UnpinCell` would enable native pin projection without unsafe code
7. MinPin is the most minimal backwards-compatible proposal for better pin projection and drop
8. The `Overwrite` trait separates field modification from whole-object replacement

# Construction / Recognition

This card documents design alternatives and proposals, not procedural knowledge. There is no construction procedure.

## To Evaluate Whether an Alternative Would Help Your Use Case

1. Identify your pain point: Is it pin projection ergonomics? Drop interaction? Infectious bounds?
2. Pinned places primarily helps with method call ergonomics and reborrowing
3. `UnpinCell`/MinPin primarily helps with pin projection
4. The `Overwrite` trait primarily helps with the `Unpin` model and field immutability

# Context & Application

This topic is primarily of interest to language designers, compiler contributors, and those curious about Rust's design trade-offs. The source is explicit: "This section is for those with a curiosity about the language design around pinning. You absolutely don't need to read this section if you just want to read, understand, and write async programs." (Ch. 2, "Alternatives and extensions")

Understanding the alternatives illuminates *why* pinning works the way it does. The phased nature of pinning (objects start unpinned, become pinned) is a key insight that explains why simpler approaches like a `Move` trait don't work: types describe whole-lifetime properties, but pinning is a state change during an object's lifetime.

The extensions are active areas of Rust language development. Pinned places and MinPin in particular may materialize in future Rust editions.

# Examples

**Why a Move trait fails** (Ch. 2, "Alternatives"):
> "pinning today is a phased concept (a place starts unpinned and becomes pinned) and types apply to the whole lifetime of values."

**Why move constructors fail** (Ch. 2, "Alternatives"):
> "this breaks the fundamental invariant of Rust that objects can always be bit-wise moved. That would make Rust much less predictable... This is a backwards-incompatible change of the worst kind because it would silently break unsafe code."

**Why offset references fail** (Ch. 2, "Alternatives"):
> "references in async functions become fields which sometimes reference memory internal to the future object and sometimes reference memory outside it."

**Pinned places proposal** (Ch. 2, "Extensions"):
> "Pinned places runs with the idea that pinning is property of places rather than values or types, and adds a `pin`/`pinned` modifier to references similar to `mut`."

# Relationships

## Builds Upon
- **Pinning** — These are alternatives to and extensions of the current pinning design
- **Move semantics** — The `Move` trait and move constructor alternatives directly relate to move semantics

## Enables
(none — these are proposals, not implemented features)

## Related
- **Pin and async** — Async/await is the primary motivation driving both the current design and proposed improvements
- **Structural pinning** — Pin projection ergonomics is a major driver for the extension proposals

## Contrasts With
(none)

# Common Errors

- **Error**: Attempting to implement a `Move`-like trait or immovable type pattern in current Rust.
  **Correction**: Rust does not support immovable types. Use `Pin` with `!Unpin` to express address stability for specific pointer/place combinations.

# Common Confusions

- **Confusion**: Thinking that pinning is a poor design that should have been avoided.
  **Clarification**: Pinning was the pragmatic choice given Rust's post-1.0 constraints. The source notes that solutions involving linear types "would require fundamental research, design, and implementation that would realistically be measured in decades."

- **Confusion**: Expecting the proposed extensions to be available now.
  **Clarification**: Pinned places, `UnpinCell`, MinPin, and `Overwrite` are proposals at various stages of development. None are stabilized in Rust as of the source's writing.

- **Confusion**: Believing C++ move constructors would solve Rust's problems better.
  **Clarification**: Move constructors would break Rust's bitwise-move invariant, and external references to a moved object could not be fixed up by a move constructor anyway.

# Source Reference

Chapter 2: Pinning, sections "Alternatives and extensions," "Alternatives," and "Extensions." References multiple blog posts including: "Two Ways Not to Move" (theincredibleholk), "Ergonomic Self-Referential Types for Rust" (yoshuawuyts), "Pin" (without.boats), "Pinned places" (without.boats), "UnpinCell" (without.boats), "MinPin" (smallcultfollowing), and "Overwrite trait" (smallcultfollowing).

# Verification Notes

- Definition source: Direct quotations from Ch. 2, "Alternatives and extensions" sections (lines 286-318 of source)
- Confidence rationale: HIGH — the source provides detailed analysis of each alternative with clear reasoning for why they were rejected or how they would work
- Uncertainties: The extension proposals are evolving — their current status may differ from the source's description
- Cross-reference status: Slugs verified against Agent A concepts (pinning, unpin-trait, move-semantics) and co-extracted concepts (pin-type, pin-and-async, structural-pinning)
