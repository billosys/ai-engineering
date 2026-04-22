---
concept: Rust API Guidelines Overview
slug: api-guidelines-overview
category: api-design
subcategory: null
tier: foundational
source: "Rust API Guidelines"
source_slug: api-guidelines
authors: "The Rust Library Team"
chapter: "00-about"
chapter_number: 0
pdf_page: null
section: "About / Checklist"
extraction_confidence: high
aliases:
  - "rust api guidelines"
  - "rust library guidelines"
  - "api guidelines checklist"
prerequisites: []
extends: []
related:
  - api-naming-guidelines
  - api-interoperability-guidelines
  - api-macro-guidelines
  - api-documentation-guidelines
  - api-predictability-guidelines
  - api-flexibility-guidelines
  - api-type-safety-guidelines
  - api-dependability-guidelines
  - api-future-proofing-guidelines
  - api-necessities-guidelines
contrasts_with: []
answers_questions:
  - "What are the official Rust API design guidelines?"
  - "How should I design a Rust library API?"
  - "What checklist should I use when reviewing a Rust crate's API?"
  - "What categories do the Rust API guidelines cover?"
---

# Quick Definition

The Rust API Guidelines are the canonical set of recommendations on how to design and present APIs for the Rust programming language. Authored largely by the Rust library team based on experience building the standard library and the broader ecosystem, they cover naming, interoperability, macros, documentation, predictability, flexibility, type safety, dependability, debuggability, future proofing, and necessities.

# Core Definition

"This is a set of recommendations on how to design and present APIs for the Rust programming language. They are authored largely by the Rust library team, based on experiences building the Rust standard library and other crates in the Rust ecosystem." (Ch. 0, About)

The guidelines are explicitly not mandates: "These guidelines should not in any way be considered a mandate that crate authors must follow, though they may find that crates that conform well to these guidelines integrate better with the existing crate ecosystem than those that do not." (Ch. 0, About)

The book is organized in two parts: a concise checklist of all individual guidelines suitable for quick scanning during crate reviews, and topical chapters containing detailed explanations.

# Prerequisites

This is the foundational overview concept for the Rust API Guidelines with no prerequisites.

# Key Properties

1. Guidelines are organized into 10 topical categories: Naming, Interoperability, Macros, Documentation, Predictability, Flexibility, Type safety, Dependability, Debuggability, Future proofing, and Necessities
2. Each guideline has a unique identifier (e.g., C-CASE, C-CONV, C-COMMON-TRAITS) for cross-referencing
3. The guidelines are recommendations, not mandates -- crate authors should use them as they see fit
4. Crates that conform well to these guidelines integrate better with the existing crate ecosystem
5. The checklist format enables quick scanning during crate reviews
6. Guidelines are based on real experience building the Rust standard library and ecosystem crates

# Construction / Recognition

## Full Checklist of All Guidelines:

**Naming** (crate aligns with Rust naming conventions):
- C-CASE: Casing conforms to RFC 430
- C-CONV: Ad-hoc conversions follow `as_`, `to_`, `into_` conventions
- C-GETTER: Getter names follow Rust convention
- C-ITER: Methods on collections that produce iterators follow `iter`, `iter_mut`, `into_iter`
- C-ITER-TY: Iterator type names match the methods that produce them
- C-FEATURE: Feature names are free of placeholder words
- C-WORD-ORDER: Names use a consistent word order

**Interoperability** (crate interacts nicely with other library functionality):
- C-COMMON-TRAITS: Types eagerly implement common traits (Copy, Clone, Eq, PartialEq, Ord, PartialOrd, Hash, Debug, Display, Default)
- C-CONV-TRAITS: Conversions use the standard traits From, AsRef, AsMut
- C-COLLECT: Collections implement FromIterator and Extend
- C-SERDE: Data structures implement Serde's Serialize, Deserialize
- C-SEND-SYNC: Types are Send and Sync where possible
- C-GOOD-ERR: Error types are meaningful and well-behaved
- C-NUM-FMT: Binary number types provide Hex, Octal, Binary formatting
- C-RW-VALUE: Generic reader/writer functions take R: Read and W: Write by value

**Macros** (crate presents well-behaved macros):
- C-EVOCATIVE: Input syntax is evocative of the output
- C-MACRO-ATTR: Macros compose well with attributes
- C-ANYWHERE: Item macros work anywhere that items are allowed
- C-MACRO-VIS: Item macros support visibility specifiers
- C-MACRO-TY: Type fragments are flexible

**Documentation** (crate is abundantly documented):
- C-CRATE-DOC: Crate level docs are thorough and include examples
- C-EXAMPLE: All items have a rustdoc example
- C-QUESTION-MARK: Examples use `?`, not `try!`, not `unwrap`
- C-FAILURE: Function docs include error, panic, and safety considerations
- C-LINK: Prose contains hyperlinks to relevant things
- C-METADATA: Cargo.toml includes all common metadata
- C-RELNOTES: Release notes document all significant changes
- C-HIDDEN: Rustdoc does not show unhelpful implementation details

**Predictability** (crate enables legible code that acts how it looks):
- C-SMART-PTR: Smart pointers do not add inherent methods
- C-CONV-SPECIFIC: Conversions live on the most specific type involved
- C-METHOD: Functions with a clear receiver are methods
- C-NO-OUT: Functions do not take out-parameters
- C-OVERLOAD: Operator overloads are unsurprising
- C-DEREF: Only smart pointers implement Deref and DerefMut
- C-CTOR: Constructors are static, inherent methods

