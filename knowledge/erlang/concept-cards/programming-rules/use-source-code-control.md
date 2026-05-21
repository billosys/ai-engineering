---
concept: Use A Source Code Control System
slug: use-source-code-control
category: tooling
subcategory: documenting-code
tier: foundational
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Documenting Code"
chapter_number: 8
pdf_page: null
section: "8.12 Use a source code control system"
extraction_confidence: high
aliases:
  - "source code control"
  - "version control"
prerequisites: []
extends: []
related:
  - remove-old-code
  - file-header-revision-history
contrasts_with: []
answers_questions:
  - "Should a project use a source code control system?"
---

# Quick Definition

All non-trivial projects must use a source code control system to keep track of all modules.

# Core Definition

"All non trivial projects must use a source code control system such as RCS, CVS or Clearcase to keep track of all modules" (Programming Rules, 8.12).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Every non-trivial project uses a source code control system.
2. The system tracks all of the project's modules.
3. The source names RCS, CVS, and Clearcase as examples (the document dates from 2000).

# Construction / Recognition

## To Apply

1. Place all of a project's modules under a source code control system.

## To Recognize a Violation

1. A non-trivial project's code is not under version control.

# Context & Application

A core documentation rule (section 8).

- **Typical contexts**: every non-trivial project.
- **Common applications**: keeping all modules under version control (today, typically Git).

# Examples

The source names RCS, CVS, and Clearcase as example systems; no code listing is given.

# Relationships

## Related

- **Do not comment out old code - remove it** — the control system is what preserves removed code.
- **File headers, revision history** — version control complements the in-file revision history.

# Common Errors

- **Error**: Developing a non-trivial project without version control.
  **Correction**: Put all modules under a source code control system.

# Common Confusions

- **Confusion**: Reading RCS/CVS/Clearcase as current recommendations.
  **Clarification**: They are the 2000-era examples; the enduring rule is simply "use version control" — today, e.g., Git.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 8.12 "Use a source code control system".

# Verification Notes

- Definition source: Direct adaptation of section 8.12.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: The named tools are dated; the underlying rule is not.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
