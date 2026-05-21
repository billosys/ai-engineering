---
concept: No Trailing Whitespace
slug: no-trailing-whitespace
category: core-idioms
subcategory: source-code-layout
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Source Code Layout"
chapter_number: null
pdf_page: null
section: "No Trailing Whitespace"
extraction_confidence: high
aliases:
  - "trailing whitespace"
  - "no trailing spaces"
prerequisites: []
extends: []
related:
  - surround-operators-with-spaces
  - spaces-over-tabs
contrasts_with: []
answers_questions:
  - "Why should I remove trailing whitespace from Erlang source?"
---

# Quick Definition

Remove trailing whitespace from the ends of source lines.

# Core Definition

"Remove trailing whitespaces from your lines" (Inaka, "No Trailing Whitespace"). No line ends with space or tab characters after its last non-whitespace token.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Source lines end immediately after their last meaningful character.
2. It applies to blank lines too — they contain no spaces.
3. It is a PR-rejection rule under Source Code Layout.
4. The motivation is reduction of "commit noise" in version control diffs.

# Construction / Recognition

## To Apply

1. Enable "trim trailing whitespace on save" in your editor.
2. Optionally enforce with a pre-commit hook or `erlfmt`.

## To Recognize a Violation

1. `git diff` shows whitespace-only changes, or a diff highlights red trailing space markers.

# Context & Application

A PR-blocking convention applied to every line of every file.

- **Typical contexts**: all source files; especially noticeable in code review diffs.
- **Common applications**: editor configuration; CI whitespace linting.

# Examples

**Example 1** — bad: `bad() -> "this line has trailing whitespace".` followed by stray spaces.

**Example 2** — good: `good() -> "this line has not".` with a clean line ending.

# Relationships

## Related

- **Surround operators with spaces** — companion whitespace-formatting rule.
- **Spaces over tabs** — companion whitespace rule.

# Common Errors

- **Error**: Leaving whitespace on otherwise-blank lines between functions.
  **Correction**: Trim all lines, including blank ones.

# Common Confusions

- **Confusion**: Thinking trailing whitespace is harmless because it is invisible.
  **Clarification**: It is invisible *in code* but very visible *in diffs*, where it adds review noise.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Source Code Layout", guideline "No Trailing Whitespace". The source links a StackExchange discussion on why trailing whitespace matters.

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with a bad/good example.
- Uncertainties: None.
- Cross-reference status: related slugs are planned cards in this extraction.
