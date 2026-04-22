---
concept: AI Design Guidelines
slug: ai-design-guidelines
category: guidelines
subcategory: null
tier: advanced
source: "Pragmatic Rust"
source_slug: pragmatic-rust
authors: "Pragmatic Rust Contributors"
chapter: "08-ai"
chapter_number: 8
pdf_page: null
section: "AI Guidelines"
extraction_confidence: high
aliases:
  - "AI coding guidelines"
  - "LLM-friendly APIs"
  - "agent-friendly Rust"
  - "design for AI"
prerequisites:
  - documentation-guidelines
  - library-ux-guidelines
extends: []
related:
  - naming-and-quality-guidelines
  - library-interop-guidelines
contrasts_with: []
answers_questions:
  - "How do I design Rust APIs that work well with AI coding agents?"
  - "What makes a Rust codebase AI-friendly?"
  - "Why does Rust's type system help AI agents?"
  - "How should I document code for AI consumption?"
  - "What resources exist for using Pragmatic Rust guidelines with LLMs?"
---

# Quick Definition

AI design guidelines establishing that APIs designed for human ergonomics also benefit AI agents (M-DESIGN-FOR-AI), with six specific practices: create idiomatic Rust patterns, provide thorough documentation, include directly usable examples, use strong types to avoid primitive obsession, make APIs testable for rapid AI iteration, and ensure good test coverage for hands-off refactoring. The companion Agents chapter (Ch. 9) offers condensed guideline files for direct inclusion in agent sessions.

# Core Definition

M-DESIGN-FOR-AI establishes that making APIs easier to use for humans also makes them easier for AI, and that Rust's strong type system is "a boon for agents, as their lack of genuine understanding can often be counterbalanced by comprehensive compiler checks." The guideline identifies six practices particularly important for AI effectiveness: (1) Create idiomatic Rust API patterns following the Rust API Guidelines and the Library/UX section; (2) Provide thorough docs for all modules and public items, assuming solid but not expert Rust knowledge; (3) Provide directly usable examples in documentation and elaborate ones in the repository; (4) Use strong types to avoid primitive obsession (C-NEWTYPE); (5) Design testable APIs with mocks, fakes, or cargo features so agents can iterate quickly; (6) Ensure good test coverage over observable behavior to enable hands-off refactoring. Chapter 9 (Agents and LLMs) complements this by offering condensed "all-in-one" guideline text files designed for inclusion in agent sessions. (Ch. 8-9, "AI Guidelines" and "Agents & LLMs")

# Prerequisites

- **documentation-guidelines** -- thorough documentation (M-CANONICAL-DOCS, M-MODULE-DOCS) is explicitly called out as critical for AI effectiveness
- **library-ux-guidelines** -- idiomatic API patterns from the UX guidelines are referenced as the foundation for AI-friendly design

# Key Properties

1. Making APIs easier for humans also makes them easier for AI -- following the other guidelines in the book puts you in good shape
2. Rust's strong type system compensates for AI agents' lack of genuine understanding through comprehensive compiler checks
3. **Idiomatic patterns**: APIs should look and feel like the majority of Rust code; follow the Rust API Guidelines checklist and the Library/UX guidelines
4. **Thorough docs**: Include docs for all modules and public items; assume the reader has solid but not expert understanding of Rust and the standard library
5. **Thorough examples**: Documentation should have directly usable examples; the repository should include more elaborate ones (C-EXAMPLE, C-QUESTION-MARK)
6. **Strong types**: Avoid primitive obsession by using strong types with strict, well-documented semantics (C-NEWTYPE)
7. **Testable APIs**: Design APIs that allow customers to test their usage in unit tests; agents need quick iteration to prove their code works
8. **Test coverage**: Good coverage over observable behavior enables agents to work in mostly hands-off mode during refactoring
9. Chapter 9 provides condensed guideline files for direct inclusion in agent coding or review sessions

# Construction / Recognition

## To Apply M-DESIGN-FOR-AI:
1. Follow the Rust API Guidelines checklist and Library/UX guidelines for idiomatic patterns
2. Document all public modules and items following M-CANONICAL-DOCS and M-MODULE-DOCS
3. Provide runnable code examples in doc comments and the repository examples directory
4. Replace primitive types with strong types (newtypes) where semantics differ
5. Design APIs to be testable without requiring real I/O or external services
6. Maintain comprehensive test coverage over observable behavior

## To Use Agent Resources (Ch. 9):
1. Include the condensed "all" text file in agent sessions for coding or reviewing Rust code
2. The condensed version contains the full guidelines in a single file sized for LLM context windows

# Context & Application

