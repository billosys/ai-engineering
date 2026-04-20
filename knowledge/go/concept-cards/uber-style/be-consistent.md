---
# === CORE IDENTIFICATION ===
concept: Be Consistent
slug: be-consistent

# === CLASSIFICATION ===
category: style
subcategory: principles
tier: foundational

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton (and Uber Go team)"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "Be Consistent"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "consistency principle"
  - "codebase consistency"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - avoid-overly-long-lines
  - group-similar-declarations
  - use-field-tags-in-marshaled-structs
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the most important style principle in the Uber Go style guide?"
  - "Why is consistency more important than any single style rule?"
  - "At what level should style changes be applied?"
---

# Quick Definition

Consistency is the overriding style principle. Above all else, be consistent. Consistent code is easier to maintain, rationalize, and migrate. Style changes should be applied at a package level or larger, never at the sub-package level.

# Core Definition

The Uber Go Style Guide acknowledges that some guidelines can be evaluated objectively while others are situational, contextual, or subjective. Regardless of the specific rule, **consistency** is the most important principle.

Consistent code:
- Is easier to maintain
- Is easier to rationalize
- Requires less cognitive overhead
- Is easier to migrate or update as new conventions emerge or bugs are fixed

Conversely, having multiple disparate or conflicting styles within a single codebase causes maintenance overhead, uncertainty, and cognitive dissonance, all of which directly contribute to lower velocity, painful code reviews, and bugs.

When applying style guidelines to a codebase, changes should be made at a **package level or larger**. Applying changes at a sub-package level violates the consistency concern by introducing multiple styles into the same code.

# Prerequisites

No prerequisites. This is the foundational meta-principle that governs all other style decisions.

# Key Properties

1. **Overriding principle** -- "Above all else, be consistent" -- consistency takes priority over any individual style rule.
2. **Package-level adoption** -- Style changes should be applied at the package level or larger, not at the sub-package or file level.
3. **Reduces cognitive overhead** -- Developers reading consistent code can focus on logic rather than adapting to varying conventions.
4. **Enables migration** -- Consistent code is easier to update when conventions change, because patterns are uniform and predictable.

# Construction / Recognition

## To Construct/Create:
1. When introducing a style convention, apply it across the entire package or module.
2. When modifying existing code, follow the conventions already established in that package.
3. Avoid mixing old and new styles within the same package.

## To Identify/Recognize:
1. Inconsistent formatting, naming, or patterns within a single package indicate a consistency violation.
2. Pull requests that apply style changes to only part of a package may create inconsistency.

# Context & Application

- **Typical contexts**: Code reviews, style guide adoption, refactoring initiatives, onboarding new team members.
- **Common applications**: Deciding whether to apply a new convention retroactively, resolving style disagreements, evaluating the scope of a refactoring change.

# Examples

No specific code examples are provided in the source for this section. The guidance is stated as a principle: consistency is more important than any individual style preference.

# Relationships

- **Related to** `avoid-overly-long-lines`: Line length conventions should be applied consistently.
- **Related to** `group-similar-declarations`: Grouping conventions should be applied consistently throughout a package.
- **Related to** `use-field-tags-in-marshaled-structs`: Tag conventions should be applied consistently to all marshaled structs.

# Common Errors

1. **Partial adoption** -- Applying a new style rule to some files in a package but not others creates inconsistency worse than not adopting the rule at all.
2. **Style churn** -- Repeatedly changing style conventions without applying them broadly leads to a patchwork of different styles.

# Common Confusions

1. **"Consistent" does not mean "never change"** -- Consistency means applying changes uniformly. When a better convention emerges, adopt it across the codebase at the package level or larger.
2. **Consistency vs. correctness** -- If existing code has a genuine bug or anti-pattern, fixing it takes priority over being consistent with the broken pattern.

# Source Reference

- Source: "Uber Go Style Guide"
- Chapter: "Style" (Ch 4)
- Section: "Be Consistent"

# Verification Notes

- Extraction confidence: high -- Explicitly defined section with clear statement of the consistency principle as the overriding concern.
