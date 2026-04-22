---
concept: Pragmatic Rust Guidelines Overview
slug: pragmatic-rust-overview
category: guidelines
subcategory: null
tier: foundational
source: "Pragmatic Rust"
source_slug: pragmatic-rust
authors: "Pragmatic Rust Contributors"
chapter: "00-about"
chapter_number: 0
pdf_page: null
section: "About"
extraction_confidence: high
aliases:
  - "microsoft rust guidelines"
  - "pragmatic rust book"
  - "rust guidelines checklist"
prerequisites: []
extends: []
related:
  - panic-vs-error-guidelines
  - naming-and-quality-guidelines
  - logging-and-observability
  - public-type-guidelines
  - application-guidelines
contrasts_with: []
answers_questions:
  - "What are the Pragmatic Rust guidelines?"
  - "How are the Pragmatic Rust guidelines organized?"
  - "What maturity levels do the guidelines use?"
  - "What criteria must a guideline meet to be included?"
  - "What is the difference between 'must' and 'should' guidelines?"
---

# Quick Definition

Pragmatic Rust is a collection of pragmatic design guidelines helping application and library developers produce idiomatic Rust that scales. The guidelines complement existing upstream resources (Rust API Guidelines, Rust Style Guide, Rust Design Patterns) and address topics often encountered by Rust developers, organized across universal, library, application, FFI, safety, performance, documentation, and AI categories.

# Core Definition

The guidelines build on existing high-quality resources, most notably the Rust API Guidelines checklist. For a guideline to be included, it must meet these meta design principles:

1. It positively affects safety, COGs, or maintenance -- specifically, it must promote safety best practices, lead to high throughput / low latency / low memory usage, or make code readable and understandable.
2. A majority of experienced (3+ years) Rust developers would agree with the guideline.
3. The guideline is reasonably comprehensible to Rust novices (4+ weeks).
4. It is pragmatic -- unrealistic guidelines will not be followed.

The Golden Rule: "Each item here exists for a reason; and it is the spirit that counts, not the letter. Before attempting to work around a guideline, you should understand why it exists and what it tries to safeguard. Likewise, you should not blindly follow a guideline if it becomes apparent that doing so would violate its underlying motivation!" (Ch. 0, About)

# Prerequisites

This is a foundational overview concept with no prerequisites within this source.

# Key Properties

1. Guidelines are organized into categories: Universal, Library (Interoperability, UX, Resilience, Building), Applications, FFI, Safety, Performance, Documentation, and AI
2. Each guideline has a unique identifier (e.g., M-PANIC-IS-STOP, M-APP-ERROR) for cross-referencing
3. Applicability levels: "must" guidelines are supposed to always hold; "should" guidelines indicate more flexibility
4. Each guideline carries a version number analogous to Rust's semver usage, reflecting maturity and evolution
5. The guidelines complement -- not replace -- the Rust API Guidelines, Rust Style Guide, Clippy, and Rust Design Patterns
6. Teams are free to adopt guidelines as they see fit, but deviations should be understood and justified
7. The spirit of each guideline matters more than its literal text

# Construction / Recognition

## To Apply These Guidelines:
1. Start with the upstream guidelines (Rust API Guidelines, Rust Style Guide, Rust Design Patterns) as the foundation
2. Apply the full checklist from Pragmatic Rust as an additional layer
3. For each item that does not make sense for your project, investigate whether the item has issues or truly does not apply
4. When deviating, understand the underlying motivation before working around a guideline

## Checklist Organization (Ch. 0):
- **Universal** (12 items): M-UPSTREAM-GUIDELINES, M-STATIC-VERIFICATION, M-LINT-OVERRIDE-EXPECT, M-PUBLIC-DEBUG, M-PUBLIC-DISPLAY, M-SMALLER-CRATES, M-CONCISE-NAMES, M-REGULAR-FN, M-PANIC-IS-STOP, M-PANIC-ON-BUG, M-DOCUMENTED-MAGIC, M-LOG-STRUCTURED
- **Library / Interoperability** (3 items): M-TYPES-SEND, M-ESCAPE-HATCHES, M-DONT-LEAK-TYPES
- **Library / UX** (11 items): M-SIMPLE-ABSTRACTIONS, M-AVOID-WRAPPERS, M-DI-HIERARCHY, M-ERRORS-CANONICAL-STRUCTS, M-INIT-BUILDER, M-INIT-CASCADED, M-SERVICES-CLONE, M-IMPL-ASREF, M-IMPL-RANGEBOUNDS, M-IMPL-IO, M-ESSENTIAL-FN-INHERENT
- **Library / Resilience** (5 items): M-MOCKABLE-SYSCALLS, M-TEST-UTIL, M-STRONG-TYPES, M-NO-GLOB-REEXPORTS, M-AVOID-STATICS
- **Library / Building** (3 items): M-OOBE, M-SYS-CRATES, M-FEATURES-ADDITIVE
- **Applications** (2 items): M-MIMALLOC-APP, M-APP-ERROR
- **FFI** (1 item): M-ISOLATE-DLL-STATE
- **Safety** (3 items): M-UNSAFE, M-UNSAFE-IMPLIES-UB, M-UNSOUND
- **Performance** (3 items): M-THROUGHPUT, M-HOTPATH, M-YIELD-POINTS
- **Documentation** (4 items): M-FIRST-DOC-SENTENCE, M-MODULE-DOCS, M-CANONICAL-DOCS, M-DOC-INLINE
- **AI** (1 item): M-DESIGN-FOR-AI