This guideline is notable for explicitly addressing the emerging intersection of AI coding agents and API design. Rather than introducing entirely new practices, it identifies which existing good practices matter most for AI effectiveness. The emphasis on compiler-checked types reflects a key insight: AI agents make frequent mistakes in areas where the compiler cannot help (logic, semantics) but rarely make mistakes where the compiler provides strong feedback (types, lifetimes, borrowing). The testability emphasis reflects that AI agents need rapid feedback loops -- they cannot reason about correctness from first principles as reliably as they can iterate on compile-and-test cycles.

# Examples

**Example 1** (Ch. 8, M-DESIGN-FOR-AI -- Idiomatic patterns): "The more your APIs, whether public or internal, look and feel like the majority of Rust code in the world, the better it is for AI." The guideline references both the Rust API Guidelines checklist and the Library/UX section as the standard to follow.

**Example 2** (Ch. 8, M-DESIGN-FOR-AI -- Documentation for AI): "Agents love good detailed docs. Include docs for all of your modules and public items in your crate. Assume the reader has a solid, but not expert, level of understanding of Rust." References M-MODULE-DOCS, M-CANONICAL-DOCS, C-CRATE-DOC, C-FAILURE, and C-LINK.

**Example 3** (Ch. 8, M-DESIGN-FOR-AI -- Testability): "AI agents need to be able to iterate quickly to prove that the code they are writing that calls your API is working correctly." This may involve introducing mocks, fakes, or cargo features.

**Example 4** (Ch. 9, Agent resources): The "Agents & LLMs" chapter provides a condensed "all" file containing the entire Pragmatic Rust Guidelines in one text file, designed for inclusion in agent sessions.

# Relationships

## Builds Upon
- **documentation-guidelines** -- M-CANONICAL-DOCS and M-MODULE-DOCS are explicitly listed as critical for AI
- **library-ux-guidelines** -- idiomatic API patterns from UX guidelines form the foundation for AI-friendly design

## Enables
- Effective AI-assisted Rust development through well-structured, compiler-checkable APIs
- Hands-off AI refactoring through comprehensive test coverage

## Related
- **naming-and-quality-guidelines** -- consistent naming helps AI pattern-match against training data
- **library-interop-guidelines** -- standard types and patterns improve AI's ability to work with APIs

## Contrasts With
- AI-specific API annotations or metadata (this guideline says good human design is sufficient)
- Projects that rely on comments and documentation alone without compiler-enforced types

# Common Errors

- **Error**: Creating AI-specific documentation or special annotations to help AI agents understand the API.
  **Correction**: Focus on standard Rust idioms, thorough documentation, and strong types. "Making APIs easier to use for humans also makes them easier to use by AI."

- **Error**: Relying on AI to understand subtle API semantics without providing test infrastructure.
  **Correction**: Design testable APIs so agents can iterate through compile-test cycles rather than reasoning about correctness.

- **Error**: Using stringly-typed APIs (passing configuration as raw strings) that compile regardless of semantic errors.
  **Correction**: Use strong types (newtypes) with documented semantics so the compiler catches semantic mistakes that AI agents frequently make.

# Common Confusions

- **Confusion**: Thinking AI-friendly design requires fundamentally different API patterns from human-friendly design.
  **Clarification**: The source explicitly states: "As a general rule, making APIs easier to use for humans also makes them easier to use by AI. If you follow the guidelines in this book, you should be in good shape."

- **Confusion**: Believing that Rust's complexity makes it harder for AI agents than dynamically typed languages.
  **Clarification**: The source argues the opposite: "Rust's strong type system is a boon for agents, as their lack of genuine understanding can often be counterbalanced by comprehensive compiler checks."

# Source Reference

Chapter 8: AI Guidelines, containing one guideline: M-DESIGN-FOR-AI (v0.1). Lists six specific practices with references to Rust API Guidelines (C-CRATE-DOC, C-FAILURE, C-LINK, C-EXAMPLE, C-QUESTION-MARK, C-NEWTYPE) and Pragmatic Rust guidelines (M-MODULE-DOCS, M-CANONICAL-DOCS, Library/UX section). Chapter 9: Agents & LLMs, providing condensed guideline files for agent session inclusion, with a table listing available resources and their sizes.

# Verification Notes

- Definition source: Direct from M-DESIGN-FOR-AI guideline text and Chapter 9 introductory text
- Key Properties: Derived from the six bullet-pointed practices in M-DESIGN-FOR-AI and the resource table in Chapter 9
- Confidence rationale: HIGH -- the guideline is concise and explicit; all six practices are clearly stated with references
- Uncertainties: M-DESIGN-FOR-AI is v0.1, indicating it may evolve significantly; Chapter 9 is very brief (27 lines)
- Cross-reference status: documentation-guidelines, library-ux-guidelines, naming-and-quality-guidelines are from sibling extraction sets
