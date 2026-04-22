---
concept: Contain Unsafety in Small Modules
slug: contain-unsafety
category: structural-pattern
subcategory: null
tier: intermediate
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "02-design-patterns"
chapter_number: 2
pdf_page: null
section: "Contain unsafety in small modules"
extraction_confidence: high
aliases:
  - "unsafe containment"
  - "safe wrapper over unsafe"
  - "minimal unsafe surface"
prerequisites: []
extends: []
related:
  - prefer-small-crates
  - ffi-object-based-api
  - ffi-type-consolidation
contrasts_with: []
answers_questions:
  - "How should I organize unsafe code in Rust?"
  - "How do I minimize the unsafe surface area in my crate?"
  - "What is the relationship between safe wrappers and unsafe implementations?"
---

# Quick Definition

When using `unsafe` code, create the smallest possible module that upholds the needed invariants and build a minimal safe interface on top of it. Embed this module into a larger one containing only safe code that presents an ergonomic API. This restricts the scope of code requiring audit and makes writing the outer safe module easier.

# Core Definition

"If you have unsafe code, create the smallest possible module that can uphold the needed invariants to build a minimal safe interface upon the unsafety. Embed this into a larger module that contains only safe code and presents an ergonomic interface. Note that the outer module can contain unsafe functions and methods that call directly into the unsafe code. Users may use this to gain speed benefits." (Ch. 2, "Contain unsafety in small modules")

# Prerequisites

None -- this guideline is applicable to any Rust developer working with `unsafe` code, though understanding why `unsafe` exists is assumed.

# Key Properties

1. Unsafe code is isolated into the smallest possible module
2. The inner module upholds invariants needed for soundness and exposes a minimal safe interface
3. The outer module contains only safe code and provides an ergonomic public API
4. The outer module may optionally expose `unsafe` functions that bypass the safe wrapper for performance
5. This restricts the amount of code that must be audited for memory safety
6. The outer module can rely on the inner module's invariant guarantees

# Construction / Recognition

## To Apply This Guideline:
1. Identify all `unsafe` operations required by your functionality
2. Determine the minimal set of invariants these operations require
3. Create a small inner module that encapsulates all `unsafe` code
4. Define a safe interface on this inner module that enforces the invariants
5. Build an ergonomic outer module using only the inner module's safe interface
6. Optionally expose `unsafe` escape hatches in the outer module for power users

## To Recognize This Pattern:
1. A module with `unsafe` blocks wrapped by safe public functions
2. A layered architecture: inner unsafe module, outer safe module
3. Safe public API with optional unsafe alternatives for performance

# Context & Application

This pattern reflects a core Rust philosophy: minimize the surface area of `unsafe` code. By containing unsafety in small modules, developers reduce the amount of code that must be carefully audited for soundness.

The source provides two real-world examples. The `toolshed` crate contains its unsafe operations in submodules while presenting a safe interface to users. The standard library's `String` is a wrapper over `Vec<u8>` with the added invariant that contents are valid UTF-8. Operations on `String` enforce this invariant through safe methods, but users also have access to `unsafe` methods (like `String::from_utf8_unchecked`) where the onus is on them to guarantee validity.

This guideline is closely related to the FFI patterns, where the boundary between safe Rust and foreign code requires careful containment of unsafety.

# Examples

**Example 1** (Ch. 2, "Contain unsafety" -- Examples): "The toolshed crate contains its unsafe operations in submodules, presenting a safe interface to users." This demonstrates the inner-module/outer-module layering.

**Example 2** (Ch. 2, "Contain unsafety" -- Examples): "std's String class is a wrapper over Vec<u8> with the added invariant that the contents must be valid UTF-8. The operations on String ensure this behavior. However, users have the option of using an unsafe method to create a String, in which case the onus is on them to guarantee the validity of the contents."

# Relationships

## Builds Upon
- Rust's `unsafe` system and the concept of soundness invariants

## Enables
- **ffi-object-based-api** -- FFI APIs apply this principle by containing pointer unsafety behind safe Rust interfaces
- **ffi-type-consolidation** -- type consolidation wrappers contain unsafe lifetime management in a safe wrapper
- Auditable unsafe code with clear boundaries

## Related
- **prefer-small-crates** -- similar philosophy of keeping units small and focused, applied to crate organization

## Contrasts With
- Scattering `unsafe` blocks throughout a codebase without clear module boundaries
- Wrapping everything in `unsafe` without providing safe alternatives

# Common Errors

- **Error**: Making the inner unsafe module too large, defeating the purpose of containment.
  **Correction**: Keep the inner module as small as possible. Only include code that genuinely requires `unsafe` and the minimal logic needed to establish invariants.

- **Error**: Exposing the inner module's unsafe details in the outer module's public API.
  **Correction**: The outer module should present a fully safe ergonomic interface. Unsafe escape hatches should be clearly documented and optional.

# Common Confusions

- **Confusion**: Thinking "contain unsafety" means never using `unsafe`.
  **Clarification**: The guideline is about organization, not avoidance. `unsafe` is sometimes necessary; the point is to isolate it so the rest of the codebase can be safe.

- **Confusion**: Thinking the outer module cannot contain any `unsafe` functions.
  **Clarification**: The source explicitly says "the outer module can contain unsafe functions and methods that call directly into the unsafe code. Users may use this to gain speed benefits." The key is that the default API is safe.

# Source Reference

Chapter 2: Design Patterns, "Contain unsafety in small modules" section (Structural Patterns). Brief section with two real-world examples (toolshed crate, std::String) and a link to Ralf Jung's blog about invariants in unsafe code.

# Verification Notes

- Definition source: Direct quotation from "Description" subsection
- Key Properties: Derived from the description and examples
- Confidence rationale: HIGH -- the source is concise but clear, with real-world examples from std and the ecosystem
- Uncertainties: None
- Note: This is more of an organizational guideline than a classic design pattern. The source presents it as a structural pattern but it is primarily advice about module organization for unsafe code.
- Cross-reference status: `ffi-object-based-api` and `ffi-type-consolidation` are in this extraction set; `prefer-small-crates` is in this extraction set