# Context & Application

The Pragmatic Rust guidelines were developed to address gaps not covered by existing community resources. While the Rust API Guidelines provide a solid foundation, teams building production Rust applications and libraries encounter many additional design decisions around error handling, logging, crate organization, FFI safety, and performance that benefit from standardized guidance.

**Typical contexts:**
- Teams adopting Rust for production applications and libraries
- Code review checklists for Rust projects
- Onboarding new Rust developers to a team's coding standards
- Configuring CI/CD pipelines with static verification tooling

# Examples

**Example 1** (Ch. 0, Applicability): A team using these guidelines encounters a "must" item that does not apply to their embedded context. Rather than blindly following or ignoring it, they investigate the underlying motivation and either file feedback or document their justified deviation.

**Example 2** (Ch. 0, Meta Design Principles): A proposed guideline requiring complex lifetime annotations on all public APIs would fail the pragmatism criterion -- if it is unrealistic, developers will not follow it, so it would not be included.

# Relationships

## Builds Upon
- Rust API Guidelines (explicitly listed as the primary upstream resource)
- Rust Style Guide, Rust Design Patterns, and the Rust Reference on Undefined Behavior

## Enables
- **panic-vs-error-guidelines** -- M-PANIC-IS-STOP and M-PANIC-ON-BUG define the panic/error boundary
- **naming-and-quality-guidelines** -- M-CONCISE-NAMES, M-DOCUMENTED-MAGIC, M-LINT-OVERRIDE-EXPECT, M-STATIC-VERIFICATION, M-UPSTREAM-GUIDELINES
- **logging-and-observability** -- M-LOG-STRUCTURED for structured logging
- **public-type-guidelines** -- M-PUBLIC-DEBUG, M-PUBLIC-DISPLAY, M-REGULAR-FN, M-SMALLER-CRATES
- **application-guidelines** -- M-APP-ERROR, M-MIMALLOC-APPS, M-ISOLATE-DLL-STATE

## Related
- library-interop-guidelines, library-ux-guidelines, safety-guidelines, performance-guidelines, documentation-guidelines, ai-design-guidelines (covered by other extraction agents)

## Contrasts With
- Ad hoc team conventions lacking structured rationale and versioning

# Common Errors

- **Error**: Treating the guidelines as rigid rules that must be followed to the letter.
  **Correction**: The Golden Rule states that the spirit counts, not the letter. If following a guideline literally would violate its underlying motivation, deviate with justification.

- **Error**: Ignoring upstream guidelines (Rust API Guidelines, Clippy) and treating Pragmatic Rust as a standalone replacement.
  **Correction**: M-UPSTREAM-GUIDELINES explicitly requires following the existing community guidelines; Pragmatic Rust is a complement, not a replacement.

# Common Confusions

- **Confusion**: Thinking "must" and "should" have no practical difference.
  **Clarification**: "Must" guidelines are supposed to always hold; "should" guidelines indicate flexibility. Both can be deviated from with good reason, but "must" items require stronger justification.

- **Confusion**: Assuming guideline version numbers indicate priority or importance.
  **Clarification**: Version numbers (e.g., 1.0, 0.1) indicate maturity and evolution stage, analogous to Rust's semver system. A 0.1 guideline may still be critical but is newer and more likely to evolve.

# Source Reference

Chapter 0: About, all sections (Meta Design Principles, Applicability, The Golden Rule, Guideline Maturity, Submitting New Guidelines) and the full Checklist. The chapter defines the purpose, organizational structure, and adoption philosophy of the guidelines.

# Verification Notes

- Definition: Drawn directly from the opening statement and Meta Design Principles section
- Key Properties: Directly from the chapter text and checklist
- Confidence: HIGH -- the chapter is explicit about its purpose, criteria, and structure
- Uncertainties: None for the overview
- Cross-reference status: All related slugs are within this extraction set or reference Agent B's planned cards
