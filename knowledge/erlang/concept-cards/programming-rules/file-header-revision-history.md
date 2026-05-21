---
concept: File Headers, Revision History
slug: file-header-revision-history
category: documentation
subcategory: documenting-code
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Documenting Code"
chapter_number: 8
pdf_page: null
section: "8.9 File headers, revision history"
extraction_confidence: high
aliases:
  - "revision history"
  - "file header revision history"
prerequisites: []
extends: []
related:
  - file-header-copyright
  - attribute-code
  - remove-old-code
contrasts_with: []
answers_questions:
  - "What revision information should a source file's header contain?"
---

# Quick Definition

Every source file must carry a revision history showing who worked on it and what they did.

# Core Definition

"Each file of source code must be documented with its revision history which shows who has been working with the files and what they have done to it" (Programming Rules, 8.9). The example shows `%%%`-bordered revision entries, each with a revision label, date, author, and a description of the changes made.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Every source file documents its revision history in the header.
2. Each entry records who worked on the file and what they did.
3. Entries carry a revision label, date, author, and change description.

# Construction / Recognition

## To Apply

1. Maintain a `%%%` revision-history block in the file header.
2. Add an entry — label, date, author, description — for each change.

## To Recognize a Violation

1. A file has no revision history, or entries omit author or change description.

# Context & Application

A core documentation rule (section 8).

- **Typical contexts**: the file header, after the copyright block.
- **Common applications**: a `%%% Revision History` block with dated, attributed entries.

# Examples

**Example** (from source): two `%%%` revision entries — "Rev PA1 ... Author Fred Bloggs ..." and "Rev A ... Author Johanna Johansson ..." — each describing the changes made.

# Relationships

## Related

- **File headers, copyright** — the preceding file-header element.
- **Attribute code** — revision history is part of recording authorship.
- **Do not comment out old code - remove it** — removed code is noted in the revision history.

# Common Errors

- **Error**: Editing a file without adding a revision-history entry.
  **Correction**: Record the change — label, date, author, description.

# Common Confusions

- **Confusion**: Thinking a version-control log makes the in-file history redundant.
  **Clarification**: The source (written in 2000) requires the in-file revision history regardless.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 8.9 "File headers, revision history".

# Verification Notes

- Definition source: Direct adaptation of section 8.9.
- Confidence rationale: HIGH — the rule is stated explicitly with an example block.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
