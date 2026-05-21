---
concept: Avoid Boolean Parameters
slug: avoid-boolean-parameters
category: api-design
subcategory: naming
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Naming"
chapter_number: null
pdf_page: null
section: "Avoid boolean parameters"
extraction_confidence: high
aliases:
  - "boolean parameters"
  - "boolean blindness"
  - "flag arguments"
prerequisites: []
extends: []
related:
  - prefer-pattern-matching-over-equality
  - tagged-tuple-messages
contrasts_with: []
answers_questions:
  - "Why should I avoid boolean parameters in Erlang functions?"
  - "What distinguishes a boolean parameter from a descriptive-atom parameter?"
---

# Quick Definition

Don't pass `true`/`false` to control which function clause is selected; use descriptive atoms instead.

# Core Definition

"Don't use boolean parameters (i.e. `true` and `false`) to control clause selection" (Inaka, "Avoid boolean parameters"). A bare boolean forces the reader to consult the function definition to learn what it means; a descriptive atom (`full`, `empty`) states the intent at the call site.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Clause selection is not driven by `true`/`false` arguments.
2. Descriptive atoms replace booleans at decision points.
3. The atom makes the caller's intent self-documenting.
4. It is a PR-rejection rule under Naming.

# Construction / Recognition

## To Apply

1. Replace a boolean flag argument with an atom that names the alternative (e.g., `full` vs `empty`).
2. Update the matching function clauses to pattern-match those atoms.

## To Recognize a Violation

1. A function is called with a literal `true` or `false` whose meaning is not obvious.

# Context & Application

A PR-blocking convention under Naming.

- **Typical contexts**: helper functions with a mode/flag parameter.
- **Common applications**: `draw_square(EdgeLength, full)` instead of `draw_square(EdgeLength, true)`.

# Examples

**Example 1** — bad: `bad_draw_square(EdgeLength, true)` / `bad_draw_square(EdgeLength, false)`.

**Example 2** — good: `good_draw_square(EdgeLength, full)` / `good_draw_square(EdgeLength, empty)`.

# Relationships

## Related

- **Prefer pattern-matching over testing for equality** — both prefer meaningful matching over boolean logic.
- **Use atoms or tagged tuples for messages** — same preference for human-readable atoms over opaque values.

# Common Errors

- **Error**: Adding a `true`/`false` flag parameter to toggle behavior.
  **Correction**: Use two named atoms so the call site reads clearly.

# Common Confusions

- **Confusion**: Thinking a boolean is fine because the function only has two modes.
  **Clarification**: Even two modes deserve names; the cost is reader effort, not arity.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Naming", guideline "Avoid boolean parameters".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