**Flexibility** (crate supports diverse real-world use cases):
- C-INTERMEDIATE: Functions expose intermediate results to avoid duplicate work
- C-CALLER-CONTROL: Caller decides where to copy and place data
- C-GENERIC: Functions minimize assumptions about parameters by using generics
- C-OBJECT: Traits are object-safe if they may be useful as a trait object

**Type safety** (crate leverages the type system effectively):
- C-NEWTYPE: Newtypes provide static distinctions
- C-CUSTOM-TYPE: Arguments convey meaning through types, not bool or Option
- C-BITFLAG: Types for a set of flags are bitflags, not enums
- C-BUILDER: Builders enable construction of complex values

**Dependability** (crate is unlikely to do the wrong thing):
- C-VALIDATE: Functions validate their arguments
- C-DTOR-FAIL: Destructors never fail
- C-DTOR-BLOCK: Destructors that may block have alternatives

**Debuggability** (crate is conducive to easy debugging):
- C-DEBUG: All public types implement Debug
- C-DEBUG-NONEMPTY: Debug representation is never empty

**Future proofing** (crate is free to improve without breaking users' code):
- C-SEALED: Sealed traits protect against downstream implementations
- C-STRUCT-PRIVATE: Structs have private fields
- C-NEWTYPE-HIDE: Newtypes encapsulate implementation details
- C-STRUCT-BOUNDS: Data structures do not duplicate derived trait bounds

**Necessities** (to whom they matter, they really matter):
- C-STABLE: Public dependencies of a stable crate are stable
- C-PERMISSIVE: Crate and its dependencies have a permissive license

# Context & Application

These guidelines represent the accumulated wisdom of the Rust library team from building the standard library and reviewing ecosystem crates. They serve as the authoritative reference for Rust API design, used by:
- Crate authors designing new public APIs
- Reviewers evaluating crate quality and idiomatic adherence
- Teams establishing Rust coding standards
- Contributors to the Rust standard library and ecosystem

The checklist format makes them practical for systematic review: a crate author can walk through each item and evaluate their API against it.

# Examples

**Example 1** (Ch. 0, Checklist): The full checklist provides a scannable format for crate reviews. Each category has a clear theme summarized in parentheses, e.g., "Naming (crate aligns with Rust naming conventions)" and "Interoperability (crate interacts nicely with other library functionality)."

**Example 2** (Ch. 0, About): The guidelines explicitly set expectations for their authority level: "These are only guidelines, some more firm than others. In some cases they are vague and still in development. Rust crate authors should consider them as a set of important considerations in the development of idiomatic and interoperable Rust libraries."

# Relationships

## Builds Upon
- RFC 430 (naming conventions)
- RFC 199 (ownership variants for iterator methods)
- RFC 1574 (API documentation conventions)
- RFC 1105 (API evolution / semver)

## Enables
- **api-naming-guidelines** -- detailed naming conventions (Ch. 1)
- **api-interoperability-guidelines** -- trait and conversion conventions (Ch. 2)
- **api-macro-guidelines** -- macro design guidelines (Ch. 3)
- **api-documentation-guidelines** -- documentation standards (Ch. 4)
- **api-predictability-guidelines** -- predictable API behavior (Ch. 5)
- **api-flexibility-guidelines** -- flexible API design (Ch. 6)

## Related
- **api-type-safety-guidelines** -- type system leverage (Ch. 7, covered by Agent B)
- **api-dependability-guidelines** -- correctness guarantees (Ch. 8, covered by Agent B)
- **api-future-proofing-guidelines** -- backward compatibility (Ch. 9, covered by Agent B)
- **api-necessities-guidelines** -- ecosystem requirements (Ch. 10, covered by Agent B)

## Contrasts With
- Ad hoc API design without systematic review criteria

# Common Errors

- **Error**: Treating the guidelines as absolute rules that must be followed in every case.
  **Correction**: The guidelines are recommendations, not mandates. Some are more firm than others, and some are still in development. Use them as important considerations, not rigid requirements.

- **Error**: Applying the guidelines only to public crate APIs and ignoring internal module boundaries.
  **Correction**: While primarily aimed at public APIs, many guidelines (naming, documentation, predictability) improve code quality at internal module boundaries as well.

# Common Confusions

- **Confusion**: Thinking that following all guidelines guarantees a good API.
  **Clarification**: The guidelines cover necessary but not sufficient conditions. A mechanically compliant API may still have poor ergonomics, unclear abstractions, or missing functionality.

- **Confusion**: Assuming all guidelines carry equal weight.
  **Clarification**: Some guidelines are more firm than others. For example, C-CASE (naming conventions) is nearly universal, while C-SERDE (Serde support) depends on whether the type is a data structure.

# Source Reference

Chapter 0: About and Checklist. The About section defines the purpose and authority of the guidelines. The Checklist section provides the complete enumeration of all guidelines across all categories with their unique identifiers.

# Verification Notes

- Definition: Direct quotation from the opening paragraphs of Chapter 0
- Key Properties: Derived from the structural organization visible in the checklist
- Confidence: HIGH -- this is the official introduction to the canonical Rust API Guidelines
- Uncertainties: None for the overview
- Cross-reference status: All related slugs reference cards in this extraction set or Agent B's planned cards
