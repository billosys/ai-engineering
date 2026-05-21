---
concept: 100-Column Line Limit
slug: 100-column-line-limit
category: core-idioms
subcategory: source-code-layout
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Source Code Layout"
chapter_number: null
pdf_page: null
section: "100 column per line"
extraction_confidence: high
aliases:
  - "100 chars per line"
  - "line length limit"
  - "column width"
prerequisites: []
extends: []
related:
  - spaces-over-tabs
  - short-meaningful-variable-names
  - keep-functions-small
contrasts_with: []
answers_questions:
  - "How long can a line of Erlang code be?"
  - "Why is there a maximum line width?"
---

# Quick Definition

Keep each source line to a maximum of 100 characters.

# Core Definition

"Stick to 100 chars per line, maximum" (Inaka, "100 column per line"). Lines wider than 100 characters must be broken across multiple lines.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The hard maximum is 100 characters per line.
2. Lines that exceed it are wrapped at meaningful points (e.g., one record pattern per line).
3. It is a PR-rejection rule under Source Code Layout.
4. The limit permits two files side by side on a laptop, three on a 1080p display.

# Construction / Recognition

## To Apply

1. Set an editor ruler/guide at column 100.
2. When a clause head or expression exceeds the limit, extract bindings or split the expression.

## To Recognize a Violation

1. Code extends past the column-100 guide.

# Context & Application

A PR-blocking convention applied to every line.

- **Typical contexts**: long function heads, deeply parameterized calls, wide record patterns.
- **Common applications**: refactoring a wide clause head into intermediate `=` bindings.

# Examples

**Example 1** — bad: a `bad/2` clause whose head inlines two full `#rec{...}` patterns, pushing the line well past 100 characters.

**Example 2** — good: `good/2` binds `Foo` and `Bar` to record patterns on separate lines, keeping every line under 100 characters.

# Relationships

## Related

- **Spaces over tabs** — 2-space indentation conserves columns toward this budget.
- **Short, meaningful variable names** — shorter names help fit the limit.
- **Keep functions small** — smaller functions tend to have shorter lines.

# Common Errors

- **Error**: Inlining multiple record patterns in one clause head.
  **Correction**: Bind each record to a variable on its own line, then destructure.

# Common Confusions

- **Confusion**: Assuming the classic 80-column limit applies.
  **Clarification**: This guideline sets the limit at 100, not 80.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Source Code Layout", guideline "100 column per line".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit numeric rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: related slugs are planned cards in this extraction.
