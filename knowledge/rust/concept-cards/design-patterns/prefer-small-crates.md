---
concept: Prefer Small Crates
slug: prefer-small-crates
category: structural-pattern
subcategory: null
tier: intermediate
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "02-design-patterns"
chapter_number: 2
pdf_page: null
section: "Prefer small crates"
extraction_confidence: high
aliases:
  - "small crate philosophy"
  - "fine-grained dependencies"
  - "modular crates"
prerequisites: []
extends: []
related:
  - contain-unsafety
contrasts_with: []
answers_questions:
  - "Should I use many small crates or fewer large ones in Rust?"
  - "What are the trade-offs of fine-grained dependencies in Rust?"
  - "How does Rust's compilation model affect crate organization?"
---

# Quick Definition

Prefer small crates that do one thing well. Cargo and crates.io make it easy to add third-party libraries, and since published packages cannot be edited or removed, builds that work now should continue to work. Smaller, more fine-grained dependencies encourage modular code and enable parallel compilation.

# Core Definition

"Prefer small crates that do one thing well. Cargo and crates.io make it easy to add third-party libraries, much more so than in say C or C++. Moreover, since packages on crates.io cannot be edited or removed after publication, any build that works now should continue to work in the future. We should take advantage of this tooling, and use smaller, more fine-grained dependencies." (Ch. 2, "Prefer small crates")

# Prerequisites

None -- this is a high-level organizational guideline accessible to all Rust developers.

# Key Properties

1. Small crates are easier to understand and encourage modular code
2. Crates enable code reuse across projects (e.g., the `url` crate originated from Servo but is now widely used)
3. Since Rust's compilation unit is the crate, splitting into multiple crates enables more parallel compilation
4. Published crates on crates.io cannot be edited or removed, providing build stability
5. Cargo makes adding dependencies straightforward compared to C/C++
6. The trade-off includes risk of dependency conflicts, uncurated quality, and reduced cross-crate optimization

# Construction / Recognition

## To Apply This Guideline:
1. When building a project, identify self-contained units of functionality
2. Extract these into separate crates if they could be reused across projects
3. Prefer using existing well-maintained small crates over reimplementing functionality
4. Keep each crate focused on a single responsibility

## To Recognize When This Applies:
1. A project contains utility code that could benefit other projects
2. A monolithic crate has grown large and compilation is slow
3. A function or module has no project-specific dependencies and could stand alone

# Context & Application

This guideline reflects the Rust ecosystem's philosophy, modeled partly on the npm ecosystem's emphasis on small, composable packages. The Cargo package manager and crates.io registry make this feasible by providing easy dependency management and immutable publication.

The source highlights three concrete examples: the `url` crate (URL parsing, originated from Servo), the `num_cpus` crate (querying CPU count), and the `ref_slice` crate (converting `&T` to `&[T]`, noted as a historical example).

However, the source also warns of real drawbacks: dependency hell when conflicting versions are required (e.g., `url` 1.0 vs 0.5 producing incompatible types), uncurated quality on crates.io (poorly written, undocumented, or malicious crates), and reduced optimization since the compiler does not perform link-time optimization (LTO) by default across crate boundaries.

# Examples

**Example 1** (Ch. 2, "Prefer small crates" -- Examples): The `url` crate provides tools for working with URLs. Originally developed for the Servo browser engine, it found wide use outside the project, demonstrating how small crates promote code reuse.

**Example 2** (Ch. 2, "Prefer small crates" -- Disadvantages): The source describes dependency hell: "the url crate has both versions 1.0 and 0.5. Since the Url from url:1.0 and the Url from url:0.5 are different types, an HTTP client that uses url:0.5 would not accept Url values from a web scraper that uses url:1.0."

# Relationships

## Builds Upon
- Rust's crate-based compilation model
- Cargo's dependency management

## Enables
- Code reuse across projects
- Faster parallel compilation
- Ecosystem growth through composable packages

## Related
- **contain-unsafety** -- another structural guideline about module organization within a crate

## Contrasts With
- Monolithic crate design (all functionality in one large crate)
- Vendoring or copying code rather than depending on external crates

# Common Errors

- **Error**: Depending on many small crates without auditing them for quality or security.
  **Correction**: The source warns that "packages on crates.io are not curated. A crate may be poorly written, have unhelpful documentation, or be outright malicious." Evaluate dependencies before adopting them.

- **Error**: Splitting a project into too many crates, creating circular or conflicting version dependencies.
  **Correction**: Balance modularity with practical dependency management. Not every function needs its own crate.

# Common Confusions

- **Confusion**: Thinking small crates always lead to better performance.
  **Clarification**: The source notes "two small crates may be less optimized than one large one, since the compiler does not perform link-time optimization (LTO) by default." Cross-crate optimization boundaries can reduce performance.

- **Confusion**: Thinking crates.io immutability means dependencies are always safe.
  **Clarification**: Immutability means a published version cannot be silently changed, but it does not mean the crate is well-written, secure, or maintained.

# Source Reference

Chapter 2: Design Patterns, "Prefer small crates" section (Structural Patterns). Provides advantages, disadvantages, and examples including `url`, `num_cpus`, and `ref_slice` crates. No code examples -- this is a guideline rather than a code pattern.

# Verification Notes

- Definition source: Direct quotation from "Description" subsection
- Key Properties: All from explicit statements in the source
- Confidence rationale: HIGH -- the source clearly states the guideline with concrete examples and balanced trade-offs
- Uncertainties: None
- Note: This is more of an organizational guideline or philosophy than a classic design pattern. The source presents it alongside patterns but it is primarily advice about crate granularity rather than a code-level pattern.
- Cross-reference status: `contain-unsafety` is in this extraction set
