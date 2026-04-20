---
# === CORE IDENTIFICATION ===
concept: Consistency Principle
slug: consistency-principle

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
  - "code consistency"
  - "stylistic consistency"
  - "consistent Go code"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clarity-principle
extends: []
related:
  - local-consistency
  - gofmt-formatting
  - maintainability-principle
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How important is consistency relative to other style principles?"
  - "When should consistency override other considerations?"
  - "At what level should consistency be maintained?"
---

# Quick Definition

Consistent code looks, feels, and behaves like similar code throughout the broader codebase. Consistency does not override the other four principles (clarity, simplicity, concision, maintainability) but serves as a tiebreaker when they do not resolve a decision.

# Core Definition

Consistency is the fifth-ranked style principle. Consistent code looks, feels, and behaves like similar code across the broader codebase, within a team or package, and within a single file. Consistency concerns do not override any of the higher-ranked principles (clarity, simplicity, concision, maintainability), but when a tie must be broken, it is often beneficial to break it in favor of consistency. Package-level consistency is often the most immediately important level -- approaching the same problem in multiple ways within a package or using many names for the same concept within a file is jarring. However, even package-level consistency should not override documented style principles or global consistency.

# Prerequisites

- **clarity-principle** -- Understanding the principle hierarchy: clarity > simplicity > concision > maintainability > consistency

# Key Properties

1. Ranked fifth among five style principles -- a tiebreaker, not a trump card
2. Operates at multiple levels: codebase, team/package, file
3. Does not override clarity, simplicity, concision, or maintainability
4. Package-level consistency is often the most immediately important
5. Same problem should not be approached in multiple ways within a package
6. Same concept should not have many names within a file

# Construction / Recognition

## To Apply:
1. Follow existing patterns within the package when solving a similar problem
2. Use consistent names for the same concept throughout a file
3. When the style guide is silent and other principles tie, choose the approach consistent with surrounding code
4. Do not use consistency as a reason to violate higher-priority principles

## To Recognize:
1. Multiple approaches to the same problem within a single package
2. Different names for the same concept within a file
3. Code that follows local conventions but violates the broader style guide

# Context & Application

Consistency is the "tiebreaker" principle. When two approaches are equally clear, simple, concise, and maintainable, pick the one that matches surrounding code. This reduces cognitive load because readers can reuse patterns they have already learned. However, consistency should never be used to justify continuing a bad pattern -- if the surrounding code violates higher-priority principles, fix it rather than matching it.

# Examples

**Example 1 -- Package-level consistency**:

If a package consistently handles errors with early returns, a new function in that package should follow the same pattern rather than introducing nested if-else chains, even if both approaches are equally valid in isolation.

**Example 2 -- Consistency as tiebreaker**:

When choosing between `%s` and `%v` for printing errors (both valid), use whichever the surrounding code uses consistently.

# Relationships

## Related
- **local-consistency** -- Expands on what to do when the style guide is silent
- **gofmt-formatting** -- Gofmt enforces mechanical consistency in formatting
- **maintainability-principle** -- Consistent code is easier to maintain

# Common Errors

- **Error**: Using consistency to justify perpetuating a bad pattern
  **Correction**: Consistency does not override the four higher-priority principles. Fix bad patterns rather than matching them.

- **Error**: Prioritizing global consistency over local clarity
  **Correction**: Package-level consistency is often most immediately important, but neither should override documented style principles.

# Common Confusions

- **Confusion**: Thinking consistency is the most important style principle
  **Clarification**: Consistency is ranked last among the five principles. It is a tiebreaker, not a trump card.

- **Confusion**: Believing all code must look identical across the entire codebase
  **Clarification**: Consistency operates at multiple levels (file, package, codebase). Package-level consistency is often more important than codebase-wide uniformity.

# Source Reference

Chapter 2: Guide, Section "Style principles" > "Consistency".

# Verification Notes

- Definition source: Directly from the "Consistency" section of the Style Guide
- Confidence rationale: HIGH -- explicitly defined with clear ranking and scope
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
