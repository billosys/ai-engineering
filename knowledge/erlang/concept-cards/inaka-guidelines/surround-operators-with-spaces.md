---
concept: Surround Operators With Spaces
slug: surround-operators-with-spaces
category: core-idioms
subcategory: source-code-layout
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Source Code Layout"
chapter_number: null
pdf_page: null
section: "Use your spacebar"
extraction_confidence: high
aliases:
  - "use your spacebar"
  - "spaces around operators"
  - "spaces after commas"
prerequisites: []
extends: []
related:
  - spaces-over-tabs
  - no-trailing-whitespace
contrasts_with: []
answers_questions:
  - "Should operators and commas have spaces around them in Erlang?"
  - "How do I make Erlang code easier to read?"
---

# Quick Definition

Surround operators and commas with spaces so code is easier to scan and read.

# Core Definition

"Surround operators and commas with spaces" (Inaka, "Use your spacebar"). Binary operators, `->`, and the commas separating arguments and list elements each get whitespace around (or after) them, producing visually separated tokens.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Operators are padded with a space on each side.
2. Commas are followed by a space.
3. The function arrow `->` is surrounded by spaces.
4. It is a PR-rejection rule under Source Code Layout.

# Construction / Recognition

## To Apply

1. Write `A + B`, not `A+B`; `[is, 'not', working]`, not `[is,'not',working]`.
2. Write `good(_Hey, _Now, _It) ->`, not `good(_My,_Space,_Bar)->`.

## To Recognize a Violation

1. Two tokens abut with no separating whitespace around an operator or after a comma.

# Context & Application

A PR-blocking convention applied to every expression.

- **Typical contexts**: function heads, argument lists, list literals, arithmetic and comparison expressions.
- **Common applications**: enforced automatically by `erlfmt`.

# Examples

**Example 1** — bad: `bad(_My,_Space,_Bar)->[is,'not',working].` — no spaces anywhere.

**Example 2** — good: `good(_Hey, _Now, _It) -> ["works " ++ "again, " | [hooray]].`

# Relationships

## Related

- **Spaces over tabs** — companion whitespace rule for indentation.
- **No trailing whitespace** — companion whitespace-hygiene rule.

# Common Errors

- **Error**: Omitting the space before `->` in a function clause head.
  **Correction**: Always pad `->` with spaces.

# Common Confusions

- **Confusion**: Treating this as cosmetic only.
  **Clarification**: The source's rationale is concrete — spacing produces "cleaner code that's easier to find / read."

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Source Code Layout", guideline "Use your spacebar".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example pair.
- Uncertainties: None.
- Cross-reference status: related slugs are planned cards in this extraction.
