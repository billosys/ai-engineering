---
concept: Spaces Over Tabs
slug: spaces-over-tabs
category: core-idioms
subcategory: source-code-layout
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Source Code Layout"
chapter_number: null
pdf_page: null
section: "Spaces over tabs"
extraction_confidence: high
aliases:
  - "2-space indentation"
  - "no tabs"
  - "indentation width"
prerequisites: []
extends: []
related:
  - surround-operators-with-spaces
  - avoid-deep-nesting
contrasts_with: []
answers_questions:
  - "How should Erlang code be indented?"
  - "Should I use tabs or spaces in Erlang?"
---

# Quick Definition

Indent Erlang code with spaces, not tabs, using 2 spaces per indentation level.

# Core Definition

"Spaces over tabs, 2 space indentation" (Inaka, "Spaces over tabs"). Indentation is expressed exclusively with space characters, and each nesting level adds exactly two of them. The rule is explicitly *not* a license to nest deeply — two spaces suffice because clean code stays shallow.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Tabs are disallowed for indentation.
2. One indentation level equals exactly 2 spaces.
3. Consistency matters: 4-space indentation is "better" than mixed, but still wrong.
4. The narrow indent leaves more room within the 100-column line limit.

# Construction / Recognition

## To Apply

1. Configure your editor to insert 2 spaces on Tab and to never emit tab characters.
2. Indent each nested block (clause body, `case`, `receive`, `try`) by 2 more spaces than its parent.

## To Recognize a Violation

1. A literal tab character appears in source indentation.
2. Indentation steps by 4 (or an inconsistent amount) instead of 2.

# Context & Application

A PR-blocking convention applied to every source file.

- **Typical contexts**: all `.erl`/`.hrl` files.
- **Common applications**: editor/formatter configuration; `erlfmt` defaults align with this.

# Examples

**Example 1** — bad: a module mixes 2-space and 4-space indentation across `try`/`catch` clauses.

**Example 2** — "better": consistent 4-space indentation — consistent, but still not the rule.

**Example 3** — good: a `case` expression whose clauses are indented exactly 2 spaces.

# Relationships

## Related

- **Surround operators with spaces** — a companion whitespace-formatting rule.
- **Avoid deep nesting** — the 2-space rule is explicitly justified by *not* encouraging deep nesting.

# Common Errors

- **Error**: Letting an editor insert hard tabs.
  **Correction**: Set "insert spaces for tab" and a tab width of 2.

# Common Confusions

- **Confusion**: Thinking 2-space indentation exists to permit many nesting levels.
  **Clarification**: The source states the opposite — it keeps code concise, not deeper.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Source Code Layout", guideline "Spaces over tabs".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with three contrasting examples.
- Uncertainties: None.
- Cross-reference status: related slugs are planned cards in this extraction.
