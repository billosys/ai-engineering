---
# === CORE IDENTIFICATION ===
concept: Local Consistency
slug: local-consistency

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
section: "Core guidelines"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "local style"
  - "within-package consistency"
  - "author freedom"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - consistency-principle
extends:
  - consistency-principle
related:
  - go-style-document-hierarchy
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What should I do when the style guide is silent on a point?"
  - "Can I choose my own style for things the guide does not cover?"
  - "When is local consistency not a valid justification?"
---

# Quick Definition

When the style guide has nothing to say about a particular point, authors are free to choose their preferred style, provided nearby code (same file, package, or project) has not already taken a consistent stance. Local consistency is not a valid justification for violating the style guide.

# Core Definition

Where the style guide is silent on a particular style point, authors are free to choose the style they prefer -- unless code in close proximity (usually the same file or package, sometimes the same team or project directory) has already established a consistent stance. Valid local style choices include `%s` vs `%v` for error formatting or buffered channels vs mutexes. Invalid local style choices include line length restrictions or use of assertion-based testing libraries (which the guide addresses). If a local style disagrees with the guide but the impact is limited to one file, it is surfaced in code review and a bug is filed. If a change would worsen an existing deviation, expose it in more API surfaces, or introduce a bug, local consistency is no longer a valid justification.

# Prerequisites

- **consistency-principle** -- Understanding consistency as the tiebreaker principle

# Key Properties

1. Authors are free to choose style where the guide is silent
2. Must follow the stance already taken by nearby code (same file, package, team)
3. Valid local choices: `%s` vs `%v` for errors, buffered channels vs mutexes
4. Invalid local choices: line length restrictions, assertion-based testing libraries
5. Local consistency is not a justification for violating the style guide
6. If a change would worsen an existing deviation, local consistency does not apply

# Construction / Recognition

## To Apply:
1. Check if the style guide addresses the point -- if so, follow the guide
2. If the guide is silent, look at surrounding code for an established convention
3. If no convention exists, choose freely and be consistent going forward
4. Do not use local consistency to justify extending a bad pattern

## To Recognize:
1. Code review comments about style points the guide does not cover
2. Inconsistent approaches to the same problem within a single package
3. Appeals to "local consistency" that actually violate the style guide

# Context & Application

This guideline balances freedom with order. The style guide cannot cover every possible style decision, so authors need latitude. But that latitude is bounded: once nearby code establishes a pattern, follow it for consistency. The critical safeguard is that local consistency never trumps the style guide itself -- if surrounding code is wrong, fix it rather than matching it. This prevents bad patterns from spreading through appeals to consistency.

# Examples

**Example 1 -- Valid local style choice**:

A package consistently uses `%s` for formatting errors. New code in the same package should use `%s` to match, even though `%v` would also be acceptable.

**Example 2 -- Invalid appeal to local consistency**:

A package uses an assertion-based testing library. New code should not follow this pattern because the style guide addresses testing libraries. Instead, file a bug to migrate the existing code.

# Relationships

## Related
- **go-style-document-hierarchy** -- Local consistency operates within the framework of the document hierarchy

## Extends
- **consistency-principle** -- Local consistency is a specific application of the broader consistency principle

# Common Errors

- **Error**: Using local consistency to justify extending a pattern that violates the style guide
  **Correction**: If the existing pattern violates the guide, clean it up rather than matching it

- **Error**: Ignoring established local conventions when the guide is silent
  **Correction**: Check surrounding code before introducing a different style

# Common Confusions

- **Confusion**: Thinking local consistency means "do whatever the file does"
  **Clarification**: Local consistency only applies to points the style guide is silent on. If the guide has a rule, follow it regardless of local practice.

- **Confusion**: Believing all local style decisions are valid
  **Clarification**: Some decisions (like line length restrictions or testing library choices) are addressed by the guide and are not valid local style choices.

# Source Reference

Chapter 2: Guide, Section "Core guidelines" > "Local consistency".

# Verification Notes

- Definition source: Directly from the "Local consistency" section of Core guidelines
- Confidence rationale: HIGH -- explicit guidance with valid and invalid examples
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
