---
concept: Format Programs In A Consistent Manner
slug: consistent-formatting
category: core-idioms
subcategory: lexical-stylistic-conventions
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Specific Lexical and Stylistic Conventions"
chapter_number: 7
pdf_page: null
section: "7.8 Format programs in a consistent manner"
extraction_confidence: high
aliases:
  - "consistent formatting"
  - "consistent programming style"
prerequisites: []
extends: []
related:
  - principle-of-least-astonishment
  - dont-write-long-lines
contrasts_with: []
answers_questions:
  - "Why should programs be formatted consistently?"
---

# Quick Definition

Format programs consistently — adopt a style and stick to it, and use the same style across an entire project.

# Core Definition

"A consistent programming style will help you, and other people, to understand your code" (Programming Rules, 7.8). Different people have different styles for indentation, spacing, etc.; for example, one might write `{12,23,45}` and another `{12, 23, 45}`. "Once you have adopted style — stick to it." Within a larger project, the same style should be used in all parts.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A consistent style aids comprehension for the author and for others.
2. Once a style is adopted, it is kept.
3. Within a larger project, one style is used across all parts.
4. The *choice* of style (e.g. comma spacing) matters less than its consistency.

# Construction / Recognition

## To Apply

1. Adopt a formatting style and apply it uniformly.
2. Use one project-wide style across all modules.

## To Recognize a Violation

1. Formatting style varies within a file or across a project.

# Context & Application

A core lexical/stylistic convention (section 7).

- **Typical contexts**: every module; project-wide style.
- **Common applications**: agreeing on indentation and spacing conventions for a project.

# Examples

**Example** (from source): tuples written `{12,23,45}` (no space) versus `{12, 23, 45}` (comma + blank) — either is acceptable, but the chosen style must be kept.

# Relationships

## Related

- **Use the principle of "least astonishment"** — consistent style is part of a predictable system.
- **Don't write very long lines** — line length is one element of consistent formatting.

# Common Errors

- **Error**: Mixing formatting styles within a file or project.
  **Correction**: Pick one style and apply it everywhere.

# Common Confusions

- **Confusion**: Debating which formatting style is "correct".
  **Clarification**: The source's point is consistency — adopt one and stick to it project-wide.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 7.8 "Format programs in a consistent manner".

# Verification Notes

- Definition source: Direct adaptation of section 7.8.
- Confidence rationale: HIGH — the rule is stated explicitly with an example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
