---
concept: File Headers, Copyright
slug: file-header-copyright
category: documentation
subcategory: documenting-code
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Documenting Code"
chapter_number: 8
pdf_page: null
section: "8.8 File headers, copyright"
extraction_confidence: high
aliases:
  - "file header copyright"
  - "copyright notice"
prerequisites: []
extends: []
related:
  - file-header-revision-history
  - file-header-description
contrasts_with: []
answers_questions:
  - "What copyright information should a source file start with?"
---

# Quick Definition

Every source file must start with copyright information.

# Core Definition

"Each file of source code must start with copyright information" (Programming Rules, 8.8). The source gives an example `%%%`-commented copyright block — naming the copyright holder and year and stating the reservation of rights.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Every source file begins with a copyright notice.
2. The notice is written as a `%%%` module-level comment block.
3. It names the copyright holder and year and states the rights reserved.

# Construction / Recognition

## To Apply

1. Begin each file with a `%%%` copyright comment block.

## To Recognize a Violation

1. A source file has no copyright header.

# Context & Application

A core documentation rule (section 8).

- **Typical contexts**: the top of every source file.
- **Common applications**: a boxed `%%%` copyright block.

# Examples

**Example** (from source): a `%%%`-bordered block reading "Copyright Ericsson Telecom AB 1996 / All rights reserved..." at the start of the file.

# Relationships

## Related

- **File headers, revision history** — the next element of the file header.
- **File Header, description** — the file header's module-description element.

# Common Errors

- **Error**: Starting a source file straight into code with no copyright header.
  **Correction**: Begin with the `%%%` copyright block.

# Common Confusions

- **Confusion**: Thinking copyright headers are optional boilerplate.
  **Clarification**: The source states each file *must* start with copyright information.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 8.8 "File headers, copyright".

# Verification Notes

- Definition source: Direct adaptation of section 8.8.
- Confidence rationale: HIGH — the rule is stated explicitly with an example block.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
