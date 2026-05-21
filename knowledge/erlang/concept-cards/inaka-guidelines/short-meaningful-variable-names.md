---
concept: Prefer Shorter (But Still Meaningful) Variable Names
slug: short-meaningful-variable-names
category: core-idioms
subcategory: suggestions
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Suggestions & Great Ideas"
chapter_number: null
pdf_page: null
section: "Prefer shorter (but still meaningful) variable names"
extraction_confidence: high
aliases:
  - "short variable names"
  - "concise variable names"
prerequisites: []
extends: []
related:
  - variable-name-format
  - consistent-concept-naming
  - 100-column-line-limit
contrasts_with: []
answers_questions:
  - "How long should Erlang variable names be?"
---

# Quick Definition

Keep variable names short — as long as they remain easy to read and understand.

# Core Definition

"As long as it's easy to read and understand, keep variable names short" (Inaka, "Prefer shorter (but still meaningful) variable names"). Brevity is favored, but never at the cost of meaning — `OrgToken` over `OrganizationToken`, not a cryptic abbreviation.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Shorter variable names are preferred when still clearly meaningful.
2. Meaning is the hard constraint; brevity is the optimization.
3. Shorter names help keep lines within the column limit.
4. This is a "Suggestion & Great Idea" — advisory, not a PR-blocking rule.

# Construction / Recognition

## To Apply

1. Choose the shortest name that still conveys the concept (`OrgToken`, `OrgID`).

## To Recognize a Candidate

1. A variable name is long-winded where a shorter, equally clear name exists (`OrganizationToken` → `OrgToken`).

# Context & Application

A "Suggestion & Great Idea" — advisory; does not by itself block a PR.

- **Typical contexts**: local bindings in functions.
- **Common applications**: `OrgToken`/`OrgID` instead of `OrganizationToken`/`OID`.

# Examples

**Example 1** — bad: `bad(OrganizationToken) -> OID = organization:get_id(OrganizationToken), OID.`

**Example 2** — good: `good(OrgToken) -> OrgID = organization:get_id(OrgToken), OrgID.`

# Relationships

## Related

- **Variable Names** — the format rule this suggestion refines.
- **Be consistent when naming concepts** — the chosen short name must still be used consistently.
- **100 column per line** — shorter names help fit the line-length limit.

# Common Errors

- **Error**: Shortening `OrganizationToken` to a cryptic `OID`.
  **Correction**: Pick a name that is both short *and* meaningful (`OrgID`).

# Common Confusions

- **Confusion**: Reading "shorter" as "abbreviate aggressively."
  **Clarification**: The qualifier "but still meaningful" is the point — readability bounds brevity.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Suggestions & Great Ideas", guideline "Prefer shorter (but still meaningful) variable names".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit suggestion with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
