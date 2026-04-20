---
# === CORE IDENTIFICATION ===
concept: Simplicity Principle
slug: simplicity-principle

# === CLASSIFICATION ===
category: principles
subcategory: style-principles
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Guide"
chapter_number: 2
pdf_page: null
section: "Style principles"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "simplicity in Go"
  - "simple code principle"
  - "avoid unnecessary complexity"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clarity-principle
extends: []
related:
  - least-mechanism
  - concision-principle
  - maintainability-principle
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should Go code handle complexity?"
  - "When is complexity justified in Go code?"
  - "What does simple Go code look like?"
---

# Quick Definition

Go code should be written in the simplest way that accomplishes its goals in terms of both behavior and performance. Complexity should be added deliberately and only when justified, with accompanying documentation.

# Core Definition

Simplicity is the second-ranked style principle. Simple Go code is easy to read top to bottom, does not assume prior knowledge, avoids unnecessary abstraction, makes value propagation clear, has comments explaining why (not what), has documentation that stands on its own, and produces useful errors and test failures. Complexity is often mutually exclusive with "clever" code. When complexity is needed (e.g., for performance or multiple disparate consumers), it should be added deliberately with documentation so maintainers can understand and navigate it. If code is very complex but its purpose is simple, that signals the implementation should be revisited.

# Prerequisites

- **clarity-principle** -- Clarity is the higher-priority principle that simplicity supports

# Key Properties

1. Easy to read from top to bottom
2. Does not assume the reader already knows what it is doing
3. Does not assume the reader can memorize all preceding code
4. No unnecessary levels of abstraction
5. Names do not call attention to mundane things
6. Value propagation and decisions are clear to the reader
7. Comments explain why, not what
8. Documentation stands on its own
9. Useful errors and useful test failures
10. Often mutually exclusive with "clever" code

# Construction / Recognition

## To Apply:
1. Write code that reads linearly from top to bottom
2. Avoid abstraction layers that do not provide clear benefit
3. Add complexity deliberately -- only for performance or multiple consumers
4. Document the rationale when complexity is necessary
5. Supplement complex code with tests and examples showing correct usage

## To Recognize:
1. Code where the purpose is immediately apparent without deep context
2. Absence of unnecessary abstraction layers
3. Complex code accompanied by documentation explaining why it is complex

# Context & Application

Tradeoffs can arise between code simplicity and API usage simplicity. It may be worthwhile to have more complex internal code so the API is easier to use correctly. Conversely, leaving extra work to the API user may keep the implementation simple and understandable. When complexity does appear in a codebase that strives for simplicity, it signals performance-critical code requiring care, such as preallocating buffers and reusing them throughout a goroutine lifetime.

# Examples

**Example 1 -- Characteristics of simple Go code**:

Simple code reads top to bottom without requiring the reader to jump between functions or hold previous context in memory. It avoids clever tricks in favor of straightforward logic.

**Example 2 -- Justified complexity (from source)**:

Preallocating a buffer and reusing it throughout a goroutine lifetime is a complex pattern. When a maintainer sees this, it signals performance-critical code. This complexity is justified but should be documented so future maintainers understand why it exists and take appropriate care when modifying it.

# Relationships

## Related
- **least-mechanism** -- A sub-principle of simplicity: prefer standard tools over sophisticated machinery
- **concision-principle** -- Concise code removes noise, complementing simplicity
- **maintainability-principle** -- Simple code is easier to maintain correctly

# Common Errors

- **Error**: Adding abstraction layers "just in case" they are needed later
  **Correction**: Add complexity only when justified by current requirements; it is easy to add later but hard to remove

- **Error**: Writing clever one-liners that are hard to understand
  **Correction**: Prefer straightforward code that reads clearly top to bottom, even if it takes more lines

# Common Confusions

- **Confusion**: Thinking simplicity means the code cannot be complex
  **Clarification**: Simplicity means avoiding *unnecessary* complexity. When complexity is justified (performance, multiple consumers), it should be deliberate and documented.

- **Confusion**: Believing simplicity and concision are the same thing
  **Clarification**: Simplicity is about straightforward logic; concision is about signal-to-noise ratio. They are complementary but distinct.

# Source Reference

Chapter 2: Guide, Section "Style principles" > "Simplicity".

# Verification Notes

- Definition source: Directly from the "Simplicity" section of the Style Guide
- Confidence rationale: HIGH -- explicitly defined with a detailed bullet list and discussion
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
