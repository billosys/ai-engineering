---
# === CORE IDENTIFICATION ===
concept: Edition Interoperability
slug: edition-interoperability

# === CLASSIFICATION ===
category: edition-system
subcategory: core-concepts
tier: foundational

# === PROVENANCE ===
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "What Are Editions"
chapter_number: 1
pdf_page: null
section: "Editions do not split the ecosystem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "cross-edition compatibility"
  - "edition compatibility"
  - "editions do not split the ecosystem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rust-editions
extends: []
related:
  - edition-migration
  - rust-2015-edition
  - rust-2018-edition
  - rust-2021-edition
  - rust-2024-edition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can a crate on Rust 2018 depend on a crate on Rust 2015?"
  - "Do editions split the Rust ecosystem?"
  - "How do crates on different editions work together?"
  - "What limits do interoperability requirements place on edition changes?"
  - "How does macro edition hygiene work across editions?"
---

# Quick Definition

Edition interoperability is the guarantee that Rust crates compiled with different editions can seamlessly depend on and interoperate with each other. This is the "most consequential rule" of the edition system: editions never split the ecosystem, and each crate's edition choice is a private decision that does not affect its dependents or dependencies.

# Core Definition

The source states: "When creating editions, there is one most consequential rule: crates in one edition must seamlessly interoperate with those compiled with other editions." (Ch. 1: What Are Editions). This means a crate on edition 2024 can depend on a crate compiled with edition 2015, and vice versa, with no compatibility issues. Each crate's edition choice is described as "private" -- it won't affect other crates in the ecosystem.

This interoperability guarantee constrains what editions can change. As the source explains: "For Rust, this required compatibility implies some limits on the kinds of changes that can be featured in an edition. As a result, changes found in new Rust editions tend to be 'skin deep'." All Rust code, regardless of edition, compiles to the same internal representation within the compiler.

# Prerequisites

- **rust-editions** -- Understanding the edition system is necessary to understand interoperability

# Key Properties

1. **Seamless cross-edition dependencies**: Crates on any edition can depend on crates on any other edition
2. **Private edition choice**: A crate's edition selection does not propagate to or constrain its dependencies or dependents
3. **Same internal representation**: All editions compile to identical compiler IR, ensuring binary compatibility
4. **Skin-deep changes**: The interoperability requirement limits editions to surface-level (syntactic) changes
5. **Macro hygiene across editions**: Tokens in macros are tagged with their source edition, allowing macros defined in one edition to be called from another

# Construction / Recognition

## How Interoperability Works:
- The compiler handles edition differences during parsing/compilation
- Each crate's tokens are tagged with their edition for proper interpretation
- After parsing, all editions produce the same internal representation
- The linker and runtime see no edition distinctions

## Macro Edition Hygiene:
- Tokens within macros are marked with which edition they come from
- A macro defined in a 2015 crate using `dyn` as an identifier works when called from a 2018 crate (where `dyn` is a keyword) because the tokens retain their 2015 edition tag
- "The parser looks at the edition of the tokens to know how to interpret it"

# Context & Application

Edition interoperability is what makes the entire edition system viable. Without it, each new edition would fragment the ecosystem into incompatible subsets (similar to the Python 2/3 split). Because interoperability is guaranteed, library authors can stay on older editions without blocking their users from adopting newer editions, and projects can incrementally migrate their dependency trees without coordination.

This guarantee also means that edition adoption has no urgency pressure from the ecosystem. A crate on edition 2015 will continue to work as a dependency for crates on edition 2024, indefinitely.

# Examples

**Example 1** (Ch 1): The fundamental guarantee:
> "Crates in one edition must seamlessly interoperate with those compiled with other editions. In other words, each crate can decide when to migrate to a new edition independently. This decision is 'private' -- it won't affect other crates in the ecosystem."

**Example 2** (Ch 1): Why changes are "skin deep":
> "For Rust, this required compatibility implies some limits on the kinds of changes that can be featured in an edition. As a result, changes found in new Rust editions tend to be 'skin deep'. All Rust code -- regardless of edition -- will ultimately compile down to the same internal representation within the compiler."

**Example 3** (Ch 1): Macro hygiene preserving cross-edition compatibility:
> "If [a] macro was defined in a crate using the 2015 edition, then that macro works fine, even if it were called from a 2018 crate where `dyn` is a keyword and that would normally be a syntax error. The `let dyn = 1;` tokens are marked as being from 2015, and the compiler will remember that wherever that code gets expanded."

# Relationships

## Builds Upon
- **rust-editions** -- interoperability is a core property of the edition system

## Enables
- **edition-migration** -- because editions interoperate, migration can happen incrementally without coordinating with dependencies
- **rust-2018-edition** -- interoperability ensures 2018 crates work with all other editions
- **rust-2021-edition** -- interoperability ensures 2021 crates work with all other editions
- **rust-2024-edition** -- interoperability ensures 2024 crates work with all other editions

## Related
- **edition-migration** -- migration is optional precisely because interoperability is guaranteed
- **rust-2015-edition** -- 2015 crates remain compatible with all future editions

## Contrasts With
- None within this source

# Common Errors

- **Error**: Assuming that upgrading your crate's edition will break downstream users on older editions.
  **Correction**: Edition choice is private. Upgrading your crate to a newer edition has no effect on your dependents regardless of which edition they use.

- **Error**: Believing you must upgrade your dependencies' editions before upgrading your own.
  **Correction**: Dependencies on older editions work seamlessly. You can upgrade your crate independently.

# Common Confusions

- **Confusion**: Comparing Rust editions to the Python 2/3 ecosystem split.
  **Clarification**: Unlike Python 2/3, Rust editions are fully interoperable. A crate on edition 2015 and a crate on edition 2024 can be linked together in the same binary with no issues.

- **Confusion**: Thinking that macros from older-edition crates won't work in newer-edition crates.
  **Clarification**: Macro edition hygiene tags tokens with their source edition. A macro defined in a 2015 crate generally works when invoked from a 2018+ crate. The exception is when the macro's own crate upgrades its edition, potentially changing how its tokens are parsed.

- **Confusion**: Assuming interoperability means editions can't make meaningful changes.
  **Clarification**: Editions can introduce new keywords, change path resolution, and modify other surface syntax. The constraint is that changes must be "skin deep" -- they all compile to the same internal representation.

# Source Reference

Chapter 1: What Are Editions; section "Editions do not split the ecosystem" and "Advanced migration strategies" (macro hygiene). No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch 1 -- "crates in one edition must seamlessly interoperate with those compiled with other editions"
- Confidence rationale: HIGH -- the source explicitly states this as the "most consequential rule" of the edition system
- Uncertainties: The macro hygiene discussion notes some edge cases where macros may not work correctly across edition boundaries
- Cross-reference status: rust-editions, edition-migration are in this extraction set; rust-2021-edition, rust-2024-edition from other agents
