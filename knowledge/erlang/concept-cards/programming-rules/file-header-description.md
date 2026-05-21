---
concept: File Header, Description
slug: file-header-description
category: documentation
subcategory: documenting-code
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Documenting Code"
chapter_number: 8
pdf_page: null
section: "8.10 File Header, description"
extraction_confidence: high
aliases:
  - "file header description"
  - "module description header"
prerequisites: []
extends: []
related:
  - file-header-copyright
  - comment-conventions
  - comment-each-function
contrasts_with: []
answers_questions:
  - "What module-level description should a file header contain?"
  - "Should known bugs and weaknesses be documented?"
---

# Quick Definition

Each file must begin with a short description of its module and a brief description of all exported functions — and known weaknesses should be noted, not hidden.

# Core Definition

"Each file must start with a short description of the module contained in the file and a brief description of all exported functions" (Programming Rules, 8.10), written as a `%%%` header block. If you know of any weakness, bug, or badly tested feature, make a note of it in a special comment — don't hide it. Note any incomplete part, and add comments helpful to future maintainers, who may improve the module years later.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The file header includes a short description of the module.
2. It briefly describes every exported function.
3. Known weaknesses, bugs, and badly tested features are noted, not hidden.
4. Incomplete parts and maintainer-helpful notes are added.

# Construction / Recognition

## To Apply

1. Write a `%%%` header block describing the module and listing its exported functions.
2. Add explicit notes for any known weakness, bug, or incomplete part.

## To Recognize a Violation

1. A file has no module-description header, or hides known bugs.

# Context & Application

A core documentation rule (section 8).

- **Typical contexts**: the file header, after copyright and revision history.
- **Common applications**: a `%%% Description module foobar_data_manipulation` block listing exports.

# Examples

**Example** (from source): a `%%% Description module foobar_data_manipulation` header with an `%%% Exports` section briefly describing functions such as `create_foobar(Parent, Type)`.

# Relationships

## Related

- **File headers, copyright** — the preceding file-header element.
- **Comments** — the header uses `%%%` module-level comments.
- **Comment each function** — the header's per-export descriptions complement full function comments.

# Common Errors

- **Error**: Hiding a known bug or weakness instead of noting it.
  **Correction**: Record it in a special comment for future maintainers.

# Common Confusions

- **Confusion**: Thinking noting bugs looks unprofessional.
  **Clarification**: The source explicitly says don't hide them — honest notes help whoever maintains the module later.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 8.10 "File Header, description".

# Verification Notes

- Definition source: Direct adaptation of section 8.10.
- Confidence rationale: HIGH — the rule is stated explicitly with an example block.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
