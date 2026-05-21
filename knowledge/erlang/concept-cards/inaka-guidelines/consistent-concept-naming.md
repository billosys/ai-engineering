---
concept: Be Consistent When Naming Concepts
slug: consistent-concept-naming
category: core-idioms
subcategory: naming
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Naming"
chapter_number: null
pdf_page: null
section: "Be consistent when naming concepts"
extraction_confidence: high
aliases:
  - "consistent naming"
  - "same name for the same concept"
prerequisites: []
extends: []
related:
  - variable-name-format
  - short-meaningful-variable-names
contrasts_with: []
answers_questions:
  - "Why should the same concept use the same variable name everywhere?"
---

# Quick Definition

Use the same variable name for the same concept everywhere — even across different modules.

# Core Definition

"Use the same variable name for the same concept everywhere (even in different modules)" (Inaka, "Be consistent when naming concepts"). A concept like a user id is referred to by one canonical name (`UserId`), not a different name in every function (`User_Id`, `Usr`).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. One concept maps to one variable name, project-wide.
2. The same name is used even when the concept crosses module boundaries.
3. Consistent naming makes the concept greppable.
4. It is a PR-rejection rule under Naming.

# Construction / Recognition

## To Apply

1. Pick a canonical name for each domain concept (e.g., `OrgID`).
2. Use that exact name in every function and module that handles the concept.

## To Recognize a Violation

1. The same value is called `UserId` in one function and `Usr` in the next.

# Context & Application

A PR-blocking convention under Naming.

- **Typical contexts**: ids and tokens threaded through call chains.
- **Common applications**: keeping `UserId` identical across `good/1`, `internal_good/1`, `internal_good2/1`.

# Examples

**Example 1** — bad: a value passes through `bad/1`, `internal_bad/1`, `internal_bad2/1` as `UserId`, then `User_Id`, then `Usr`.

**Example 2** — good: the same value stays `UserId` through every helper.

# Relationships

## Related

- **Variable Names** — consistent naming and the CamelCase format rule reinforce each other.
- **Prefer shorter (but still meaningful) variable names** — both shape variable-naming discipline.

# Common Errors

- **Error**: Renaming a value as it passes through internal helpers.
  **Correction**: Keep the canonical name; thread it unchanged.

# Common Confusions

- **Confusion**: Believing internal/private functions can name things freely.
  **Clarification**: Consistency aids grep-driven refactoring everywhere, including private functions and other modules.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Naming", guideline "Be consistent when naming concepts".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
