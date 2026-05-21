---
concept: Move Stuff To Independent Applications
slug: move-code-to-independent-applications
category: applications-releases
subcategory: suggestions
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Suggestions & Great Ideas"
chapter_number: null
pdf_page: null
section: "Move stuff to independent applications"
extraction_confidence: high
aliases:
  - "independent applications"
  - "extract to separate application"
prerequisites: []
extends: []
related:
  - no-god-modules
  - group-modules-in-subdirectories
  - facade-pattern-for-libraries
contrasts_with: []
answers_questions:
  - "When should I extract code into a separate Erlang application?"
---

# Quick Definition

When a block of functionality is self-contained and independent of your application's main purpose, move it into a separate application — and consider open-sourcing it.

# Core Definition

"When you identify a block of functionality that is self-contained (it may be several modules or just a big one) and actually independent of the main purpose of your application, place that in a separate application. And consider open-sourcing it" (Inaka, "Move stuff to independent applications").

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The candidate functionality is self-contained and independent of the app's core purpose.
2. It may be several modules or one large one.
3. Extracting it into its own application makes it shareable across apps.
4. This is a "Suggestion & Great Idea" — advisory, not a PR-blocking rule.

# Construction / Recognition

## To Apply

1. Identify a cohesive, independent block of functionality.
2. Move it into its own OTP application; depend on that application.
3. Consider open-sourcing it if it is genuinely reusable.

## To Recognize a Candidate

1. A cluster of modules has no real dependence on the host application's purpose.

# Context & Application

A "Suggestion & Great Idea" — advisory; does not by itself block a PR.

- **Typical contexts**: utility layers, protocol clients, generic infrastructure embedded in a product.
- **Common applications**: extracting a reusable library application from a product codebase.

# Examples

The source provides no code example for this guideline; it adds a note instead (see Common Confusions).

# Relationships

## Related

- **No God modules** — the same decomposition instinct, applied at the application level.
- **Group modules in subdirectories by functionality** — a lighter-weight grouping that precedes full extraction.
- **Use the facade pattern on libraries** — an extracted library benefits from a facade.

# Common Errors

- **Error**: Leaving independent, reusable functionality entangled in the product application.
  **Correction**: Extract it into its own application.

# Common Confusions

- **Confusion**: Extracting *anything* into a library.
  **Clarification**: The source warns explicitly — do *not* create highly specific libraries too coupled to the current project; reserve extraction for genuinely reusable functionality.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Suggestions & Great Ideas", guideline "Move stuff to independent applications".

# Verification Notes

- Definition source: Direct quote plus the source's cautionary note.
- Confidence rationale: HIGH — explicit suggestion; no code example exists (noted above).
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
